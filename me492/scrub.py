# -*- coding: utf-8 -*-
"""Strip option letters and paper citations out of the explanations.

Two things do not belong in an explanation on this site.

Option letters. The options are written out in full and shuffled on every
render, so "the answer is A" is meaningless here and actively misleading. Where
a letter carried a fact, the fact is spelled out instead.

Paper citations. "The 2005 official marking scheme marks", "one compiled answer
sheet", "trap list 12", "Guide 6.11". That is bookkeeping about where the answer
came from. It does not help you answer the question, so it goes. The verified
field still records how far each answer is trusted.

The rules rewrite the phrasing rather than deleting the sentence, because the
reasoning usually sits in the same sentence as the citation.
"""
import re

RULES = [
    # --- a key or a paper marking something -------------------------------
    (r"\bWarning: the \d{4} official key marks\b", "Note that the marked answer is"),
    (r"\bthe \d{4} (?:official )?(?:key|exam|paper|marking scheme) (?:marks|marked|takes|took)\b",
     "the marked answer is"),
    (r"\bthe \d{4} (?:online )?(?:key|exam|paper) confirms?(?:ed)?\b", "this confirms"),
    (r"\bthe \d{4} (?:online )?(?:exam|paper|key)\b", "the marked answer"),
    (r"\bEvery KNUST paper marks\b", "The answer is"),
    (r"\bthe papers? marks?\b", "the answer is"),
    (r"\bthe papers? rejects?\b", "the answer rejects"),
    (r"\bthe papers? accepts?\b", "the accepted answers"),
    (r"\bthe papers? prints?\b", "the options print"),
    (r"\bthe papers? swaps?\b", "the options swap"),
    (r"\bthe papers? mixes\b", "the options mix"),
    (r"\bthe papers? attaches\b", "the options attach"),
    (r"\bthe papers? asks?\b", "you are asked"),
    (r"\bthe papers? uses?\b", "the options use"),
    (r"\bthe papers? wants?\b", "the answer wants"),
    (r"\bthe papers? offers?\b", "the options offer"),
    (r"\bthe papers? forces?\b", "the options force"),
    (r"\bthe key (?:marks|marked|gives|says)\b", "the marked answer is"),
    (r"\banswer as the key does\b", "answer with the text, not the letter"),

    # --- whole clauses that are provenance only ---------------------------
    (r",? ?(?:and )?(?:one|some) compiled (?:answer )?sheets? (?:wrongly )?"
     r"(?:gives?|says?|marks?|calls?|gets? this wrong)[^.;]*[.;]", "."),
    (r"\bNo printed key exists for this item\.\s*", ""),
    (r"\bThis (?:answer|item) (?:has not changed|is fixed) across[^.]*\.\s*",
     "This answer does not change. "),
    (r"\bA fixed answer across[^.]*\.\s*", "This answer does not change. "),
    (r"\bConfirmed in the [^.]*papers?\.\s*", "This answer does not change. "),
    (r"\bboth the circled \d{4} script and the [A-Za-z]+ paper\b", "every marked version"),
    (r"\bagainst one compiled sheet[^.]*\.", "."),
    (r"\bThe \d{4} red-marked paper takes\b", "The marked answer is"),
    (r"\bIn \d{4} the same question was\b", "The same question is also"),
    (r"\bthe \d{4} wording\b", "another wording"),
    (r"\bin \d{4} and [a-z ]+ in \d{4}\b", "in one year and something else in another"),

    # --- guide and trap-list pointers -------------------------------------
    (r"\s*(?:See|see) (?:section|Guide) \d+(?:\.\d+[a-z]?)?(?: step \d+)?\.", ""),
    (r"\bThat is trap \d+\.\s*", ""),
    (r"\bwhich is trap \d+\b", "which is the standard trap"),
    (r"\bThis is trap \d+:\s*", ""),
    (r"\btrap list \d+\b", "the trap list"),
    (r"\bGuide \d+(?:\.\d+[a-z]?)?\b", "the notes"),
    (r"\bsection \d+(?:\.\d+[a-z]?)?\b", "the notes"),

    # --- leftovers --------------------------------------------------------
    (r"\bany other item in the paper\b", "any other item"),
    (r"\bin the whole paper\b", "anywhere"),
    (r"\bthe printed distractor\b", "the printed wrong option"),
    (r"\bCORRECTED\. The site marks[^.]*\.\s*",
     "Corrected against the lecturer's notes. "),
]

COMPILED = [(re.compile(pattern), replacement) for pattern, replacement in RULES]

TIDY = [
    (re.compile(r"\s+([.,;])"), r"\1"),
    (re.compile(r"([.;])\1+"), r"\1"),
    (re.compile(r"\.\s*;"), "."),
    (re.compile(r"\s{2,}"), " "),
    (re.compile(r",\s*\."), "."),
]

# Nothing may survive that names an option letter as the answer, or cites a
# year, a marking scheme or a guide section.
BANNED = re.compile(
    r"answers? (?:is|was|are) +\*?\*?[A-E]\b"
    r"|\banswer +\*?\*?[A-E]\b"
    r"|\bmarked +\*?\*?[A-E]\b"
    r"|\bpairs? +answers? +[A-E]\b"
    r"|\b(?:19|20)\d{2}\b"
    r"|marking scheme"
    r"|compiled (?:answer )?sheet"
    r"|canvas paper"
    r"|trap list"
    r"|\bGuide \d")


def clean(text):
    for pattern, replacement in COMPILED:
        text = pattern.sub(replacement, text)
    for pattern, replacement in TIDY:
        text = pattern.sub(replacement, text)

    # Anything still carrying a citation is provenance, not reasoning. Drop the
    # sentence. Sentences that carried both were rewritten by the rules above.
    if BANNED.search(text):
        kept = [s for s in re.split(r"(?<=[.])\s+", text)
                if s.strip() and not BANNED.search(s)]
        text = " ".join(kept)

    for pattern, replacement in TIDY:
        text = pattern.sub(replacement, text)
    return text.strip()
