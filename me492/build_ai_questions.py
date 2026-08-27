# -*- coding: utf-8 -*-
"""Build 100 AI-generated ME 492 questions -> ai-generated-100.json

Every item is grounded in 1-guides/01-STUDY-GUIDE.md, the lecture decks or the
2025 course notes. The mix copies the philosophy of the real papers:
  70 plain single-answer, 22 i/ii/iii combination, 8 "because" pairs.
The combination and "because" answers copy the measured skew of the past papers.
"""
import json

C = "GH¢"

ALL = "i, ii and iii are correct"
I_II = "i and ii only are correct"
I_III = "i and iii only are correct"
II_III = "ii and iii only are correct"
I_O = "i only is correct"
II_O = "ii only is correct"
III_O = "iii only is correct"


def combo_opts(correct):
    if correct == II_III:
        return [ALL, I_II, II_III, I_O, III_O]
    if correct == II_O:
        return [ALL, II_III, I_O, II_O, III_O]
    return [ALL, I_II, I_III, I_O, III_O]


AR = ["both statements are TRUE and the second is a correct explanation of the first",
      "both statements are TRUE and the second is NOT a correct explanation of the first",
      "the first statement is TRUE and the second is FALSE",
      "the first statement is FALSE and the second is TRUE",
      "both statements are FALSE"]

Q = []


def plain(src, text, correct, distractors, expl):
    Q.append((src, text, correct, list(distractors), expl))


def combo(src, text, correct, expl):
    Q.append((src, text, correct, [o for o in combo_opts(correct) if o != correct], expl))


def because(src, s1, s2, correct, expl):
    text = ("Consider the two statements below. S1: %s BECAUSE S2: %s "
            "Select the correct response." % (s1, s2))
    Q.append((src, text, correct, [o for o in AR if o != correct], expl))


# ------------------------------------------- 1. Entrepreneurship and free enterprise (8)
plain("Guide 4.1, the economists",
      "Jean Baptiste Say's account of the entrepreneur combined which two earlier ideas?",
      "Cantillon's economic risk taker and Adam Smith's industrial manager",
      ["Schumpeter's innovator and Drucker's opportunity seeker",
       "Menger's resource converter and John Stuart Mill's risk bearer",
       "Adam Smith's enterpriser and Schumpeter's creative destroyer",
       "Cantillon's resource allocator and Carl Menger's value creator"],
      "Say joined Cantillon's economic risk taker to Smith's industrial manager. He added exceptional insight into the needs of society, and said the entrepreneur both influences society and is influenced by it.")
plain("Guide 4.9, recurring facts",
      "The most common reason given for the failure of a new business is",
      "inexperience",
      ["a shortage of bank credit", "poor location", "high interest rates", "government regulation"],
      "Inexperience heads the list. The related fact is that a business started from scratch carries a higher risk of failure than one that is bought.")
plain("Guide 5.4, windows and corridors",
      "Most technical entrepreneurs start businesses close to their previous career work. This observation is known as",
      "the corridor principle",
      ["the window of opportunity", "creative destruction", "income substitution", "the technology spectrum"],
      "The corridor principle. Successful ventures evolve from entrepreneurs already positioned in similar or related work, so they move quickly when a window opens. A window is the time horizon, not the position.")
plain("Guide 4.8, intrapreneurship",
      "In corporate entrepreneurship, managers combine resources in unusual ways and also",
      "commit time and energy and risk their careers",
      ["take personal investment risks with their own savings",
       "assume unlimited liability for the new product line",
       "acquire an ownership position in the parent company",
       "provide the collateral for the venture's borrowing"],
      "They risk time, energy and their careers. They do not take a personal investment risk. The company carries the money risk. That is the standard trap in this item.")
combo("Slides 1.16 and 1.17, the origin of the word",
      "The word entrepreneurship\n(i) comes from the 17th century French entreprendre, meaning to undertake\n(ii) was discovered by business students studying commercial history\n(iii) referred to contractors and builders who bore the risk of profit or loss",
      I_III,
      "Statements (i) and (iii) are on the slides. Statement (ii) is the added clause that makes it false. The word was not discovered by business students.")
combo("Guide 4.10, the concept of entrepreneurship",
      "The concept of entrepreneurship\n(i) has given enterprise a new direction\n(ii) has only just been discovered by modern economists\n(iii) has been around for a very long time",
      I_III,
      "New direction and long standing. Statement (ii) contradicts (iii): Cantillon wrote in the 18th century, so the concept is not new.")
combo("Guide 4.7, effects on the economy",
      "Entrepreneurship affects the economy by\n(i) altering the direction of national economies and ensuring their stability\n(ii) introducing quantum leaps in technology and new systems of services\n(iii) forcing the reallocation of resources from existing uses to new and more productive uses",
      ALL,
      "All three are on the slides. When every statement restates a listed effect, take all three.")
combo("Guide 4.5, popular myths",
      "Several thoughts about entrepreneurs have proved to be more myth than fact. These include\n(i) that entrepreneurs struggle to succeed and get their ideas by hard work\n(ii) that entrepreneurs are mavericks and misfits, and that entrepreneurs are born and not made\n(iii) that entrepreneurs strike it rich on the first flash of genius",
      II_III,
      "Statement (i) is the truth, not a myth. The slides say entrepreneurs make their own luck by working hard. Mavericks and misfits, born not made, and the first flash of genius are all myths.")

