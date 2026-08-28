# -*- coding: utf-8 -*-
"""Add a memory hook to every question, and full workings to the calculations.

Two problems this fixes.

1. The calculation explanations were written when the figures sat in the
   sentence. Now that the stem carries the paper's table, several of them
   asserted a number without deriving it. Q215 said "31,000 + 749,000" without
   saying where 31,000 came from. Every one of the 30 is now worked from the
   table.

2. Explanations averaged 167 characters. That tells you the answer but leaves
   nothing to carry into the hall. Each question now also gets a "hook": the
   rule in shorthand, with the trap named. Hooks are shared by topic, so the
   same wording repeats across a block. That repetition is the point.

Run after the two builders. build_all.py does the whole chain in order.
Idempotent: it rewrites the hook and the listed explanations every time.
"""
import io
import json
import re

C = "GH¢"
FILES = ("compiled.json", "ai-generated-100.json", "site-extracted-48.json")

# --------------------------------------------------------------------------
# Memory hooks, keyed by the guide section named in the question's source.
# Longest key wins, so "13.3" beats "13".
# --------------------------------------------------------------------------
HOOKS = {
    "3": "Segment you own = NICHE. Time you have = WINDOW. Who you sell to = CUSTOMER SCENARIO. "
         "Anyone affected = STAKEHOLDER. Learn these as text; their letters move every year.",

    "4": "Entrepreneur = initiative + risk + something new. Small business person = income substitution.",
    "4.1": "Cantillon ALLOCATES resources and seeks higher yields. Adam Smith FORESEES demand. "
           "Say COMBINES the two and adds insight into society's needs. Menger CONVERTS resources "
           "into value. Schumpeter DESTROYS creatively. Drucker takes OPPORTUNITIES. "
           "Creative destruction is always Schumpeter, never Menger.",
    "4.2": "Five sources of change: Science, Process, Industry, Market, Demographics. "
           "Find the phrase that is not on that list. That is the false statement.",
    "4.3": "Vision, Commitment, Persistence. Any option with INCOME SUBSTITUTION is the small "
           "business person, never the entrepreneur.",
    "4.4": "Small by their NATURE and by the OWNER'S INTENTION. Not by legal contracts.",
    "4.5": "The myths are misfits, born not made, and the first flash of genius. "
           "Working hard for your luck is the TRUTH, not a myth.",
    "4.6": "Team, Plan, Timing, Ideology. A fat bank account is not a success factor.",
    "4.7": "Direction of the economy, Technology leaps, Reallocation of resources. Usually all three.",
    "4.8": "Intrapreneur = INTRA-COMPANY entrepreneur. They risk TIME and CAREER. "
           "They never risk their own MONEY: the company carries that.",
    "4.9": "Failure comes from INEXPERIENCE. Starting from scratch is the HIGHER risk. "
           "Entrepreneurs form SERVICE businesses and have a high internal locus of control.",
    "4.10": "entreprendre = to undertake. Undertakers, contractors, builders. "
            "NOT discovered by business students. That clause is what makes the statement false.",

    "5": "Creativity is the seed. Innovation is the process.",
    "5.1": "Creativity = an ABILITY. Innovation = a PROCESS. Invention = the verified RESULT. "
           "Creativity is a prerequisite for innovation, never the other way round.",
    "5.2": "G-P-I-I-V: Germination, Preparation, Incubation, Illumination, Verification. "
           "CONSCIOUS search = Preparation. SUBCONSCIOUS = Incubation. FLASH = Illumination. "
           "TEST for value = Verification. Flash and test are the pair they swap.",
    "5.3": "Innovation process = Analytical planning, Organising resources, Implementation, "
           "Commercial application. Germination, preparation and verification belong to the "
           "CREATIVE process. Innovation is not invention.",
    "5.4": "WINDOW = the time you have. CORRIDOR = where you already stand. "
           "Corridor principle: you start near your old career, so you move first when a window opens.",
    "5.5": "Creative source, Champion, Sponsor. Never the inventor, never the investor, "
           "never the promoter.",
    "5.6": "No criticism, high quantity, fixed period. Nothing is judged or discarded inside "
           "the session. Any option that discards ideas is false.",
    "5.7": "A mind map starts at your own interest, spreads to products and markets, "
           "then follows one path down.",
    "5.8": "Most new products are LOW-tech: easy to make, quick to market, cheap to kill, "
           "because patents cannot protect them. High versus mid tech is a matter of PERCEPTION.",

    "6": "The entrepreneur writes the plan. Lenders and investors read it.",
    "6.1": "The ENTREPRENEUR writes it, in consultation with specialists. Never a consultant, "
           "never a financial expert. Specialists know finance, not how to run a business.",
    "6.2": "A feasibility plan integrates operations, marketing, finance and HR, and asks one "
           "question: can this venture be expected to succeed?",
    "6.3": "Three perspectives: Entrepreneur, Marketing, Investor.",
    "6.4": "Check market/finance/operations, concept/team, and goals/finance/product. All three.",
    "6.5": "MARKET POTENTIAL first. Nothing else matters if there is no market.",
    "6.6": "The executive summary is written LAST and read FIRST. Two or three pages, "
           "concise and convincing.",
    "6.7": "Cover page: name, address, money needed, contacts, brief concept, and the "
           "CONFIDENTIALITY clause. When one answer is wanted, take confidentiality.",
    "6.8": "Executive Summary, or Market research and analysis. NEVER Abstract, Literature "
           "Review, Conclusions or Product design. Those come from academic reports.",
    "6.9": "Location, Competitors and industry trends, External uncontrollables. All three.",
    "6.10": "Operations section: leadership and team, facilities and inventory, operations and "
            "human resources.",
    "6.11": "Appendix = resumes, layouts, agreements. Supporting paper only.",
    "6.12": "The plan is primarily for LENDERS AND INVESTORS. Not for running the business day to day.",
    "6.13": "Plans go out of date because the MARKET AND INDUSTRY change. That is the single "
            "best answer, even though team, location and concept are also on the list.",
    "6.14": "Plans fail on unreasonable goals, no total commitment, and no experience. All three.",
    "6.15": "Planning never ends: four stages, each needs its own plan. On the because pair, answer A.",
    "6.16": "Counter loose copies with a NON-DISCLOSURE statement. A Disclosure Document is a "
            "patent office filing and is a different instrument.",

    "7": "Pre-start-up, Start-up, Early growth, Later growth.",
    "7.1": "Pre-start-up = assembling resources. Start-up = REALITY SHOCK, the real world. "
           "Early growth = growing healthily. Later growth = established and professionally managed.",
    "7.2": "Pre-start-up: product/market survey, concept defined, implementation. "
           "A competitive analysis BEFORE the doors open is pre-start-up work.",
    "7.3": "Two benchmarks: meet operating objectives, and position for long-term growth. "
           "A fixed answer across 2007, 2015 and 2020.",
    "7.4": "Start-up objectives: Sales, Revenue, Growth, Position.",
    "7.5": "Measure start-up progress with a 12-MONTH schedule.",
    "7.6": "Cut the burden by planning ASSETS carefully. Not by cutting staff, capacity or salaries.",
    "7.7": "Pre-start-up financial planning need not be extensive, but it must rest on "
           "VERIFIABLE information.",

    "8": "Research gathers the information. The plan uses it.",
    "8.1": "MARKET RESEARCH GATHERS THE INFORMATION. THE MARKET PLAN USES IT in a strategy to "
           "attract customers. This sentence appears almost every year. Learn it word for word.",
    "8.2": "Identify customers, evaluate markets, analyse competitors, describe ASSUMPTIONS. "
           "The distractor is the one that drops assumptions.",
    "8.3": "The market plan answers WHO the customer is and WHERE he or she is.",
    "8.4": "Product, Price, Place (distribution), Promotion. Take the FULLEST option printed. "
           "If all of the above is offered, take it.",
    "8.5": "A niche is a defined segment that sets POSITIONING. On the because pair about "
           "segmentation, answer A.",
    "8.6": "Good market research produces a WELL DEFINED SALES FORECAST. Only that. "
           "Not a revenue estimate, not investment needs.",
    "8.7": "Distribution = getting goods to market + locating services. Channels are consumer, "
           "industrial and service. Taking materials through production is MANUFACTURING.",
    "8.8": "Product covers the business concept, the physical object with its packaging and brand, "
           "and the physical attributes. All three layers.",
    "8.9": "Start-up advertising gets someone THROUGH YOUR DOOR. Integrated Marketing "
           "Communications sends ONE focused message, not an assortment of messages.",
    "8.10": "The marketing plan sets how you compete and operate. It is implemented through a "
            "marketing PROGRAM. Take marketing activities only if program is not printed.",
    "8.11": "Prices send perceptual messages to consumers. On that because pair, answer A.",
    "8.12": "Timing = when the product is introduced, priced, distributed and promoted. "
            "On that because pair, answer A.",
    "8.13": "Customer profile: age and sex, income status, where the customer base is. All three.",
    "8.14": "Research AFTER the doors open is COMPETITIVE ANALYSIS.",

    "9": "A patent is a government grant of a property right to an inventor.",
    "9.1": "A patent SEARCH asks whether the creation already exists and is still protected. "
           "A PLANT patent covers hybrid roses and food grains. The 17 years figure is the trap.",
    "9.2": "A Disclosure Document is a statement of INTENT to patent. It matters when an "
           "infringement occurs. It is not a patent.",
    "9.3": "A trademark may be a sound, a word, a symbol, a design or a slogan, and it lasts "
           "indefinitely. Take all of the above.",
    "9.4": "Product liability: make SAFE products and WARN of hazards. Zero defects is not "
           "achievable, so it is never the protection.",
    "9.5": "Contracts: describe the transaction, get signatures, and remember oral agreements "
           "are invalid over one year. All three.",

    "10": "Sole proprietorship, partnership, corporation.",
    "10.1": "Structure first, then JOB ANALYSIS to find the activities, then job description, "
            "then job specification, then training.",
    "10.2": "Three criteria: Preferences of the entrepreneur, Profile of the enterprise, "
            "Pros and cons of the entity.",
    "10.4": "Sole proprietorship: main advantage AUTONOMY, main disadvantage UNLIMITED LIABILITY. "
            "It dies with the owner. It has no expanded network and no strong borrowing profile.",
    "10.5": "GENERAL partner manages and carries unlimited liability. LIMITED partner invests and "
            "cannot manage. MLP trades like a corporation but is taxed like a partnership. "
            "Disadvantages: unlimited joint and several liability, and death or withdrawal ends it. "
            "Limited access to resources is NOT a partnership disadvantage.",
    "10.6": "A corporation is an ARTIFICIAL PERSON: perpetual life, limited liability, "
            "double taxation. Shareholders elect the Board, the Board hires Officers, "
            "Officers pick Managers.",
    "10.7": "A formal board is required by law only for INCORPORATED companies. Membership 5 to 9. "
            "Directors give a social network, handle disturbances and mentor.",
    "10.8": "The entrepreneurial team builds the organisation, gives identity, handles operations "
            "and guides the venture through change.",
    "10.9": "FRANCHISOR originates the system and supplies the package for a fee and royalties. "
            "FRANCHISEE acquires. FRANCHISE is the system the contract creates.",
    "10.10": "Society wants VALUE ADDED products and services. Investors want a RETURN. "
             "Lenders want cash flow, collateral and equity contribution.",

    "11": "Fixed, working and liquid capital. Debt needs collateral. Equity gives ownership.",
    "11.1": "FIXED = buildings, fixtures, equipment. WORKING = day to day running costs. "
            "LIQUID = emergency reserve in cash or securities. All three are asked separately.",
    "11.2": "SHORT term, under 1 year, funds WORKING capital and is self liquidating. "
            "INTERMEDIATE, 1 to 5 years, buys fixtures and equipment. "
            "LONG term, over 5 years, buys BUILDINGS AND LAND.",
    "11.3": "DEBT is asset-based, NEEDS collateral, and uses 50 to 80 percent of the asset value. "
            "EQUITY needs NO collateral and gives an OWNERSHIP position. "
            "Low interest rates favour DEBT, because you keep more of the company.",
    "11.4": "INTERNAL: profits, asset sales, working capital cuts, faster collection. "
            "EXTERNAL: personal funds, family, banks, venture capital, and GOVERNMENT GRANTS.",
    "11.5": "PERSONAL FUNDS are cheapest and are essential to attracting anyone else. "
            "COMMERCIAL BANKS are the most used short-term source when collateral exists. "
            "VENTURE CAPITAL is for higher risks such as start-ups. Money portability is invented.",
    "11.6": "RECEIVABLE is money coming IN, PAYABLE is money going OUT. Net worth = invested plus "
            "retained. Retained earnings = accumulated profits. Covenants = loan restrictions. "
            "Cash flow = receipts minus disbursements.",

    "12": "Operating, capital and financial statement budgets. One year. Start with sales.",
    "12.1": "STRATEGIC planning is long term and picks the niche. CAPITAL budgeting decides buy "
            "or lease. OPERATIONS budgeting is short term and the MOST SPECIFIC.",
    "12.2": "Master budget = OPERATING + CAPITAL + FINANCIAL STATEMENT budgets, over ONE YEAR. "
            "It begins with the operating budgets, and those begin with the SALES FORECAST. "
            "Continuous budgeting rolls 12 months. Expenditure over one year = CAPITAL budgets, "
            "never strategic budgets.",
    "12.3": "INCOME statement = projected PROFITS. BALANCE sheet = ASSETS, LIABILITIES, EQUITY. "
            "CASH FLOW = accumulations minus disbursements. The balance sheet is the one that "
            "summarises assets, liabilities and equity.",
    "12.4": "All forecasts rest on assumptions, because future outcomes cannot be predicted. "
            "On that because pair, answer A.",

    "13": "Three calculation types only. Learn the method, never the numbers.",
    "13.1": "AR for a month = LAST month's credit sales. October uses the OPENING balance. "
            "Cash sales are read straight off the table. Year-end AR on the balance sheet = "
            "DECEMBER'S CREDIT sales, not December total. Revenue = sum of TOTAL budgeted sales.",
    "13.2": "First quarter to fourth quarter is THREE steps. CUBE the multiplier: (1+g)^3. "
            "Raising it to the fourth power lands you exactly on the printed distractor.",
    "13.3": "Beginning = last month's ending. Available = beginning + receipts. "
            "SHORTAGE: borrow = shortage + cushion. "
            "SURPLUS bigger than the cushion: repay = surplus - cushion. "
            "SURPLUS SMALLER than the cushion: BORROW the difference. "
            "Interest is charged on the CUMULATIVE loan balance, not on the new borrowing.",

    "14": "Judge S1 alone, then S2 alone. Only if BOTH are true, ask whether S2 explains S1. "
          "Most answers are A. In the whole bank, 'first false, second true' has never been correct.",
    "15": "All three is correct about 41 percent of the time. Statement iii sits in the answer "
          "81 percent of the time, statement ii only 63 percent. Doubt ii first.",
    "16": "Asset-based = DEBT. Primary client specs = CUSTOMER SCENARIO. Over one year = CAPITAL "
          "budgets. Assets, liabilities and equity = BALANCE sheet. Creative destruction = SCHUMPETER.",
}

