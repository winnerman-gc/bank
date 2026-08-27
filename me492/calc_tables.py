# -*- coding: utf-8 -*-
"""The data tables for every ME 492 calculation scenario, in the paper's layout.

The exam prints the figures as a table with question marks in the cells you must
fill. Reading the right row is part of the task. Eleven of these tables are
transcribed from the past papers, through site-raw-228.json. Three are built for
the scenarios invented for the AI set, in the same layout.

Each entry is (preamble, table). The preamble is the sentence block above the
table. The table is markdown; index.html renders it as a real table.
"""

C = "GH¢"

# --------------------------------------------------------------------------
# Type 1: sales budget and schedule of cash receipts
# --------------------------------------------------------------------------
TOPSY = (
    "The Topsy Turvy Company Ltd sells furniture and other wood products. Its budget "
    "director has prepared the sales budget that follows. The company has a beginning "
    "balance of $40,000 in accounts receivable on October 1. The Topsy Turvy Company Ltd "
    "normally collects 100 percent of accounts receivable in the month following the month "
    "of sale. All computations are rounded to the nearest whole dollar.",
    """| Sales Budget | October $ | November $ | December $ |
| :--- | :--- | :--- | :--- |
| Cash sales | 15,000 | 17,250 | 19,838 |
| Sales on account | 45,000 | 51,750 | 59,513 |
| Total budgeted sales | 60,000 | 69,000 | 79,351 |
| | | | |
| **Schedule of Cash Receipts** | | | |
| Current month's cash sales | ? | ? | ? |
| Collections from accounts receivable | ? | ? | ? |
| Total Budgeted Collections | 55,000 | 62,250 | 71,588 |""")

KANEAPA = (
    "Kaneapa Company Ltd sells lamps and other lighting fixtures. Its budget director has "
    "prepared the sales budget that follows. The company had a beginning balance of $60,000 "
    "in accounts receivable on October 1. The Kaneapa Company normally collects 100 percent "
    "of accounts receivable in the month following the month of sale.",
    """| Sales Budget | October $ | November $ | December $ |
| :--- | :--- | :--- | :--- |
| Cash sales | 20,000 | 22,000 | 24,200 |
| Sales on account | 45,000 | 49,500 | 54,450 |
| Total budgeted sales | 65,000 | 71,500 | 78,650 |
| | | | |
| **Schedule of Cash Receipts** | | | |
| Current month's cash sales | ? | ? | ? |
| Collections from accounts receivable | ? | ? | ? |
| Total Budgeted Collections | 80,000 | 67,000 | 73,700 |""")

DANDY = (
    "Dandy Electronics Company Ltd is a venture that will be selling computers and computer "
    "accessories. The company's budget director has prepared the sales budget that follows. "
    "The company has no accounts receivable on October 1. Dandy Electronics Company Ltd will "
    "normally be collecting 100 percent of accounts receivable in the month following the "
    "month of sale. All computations are rounded to the nearest whole Ghana Cedi (" + C + ").",
    """| Sales Budget | October """ + C + """ | November """ + C + """ | December """ + C + """ |
| :--- | :--- | :--- | :--- |
| Cash sales | 787,500 | 984,375 | 1,230,469 |
| Sales on account | 337,500 | 421,875 | 527,344 |
| Total budgeted sales | 1,125,000 | 1,406,250 | 1,757,813 |
| | | | |
| **Schedule of Cash Receipts** | | | |
| Current month's cash sales | ? | ? | ? |
| Collections from accounts receivable | ? | ? | ? |
| Total Budgeted Collections | 787,500 | 1,321,875 | 1,652,344 |""")

LOVY = (
    "The Lovy-Dovy Company Ltd sells flowers (roses). Its budget director has prepared the "
    "sales budget that follows. The company had a beginning balance of " + C + "115,385 in "
    "accounts receivable on October 1. The Lovy-Dovy Company Ltd normally collects 100 "
    "percent of accounts receivable in the month following the month of sale. All "
    "computations are rounded to the nearest whole Ghana Cedi (" + C + ").",
    """| Sales Budget | October """ + C + """ | November """ + C + """ | December """ + C + """ |
| :--- | :--- | :--- | :--- |
| Cash sales | 30,000 | 39,000 | 50,700 |
| Sales on account | 150,000 | 195,000 | 253,500 |
| Total budgeted sales | 180,000 | 234,000 | 302,200 |
| | | | |
| **Schedule of Cash Receipts** | | | |
| Current month's cash sales | ? | ? | ? |
| Collections from accounts receivable | ? | ? | ? |
| Total Budgeted Collections | 143,385 | 189,000 | 245,700 |""")