# ------------------------------------------- 2. Creativity and innovation (8)
plain("Guide 5.2, the five stages",
      "A person who embarks on a conscious search for the knowledge needed to bring an idea to life is in which stage of the creative process?",
      "preparation",
      ["incubation", "illumination", "verification", "idea germination"],
      "Preparation is the conscious search. Incubation is the subconscious one. Keep the word conscious attached to preparation.")
plain("Guide 5.1, definitions",
      "Creativity differs from innovation in that creativity is",
      "the ability to bring something new into existence",
      ["the process of doing new things",
       "the verified result of a creative idea",
       "the conversion of something new into useful goods or services",
       "the transformation of creative ideas into useful applications"],
      "Creativity is an ability, not an activity. The other four options define innovation or invention. Creativity is the seed; innovation is the process.")
plain("Guide 5.5, the three key people",
      "Technological innovation depends on three key people. They are",
      "the creative source, the champion and the sponsor",
      ["the inventor, the investor and the champion",
       "the creative source, the entrepreneur and the promoter",
       "the sponsor, the financier and the project manager",
       "the inventor, the sponsor and the venture capitalist"],
      "Only this trio is correct. Reject any option that swaps in the inventor, the investor or the promoter.")
combo("Guide 5.2, the five stages; trap list 5",
      "A person is in the verification stage of the creative process when he or she\n(i) applies or tests the idea to prove that it has value\n(ii) has a sudden flash that the idea has merit\n(iii) subconsciously assimilates information about the idea",
      I_O,
      "Only (i). The sudden flash is illumination and the subconscious work is incubation. This is the trap that the 2005 key punished.")
combo("Slide 2.40; Guide 5.3, the innovation process",
      "Innovation is the development process of translating a new idea into a commercial reality. It involves\n(i) the translation of the idea into a new invention\n(ii) persistence in analytically working out the details of product design, marketing, finance and operations\n(iii) obtaining materials and manufacturing capability, staffing operations and establishing an organisation",
      II_III,
      "Statements (ii) and (iii) are analytical planning and organising resources. Statement (i) fails because innovation is not invention. Invention is the verified result of a creative idea.")
combo("Guide 5.6, brainstorming rules",
      "The rules of brainstorming state that\n(i) no criticism is allowed by anyone in the group, and free wheeling is encouraged\n(ii) ideas found to be without merit are discarded as the session runs\n(iii) a high quantity of ideas is wanted, and combining and improving ideas is encouraged",
      I_III,
      "Nothing is judged inside the session, so (ii) is false. Quantity first, judgement later. The period for generating ideas is fixed in advance.")
because("Guide 5.1, definitions",
        "Creativity is a prerequisite for innovation.",
        "Innovation is the transformation of creative ideas into useful applications.",
        AR[0],
        "Both are true, and S2 explains S1. Innovation has nothing to transform until creativity supplies the idea.")
because("Guide 5.8, the technology spectrum",
        "A majority of new products evolve at the low-tech end of the technology spectrum.",
        "Entrepreneurs have to be inventive geniuses to pursue mid-tech innovations.",
        AR[2],
        "S1 is true. S2 is false: mid-tech products presume the application of new knowledge, but they do not require an inventive genius. So the first is true and the second is false.")

# ------------------------------------------- 3. Feasibility and the business plan (11)
plain("Guide 6.1, who writes the plan",
      "The feasibility plan for a new venture is best prepared by",
      "the entrepreneur, in consultation with specialists",
      ["a firm of management consultants",
       "the financial expert engaged by the lender",
       "the marketing department of the parent company",
       "an accountant acting for the investors"],
      "The entrepreneur has the vision and the motivation and can articulate the information. Specialists advise. They do not take the job over.")
plain("Guide 6.7, the cover page",
      "Which single item must the introductory or cover page of a business plan carry?",
      "a statement of confidentiality of the report",
      ["a summary of the market research findings",
       "the pro forma balance sheet",
       "the resumes of the partners",
       "a literature review of the industry"],
      "The cover page carries the name and address, the amount of financing required, the contacts, a brief description of the concept, and a confidentiality statement. When one answer is wanted, take the confidentiality clause.")
plain("Guide 6.5, the first element of information",
      "The first element of information an entrepreneur needs when planning a new venture is",
      "the market potential for the product or service",
      ["the basic operational needs of the venture",
       "an evaluation of the entrepreneurial team",
       "the expected profitability in the first year",
       "the amount of external financing available"],
      "Market potential comes first. Without a market the other three questions do not arise.")
plain("Guide 6.11, the appendix",
      "The appendix of a business plan holds",
      "resumes of partners, facility layouts and partnership agreements",
      ["the executive summary and the venture definition",
       "the pro forma statements and the capital budget",
       "the competitive analysis and industry trends",
       "the marketing programme and the promotional mix"],
      "The appendix carries supporting documents. When only one option is allowed, pick the resumes of partners.")
plain("Guide 6.12, what the plan is for",
      "A business plan is prepared primarily",
      "to give information to lenders and investors",
      ["to guide the entrepreneur through daily operations",
       "to inform suppliers of the venture's requirements",
       "to satisfy a legal requirement for registration",
       "to record the history of the business concept"],
      "Lenders and investors are the primary audience. The plan can also provide direction, prove feasibility and attract money, but the examined single answer is the information to lenders and investors.")