# Questions with no guide section in the source: match on the stem instead.
# Order matters. The first pattern that matches wins.
TEXT_HOOKS = [
    (r"consider the two statements|because s2|\bs1:",
     HOOKS["14"]),
    (r"entreprendre|undertaker|soldiers of fortune",
     "entreprendre = to undertake. Undertakers, contractors, builders, merchants. "
     "The false version adds 'discovered by business students'."),
    (r"concept of entrepreneurship",
     "The concept gave enterprise a NEW DIRECTION and has been around a LONG TIME. "
     "It has not 'just been discovered'. Cantillon wrote in the 18th century."),
    (r"sources of change|shop changes",
     "Five sources of change: Science, Process, Industry, Market, Demographics. "
     "Find the phrase that is not on the list."),
    (r"\bmyth",
     "The myths are misfits, born not made, and the first flash of genius. "
     "Hard work is the truth, not a myth."),
    (r"technological innovation|creative source|champion|sponsor",
     HOOKS["5.5"]),
    (r"directors of new ventures|board of directors|board of advisors",
     HOOKS["10.7"]),
    (r"solvency ratio|current ratio|debt to equity",
     "Long-term SOLVENCY asks whether the venture can meet debt over years, so it compares "
     "DEBT against EQUITY or assets. Liquidity ratios such as the current ratio are short term."),
    (r"pro forma balance sheet|assets, liabilities",
     HOOKS["12.3"]),
    (r"resources expected to produce",
     "Resources expected to produce current and future benefits are ASSETS. "
     "A budget plans, a financial statement reports, an asset is the resource itself."),
    (r"estimated income and expenses|formal plan expressed in numerical|administration plans",
     "A BUDGET is a formal plan in numerical terms, a statement of estimated income and "
     "expenses over a set period. A financial statement reports what HAPPENED. "
     "A budget plans what SHOULD happen."),
    (r"entrepreneurs are\b",
     HOOKS["4.9"]),
]

