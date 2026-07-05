# Digital Signal Processing (TE 454) - MCQ Practice

A static MCQ practice site for the TE 454 Digital Signal Processing course.
The exam is theory-based, so this bank is built for **studying the theory**: the
124 questions target conceptual understanding of the ideas in the lecture slides
rather than numerical calculation. It is a single combined bank (`compiled.json`)
organised into four themed areas that follow the three lecture decks:

| Area | Focus |
| ---- | ----- |
| DSP fundamentals | analog vs digital signals, sampling & quantization, why digital (programmability, precision, stability, error-correcting codes, compression), why analog is still needed, applications |
| Continuous-time signals & LTI systems | causal signals, unit step / sinusoid / exponential / gate, the unit impulse and its properties, impulse representation, linearity & time-invariance, impulse response, convolution |
| Fourier / frequency-domain analysis | Fourier series & spectra, the Fourier transform, transforms of typical signals, transform properties (linearity, time & frequency shift, Parseval, convolution theorem), system/transfer function, frequency sweep |
| Discrete-time signals & systems | sequences, sampling & the Nyquist theorem, sequence operations, interpolation/decimation, energy/power & bounded sequences, basic sequences, LTI DT systems, the convolution sum, FIR vs IIR, recursive vs non-recursive |

## Source material

Questions are derived from the lecture slide decks in this folder:

- `TE 454 Lecture 1.pdf` - Introduction to DSP; analog vs digital; applications
- `TE 454 Lecture 2.pdf` - Continuous-time signals & systems; impulse; LTI; Fourier
- `TE 454 Lecture 3.pdf` - Discrete-time signals & systems; convolution; FIR/IIR

Questions emphasise conceptual understanding and applied reasoning rather than
rote recall, with plausible distractors built around common misconceptions.

## Features

- A single 124-question bank with live stats tracking
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

The bank is generated from `build_questions.py`:

```bash
python3 build_questions.py
```

The script holds every question as
`(question_text, correct_answer, [distractor, distractor, distractor])` and
places the correct answer at a balanced, reproducible position so the key
(A/B/C/D) is evenly distributed across the bank (31 / 31 / 31 / 31). Distractors
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

`TE454-Digital-Signal-Processing-MCQs-with-answers.pdf` is a printable copy of
all 124 questions with their options and the correct answer marked. Regenerate
it with:

```bash
python3 make_pdf.py
```

## Notes

- Answers are stored separately for the main bank and the retake flow.
- The page is designed for static hosting and works well on GitHub Pages.