plain("Guide 6.13, why plans go out of date",
      "The single most common reason a business plan goes out of date is",
      "changes in the market and the industry",
      ["the loss or addition of key members of the team",
       "a change in the location of the venture",
       "poor articulation of the business concept",
       "a delay in obtaining the required financing"],
      "The market and the industry move. The other three appear on the list but the single best answer is the market and industry change.")
plain("Guide 6.16, security of the plan",
      "Many copies of a business plan circulate among outsiders. The entrepreneur counters this risk with",
      "a non-disclosure statement",
      ["a patent application", "a trademark registration", "a restrictive covenant", "a disclosure document"],
      "A non-disclosure statement. A disclosure document is a patent office filing and is a different instrument entirely.")
plain("Guide 6.4, barriers to success",
      "In checking the barriers to success before writing the plan, the entrepreneur examines",
      "the market, finance and operations, the business concept and the team, and the goals and objectives of the venture",
      ["the market, finance and operations only",
       "the business concept and the entrepreneurial team only",
       "the goals and objectives of the venture only",
       "the legal form of the business and its tax position"],
      "All the listed groups are checked. When the paper spells them out as one long option, take the combined option.")
combo("Guide 6.6, the executive summary",
      "The executive summary of a business plan is written\n(i) to stimulate the interest of the reader\n(ii) in a concise and convincing manner covering the key points of the plan\n(iii) after the whole plan has been written",
      ALL,
      "All three. It is written last even though it is read first, and it runs to about two or three pages.")
combo("Guide 6.9, environmental and industry analysis",
      "The environmental and industry analysis section deals with\n(i) an assessment of the location of the venture and its immediate area\n(ii) an assessment of competitive strategies and industry trends\n(iii) an assessment of external uncontrollable variables that may affect the business",
      ALL,
      "All three. The 2020 exam confirmed the combined answer.")
because("Guide 6.1; Guide 16, conflicts",
        "Feasibility plans are best prepared by specialists.",
        "Specialists such as financial experts know how to operate businesses.",
        AR[4],
        "Both are false. The entrepreneur prepares the plan, and a financial expert knows finance, not how to run a business. Some compiled sheets give C. The 2005 key and the 2020 exam both give both false.")

# ------------------------------------------- 4. Growth stages and the start-up (6)
plain("Guide 7.1, the four growth stages",
      "Reality shock sets in as the entrepreneur positions the business to compete in the real world. This describes which stage?",
      "start-up",
      ["pre-start-up", "early growth", "later growth", "maturity"],
      "Start-up covers the initial business operations. Pre-start-up is the assembly of resources before the doors open.")
plain("Guide 7.1, the four growth stages",
      "The assembly of resources and the organising of the new venture for opening is the",
      "pre-start-up stage",
      ["start-up stage", "early growth stage", "later growth stage", "verification stage"],
      "Pre-start-up. Verification belongs to the creative process, not to the growth stages.")
plain("Guide 7.3, benchmark considerations",
      "The two benchmark considerations for the start-up stage are",
      "meeting operating objectives and positioning the venture for long-term growth",
      ["raising capital and recruiting staff",
       "controlling costs and increasing market share",
       "registering the business and obtaining licences",
       "building the brand and setting the pricing policy"],
      "A fixed answer, confirmed in the 2007, 2015 and 2020 papers.")
plain("Guide 7.4, start-up operating objectives",
      "The operating objectives of the start-up stage are",
      "sales, revenue, growth and position",
      ["cost, quality, delivery and safety",
       "liquidity, solvency, profitability and gearing",
       "product, price, distribution and promotion",
       "recruitment, training, appraisal and reward"],
      "Sales, revenue, growth and position. Product, price, distribution and promotion are the marketing functions, not the start-up objectives.")
plain("Guide 7.6, reducing the financial burden",
      "The financial burden on a new venture before start-up is reduced by",
      "planning assets carefully",
      ["cutting production capacity", "reducing the number of staff", "paying low salaries", "delaying supplier payments"],
      "Careful asset planning. The other four cut the venture's capacity to trade instead of cutting the money tied up in it.")
because("Guide 7.1, the four growth stages",
        "A reality shock is felt by the entrepreneur during the start-up stage.",
        "The start-up stage is where the entrepreneur first positions the business to compete in the real world.",
        AR[0],
        "Both are true, and S2 explains S1. Pre-start-up assembles resources in private. Start-up meets the real market, which is where the shock comes from.")

# ------------------------------------------- 5. Market research and the marketing plan (14)
plain("Guide 8.1, research versus plan",
      "The main difference between market research and analysis and the market plan is that",
      "market research gathers the information, and the market plan then uses it in a marketing strategy to attract customers",
      ["market research is done after opening, and the market plan before opening",
       "market research is prepared by specialists, and the market plan by the entrepreneur",
       "market research covers competitors, and the market plan covers customers",
       "market research is part of the appendix, and the market plan part of the main body"],
      "Learn this sentence word for word. Research gathers, the plan uses.")
plain("Guide 8.6, results of good market research",
      "Market research culminates in",
      "a sales forecast",
      ["a cash budget", "a pro forma balance sheet", "a competitive analysis", "a promotional mix"],
      "The sales forecast. It is also the first step in preparing the operating budget, which is why this item links the marketing block to the finance block.")
plain("Guide 8.2, market research activities",
      "The objective of market research is to establish that a ________ exists.",
      "market",
      ["niche", "customer scenario", "sales forecast", "distribution channel"],
      "A market. The niche and the customer scenario are found inside the market once the market itself is proved.")
