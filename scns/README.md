# Satellite Communication & NTN (TE 456) - MCQ Practice

A static MCQ practice site for the KNUST TE 456 *Satellite Communication and
Navigation Systems* course. The bank holds **240 questions** in a single file
(`compiled.json`), built from the **24 student group presentations**, ten
questions per deck.

| Group | Topic |
| ----- | ----- |
| 1 | Timing advance & frequency offset compensation in LEO NTN |
| 2 | UAV-enhanced 3D beamforming for rural 5G NTN |
| 3 | Machine learning for RACH optimization |
| 4 | GPS signal integration & augmentation in 5G-NTN |
| 5 | HAPS-based disaster recovery with 5G core integration |
| 6 | Multi-connectivity & session continuity across TN-NTN |
| 7 | Spectrum sharing & interference management, NTN vs TN |
| 8 | Mobility management & handover optimization |
| 9 | ISAC-enabled NTN for 6G |
| 10 | AI-native Open RAN for NTN |
| 11 | Federated learning for CSI feedback & beam management |
| 12 | AI-driven dynamic beam control for LEO 5G-NTN |
| 13 | GPS & Galileo |
| 14 | Post-quantum cryptography for NTN |
| 15 | Doppler shift estimation in 5G NR NTN |
| 16 | Network slicing in NTN |
| 17 | eRACH, a learned random access protocol |
| 18 | RIS-enhanced NTN for coverage & capacity in 6G |
| 21 | Uplink time synchronization without GNSS |
| 22 | Deep reinforcement learning for SAGIN resource allocation |
| 23 | HARQ mechanisms & limitations in NTN |
| 24 | Network digital twinning for 3D constellations |
| - | AI-driven predictive handover for high-mobility LEO |
| - | AI-assisted trajectory optimization of UAV/HAPS platforms |

The last two decks carry no group number on their title slide. Groups 19 and 20
are absent from the source folder.

## Source material

The questions come from the 24 student group presentations in
`~/Documents/y4s2/scns/TE 456 PRESENTATIONS`. The `.pptx` files are not copied
into this folder; they total about 290 MB, which does not belong in the repo.

Those decks are **image heavy**. Many slides carry a title and nothing else, and
the content sits inside a diagram, a table or a figure. Extracting the slide text
alone gives headings and no substance: one 11-slide deck yields 499 characters of
text in total.

Each deck was therefore converted to PDF with LibreOffice, rendered page by page
with PyMuPDF, and read as images. Every question rests on what the slides
actually show, so a figure quoted here (650 us of differential delay, a 684 us
cyclic prefix, +/-48 kHz of S-band Doppler, 28 dB of HAPS link-budget advantage)
came off a rendered slide rather than off a text layer.

Questions emphasise conceptual understanding and applied scenarios rather than
rote recall, with plausible distractors built around common misconceptions.

The three lecturer PDFs in this folder (`TE456-NTN-What&Why.pdf`,
`TE456-NTN-Overview-1.pdf`, `TE456-Elements-SatCom5GSystems-2026-Complete.pdf`)
are kept as reference material. No questions are currently built from them.

## Earlier banks, removed

Four banks preceded this one and were removed in August 2026, along with their
build scripts:

| Bank | Questions | Covered |
| ---- | --------- | ------- |
| Parts 1 & 2 | 200 | 5G NR-NTN architecture & challenges, from `TE456-5GNR-NTN-2026-complete.pdf` |
| Part 3 | 100 | NTN fundamentals, orbits & beams, SatCom payload & 5G NR systems, from the three lecturer PDFs |

Recover any of them from git history if they are ever wanted:

```bash
git show 90e4a19:scns/compiled.json   > old-part1.json
git show 90e4a19:scns/compiled_2.json > old-part2.json
git show 90e4a19:scns/compiled_3.json > old-part3.json
```

## Features

- A single 240-question bank with live stats tracking
- Auto-shuffled answer options with a stable per-question order
- `Retake Wrong` mode that includes only questions answered incorrectly
- `Back to Main` button to return from retake mode
- Persistent answer storage in the browser
- Auto-scroll to the next question after a correct answer
- **An explanation on every question.** A wrong answer shows it at once. A
  correct answer hides it behind a `Why` toggle. Each one names the deck and the
  slides it rests on.

## How to use

1. Open `index.html` through a local web server or GitHub Pages
   (e.g. `python3 -m http.server` from this folder, then visit the page).
2. Answer questions normally - stats are tracked as you go.
3. Use `Retake Wrong` to practise only the questions you missed.
4. Use `Back to Main` to return to the full bank.

## Rebuilding the question bank

```bash
python3 build_questions.py
```

The question data lives in three modules, eight decks each, so no single file
becomes unmanageable:

| Module | Decks |
| ------ | ----- |
| `deck_questions_a.py` | Groups 1 to 8 |
| `deck_questions_b.py` | Groups 9 to 16 |
| `deck_questions_c.py` | Groups 17 to 24 |

Each deck is a dict with a `topic`, a `source` naming the deck and slides, and
ten questions held as
`(stem, correct_answer, [distractor, distractor, distractor], explanation)`.

The build fails rather than producing a bad bank. It rejects a deck that does not
hold exactly ten questions, a question with the wrong number of distractors, and
a question that repeats an option. It reports any question missing an
explanation.

The correct answer is placed at slot `(deck_index + question_index) % 4`, so the
key walks forward by deck **and** by position. Neither the deck boundary nor the
question number lines up with one letter, and the spread comes out at exactly
**60 / 60 / 60 / 60**.

Output format, which extends the shape used by the other banks in this repository
with the two fields the page reads for the explanation panel:

```json
{
  "question_number": 1,
  "question_text": "...",
  "options": ["...", "...", "...", "..."],
  "correct_answer": ["..."],
  "explanation": "...",
  "topic": "Timing advance and frequency offset compensation in LEO NTN",
  "source": "Group 1 deck, slides 2 to 9"
}
```

## Question & answer PDF

`TE456-Presentation-Decks-MCQs-with-answers.pdf` is a printable copy of all 240
questions, grouped by deck, with the correct option ticked and the explanation
printed beneath each answer. 43 pages. Regenerate it with:

```bash
python3 make_pdf.py
```

## Study guide

`TE456-Presentation-Decks-Study-Guide.md` is the companion revision guide. It
writes out the content of all 24 decks as continuous text, in the same order the
bank uses, including what the diagrams show. It opens with six cross-cutting
ideas that recur across the decks and closes with a table of the figures worth
memorising.

Read the deck section, then answer that deck's ten questions. Every question
names its deck in `topic` and its slides in `source`, so a wrong answer points
back to the right section of the guide.

## How this bank was checked

- The build asserts the shape of every record and the even spread of the key.
- `compiled.json` was validated: 240 records, 24 topics, four options each, the
  correct answer present in the options, an explanation and a source on every
  one.
- The page was rendered in jsdom against a local server and driven end to end:
  the bank loads, all 240 questions render, a wrong answer shows the explanation
  and the source line inline, and a correct answer puts it behind the `Why`
  toggle.
- The PDF was regenerated and its text layer spot-checked on the first and last
  pages.
