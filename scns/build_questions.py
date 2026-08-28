#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build compiled.json - TE 456, the student presentation decks.

The questions come from the 24 student group presentations in
``~/Documents/y4s2/scns/TE 456 PRESENTATIONS``, one themed set of ten questions
per deck.

Those decks are image heavy. Many slides carry a title and nothing else, and the
content sits inside a diagram. The questions were written after rendering every
slide and reading the figures, not from the slide text alone, so a question can
rest on a number or a relationship that appears only in a picture.

The question data lives in three modules, eight decks each:

    deck_questions_a.py   groups 1 to 8
    deck_questions_b.py   groups 9 to 16
    deck_questions_c.py   groups 17 to 24

Each deck is a dict::

    {
        "topic":  short name shown on the card,
        "source": which deck and which slides the answer rests on,
        "questions": [ (stem, correct, [d1, d2, d3], explanation), ... ]
    }

Run it with::

    python3 build_questions.py
"""

import json
import os
import sys

from deck_questions_a import DECKS as DECKS_A
from deck_questions_b import DECKS as DECKS_B
from deck_questions_c import DECKS as DECKS_C

DECKS = DECKS_A + DECKS_B + DECKS_C

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "compiled.json")

# The practice page shuffles the options anyway, but the stored order is what a
# printed copy shows. Cycling the slot keeps the key evenly spread so the PDF
# does not develop a visible bias toward one letter.
NUM_OPTIONS = 4


def build():
    records = []
    slot_counts = [0] * NUM_OPTIONS
    number = 0

    for deck_index, deck in enumerate(DECKS):
        topic = deck["topic"]
        source = deck["source"]
        questions = deck["questions"]

        if len(questions) != 10:
            sys.exit(
                "%s has %d questions, expected 10" % (topic, len(questions))
            )

        for q_index, item in enumerate(questions):
            if len(item) != 4:
                sys.exit(
                    "%s question %d is malformed; expected 4 fields, got %d"
                    % (topic, q_index + 1, len(item))
                )

            stem, correct, distractors, explanation = item

            if len(distractors) != NUM_OPTIONS - 1:
                sys.exit(
                    "%s question %d has %d distractors, expected %d"
                    % (topic, q_index + 1, len(distractors), NUM_OPTIONS - 1)
                )

            pool = [correct] + list(distractors)
            if len(set(pool)) != NUM_OPTIONS:
                sys.exit(
                    "%s question %d repeats an option" % (topic, q_index + 1)
                )

            # Walk the slot forward by deck and by position, so neither the deck
            # boundary nor the question number lines up with one letter.
            slot = (deck_index + q_index) % NUM_OPTIONS
            options = list(distractors)
            options.insert(slot, correct)
            slot_counts[slot] += 1

            number += 1
            records.append(
                {
                    "question_number": number,
                    "question_text": stem,
                    "options": options,
                    "correct_answer": [correct],
                    "explanation": explanation,
                    "topic": topic,
                    "source": source,
                }
            )

    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(records, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    print("decks:     %d" % len(DECKS))
    print("questions: %d" % len(records))
    print("key spread by slot (A/B/C/D): %s" % " / ".join(str(c) for c in slot_counts))
    print("written:   %s" % OUTPUT)

    missing = [r["question_number"] for r in records if not r["explanation"]]
    if missing:
        print("WARNING: no explanation on questions %s" % missing)
    else:
        print("every question carries an explanation")


if __name__ == "__main__":
    build()
