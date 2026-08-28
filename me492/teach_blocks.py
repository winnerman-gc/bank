# -*- coding: utf-8 -*-
"""The teaching block and the topic name for each guide section.

The explanation says why this answer is right. The teaching block gives the
whole topic around it, so the cluster of facts the paper draws on is in front
of you every time a question from that block comes up. Blocks are shared across
a topic on purpose: seeing the same picture on each of seventeen questions is
how it sticks.

Keys are guide sections. The longest matching key wins, so "13.3" beats "13".
"""

# Topic names for the card footer. The guide numbering is internal and means
# nothing while you are answering, so the page shows the topic instead.
TOPICS = {
    "3": "High frequency definitions",
    "4": "Entrepreneurship and free enterprise",
    "5": "Creativity and innovation",
    "6": "Business planning and the feasibility plan",
    "7": "Venture stages and the start-up",
    "8": "Market research and the marketing plan",
    "9": "Intellectual property",
    "10": "Organising the venture and legal forms",
    "11": "Financing the new venture",
    "12": "The financial plan and budgeting",
    "13": "The calculations",
    "14": "The because pairs",
    "15": "The i, ii and iii bank",
    "16": "Commonly missed answers",
}

TEACH = {
    "3": "These definitions carry more marks than any other single block, and they return almost "
         "unchanged every year. Niche is the segment you concentrate on. Window is the time "
         "horizon before something closes the opportunity. Customer scenario is the specification "
         "of your primary clients. Stakeholder is anyone with an interest in, or affected by, the "
         "business. Pricing policy is the planned process of setting prices and how they change. "
         "Promotion is the broad term for tactics that attract or inform customers. Promotional "
         "mix is the careful selection of those methods. The franchisor originates the system and "
         "takes a fee and royalties; the franchise is the system the contract creates. Learn every "
         "one as text, because the letters move between papers.",

    "4": "Who the entrepreneur is, and what entrepreneurship does to an economy. It splits into "
         "the economists, the sources of change, the myths, the success factors and "
         "intrapreneurship.",
    "4.1": "Six names, six contributions, and the paper mixes them deliberately. CANTILLON gave "
           "entrepreneurship its central role in economics: conscious decisions about resource "
           "allocation, paying a certain price and reselling at an uncertain one, seeking higher "
           "yields for money and materials. ADAM SMITH described the enterpriser who undertook "
           "the formation of an organisation, had unusual foresight to recognise potential "
           "demand, and turned demand into supply. SAY combined Cantillon's economic risk taker "
           "with Smith's industrial manager, and added exceptional insight into society's needs; "
           "the entrepreneur influences society and is influenced by it. MENGER: converting "
           "resources into goods and services of value to consumers. SCHUMPETER: creative "
           "destruction, replacing existing products and businesses with better ones, "
           "entrepreneurs as innovators. DRUCKER: resources used not merely to solve problems but "
           "to take advantage of opportunities. Mill is the fourth European name. The commonest "
           "trap in the whole paper is handing creative destruction to Menger.",
    "4.2": "The slides list the sources of change: scientific knowledge and the industrial "
           "revolution, demographic and market changes, process innovation, and social and "
           "cultural changes. Every question on this item works the same way. One statement "
           "contains a phrase that is not on the list, and that statement is the false one. It "
           "was the industrial revolution in 2005 and shop changes in 2007. Find the intruder.",
    "4.3": "An entrepreneur has a vision for growth and the energy to achieve unusual results, a "
           "commitment to constructive change, and the persistence to gather the necessary "
           "resources. A small business person substitutes income. That is the whole distinction, "
           "and income substitution is the marker the paper uses to make a statement false.",
    "4.4": "Small businesses are small by their nature and by the intention of the owner. Their "
           "creation through legal contracts is the false clause the paper attaches.",
    "4.5": "Five myths against their realities. Entrepreneurs are lucky, when most make their own "
           "luck by working hard. They are make-or-break people, when most ventures start slow "
           "and change in increments. They are misfits, when in fact they disrupt the status quo "
           "and lead the parade in a new direction. They are born not made, when environment, "
           "background, education, family and career shape them. All you need is money, when most "
           "successful companies were founded with very little.",
    "4.6": "Four success factors: a good entrepreneurial team, a well planned enterprise pursuing "
           "incremental change and growth, good timing that coincides with the window of "
           "opportunity, and a business ideology that serves customers rather than exploiting "
           "them. The venture's products or services, and its markets and timing, are also "
           "examinable.",
    "4.7": "Entrepreneurship alters the direction of national economies and helps ensure their "
           "stability, introduces quantum leaps in technology with new means of production and "
           "new systems of services, and forces the reallocation of resources from existing uses "
           "to new and more productive ones. All three are on the slides, so this item usually "
           "takes the combined answer.",
    "4.8": "Corporate entrepreneurship, or intrapreneurship, helps established companies become "
           "more productive through innovation by creative employees. The word is contrived from "
           "intra-company entrepreneur. To achieve it, corporate managers combine resources in "
           "unusual ways to create innovative products or services, and commit time and energy "
           "and risk their careers. The company carries the money risk, which is why personal "
           "investment risk is always the false statement here.",
    "4.9": "The recurring facts. Business failure comes most often from inexperience. A business "
           "started from scratch carries a higher risk than one bought. Entrepreneurs are high "
           "risk takers, have a high internal locus of control, and typically form service "
           "businesses rather than manufacturing ones. Most technical entrepreneurs start close "
           "to their previous career work, which is the corridor principle. And to live where I "
           "like is not a reason for going into business for yourself.",
    "4.10": "The word comes from the 17th century French entreprendre, to undertake. It referred "
            "to individuals who were undertakers, meaning those who undertook the risk of a new "
            "enterprise, and to contractors and builders who bore the risk of profit or loss. The "
            "early slides add soldiers of fortune, adventurers and merchants. The clause that "
            "makes a statement false is the one saying the term was discovered by business "
            "students. A companion item says the concept has given enterprise a new direction and "
            "has been around a very long time; it has not just been discovered.",

    "5": "Creativity produces the idea. Innovation turns it into something useful. Almost every "
         "trap in this topic comes from mixing the two processes.",
    "5.1": "Creativity is the ABILITY to bring something new into existence, so it is a capacity, "
           "not an activity. Innovation is the PROCESS of doing new things, the transformation of "
           "creative ideas into useful applications, and the conversion of something new into "
           "useful goods or services. It is also the ability to see, conceive and create new and "
           "unique products, processes or services. Invention is the verified RESULT of a "
           "creative idea. Creativity is a prerequisite for innovation, never the other way "
           "round. Creativity is the seed; innovation is the process.",
    "5.2": "Five stages, and the paper asks about them one at a time. IDEA GERMINATION, seeding: "
           "the seed of an idea is implanted by curiosity or interest. PREPARATION, "
           "rationalisation: a conscious search for the knowledge to bring the idea to life. "
           "INCUBATION, fantasising: subconscious assimilation of information, sleeping on it. "
           "ILLUMINATION, realisation: recognising the idea as feasible, the sudden flash, the "
           "oh-I-see moment. VERIFICATION, validation: applying or testing to prove the idea has "
           "value. The pair the paper swaps is illumination against verification, because both "
           "sound like the end of the process.",
    "5.3": "The innovation process has four elements: analytical planning, organising resources, "
           "implementation, and commercial application. The creative process elements, idea "
           "germination, preparation, incubation, illumination and verification, do not belong "
           "here, and any option mixing them in is false. In 2007 the same question was worded "
           "around translating a new idea into commercial reality, and the false statement was "
           "the one calling it an invention. Innovation is different from invention.",
    "5.4": "A window is the time horizon during which an opportunity exists before something else "
           "eliminates it. When a window opens competitors rush in, the market saturates, and the "
           "window closes. The corridor principle says successful ventures evolve from "
           "entrepreneurs already positioned in similar work or related ventures, so when a "
           "window opens they move quickly. A corridor is a route down which a person travels: "
           "one idea leads to revisions and further innovations.",
    "5.5": "Three key people for technological innovation: the creative source, the champion and "
           "the sponsor. The wrong trios swap in the inventor, the investor, the entrepreneur or "
           "the promoter. When the 2020 paper reworded it as conditions necessary, the answer was "
           "still this trio. Alongside sit seven conditions, of which the examined statements are "
           "adequate support from external sources, a clear need from enough potential consumers "
           "to warrant committing resources, and realisation of the product as a useful "
           "innovation providing value to society. Watch for a little support, which is false as "
           "printed: the condition is adequate support.",
    "5.6": "Brainstorming rules: no criticism is allowed by anyone in the group, free wheeling is "
           "encouraged, a high quantity of ideas is wanted, combination and improvement of ideas "
           "are encouraged, and the period for generating ideas is predetermined. Nothing is "
           "judged inside the session, so any option saying ideas without merit are discarded is "
           "false.",
    "5.7": "A mind map begins with a person's interest or advocation, expands to include related "
           "products and market opportunities, then selectively follows a path of investigating "
           "each option, expanding new business ideas as it goes.",
    "5.8": "A majority of new products evolve at the LOW-tech end of the spectrum. Low-tech "
           "products should be easy to make, quick to market and cheap to terminate, because "
           "patents cannot protect them and they can be copied. Mid-tech products presume the "
           "application of new knowledge, but you do not need to be an inventive genius to pursue "
           "them. Telling high-tech from mid-tech is largely a matter of perception: what is "
           "high-tech to one person is mid-tech to another.",

    "6": "The feasibility plan and the business plan: who writes it, what goes in it, who reads "
         "it, and why it fails.",
    "6.1": "The entrepreneur writes the plan, because the entrepreneur has the vision and the "
           "motivation and can articulate the necessary information effectively. Specialists and "
           "other sources are consulted, never handed the job. The because pair claiming "
           "feasibility plans are best prepared by specialists, because specialists such as "
           "financial experts know how to operate businesses, is FALSE on both statements. One "
           "compiled answer sheet gets this wrong; the 2005 key and the 2020 exam both give both "
           "false.",
    "6.2": "A feasibility plan is a written document that integrates the fundamental areas of "
           "business, operations, marketing, finance and human resources, describes the relevant "
           "external and internal elements of starting a new venture, is prepared by the "
           "entrepreneur, and has one objective: determining whether the venture can be expected "
           "to succeed. It is deliberately pragmatic, doing the planning needed to ensure "
           "feasibility without overwhelming the entrepreneur in the process.",
    "6.3": "Three perspectives are considered when writing the plan: the entrepreneur's, the "
           "marketing perspective, and the investor's. Read what is printed, because one paper "
           "offers the government, all interested constituents, and the market and investors as "
           "distractors.",
    "6.4": "Before writing, check the barriers to success: the market, finance and operations or "
           "manufacturing; the business concept and the entrepreneurial team; and the goals and "
           "objectives of the venture, finance, and the product or service. The 2020 exam "
           "confirmed all three groups.",
    "6.5": "The first element of information the entrepreneur needs is the market potential for "
           "the products or services. Only that. Not basic operational needs, not an evaluation "
           "of the team, and not profitability. Nothing else matters if there is no market.",
    "6.6": "The executive summary stimulates the reader's interest, covers the key points of the "
           "plan concisely and convincingly, runs to about two or three pages, and is written "
           "AFTER the whole plan. The venture definition inside it names the business and states "
           "why it was founded. The business concept, in the main body, goes further into the "
           "evolution of the business and the nature of market demand.",
    "6.7": "The introductory or cover page carries the name and address of the business, the "
           "amount of financing required, a statement of confidentiality, the names and contacts "
           "of the entrepreneurs, and a brief description of the business concept. When the paper "
           "wants a single answer, it wants the confidentiality clause.",
    "6.8": "The elements the papers accept are the Executive Summary and Market research and "
           "analysis, depending which distractors are printed alongside. Abstract, Literature "
           "Review, Product design and Conclusions and recommendations come from academic "
           "reports, not business plans, and are never correct.",
    "6.9": "Environmental and industry analysis deals with an assessment of the location of the "
           "venture and its immediate area, an assessment of competitive strategies and industry "
           "trends, and an assessment of external uncontrollable variables that may affect the "
           "business. The 2020 exam confirmed all three.",
    "6.10": "The manufacturing or operations section is needed for ventures that manufacture, "
            "design or sell products, and for service firms needing capital equipment. It covers "
            "leadership and the entrepreneurial team, facilities and inventory, and operations "
            "and human resources. The financial section is fed by the product and service "
            "description, the operations segment, and the market research and market plan "
            "segments, all three.",
    "6.11": "The appendix carries resumes of partners, facility layouts and partnership "
            "agreements. Supporting paper only. When one option is allowed, take the resumes of "
            "partners.",
    "6.12": "The plan exists primarily to give information to lenders and investors. It also "
            "provides direction, proves feasibility and attracts money, so where an all-of-the-"
            "above style option is printed, take it. It is not there to guide the entrepreneur "
            "through daily operations, and not to tell suppliers anything.",
    "6.13": "Plans go out of date through changes in the market and the industry, the loss or "
            "addition of key team members, a new location, and poor articulation of the business "
            "concept. For a single answer, take the market and industry change.",
    "6.14": "Business plans fail because goals set by the entrepreneurs are unreasonable and "
            "unmeasurable, because the entrepreneur has not made a total commitment to the "
            "business, and because the entrepreneur has no experience in the planned business. "
            "All three. Forced to one option, the 2020 key took the unreasonable goals.",
    "6.15": "Planning is a process that never ends for a new venture, because businesses evolve "
            "from early start-up to a final growth stage if planning is done well at the "
            "beginning. A good way to fail quickly is to start without a clear vision, because a "
            "business without one shows a lack of understanding of marketing issues. Both pairs "
            "answer A.",
    "6.16": "Many copies of the plan circulate among outsiders. Counter the risk with a "
            "non-disclosure statement. A Disclosure Document is a patent office filing and is a "
            "completely different instrument, which is why it is offered as a distractor.",

    "7": "Four growth stages, and the start-up is where most of the questions sit.",
    "7.1": "PRE-START-UP is the assembly of resources and the organising of the venture for "
           "opening. START-UP is initial business operations, where reality shock sets in as the "
           "entrepreneur positions the business to compete in the real world. EARLY GROWTH "
           "follows initial success, growing at a healthy rate and needing careful co-ordination "
           "of resources so the entrepreneur takes a profit. LATER GROWTH is the established, "
           "professionally managed enterprise.",
    "7.2": "Pre-start-up activities are the product or market survey and the definition of the "
           "business concept. A competitive analysis carried out in the pre-start-up stage is "
           "marketing research before the doors open, which is the mirror of the competitive "
           "analysis done after opening.",
    "7.3": "The two benchmark considerations for the start-up stage are meeting operating "
           "objectives and positioning the venture for long-term growth. This answer has not "
           "changed across the 2007, 2015 and 2020 papers. The operating objectives themselves "
           "are sales, revenue, growth and position, and progress is measured with a 12-month "
           "schedule to see whether the plan has been achieved.",
    "7.6": "The financial burden before start-up is reduced by planning assets carefully. Not by "
           "cutting capacity, not by cutting staff, and not by paying low salaries. Financial "
           "planning in the pre-start-up stage need not be extensive, but it must be based on "
           "verifiable information.",

    "8": "Market research gathers. The market plan uses. Everything in this topic hangs off that "
         "one distinction.",
    "8.1": "Market research and analysis gathers the information. The market plan then uses it in "
           "a marketing strategy to attract customers. This exact sentence has appeared every "
           "year; learn it word for word. The research activities are identifying potential "
           "customers, evaluating markets, analysing competitors and describing assumptions, and "
           "the distractor is the option that drops the assumptions.",
    "8.2": "The objective of market research is to establish that a market exists. It culminates "
           "in a sales forecast, which is also the first step of the operating budget, so this "
           "item is the hinge between the marketing block and the finance block.",
    "8.3": "The market plan answers who the customer is and where he or she is located.",
    "8.4": "The marketing functions are the four Ps: product, price, place or distribution, and "
           "promotion. The paper prints different subsets in different years, so take the fullest "
           "option shown, and take all of the above whenever it is offered.",
    "8.5": "A market niche is a carefully defined segment of a broader market that defines the "
           "positioning of a product or service to create a distinct marketing focus. New "
           "ventures establish themselves in a niche because companies establish segmentation "
           "strategies so that resources are used efficiently and without ambiguity, and that "
           "because pair answers A. This word has moved letters more than any other item in the "
           "paper, so answer it by text and never by position.",
    "8.6": "The result of good market research is a well defined sales forecast. Only that. Not a "
           "good estimate of revenue, and not well defined investment needs; those come later, "
           "from the budgets.",
    "8.7": "A distribution system is the physical process of getting goods to market and the "
           "process of locating services. Taking raw materials through production is "
           "manufacturing, not distribution. The three channel types are consumer, industrial and "
           "service. The infrastructure of a marketing plan is often built solely on the firm's "
           "distribution system.",
    "8.8": "Product is a catchall term covering three layers: the business concept, such as "
           "fast-food franchising; the physical object or service sold, with its packaging, "
           "image, brand name and warranty; and the physical attributes that shape how customers "
           "see it, the colours, shapes, sizes and materials. The expanded view of a product adds "
           "function, form, packaging characteristics and after-sales support. A marketing "
           "strategy provides guidelines on the marketing programme, the expected results and "
           "allocation of resources, and the ways the enterprise will be controlled.",
    "8.9": "Advertising at start-up has one job: convince someone to walk in your door. It does "
           "not make a satisfied customer, and it does not sell to someone who cannot afford the "
           "product. Integrating promotion into the marketing mix increases sales, builds "
           "recognition and builds consumer loyalty, all three. Integrated Marketing "
           "Communications consolidates all communications into a single focused marketing, sales "
           "or image message, which is the exact opposite of an assortment of forms delivering a "
           "variety of messages.",
    "8.10": "The marketing plan establishes how the entrepreneur will effectively compete and "
            "operate in the market, and it is implemented through a marketing programme; take "
            "marketing activities only when programme is not printed. Marketing plans fail "
            "through lack of a real plan, lack of adequate situation analysis, unrealistic goals "
            "and unanticipated competitive moves, so where all of the above is printed, take it.",
    "8.11": "Prices for goods and services must coincide with strategies that reinforce the "
            "entrepreneur's business and reputation, because prices communicate perceptual "
            "messages to consumers. That because pair answers A. The planned process of "
            "determining prices and how they change in the field is the pricing policy.",
    "8.12": "Market potential is critically influenced by the timing of new products or services, "
            "because timing pertains to when products are introduced, how they are priced, how "
            "they are distributed and how they are promoted. That because pair answers A, and "
            "note that timing runs through all four marketing functions.",
    "8.13": "A clear profile of potential customers looks at age and sex, income status, and "
            "locating the potential customer base. All three.",
    "8.14": "Marketing research undertaken after a new venture opens its doors is called a "
            "competitive analysis. Note the pairing: the same competitive analysis carried out "
            "before opening belongs to the pre-start-up stage.",

    "9": "Patents, disclosure documents, trademarks, product liability and contracts.",
    "9.1": "A patent is a grant of a property right by a government to an inventor. A patent "
           "search determines whether an inventor's creation already exists and remains actively "
           "protected under the law, so it is a legal check and not a commercial one. A plant "
           "patent is given for hybrid roses and food grains; the 17 years figure belongs to the "
           "old utility patent term and is the distractor. A successful utility patent requires "
           "proof that the creation is the applicant's and that it is useful and new; the 2020 "
           "exam marked all three statements, while older papers marked only those two and "
           "rejected personal investment risk.",
    "9.2": "A Disclosure Document is a statement to the patent office by the inventor declaring "
           "the intent to patent an idea. It becomes important when a patent infringement has "
           "occurred. It is not the same thing as a patent.",
    "9.3": "A trademark may be a particular sound, a word or symbol, or a word, design or slogan, "
           "and it can last indefinitely, so this item takes all of the above. Filing a trademark "
           "registration requires completion of the written form and payment of the fee, a "
           "drawing of the mark with five specimens showing actual use, and publication in the "
           "Trade Mark Official Gazette.",
    "9.4": "The best protection against product liability is to produce safe products and to warn "
           "customers of potential hazards. Zero defects is not achievable, so no venture can "
           "offer it as a protection, and it is the printed trap.",
    "9.5": "Contract guidelines: describe the transaction in detail, obtain the signatures of the "
           "people you are doing business with, and remember that oral agreements are invalid for "
           "deals running over one year. All three.",

    "10": "Sole proprietorship, partnership and corporation, plus how the venture is organised.",
    "10.1": "After choosing the legal form, decide the organisational structure first. Then "
            "identify the major activities through job analysis, write the job description, set "
            "the job specification and selection criteria, and train. Structure comes first, and "
            "activities are found through job analysis, not through the job description.",
    "10.2": "Selecting a legal form involves at least three criteria: the preferences of the "
            "entrepreneur, the profile of the enterprise, and the advantages and disadvantages of "
            "the legal business entity itself.",
    "10.4": "Sole proprietorship advantages: ease of starting and ending, being your own boss "
            "with autonomy of control, decision making and administration, pride of ownership, "
            "retention of profit, no special taxes, inexpensive and self directing and easy to "
            "set up, and simplicity. Disadvantages: unlimited liability, limited financial "
            "resources, difficulty in management, overwhelming time commitment, few fringe "
            "benefits, limited growth, and a limited life span, since the business ends with the "
            "owner's death. The main disadvantage examined is unlimited legal and financial "
            "liability. An expanded network of contacts and a strong profile for obtaining debt "
            "financing are both false as advantages.",
    "10.5": "Three types: general partnership, limited partnership and master limited "
            "partnership. A general partner has unlimited liability and manages the firm. A "
            "limited partner invests, has limited liability, and cannot legally help manage. An "
            "MLP acts and trades like a corporation but is taxed like a partnership, so it avoids "
            "corporate income tax. Advantages: more financial resources, shared management and "
            "pooled knowledge, longer survival. Disadvantages: conflict and tension, unlimited "
            "legal liability for all parties jointly and severally, division of profits, "
            "disagreements among partners, difficulty terminating, and the business ending on the "
            "death or withdrawal of any partner. Limited access to external resources is NOT a "
            "partnership disadvantage; a partnership has more access than a sole proprietorship. "
            "Limited partners enjoy exemption from management responsibility, profits and losses "
            "passed through, and an investment that can be sold or assigned.",
    "10.6": "A corporation is a legal entity with authority to act and have liability separate "
            "from its owners, chartered by the state to do business as an artificial person and "
            "owned by shareholders. Advantages: more money for investment, limited liability, "
            "size, perpetual life, ease of ownership change, ease of drawing talented employees "
            "through stock options, and separation of ownership from management. Disadvantages: "
            "initial cost, paperwork, two tax returns, size, difficulty of termination, double "
            "taxation, and expense to start. The hierarchy: owners and shareholders elect the "
            "Board of Directors, the Board hires Officers, Officers set objectives and select "
            "Managers, Managers supervise Employees. Owners have some say in who runs the "
            "corporation, but no control.",
    "10.7": "A formal board of directors is required by law only for incorporated companies, and "
            "membership for a new venture should be five to nine. A board of advisors serves in "
            "an advisory capacity; the papers print a lawyer, a banker and a marketer, or a "
            "lawyer, a banker, an accountant and an advertising agent, so take the fullest "
            "professional list shown. Beyond decision making, directors act as members of an "
            "expanded social network, as disturbance handlers and resource allocators, and as "
            "mentors and professional advisors.",
    "10.8": "The entrepreneurial team is responsible for building an organisation, giving "
            "identity to the venture, focusing on operational issues and immediate problems, and "
            "guiding the venture through change; take all of the above, and where one option is "
            "forced the 2015 key marked guiding the venture through change. The founder's "
            "responsibilities are defining the business and identifying human resource "
            "requirements.",
    "10.9": "The franchisor originates the business system and supplies services, products, "
            "training, inventory and support, taking a fee and royalties. The franchisee is the "
            "acquiring owner. The franchise is the business system created by the contract "
            "between them.",
    "10.10": "Stakeholders want different things. Society and humankind want value added products "
             "and services. Lenders want cash flow, collateral and equity contribution. Employees "
             "want income and job stability and career positions. Investors want a profitable "
             "return on investment. The paper swaps these round, so read whose interest is asked.",

    "11": "Where the money comes from, what it costs, and what it costs you in control.",
    "11.1": "Three capital requirements, asked as three separate questions, so learn all three. "
            "FIXED capital buys physical facilities: buildings, fixtures and equipment. It is a "
            "long term investment financed by long term credit. WORKING capital covers day to day "
            "operating costs: rent, utility bills, inventories and payroll. It is financed by "
            "short term credit. LIQUID or fluid capital is money held in reserve for emergencies, "
            "as cash or disposable securities such as stocks, bonds and certificates of deposit.",
    "11.2": "Short term credit runs under one year, funds working capital, and is self "
            "liquidating because the sales it funds generate the cash to repay it. Intermediate "
            "term credit runs one to five years and buys smaller fixed capital such as fixtures "
            "and equipment. Long term credit runs beyond five years and buys major fixed capital "
            "such as buildings and land. Where short term financing is used, the funds are repaid "
            "from sales and profits.",
    "11.3": "Debt financing is also called asset-based financing. It requires collateral, pays "
            "the investor interest, and is repaid as principal plus interest, with long term debt "
            "using 50 to 80 percent of the asset value as collateral. Equity financing requires "
            "no collateral, gives the investor a form of ownership position, and is repaid as a "
            "pro rata share of profits. When interest rates are low, DEBT lets the entrepreneur "
            "retain a larger ownership portion and get a greater return on equity. The key "
            "factors favouring one over the other are the availability of funds, the assets of "
            "the venture, and prevailing interest rates.",
    "11.4": "Internal sources: profits, sale of assets, reduction in working capital, extended "
            "payment terms, and collecting receivables faster. External sources: personal funds, "
            "family and friends, commercial banks, venture capital, and government grants. "
            "Government grants are external, which is the one students most often reverse. "
            "External financing is evaluated on the length of time the funds are available, the "
            "cost, and the amount of company control lost.",
    "11.5": "Personal funds are the least expensive in terms of cost and control, and are "
            "absolutely essential to attracting outside funding from banks, private investors and "
            "venture capitalists. Family and friends are next; keep it strictly business and in "
            "writing. Commercial banks are by far the most frequently used source of short-term "
            "funds where collateral is available. Venture capital is intended for higher risks "
            "such as start-up situations, and venture capitalists look for extremely high growth "
            "and profit potential, a willingness to exchange equity, and the potential to cash "
            "out in five years. Development capital serves more mature investments; replacement "
            "capital brings in an institution in place of an original shareholder. Which source "
            "is used depends on the type of financing needed, the nature and size of the "
            "business, and the entrepreneur's financial condition, never on money portability.",
    "11.6": "Equity is the ordinary share capital of a business. Net worth is the amount owners "
            "have invested or retained from operations. Retained earnings are accumulated profits "
            "in excess of losses and payments to owners. An account PAYABLE is an obligation from "
            "the purchase of goods or services on credit, money going out. An account RECEIVABLE "
            "is money due from another for services performed or goods sold on credit, money "
            "coming in. They are asked back to back, so fix the direction. Covenants are "
            "restrictions in loan agreements. Cash flow is receipts minus disbursements. "
            "Financial co-ordination is the integration and synchronisation of financial "
            "activities so all functions work towards common objectives. Seed financing is needed "
            "prior to or during start-up, to underwrite operations, assets or business "
            "development.",

    "12": "Three levels of planning, the master budget, and the pro forma statements. This block "
          "is copied almost word for word out of the course notes.",
    "12.1": "Strategic planning is long term: defining the scope of the venture, which products "
            "to develop, and deciding which market niche should be profitable. Capital budgeting "
            "is intermediate: whether to buy or lease equipment. Operations budgeting is short "
            "term and the most specific: sales targets, production objectives and financing "
            "plans. Budgeting itself is the process that co-ordinates the finances of all areas "
            "of the new venture, which is neither cost accounting nor financial accounting.",
    "12.2": "The master budget covers a one year time span and is the composition of numerous "
            "separate but interdependent departmental budgets covering sales, production, "
            "manufacturing expenses and administrative expenses. Its three categories are "
            "operating budgets, capital budgets and financial statement budgets. The process "
            "begins with the operating budgets, and the first step in preparing those is the "
            "sales forecast. Information in the operating budgets is then used to prepare the "
            "financial statement budgets, and the flow runs one way only. Financial statement "
            "budgets are also called pro forma statements. Perpetual or continuous budgeting uses "
            "a rolling 12-month reporting period: at the end of each month a new month is added "
            "to the end. Capital budgets evaluate expenditure affecting the business for more "
            "than one year, and are never called strategic budgets. A budget is prepared as a "
            "planning function, administered as a control function, and is a statement of "
            "expected results in financial or numerical terms, so take the combined option. The "
            "four operating budgets for a retail venture are sales, inventory purchases, selling "
            "and administrative, and cash.",
    "12.3": "The pro forma INCOME statement shows projected net profits from projected revenues "
            "and projected costs and expenses, and the income statement is referred to as a "
            "summary of operations. The pro forma BALANCE SHEET shows projected assets, "
            "liabilities and owners equity, and those three are its main segments. The pro forma "
            "CASH FLOW shows projected cash available, which is projected cash accumulations "
            "minus projected cash disbursements. Before developing the income statement, prepare "
            "the capital and operating budgets, and within that start with the sales budget. The "
            "balance sheet draws on the income and cash flow statements, the operations and sales "
            "budgets, and the capital budgets. One compiled sheet wrongly gives the income "
            "statement as the one summarising assets, liabilities and equity; it is the balance "
            "sheet.",
    "12.4": "All financial forecasts and projections are based on a number of financial "
            "assumptions, because the outcomes of future events are not predictable. That because "
            "pair answers A.",

    "13": "Only three calculation types exist, and the wording has not changed since 2005. Learn "
          "the method; only the table changes.",
    "13.1": "You are given cash sales, sales on account and total budgeted collections for three "
            "months, and told the company collects 100 percent of receivables in the month "
            "following the sale. Five rules. Accounts receivable for a month is the PREVIOUS "
            "month's credit sales, except the first month, which uses the given opening balance. "
            "Budgeted cash sales are read straight off the table, which is a free mark. Total "
            "budgeted collections are this month's cash sales plus last month's credit sales, "
            "which is how you check your work. Receivables on the fourth quarter balance sheet "
            "are DECEMBER'S sales on account alone, the money still uncollected at 31 December. "
            "Sales revenue on the fourth quarter income statement is the sum of the three TOTAL "
            "budgeted sales figures. Where the stem gives a collection percent that the table "
            "contradicts, trust the table.",
    "13.2": "Three divisions or districts, each with a first quarter figure and its own growth "
            "rate per quarter. From the first quarter to the fourth there are THREE growth steps, "
            "not four, so multiply by (1 + g) cubed. Memorise the multipliers: 2 percent gives "
            "1.061208, 3 percent gives 1.092727, 4 percent gives 1.124864, 5 percent gives "
            "1.157625, 10 percent gives 1.331. Raising the multiplier to the fourth power lands "
            "you exactly on a printed distractor, which is what it is there for. For the total on "
            "the income statement, grow each division separately and then add.",
    "13.3": "Seven steps. Beginning cash balance is last month's ending balance. Total cash "
            "available is beginning plus cash receipts. Total budgeted disbursements are "
            "inventory purchases plus selling and administrative expenses. Shortage or surplus is "
            "disbursements minus available: a positive number is a shortage, a negative one is a "
            "surplus. On a shortage, borrowing equals shortage plus cushion. On a surplus larger "
            "than the cushion, repayment equals surplus minus cushion. On a surplus SMALLER than "
            "the cushion, you borrow the difference, because the surplus alone does not reach the "
            "cushion you must hold. Interest is the rate times the CUMULATIVE loan balance after "
            "financing, so track the running balance. Ending balance is available minus "
            "disbursements plus borrowing minus repayment minus interest. The same table also "
            "asks for net cash flow from financing, which is total borrowed minus total repaid "
            "and equals the closing loan balance, and net cash flow from operating, which is "
            "receipts minus disbursements minus interest paid.",

    "14": "The because section pairs two statements. Judge S1 alone and write T or F above it. "
          "Judge S2 alone the same way. Only if both are true do you ask whether S2 explains why "
          "S1 is true. Never read the pair as one sentence; that is the whole trap. The code is "
          "stable across every paper: A is both true with S2 explaining S1, B is both true with "
          "S2 not explaining, C is S1 true and S2 false, D is S1 false and S2 true, E is both "
          "false. Across the whole bank A is correct about 72 percent of the time, and D has "
          "never once been correct. The exceptions worth memorising are the low-tech pair, the "
          "mid-tech inventive genius pair, the feasibility specialists pair, the A-team pair and "
          "the inventors pair.",
    "15": "The i, ii and iii section uses a printed code that has appeared two different ways, so "
          "read the KEY box first and circle it. In version A, A is all three, B is i and ii, C "
          "is i and iii, D is i only, E is iii only. Version A cannot express ii and iii or ii "
          "only, so if you reason your way to ii and iii you are either on a version B paper or "
          "you have misread a statement; that is a free error check. Across the bank all three is "
          "correct 41 percent of the time, statement iii appears in the answer 81 percent of the "
          "time and statement ii only 63 percent, so doubt statement ii first. Read every clause "
          "of every statement: one wrong word, such as shop changes, a little support, or "
          "discovered by business students, makes the whole statement false.",
    "16": "The items students most often lose. Asset-based financing is DEBT, not equity. Budgets "
          "for expenditure over one year are CAPITAL budgets, not strategic. The statement "
          "summarising projected assets, liabilities and equity is the BALANCE SHEET, not the "
          "income statement. Setting the specifications of primary clients is the CUSTOMER "
          "SCENARIO, not a market survey. The planned process of determining prices is PRICING "
          "POLICY, not price setting. The organisational plan describes the ORGANOGRAM. "
          "Replacement of existing products with new and better ones is CREATIVE DESTRUCTION, "
          "from Schumpeter, not upscaling. Feasibility plans best prepared by specialists is both "
          "statements FALSE. A marketing plan is implemented through a marketing PROGRAM.",
}