BIRDY_CLOTHING = (
    "Birdy-Birdy Clothing Company Ltd is a venture that will be selling designer clothing. "
    "The company's budget director has prepared the sales budget that follows. The company "
    "has no accounts receivable on October 1. Birdy-Birdy Clothing Company Ltd will normally "
    "be collecting 100 percent of accounts receivable in the month following the month of "
    "sale. All computations are rounded to the nearest whole Ghana Cedi (" + C + ").",
    """| Sales Budget | October """ + C + """ | November """ + C + """ | December """ + C + """ |
| :--- | :--- | :--- | :--- |
| Cash sales | 4,800,000 | 6,000,000 | 7,500,000 |
| Sales on account | 3,200,000 | 4,000,000 | 5,000,000 |
| Total budgeted sales | 8,000,000 | 10,000,000 | 12,500,000 |
| | | | |
| **Schedule of Cash Receipts** | | | |
| Current month's cash sales | ? | ? | ? |
| Collections from accounts receivable | ? | ? | ? |
| Total Budgeted Collections | 4,800,000 | 9,200,000 | 11,500,000 |""")

NKWANTA = (
    "Nkwanta Hardware Ltd sells building materials. Its budget director has prepared the "
    "sales budget that follows. The company had a beginning balance of " + C + "32,000 in "
    "accounts receivable on April 1. Nkwanta Hardware Ltd normally collects 100 percent of "
    "accounts receivable in the month following the month of sale. All computations are "
    "rounded to the nearest whole Ghana Cedi (" + C + ").",
    """| Sales Budget | April """ + C + """ | May """ + C + """ | June """ + C + """ |
| :--- | :--- | :--- | :--- |
| Cash sales | 24,000 | 28,800 | 34,560 |
| Sales on account | 36,000 | 43,200 | 51,840 |
| Total budgeted sales | 60,000 | 72,000 | 86,400 |
| | | | |
| **Schedule of Cash Receipts** | | | |
| Current month's cash sales | ? | ? | ? |
| Collections from accounts receivable | ? | ? | ? |
| Total Budgeted Collections | 56,000 | 64,800 | 77,760 |""")

# --------------------------------------------------------------------------
# Type 2: divisional growth to the fourth quarter
# --------------------------------------------------------------------------
GOLDCOM = (
    "GoldCom Corporation, which has three divisions, is preparing its sales budget. However, "
    "each division expects a different growth rate because the economic conditions vary in "
    "different regions of the country. The growth expectations per quarter are 2 percent for "
    "East Division, 3 percent for West Division and 5 percent for South Division.",
    """| Current Quarter | First Quarter ($) | Second Quarter ($) | Third Quarter ($) | Fourth Quarter ($) |
| :--- | :--- | :--- | :--- | :--- |
| East Division | 520,000 | ? | ? | ? |
| West Division | 740,000 | ? | ? | ? |
| South Division | 340,000 | ? | ? | ? |""")

HOKUS = (
    "Hokus Pokus Company Ltd, which has three districts, is preparing its sales budget. "
    "However, each district expects a different growth rate because the economic conditions "
    "vary in different regions of the country. The growth expectations per quarter are 4 "
    "percent for Kumasi District, 5 percent for Accra District and 10 percent for Cape Coast "
    "District. All computations are rounded to the nearest whole dollar.",
    """| Current Quarter | First Quarter ($) | Second Quarter ($) | Third Quarter ($) | Fourth Quarter ($) |
| :--- | :--- | :--- | :--- | :--- |
| Kumasi District | 650,000 | ? | ? | ? |
| Accra District | 880,000 | ? | ? | ? |
| Cape Coast District | 420,000 | ? | ? | ? |""")

