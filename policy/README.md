# Telecommunications Policy & Regulation - MCQ Practice

A static MCQ practice site covering the TE 452 / TE 462 telecommunications
regulation course material. It is three 100-question banks (`compiled.json`,
`compiled_2.json` and `compiled_3.json`, 300 questions total) spanning four
themed areas:

| Area | Focus |
| ---- | ----- |
| Market economics & fundamentals | demand, supply, elasticity, equilibrium, price controls, taxes, monopoly & natural monopoly |
| Sector reform & regulatory foundations | liberalization, privatization, regulatory objectives, ITU, WTO Reference Paper |
| Framework for regulation | styles of regulation, instruments, consultation, enforcement, dangers of regulation |
| Licensing, scarce resources & interconnection | licence types, licensing objectives, spectrum & numbers, number portability |

## Source material

Questions are derived from the slide decks in this folder:

- `TE 452 - 1&2.pdf` - Background to regulation; overview of telecom regulation
- `TE 462 - Framework for Regulation.pdf`
- `TE 462 - Licensing Telecommunication Services.pdf`

Questions emphasise conceptual understanding and applied scenarios rather than
rote recall, with plausible distractors built around common misconceptions.

## Features

- A single 100-question bank with live stats tracking
- Auto-shuffled answer options with a stable per-question order
- `Retake Wrong` mode that includes only questions answered incorrectly
- `Back to Main` button to return from retake mode
- Persistent answer storage in the browser
- Auto-scroll to the next question after a correct answer

## How to use

1. Open `index.html` through a local web server or GitHub Pages
   (e.g. `python3 -m http.server` from this folder, then visit the page).
2. Answer questions normally - stats are tracked as you go.
3. Use `Retake Wrong` to practise only the questions you missed.
4. Use `Back to Main` to return to the full bank.

## Rebuilding the question bank

Each bank is generated from its own build script — `build_questions.py`,
`build_questions_2.py` and `build_questions_3.py` respectively:

```bash
python3 build_questions.py
python3 build_questions_2.py
python3 build_questions_3.py
```

Each script holds every question as
`(question_text, correct_answer, [distractor, distractor, distractor])` and
places the correct answer at a balanced, reproducible position so the key
(A/B/C/D) is evenly distributed across the bank (25 / 25 / 25 / 25). Distractors
are written to avoid answer-guessability tells (comparable option lengths, no
absolutist wording). The output JSON matches the format used by the other
practice sites in this repository:

```json
{
  "question_number": 1,
  "question_text": "...",
  "options": ["...", "...", "...", "..."],
  "correct_answer": ["..."]
}
```

## Question & answer PDF

`TE452-TE462-Policy-Regulation-MCQs-with-answers.pdf` is a printable copy of
all 300 questions (Part 1, Part 2 and Part 3 banks) with their options and the
correct answer marked. Regenerate it with:

```bash
python3 make_pdf.py
```

## Notes

- Answers are stored separately for the main bank and the retake flow.
- The page is designed for static hosting and works well on GitHub Pages.