plain("Guide 8.14, marketing research after opening",
      "Marketing research undertaken after a new venture opens its doors is called",
      "competitive analysis",
      ["market survey", "customer scenario", "product/market survey", "situation analysis"],
      "Competitive analysis. Note the pairing: a competitive analysis carried out before opening belongs to the pre-start-up stage.")
plain("Guide 8.5, a market niche",
      "A carefully defined segment of a broader market that sets the positioning of a product or service is",
      "a market niche",
      ["a customer scenario", "a distribution channel", "a market survey", "a promotional mix"],
      "A market niche. Answer this one by text. Its letter has moved between papers more than any other item.")
plain("Guide 8.7, distribution",
      "A distribution system is",
      "the physical process of getting goods to market and the process of locating services",
      ["the selection of promotional methods consistent with the marketing strategy",
       "the process of taking raw materials through production",
       "the planned process of determining prices and how prices change",
       "the consolidation of all communications into a single message"],
      "Getting goods to market and locating services. Taking materials through production is manufacturing, not distribution. The channels are consumer, industrial and service.")
plain("Guide 8.9, promotion and advertising",
      "Integrated Marketing Communications seeks to",
      "consolidate all communications to present a single, focused marketing, sales or image message",
      ["use an assortment of forms to deliver a variety of messages",
       "convince someone to walk in your door",
       "select promotional methods consistent with a grand marketing strategy",
       "determine prices and how prices will change in the field"],
      "A single focused message. The assortment of forms delivering a variety of messages is the exact opposite, and it is the printed distractor.")
combo("Guide 8.6, results of good market research",
      "The result of good market research is\n(i) a well defined sales forecast\n(ii) a good estimate of the revenue the venture will earn\n(iii) well defined investment needs for the venture",
      I_O,
      "Only (i). The sales forecast is the stated result. Revenue estimates and investment needs are produced later, by the budgets.")
combo("Guide 8.9, advertising for a start-up",
      "Advertising for a start-up business seeks to\n(i) make a satisfied customer of the buyer\n(ii) sell to someone even if that person cannot afford the product\n(iii) convince someone to walk in your door",
      III_O,
      "Only (iii). At start-up the job of advertising is to get the customer through the door. Satisfaction is the job of the product, and (ii) is simply bad practice.")
combo("Guide 8.8, the expanded view of a product",
      "In marketing, the term product covers\n(i) the business concept, such as fast-food franchising\n(ii) the physical object or service sold, with its packaging, image, brand name and warranty\n(iii) the physical attributes that shape how customers see it: colours, shapes, sizes and materials",
      ALL,
      "All three. Product is a catchall term in marketing, and every one of the three layers belongs to it.")
combo("Guide 8.8b, what a marketing strategy provides",
      "As part of the market plan, the marketing strategy gives guidelines on\n(i) a marketing programme that addresses the marketing activities\n(ii) the expected results, the allocation of resources and who is responsible\n(iii) the ways in which the enterprise will be controlled",
      ALL,
      "All three. The strategy sets the programme, the results and resources, and the controls.")
combo("Guide 8.13, customer profile",
      "Developing a clear profile of potential customers involves looking at\n(i) age and sex\n(ii) income status\n(iii) locating the potential customer base",
      ALL,
      "All three. The profile describes who they are and where they are.")
because("Guide 8.5, a market niche",
        "New ventures establish themselves in a market niche.",
        "Companies establish segmentation strategies so that efficient use of resources can be achieved without ambiguity.",
        AR[0],
        "Both are true, and S2 explains S1. A new venture cannot serve a broad market efficiently, so it segments and takes a niche.")
because("Guide 8.12, timing",
        "Market potential is critically influenced by the timing of new products or services.",
        "Timing pertains to when products are introduced, how they are priced, how they are distributed and how they are promoted.",
        AR[0],
        "Both are true, and S2 explains S1. Timing runs through all four marketing functions, so it drives market potential.")

# ------------------------------------------- 6. Intellectual property (4)
plain("Guide 9.1, patents",
      "A patent search is carried out to determine",
      "whether the inventor's creation already exists and remains actively protected under the law",
      ["whether the invention is commercially viable",
       "whether the inventor has the resources to exploit the patent",
       "the market value of the patent to a licensee",
       "the period for which a trademark can be renewed"],
      "A patent search asks whether the creation already exists and is still protected. It is a legal check, not a commercial one.")
plain("Guide 9.2, the disclosure document",
      "A Disclosure Document is",
      "a statement to the patent office by the inventor declaring the intent to patent an idea",
      ["a granted property right over an invention",
       "the confidentiality clause on the cover page of a business plan",
       "the published notice of a trademark in the official gazette",
       "the written record of a partnership agreement"],
      "A statement of intent to patent. It becomes important when an infringement occurs. It is not itself a patent.")
combo("Guide 9.1, patents",
      "A plant patent\n(i) runs for a fixed term of 17 years\n(ii) is granted for hybrid roses\n(iii) is granted for food grains",
      II_III,
      "Hybrid roses and food grains. The 17 year term is the distractor that gets attached to this item, and it is not the answer the papers mark.")
combo("Guide 9.4, product liability",
      "The best protection against product liability is\n(i) to produce safe products\n(ii) to warn customers of potential hazards\n(iii) to guarantee zero defects in every unit sold",
      I_II,
      "Safe products and clear warnings. Zero defects is not achievable, so no venture can offer it as a protection.")

