#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace option sets in a deck data module, leaving everything else intact.

The banks were written with a careful correct answer and three quick
distractors, which produced a severe length tell: the correct option was the
longest in 70% of the main bank and in 100% of the study bank. A reader could
score without reading the question.

Rewriting the options by hand would mean retyping the explanation and teach
blocks around them, which invites transcription drift. This loads a module,
substitutes only the option tuples, and re-emits the file with everything else
copied verbatim.

Supply replacements as REPLACEMENTS[question_number] = (correct, [d1, d2, d3]),
numbered in the order the build script walks the decks, starting at 1.

Usage::

    python3 rebalance_options.py --check deck_study_a.py
    python3 rebalance_options.py --apply deck_study_a.py
"""

import argparse
import importlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def wrap(text, indent, width=92):
    """Emit a Python string literal, split across lines if long."""
    if len(text) + indent <= width:
        return " " * indent + repr(text)
    out, line, parts = [], "", text.split(" ")
    for w in parts:
        if len(line) + len(w) + 1 > width - indent - 4 and line:
            out.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        out.append(line)
    pieces = []
    for i, seg in enumerate(out):
        seg = seg if i == len(out) - 1 else seg + " "
        pieces.append(" " * indent + repr(seg))
    return "\n".join(pieces)


def emit(decks, module_doc, per_deck):
    buf = io.StringIO()
    buf.write("# -*- coding: utf-8 -*-\n")
    buf.write('"""%s"""\n\n' % module_doc)
    buf.write("DECKS = [\n")
    for deck in decks:
        buf.write("    {\n")
        buf.write("        %s\n" % ('"topic": %r,' % deck["topic"]))
        buf.write("        %s\n" % ('"source": %r,' % deck["source"]))
        buf.write('        "questions": [\n')
        for q in deck["questions"]:
            stem, correct, dists, expl = q[0], q[1], q[2], q[3]
            teach = q[4] if len(q) > 4 else None
            buf.write("            (\n")
            buf.write(wrap(stem, 16) + ",\n")
            buf.write(wrap(correct, 16) + ",\n")
            buf.write("                [\n")
            for d in dists:
                buf.write(wrap(d, 20) + ",\n")
            buf.write("                ],\n")
            buf.write(wrap(expl, 16) + ",\n")
            if teach is not None:
                buf.write(wrap(teach, 16) + ",\n")
            buf.write("            ),\n")
        buf.write("        ],\n")
        buf.write("    },\n")
    buf.write("]\n")
    return buf.getvalue()


def spread(opts, correct):
    lens = [len(o) for o in opts]
    return (max(lens) - min(lens)) / max(min(lens), 1) * 100, len(correct) == max(lens)


def run(module_name, replacements, apply_changes, forced_offset=None):
    mod = importlib.import_module(module_name.replace(".py", ""))
    decks = [dict(d) for d in mod.DECKS]

    total_qs = sum(len(d["questions"]) for d in decks)
    # Replacement keys use the numbering of the compiled bank, which runs across
    # all three modules. Within a module, questions restart at 1, so infer the
    # offset from the keys rather than silently matching nothing.
    lo = min(replacements) if replacements else 1
    if forced_offset is not None:
        offset = forced_offset
    else:
        offset = lo - 1 if lo > total_qs else 0
    if offset:
        print("  (keys start at %d; treating as offset %d)" % (lo, offset))

    number = 0
    changed = 0
    worst = []
    for deck in decks:
        new_qs = []
        for q in deck["questions"]:
            number += 1
            q = list(q)
            if (number + offset) in replacements:
                correct, dists = replacements[number + offset]
                q[1], q[2] = correct, list(dists)
                changed += 1
            opts = [q[1]] + list(q[2])
            pct, longest = spread(opts, q[1])
            if longest or pct > 45:
                worst.append((number, round(pct), len(q[1]),
                              [len(x) for x in q[2]]))
            new_qs.append(tuple(q))
        deck["questions"] = new_qs

    total = number
    print("%s: %d questions, %d replaced" % (module_name, total, changed))
    if changed and changed < total:
        print("  (partial range; %d left untouched)" % (total - changed))
    print("  still flagged (correct longest, or spread > 45%%): %d" % len(worst))
    for w in worst[:12]:
        print("    q%-4d spread %3d%%  correct %3d  distractors %s"
              % (w[0], w[1], w[2], w[3]))
    if len(worst) > 12:
        print("    ... and %d more" % (len(worst) - 12))

    if not apply_changes:
        print("  (check only, nothing written)")
        return

    doc = (mod.__doc__ or "").strip("\n")
    src = emit(decks, doc, None)
    path = os.path.join(HERE, module_name if module_name.endswith(".py")
                        else module_name + ".py")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    print("  written: %s" % path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("module")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--offset", type=int, default=None,
                    help="question number of this module's first question, minus one")
    args = ap.parse_args()

    name = args.module.replace(".py", "")
    repl_mod = importlib.import_module("options_" + name.split("_", 1)[1]
                                       if name.startswith("deck_") else name)
    run(name, repl_mod.REPLACEMENTS, args.apply and not args.check, args.offset)


if __name__ == "__main__":
    main()
