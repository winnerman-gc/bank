# Power BI Mastery - MCQ Practice

A static MCQ practice site for the three Power BI question banks in this folder:

- `gemini-code-1779139672572.json` (Set 1)
- `gemini-code-1779139949310.json` (Set 2)
- `gemini-code-1779140176314.json` (Set 3)

## Features

- Three separate question sets with independent stats tracking
- Next Set button to move between sets
- Auto-shuffled answer options with stable per-question order
- Retake Wrong mode that only includes questions answered incorrectly from the current set
- Back to Main button to return from retake mode
- Persistent answer storage in the browser per set
- Multi-answer support when a question has more than one correct answer
- Auto-scroll to the next question after a correct answer

## How to use

1. Open `index.html` in a browser through a local web server or GitHub Pages.
2. Pick a source set from the selector.
3. Answer questions normally. Stats are tracked per set.
4. Use `Retake Wrong` to practice only missed questions from that set.
5. Use `Back to Main` to return to the main set view.
6. Use `Next Set` button at the end of a set to move to the next one.

## Notes

- Answers are stored separately for each set and for retake flows.
- Question numbering and stats are tracked independently per source bank.
- The page is designed for static hosting and works well on GitHub Pages.
