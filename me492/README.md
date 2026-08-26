# Management & Entrepreneurship Development (ME 492) - MCQ Practice

A static MCQ practice site for the KNUST ME 492 Management and Entrepreneurship
Development course.

Unlike the other banks in this repository, these are **not authored questions**.
They are the **actual past questions**, extracted from the KNUST papers and
matched to their official marking schemes. The bank holds **244 questions** in a
single file (`compiled.json`), grouped into eleven themed sets that follow the
course outline.

| Set | Focus | Count |
| --- | ----- | ----- |
| Entrepreneurship & free enterprise | Cantillon, Smith, Say, Menger, Schumpeter, Drucker; myths; sources of change; small business; success factors; intrapreneurship | 29 |
| Creativity & innovation | creativity vs innovation vs invention; the five stages of the creative process; the innovation process; windows & corridors; brainstorming; the technology spectrum | 17 |
| Business planning & feasibility | who writes the plan; the feasibility plan; the three perspectives; executive summary; cover page; sections of the plan; why plans fail | 25 |
| Venture stages & start-up | pre-start-up, start-up, early growth, later growth; benchmark considerations; operating objectives; measuring progress | 11 |
| Market research & marketing plan | market niche; customer scenario; the 4 Ps; sales forecast; promotion & promotional mix; distribution; IMC; competitive analysis | 29 |
| Intellectual property & law | patents; patent search; Disclosure Document; trademarks; product liability; contracts | 10 |
| Organising & legal forms | sole proprietorship, partnership, corporation; franchising; boards; the entrepreneurial team; job analysis | 21 |
| Financing the new venture | fixed / working / liquid capital; short, intermediate & long term credit; debt vs equity; internal vs external funds; sources of funding | 26 |
| Budgeting & pro forma statements | the three levels of financial planning; the master budget; perpetual budgeting; pro forma income statement, balance sheet and cash flow | 28 |
| Calculations | sales budget & schedule of cash receipts; divisional growth to the fourth quarter; cash budget with borrowing and interest | 30 |
| "Because" statements | the S1 / S2 section, reproduced with the official key | 18 |

## Source material

Questions are extracted from the past papers held in
`~/Documents/y4s2/enterpreneur`:

- `ME492- 2005 MARKING SCHEME.pdf` and `ME492-120 Questions _ solutions.pdf` -
  the 2005 paper with official answers
- `ENTREPRENEUR MCQ 1pdf.pdf` - 2004/2005 Section A, 40 finance questions with
  answers in bold
- `Pasco2.pdf` (pcu/coe/216/07) - the 2007 paper, correct options marked in red
- `PASCO 1.pdf` - a 2008-style paper, 135+ questions, hand-marked
- `ME 492 PRACTICEOBJECTIVES(2)-1.pdf` - 2007/2008, 150 questions
- `IMAGE PASSCO.pdf` - several papers, including a newer 2015/2016 paper
- `ME 492 ONLINE 2020-1.pdf` - the 2020 Moodle exam, answers highlighted
- Lecture slides 1, 2, 3, 8, 9, 10 and `ME 492 2025 NOTES.pdf`

## How the past questions were adapted

Two edits were needed, because the practice page shuffles the option order:

