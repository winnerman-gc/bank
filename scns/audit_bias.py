#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Measure answer-selection bias in the TE 456 question banks.

A multiple-choice question is biased when the correct option can be picked
without knowing the subject. This checks the tells that actually work on a
four-option bank:

  LENGTH       the correct option is reliably the longest, or the shortest.
               Chance is 25% for a four-option question.
  POSITION     the answer sits at one slot more often than the others.
  ABSOLUTES    distractors carry always/never/only/all, which a test-wise
               reader eliminates on sight.
  HEDGES       the correct option carries may/typically/generally, which a
               test-wise reader selects on sight.
  STEM ECHO    the correct option repeats distinctive words from the stem
               while the distractors do not.
  NUMERALS     the correct option is the only one carrying a figure, or the
               only one without.

Run it with::

    python3 audit_bias.py                    # audit every bank
    python3 audit_bias.py compiled.json      # audit one
    python3 audit_bias.py --verbose          # list the offending questions
"""

import argparse
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULTS = ["compiled.json", "compiled-study.json"]

ABSOLUTE = r"\b(all|always|never|none|only|every|entirely|completely|no\s+\w+\s+(?:is|are|can)|impossible|must\s+always|cannot\s+ever)\b"
HEDGE = r"\b(may|might|typically|generally|usually|often|tends?\s+to|can\s+be|approximately|roughly|about)\b"

# Words too common to signal an echo between stem and option.
STOP = set("""a an the of to in on for with and or is are was were be been being
that this these those it its as at by from into than then there their they them
which what when where why how does do did can could may might must should would
will not no nor but if so such other another each any some more most less least
same different between across over under about within without during while
because since although though however therefore thus hence rather instead
one two three four both all every only very much many few several
question following statement true false correct incorrect best describe
describes described explain explains explained give gives given name names
named list lists listed state states stated define defines defined
what's whats does_not""".split())


def words(text):
    return {w for w in re.findall(r"[a-z][a-z0-9-]{3,}", text.lower()) if w not in STOP}


