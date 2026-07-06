# TE 452 / TE 462 — Policy & Regulation Past Paper (MCQ practice)

A practice site built from **`Policy.pdf`**, a set of photographs of a past
examination paper for the Policy & Regulation course. The exam has:

- **Section A** — 60 shuffled multiple-choice questions (this is what the site practises)
- **Section B** — 4 essay questions (listed below for reference; not part of the quiz)

The site now has **two selectable question sets**:

- **Set 1 · Past Paper** — 54 questions transcribed from the exam (`compiled.json`,
  built by `build_questions.py`).
- **Set 2 · Deck-based** — 50 new questions authored in the same style as the past
  paper but written from the lecture decks (`compiled_2.json`, built by
  `build_questions_2.py`), for extra practice.

Open `index.html` (or the GitHub Pages URL) to practise. Options are reshuffled per
question, progress is saved locally, and a "Retake Wrong" button drills the ones you miss.

## Important: the answers here are *not* the circled ones

The exam photos have answers circled/bubbled in, but **many of those circles are wrong**.
Every answer in this bank was re-derived independently from the course lecture decks in
[`../policy/`](../policy) (TE 452 - 1&2, TE 462 - Framework for Regulation, TE 462 -
Licensing Telecommunication Services). Examples where the circle disagrees with the
grounded correct answer include Q2, Q4, Q24, Q26, Q38, Q42, Q45, Q49, Q50, Q58 and Q60.

Every question carries an **insight** (the 💡 lamp icon on the card) explaining *why*
the answer is right — grounded in the decks, quoting them where possible. The insight
opens automatically when you answer wrong, or on demand by clicking the lamp. The same
notes appear under each answer in the PDF.

### Two answers were corrected on a second, careful pass

- **Q11** — the framework deck lists the grounds of appeal verbatim as *law (illegality),
  procedure (misadministration), logic (irrationality)* and the *substance* of the action.
  So "logic" **is** a valid ground; **authority** is the odd one out → the answer is
  **authority** (here the exam's circle was actually right).
- **Q49** — the deck states "industries with zero regulation … are also said to be
  **completely deregulated**", i.e. no external intervention, so a de-regulated industry
  reads as **TRUE** (the exam circled FALSE — worth confirming with your lecturer).

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
python3 build_questions.py     # writes compiled.json  (Set 1, stdlib only)
python3 build_questions_2.py   # writes compiled_2.json (Set 2, stdlib only)
python3 make_pdf.py            # writes the answer-key PDF for both sets (needs PyMuPDF)
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
