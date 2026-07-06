# TE 452 / TE 462 — Policy & Regulation Past Paper (MCQ practice)

A practice site built from **`Policy.pdf`**, a set of photographs of a past
examination paper for the Policy & Regulation course. The exam has:

- **Section A** — 60 shuffled multiple-choice questions (this is what the site practises)
- **Section B** — 4 essay questions (listed below for reference; not part of the quiz)

Open `index.html` (or the GitHub Pages URL) to practise. Options are reshuffled per
question, progress is saved locally, and a "Retake Wrong" button drills the ones you miss.

## Important: the answers here are *not* the circled ones

The exam photos have answers circled/bubbled in, but **many of those circles are wrong**.
Every answer in this bank was re-derived independently from the course lecture decks in
[`../policy/`](../policy) (TE 452 - 1&2, TE 462 - Framework for Regulation, TE 462 -
Licensing Telecommunication Services). Examples where the circle disagrees with the
grounded correct answer include Q2, Q4, Q11, Q24, Q26, Q38, Q42, Q45, Q50, Q52, Q58 and Q60.

## What's covered

**54 of the 60 Section A questions.** The following were **not captured** in the
photographs and are omitted: **Q12, Q20, Q21, Q31, Q32, Q33**. Re-photograph those
pages (top of frame included) and they can be added.

Three questions had their stems cut off at a page top; the stems were reconstructed
from the visible options + course material and are marked **`[stem reconstructed]`** in
the question text: **Q13, Q22, Q34**.

### A few answers worth double-checking

- **Q13** — the stem was cut off; if the original question asked about *policy-making*
  rather than *regulation*, the answer would be "the ministry" instead of
  "the national telecommunication regulator".
- **Q27** ("common sense" regulation) — the phrase isn't verbatim in the decks; answered
  as *ex-post* on the reasoning that it is the judgment/principle-based approach.
- **Q37** (supply curve slope vs elasticity) — answered *A* (flatter/smaller slope = more
  elastic); note that for supply curves elasticity is not determined by slope alone.
- **Q29** — a spelling trap: the official name is *International Telecommunication Union*
  (singular "Telecommunication").

## Rebuilding

```bash
python3 build_questions.py     # writes compiled.json (stdlib only)
python3 make_pdf.py            # writes the answer-key PDF (needs PyMuPDF)
```

After editing content, bump `CACHE_VERSION` in `index.html` so the CDN serves the new JSON.

## Section B (essay questions — reference only)

> Answer Question 1 and any other TWO (2).

1. (a) What is a Bottom of the Pyramid (BoP) market?
   (b) What is the strategy used to serve BoP markets?
   (c) Give a typical example of how mobile communication service providers have
       implemented the BoP strategy.
   (d) Outline the four (4) stages in the consultation process the regulator goes
       through before arriving at a strategic decision.
2. Explain three (3) ways by which universal access policies can be funded.
3. Explain three (3) circumstances that can cause regulation to be hazardous.
4. Differentiate between interconnection and local loop unbundling.
