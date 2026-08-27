# -*- coding: utf-8 -*-
"""Build site-extracted-48.json from site-raw-228.json.

Source: https://samplequestions.vercel.app/quiz, pulled 27 August 2026.
Of its 228 ME 492 questions, 133 already sit in compiled.json. This script keeps
the 48 that are genuinely new and defensible:

  19 non-table questions (7 of them on the economists, the thinnest block in the
     existing bank)
  29 table questions from four scenarios: two new cash budgets and two new sales
     budgets.

Three combination answers are corrected against the lecturer's notes, because
the site marks them wrong. One further item is dropped as unsettled. Each
correction is recorded in CORRECTIONS below and named in the explanation.

Table stems are rewritten as self-contained prose, the same convention the
existing calculation questions in compiled.json already use.
"""
import io
import json
import random
import re

import calc_tables as T

C = "GH¢"          # the cedi form used throughout compiled.json
CEDI_ALT = "₵"      # the site mixes this in; normalise it away

RAW = "site-raw-228.json"
OUT = "site-extracted-48.json"

VERIFIED_CALC = "recomputed from the printed data"
VERIFIED_NOTES = "re-derived from the lecture notes and slides"
VERIFIED_SITE = "taken from samplequestions.vercel.app, checked against the notes"

# --------------------------------------------------------------------------
# 1. The 19 non-table questions, keyed by a unique prefix of the site's stem.
#    override = the answer the notes give, where it differs from the site.
# --------------------------------------------------------------------------
CORRECTIONS = {}

