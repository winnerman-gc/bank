#!/usr/bin/env python3
"""
Render compiled.json into a single printable PDF of all the past-paper questions,
options and answers.

Uses PyMuPDF's Story API for automatic multi-page text reflow.
    pip install pymupdf
    python3 make_pdf.py
"""
import html
import json

import fitz  # PyMuPDF

SOURCES = [
    ("compiled.json", "Set 1 - Past paper (transcribed, Section A)"),
    ("compiled_2.json", "Set 2 - Deck-based practice questions"),
]
OUT = "TE452-TE462-Policy-Regulation-Past-Paper-with-answers.pdf"
TITLE = "TE 452 / TE 462 - Policy & Regulation"
SUBTITLE = ("Set 1: 54 past-paper questions (answers verified against the decks) + "
            "Set 2: 50 deck-based practice questions, all with insights")

CSS = """
body { font-family: sans-serif; color: #14213a; }
h1 { font-size: 17px; margin: 0 0 2px 0; color: #115e59; }
h2 { font-size: 11px; margin: 0 0 14px 0; color: #64748b; font-weight: normal; }
h3 { font-size: 13px; margin: 18px 0 6px 0; color: #115e59; border-top: 1px solid #cbd5e1; padding-top: 10px; }
.q  { font-size: 10.5px; font-weight: bold; margin: 11px 0 3px 0; }
.opt { font-size: 10px; margin: 1px 0 1px 16px; color: #1f2937; }
.correct { color: #15803d; font-weight: bold; }
.ans { font-size: 9.5px; margin: 3px 0 0 16px; color: #15803d; font-weight: bold; }
.why { font-size: 9px; margin: 2px 0 0 16px; color: #92400e; }
"""

LETTERS = ["A", "B", "C", "D", "E", "F"]


def build_html():
    parts = [f"<h1>{html.escape(TITLE)}</h1>", f"<h2>{html.escape(SUBTITLE)}</h2>"]
    total = 0
    for src, section_title in SOURCES:
        records = json.load(open(src, encoding="utf-8"))
        parts.append(f"<h3>{html.escape(section_title)}</h3>")
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
            why = q.get("explanation")
            if why:
                parts.append(f'<p class="why">Insight: {html.escape(why)}</p>')
        total += len(records)
    return "<body>" + "".join(parts) + "</body>", total


def main():
    body_html, total = build_html()
    story = fitz.Story(html=body_html, user_css=CSS)
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
    print(f"Wrote {OUT}: {total} questions across {pages} pages")


if __name__ == "__main__":
    main()
