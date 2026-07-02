# Satellite Communication & NTN (TE 456) - MCQ Practice

A static MCQ practice site covering the TE 456 *Satellite Communication and
Navigation System* material, focused on Non-Terrestrial Networks (NTN) and their
integration with 5G. It is a single bank of 100 questions (`compiled.json`)
spanning four themed areas:

| Area | Focus |
| ---- | ----- |
| NTN fundamentals - what & why | TN vs NTN, spaceborne/airborne platforms, HAPS, service ubiquity/continuity/scalability, standardization, 6G vision |
| Orbits, platforms & beams | Kepler orbits, GEO/MEO/LEO characteristics, constellations (GPS, Starlink), HAPS, Earth-fixed / quasi-Earth-fixed / Earth-moving beams |
| 5G NR-NTN architecture & challenges | Service/feeder links, transparent vs regenerative payloads, gNB CU/DU split, ISL, RTT, Doppler shift/rate, Faraday rotation |
| SatCom payload, links & 5G systems | Repeaters/transponders, satellite subsystems, link budget (EIRP, G/T, C/N0), 5G NR frame structure, OFDMA, physical channels, initial access |

## Source material

Questions are derived from the slide decks in this folder:

- `TE456-NTN-What&Why.pdf` - Legacy satellite communication to NTN (what & why)
- `TE456-NTN-Overview-1.pdf` - Orbits, platforms and beams
- `TE456-5GNR-NTN-2026-complete.pdf` - 3GPP 5G NR-NTN architecture and challenges
- `TE456-Elements-SatCom5GSystems-2026-Complete.pdf` - SatCom payload, links & 5G systems

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

`compiled.json` is generated from `build_questions.py`:

```bash
python3 build_questions.py
```

The script holds every question as
`(question_text, correct_answer, [distractor, distractor, distractor])` and
places the correct answer at a balanced, reproducible position so the key
(A/B/C/D) is evenly distributed across the bank (25 / 25 / 25 / 25). The output
JSON matches the format used by the other practice sites in this repository.

## Question & answer PDF

`TE456-NTN-MCQs-with-answers.pdf` is a printable copy of all 200 questions
(both Part 1 and Part 2 banks) with their options and the correct answer
marked. Regenerate it with:

```bash
python3 make_pdf.py
```
