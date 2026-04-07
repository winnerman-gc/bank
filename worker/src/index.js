function corsHeaders(origin, allowedOrigin) {
  const useOrigin = allowedOrigin || origin || "*";
  return {
    "Access-Control-Allow-Origin": useOrigin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json",
  };
}

function json(body, status, headers) {
  return new Response(JSON.stringify(body), { status, headers });
}

function normalizeBaseUrl(url) {
  return (url || "").replace(/\/$/, "");
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin");
    const headers = corsHeaders(origin, env.ALLOWED_ORIGIN);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers });
    }

    const { pathname } = new URL(request.url);

    if (request.method !== "POST") {
      return json({ error: "Method not allowed" }, 405, headers);
    }

    if (pathname === "/ai-explain") {
      return handleAiExplain(request, env, headers);
    }

    if (pathname === "/report-miss") {
      return handleReportMiss(request, env, headers);
    }

    if (pathname === "/migrate-kv-to-upstash") {
      return handleMigrateKvToUpstash(request, env, headers);
    }

    return json({ error: "Not found" }, 404, headers);
  },
};

async function handleAiExplain(request, env, headers) {
  if (!env.DEEPSEEK_API_KEY) {
    return json({ error: "DeepSeek API key not configured" }, 500, headers);
  }

  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: "Invalid JSON body" }, 400, headers);
  }

  const question = String(payload.question || "").trim();
  const selected = String(payload.selected || "").trim();
  const correct = String(payload.correct || "").trim();

  if (!question || !correct) {
    return json({ error: "Missing required fields" }, 400, headers);
  }

  const deepseekReq = {
    model: "deepseek-chat",
    messages: [
      {
        role: "system",
        content:
          "You are a Cryptography and Network Security tutor. Base explanations on the principles and terminology of William Stallings, Cryptography and Network Security: Principles and Practice, Eighth Edition. Give precise, technical, study-guide style explanations: define the core concept, state why the correct option is correct, and briefly state why the selected or other options are incorrect. Use plain text only, no markdown, no bullets, no headings, no conversational filler. Keep it concise but exam-focused and accurate.",
      },
      {
        role: "user",
        content: `Question: ${question}\nSelected Answer: ${selected}\nCorrect Answer: ${correct}`,
      },
    ],
    stream: false,
  };

  const resp = await fetch("https://api.deepseek.com/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${env.DEEPSEEK_API_KEY}`,
    },
    body: JSON.stringify(deepseekReq),
  });

  if (!resp.ok) {
    const text = await resp.text();
    return json({ error: `DeepSeek error ${resp.status}: ${text}` }, 502, headers);
  }

  const data = await resp.json();
  const explanation =
    data?.choices?.[0]?.message?.content?.trim() || "No explanation available.";

  return json({ explanation }, 200, headers);
}

async function handleReportMiss(request, env, headers) {
  if (!env.UPSTASH_REDIS_REST_URL || !env.UPSTASH_REDIS_REST_TOKEN) {
    return json({ error: "Upstash credentials not configured" }, 500, headers);
  }

  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: "Invalid JSON body" }, 400, headers);
  }

  const qNum = Number(payload.q_num);
  if (!Number.isInteger(qNum) || qNum <= 0) {
    return json({ error: "q_num must be a positive integer" }, 400, headers);
  }

  const base = normalizeBaseUrl(env.UPSTASH_REDIS_REST_URL);
  const scoreKey = `wrong:q:${qNum}`;
  const leaderboardKey = "wrong:leaderboard";

  const authHeaders = {
    Authorization: `Bearer ${env.UPSTASH_REDIS_REST_TOKEN}`,
    "Content-Type": "application/json",
  };

  const incrResp = await fetch(`${base}/incr/${encodeURIComponent(scoreKey)}`, {
    method: "POST",
    headers: authHeaders,
  });

  if (!incrResp.ok) {
    const text = await incrResp.text();
    return json({ error: `Upstash INCR failed: ${text}` }, 502, headers);
  }

  const zResp = await fetch(`${base}/zincrby/${encodeURIComponent(leaderboardKey)}/1/${qNum}`, {
    method: "POST",
    headers: authHeaders,
  });

  if (!zResp.ok) {
    const text = await zResp.text();
    return json({ error: `Upstash ZINCRBY failed: ${text}` }, 502, headers);
  }

  return json({ ok: true }, 200, headers);
}

async function handleMigrateKvToUpstash(request, env, headers) {
  if (!env.MIGRATION_TOKEN) {
    return json({ error: "Migration token not configured" }, 500, headers);
  }
  if (!env.STATS) {
    return json({ error: "KV binding STATS is not configured" }, 500, headers);
  }
  if (!env.UPSTASH_REDIS_REST_URL || !env.UPSTASH_REDIS_REST_TOKEN) {
    return json({ error: "Upstash credentials not configured" }, 500, headers);
  }

  const providedToken = request.headers.get("x-migration-token") || "";
  if (providedToken !== env.MIGRATION_TOKEN) {
    return json({ error: "Unauthorized" }, 401, headers);
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch {
    payload = {};
  }

  const cursor = typeof payload.cursor === "string" ? payload.cursor : undefined;
  const requestedBatch = Number(payload.batchSize);
  const batchSize =
    Number.isInteger(requestedBatch) && requestedBatch > 0 && requestedBatch <= 1000
      ? requestedBatch
      : 500;

  const base = normalizeBaseUrl(env.UPSTASH_REDIS_REST_URL);
  const authHeaders = {
    Authorization: `Bearer ${env.UPSTASH_REDIS_REST_TOKEN}`,
    "Content-Type": "application/json",
  };

  const list = await env.STATS.list({ prefix: "", limit: batchSize, cursor });

  let scanned = 0;
  let migrated = 0;
  const errors = [];

  for (const keyMeta of list.keys) {
    scanned++;
    const key = keyMeta.name;
    const match = key.match(/^(?:q:|wrong:q:)?(\d+)$/);
    if (!match) {
      continue;
    }

    const qNum = Number(match[1]);
    if (!Number.isInteger(qNum) || qNum <= 0) {
      continue;
    }

    const value = await env.STATS.get(key);
    const count = Number(value);
    if (!Number.isFinite(count) || count <= 0) {
      continue;
    }

    const scoreKey = `wrong:q:${qNum}`;
    const leaderboardKey = "wrong:leaderboard";

    const incrResp = await fetch(`${base}/incrby/${encodeURIComponent(scoreKey)}/${Math.trunc(count)}`, {
      method: "POST",
      headers: authHeaders,
    });

    if (!incrResp.ok) {
      const text = await incrResp.text();
      errors.push({ key, step: "incrby", error: text });
      continue;
    }

    const zResp = await fetch(
      `${base}/zincrby/${encodeURIComponent(leaderboardKey)}/${Math.trunc(count)}/${qNum}`,
      {
        method: "POST",
        headers: authHeaders,
      }
    );

    if (!zResp.ok) {
      const text = await zResp.text();
      errors.push({ key, step: "zincrby", error: text });
      continue;
    }

    migrated++;
  }

  return json(
    {
      ok: true,
      scanned,
      migrated,
      nextCursor: list.list_complete ? null : list.cursor,
      listComplete: list.list_complete,
      errors,
    },
    200,
    headers
  );
}