1. **Options that referred to other options by letter** ("a and b only", "all of
   the above") are rewritten as self-contained text. For example, "a, b and c
   only" for the trademark filing question becomes the three requirements spelled
   out in one option.
2. **Where two papers printed different option sets for the same stem**, the
   fuller set is used and the answer follows the printed marking scheme.

The multiple-completion questions keep their original form: the (i) (ii) (iii)
statements sit in the stem and the options read "i only is correct", "i, ii and
iii are correct" and so on. This matches how the 2020 online exam presented them
and it survives shuffling. Each (i) (ii) (iii) statement starts on its own line,
so the stem reads like the printed paper.

Every question carries **five options**, matching the source papers.

## Why the letters do not matter

The same question bank has run since 2005, but the **option letters are shuffled
every year**. "A market segment on which a business can choose to concentrate its
efforts" was `c` in 2005, `c` in 2007, `a` in one 2020 item and `e` in another.
The answer was always **market niche**.

This site shuffles the options for the same reason. Learn the answer text, never
the letter.

## Features

- A single 244-question bank with live stats tracking
- Auto-shuffled answer options with a stable per-question order
- `Retake Wrong` mode that includes only questions answered incorrectly
- `Back to Main` button to return from retake mode
- Persistent answer storage in the browser
- Auto-scroll to the next question after a correct answer
- An explanation on every question. A wrong answer shows it at once. A correct
  answer hides it behind a `Why` toggle. Each one names its source.

## How to use

1. Open `index.html` through a local web server or GitHub Pages
   (e.g. `python3 -m http.server` from this folder, then visit the page).
2. Answer questions normally. Stats are tracked as you go.
3. Use `Retake Wrong` to practise only the questions you missed.
4. Use `Back to Main` to return to the full bank.

## Rebuilding the question bank

The bank is generated from `build_questions.py`:

```bash
python3 build_questions.py
```

`explanations.py` holds the explanations, one entry per question number, as
`(stem_prefix, explanation, source)`. The build checks each `stem_prefix`
against the real stem, so a reordered set fails the build instead of attaching
the wrong explanation. The build also reports any question that has no
explanation yet.

The script holds every question as
`(question_text, correct_answer, [distractor, ...])` and places the correct
answer at a balanced, reproducible position so the key is evenly distributed
across the bank (46 / 46 / 46 / 45 / 45 across the five slots). The output JSON
matches the format used by the other practice sites in this repository:

```json
{
  "question_number": 1,
  "question_text": "...",
  "options": ["...", "...", "...", "...", "..."],
  "correct_answer": ["..."],
  "explanation": "...",
  "source": "..."
}
```

## Question & answer PDF

`ME492-Entrepreneurship-Past-Questions-with-answers.pdf` is a printable copy of
all 244 questions with their options and the correct answer marked. Regenerate
it with:

```bash
python3 make_pdf.py
```

## Study guide

`ME492-Study-Guide.md` is the companion revision guide. It maps the past
questions onto the lecture slides, sets out the two answer codes the paper uses,
works all three calculation types step by step, and lists the items where two
papers disagree with each other.

## How far the answers were verified

Each record carries a `verified` field:

| Value | Questions | What it means |
| --- | --- | --- |
| `checked against the 2005 official marking scheme` | 107 | The stem was matched to `ME492- 2005 MARKING SCHEME.pdf` and the recorded answer compared with the printed key. Section A keys are letters; Section C answers are marked in bold in the PDF. |
| `recomputed from the printed data` | 30 | The calculation items. Every one was worked through from the figures in the stem. |
| `derived from the lecture notes and slides` | 11 | Added 2026. Found in the scans with no printed key. The answer was worked out from `ME 492 2025 NOTES` or a named slide, and the explanation says which. |
| `matched to a marked past paper` | 3 | Added 2026. No printed key, but a circled option on the 2015 script or a selected radio on the Canvas paper shows the answer. |
| `not checked against a printed key` | 93 | These come from papers that are image-only scans with no text layer: `PASCO 1`, `Pasco2`, `IMAGE PASSCO`, `ENTREPRENEUR MCQ 1pdf` and `ME 492 ONLINE 2020`. The page calls these out under the explanation. |

The cross-check found one wrong answer, since corrected: the roles of directors
item. `ME 492 2025 NOTES` lists the roles beyond decision making as mentors,
professional advisers and members of an expanded social network. Disturbance
handling and resource allocation are not among them, and the 2005 key marks
`i and ii only`. The bank had marked all three.

## The 2026 audit: 16 questions added

The five image-only files were read twice: once with OCR for the text, and once
by eye for the pen marks, which OCR cannot see. See
`AUDIT-against-source-papers.md`. The pass found 16 questions in the papers that
the bank did not hold. All 16 are now in.

**From the 2007/2008 multiple-completion section** (`IMAGE PASSCO` p44 to p51):
entrepreneurship myths; product as a catchall term; what a marketing strategy
provides; the innovation development process; the seven conditions for
technological innovation; sources of change for strategic thinkers; the inputs
to the financial section; the inputs to the pro forma balance sheet; the concept
of entrepreneurship; and the origin of the word.

**From a Canvas quiz** (`IMAGE PASSCO` p1 to p33, a 40 question, 40 minute
paper, separate from the Moodle 2020 exam): entrepreneurs as risk takers; the
cocktail party item; resources producing current and future benefits; how long
administration plans run; the statement of estimated income and expenses; and
the formal plan expressed in numerical terms.

Nine of these carried no mark of any kind. Their answers were worked out from
the lecture notes and slides, and each explanation names the slide or the page
it rests on. One item, `Administration plans generally cover a period of`, has
no support in the course materials at all. Its answer comes from the Canvas
paper alone and it is the weakest record in the bank.

It also found three items where the printed sources contradict each other. The
bank keeps its answer and the explanation names both readings: Cantillon's
description, the low tech products `because` item, and the market niche
`because` item.

## Notes on disputed answers

A few items have different answers in different sources. The bank follows the
printed marking schemes. The study guide has the full list with reasons. The main
ones:

- Feasibility plans best prepared by specialists: **both statements false**
- The organisational plan describes: **the organogram of the venture**
- Budgets for expenditure impacting more than one year: **capital budgets**
- Asset-based financing: **debt financing**
- Summarises projected assets, liabilities and equity: **pro forma balance sheet**
- Replacement of products with new and better ones: **creative destruction**

## Known errors in the original papers

These are reproduced faithfully in the study guide, not in the bank:

- The **Kaneapa** item asks for accounts receivable on the fourth quarter pro
  forma balance sheet. The correct figure ($54,450, December credit sales) was
  not printed as an option, and the key marks $78,650.
- The **Dandy Electronics** stem says the company collects 30 percent of accounts
  receivable in the following month. The table shows 100 percent collection.
  Trust the table.
- The **Mercy's Bookshop** stem gives a cash cushion of GH¢9,000 while its table
  uses GH¢7,000.