# ------------------------------------------- 7. Organising the venture and forms of ownership (11)
plain("Guide 10.1, designing the organisation",
      "After the legal form has been chosen, the first step in designing the organisation is to",
      "decide the organisational structure",
      ["write the job descriptions", "carry out the job analysis",
       "set the job specification and selection criteria", "recruit and train the employees"],
      "Structure first. Then job analysis identifies the major activities, then the job description, then the job specification, then training.")
plain("Guide 10.1, designing the organisation",
      "The major activities of a new venture are identified through",
      "job analysis",
      ["job description", "job specification", "job evaluation", "job rotation"],
      "Job analysis identifies the activities. The job description then writes them down, and the job specification sets what the holder must be.")
plain("Guide 10.4, sole proprietorship",
      "The main disadvantage of the sole proprietorship is",
      "unlimited legal and financial liability",
      ["limited financial resources", "a limited life span", "difficulty in management", "few fringe benefits"],
      "Unlimited liability. The other four are genuine disadvantages, but the examined main one is the unlimited legal and financial liability.")
plain("Guide 10.5, partnership",
      "A limited partner is one who",
      "invests in the firm, has limited liability, and cannot legally help manage the company",
      ["manages the firm and has unlimited liability",
       "trades the partnership interest like a corporate share and is taxed as a corporation",
       "joins the partnership for a fixed period and then withdraws",
       "guarantees the debts of the other partners jointly and severally"],
      "The limited partner puts in money and stays out of management. The moment a limited partner manages, the protection is lost. The general partner manages and carries unlimited liability.")
plain("Guide 10.6, corporation",
      "A corporation is chartered by the state to conduct business as",
      "an artificial person with liability separate from its owners",
      ["a voluntary association of two or more owners",
       "an extension of the personal estate of its founder",
       "a partnership taxed at the shareholder level only",
       "a franchise operating under a parent company's system"],
      "A legal entity, an artificial person, owned by shareholders, with perpetual life and limited liability. Separate liability is the point of the form.")
plain("Guide 10.7, boards",
      "By law, which form of business is obliged to have a formal board of directors?",
      "an incorporated company",
      ["a sole proprietorship", "a general partnership", "a limited partnership", "a franchised outlet"],
      "Only incorporated companies. Other forms may keep a board of advisors, but no law compels them.")
plain("Guide 10.9, franchising",
      "The party that originates a business system and supplies the package of services, products, training and support for a fee and royalties is the",
      "franchisor",
      ["franchisee", "general partner", "sponsor", "venture capitalist"],
      "The franchisor originates and supplies. The franchisee is the acquiring owner. The franchise is the business system created by the contract between them.")
combo("Guide 10.2, selecting the legal form",
      "Selecting a legal form of business involves at least three criteria. They are\n(i) the preferences of the entrepreneur\n(ii) the profile of the enterprise\n(iii) the advantages and disadvantages of the legal business entity",
      ALL,
      "All three. Preferences, profile and the trade-offs of the entity itself.")
combo("Guide 10.4, sole proprietorship",
      "Besides the ease of starting and ending it, the sole proprietorship offers\n(i) an expanded network of contacts\n(ii) a strong profile for obtaining debt financing\n(iii) autonomy of control, decision making and administration",
      III_O,
      "Only (iii). A sole proprietor has neither an expanded network nor a strong borrowing profile. Autonomy is the real advantage. Read the printed option (iii) first: in 2005 it read inexpensive and self directing, which is also true.")
combo("Guide 10.5, partnership",
      "The disadvantages of a partnership include\n(i) a complicated form of administration\n(ii) unlimited legal liability for the business by all parties, jointly and severally\n(iii) limited access to external resources",
      II_O,
      "Only (ii). A partnership is simple to administer, and it has more access to resources than a sole proprietorship, not less. Joint and several unlimited liability is the real disadvantage.")
combo("Guide 10.7, boards",
      "Beyond decision making, the directors of a new venture serve as\n(i) members of an expanded social network\n(ii) disturbance handlers and resource allocators\n(iii) mentors and professional advisors",
      ALL,
      "All three. Directors bring contacts, they settle disturbances and allocate resources, and they mentor the entrepreneur.")

# ------------------------------------------- 8. Financing the new venture (13)
plain("Guide 11.1, the three capital requirements",
      "Money required to purchase physical facilities such as buildings, fixtures and equipment is",
      "fixed capital",
      ["working capital", "liquid capital", "replacement capital", "development capital"],
      "Fixed capital is the long term investment in facilities. It is financed by long term credit.")
plain("Guide 11.1, the three capital requirements",
      "Money required for day to day operating costs such as rent, utility bills, inventories and payroll is",
      "working capital",
      ["fixed capital", "liquid capital", "seed capital", "replacement capital"],
      "Working capital. It is financed by short term credit, which is self liquidating because the sales it funds generate the cash to repay it.")
plain("Guide 11.1, the three capital requirements",
      "Money held in reserve for emergencies, as cash or as disposable securities such as stocks, bonds and certificates of deposit, is",
      "liquid capital",
      ["working capital", "fixed capital", "retained earnings", "net worth"],
      "Liquid capital, also called fluid capital. The three requirements are asked as three separate questions, so learn all three definitions.")