ASHANTI = (
    "Ashanti Foods Company Ltd, which has three divisions, is preparing its sales budget. "
    "However, each division expects a different growth rate because the economic conditions "
    "vary in different regions of the country. The growth expectations per quarter are 2 "
    "percent for Tamale Division, 4 percent for Takoradi Division and 10 percent for Ho "
    "Division. All computations are rounded to the nearest whole Ghana Cedi (" + C + ").",
    """| Current Quarter | First Quarter (""" + C + """) | Second Quarter (""" + C + """) | Third Quarter (""" + C + """) | Fourth Quarter (""" + C + """) |
| :--- | :--- | :--- | :--- | :--- |
| Tamale Division | 480,000 | ? | ? | ? |
| Takoradi Division | 620,000 | ? | ? | ? |
| Ho Division | 350,000 | ? | ? | ? |""")

# --------------------------------------------------------------------------
# Type 3: the cash budget with borrowing and interest
# --------------------------------------------------------------------------
OSAGYEFO = (
    "The Finance Officer for Osagyefo Clothing Company Ltd prepared the following cash "
    "budget. Osagyefo Clothing desires to maintain a cash cushion of " + C + "40,000 before "
    "the interest payment at the end of each month. Funds are assumed to be borrowed and "
    "repaid on the first day of each month. Interest is charged at the rate of 5 percent per "
    "month. The company had a beginning cash balance of " + C + "42,500. All computations are "
    "rounded to the nearest whole Ghana Cedi (" + C + ").",
    """| Cash Budget | July """ + C + """ | August """ + C + """ | September """ + C + """ |
| :--- | :--- | :--- | :--- |
| Beginning cash balance | 42,500 | ? | ? |
| Cash receipts | 230,000 | 486,000 | 749,000 |
| Total cash available | 272,500 | ? | ? |
| | | | |
| **Disbursements** | | | |
| Inventory purchases | 93,000 | 409,100 | 447,250 |
| Selling & Administrative expenses | 259,500 | 130,900 | 184,750 |
| Total budgeted disbursements | 352,500 | ? | ? |
| | | | |
| **Cash needs** | | | |
| Shortage (surplus) of cash | 80,000 | ? | ? |
| Cash cushion | 40,000 | 40,000 | 40,000 |
| | | | |
| **Financing activity** | | | |
| Borrowing (repayment) | 120,000 | ? | ? |
| Interest expense at 5 percent per month | (6,000) | ? | ? |
| Ending cash balance | 34,000 | ? | ? |""")

BIRDY_JEWELLERY = (
    "The accountant for Birdy-Birdy's Jewellery Shop prepared the following cash budget. "
    "Birdy-Birdy desires to maintain a cash cushion of " + C + "9,000 before the interest "
    "payment at the end of each month. Funds are assumed to be borrowed and repaid on the "
    "first day of each month. Interest is charged at the rate of 2 percent per month. The "
    "company had a beginning cash balance of " + C + "7,500.",
    """| Cash Budget | July """ + C + """ | August """ + C + """ | September """ + C + """ |
| :--- | :--- | :--- | :--- |
| Beginning cash balance | 7,500 | ? | ? |
| Cash receipts | 50,000 | 180,000 | 216,000 |
| Total cash available | 57,500 | ? | ? |
| | | | |
| **Disbursements** | | | |
| Inventory purchases | 110,000 | 140,800 | 164,736 |
| Selling & Administrative expenses | 31,560 | 33,600 | 35,280 |
| Total budgeted disbursements | 141,560 | ? | ? |
| | | | |
| **Cash needs** | | | |
| Shortage (surplus) of cash | 84,060 | ? | ? |
| Cash cushion | 9,000 | 9,000 | 9,000 |
| | | | |
| **Financing activity** | | | |
| Borrowing (repayment) | 93,060 | ? | ? |
| Interest expense at 2 percent per month | (1,861) | ? | ? |
| Ending cash balance | 7,139 | 7,214 | ? |""")

