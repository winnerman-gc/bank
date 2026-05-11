# Madlene Advanced Excel Mastery - MCQ Practice

A static MCQ practice site for the two question banks in this folder:

- `advanced_excel_mastery_200_mcqs_json.json`
- `advanced_excel_mastery_MCQs.json`

## Features

- Source selector for each question bank
- All Questions mode
- Random mode
- Auto-shuffled answer options with stable per-question order
- Retake Wrong mode that only includes questions answered incorrectly
- Back to Main button to return from retake mode
- Persistent answer storage in the browser
- Multi-answer support when a question has more than one correct answer
- Auto-scroll to the next question after a correct answer

## How to use

1. Open `index.html` in a browser through a local web server or GitHub Pages.
2. Pick a source set or open all questions.
3. Answer questions normally.
4. Use `Retake Wrong` to practice only missed questions.
5. Use `Back to Main` to return to the main set view.

## Notes

- Answers are stored separately for the main and retake flows.
- Question numbering is kept per source bank, so the page stores answers with a source prefix internally.
- The page is designed for static hosting and works well on GitHub Pages.