plain("Guide 11.2, the three types of credit",
      "Entrepreneurs use which type of credit to purchase major fixed capital such as buildings and land?",
      "long term credit",
      ["short term credit", "intermediate term credit", "trade credit", "revolving credit"],
      "Long term credit runs beyond five years. Intermediate term credit, one to five years, buys the smaller fixed capital such as fixtures and equipment.")
plain("Guide 11.3, debt versus equity",
      "The course notes give debt financing a second name. That name is",
      "asset-based financing",
      ["ownership financing", "equity financing", "seed financing", "replacement capital"],
      "Notes page 11 reads debt financing, also called asset-based financing. The asset is the collateral, which is why the name attaches to debt and never to equity. One compiled answer sheet calls asset-based financing equity. Two printed keys and the notes say debt.")
plain("Guide 11.3, debt versus equity",
      "When interest rates are low, which form of financing lets the entrepreneur keep a larger ownership portion and earn a greater return on equity?",
      "debt financing",
      ["equity financing", "venture capital", "a government grant", "a share issue to employees"],
      "Debt. Cheap borrowing buys the asset without giving away ownership. Equity always costs a share of the business.")
plain("Guide 11.4, internal versus external funds",
      "A government grant to a new business is classified as",
      "an external fund",
      ["an internal fund", "a form of equity held by the state", "retained earnings", "a reduction in working capital"],
      "External. Internal sources are profits, the sale of assets, a reduction in working capital, extended payment terms and faster collection of receivables.")
plain("Guide 11.5, the sources ranked",
      "Which source of funds is the least expensive in terms of cost and control, and is absolutely essential to attracting outside funding?",
      "personal funds",
      ["family and friends", "commercial bank loans", "venture capital", "government grants"],
      "Personal funds. No outside party will commit money until the entrepreneur has committed their own.")
plain("Guide 11.5, the sources ranked",
      "By far the most frequently used source of short-term funds, where collateral is available, is",
      "a commercial bank",
      ["a venture capital firm", "family and friends", "a government agency", "a development finance house"],
      "Commercial banks, when collateral is available. Venture capital is for the higher risks such as start-up situations.")
plain("Guide 11.6, terms to know",
      "The integration and synchronisation of the various financial activities so that all functions work towards common objectives is",
      "financial co-ordination",
      ["budgeting", "strategic planning", "capital budgeting", "financial accounting"],
      "Financial co-ordination. Budgeting is the narrower process of co-ordinating the finances of all areas of the venture.")
plain("Guide 11.6, terms to know",
      "Restrictions written into a loan agreement are called",
      "covenants",
      ["collateral", "royalties", "guarantees", "debentures"],
      "Covenants. Collateral is the asset pledged, not the restriction on the borrower's conduct.")
combo("Guide 11.5, the sources ranked",
      "Determining which source of funding an entrepreneur uses depends on\n(i) the type of financing needed, whether short, intermediate or long term\n(ii) the portability of the money once it is raised\n(iii) the entrepreneur's particular financial condition",
      I_III,
      "Statements (i) and (iii), together with the nature and size of the business. Money portability is the invented option that the except version of this question relies on.")
because("Guide 11.5, the sources ranked",
        "Personal funds are absolutely essential to attracting outside funding for a new venture.",
        "Banks, private investors and venture capitalists look for the entrepreneur's own commitment before they commit their money.",
        AR[0],
        "Both are true, and S2 explains S1. Personal funds signal commitment, which is why they unlock the other sources.")

# ------------------------------------------- 9. Budgets and the pro forma statements (13)
plain("Guide 12.1, levels of financial planning",
      "The process that co-ordinates the finances of all areas of the new venture is",
      "budgeting",
      ["cost accounting", "financial accounting", "auditing", "financial co-ordination"],
      "Budgeting. Cost accounting and financial accounting record what has happened. A budget plans what should happen.")
plain("Guide 12.1, levels of financial planning",
      "Deciding whether to buy or to lease equipment is a matter of",
      "capital budgeting",
      ["strategic planning", "operations budgeting", "cash budgeting", "financial accounting"],
      "Capital budgeting, the intermediate level. Strategic planning is long term and covers the scope of the venture and the choice of niche.")
plain("Guide 12.1, levels of financial planning",
      "Deciding which market niche should be profitable is a matter of",
      "strategic planning",
      ["capital budgeting", "operations budgeting", "tactical budgeting", "market research"],
      "Strategic planning, the long term level. The three levels are strategic planning, capital budgeting and operations budgeting.")
plain("Guide 12.2, the master budget",
      "The three major budget categories under the master budget are",
      "operating budgets, capital budgets and financial statement budgets",
      ["sales budgets, cash budgets and inventory purchases budgets",
       "strategic budgets, tactical budgets and operational budgets",
       "fixed budgets, flexible budgets and rolling budgets",
       "income budgets, expenditure budgets and capital budgets"],
      "Operating, capital and financial statement budgets. Financial statement budgets are also called pro forma statements.")
plain("Guide 12.2, the master budget",
      "The master budget normally covers",
      "a one-year time span",
      ["a five-year time span", "a three-month time span", "a period of more than one year", "an indefinite period"],
      "One year. Do not confuse this with the capital budget, which evaluates expenditure affecting the business for more than one year.")
