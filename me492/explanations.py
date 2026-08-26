#!/usr/bin/env python3
"""
Why each ME 492 answer is right.

One entry per question, keyed by the question number used in compiled.json:

    number: (stem_prefix, explanation, source)

stem_prefix is the first words of the stem. build_questions.py checks it against
the real stem, so a reordered set fails the build instead of attaching the wrong
explanation.

Grounding: the lecture slides and ME 492 2025 NOTES, the printed marking schemes
(2005, 2007, 2015 and the 2020 online exam), and ME492-Study-Guide.md, which
reconciles the papers where they disagree.
"""

# Questions whose recorded answer was checked against the 2005 official marking
# scheme (the only printed key with a text layer). The other papers are
# image-only scans and were not machine checked.
CHECKED_AGAINST_2005_KEY = {
    1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 33, 35, 39, 42, 47, 51, 52,
    56, 57, 58, 59, 77, 78, 81, 83, 84, 85, 86, 87, 88, 90, 92, 93, 95, 96,
    97, 98, 99, 100, 101, 102, 103, 112, 122, 123, 124, 125, 126, 127, 128,
    130, 131, 132, 134, 135, 136, 137, 138, 139, 140, 141, 142, 148, 149,
    150, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 169,
    170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 181, 182, 184, 186,
    188, 189, 191, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236,
}

# The calculation items. Every one was worked through from the printed data.
RECOMPUTED = set(range(197, 227))

# Added 2026. These questions were found in the scanned papers but carried no
# printed key. The answer was worked out from the lecture notes and slides, and
# the explanation names the slide or the page it rests on.
DERIVED_FROM_MATERIALS = {24, 25, 26, 27, 45, 46, 71, 110, 111, 193, 194}

# Added 2026. No printed key either, but a marked past paper shows the answer:
# a circled option on the 2015 script, or a selected radio on the Canvas paper.
MATCHED_TO_A_MARKED_PAPER = {28, 168, 195}


def verification(number):
    """How the answer to this question was checked."""
    if number in RECOMPUTED:
        return "recomputed from the printed data"
    if number in CHECKED_AGAINST_2005_KEY:
        return "checked against the 2005 official marking scheme"
    if number in DERIVED_FROM_MATERIALS:
        return "derived from the lecture notes and slides"
    if number in MATCHED_TO_A_MARKED_PAPER:
        return "matched to a marked past paper"
    return "not checked against a printed key"


