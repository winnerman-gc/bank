# AWS Certified Cloud Practitioner - MCQ Practice

A comprehensive interactive practice platform for AWS Certified Cloud Practitioner exam preparation with **1,142 questions** from 23 different practice exams.

## Features

✅ **1,142 AWS MCQ Questions** - From official AWS practice exams (Exams 1-23)
✅ **Single & Multiple-Choice Questions** - 982 single-answer + 159 "Choose TWO/THREE" questions
✅ **Block-based Learning** - Complete one exam block and move to the next
✅ **Exam Filtering** - Select and practice specific exams or view all questions
✅ **Random Mode** - Practice random questions for variety
✅ **Option Shuffling** - Randomize answer options to prevent memorization
✅ **Cache Busting** - Versioned page/data URLs help GitHub Pages pick up fresh builds
✅ **Progress Tracking** - Automatic tracking of correct/wrong answers
✅ **Answer Review** - Review and retake only wrong answers
✅ **Persistent Storage** - Progress saved locally in browser storage
✅ **AWS Themed UI** - Orange and gray AWS color scheme

## Getting Started

### 1. Open the Practice Page
Simply open `index.html` in your web browser:
- Double-click `index.html` to open it
- Or right-click and select "Open with" → your preferred browser

### 2. Choose a Study Mode

#### **Exam Mode** (Default)
- Select individual exams (1-23)
- Work through 50 questions per exam
- Complete the block and move to the next

#### **All Questions Mode**
- Practice all 1,142 questions at once
- Great for comprehensive review

#### **Random Mode**
- Get random questions from the entire bank
- Good for testing knowledge diversity

### 3. Study Features

**Progress Tracking**
- Real-time stats: Correct/Wrong/Score/Progress
- View your completion percentage

**Option Shuffling**
- Click "Shuffle" button to randomize answer positions
- Prevents memorization by position
- Helps identify deep understanding

**Cache Busting**
- The page and `compiled.json` are loaded with a shared version token
- If you update the page and want to force a refresh, bump the `CACHE_VERSION` value in `index.html`
- The page also updates the browser URL to include that version, so refreshes stay on the latest build

**Retake Wrong Answers**
- Click "Retake Wrong" to focus on problem areas
- Practice only the questions you got wrong
- Build confidence with difficult topics

**Reset Progress**
- Start fresh with the "Reset" button
- Clears all stored answers

## How Questions Are Organized

Questions are divided into **23 exam blocks**, each containing ~50 questions:
- **Exam 1-22**: 50 questions each
- **Exam 23**: 50 questions
- **Total**: 1,142 questions

Each question has:
- Clear question text
- 4-5 multiple choice options
- Correct answer validation
- Immediate feedback

## Data Storage

Your progress is automatically saved:
- **Browser LocalStorage** - Persists when you close and reopen
- **Privacy** - All data stored locally on your device
- **Reset** - Use the "Reset" button to clear all progress

## File Structure

```
aws/
├── index.html           # Main practice page
├── compiled.json        # All 1,142 questions with answers
├── compile_questions.py # Script to fetch and compile questions
├── verify.py           # Verification script for data quality
└── README.md           # This file
```

## How It Works

1. **Question Compilation**
   - `compile_questions.py` fetches practice exams from the GitHub repository
   - Parses question text, options, and correct answers
   - Generates `compiled.json` with structured data

2. **Interactive Practice**
   - `index.html` loads questions from `compiled.json`
   - Provides interactive UI for practicing
   - Saves progress to browser storage

3. **Quality Verification**
   - `verify.py` checks that all questions and answers are properly parsed
   - 1,141 questions have correct answers extracted

## Tips for Success

1. **Start with Exam Blocks**
   - Work through exams sequentially to build concepts
   - Don't jump around initially

2. **Enable Option Shuffling**
   - Click "Shuffle" to randomize answers
   - Prevents memorization by position

3. **Review Wrong Answers**
   - Use "Retake Wrong" to focus on weak areas
   - Repeat until confident

4. **Take Multiple Passes**
   - First pass: Learn the content
   - Second pass: Strengthen weak areas
   - Third pass: Random mode for final review

5. **Track Your Progress**
   - Monitor the score percentage
   - Aim for 70%+ on all exams

## Browser Compatibility

- Chrome / Chromium ✅
- Firefox ✅
- Safari ✅
- Edge ✅
- Any modern browser with LocalStorage support

## Questions Source

Questions are sourced from:
- [AWS Certified Cloud Practitioner Notes Repository](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes)
- Official AWS practice exams
- Community-contributed content

## Customization

To regenerate questions from source:
```bash
python compile_questions.py
```

This will:
- Fetch latest practice exams from GitHub
- Parse questions and answers
- Update `compiled.json`

## License

Study materials sourced from: https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes

This is a learning tool for exam preparation. Always verify with official AWS documentation for the most current information.

---

**Good luck with your AWS certification! 🚀**
