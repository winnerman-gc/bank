#!/usr/bin/env python3
"""
Render compiled.json into a printable PDF of all questions, options and answers.

Uses PyMuPDF's Story API for automatic multi-page text reflow.
    pip install pymupdf
    python3 make_pdf.py
"""
import html
import json

import fitz  # PyMuPDF

SRC = "compiled.json"
OUT = "TE456-NTN-MCQs-with-answers.pdf"
TITLE = "TE 456 - Satellite Communication & NTN"
SUBTITLE = "100 Multiple-Choice Questions with Answers"

CSS = """
body { font-family: sans-serif; color: #14213a; }
h1 { font-size: 17px; margin: 0 0 2px 0; color: #3730a3; }
h2 { font-size: 11px; margin: 0 0 14px 0; color: #64748b; font-weight: normal; }
.q  { font-size: 10.5px; font-weight: bold; margin: 11px 0 3px 0; }
.opt { font-size: 10px; margin: 1px 0 1px 16px; color: #1f2937; }
.correct { color: #15803d; font-weight: bold; }
.ans { font-size: 9.5px; margin: 3px 0 0 16px; color: #15803d; font-weight: bold; }
"""

LETTERS = ["A", "B", "C", "D", "E", "F"]


def build_html(records):
    parts = [f"<h1>{html.escape(TITLE)}</h1>", f"<h2>{html.escape(SUBTITLE)}</h2>"]
    for q in records:
        n = q["question_number"]
        correct = q["correct_answer"][0]
        parts.append(f'<p class="q">{n}. {html.escape(q["question_text"])}</p>')
        correct_letter = "?"
        for i, opt in enumerate(q["options"]):
            letter = LETTERS[i]
            is_correct = opt == correct
            cls = "opt correct" if is_correct else "opt"
            mark = "  ✓" if is_correct else ""
            if is_correct:
                correct_letter = letter
            parts.append(f'<p class="{cls}">{letter}. {html.escape(opt)}{mark}</p>')
        parts.append(f'<p class="ans">Answer: {correct_letter}. {html.escape(correct)}</p>')
    return "<body>" + "".join(parts) + "</body>"


def main():
    records = json.load(open(SRC, encoding="utf-8"))
    story = fitz.Story(html=build_html(records), user_css=CSS)
    writer = fitz.DocumentWriter(OUT)
    mediabox = fitz.paper_rect("a4")
    where = mediabox + (50, 50, -50, -50)

    pages = 0
    more = 1
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
        pages += 1
    writer.close()
    print(f"Wrote {OUT}: {len(records)} questions across {pages} pages")


if __name__ == "__main__":
    main()