DEFAULT_HOOK = ("Answer by TEXT, never by letter. The options are reshuffled every year, "
                "and the i/ii/iii key has been printed both ways.")

# --------------------------------------------------------------------------
# Full workings for the 30 calculation questions in compiled.json.
# Each one is derived from the table now printed in the stem.
# --------------------------------------------------------------------------
TOPSY = ("Topsy Turvy, from the table: cash sales 15,000 / 17,250 / 19,838, "
         "sales on account 45,000 / 51,750 / 59,513, opening receivables $40,000. ")
KANEAPA = ("Kaneapa, from the table: cash sales 20,000 / 22,000 / 24,200, "
           "sales on account 45,000 / 49,500 / 54,450, opening receivables $60,000. ")

CALC = {
197: TOPSY + "October is the only month that uses the OPENING balance, because there are no "
     "earlier credit sales to collect. Answer $40,000. Check it on the collections row: "
     "15,000 cash + 40,000 collected = $55,000, exactly what the table prints. "
     "The trap is $45,000, which is October's own credit sales. Those are collected in NOVEMBER.",
198: TOPSY + "November collects OCTOBER's sales on account: $45,000. Check the collections row: "
     "17,250 cash + 45,000 = $62,250, which the table prints. "
     "The trap is $51,750, November's own credit sales, which are not collected until December.",
199: TOPSY + "December collects NOVEMBER's sales on account: $51,750. Check: "
     "19,838 cash + 51,750 = $71,588, the printed figure. "
     "Always take the row above the month you are asked about.",
200: TOPSY + "This is a free mark. Read the cash sales row, October column: $15,000. "
     "No arithmetic at all. Do not confuse it with total budgeted sales of $60,000 or with "
     "total collections of $55,000.",
201: TOPSY + "Read the cash sales row, December column: $19,838. "
     "The neighbouring traps are $59,513 (December CREDIT sales) and $79,351 (December TOTAL sales).",
202: TOPSY + "Year-end receivables are what is still owed on 31 December, so they are DECEMBER'S "
     "CREDIT sales alone: $59,513. Not December total sales ($79,351), not the sum of the "
     "quarter's credit sales ($156,263). Nothing collected in January has happened yet.",
203: TOPSY + "The income statement uses TOTAL sales, cash and credit together: "
     "60,000 + 69,000 + 79,351 = $208,351. Do not use the collections row: collections are cash "
     "movements, and the income statement records sales as they are made.",

204: KANEAPA + "November collects OCTOBER's sales on account: $45,000. "
     "Check: 22,000 cash + 45,000 = $67,000, which the table prints. "
     "The opening $60,000 belongs to October, not November.",
205: KANEAPA + "Read the cash sales row, November column: $22,000. A free mark. "
     "$71,500 is November TOTAL sales and $49,500 is November CREDIT sales.",

206: "Dandy, from the table: sales on account 337,500 / 421,875 / 527,344, and no receivables on "
     "1 October. November collects OCTOBER's credit sales: " + C + "337,500. "
     "Check it against the collections row: 1,321,875 - 984,375 cash = 337,500. "
     "Note the stem says the company collects 30 percent in the following month while the table "
     "shows 100 percent. TRUST THE TABLE. The collections row proves it.",
207: "Dandy: year-end receivables are DECEMBER'S credit sales alone, " + C + "527,344. "
     "Not December total sales of " + C + "1,757,813, and not the sum of the quarter.",
208: "Dandy: add the total budgeted sales row: 1,125,000 + 1,406,250 + 1,757,813 = "
     + C + "4,289,063. Total sales, not collections.",
209: "Dandy: divide one month's total sales by the month before. "
     "1,406,250 / 1,125,000 = 1.25, so a 25 percent increase. "
     "Confirm on the next pair: 1,757,813 / 1,406,250 = 1.25 as well. "
     "The same 25 percent appears in the cash and credit rows, because both grow together.",

210: "GoldCom: the first quarter is given and you want the fourth, so there are THREE growth "
     "steps, not four. West grows at 3 percent: 740,000 x 1.03^3 = 740,000 x 1.092727 = $808,618. "
     "Using the fourth power gives $832,877, which is why that option is printed.",
211: "GoldCom: grow each division by three steps, then add. "
     "East 520,000 x 1.02^3 = 551,828. West 740,000 x 1.03^3 = 808,618. "
     "South 340,000 x 1.05^3 = 393,593. Total $1,754,039. "
     "Worth memorising: 1.02^3 = 1.061208, 1.03^3 = 1.092727, 1.05^3 = 1.157625.",
212: "Hokus Pokus: three steps from first quarter to fourth. Accra grows at 5 percent: "
     "880,000 x 1.05^3 = 880,000 x 1.157625 = $1,018,710. "
     "The fourth power gives $1,069,645, the printed trap.",
213: "Hokus Pokus: Kumasi 650,000 x 1.04^3 = 731,162. Accra 880,000 x 1.05^3 = 1,018,710. "
     "Cape Coast 420,000 x 1.10^3 = 559,020. Total $2,308,892. "
     "Useful multipliers: 1.04^3 = 1.124864, 1.10^3 = 1.331.",

214: "Osagyefo: total cash available = beginning balance + cash receipts, and the beginning "
     "balance is always LAST month's ending balance. The table prints July's ending as 34,000, "
     "so August = 34,000 + 486,000 = " + C + "520,000. The cushion never enters this line. "
     "If you want to prove the 34,000: July available 272,500, disbursements 352,500, "
     "shortage 80,000, borrowing 80,000 + 40,000 cushion = 120,000, interest 5 percent of "
     "120,000 = 6,000, ending 272,500 - 352,500 + 120,000 - 6,000 = 34,000.",
215: "Osagyefo: you need AUGUST'S ENDING balance, which the table does not print. Build it. "
     "August available = 34,000 + 486,000 = 520,000. August disbursements = 409,100 + 130,900 = "
     "540,000. Shortage = 540,000 - 520,000 = 20,000. Borrowing = 20,000 + 40,000 = 60,000. "
     "Loan balance = 120,000 + 60,000 = 180,000, so interest = 5 percent of 180,000 = 9,000. "
     "August ending = 520,000 - 540,000 + 60,000 - 9,000 = 31,000. "
     "September = 31,000 + 749,000 = " + C + "780,000. "
     "The trap is " + C + "749,000, the receipts on their own.",
216: "Osagyefo: shortage or surplus = total disbursements MINUS total cash available. "
     "August available = 34,000 + 486,000 = 520,000. August disbursements = 409,100 + 130,900 = "
     "540,000. 540,000 - 520,000 = " + C + "20,000, a positive number, so it is a SHORTAGE and "
     "the company must borrow. Subtracting the other way round is the common slip.",
217: "Osagyefo: September available = 31,000 + 749,000 = 780,000. "
     "September disbursements = 447,250 + 184,750 = 632,000. "
     "632,000 - 780,000 = -148,000, a negative number, so it is a SURPLUS of " + C + "148,000. "
     "The cushion is not subtracted here. That happens at the financing line.",
218: "Osagyefo: on a SHORTAGE, borrowing = shortage + cushion. The company must cover the gap "
     "AND still hold its cushion. 20,000 + 40,000 = " + C + "60,000. "
     "Borrowing only the 20,000 shortage leaves nothing in reserve, which is the trap.",
219: "Osagyefo: on a SURPLUS, repayment = surplus - cushion. You may only repay what is left "
     "after keeping the cushion. 148,000 - 40,000 = " + C + "108,000. "
     "Add the cushion when borrowing, subtract it when repaying. Getting that backwards is trap 12.",
220: "Osagyefo: interest is charged on the CUMULATIVE loan balance each month, not on the new "
     "borrowing. July: borrowed 120,000, balance 120,000, interest 6,000. "
     "August: borrowed a further 60,000, balance 180,000, interest 9,000. "
     "September: repaid 108,000, balance 72,000, interest 3,600. "
     "Total = 6,000 + 9,000 + 3,600 = " + C + "18,600. "
     "Charging 5 percent on each month's new borrowing gives 9,000 and misses the mark.",

221: "Birdy-Birdy: total cash available = beginning + receipts, and the beginning is last "
     "month's ending, which the table prints as 7,139 for the end of July. "
     "August = 7,139 + 180,000 = " + C + "187,139. "
     "Check July if you want: 57,500 available, 141,560 disbursed, shortage 84,060, "
     "borrowing 84,060 + 9,000 = 93,060, interest 2 percent of 93,060 = 1,861, "
     "ending 57,500 - 141,560 + 93,060 - 1,861 = 7,139.",
222: "Birdy-Birdy: September = August ending + September receipts. The table prints August's "
     "ending as 7,214, so 7,214 + 216,000 = " + C + "223,214. "
     "If it were not printed you would build it: 187,139 - 174,400 - 3,739 - 1,786 = 7,214.",
223: "Birdy-Birdy: August disbursements = 140,800 + 33,600 = 174,400. "
     "174,400 - 187,139 = -12,739, a negative number, so a SURPLUS of " + C + "12,739. "
     "The surplus is larger than the 9,000 cushion, so a repayment follows. "
     "Watch the sign: disbursements minus available, always in that order.",
224: "Birdy-Birdy: September available 223,214, disbursements 164,736 + 35,280 = 200,016, "
     "so the surplus is 23,198. Repayment = surplus - cushion = 23,198 - 9,000 = " + C + "14,198. "
     "The surplus is bigger than the cushion, so the normal repayment rule applies.",
225: "Birdy-Birdy: interest at 2 percent on the running balance. "
     "July: balance 93,060, interest 1,861. August: repaid 3,739, balance 89,321, interest 1,786. "
     "September: repaid 14,198, balance 75,123, interest 1,502. "
     "Total = 1,861 + 1,786 + 1,502 = 5,149, and the paper offers " + C + "5,150 for the rounding. "
     "Take the offered figure when your total is a cedi or two away.",
226: "Birdy-Birdy: ending = available - disbursements + borrowing - repayment - interest. "
     "September has no borrowing: 223,214 - 200,016 - 14,198 - 1,502 = " + C + "7,498. "
     "Notice the ending balance stays near the 9,000 cushion every month. That is the whole "
     "point of the cushion, and it is a quick sanity check on your arithmetic.",
}