NON_TABLE = [
    ("A feasibility plan is a written document\ni. comprising all",
     None,
     "Guide 6.2, what a feasibility plan is",
     "Statements (ii) and (iii) are on the list: the objective is to determine whether the "
     "venture can be expected to succeed, and the promoters prepare it. Statement (i) fails "
     "because a feasibility plan is deliberately not the full business plan. It carries only "
     "the planning needed to prove feasibility, without overwhelming the entrepreneur."),

    ("A feasibility plan (business plan for a new venture) should be written by",
     None,
     "Guide 6.1, who writes the plan",
     "The entrepreneur, alone or in consultation with other sources. Statement (iii) hands the "
     "job to a business consultant, and that is the standard wrong option. Specialists advise. "
     "They do not take the plan over."),

    ("French economist Jean Baptiste Say, in his 1803",
     "if ii and iii only are correct",
     "Guide 4.1, the economists",
     "CORRECTED. The site marks all three. Statement (i) says Say described skills for "
     "MANAGING EXISTING enterprises. The notes say CREATING NEW economic enterprises, so (i) is "
     "false on one word. Statements (ii) and (iii) match the notes exactly. This is trap 17: "
     "one wrong word makes a whole statement false."),

    ("In the creative process, a person is said to be in the preparation stage",
     None,
     "Guide 5.2, the five stages",
     "Only (iii). Preparation is the conscious search for knowledge to bring the idea to life. "
     "The sudden flash in (i) is illumination, and the test to prove value in (ii) is "
     "verification."),

    ("Entrepreneurship is one of the four mainstream economic factors",
     None,
     "Guide 4.1; slides on the factors of production",
     "The four factors are land, labour, capital and entrepreneurship, so (ii) and (iii) "
     "together name them. Statement (i) swaps in raw materials and overhead costs, which are "
     "cost categories, not factors of production."),

    ("The word entrepreneur is derived from 17th-century",
     None,
     "Slides 1.13 to 1.24, history of entrepreneurship",
     "All three. Undertakers who undertook the risk, contractors who bore profit or loss, and "
     "the soldiers of fortune, adventurers, builders and merchants of the early slides. Note "
     "the contrast with the other origin item, where the added clause about business students "
     "makes a statement false."),

    ("In the Pre-start-Up Stage",
     None,
     "Guide 7.2, pre-start-up activities",
     "All three. The business concept is defined, the product-market study is done, and "
     "pre-start-up implementation follows. Pre-start-up is the assembly of resources before "
     "the doors open."),

    ("The entrepreneur is most knowledgeable person about the proposed business",
     None,
     "Guide 6.1, who writes the plan",
     "The entrepreneur keeps the responsibility. Help is available from a banker, a professional "
     "or a plan writer, but the responsibility for planning the venture does not transfer. The "
     "entrepreneur has the vision and the motivation."),

    ("Adam Smith spoke of the \"enterpriser\"",
     None,
     "Guide 4.1, the economists",
     "All three match the notes on Smith: he undertook the formation of an organisation for "
     "commercial purposes, had unusual foresight to recognise potential demand, and reacted to "
     "economic change by transforming demand into supply."),

    ("Elements in the innovative process are",
     None,
     "Guide 5.3, the innovation process",
     "Statements (i) and (iii). Organising resources with analytical planning, then "
     "implementation and commercial application. Statement (ii) lists idea germination, "
     "preparation and verification, which belong to the CREATIVE process. That is trap 4."),

    ("Limited partners enjoy certain advantages over general partners that include\n"
     "i. Flexibility and simplicity",
     None,
     "Guide 10.5, partnership",
     "Statements (ii) and (iii). Exemption from management responsibility, and an investment "
     "that can be sold, assigned or willed. Read (i) carefully: the notes list profits and "
     "losses passing through to all partners, not flexibility and simplicity."),

    ("In Drucker's view, entrepreneurship occurs when",
     None,
     "Guide 4.1, the economists",
     "Only (ii). Drucker said resources are redirected to progressive opportunities. "
     "Administrative efficiency in (i) is the opposite of his point, and organising industrial "
     "activity to match demand with supply in (iii) belongs to the earlier economists."),

    ("French economist Jean Baptiste Say\ni. combined",
     "if i, ii and iii are correct",
     "Guide 4.1, the economists",
     "CORRECTED. The site marks (iii) only. All three statements are in the notes on Say: he "
     "combined Cantillon's economic risk taker with Smith's industrial manager, he described "
     "arts and skills for creating new enterprises plus exceptional insight into society's "
     "needs, and he said the entrepreneur both influences society and is influenced by it."),

    ("Carl Menger described entrepreneurship as",
     None,
     "Guide 4.1; trap list 6",
     "Only (iii): converting resources into goods and services of value to consumers. Creative "
     "destruction and entrepreneurs as innovators belong to SCHUMPETER. This is the classic "
     "Menger trap and it appears in almost every paper."),

    ("Jean Baptiste Say believed that entrepreneurs",
     None,
     "Guide 4.1, the economists",
     "Only (iii): exceptional insight into society's needs, fulfilled through taking risks. "
     "Statement (ii), buying at known prices and reselling at unknown prices, is CANTILLON. "
     "Watch this pair: the same clause is offered under both names in different questions."),

    ("A partnership, as a legal form of business has certain disadvantages",
     None,
     "Guide 10.5, partnership",
     "Statements (ii) and (iii). The business ends on the death or withdrawal of any partner, "
     "and liability is unlimited, joint and several. Statement (i) is false: a partnership is a "
     "simple form to administer, which is one of its attractions."),

    ("In Drucker's view, the entrepreneur",
     None,
     "Guide 4.1; trap list 6",
     "Only (i): resources are used not merely to solve problems but to take advantage of "
     "opportunities. Statement (ii) misquotes Schumpeter's creative destruction as creative "
     "disruption, and (iii) belongs to the earlier economists."),

    ("Richard Cantillon, a French Economists",
     "if i and iii only are correct",
     "Guide 4.1; Guide 16, conflicts",
     "CORRECTED. The site marks (i) and (ii). The notes give Cantillon two things: conscious "
     "decisions about resource allocation, and seeking higher yields for money and materials. "
     "That is (i) and (iii). Statement (ii), exceptional insight into society's needs, is SAY, "
     "and the site's own Say question marks it as Say. The site appears to have carried a "
     "letter across from a paper whose options ran in a different order. Answer by text."),

    ("**S1:** A good way to fail quickly in a new business",
     None,
     "Guide 6.15, planning is never finished",
     "Both statements are true and the second explains the first. A venture with no clear "
     "vision has nothing to plan against. The same pair appears elsewhere with the second "
     "statement worded as a lack of understanding of marketing issues. The answer does not "
     "change."),
]