EXPLANATIONS = {
    # -- Set 1: entrepreneurship and free enterprise -------------------------
    1: ("A person who starts a new business",
        "This is the textbook definition of the entrepreneur: initiative, risk, and "
        "value created either from something new or from resources used in unusual "
        "ways. Sole proprietor names a legal form, not the role.",
        "Guide 3, high frequency definitions"),

    2: ("Any person or organisation that has an interest in",
        "A stakeholder holds an interest in the business or is affected by it. The group "
        "is wide: owners, lenders, employees, customers, suppliers and society. A vendor "
        "or a partner is only one kind of stakeholder.",
        "Guide 3; Slide 1"),

    3: ("A time horizon during which opportunities exist",
        "A window of opportunity is open only for a period. Competitors rush in, the "
        "market saturates, and the window closes. A corridor is different: it is the "
        "route the entrepreneur travels, where one idea leads to the next.",
        "Guide 5.4, windows and corridors"),

    4: ("Richard Cantillon, a French economist",
        "Cantillon put the entrepreneur at the centre of economics as the person who "
        "consciously decides how to allocate resources and seeks higher yields. He also "
        "buys at a certain price and sells at an uncertain one, so he carries the risk. "
        "Warning: the 2005 official key marks resource allocation plus exceptional insight "
        "into society's needs. The slides give that insight to Say, not Cantillon. If the "
        "paper prints the i/ii/iii version, answer as the key does.",
        "Guide 4.1; 2005 marking scheme item 7"),

    5: ("Carl Menger described entrepreneurship as",
        "Menger defined entrepreneurship as converting resources into goods and services "
        "that consumers value. Creative destruction and entrepreneurs as innovators "
        "belong to Schumpeter. This swap is the classic trap in this item.",
        "Guide 4.1; trap list 6"),

    6: ("Jean Baptiste Say combined the economic risk taker",
        "Say merged Cantillon's risk taker with Smith's industrial manager. His "
        "entrepreneur holds the arts and skills to create new enterprises and has "
        "exceptional insight into what society needs.",
        "Guide 4.1, the economists"),

    7: ("Adam Smith spoke of the enterpriser",
        "Smith's enterpriser forms an organisation for commercial purposes, has unusual "
        "foresight to see potential demand, and transforms that demand into supply.",
        "Guide 4.1, the economists"),

    8: ("In Drucker's view, the entrepreneur",
        "Drucker's point is the shift from problems to opportunities. Resources are "
        "redirected towards progressive opportunities, not merely used to fix what is "
        "broken.",
        "Guide 4.1, the economists"),

    9: ("The replacement of existing products and businesses",
        "Creative destruction is Schumpeter's term. New and better products displace the "
        "old ones, and the firms behind them. Upscaling is circled on one student script, "
        "but it is not the term.",
        "Guide 4.1; Guide 16, conflicts"),

    10: ("Entrepreneurship has influenced economic development",
         "All three effects are taught. Entrepreneurship alters the direction of national "
         "economies, drives quantum leaps in technology, and forces resources out of old "
         "uses into more productive ones.",
         "Guide 4.7, effects on the economy"),

    11: ("Entrepreneurs are often thought to be inspired people",
         "The four sources of change are scientific knowledge and the industrial "
         "revolution, demographic and market changes, process innovation, and social and "
         "cultural changes. As printed here, i and iii carry them, so the 2005 key marks "
         "i and iii only.",
         "Guide 4.2, sources of change"),

    12: ("Distinguishing factors that differentiate entrepreneurs",
         "Vision for growth, commitment to constructive change and persistence mark the "
         "entrepreneur. Item ii fails on income substitution. That is what a small "
         "business person does, replacing a salary rather than building growth.",
         "Guide 4.3, entrepreneur versus small business person"),

    13: ("Many small businesses are small by",
         "Small businesses stay small by their nature and by the owner's intention. Legal "
         "contracts create the legal form of a business, not its size.",
         "Guide 4.4, why small businesses are small"),

    14: ("Some of the main factors that lead to success",
         "The four success factors are a good entrepreneurial team, a well planned "
         "enterprise pursuing incremental growth, good timing, and a business ideology "
         "that serves customers. Item ii fails on a fat bank account. Most successful "
         "firms started with little money.",
         "Guide 4.6, success factors; Guide 4.5, myths"),

    15: ("Contributions by these European economists",
         "Menger, Mill and Say are all named in the slides as European economists who "
         "shaped the modern idea of entrepreneurship.",
         "Guide 4.1, the economists"),

    16: ("Corporate entrepreneurship",
         "All three describe it. Corporate entrepreneurship makes established companies "
         "more productive, it is also called intrapreneurship, and it runs on the "
         "innovation of creative employees inside the firm.",
         "Guide 4.8, intrapreneurship"),

    17: ("Intrapreneurship is concerned with innovation",
         "Corporate managers combine resources in unusual ways, and they commit time, "
         "energy and their careers. They do not take personal investment risks. The "
         "company carries the money risk. That is the standard trap here.",
         "Guide 4.8; trap list 15"),

    18: ("The reason for business failure is most commonly",
         "Inexperience is the most common cause in the slides. It is an internal cause, "
         "but the paper wants the specific word, not the category.",
         "Guide 4.9, recurring facts"),

    19: ("The risk of business failure for businesses starting from scratch",
         "Starting from scratch carries higher failure risk than buying a going concern "
         "or a franchise, because nothing is proven yet: no customers, no systems, no "
         "record.",
         "Guide 4.9, recurring facts"),

    20: ("Which of the following is not a reason for people going into business",
         "Money, independence, being your own boss and leaving an inheritance are all "
         "listed reasons. To live where I like is the odd one out in the slides.",
         "Guide 4.9, recurring facts"),

    21: ("Entrepreneurs typically form",
         "Service businesses are the most common start, because they need the least "
         "capital and the least fixed plant.",
         "Guide 4.9, recurring facts"),

    22: ("Entrepreneurs typically have a high internal locus of control",
         "True. A high internal locus of control means the person believes outcomes "
         "follow from their own action, not from luck or fate. It is a standard "
         "entrepreneurial trait.",
         "Guide 4.9, recurring facts"),

    23: ("Society and humankind as stakeholders",
         "Each stakeholder group wants something different. Society wants value added "
         "products and services. Lenders want cash flow and collateral, investors want a "
         "profitable return, and employees want income and job stability.",
         "Guide 10.10, stakeholders"),

    # -- Set 2: creativity and innovation ------------------------------------
    30: ("Which of the following is the ability to see, conceive, and create",
         "Watch the wording. The slides define innovation as the ability to see, conceive "
         "and create new and unique products, processes or services. Creativity is the "
         "ability to bring something new into existence. Here the stem names products, "
         "processes and services, so the answer is innovation.",
         "Guide 5.1, definitions"),

    31: ("Creativity is best defined as",
         "Creativity is an ability, not an activity. It is the ability to bring something "
         "new into existence. Innovation is the process that follows, so creativity is a "
         "prerequisite for innovation.",
         "Guide 5.1, definitions"),

    32: ("Innovation is best defined as",
         "Innovation is the process of doing new things: creative ideas turned into "
         "useful applications. The seed is creativity, the process is innovation.",
         "Guide 5.1, definitions"),

    33: ("In the creative process, a person is said to be in the verification stage",
         "Verification is validation: apply or test the idea to prove it has value. Item "
         "ii is preparation, the conscious search. Item iii is illumination, the sudden "
         "flash. This mix-up is why the 2005 key marks i only.",
         "Guide 5.2, the five stages; trap list 5"),

    34: ("In the creative process, a person is said to be in the preparation stage",
         "Preparation is the conscious search for the knowledge needed to bring the idea "
         "to life. Note the word conscious. Incubation is the subconscious stage.",
         "Guide 5.2, the five stages"),

    35: ("In the creative process, verification is",
         "Verification is the fifth stage: the application or test that proves the idea "
         "has value. Recognising an idea as feasible is illumination, one stage earlier.",
         "Guide 5.2, the five stages"),

    36: ("In the creative process, the subconscious assimilation of information",
         "Incubation is the subconscious stage, the one people call sleeping on the "
         "problem. Preparation is the conscious search that comes before it.",
         "Guide 5.2, the five stages"),

    37: ("In the creative process, the stage at which an idea resurfaces",
         "Illumination is the realisation stage: the Oh, I see moment when the idea is "
         "recognised as feasible. The test that proves its value comes later, in "
         "verification.",
         "Guide 5.2, the five stages"),

    38: ("The seeding stage of a new idea",
         "Idea germination is stage one, the seeding stage. The seed is planted by the "
         "person's own curiosity or interest.",
         "Guide 5.2, the five stages"),

    39: ("The innovation process is the translation of useful ideas",
         "The innovation process holds analytical planning, organising resources, "
         "implementation and commercial application. Item ii lists germination, "
         "preparation and verification, which belong to the creative process. Do not mix "
         "the two lists.",
         "Guide 5.3; trap list 4"),

    40: ("For technological innovation to succeed, the key people",
         "The trio is the creative source, the champion and the sponsor. Reject any "
         "option that swaps in the inventor, the investor, the entrepreneur or the "
         "promoter. The 2020 paper reworded the stem and the answer stayed iii only.",
         "Guide 5.5, the three key people"),

    41: ("The brainstorming method for generating new product and venture ideas",
         "No criticism, free wheeling, high quantity, and combining or improving ideas "
         "are the rules. Item ii fails because discarding ideas without merit is "
         "judgement, and no idea is judged during the session.",
         "Guide 5.6, brainstorming rules"),

    42: ("A majority of new products evolve at the end of the technology spectrum",
         "Most new products are low-tech. That is why the advice is to make them easily, "
         "market them quickly and terminate them cheaply: patents cannot protect them.",
         "Guide 5.8, the technology spectrum"),

    43: ("Something that begins with a person's interest or advocation",
         "A mind map starts from the person's own interest, branches into related "
         "products and market opportunities, then follows each branch to expand new "
         "business ideas.",
         "Guide 5.7, mind map"),

    44: ("The principle which suggests that successful ventures evolve",
         "The corridor principle. Entrepreneurs already positioned in similar work can "
         "move fast when a window opens. The window is the time horizon; the corridor is "
         "the route travelled.",
         "Guide 5.4, windows and corridors"),

    # -- Set 3: business planning and feasibility ----------------------------
    47: ("A description of the future direction of a business",
         "The business plan describes where the business is going. Keep it apart from the "
         "pro forma statement, which predicts what the financial statements will look "
         "like at period end.",
         "Guide 3, high frequency definitions"),

    48: ("The business plan is primarily supposed to",
         "Primarily it informs lenders and investors, the people who decide whether to "
         "put money in. It does guide the entrepreneur too, but the papers mark the "
         "funding purpose as the primary one.",
         "Guide 6.12, what the plan is for"),

    49: ("When considering starting up a business, a business plan can",
         "It does all three: provide direction, prove feasibility, and attract money. "
         "When the paper offers the combined option, take it.",
         "Guide 6.12, what the plan is for"),

    50: ("Responsibility for planning a new venture rests on",
         "The entrepreneur carries the responsibility, because the entrepreneur holds the "
         "vision and the motivation and can articulate the information. Consultants and "
         "university centres can help, but the duty does not transfer.",
         "Guide 6.1, who writes the plan"),

    51: ("A feasibility plan should be prepared by",
         "The entrepreneur prepares it, in consultation with specialists. Not alone, and "
         "not handed to a consultant. The related because item, that specialists prepare "
         "it best, is marked E, both statements false.",
         "Guide 6.1; Guide 16, conflicts"),

    52: ("A feasibility plan is a written document",
         "All three hold. It integrates operations, marketing, finance and human "
         "resources, it describes the external and internal elements of starting up, and "
         "the entrepreneur prepares it.",
         "Guide 6.2, what a feasibility plan is"),

    53: ("The model for developing a new entrepreneurial venture",
         "The feasibility plan is the pragmatic plan. It does enough planning to prove "
         "the venture can work, without drowning the entrepreneur in detail. It is not a "
         "summary, and it is not the full plan of an existing company.",
         "Guide 6.2, what a feasibility plan is"),

    54: ("The perspectives that should be considered when writing a business plan",
         "Three perspectives: the entrepreneur, the market, and the investor. The plan "
         "has to satisfy all three readers at once.",
         "Guide 6.3, three perspectives"),

    55: ("Before an entrepreneur commits time and effort to do a business plan",
         "All three areas are checked for barriers: market, finance and operations; the "
         "business concept and the team; and the goals, finance and the product itself. "
         "The 2020 exam confirms all three.",
         "Guide 6.4, barriers to success"),

    56: ("One of the initial important elements of information needed",
         "Market potential comes first. Operational needs and profitability matter later, "
         "but if there is no market there is nothing to plan. The key marks i only.",
         "Guide 6.5, the first element of information"),

    57: ("The executive summary is the part of the plan that is written",
         "All three are true. It stimulates interest, it is concise and convincing, and "
         "it is written last, after the whole plan exists. Two or three pages is the "
         "usual length.",
         "Guide 6.6, the executive summary"),

    58: ("The difference between the venture definition in the executive summary",
         "The venture definition is short: the name of the business and why it was "
         "founded. The business concept in the main body goes further, into how the "
         "business evolved and the nature of market demand.",
         "Guide 6.6, the executive summary"),

    59: ("The introductory or cover page of a business plan should contain information on the business and should include",
         "When the paper forces a single answer for the cover page, the answer is the "
         "confidentiality clause. The executive summary and the financial summary sit "
         "inside the plan, not on the cover page.",
         "Guide 6.7, the cover page"),

    60: ("The introductory or cover page of a business plan should contain information on the business and should include (i)",
         "All three belong on the cover page: name, address and financing required; the "
         "confidentiality statement with the entrepreneurs' contacts; and a brief "
         "description of the business concept.",
         "Guide 6.7, the cover page"),

    61: ("The common elements of a business plan include",
         "The executive summary is a business plan element. Abstract, literature review, "
         "product design and conclusions come from academic reports. Never pick those. "
         "When market research and analysis is offered instead, that is the answer.",
         "Guide 6.8, common elements"),

    62: ("The organisational plan is the part of the business plan that describes",
         "The organisational plan sets out the organogram: who reports to whom. The 2020 "
         "online exam and the 2015 paper agree, against one compiled sheet that says the "
         "form of ownership.",
         "Guide 16, conflicts"),

    63: ("Environmental and industry analysis of a business plan deals with",
         "All three. Location and immediate area, competitive strategies and industry "
         "trends, and the external uncontrollable variables. The word environmental "
         "points to what the venture cannot control.",
         "Guide 6.9, environmental and industry analysis"),

    64: ("For ventures that manufacture, design or sell products",
         "All three. The older wording of this section is operations, human resources, "
         "facilities, inventory and related issues, with leadership and the team named "
         "alongside.",
         "Guide 6.10, manufacturing or operations section"),

    65: ("What type of information should be put in the appendix",
         "The appendix carries supporting documents: resumes of partners, facility "
         "layouts and partnership agreements. Take the fullest option printed. When only "
         "one is allowed, pick resumes of partners.",
         "Guide 6.11, the appendix"),

    66: ("Many copies of a business plan are circulated",
         "A non-disclosure statement is the counter. It is a written, enforceable "
         "undertaking, which a verbal warning or a vague agreement is not. Hiding vital "
         "information defeats the purpose of the plan.",
         "Guide 6.16, security of the plan"),

    67: ("Conditions that can render the most effective business plans out-of-date",
         "For the single best answer, changes in the market and the industry. Those move "
         "the ground the whole plan stands on.",
         "Guide 6.13, why plans go out of date"),

    68: ("The most effective business plans can become out-of-date",
         "All three change the direction of a plan: poor articulation of the concept, "
         "loss or addition of key team members, and a new location.",
         "Guide 6.13, why plans go out of date"),

    69: ("Some business plans fail because",
         "All three. Unreasonable and unmeasurable goals, no total commitment from the "
         "entrepreneur, and no experience in the planned business. When only one option "
         "is allowed, the 2020 key marks the unreasonable goals.",
         "Guide 6.14, why business plans fail"),

    70: ("Entrepreneurs can be described in terms of",
         "The 2015 red-marked paper takes all three: experience and family background, "
         "personal characteristics and skills, and successfully incubating a business. "
         "Pick the fuller option unless item iii is absent from the printed options.",
         "Guide 16, conflicts"),

    # -- Set 4: venture stages and start-up ----------------------------------
    72: ("Which stage describes the assembly of resources",
         "Pre-start-up is the assembly stage: gather the resources and organise the "
         "venture for opening. Nothing is trading yet.",
         "Guide 7.1, the four growth stages"),

    73: ("This type of growth model is concerned with the initial business operations",
         "Start-up is the stage of initial business operations. Pre-start-up is still "
         "assembly; early growth comes after the venture proves itself.",
         "Guide 7.1, the four growth stages"),

    74: ("In which type of growth model does reality shock set in",
         "Reality shock belongs to the start-up stage. The entrepreneur meets the real "
         "market for the first time and has to position the business to compete in it.",
         "Guide 7.1, the four growth stages"),

    75: ("The stage in which the venture has been initially successful",
         "Early growth. The venture worked and is growing at a healthy rate, so resources "
         "now need careful co-ordination for the entrepreneur to take profit.",
         "Guide 7.1, the four growth stages"),

    76: ("The stage in which the enterprise is established",
         "Later growth. The enterprise is established and professionally managed, so the "
         "founder is no longer the only manager.",
         "Guide 7.1, the four growth stages"),

    77: ("Pre-start-up activities for new ventures include",
         "The product or market survey is a pre-start-up activity, along with defining the "
         "business concept. Positioning the venture belongs to start-up, and going public "
         "belongs to later growth.",
         "Guide 7.2, pre-start-up activities"),

    78: ("There are two benchmark considerations for the start-up stage",
         "The two benchmarks are meeting operating objectives and positioning the venture "
         "for long-term growth. This answer is fixed across the 2007, 2015 and 2020 "
         "papers, so learn it word for word.",
         "Guide 7.3, benchmark considerations"),

    79: ("Start-up operating objectives are",
         "Sales, revenue, growth and position. Profit is not on the start-up list. The "
         "venture is buying its place in the market first.",
         "Guide 7.4, start-up operating objectives"),

    80: ("Measuring the progress of the business in the start-up stage",
         "Make a 12 month schedule and check the plan against it. The other options are "
         "sensible habits, but the paper wants the scheduled review.",
         "Guide 7.5, measuring progress"),

    81: ("Prior to start-up, entrepreneurs can reduce financial burdens by",
         "Plan the assets carefully. Cutting capacity, cutting staff or underpaying people "
         "damages the venture instead of financing it.",
         "Guide 7.6, reducing the financial burden"),

    82: ("Financial planning in the pre-start-up stage",
         "It need not be extensive, but it must rest on verifiable information. Figures "
         "you cannot verify make the whole plan worthless to a lender.",
         "Guide 7.7, financial planning before start-up"),

    # -- Set 5: market research and the marketing plan -----------------------
    83: ("A market segment on which a business can choose to concentrate",
         "Market niche. This item has appeared as option c, a and e in different years, "
         "and the answer text never changed. Learn the text, not the letter.",
         "Guide 3; Guide 1, rule 1"),

    84: ("A market niche is a carefully defined segment",
         "The niche defines the positioning of the product or service. Positioning is "
         "where the product stands in the customer's mind against the alternatives.",
         "Guide 8.5, a market niche"),

    85: ("Setting up the specifications of one's primary clients",
         "Customer scenario. It sets out who the primary clients are in specific terms. "
         "One compiled answer sheet says market survey, and that is wrong against every "
         "printed key.",
         "Guide 16, conflicts"),

    86: ("The objective of market research and analysis is to establish",
         "The objective is to prove a market exists. Customers, products and competitors "
         "are studied, but the finding you need is the market itself.",
         "Guide 3, high frequency definitions"),

    87: ("Market research and analysis activities include",
         "Four activities: identify potential customers, evaluate markets, analyse "
         "competitors, and describe assumptions. The distractor drops the assumptions. "
         "Take the option that keeps them.",
         "Guide 8.2, market research activities"),

    88: ("The market research culminates in a",
         "Market research ends in a sales forecast, which sets the expected volume and "
         "revenue. The sales forecast is then the first step of the operating budget.",
         "Guide 3; Guide 12.2, the master budget"),

    89: ("The results of good market research include",
         "Only the well defined sales forecast. A revenue estimate follows from the "
         "forecast, and investment needs come from the financial plan, not from market "
         "research.",
         "Guide 8.6, results of good market research"),

    90: ("The main difference between market research analysis and market plan",
         "Market research gathers the information. The market plan then uses it in a "
         "strategy to attract customers. This sentence appears almost every year, so "
         "learn it word for word.",
         "Guide 8.1, research versus plan"),

    91: ("The market plan tried to respond to the question",
         "Who is the customer and where is he or she located. The plan starts from the "
         "customer, not from the product or the factory.",
         "Guide 8.3, what the market plan answers"),

    92: ("The ________ describes an entrepreneur's intended strategy",
         "The market plan carries the intended strategy. Distribution, operations and "
         "promotion are parts that serve it.",
         "Guide 8.10, the marketing plan"),

    93: ("Marketing research activities that are undertaken after a new venture opens",
         "Competitive analysis is the marketing research done once the doors are open, "
         "when real competitors respond to you.",
         "Guide 8.14, marketing research after opening"),

    94: ("A competitive analysis is marketing research",
         "The key marks the pre-start-up stage only. Take the stage the paper prints; the "
         "related item on research after opening is answered by the term competitive "
         "analysis itself.",
         "Guide 8.14; Guide 15, the i/ii/iii bank"),

    95: ("The marketing functions include",
         "The 4 Ps: product, price, place or distribution, and promotion. Always take the "
         "fullest option printed. If promotion is not listed anywhere, product, price and "
         "distribution is the answer.",
         "Guide 8.4, the marketing functions; trap list 9"),

    96: ("An expanded view of a company's product includes",
         "Four elements: function, form, packaging characteristics, and after sales "
         "service support. The distractor stops at packaging and drops the service.",
         "Guide 8.8, product"),

    97: ("The planned process of determining prices",
         "Pricing policy. It is the planned process, including how prices change in the "
         "field for unusual circumstances. Price setting is the single act, not the "
         "policy.",
         "Guide 3; Guide 16, conflicts"),

    98: ("A broad term applied to marketing tactics that serve to attract customers",
         "Promotion is the broad term. Advertising, publicity and personal selling are "
         "methods inside it.",
         "Guide 3, high frequency definitions"),

    99: ("A careful selection of promotional methods",
         "The promotional mix is the selected set of methods, chosen to fit the grand "
         "marketing strategy. Note it is the selection, not any single method.",
         "Guide 3, high frequency definitions"),

    100: ("As a start-up business, advertising is a vital part",
         "Advertising seeks to convince someone to walk in your door. Making a satisfied "
         "customer is the job of the product and the service. Selling to someone who "
         "cannot afford it is not a marketing objective.",
         "Guide 8.9, promotion and advertising"),

    101: ("Marketing Communications or Integrated Marketing Communications",
         "Integrated means one consolidated, focused message. Item ii says the opposite, "
         "an assortment of forms with a variety of messages. Item iii describes the "
         "marketing mix, not communications.",
         "Guide 8.9, promotion and advertising"),

    102: ("Integrating promotion into the marketing mix seeks to",
         "All three: increase sales, build recognition and build consumer loyalty.",
         "Guide 8.9, promotion and advertising"),

    103: ("A marketing plan is implemented through a",
         "The marketing program implements the plan. Older hand-marked papers show "
         "marketing activities, but the printed 2015 key marks marketing program. Choose "
         "activities only when program is not printed.",
         "Guide 8.10; Guide 16, conflicts"),

    104: ("Marketing Plan for a new venture",
         "The 2005 key marks i only. The plan establishes how the entrepreneur will "
         "compete and operate in the market. Describing the customer belongs to market "
         "research, and solid projected sales data come from the sales forecast.",
         "Guide 8.10, the marketing plan"),

    105: ("Marketing plans are ineffective or fail in meeting marketing goals",
         "All four causes are listed together: no real plan, weak situation analysis, "
         "unrealistic goals, and unanticipated competitive moves. Take the combined "
         "option.",
         "Guide 8.10, the marketing plan"),

    106: ("A distribution system is",
         "Distribution covers the physical process of getting goods to market and the "
         "process of locating services. Item i describes production, which happens before "
         "distribution starts.",
         "Guide 8.7, distribution"),

    107: ("The types of distribution channels that exist are",
         "Three channel types: consumer, industrial and service.",
         "Guide 8.7, distribution"),

    108: ("The infrastructure of a marketing plan is often built solely",
         "Distribution. Everything else in the plan depends on being able to put the "
         "product or the service in front of the customer.",
         "Guide 8.7, distribution"),

    109: ("Developing a clear profile of potential customers",
          "All three: age and sex, income status, and where the customer base is located. "
          "The profile answers who they are and where they are.",
          "Guide 8.13, customer profile"),

    # -- Set 6: intellectual property and law --------------------------------
    112: ("A grant of a property right by a government to an inventor",
          "A patent is the government grant of a property right to an inventor. A "
          "trademark protects a mark that identifies a trader, and a disclosure document "
          "only states the intent to patent.",
          "Guide 9.1, patents"),

    113: ("A patent search is done to determine",
          "The search answers one question: does the creation already exist, and is it "
          "still actively protected. Fees, oaths and filing sections are procedure, not "
          "the purpose of the search.",
          "Guide 9.1, patents"),

    114: ("A Disclosure Document, if filed by an entrepreneur, becomes important",
          "The disclosure document matters when infringement occurs, because it evidences "
          "the date the inventor declared the intent to patent.",
          "Guide 9.2, the disclosure document"),

    115: ("A Disclosure Document is",
          "Only ii. It is a statement to the patent office declaring the intent to patent "
          "an idea. It is not a patent, and it is not part of the business plan.",
          "Guide 9.2, the disclosure document"),

    116: ("The requirements for a successful utility patent grant",
          "The creation must be the applicant's own, and it must be useful and new. "
          "Personal investment risk is not a patent requirement. Note the split: the older "
          "papers mark ii and iii, while the 2020 online wording marked all three.",
          "Guide 9.1, patents"),

    117: ("A plant patent is given for",
          "Plant patents cover hybrid roses and food grains. The 17 years figure belongs "
          "to the old utility patent term, not to what a plant patent is given for.",
          "Guide 9.1, patents"),

    118: ("A trademark",
          "A trademark may be a sound, a word, a symbol, a design or a slogan, and it can "
          "last indefinitely while it stays in use. Take the option that combines them.",
          "Guide 9.3, trademarks"),

    119: ("Filing of trade mark registrations meets these form requirements",
          "Three requirements: the written form with the fee, the drawing plus five "
          "specimens showing actual use, and publication in the Trade Mark Official "
          "Gazette. All three are needed, so take the combined option.",
          "Guide 9.3, trademarks"),

    120: ("Contracts are an important part of the transactions",
          "All three. Describe the transaction in detail, obtain signatures, and remember "
          "that an oral agreement will not hold for a deal running over one year.",
          "Guide 9.5, contracts"),

    121: ("The best protection against product liability",
          "Produce safe products and warn customers of potential hazards. Zero defects is "
          "not achievable, so it cannot be the protection.",
          "Guide 9.4, product liability"),

    # -- Set 7: organising and legal forms -----------------------------------
    122: ("A person who is involved in a voluntary association",
          "A general partner joins voluntarily and carries operational responsibility, "
          "with unlimited liability. A limited partner invests but may not legally help "
          "manage the firm.",
          "Guide 10.5, partnership"),

    123: ("A person or company that originates a business system",
          "The franchisor originates the system and supplies the package for a fee and "
          "royalties. The franchisee is the acquiring owner. The franchise is the system "
          "created by the contract.",
          "Guide 10.9, franchising"),

    124: ("A business system created by a contract between a parent company",
          "The franchise is the business system itself, created by the contract. Keep the "
          "three words apart: franchisor originates, franchisee acquires, franchise is "
          "the system.",
          "Guide 10.9, franchising"),

    125: ("A legal form of business created through law that empowers a business",
          "A corporation is created by law as a separate legal entity, so it has "
          "perpetual life and survives its investors. That separation also gives limited "
          "liability.",
          "Guide 10.6, corporation"),

    126: ("A legal organisation created through investments by two or more companies",
          "A joint venture is formed by companies investing together to pursue one "
          "commercial activity. A partnership is formed by persons, and a corporation is "
          "chartered by the state.",
          "Guide 3, high frequency definitions"),

    127: ("Selecting a legal form of business involves a decision",
          "Three criteria: the preferences of the entrepreneur, the profile of the "
          "enterprise, and the advantages and disadvantages of the legal entity. Tax and "
          "succession issues sit inside the third criterion.",
          "Guide 10.2, selecting the legal form"),

    128: ("The main disadvantage of a sole proprietorship is",
          "Unlimited legal and financial liability. The owner and the business are one in "
          "law, so personal assets are exposed. Limited life is a real disadvantage too, "
          "but the papers mark liability as the main one.",
          "Guide 10.4, sole proprietorship"),

    129: ("Which of the following is an advantage of owning a sole proprietorship?",
          "Easy to set up. The other four options are the standard disadvantages: lack of "
          "continuity, limited resources, unlimited liability and few fringe benefits.",
          "Guide 10.4, sole proprietorship"),

    130: ("Compared to other legal forms of business, the sole proprietorship",
          "Items i and iii are true as printed here: autonomy of control, and inexpensive "
          "and self directing. Item ii is false, because a sole proprietor has a narrower "
          "network than a partnership or a corporation. Read option iii carefully; when it "
          "reads differently the 2020 exam marks i only.",
          "Guide 10.4, sole proprietorship"),

    131: ("A partnership, as a legal form of business, has certain disadvantages",
          "The business ends on the death or withdrawal of a partner, and liability is "
          "unlimited for all parties, jointly and severally. Item iii is false: a "
          "partnership has more access to resources than a sole proprietorship, not less.",
          "Guide 10.5, partnership"),

    132: ("Limited partners enjoy certain advantages over general partners",
          "All three. The limited partner is exempt from management responsibility, "
          "profits and losses pass through to all partners, and the investment can be sold "
          "or assigned.",
          "Guide 10.5, partnership"),

    133: ("A disadvantage of owning a closely held corporation is",
          "Expensive to start. Incorporation costs money and paperwork. Limited liability, "
          "perpetual life and better access to resources are the advantages.",
          "Guide 10.6, corporation"),

    134: ("A formal board of directors is required by law only for",
          "Only incorporated companies must have a formal board. Other forms may keep a "
          "board of advisors, but the law does not require one.",
          "Guide 10.7, boards"),

    135: ("The membership of a Board of Directors for a new venture should be",
          "Five to nine members. Large enough for a mix of skills, small enough to decide.",
          "Guide 10.7, boards"),

    136: ("A board of advisors serves a new venture in an advisory capacity",
          "Advisors are outside professionals. The 2015 paper prints a lawyer, a banker, "
          "an accountant and an advertising agent; the 2005 key prints a lawyer, a banker "
          "and a marketer. Take the fuller professional mix that is printed.",
          "Guide 10.7; Guide 16, conflicts"),

    137: ("Directors of new ventures fulfil important roles",
          "Two roles, not three. ME 492 2025 NOTES says directors act as mentors, "
          "professional advisers and members of an expanded social network. Disturbance "
          "handling and resource allocation are decision making duties, and the stem asks "
          "for the roles beyond those. The 2005 official key marks i and ii only.",
          "ME 492 2025 NOTES; 2005 marking scheme item 25"),

    138: ("The entrepreneurial team is a very vital part of the management team",
          "All four duties belong to the team: build the organisation, give the venture "
          "its identity, handle operational issues, and guide the venture through change. "
          "When the paper forces one option, the 2015 key marks guiding the venture "
          "through change.",
          "Guide 10.8, the entrepreneurial team"),

    139: ("The responsibilities of the founder are",
          "The founder defines the business and identifies the human resource "
          "requirements. Running the functional areas is the work of the team that the "
          "founder then hires.",
          "Guide 10.8, the entrepreneurial team"),

    140: ("After the legal form of business has been decided",
          "The first step is the organisational structure. Job analysis, job description, "
          "job specification and training all follow it, in that order.",
          "Guide 10.1, designing the organisation"),

    141: ("The organisation must identify the major activities",
          "Job analysis identifies the major activities. The job description then writes "
          "them down, and the job specification sets the person requirements.",
          "Guide 10.1, designing the organisation"),

    142: ("Individuals within someone's immediate circle of daily relationships",
          "That circle is the personal network. It is the closest ring of contacts, "
          "tighter than the wider social network of loose ties.",
          "Guide 3, high frequency definitions"),

    # -- Set 8: financing the new venture ------------------------------------
    143: ("Money needed to purchase such physical facilities",
          "Fixed capital buys the physical facilities: buildings, fixtures and equipment. "
          "It is a long term investment, so it is financed with long term credit.",
          "Guide 11.1, the three capital requirements"),

    144: ("Money used to pay the rent and utility bills",
          "Working capital pays the day to day costs: rent, utilities, inventories and "
          "payroll. Short term credit funds it, because the sales it generates repay it.",
          "Guide 11.1, the three capital requirements"),

    145: ("Which of the following is money held in reserve for emergency situations",
          "Fluid or liquid capital is the emergency reserve, held as cash or as securities "
          "you can sell quickly. It is not spent on operations or on plant.",
          "Guide 11.1, the three capital requirements"),

    146: ("Lending institutions provide entrepreneurs with short term loans",
          "Short term loans fund working capital. They are self liquidating: the trading "
          "they support brings in the cash that repays them.",
          "Guide 11.2, the three types of credit"),

    147: ("Entrepreneurs use ________ to purchase major fixed capital",
          "Long term financing, over five years, buys buildings and land. Intermediate "
          "term credit, one to five years, buys the smaller fixed items such as fixtures "
          "and equipment.",
          "Guide 11.2, the three types of credit"),

    148: ("If short term financing is used by a new venture",
          "Sales and profits repay short term funds. That is what makes them self "
          "liquidating. Selling fixed assets to repay a short term loan means the venture "
          "is in trouble.",
          "Guide 11.2, the three types of credit"),

    149: ("By far the most frequently used source of short-term funds",
          "Commercial banks, when collateral is available. Venture capital targets high "
          "risk start-ups, and personal funds are the cheapest but the most limited.",
          "Guide 11.5, the sources ranked"),

    150: ("Which of the following is intended for higher risks such as start up",
          "Venture capital carries the high risk of start-ups. Development capital funds "
          "more mature investments, and replacement capital buys out an original "
          "shareholder.",
          "Guide 11.5, the sources ranked"),

    151: ("Investors who look for businesses that offer extremely high growth",
          "Venture capitalists. The three markers in the stem are their standard test: "
          "very high growth potential, willingness to give up equity, and a way to cash "
          "out in about five years.",
          "Guide 11.5, the sources ranked"),

    152: ("Asset-based financing refers to",
          "Asset-based financing is debt financing, because the asset is the collateral. "
          "One compiled answer sheet says equity, and that is wrong against the notes and "
          "the 2005 key.",
          "Guide 11.3; Guide 16, conflicts"),

    153: ("Which of the following does not require collateral and offers the investor",
          "Equity financing. The investor gets an ownership position instead of security, "
          "and is repaid with a share of the profits, not with principal and interest.",
          "Guide 11.3, debt versus equity"),

    154: ("Government grants for a new business can be referred to as",
          "Grants are an external fund. Internal sources are profits, asset sales, lower "
          "working capital and faster collection of receivables. Money from outside the "
          "business is external, even when nobody has to repay it.",
          "Guide 11.4, internal versus external funds"),

    155: ("________ are the least expensive funds in terms of cost and control",
          "Personal funds. They cost nothing in interest and nothing in control, and "
          "outside funders insist on seeing them. Nobody backs a founder who has not "
          "backed the venture.",
          "Guide 11.5, the sources ranked"),

    156: ("Long term debt is frequently used to purchase some asset",
          "Lenders take 50 to 80 percent of the asset value as collateral. The margin "
          "protects them if the asset has to be sold in a hurry.",
          "Guide 11.3, debt versus equity"),

    157: ("When interest rates are low, ________ financing allows the entrepreneur",
          "Debt. Cheap interest lets the entrepreneur borrow rather than sell shares, so "
          "ownership stays larger and the return on equity is greater.",
          "Guide 11.3; trap list 7"),

    158: ("________ is the term commonly used to describe the ordinary share capital",
          "Equity is the ordinary share capital. Keep it apart from net worth, which is "
          "what owners have put in and left in.",
          "Guide 11.6, terms to know"),

    159: ("________ represents the amount owners have invested",
          "Net worth is what the owners invested plus what they retained from operations.",
          "Guide 11.6, terms to know"),

    160: ("The component of equity in a business representing accumulated profits",
          "Retained earnings are the accumulated profits above losses and payments to "
          "owners. They are profits kept in the business instead of paid out as dividends.",
          "Guide 11.6, terms to know"),

    161: ("An obligation arising from the purchase of goods or services on credit",
          "An account payable is money going out: you bought on credit and owe. The "
          "receivable item is asked right beside this one, so read the direction of the "
          "money.",
          "Guide 11.6; trap list 8"),

    162: ("Money due from an individual or another business as payment",
          "An account receivable is money coming in: you sold on credit and are owed. "
          "Receivable is due from another party.",
          "Guide 11.6; trap list 8"),

    163: ("________ is the integration and synchronisation of the various financial",
          "Financial co-ordination. It ties the separate financial activities together so "
          "every function works towards the same objectives.",
          "Guide 11.6, terms to know"),

    164: ("Restrictions to loan agreements are called",
          "Covenants are the restrictions written into a loan agreement. Collateral is the "
          "security pledged, which is a different thing.",
          "Guide 11.6, terms to know"),

    165: ("Cash flow equals",
          "Cash flow is receipts minus disbursements: money in less money out. It is not "
          "profit, and it has nothing to do with equity.",
          "Guide 11.6, terms to know"),

    166: ("Determining which source of funding entrepreneurs use depends on",
          "This is an except item. The three real factors are the type of financing "
          "needed, the nature and size of the business, and the entrepreneur's financial "
          "condition. Money portability is the invented option.",
          "Guide 11.5, the sources ranked"),

    167: ("Lenders to a new venture typically focus on aspects of credit character",
          "All three: cash flow, collateral and equity contribution. A 2020 script "
          "highlights ii only, but that is a student mark, not a key.",
          "Guide 16, conflicts"),

    # -- Set 9: budgeting and pro forma statements ---------------------------
    169: ("________ is a process that involves co-ordinating the finances",
          "Budgeting co-ordinates the finances of every area of the venture. Cost and "
          "financial accounting record what already happened; budgeting plans what will.",
          "Guide 12.1, levels of financial planning"),

    170: ("________ involves deciding which market niche should be profitable",
          "Strategic planning is the long term level. It defines the scope of the venture, "
          "which products to develop, and which niche should be profitable.",
          "Guide 12.1, levels of financial planning"),

    171: ("Which of the following involves making decisions such as whether to buy or lease",
          "Capital budgeting is the intermediate level, and buy or lease is its standard "
          "example. The decision commits money for more than one year.",
          "Guide 12.1, levels of financial planning"),

    172: ("Which of the following budgets is expected to be more specific?",
          "Operating budgeting is the short term level and the most specific: sales "
          "targets, production objectives and financing plans.",
          "Guide 12.1, levels of financial planning"),

    173: ("The three major budget categories in the master budget",
          "Operating budgets, capital budgets and financial statement budgets. The "
          "financial statement budgets are the pro forma statements.",
          "Guide 12.2, the master budget"),

    174: ("The master budget normally covers a",
          "One year. Perpetual budgeting keeps that one year rolling by adding a new month "
          "at the end as the current month closes.",
          "Guide 12.2, the master budget"),

    175: ("The budgeting process normally begins with the preparation of",
          "The operating budgets come first. Their information then feeds the financial "
          "statement budgets. The flow runs one way.",
          "Guide 12.2, the master budget"),

    176: ("The first step in the preparation of the operating budget is",
          "The sales forecast. Everything else, from purchases to cash, depends on how "
          "much you expect to sell.",
          "Guide 12.2, the master budget"),

    177: ("The composition of the numerous separate but interdependent departmental budgets",
          "That composition is the master budget. It gathers the departmental budgets for "
          "sales, production, manufacturing expenses and administrative expenses.",
          "Guide 12.2, the master budget"),

    178: ("Perpetual or continuous budgeting utilises",
          "A 12 month reporting period that rolls. At the end of the current month a new "
          "month is added at the end, so the horizon is always a year.",
          "Guide 12.2, the master budget"),

    179: ("________ budgets are intended to provide a basis for evaluating expenditures",
          "Capital budgets cover expenditure that impacts the business for more than one "
          "year. Some hand-marked copies show strategic budgets, but the printed 2005 and "
          "2007 keys both mark capital.",
          "Guide 12.2; Guide 16, conflicts"),

    180: ("Budgeted financial statements prepared from information in the master budget",
          "Pro forma statements. Pro forma means projected, so these are the budgeted "
          "income statement, balance sheet and cash flow.",
          "Guide 12.3, the pro forma statements"),

    181: ("A budget is",
          "All three at once: prepared as a planning function, administered as a control "
          "function, and expressed in financial or numerical terms. Take the combined "
          "option.",
          "Guide 12.2, the master budget"),

    182: ("Which of the following is true?",
          "The operating budgets feed the financial statement budgets. Never the reverse. "
          "That one way flow is the point of the question.",
          "Guide 12.2, the master budget"),

    183: ("Pro forma income statements are",
          "The pro forma income statement projects net profit from projected revenues "
          "less projected costs and expenses. Assets, liabilities and equity belong to the "
          "balance sheet.",
          "Guide 12.3, the pro forma statements"),

    184: ("________ summarises the projected assets, liabilities and equity",
          "The pro forma balance sheet. One compiled answer sheet gives the income "
          "statement here, and that is wrong. Assets, liabilities and equity are always "
          "the balance sheet.",
          "Guide 12.3; Guide 16, conflicts"),

    185: ("What are the main segments of a pro forma balance sheet?",
          "Assets, liabilities and owners equity. Those three segments are the balance "
          "sheet equation.",
          "Guide 12.3, the pro forma statements"),

    186: ("Projected cash available calculated from projected cash accumulations",
          "The pro forma cash flow: projected cash in less projected cash out. It reports "
          "cash available, not profit.",
          "Guide 12.3, the pro forma statements"),

    187: ("In the preparation of the pro forma income statement, the entrepreneur must first",
          "Develop the sales budget first. Sales drive the revenue line, and the costs "
          "follow from the volume you plan to sell.",
          "Guide 12.3, the pro forma statements"),

    188: ("Before developing the pro forma income statement, the entrepreneur should prepare",
          "The capital and operating budgets come before the pro forma income statement. "
          "The pro forma statements are built from budget information, not the other way "
          "round.",
          "Guide 12.3, the pro forma statements"),

    189: ("A prediction of what a company's financial statements will look like",
          "A pro forma statement predicts the financial statements at the end of the "
          "forecast period. A business plan describes the future direction; a pro forma "
          "statement puts numbers on it.",
          "Guide 3, high frequency definitions"),

    190: ("Which of the following statements is referred to as a summary of operations?",
          "The income statement summarises operations over a period. The balance sheet is "
          "a position at one date.",
          "Guide 12.3, the pro forma statements"),

    191: ("Depending on the nature of a business, a manufacturing or operation plan",
          "The older wording of this section is operations, human resources, facilities, "
          "inventory and related issues. Take the option that keeps human resources in.",
          "Guide 6.10, manufacturing or operations section"),

    192: ("Which of the following represents a long-term solvency ratio?",
          "The debt to equity ratio measures long term solvency, because it compares "
          "borrowed funds with owners' funds. The current ratio measures short term "
          "liquidity, asset turnover measures efficiency, and return on equity measures "
          "profitability.",
          "Slide 10, financing new ventures"),

    # -- Set 10: calculations ------------------------------------------------
    197: ("Topsy Turvy Company Ltd sells furniture",
          "October is the first month, so there are no prior credit sales to collect. Use "
          "the given balance on 1 October: $40,000. Every other month uses the previous "
          "month's credit sales.",
          "Guide 13.1, rule 1"),

    198: ("Using the Topsy Turvy data (beginning accounts receivable $40,000",
          "Accounts receivable for a month is the previous month's credit sales. November "
          "collects October's sales on account: $45,000.",
          "Guide 13.1, rule 1"),

    199: ("Using the Topsy Turvy data (sales on account of $45,000",
          "December collects November's sales on account: $51,750. Do not take December's "
          "own figure. That money is not due until January.",
          "Guide 13.1, rule 1"),

    200: ("Using the Topsy Turvy data (cash sales of $15,000, $17,250 and $19,838 for October, November and December), determine the budgeted cash sales for October",
          "Budgeted cash sales are read straight off the table: $15,000 for October. This "
          "is a free mark, so do not compute anything.",
          "Guide 13.1, rule 2"),

    201: ("Using the Topsy Turvy data (cash sales of $15,000, $17,250 and $19,838 for October, November and December), determine the budgeted cash sales for December",
          "Read the cash sales line for December: $19,838. The larger figures offered are "
          "total sales and total collections, which are different lines.",
          "Guide 13.1, rule 2"),

    202: ("Topsy Turvy Company Ltd collects 100 percent of accounts receivable",
          "The year-end receivable is December's credit sales, $59,513, because that is "
          "the money still uncollected on 31 December. $79,351 is December total sales, "
          "which includes cash already received.",
          "Guide 13.1, rule 4; trap list 13"),

    203: ("Topsy Turvy Company Ltd has total budgeted sales of $60,000",
          "Sales revenue for the quarter is the sum of the three total sales figures: "
          "60,000 + 69,000 + 79,351 = $208,351. Revenue is recognised on sales, not on "
          "collections.",
          "Guide 13.1, rule 5"),

    204: ("Kaneapa Company Ltd had a beginning balance of $60,000",
          "November collects October's sales on account: $45,000. The $60,000 opening "
          "balance belongs to October only.",
          "Guide 13.1, rule 1"),

    205: ("Kaneapa Company Ltd has cash sales of $20,000",
          "Read the cash sales line for November: $22,000. The credit sales figures are a "
          "separate line and are collected a month later.",
          "Guide 13.1, rule 2"),

    206: ("Dandy Electronics Company Ltd has no accounts receivable on 1 October",
          "November collects October's sales on account: GH¢337,500. Check it against "
          "the collections line: 1,321,875 - 984,375 = 337,500, which is 100 percent of "
          "October credit sales.",
          "Guide 13.1, rule 1"),

    207: ("Dandy Electronics Company Ltd has sales on account of GH",
          "The year-end receivable is December's credit sales: GH¢527,344. Note the "
          "stem in the original paper says 30 percent collection, but the table shows 100 "
          "percent. Trust the table.",
          "Guide 13.1, rule 4; trap list 14"),

    208: ("Dandy Electronics Company Ltd has total budgeted sales of GH¢1,125,000, GH¢1,406,250 and GH¢1,757,813 for October, November and December. Determine the amount of sales revenue",
          "Add the three total sales figures: 1,125,000 + 1,406,250 + 1,757,813 = "
          "GH¢4,289,063.",
          "Guide 13.1, rule 5"),

    209: ("Dandy Electronics Company Ltd has total budgeted sales of GH¢1,125,000, GH¢1,406,250 and GH¢1,757,813 for October, November and December. Compute the expected increase",
          "Divide one month by the month before: 1,406,250 / 1,125,000 = 1.25, so the "
          "increase is 25 percent. Check it on the next pair: 1,757,813 / 1,406,250 = "
          "1.25.",
          "Guide 13.1, worked example 2"),

    210: ("GoldCom Corporation has three divisions",
          "First quarter to fourth quarter is three growth steps, not four. West: 740,000 "
          "x 1.03^3 = 740,000 x 1.092727 = $808,618. Raising it to the fourth power lands "
          "you on the distractor.",
          "Guide 13.2; trap list 10"),

    211: ("GoldCom Corporation has first quarter sales of East $520,000",
          "Grow each division by three steps, then add. East 520,000 x 1.02^3 = 551,828. "
          "West 740,000 x 1.03^3 = 808,618. South 340,000 x 1.05^3 = 393,593. Total "
          "$1,754,039.",
          "Guide 13.2, worked example"),

    212: ("Hokus Pokus Company Ltd has three districts",
          "Accra: 880,000 x 1.05^3 = 880,000 x 1.157625 = $1,018,710. Three steps from "
          "the first quarter to the fourth.",
          "Guide 13.2; trap list 10"),

    213: ("Hokus Pokus Company Ltd has first quarter sales of Kumasi $650,000",
          "Kumasi 650,000 x 1.04^3 = 731,162. Accra 880,000 x 1.05^3 = 1,018,710. Cape "
          "Coast 420,000 x 1.10^3 = 559,020. Total $2,308,892.",
          "Guide 13.2, worked example"),

    214: ("Osagyefo Clothing Company Ltd wants a cash cushion",
          "Total cash available = beginning cash balance + cash receipts. The beginning "
          "balance is last month's ending balance: 34,000 + 486,000 = GH¢520,000. The "
          "cushion does not enter this line.",
          "Guide 13.3, steps 1 and 2"),

    215: ("Osagyefo Clothing Company Ltd has an August ending cash balance",
          "31,000 + 749,000 = GH¢780,000. August's ending balance becomes September's "
          "beginning balance.",
          "Guide 13.3, steps 1 and 2"),

    216: ("Osagyefo Clothing Company Ltd has total cash available of GH¢520,000",
          "Disbursements minus cash available: 540,000 - 520,000 = GH¢20,000. The "
          "result is positive, so it is a shortage and the company must borrow.",
          "Guide 13.3, step 4"),

    217: ("Osagyefo Clothing Company Ltd has total cash available of GH¢780,000",
          "780,000 - 632,000 = GH¢148,000 left over, so this is a surplus. Part of it "
          "repays the loan and part stays as the cushion.",
          "Guide 13.3, step 4"),

    218: ("Osagyefo Clothing Company Ltd has an August cash shortage",
          "When there is a shortage, borrowing = shortage + cushion: 20,000 + 40,000 = "
          "GH¢60,000. Add the cushion when borrowing; subtract it when repaying.",
          "Guide 13.3, step 5; trap list 12"),

    219: ("Osagyefo Clothing Company Ltd has a September cash surplus",
          "When there is a surplus, repayment = surplus - cushion: 148,000 - 40,000 = "
          "GH¢108,000. The cushion stays in the account.",
          "Guide 13.3, step 5; trap list 12"),

    220: ("Osagyefo Clothing Company Ltd is charged interest at 5 percent",
          "Interest is charged on the running loan balance each month, not on the new "
          "borrowing. 5 percent of 120,000, 180,000 and 72,000 gives 6,000 + 9,000 + "
          "3,600 = GH¢18,600.",
          "Guide 13.3, step 6; trap list 11"),

    221: ("Birdy-Birdy's Jewellery Shop wants a cash cushion",
          "7,139 + 180,000 = GH¢187,139. July's ending balance is August's beginning "
          "balance.",
          "Guide 13.3, steps 1 and 2"),

    222: ("Birdy-Birdy's Jewellery Shop has an August ending cash balance",
          "7,214 + 216,000 = GH¢223,214.",
          "Guide 13.3, steps 1 and 2"),

    223: ("Birdy-Birdy's Jewellery Shop has total cash available of GH¢187,139",
          "187,139 - 174,400 = GH¢12,739 left over, so August runs a surplus even "
          "though July needed a large loan.",
          "Guide 13.3, step 4"),

    224: ("Birdy-Birdy's Jewellery Shop has a September cash surplus",
          "Repayment = surplus - cushion: 23,198 - 9,000 = GH¢14,198.",
          "Guide 13.3, step 5"),

    225: ("Birdy-Birdy's Jewellery Shop is charged interest at 2 percent",
          "2 percent of each month's loan balance: 1,861 + 1,786 + 1,502 = GH¢5,149. "
          "The paper prints GH¢5,150, which is the same figure after rounding.",
          "Guide 13.3, step 6"),

    226: ("Birdy-Birdy's Jewellery Shop has September total cash available",
          "Ending cash = available - disbursements + borrowing - repayment - interest. "
          "223,214 - 200,016 - 14,198 - 1,502 = GH¢7,498. It sits just below the "
          "GH¢9,000 cushion because the interest is paid after the cushion is set.",
          "Guide 13.3, step 7"),

    # -- Set 11: because statements ------------------------------------------
    # Method: judge S1 alone, judge S2 alone, and only if both are true ask
    # whether S2 explains S1. Never read the pair as one sentence.
    227: ("Consider the two statements below. S1: Entrepreneurs dealing in low tech",
          "The sources disagree on this one. S1 is true. The compiled answer sheet marks "
          "S2 false, giving C, and the bank follows it. The 2005 official marking scheme "
          "marks A, both true with S2 explaining S1, which fits the slides: low tech "
          "products are treated that way because patents cannot protect them. Learn both "
          "readings and take the code the paper prints.",
          "2005 marking scheme item 26; EntrepreneurshipPasscoNew item 21"),

    228: ("Consider the two statements below. S1: Entrepreneurs have to be inventive geniuses",
          "S1 is false: you do not need to be an inventive genius for mid-tech work. The "
          "2005 official marking scheme marks both statements false. Treat this item as "
          "unsafe. The slides do say mid-tech products presume the application of new "
          "knowledge, which would make S2 true, and the compiled answer sheet marks A. "
          "Follow the code the paper prints.",
          "2005 marking scheme item 27; EntrepreneurshipPasscoNew item 22"),

    229: ("Consider the two statements below. S1: Differentiating high-tech from mid-tech",
          "Both are true, and S2 explains S1. The line between high-tech and mid-tech is "
          "perception, precisely because the same product reads as high-tech to one person "
          "and mid-tech to another.",
          "Guide 14, item 3; Guide 5.8"),

    230: ("Consider the two statements below. S1: New ventures establish in a market niche",
          "Both are true, and S2 explains S1. New ventures start in a niche because "
          "segmentation lets a small firm use its limited resources efficiently and "
          "without ambiguity. Note the 2005 official key marks D, which calls S1 false. "
          "That reading is hard to defend, and the compiled answer sheet marks A.",
          "EntrepreneurshipPasscoNew item 24; 2005 marking scheme item 29"),

    231: ("Consider the two statements below. S1: Market research is a fundamental part",
          "Both are true, and S2 explains S1. Market research is fundamental exactly "
          "because it settles the first question: is there demand.",
          "Guide 14, item 5"),

    232: ("Consider the two statements below. S1: Feasibility plans are best prepared by specialists",
          "Both are false. The entrepreneur prepares the plan, in consultation with "
          "specialists. And knowing finance is not the same as knowing how to operate a "
          "business. One compiled sheet says C; the 2005 key and the 2020 exam both say "
          "both false.",
          "Guide 14, item 6; Guide 6.1"),

    233: ("Consider the two statements below. S1: Prices for goods and services must coincide",
          "Both are true, and S2 explains S1. Price has to match the strategy because "
          "price itself sends a message to the customer about the product and the firm.",
          "Guide 14, item 7; Guide 8.11"),

    234: ("Consider the two statements below. S1: Seed financing is needed prior to or during",
          "Both are true, and S2 explains S1. Seed money is needed at that point because "
          "it underwrites operations, assets and business development before revenue "
          "starts.",
          "Guide 14, item 8"),

    235: ("Consider the two statements below. S1: Intrapreneur is a contrived word",
          "Both are true, and S2 explains S1. The word is contrived precisely because it "
          "is built from intra-company entrepreneur.",
          "Guide 14, item 9; Guide 4.8"),

    236: ("Consider the two statements below. S1: A good way to fail quickly in a new business",
          "Both are true, and S2 explains S1. No clear vision means no grasp of the "
          "marketing issues, and that is what makes the failure quick.",
          "Guide 14, item 10; Guide 6.15"),

    237: ("Consider the two statements below. S1: Planning is a process that never ends",
          "Both are true, and S2 explains S1. The venture keeps moving through the growth "
          "stages, so the plan has to keep moving with it.",
          "Guide 14, item 11; Guide 6.15"),

    238: ("Consider the two statements below. S1: Most technical entrepreneurs tend to start",
          "Both are true, and the key treats S2 as the explanation. Founders stay near "
          "their previous work because success rests on a business ideology built up in "
          "that field. This is the corridor principle in another form.",
          "Guide 14, item 12; Guide 5.4"),

    239: ("Consider the two statements below. S1: There are more male entrepreneurs",
          "Both are true, and S2 explains S1. Men tend to launch early, while women tend "
          "to start after their children are grown, which shortens the years available.",
          "Guide 14, item 13"),

    240: ("Consider the two statements below. S1: Market potential is critically influenced by the timing",
          "Both are true, and S2 explains S1. Timing decides when the product enters, how "
          "it is priced, how it is distributed and how it is promoted, so it drives the "
          "potential.",
          "Guide 14, item 14; Guide 8.12"),

    241: ("Consider the two statements below. S1: An extraordinary change is taking place",
          "Both are true, and S2 explains S1. Demographic change is one of the four "
          "sources of change, and it creates the demand for new programmes and services "
          "that privatisation then fills.",
          "Guide 14, item 15; Guide 4.2"),

    242: ("Consider the two statements below. S1: All financial forecasts and projections",
          "Both are true, and S2 explains S1. Forecasts rest on assumptions precisely "
          "because future outcomes cannot be predicted.",
          "Guide 14, item 16; Guide 12.4"),

    243: ("Consider the two statements below. S1: Investors put greater emphasis on the entrepreneurial team",
          "Both are true, but S2 does not explain S1. S2 only restates the same "
          "preference as a venture capital saying. A restatement is not a reason, so the "
          "answer is B, not A.",
          "Guide 14, item 17; Guide 2, code 2"),

    244: ("Consider the two statements below. S1: Inventors often place more emphasis",
          "Both are false. Lenders and investors run the background checks, not inventors. "
          "And equity investors look to cash out in about five years, not in a year or "
          "two.",
          "Guide 14, item 18; Guide 11.5"),

    # -- added 2026: questions found in the scans that the bank had missed ----
    24: ("There are several thoughts about entrepreneurs that have been proven to be more",
         "The slides call these myths. Entrepreneurs are not misfits, and the born-or-made "
         "question is settled on the side of made: background, education, family and "
         "career shape them. They also rarely strike it rich on one flash of genius, "
         "because most ventures start slow and change in steps. Statement (i) is not a "
         "myth at all. The slides say entrepreneurs make their own luck by working hard.",
         "Slides 2.62 to 2.67, popular myths"),

    25: ("Entrepreneurs tend to be strategic thinkers who recognise changes",
         "The slides name five sources of change: scientific knowledge, process "
         "innovations, industrial changes, market changes and demographic changes. "
         "Statements (ii) and (iii) come straight off that list. Shop changes is not on "
         "it, so (i) fails.",
         "Slides 2.57 to 2.61"),

    26: ("The concept of entrepreneurship (i) has given us a new direction",
         "The word dates from 17th century France and the literature on it is long, so "
         "entrepreneurship has been around a very long time and has certainly not just "
         "been discovered. Statement (ii) is the only false one.",
         "Slides 1.13 to 1.24, history of entrepreneurship"),

    27: ("Entrepreneurship (i) was derived from the 17th century French word",
         "The word comes from the 17th century French entreprendre, meaning to undertake. "
         "Early entrepreneurs were contractors who bore the risk of profit or loss, and "
         "the slides list builders among them. Statement (ii) fails on its second half: "
         "business students did not discover the term.",
         "Slides 1.16 and 1.17"),

    28: ("Entrepreneurs are",
         "Every KNUST paper marks high risk takers, both the circled 2015 script and the "
         "Canvas paper. Note the tension: Table 1-1 in the overview slides calls the "
         "successful entrepreneur able to take calculated risk. Answer what the paper "
         "marks, not what the table says.",
         "2015 paper, circled; Canvas paper, selected"),

    29: ("Entrepreneurs",
         "The papers mark are the life of the party. The other options all describe a "
         "withdrawn person, which the papers reject. No printed key exists for this item.",
         "Guide 4.9, recurring facts"),

    45: ("Innovation is the development process of translating a new idea",
         "Innovation is not invention. The slides separate them: invention is the verified "
         "result of a creative idea, while innovation converts something new into useful "
         "goods or services. Analytical planning (ii) and organising resources (iii) are "
         "innovation-process elements. Turning an idea into an invention is not.",
         "Slide 2.40; Guide 5.3"),

    46: ("A number of industrial studies reveal that for a technological innovation",
         "The conditions call for adequate support from external sources, not a little "
         "support, so (i) fails as printed. A clear need from enough consumers, and a "
         "realised innovation that gives value to society, are both real conditions.",
         "Derived; no printed key exists for this item"),

    71: ("The information needed to develop the financial section of a business plan",
         "The financial section is built from the rest of the plan. Sales come from the "
         "market research and market plan segments, costs come from the operations or "
         "manufacturing segment, and the product description sets what is being sold.",
         "Notes p14 to p24; Guide 6.8"),

    110: ("Used as a catchall term, product in marketing terms includes",
          "Product in marketing is deliberately broad. It covers the business concept, the "
          "physical object or service with its packaging, brand name and warranty, and the "
          "physical attributes that shape how a customer sees it.",
          "Guide 8.8, the expanded view of a product"),

    111: ("As part of a market plan, a marketing strategy provides guidelines",
          "The strategy sets the marketing program, states the expected results and who is "
          "responsible for which resources, and says how the enterprise will be "
          "controlled. All three are guidelines the strategy supplies.",
          "Guide 8.10, the marketing plan"),

    168: ("Resources expected to produce current and future benefits are referred to as",
          "That is the accounting definition of an asset. Capital and shareholding name "
          "where the money came from, and a liability is an obligation the venture owes.",
          "Canvas paper, selected; Notes p19 to p23"),

    193: ("In preparing the pro forma balance sheet, the entrepreneur will require",
          "The notes set out the flow. Operating budgets feed the financial statement "
          "budgets, the capital budget feeds several operating budgets and the cash "
          "budget, and the pro forma income and cash flow statements supply the closing "
          "balances the balance sheet needs.",
          "Notes p15 and p19 to p22"),

    194: ("A statement of estimated income and expenses over a specified period",
          "That is the general definition of a budget. An operating budget, a capital "
          "budget and a master budget are all particular kinds of budget, so the general "
          "term is the better answer.",
          "Notes p14; 2005 key, question 89"),

    195: ("Which of the following is a formal plan expressed in numerical terms",
          "A budget states expected results or requirements in financial or numerical "
          "terms. A financial statement reports what already happened. A budget plans what "
          "should happen.",
          "Notes p14; Canvas paper, selected"),

    196: ("Administration plans generally cover a period of",
          "The Canvas paper marks less than 1 year. The phrase administration plans "
          "appears nowhere in the notes or the slides, so this answer rests on the paper "
          "alone. Treat it as the weakest item in the bank.",
          "Canvas paper, selected; not found in the course materials"),
}