def hook_for(question):
    source = question.get("source", "")
    match = re.search(r"Guide (\d+(?:\.\d+)?)", source)
    if match:
        key = match.group(1)
        if key in HOOKS:
            return HOOKS[key]
        chapter = key.split(".")[0]
        if chapter in HOOKS:
            return HOOKS[chapter]
    blob = (question.get("question_text", "") + " " + source).lower()
    for pattern, hook in TEXT_HOOKS:
        if re.search(pattern, blob):
            return hook
    return DEFAULT_HOOK


def main():
    totals = []
    for name in FILES:
        data = json.load(io.open(name, encoding="utf-8"))
        rewritten = 0
        for question in data:
            number = question["question_number"]
            if name == "compiled.json" and number in CALC:
                question["explanation"] = CALC[number]
                rewritten += 1
            question["hook"] = hook_for(question)
        keys = ["question_number", "question_text", "options", "correct_answer",
                "explanation", "hook", "source", "verified"]
        data = [{k: q[k] for k in keys if k in q} for q in data]
        json.dump(data, io.open(name, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        lengths = [len(q["explanation"]) for q in data]
        totals.append((name, len(data), rewritten,
                       round(sum(lengths) / len(lengths))))

    print("%-24s %5s %10s %14s" % ("file", "n", "reworked", "mean expl."))
    for name, count, rewritten, mean in totals:
        print("%-24s %5d %10d %14d" % (name, count, rewritten, mean))
    default_used = 0
    for name in FILES:
        for q in json.load(io.open(name, encoding="utf-8")):
            if q["hook"] == DEFAULT_HOOK:
                default_used += 1
    print("questions on the fallback hook: %d" % default_used)


if __name__ == "__main__":
    main()