plain("Guide 12.2, the master budget",
      "Perpetual or continuous budgeting uses",
      "a 12-month reporting period",
      ["a 3-month reporting period", "a 6-month reporting period", "a 24-month reporting period",
       "an annual reporting period fixed at the year end"],
      "A rolling 12 months. At the end of each month a new month is added to the far end, so the horizon never shortens.")
plain("Guide 12.2, the master budget",
      "The budgeting process normally begins with the preparation of the",
      "operating budgets",
      ["capital budgets", "financial statement budgets", "pro forma balance sheet", "cash budget"],
      "The operating budgets come first. The information in them is then used to prepare the financial statement budgets. The flow runs one way only.")
plain("Guide 12.2, the master budget",
      "The first step in preparing the operating budget is",
      "the sales forecast",
      ["the inventory purchases budget", "the selling and administrative budget", "the cash budget", "the capital budget"],
      "The sales forecast. Every other operating budget is scaled from the level of sales that is expected.")
plain("Guide 12.2, the master budget",
      "Budgets that provide a basis for evaluating expenditure which affects the business for more than one year are",
      "capital budgets",
      ["strategic budgets", "operating budgets", "master budgets", "financial statement budgets"],
      "Capital budgets. Never strategic budgets. That word belongs to strategic planning, which is a level of planning and not a budget.")
plain("Guide 12.3, the pro forma statements",
      "Budgeted financial statements prepared from information in the master budget are called",
      "pro forma statements",
      ["audited statements", "management accounts", "consolidated statements", "variance reports"],
      "Pro forma statements. A pro forma statement predicts what the financial statements will look like at the end of the period.")
plain("Guide 12.3, the pro forma statements",
      "Projected cash accumulations minus projected cash disbursements gives",
      "the pro forma cash flow",
      ["the pro forma income statement", "the pro forma balance sheet", "net worth", "retained earnings"],
      "The pro forma cash flow, which shows projected cash available. Cash flow equals receipts minus disbursements.")
combo("Guide 12.3b, what feeds the pro forma balance sheet",
      "The preparation of the pro forma balance sheet draws on\n(i) the pro forma income and cash flow statements\n(ii) the operations and sales budgets\n(iii) the capital budgets prepared under different scenarios",
      ALL,
      "All three. The balance sheet is assembled last, from everything above it, which is why the operating budgets must be finished first.")
because("Guide 12.2, the master budget",
        "The preparation of the operating budget begins with the sales forecast.",
        "Every other operating budget is scaled from the level of sales that the venture expects to achieve.",
        AR[0],
        "Both are true, and S2 explains S1. Purchases, staffing and cash all follow from the forecast sales volume.")

# ------------------------------------------- 10. The calculations (12)
S13A = "Guide 13.1, schedule of cash receipts"
plain(S13A,
      "Nkwanta Hardware Ltd had a beginning balance of " + C + "32,000 in accounts receivable on 1 April. It collects 100 percent of accounts receivable in the month following the month of sale. Its cash sales are " + C + "24,000, " + C + "28,800 and " + C + "34,560 and its sales on account are " + C + "36,000, " + C + "43,200 and " + C + "51,840 for April, May and June. Determine the accounts receivable for April.",
      C + "32,000",
      [C + "36,000", C + "24,000", C + "60,000", C + "56,000"],
      "April collects what was owed on 1 April, so the answer is the given beginning balance of " + C + "32,000. Only April uses the opening balance. Every later month uses the previous month's credit sales.")
plain(S13A,
      "Using the Nkwanta Hardware data (beginning accounts receivable " + C + "32,000; cash sales " + C + "24,000, " + C + "28,800 and " + C + "34,560; sales on account " + C + "36,000, " + C + "43,200 and " + C + "51,840 for April, May and June), determine the accounts receivable for May.",
      C + "36,000",
      [C + "43,200", C + "32,000", C + "28,800", C + "72,000"],
      "May collects April's sales on account: " + C + "36,000. Check it: May total collections are 28,800 + 36,000 = " + C + "64,800.")
plain(S13A,
      "Using the Nkwanta Hardware data (sales on account " + C + "36,000, " + C + "43,200 and " + C + "51,840 for April, May and June), determine the accounts receivable for June.",
      C + "43,200",
      [C + "51,840", C + "36,000", C + "34,560", C + "86,400"],
      "June collects May's sales on account: " + C + "43,200. June total collections are 34,560 + 43,200 = " + C + "77,760.")
plain("Guide 13.1, rule 4; trap list 13",
      "Nkwanta Hardware Ltd has sales on account of " + C + "36,000, " + C + "43,200 and " + C + "51,840 and total budgeted sales of " + C + "60,000, " + C + "72,000 and " + C + "86,400 for April, May and June. Determine the accounts receivable that appear on the second quarter pro forma balance sheet.",
      C + "51,840",
      [C + "86,400", C + "131,040", C + "43,200", C + "34,560"],
      "Year end receivables are the last month's CREDIT sales only: June sales on account, " + C + "51,840. It is not June total sales (" + C + "86,400) and it is not the sum of the quarter's credit sales (" + C + "131,040).")
plain("Guide 13.1, rule 5",
      "Nkwanta Hardware Ltd has total budgeted sales of " + C + "60,000, " + C + "72,000 and " + C + "86,400 for April, May and June. Determine the sales revenue shown on the second quarter pro forma income statement.",
      C + "218,400",
      [C + "198,400", C + "131,040", C + "86,400", C + "87,360"],
      "Add the three total budgeted sales figures: 60,000 + 72,000 + 86,400 = " + C + "218,400. Use total sales, not the credit sales and not the collections.")