# Dropped on purpose. Recorded so the decision is not silently lost.
DROPPED = [
    ("The Entrepreneurial Team segment of a business plan should",
     "The site marks (iii) only. Nothing in the notes or the slides settles whether the brief "
     "resumes in (ii) belong in the team segment or in the appendix, and Guide 6.11 puts "
     "resumes in the appendix. The site under-picks statements on 10 of the 32 combination "
     "items we can compare, so its lone (iii) is not trustworthy here. Left out rather than "
     "shipped with an answer that cannot be defended."),
]

# --------------------------------------------------------------------------
# 2. The four table scenarios. Each stem is rewritten to stand on its own.
# --------------------------------------------------------------------------
PREAMBLE = {
    "Table-0014": T.LOVY,
    "Table-0030": T.BIRDY_CLOTHING,
    "Table-0031": T.SWEETIE,
    "Table-0027": T.MERCY,
}

TABLE_SOURCE = {
    "Table-0014": "Guide 13.1, schedule of cash receipts",
    "Table-0030": "Guide 13.1, schedule of cash receipts",
    "Table-0031": "Guide 13.3, the cash budget with borrowing and interest",
    "Table-0027": "Guide 13.3, the cash budget with borrowing and interest",
}

# explanation keyed by (table reference, a distinctive fragment of the stem)
TABLE_EXPL = {
    ("Table-0014", "accounts receivable for October"):
        "October collects what was owed on 1 October, so the answer is the given opening balance, "
        + C + "115,385. Note a fault in the printed table: October collections should be "
        "30,000 + 115,385 = " + C + "145,385, but the paper prints " + C + "143,385. The November "
        "and December collection lines are both consistent, so only the October line is wrong.",
    ("Table-0014", "accounts receivable for November"):
        "November collects October's sales on account, " + C + "150,000. Check it against the "
        "collections line: 39,000 + 150,000 = " + C + "189,000, which is what the table prints.",
    ("Table-0014", "accounts receivable for December"):
        "December collects November's sales on account, " + C + "195,000. Check: 50,700 + 195,000 = "
        + C + "245,700, exactly the printed collections figure.",
    ("Table-0014", "cash sales for October"):
        "Read the cash sales line straight off the table: " + C + "30,000. This is a free mark.",
    ("Table-0014", "cash sales for November"):
        "Read the cash sales line: " + C + "39,000. The distractors here are lifted from a "
        "different company's table, which is a good reason to work from the figures you are given "
        "and not from what looks familiar.",
    ("Table-0014", "cash sales for December"):
        "Read the cash sales line: " + C + "50,700.",
    ("Table-0014", "fourth quarter pro forma balance sheet"):
        "The correct figure is December's CREDIT sales, " + C + "253,500. It is not offered. Every "
        "printed option comes from the Topsy Turvy table, so none of the above is the right "
        "response here. This repeats the known Kaneapa fault: when the correct figure is missing, "
        "check whether the option set belongs to another question before you settle.",
    ("Table-0014", "fourth quarter pro forma income statement"):
        "Add the three total budgeted sales figures. December's total is 50,700 + 253,500 = "
        + C + "304,200, although the table prints " + C + "302,200. Using the correct total: "
        "180,000 + 234,000 + 304,200 = " + C + "718,200, which is the marked answer. Trust the "
        "cash and credit rows over the total row when they disagree.",

    ("Table-0030", "accounts receivable for November"):
        "November collects October's sales on account, " + C + "3,200,000. Check: "
        "6,000,000 + 3,200,000 = " + C + "9,200,000, the printed collections figure.",
    ("Table-0030", "accounts receivable for December"):
        "December collects November's sales on account, " + C + "4,000,000. Check: "
        "7,500,000 + 4,000,000 = " + C + "11,500,000.",
    ("Table-0030", "cash sales for October"):
        "Read the cash sales line: " + C + "4,800,000. October collections equal the cash sales "
        "alone, because there were no receivables on 1 October.",
    ("Table-0030", "cash sales for November"):
        "Read the cash sales line: " + C + "6,000,000.",
    ("Table-0030", "cash sales for December"):
        "Read the cash sales line: " + C + "7,500,000.",
    ("Table-0030", "fourth quarter pro forma balance sheet"):
        "December's CREDIT sales only: " + C + "5,000,000. It is not December total sales "
        "(" + C + "12,500,000) and it is not the December collections (" + C + "11,500,000). This "
        "is the money still uncollected at 31 December.",
    ("Table-0030", "fourth quarter pro forma income statement"):
        "Add the three total budgeted sales figures: 8,000,000 + 10,000,000 + 12,500,000 = "
        + C + "30,500,000. Use total sales, not collections.",
    ("Table-0030", "expected increase in sales per month"):
        "Divide one month's total sales by the month before: 10,000,000 / 8,000,000 = 1.25, so "
        "25 percent. Check it on the next pair: 12,500,000 / 10,000,000 = 1.25 as well.",

    ("Table-0031", "total cash available for August"):
        "Total cash available = beginning cash balance + cash receipts. July ends at "
        + C + "48,000, so August is 48,000 + 3,600,000 = " + C + "3,648,000. Work July first: "
        "avail 2,500,000, disbursements 3,100,000, shortage 600,000, borrowing 600,000 + 120,000 "
        "= 720,000, interest 72,000, ending 48,000.",
    ("Table-0031", "total cash available for September"):
        "August ends at " + C + "44,800, so September is 44,800 + 4,200,000 = " + C + "4,244,800. "
        "The August ending balance is 3,648,000 - 3,560,000 + 32,000 - 75,200 = " + C + "44,800.",
    ("Table-0031", "cash surplus for August"):
        "Total disbursements are 2,000,000 + 1,560,000 = " + C + "3,560,000. Disbursements minus "
        "available: 3,560,000 - 3,648,000 = -88,000, a surplus of " + C + "88,000.",
    ("Table-0031", "cash surplus for September"):
        "Total disbursements are 2,200,000 + 1,800,000 = " + C + "4,000,000. "
        "4,000,000 - 4,244,800 = -244,800, a surplus of " + C + "244,800.",
    ("Table-0031", "borrowed for August"):
        "READ THIS ONE CAREFULLY. August shows a surplus of " + C + "88,000, but the cushion is "
        + C + "120,000. The surplus is SMALLER than the cushion, so the company cannot repay. It "
        "must BORROW the difference: 120,000 - 88,000 = " + C + "32,000. The usual rule, "
        "repayment = surplus - cushion, gives a negative number, and a negative repayment is a "
        "borrowing.",
    ("Table-0031", "repaid for September"):
        "September's surplus of " + C + "244,800 is larger than the " + C + "120,000 cushion, so "
        "the normal rule applies: repayment = surplus - cushion = 244,800 - 120,000 = "
        + C + "124,800.",
    ("Table-0031", "ending cash balance for the month of September"):
        "Ending = available - disbursements + borrowing - repayment - interest. The loan balance "
        "after September's repayment is 752,000 - 124,800 = " + C + "627,200, so interest is "
        + C + "62,720. Then 4,244,800 - 4,000,000 - 124,800 - 62,720 = " + C + "57,280.",
    ("Table-0031", "interest expense for the third quarter"):
        "Interest is charged on the CUMULATIVE loan balance each month. July: 720,000 at 10 "
        "percent = 72,000. August: the balance rises to 752,000 after the extra borrowing, so "
        "75,200. September: it falls to 627,200, so 62,720. Total = " + C + "209,920.",

    ("Table-0027", "borrowed for August"):
        "August has a surplus of " + C + "5,865 (disbursements 94,395 against available 100,260), "
        "which is smaller than the " + C + "7,000 cushion. So the company BORROWS the shortfall: "
        "7,000 - 5,865 = " + C + "1,135. Same rule as the Sweetie-Nitie August item.",
    ("Table-0027", "repaid for September"):
        "September's surplus is 110,292 disbursed against 119,011 available, so " + C + "8,719. "
        "That is larger than the cushion, so repayment = 8,719 - 7,000 = " + C + "1,719.",
    ("Table-0027", "interest expense for the third quarter"):
        "Charge 4.35 percent on the running loan balance. July: 17,013 gives 740. August: the "
        "balance rises to 18,148, giving 789. September: it falls to 16,429, giving 715. "
        "Total = " + C + "2,244.",
    ("Table-0027", "net cash flows from financing activities"):
        "Financing = everything borrowed minus everything repaid: 17,013 + 1,135 - 1,719 = "
        + C + "16,429. It equals the loan balance still outstanding at the end of September, "
        "which is the quickest way to check it.",
    ("Table-0027", "net cash flows from operating activities"):
        "Operating = cash receipts - cash disbursements - interest paid. Receipts are "
        "80,000 + 94,000 + 112,800 = 286,800. Disbursements are 99,013 + 94,395 + 110,292 = "
        "303,700. Interest is 2,244. So 286,800 - 303,700 - 2,244 = " + C + "(19,144). Leaving "
        "the interest out gives " + C + "(16,900), which is the printed trap.",
}


