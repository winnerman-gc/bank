#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build compiled-study.json - the study bank, five questions per deck.

This is a second bank alongside compiled.json. Where that one tests recall and
applied reasoning across ten questions per deck, this one carries five questions
per deck aimed at the CONCEPTS: why a mechanism exists, what it trades against,
and how it connects to the rest of the course.

Each record carries two levels of explanation:

    explanation   one or two sentences on why the answer is right
    teach         the surrounding topic, written so the card can be revised
                  from without opening the deck

The practice page shows the short explanation immediately and puts the longer
block behind a toggle, so a card works both as a quick check and as a study note.

The question data lives in three modules, eight decks each:

    deck_study_a.py   groups 1 to 8
    deck_study_b.py   groups 9 to 16
    deck_study_c.py   groups 17 to 24

Run it with::

    python3 build_study_questions.py
"""

import json
import os
import sys

from deck_study_a import DECKS as DECKS_A
from deck_study_b import DECKS as DECKS_B
from deck_study_c import DECKS as DECKS_C

DECKS = DECKS_A + DECKS_B + DECKS_C

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "compiled-study.json")

NUM_OPTIONS = 4
PER_DECK = 5

# A teach block shorter than this is almost certainly a stub rather than a
# study note, so the build calls it out.
MIN_TEACH = 400


def build():
    records = []
    slot_counts = [0] * NUM_OPTIONS
    number = 0
    thin = []

    for deck_index, deck in enumerate(DECKS):
        topic = deck["topic"]
        source = deck["source"]
        questions = deck["questions"]

        if len(questions) != PER_DECK:
            sys.exit("%s has %d questions, expected %d"
                     % (topic, len(questions), PER_DECK))

        for q_index, item in enumerate(questions):
            if len(item) != 5:
                sys.exit("%s question %d is malformed; expected 5 fields, got %d"
                         % (topic, q_index + 1, len(item)))

            stem, correct, distractors, explanation, teach = item

            if len(distractors) != NUM_OPTIONS - 1:
                sys.exit("%s question %d has %d distractors, expected %d"
                         % (topic, q_index + 1, len(distractors), NUM_OPTIONS - 1))

            pool = [correct] + list(distractors)
            if len(set(pool)) != NUM_OPTIONS:
                sys.exit("%s question %d repeats an option" % (topic, q_index + 1))

            if not explanation.strip():
                sys.exit("%s question %d has no explanation" % (topic, q_index + 1))
            if len(teach.strip()) < MIN_TEACH:
                thin.append("%s q%d (%d chars)"
                            % (topic[:40], q_index + 1, len(teach.strip())))

            # Walk the answer slot by deck and by position, so neither the deck
            # boundary nor the question number lines up with one letter.
            slot = (deck_index + q_index) % NUM_OPTIONS
            options = list(distractors)
            options.insert(slot, correct)
            slot_counts[slot] += 1

            number += 1
            records.append({
                "question_number": number,
                "question_text": stem,
                "options": options,
                "correct_answer": [correct],
                "explanation": explanation,
                "teach": teach,
                "topic": topic,
                "source": source,
            })

    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(records, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    teach_chars = sum(len(r["teach"]) for r in records)
    print("decks:      %d" % len(DECKS))
    print("questions:  %d  (%d per deck)" % (len(records), PER_DECK))
    print("key spread by slot (A/B/C/D): %s"
          % " / ".join(str(c) for c in slot_counts))
    print("teach text: %d chars, %d average per card"
          % (teach_chars, teach_chars // max(len(records), 1)))
    print("written:    %s" % OUTPUT)

    if thin:
        print("\nWARNING: teach block under %d chars on:" % MIN_TEACH)
        for t in thin:
            print("  %s" % t)
    else:
        print("every card carries a full teach block")


if __name__ == "__main__":
    build()