S13B = "Guide 13.2, divisional growth to the fourth quarter"
plain(S13B,
      "Ashanti Foods Company Ltd has three divisions preparing a sales budget. First quarter sales are Tamale " + C + "480,000, Takoradi " + C + "620,000 and Ho " + C + "350,000. Sales are expected to grow by 2, 4 and 10 percent per quarter respectively. Determine the fourth quarter sales for the Takoradi division.",
      C + "697,416",
      [C + "725,312", C + "670,592", C + "694,400", C + "644,800"],
      "Three growth steps separate the first quarter from the fourth: 620,000 x 1.04 cubed = 620,000 x 1.124864 = " + C + "697,416. Raising it to the fourth power gives " + C + "725,312, which is the trap option.")
plain(S13B,
      "Ashanti Foods Company Ltd has first quarter sales of Tamale " + C + "480,000, Takoradi " + C + "620,000 and Ho " + C + "350,000, growing at 2, 4 and 10 percent per quarter. Determine the fourth quarter sales for the Ho division.",
      C + "465,850",
      [C + "512,435", C + "423,500", C + "455,000", C + "385,000"],
      "350,000 x 1.10 cubed = 350,000 x 1.331 = " + C + "465,850. The 1.4641 multiplier is the fourth power and gives the distractor " + C + "512,435.")
plain(S13B,
      "Ashanti Foods Company Ltd has first quarter sales of Tamale " + C + "480,000, Takoradi " + C + "620,000 and Ho " + C + "350,000, growing at 2, 4 and 10 percent per quarter. Determine the total fourth quarter sales revenue on the pro forma income statement.",
      C + "1,672,646",
      [C + "1,757,315", C + "1,593,484", C + "1,658,200", C + "1,450,000"],
      "Grow each division by three steps, then add: 509,380 + 697,416 + 465,850 = " + C + "1,672,646. " + C + "1,757,315 uses the fourth power, " + C + "1,593,484 uses the square, and " + C + "1,450,000 is the first quarter total.")
S13C = "Guide 13.3, the cash budget with borrowing and interest"
plain(S13C,
      "Mampong Foods Ltd wants a cash cushion of " + C + "10,000 before the interest payment at the end of each month, and is charged interest at 3 percent per month. Its January ending cash balance is " + C + "7,510 and February cash receipts are " + C + "140,000. Compute the total cash available for February.",
      C + "147,510",
      [C + "157,510", C + "137,510", C + "132,490", C + "140,000"],
      "Total cash available = beginning cash balance + cash receipts. The beginning balance is January's ending balance: 7,510 + 140,000 = " + C + "147,510. The cushion does not enter this line.")
plain(S13C,
      "Mampong Foods Ltd has total cash available of " + C + "147,510 for February. Its February inventory purchases are " + C + "78,000 and its selling and administrative expenses are " + C + "46,000. Compute the cash surplus for February.",
      C + "23,510",
      [C + "13,510", C + "33,510", C + "69,510", C + "23,000"],
      "Total disbursements are 78,000 + 46,000 = " + C + "124,000. Disbursements minus available = 124,000 - 147,510 = -23,510, a surplus of " + C + "23,510. Subtracting the cushion here gives the repayment, not the surplus.")
plain("Guide 13.3, step 5; trap list 12",
      "Mampong Foods Ltd holds a cash cushion of " + C + "10,000. It has a March cash surplus of " + C + "35,915 and a loan balance of " + C + "69,490 carried into March. Compute the amount to be repaid in March.",
      C + "25,915",
      [C + "45,915", C + "35,915", C + "59,490", C + "10,000"],
      "On a surplus, repayment = surplus - cushion: 35,915 - 10,000 = " + C + "25,915. Add the cushion only when borrowing. Subtract it when repaying.")
plain("Guide 13.3, step 6; trap list 11",
      "Mampong Foods Ltd is charged interest at 3 percent per month on the cumulative loan balance. Its loan balances after financing are " + C + "83,000 for January, " + C + "69,490 for February and " + C + "43,575 for March. Compute the total interest for the first quarter.",
      C + "5,882",
      [C + "2,490", C + "5,192", C + "6,882", C + "1,307"],
      "Interest is charged on the running balance each month: 2,490 + 2,085 + 1,307 = " + C + "5,882. Charging interest on the new borrowing alone is the standard error.")

# ------------------------------------------- assemble
assert len(Q) == 100, "expected 100 items, got %d" % len(Q)

# Spread the correct option evenly over the five positions: 20 at each.
import random
order = [i % 5 for i in range(100)]
random.Random(492).shuffle(order)

out = []
for idx, (src, text, correct, distractors, expl) in enumerate(Q):
    assert len(distractors) == 4, "Q%d has %d distractors" % (idx + 245, len(distractors))
    opts = distractors[:]
    opts.insert(order[idx], correct)
    assert len(set(opts)) == 5, "duplicate option in Q%d" % (idx + 245)
    out.append({
        "question_number": 245 + idx,
        "question_text": text,
        "options": opts,
        "correct_answer": [correct],
        "explanation": expl,
        "source": "AI generated from " + src,
        "verified": "AI generated from the lecture notes and slides. Not from a past paper."
    })

with open("ai-generated-100.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print("wrote ai-generated-100.json with %d questions" % len(out))