SWEETIE = (
    "The Finance Director for Sweetie-Nitie Jewellery Company Ltd prepared the following cash "
    "budget. Sweetie-Nitie Jewellery Company Ltd desires to maintain a cash cushion of "
    + C + "120,000 before the interest payment at the end of each month. Funds are assumed to "
    "be borrowed and repaid on the first day of each month. Interest is charged at the rate "
    "of 10 percent per month. The company had a beginning cash balance of " + C + "0. All "
    "computations are rounded to the nearest whole Ghana Cedi (" + C + ").",
    """| Cash Budget | July """ + C + """ | August """ + C + """ | September """ + C + """ |
| :--- | :--- | :--- | :--- |
| Beginning cash balance | 0 | ? | ? |
| Cash receipts | 2,500,000 | 3,600,000 | 4,200,000 |
| Total cash available | 2,500,000 | ? | ? |
| | | | |
| **Disbursements** | | | |
| Inventory purchases | 1,800,000 | 2,000,000 | 2,200,000 |
| Selling & Administrative expenses | 1,300,000 | 1,560,000 | 1,800,000 |
| Total budgeted disbursements | 3,100,000 | ? | ? |
| | | | |
| **Cash needs** | | | |
| Shortage (surplus) of cash | 600,000 | ? | ? |
| Cash cushion | 120,000 | 120,000 | 120,000 |
| | | | |
| **Financing activity** | | | |
| Borrowing (repayment) | 720,000 | ? | ? |
| Interest expense at 10 percent per month | (72,000) | ? | ? |
| Ending cash balance | 48,000 | 44,800 | ? |""")

MERCY = (
    "The accountant for Mercy's Bookshop prepared the following cash budget. Mercy's desires "
    "to maintain a cash cushion of " + C + "7,000 before the interest payment at the end of "
    "each month. Funds are assumed to be borrowed and repaid on the first day of each month. "
    "Interest is charged at the rate of 4.35 percent per month. The company had a beginning "
    "cash balance of " + C + "9,000.",
    """| Cash Budget | July """ + C + """ | August """ + C + """ | September """ + C + """ |
| :--- | :--- | :--- | :--- |
| Beginning cash balance | 9,000 | ? | ? |
| Cash receipts | 80,000 | 94,000 | 112,800 |
| Total cash available | 89,000 | ? | ? |
| | | | |
| **Disbursements** | | | |
| Inventory purchases | 76,763 | 67,115 | 82,076 |
| Selling & Administrative expenses | 22,250 | 27,280 | 28,216 |
| Total budgeted disbursements | 99,013 | ? | ? |
| | | | |
| **Cash needs** | | | |
| Shortage (surplus) of cash | 10,013 | ? | ? |
| Cash cushion | 7,000 | 7,000 | 7,000 |
| | | | |
| **Financing activity** | | | |
| Borrowing (repayment) | 17,013 | ? | ? |
| Interest expense at 4.35 percent per month | (740) | ? | ? |
| Ending cash balance | 6,260 | 6,211 | 6,285 |""")

MAMPONG = (
    "The Finance Officer for Mampong Foods Ltd prepared the following cash budget. Mampong "
    "Foods desires to maintain a cash cushion of " + C + "10,000 before the interest payment "
    "at the end of each month. Funds are assumed to be borrowed and repaid on the first day "
    "of each month. Interest is charged at the rate of 3 percent per month. The company had "
    "a beginning cash balance of " + C + "12,000. All computations are rounded to the nearest "
    "whole Ghana Cedi (" + C + ").",
    """| Cash Budget | January """ + C + """ | February """ + C + """ | March """ + C + """ |
| :--- | :--- | :--- | :--- |
| Beginning cash balance | 12,000 | ? | ? |
| Cash receipts | 60,000 | 140,000 | 165,000 |
| Total cash available | 72,000 | ? | ? |
| | | | |
| **Disbursements** | | | |
| Inventory purchases | 90,000 | 78,000 | 85,000 |
| Selling & Administrative expenses | 55,000 | 46,000 | 52,000 |
| Total budgeted disbursements | 145,000 | ? | ? |
| | | | |
| **Cash needs** | | | |
| Shortage (surplus) of cash | 73,000 | ? | ? |
| Cash cushion | 10,000 | 10,000 | 10,000 |
| | | | |
| **Financing activity** | | | |
| Borrowing (repayment) | 83,000 | ? | ? |
| Interest expense at 3 percent per month | (2,490) | ? | ? |
| Ending cash balance | 7,510 | ? | ? |""")


def stem(scenario, ask):
    """Preamble, then the table, then the one thing being asked."""
    preamble, table = scenario
    return "%s\n\n%s\n\n%s" % (preamble, table, ask)
