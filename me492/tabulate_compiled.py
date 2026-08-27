# -*- coding: utf-8 -*-
"""Put the data tables back into the 30 calculation questions in compiled.json.

The questions were transcribed from the past papers with the figures folded into
the sentence. The papers print a table instead, and reading the right row off it
is part of the question. This restores the paper's form: preamble, table, then
the single thing being asked.

Idempotent. Running it twice changes nothing.
"""
import io
import json

import calc_tables as T

TARGET = "compiled.json"

# question_number -> (scenario, the bare ask, as the paper words it)
PLAN = {
    197: (T.TOPSY, "Determine the accounts receivable for October."),
    198: (T.TOPSY, "Determine the accounts receivable for November."),
    199: (T.TOPSY, "Determine the accounts receivable for December."),
    200: (T.TOPSY, "Determine the budgeted cash sales for October."),
    201: (T.TOPSY, "Determine the budgeted cash sales for December."),
    202: (T.TOPSY, "Determine the amount of accounts receivable that will appear on the "
                   "company's fourth quarter pro forma balance sheet."),
    203: (T.TOPSY, "Determine the amount of sales revenue that will appear on the company's "
                   "fourth quarter pro forma income statement."),

    204: (T.KANEAPA, "Determine the accounts receivable for November."),
    205: (T.KANEAPA, "Determine the budgeted cash sales for November."),

    206: (T.DANDY, "Determine the accounts receivable for November."),
    207: (T.DANDY, "Determine the amount of accounts receivable that will appear on the "
                   "company's fourth quarter pro forma balance sheet."),
    208: (T.DANDY, "Determine the amount of sales revenue that will appear on the company's "
                   "fourth quarter pro forma income statement."),
    209: (T.DANDY, "Compute the expected increase in sales per month during November and "
                   "December."),

    210: (T.GOLDCOM, "Determine the sales in the fourth quarter for the West Division."),
    211: (T.GOLDCOM, "Determine the amount of sales revenue that will appear on the company's "
                     "fourth quarter pro forma income statement."),

    212: (T.HOKUS, "Determine the sales in the fourth quarter for the Accra District."),
    213: (T.HOKUS, "Determine the amount of sales revenue that will appear on the company's "
                   "fourth quarter pro forma income statement."),

    214: (T.OSAGYEFO, "Compute the total cash available for August."),
    215: (T.OSAGYEFO, "Compute the total cash available for September."),
    216: (T.OSAGYEFO, "Determine the cash shortage for August."),
    217: (T.OSAGYEFO, "Determine the cash surplus for September."),
    218: (T.OSAGYEFO, "Calculate the amount to be borrowed for August."),
    219: (T.OSAGYEFO, "Calculate the amount to be repaid for September."),
    220: (T.OSAGYEFO, "Compute the total amount of interest expense for the third quarter."),

    221: (T.BIRDY_JEWELLERY, "Compute the total cash available for August."),
    222: (T.BIRDY_JEWELLERY, "Compute the total cash available for September."),
    223: (T.BIRDY_JEWELLERY, "Determine the cash surplus for August."),
    224: (T.BIRDY_JEWELLERY, "Calculate the amount to be repaid for September."),
    225: (T.BIRDY_JEWELLERY, "Compute the total amount of interest expense for the third "
                             "quarter."),
    226: (T.BIRDY_JEWELLERY, "Compute the ending cash balance for the month of September."),
}


def main():
    data = json.load(io.open(TARGET, encoding="utf-8"))
    by_number = {q["question_number"]: q for q in data}

    missing = [n for n in PLAN if n not in by_number]
    if missing:
        raise SystemExit("no such question: %s" % missing)

    changed = 0
    for number, (scenario, ask) in PLAN.items():
        q = by_number[number]
        new = T.stem(scenario, ask)
        if q["question_text"] != new:
            q["question_text"] = new
            changed += 1

    # The answer must still be reachable from the table alone.
    for number in PLAN:
        q = by_number[number]
        if q["correct_answer"][0] not in q["options"]:
            raise SystemExit("Q%d lost its answer" % number)
        if "|" not in q["question_text"]:
            raise SystemExit("Q%d has no table" % number)

    json.dump(data, io.open(TARGET, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("%s: %d of %d calculation questions rewritten with their table"
          % (TARGET, changed, len(PLAN)))


if __name__ == "__main__":
    main()