def audit(path, verbose=False):
    with open(path, encoding="utf-8") as fh:
        records = json.load(fh)

    n = len(records)
    if not n:
        return None
    k = len(records[0]["options"])
    chance = 100.0 / k

    longest = shortest = 0
    pos = Counter()
    corr_len, dist_len = [], []
    abs_corr = abs_dist = 0
    hedge_corr = hedge_dist = 0
    echo_corr = echo_dist = 0
    num_only_corr = num_only_dist = 0

    flags = {"longest": [], "shortest": [], "absolute": [], "hedge": [],
             "echo": [], "numeral": []}

    for r in records:
        opts = r["options"]
        correct = r["correct_answer"][0]
        ci = opts.index(correct)
        others = [o for i, o in enumerate(opts) if i != ci]

        pos[ci] += 1
        lens = [len(o) for o in opts]
        corr_len.append(len(correct))
        dist_len.extend(len(o) for o in others)

        if len(correct) == max(lens) and lens.count(max(lens)) == 1:
            longest += 1
            flags["longest"].append(r["question_number"])
        if len(correct) == min(lens) and lens.count(min(lens)) == 1:
            shortest += 1
            flags["shortest"].append(r["question_number"])

        c_abs = bool(re.search(ABSOLUTE, correct, re.I))
        d_abs = sum(bool(re.search(ABSOLUTE, o, re.I)) for o in others)
        abs_corr += c_abs
        abs_dist += d_abs
        # A giveaway: absolutes in the distractors only.
        if d_abs and not c_abs:
            flags["absolute"].append(r["question_number"])

        c_h = bool(re.search(HEDGE, correct, re.I))
        d_h = sum(bool(re.search(HEDGE, o, re.I)) for o in others)
        hedge_corr += c_h
        hedge_dist += d_h
        if c_h and not d_h:
            flags["hedge"].append(r["question_number"])

        sw = words(r["question_text"])
        c_echo = len(sw & words(correct))
        d_echo = max((len(sw & words(o)) for o in others), default=0)
        echo_corr += c_echo
        echo_dist += d_echo
        if c_echo > d_echo + 1:
            flags["echo"].append(r["question_number"])

        c_num = bool(re.search(r"\d", correct))
        d_num = sum(bool(re.search(r"\d", o)) for o in others)
        if c_num and d_num == 0:
            num_only_corr += 1
            flags["numeral"].append(r["question_number"])
        if not c_num and d_num == len(others):
            num_only_dist += 1
            flags["numeral"].append(r["question_number"])

    mean_c = sum(corr_len) / len(corr_len)
    mean_d = sum(dist_len) / len(dist_len)

    print("=" * 68)
    print("%s   %d questions, %d options each" % (os.path.basename(path), n, k))
    print("=" * 68)

    def line(label, count, note=""):
        pct = 100.0 * count / n
        bar = "#" * int(pct / 2)
        print("  %-34s %4d  %5.1f%%  %-26s %s" % (label, count, pct, bar, note))

    print("\nLENGTH   (chance = %.0f%%)" % chance)
    line("correct is the longest", longest,
         "OK" if longest <= n * (chance + 8) / 100 else "<-- BIASED")
    line("correct is the shortest", shortest,
         "OK" if shortest <= n * (chance + 8) / 100 else "<-- BIASED")
    print("  %-34s correct %.1f chars, distractors %.1f  (%+.1f%%)"
          % ("mean option length", mean_c, mean_d,
             100.0 * (mean_c - mean_d) / mean_d))

    print("\nPOSITION (chance = %.0f%%)" % chance)
    for i in range(k):
        line("answer at slot %s" % "ABCD"[i], pos[i])

    # A raw "distractors only" count is misleading: with k-1 distractors against
    # one answer, that event is common even when both sides carry a word at the
    # same rate. Compare PER-OPTION rates, and show what the naive count would
    # be if the rates were in fact equal.
    def wording(label, corr_hits, dist_hits, naive):
        p_c = corr_hits / n
        p_d = dist_hits / (n * (k - 1))
        expect = (1 - p_d) ** 0 * 0  # placeholder, computed below
        expect = (1 - min(p_d, 1.0)) ** (k - 1)
        expect_pct = 100.0 * (1 - expect) * (1 - min(p_c, 1.0))
        ratio = (p_d / p_c) if p_c else float("inf")
        verdict = "OK" if 0.6 <= ratio <= 1.7 else "<-- SKEWED"
        print("  %-24s per option: correct %5.1f%%  distractor %5.1f%%  "
              "ratio %4.2f  %s"
              % (label, 100 * p_c, 100 * p_d, ratio, verdict))
        print("  %-24s naive 'one side only' %5.1f%%, expected %5.1f%% at equal rates"
              % ("", 100.0 * naive / n, expect_pct))

    print("\nWORDING  (per-option rates; a raw one-sided count over-reports)")
    wording("absolute words", abs_corr, abs_dist, len(set(flags["absolute"])))
    wording("hedge words", hedge_corr, hedge_dist, len(set(flags["hedge"])))

    print("\nOTHER TELLS")
    line("correct echoes the stem more", len(set(flags["echo"])),
         "<-- GIVEAWAY" if len(set(flags["echo"])) > n * 0.12 else "OK")
    print("  %-34s correct %.2f, best distractor %.2f"
          % ("mean stem-word overlap", echo_corr / n, echo_dist / n))
    line("odd one out on numerals", len(set(flags["numeral"])),
         "<-- GIVEAWAY" if len(set(flags["numeral"])) > n * 0.10 else "OK")

    if verbose:
        for name, nums in flags.items():
            uniq = sorted(set(nums))
            if uniq:
                print("\n  %s (%d): %s" % (name, len(uniq),
                      ", ".join(str(x) for x in uniq[:40])
                      + (" ..." if len(uniq) > 40 else "")))
    print()
    return {"n": n, "longest": longest, "shortest": shortest,
            "mean_c": mean_c, "mean_d": mean_d, "flags": flags}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", default=None)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    for f in (args.files or DEFAULTS):
        p = f if os.path.isabs(f) else os.path.join(HERE, f)
        if os.path.exists(p):
            audit(p, args.verbose)
        else:
            print("skip, not found: %s" % p)


if __name__ == "__main__":
    main()
