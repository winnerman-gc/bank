#!/usr/bin/env python3
"""Render compiled.json into a printable PDF of all 240 questions.

The questions are grouped under the deck they came from, and the explanation is
printed beneath each answer, so the PDF works as a revision document rather than
only as a practice paper.

    pip install pymupdf
    python3 make_pdf.py
"""
import html
import json
import os

import fitz  # PyMuPDF

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "compiled.json")
OUT = os.path.join(HERE, "TE456-Presentation-Decks-MCQs-with-answers.pdf")

TITLE = "TE 456 - Satellite Communication & Navigation Systems"
SUBTITLE = "240 Multiple-Choice Questions from the 24 Presentation Decks"

CSS = """
body { font-family: sans-serif; color: #14213a; }
h1 { font-size: 17px; margin: 0 0 2px 0; color: #3730a3; }
h2 { font-size: 11px; margin: 0 0 6px 0; color: #64748b; font-weight: normal; }
h3 { font-size: 13px; margin: 18px 0 2px 0; color: #3730a3;
     border-top: 1px solid #cbd5e1; padding-top: 10px; }
.deck-source { font-size: 9px; margin: 0 0 4px 0; color: #64748b; }
.intro { font-size: 9.5px; margin: 0 0 6px 0; color: #475569; }
.q  { font-size: 10.5px; font-weight: bold; margin: 11px 0 3px 0; }
.opt { font-size: 10px; margin: 1px 0 1px 16px; color: #1f2937; }
.correct { color: #15803d; font-weight: bold; }
.ans { font-size: 9.5px; margin: 3px 0 0 16px; color: #15803d; font-weight: bold; }
.why { font-size: 9.5px; margin: 2px 0 0 16px; color: #475569; }
"""

LETTERS = ["A", "B", "C", "D", "E", "F"]


def build_html():
    records = json.load(open(SOURCE, encoding="utf-8"))

    parts = [
        "<h1>%s</h1>" % html.escape(TITLE),
        "<h2>%s</h2>" % html.escape(SUBTITLE),
        '<p class="intro">Ten questions per deck. The correct option is marked '
        "with a tick, and the reason follows each answer.</p>",
    ]

    current_topic = None
    for q in records:
        if q["topic"] != current_topic:
            current_topic = q["topic"]
            parts.append("<h3>%s</h3>" % html.escape(current_topic))
            parts.append('<p class="deck-source">%s</p>' % html.escape(q["source"]))

        parts.append(
            '<p class="q">%d. %s</p>'
            % (q["question_number"], html.escape(q["question_text"]))
        )

        correct = q["correct_answer"][0]
        correct_letter = "?"
        for i, opt in enumerate(q["options"]):
            letter = LETTERS[i]
            is_correct = opt == correct
            if is_correct:
                correct_letter = letter
            parts.append(
                '<p class="%s">%s. %s%s</p>'
                % (
                    "opt correct" if is_correct else "opt",
                    letter,
                    html.escape(opt),
                    "  ✓" if is_correct else "",
                )
            )

        parts.append(
            '<p class="ans">Answer: %s. %s</p>'
            % (correct_letter, html.escape(correct))
        )
        parts.append('<p class="why">%s</p>' % html.escape(q["explanation"]))

    return "<body>" + "".join(parts) + "</body>", len(records)


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
    print("Wrote %s: %d questions across %d pages" % (OUT, total, pages))


if __name__ == "__main__":
    main()