def clean(s):
    """Normalise the site's two cedi signs and its stray markdown."""
    s = s.replace("GH" + CEDI_ALT, C).replace(CEDI_ALT, C)
    s = s.replace("GH¢ ", C)
    s = s.replace("**", "")
    return s.strip()


def main():
    site = json.load(io.open(RAW, encoding="utf-8"))
    out = []

    # ---- non-table -------------------------------------------------------
    for prefix, override, source, expl in NON_TABLE:
        hit = [q for q in site if q["text"].startswith(prefix)]
        if len(hit) != 1:
            raise SystemExit("prefix matched %d questions: %r" % (len(hit), prefix))
        q = hit[0]
        opts = [clean(o["text"]) for o in q["options"]]
        ans = clean(override) if override else clean(q["correct_answer"])
        if ans not in opts:
            raise SystemExit("answer %r not among options for %r" % (ans, prefix))
        if override:
            CORRECTIONS[prefix] = (clean(q["correct_answer"]), ans)
        out.append({
            "question_text": clean(q["text"]),
            "options": opts,
            "correct_answer": [ans],
            "explanation": expl,
            "source": source,
            "verified": VERIFIED_NOTES if override else VERIFIED_SITE,
        })

    # ---- table -----------------------------------------------------------
    for ref in ("Table-0014", "Table-0030", "Table-0031", "Table-0027"):
        qs = [q for q in site
              if (q.get("stimuli") or [{}])[0].get("reference") == ref]
        if not qs:
            raise SystemExit("no questions for %s" % ref)
        for q in qs:
            stem = clean(q["text"]).rstrip(".")
            expl = None
            for (r, frag), text in TABLE_EXPL.items():
                if r == ref and frag.lower() in stem.lower():
                    expl = text
                    break
            if expl is None:
                raise SystemExit("no explanation for %s / %r" % (ref, stem))
            out.append({
                "question_text": T.stem(PREAMBLE[ref], stem + "."),
                "options": [clean(o["text"]) for o in q["options"]],
                "correct_answer": [clean(q["correct_answer"])],
                "explanation": expl,
                "source": TABLE_SOURCE[ref],
                "verified": VERIFIED_CALC,
            })

    # ---- finish ----------------------------------------------------------
    for q in out:
        if len(q["options"]) != 5:
            raise SystemExit("not 5 options: %r" % q["question_text"][:60])
        if len(set(q["options"])) != 5:
            raise SystemExit("duplicate option: %r" % q["question_text"][:60])
        if q["correct_answer"][0] not in q["options"]:
            raise SystemExit("answer missing: %r" % q["question_text"][:60])

    # Spread the correct option evenly, as compiled.json and the AI set do.
    order = [i % 5 for i in range(len(out))]
    random.Random(492).shuffle(order)
    for i, q in enumerate(out):
        opts = [o for o in q["options"] if o != q["correct_answer"][0]]
        opts.insert(order[i], q["correct_answer"][0])
        q["options"] = opts

    for i, q in enumerate(out):
        q["question_number"] = 345 + i
    keys = ["question_number", "question_text", "options", "correct_answer",
            "explanation", "source", "verified"]
    out = [{k: q[k] for k in keys} for q in out]

    json.dump(out, io.open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %s with %d questions (%d to %d)"
          % (OUT, len(out), out[0]["question_number"], out[-1]["question_number"]))
    print("corrected against the notes:")
    for prefix, (was, now) in CORRECTIONS.items():
        print("  %-45s %r -> %r" % (prefix[:45], was, now))
    print("dropped as unsettled: %d" % len(DROPPED))


if __name__ == "__main__":
    main()
