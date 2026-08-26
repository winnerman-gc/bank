#!/usr/bin/env python3
"""
Build the ME 492 Management & Entrepreneurship Development question bank.

Source material (KNUST past papers held in ~/Documents/y4s2/enterpreneur):
  - ME492 2005 Marking Scheme (120 questions with official answers)
  - ENTREPRENEUR MCQ 1pdf (2004/2005 Section A, 40 finance questions, answers bold)
  - Pasco2 / pcu-coe-216-07 (2007 paper, correct options marked in red)
  - PASCO 1 (2008-style paper, 135+ questions, hand-marked)
  - ME 492 PRACTICEOBJECTIVES (2007/2008, 150 questions)
  - IMAGE PASSCO (several papers, including a newer 2015/2016 paper)
  - ME 492 ONLINE 2020 (Moodle exam, 60 questions, answers highlighted)
  - Lecture slides 1, 2, 3, 8, 9, 10 and ME 492 2025 NOTES

Unlike an authored bank, these are the ACTUAL past questions. Stems and options
are reproduced as they appear on the papers, with two edits:

  1. Options that referred to other options by letter ("a and b only",
     "all of the above") are rewritten as self-contained text, because the
     practice page shuffles the option order.
  2. Where two papers printed different option sets for the same stem, the
     fuller set is used and the answer follows the printed marking scheme.

Output JSON matches the format used by the other practice sites in this repo:

    {
      "question_number": 1,
      "question_text": "...",
      "options": ["...", ...],
      "correct_answer": ["..."]
    }

Questions carry either four or five options, matching the source paper.
"""
import json
import random
import re

from explanations import EXPLANATIONS, verification

# ---------------------------------------------------------------------------
# SET 1 - Entrepreneurship and free enterprise
# ---------------------------------------------------------------------------
SET1 = [
    ("A person who starts a new business, taking the initiative and the risk associated "
     "with the new venture, and who does so by creating something new or by using "
     "resources in unusual ways to provide value to his or her customers is known as a(n)",
     "entrepreneur",
     ["business man", "sole proprietor", "industrialist", "franchisor"]),

    ("Any person or organisation that has an interest in, or can be affected by, a "
     "business is called a",
     "stakeholder",
     ["vendor", "partner", "corporation", "proprietor"]),

    ("A time horizon during which opportunities exist before something else happens to "
     "eliminate them is known as a",
     "window of opportunity",
     ["corridor of opportunity", "idea germination", "preparation", "chance time"]),

    ("Richard Cantillon, a French economist of Irish descent, is credited with giving "
     "the concept of entrepreneurship a central role in economics. He described an "
     "entrepreneur as a person who",
     "consciously makes decisions about resource allocation and seeks higher yields for "
     "money and materials",
     ["behaves with exceptional insight to fulfil society's needs through risk taking",
      "organises industrial activity, matching demand with supply through commerce",
      "engages in creative destruction by displacing established competitors",
      "redirects resources away from problems and towards progressive opportunities"]),

    ("Carl Menger described entrepreneurship as",
     "the process of converting resources into goods and services of value to consumers",
     ["a force of creative destruction",
      "a process with entrepreneurs as innovators",
      "the matching of demand with supply through commerce",
      "the substitution of employment income by self-employment income"]),

    ("Jean Baptiste Say combined the economic risk taker of Cantillon and the industrial "
     "manager of Smith into an unusual character. He believed that entrepreneurs",
     "possessed certain arts and skills of creating new economic enterprises, yet had "
     "exceptional insight into society's needs and were able to fulfil them",
     ["were change agents who displaced established firms without warning",
      "typically bought goods at known prices and transformed them to sell at unknown prices",
      "consciously allocated resources by chance as they developed their ventures",
      "organised industrial activity purely to achieve administrative efficiency"]),

    ("Adam Smith spoke of the enterpriser as an individual who",
     "undertook the formation of an organisation for commercial purposes, recognised "
     "potential demand, and transformed demand into supply",
     ["allocated resources by chance while developing new ventures",
      "was a force of creative destruction within an established industry",
      "converted resources into goods and services of value to consumers",
      "redirected resources away from existing uses towards administrative efficiency"]),

    ("In Drucker's view, the entrepreneur",
     "uses resources not merely to solve problems but also to take advantage of "
     "opportunities",
     ["engages in creative disruption of the existing industry structure",
      "organises industrial activity, matching demand with supply through commerce",
      "converts resources into goods and services of value to consumers",
      "behaves with exceptional insight to fulfil society's needs through risk taking"]),

    ("The replacement of existing products and businesses with new and better ones is "
     "called",
     "creative destruction",
     ["entrepreneurship", "outsourcing", "upscaling", "market saturation"]),

    ("Entrepreneurship has influenced economic development and productivity by (i) "
     "altering the direction of national economies and ensuring their stability (ii) "
     "introducing quantum leaps in technology and creating new means of production and "
     "new systems of services (iii) forcing the reallocation of resources away from "
     "existing uses to new and more productive uses",
     "i, ii and iii are correct",
     ["i only is correct", "ii only is correct", "iii only is correct",
      "ii and iii only are correct"]),

    ("Entrepreneurs are often thought to be inspired people, and perhaps they are, but "
     "more important, they recognise changes and opportunities that can result from a "
     "dynamic world. These sources of change are (i) demographic and market changes (ii) "
     "scientific knowledge and the industrial revolution (iii) process innovation, social "
     "and cultural changes",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Distinguishing factors that differentiate entrepreneurs from small business persons "
     "are (i) vision for growth and energy to achieve unusual results (ii) taking "
     "individual risks and income substitution (iii) commitment to constructive change "
     "and persistence to gather necessary resources",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Many small businesses are small by (i) their nature (ii) the intention of the owner "
     "(iii) their creation through legal contracts",
     "i and ii only are correct",
     ["i, ii and iii are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Some of the main factors that lead to success for new ventures are (i) a well "
     "written business plan, a first-rate product, a charismatic entrepreneur loaded with "
     "talents and a great idea (ii) a fat bank account, a demand for the product or "
     "service, a well written feasibility plan and a business ideology (iii) a good "
     "entrepreneurial team, a well-planned enterprise that pursues incremental change and "
     "growth, good timing and a business ideology to serve customers",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Contributions by these European economists have helped to evolve our present "
     "understanding of entrepreneurship: (i) Carl Menger (ii) John Stuart Mill (iii) "
     "Jean Baptiste Say",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Corporate entrepreneurship (i) describes the process of helping established "
     "companies to be more productive (ii) is also called intrapreneurship (iii) "
     "describes the innovation that goes on in established companies through the efforts "
     "of creative employees",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Intrapreneurship is concerned with innovation that leads to new corporate divisions "
     "or subsidiary ventures in larger established firms. To achieve this, corporate "
     "managers (i) combine resources in unusual ways to create innovative new products or "
     "services (ii) take personal investment risks (iii) commit time and energy and risk "
     "careers",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("The reason for business failure is most commonly",
     "inexperience",
     ["external", "governmental", "internal", "excessive regulation"]),

    ("The risk of business failure for businesses starting from scratch is",
     "higher",
     ["lower", "not measurable", "no different from an established business",
      "unrelated to the mode of entry"]),

    ("Which of the following is not a reason for people going into business for "
     "themselves?",
     "to live where I like",
     ["to earn lots of money", "to enjoy independence", "to leave an inheritance",
      "to be one's own boss"]),

    ("Entrepreneurs typically form",
     "service businesses",
     ["a variety of companies", "construction companies", "financial companies",
      "manufacturing companies"]),

    ("Entrepreneurs typically have a high internal locus of control. This statement is",
     "true",
     ["false", "undefined", "true only for corporate managers",
      "true only for franchisees"]),

    ("Society and humankind as stakeholders have the following interest in a venture",
     "value added products and services",
     ["profitable return on investment", "wealth accumulation", "career positions",
      "income and job stability"]),

    # -- added 2026: found in the 2007/2008 and Canvas papers, previously missing --
    ("There are several thoughts about entrepreneurs that have been proven to be more "
     "myths than facts and these include (i) entrepreneurs struggle to succeed and get "
     "their ideas by hard work (ii) entrepreneurs are mavericks and misfits, and "
     "entrepreneurs are born (iii) entrepreneurs strike it rich with the first great "
     "flash of genius, or conversely they fail miserably with the first venture",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Entrepreneurs tend to be strategic thinkers who recognise changes and see "
     "opportunities where others do not. Major sources of change include (i) industrial "
     "changes and shop changes (ii) scientific knowledge and process innovations "
     "(iii) societal changes and socio-cultural changes",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("The concept of entrepreneurship (i) has given us a new direction for enterprises "
     "(ii) has just been discovered (iii) has been around for a very long time",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "ii only is correct",
      "iii only is correct"]),

    ("Entrepreneurship (i) was derived from the 17th century French word entreprendre "
     "(ii) refers to individuals who were undertakers and is a term that has been "
     "discovered by business students (iii) refers to people who are contractors and "
     "builders",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "ii only is correct",
      "iii only is correct"]),

    ("Entrepreneurs are",
     "high risk takers",
     ["moderate risk takers", "small risk takers", "risk averse people",
      "people for whom risk does not matter"]),

    ("Entrepreneurs",
     "are the life of the party",
     ["will never go to parties", "just fit into the crowd at a party",
      "are bores at a cocktail party", "avoid all social gatherings"]),
]

# ---------------------------------------------------------------------------
# SET 2 - Creativity and innovation
# ---------------------------------------------------------------------------
SET2 = [
    ("Which of the following is the ability to see, conceive, and create new and unique "
     "products, processes, or services?",
     "innovation",
     ["risk taking", "dedication", "creativity", "incubation"]),

    ("Creativity is best defined as",
     "the ability to bring something new into existence",
     ["the process of doing new things",
      "the verified result of a creative idea",
      "the conversion of something new into useful goods or services",
      "the translation of a useful idea into a commercial application"]),

    ("Innovation is best defined as",
     "the process of doing new things, that is, the transformation of creative ideas "
     "into useful applications",
     ["the ability to bring something new into existence",
      "the verified result of a creative idea",
      "the subconscious assimilation of information about a problem",
      "the conscious search for knowledge related to a problem"]),

    ("In the creative process, a person is said to be in the verification stage when he "
     "or she (i) applies or tests to prove that the idea has value (ii) embarks on a "
     "conscious search for bringing the idea to life (iii) has a sudden flash that the "
     "idea has merit",
     "i only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "iii only is correct"]),

    ("In the creative process, a person is said to be in the preparation stage when he or "
     "she",
     "embarks on a conscious search for bringing the idea to life",
     ["has a sudden flash that the idea has merit",
      "applies or tests to prove that the idea has value",
      "subconsciously assimilates information about the problem",
      "organises the resources needed to commercialise the idea"]),

    ("In the creative process, verification is",
     "application or test to prove that an idea has value",
     ["subconscious assimilation of knowledge",
      "recognition of an idea as being feasible",
      "conscious search for knowledge",
      "organising resources"]),

    ("In the creative process, the subconscious assimilation of information about a "
     "problem, often described as sleeping on the problem, is called",
     "incubation",
     ["idea germination", "preparation", "illumination", "verification"]),

    ("In the creative process, the stage at which an idea resurfaces as a realistic "
     "creation, often seeming to be a sudden flash of genius, is called",
     "illumination",
     ["idea germination", "preparation", "incubation", "verification"]),

    ("The seeding stage of a new idea, arising from a person's curiosity or interest in a "
     "problem or area of study, is called",
     "idea germination",
     ["preparation", "incubation", "illumination", "verification"]),

    ("The innovation process is the translation of useful ideas into useful application "
     "and has as some of its elements (i) organising resources and analytical planning "
     "(ii) idea germination, preparation and verification (iii) implementation and "
     "commercial application",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("For technological innovation to succeed, the key people that should be involved are "
     "(i) the inventor, the investor and the champion (ii) the creative source, the "
     "entrepreneur and the promoter (iii) the creative source, the champion and the sponsor",
     "iii only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),

    ("The brainstorming method for generating new product and venture ideas should be "
     "conducted using the following rules: (i) no criticism is allowed by anyone in the "
     "group and free wheeling is encouraged (ii) the period for generating ideas is "
     "predetermined and ideas found without merit are discarded (iii) a high quantity of "
     "ideas is desired and combinations and improvement of ideas are encouraged",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("A majority of new products evolve at the end of the technology spectrum as",
     "low-tech products",
     ["high-tech products", "mid-tech products", "natural products",
      "manufactured products"]),

    ("Something that begins with a person's interest or advocation, expands to include "
     "related types of products and market opportunities, then selectively follows a path "
     "of investigating each option, further expanding new business ideas, is called a",
     "mind map",
     ["product incubation", "product development model", "market research",
      "customer scenario"]),

    ("The principle which suggests that successful ventures evolve from entrepreneurs "
     "being positioned in similar work or having had experience with related ventures, so "
     "that when a window opens it is easy for them to move quickly into a new venture, is "
     "known as the",
     "corridor principle",
     ["window principle", "incubation principle", "segmentation principle",
      "creative destruction principle"]),

    # -- added 2026: found in the 2007/2008 paper, previously missing --
    ("Innovation is the development process of translating a new idea into a commercial "
     "reality and it involves (i) the translation of an idea into a new invention "
     "(ii) persistence in analytically working out the details of product design or "
     "service, developing marketing, obtaining finances and planning operations "
     "(iii) obtaining materials and technical manufacturing capabilities, staffing "
     "operations and establishing an organisation for the manufacture of a product",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("A number of industrial studies reveal that for a technological innovation to "
     "succeed there are three important people involved and seven important conditions "
     "to satisfy. The seven conditions include (i) a little support from external "
     "sources including government agencies, investors, vendors, suppliers and creditors "
     "(ii) a clear need for the application by sufficient potential consumers to warrant "
     "the commitment of resources to the innovation (iii) the realisation of the product, "
     "process or service as a useful innovation providing value to society",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),
]

# ---------------------------------------------------------------------------
# SET 3 - Business planning and the feasibility plan
# ---------------------------------------------------------------------------
SET3 = [
    ("A description of the future direction of a business is called",
     "a business plan",
     ["a forecast", "a roadmap", "a guide", "a template"]),

    ("The business plan is primarily supposed to",
     "give information to lenders and investors",
     ["guide the entrepreneur in the first year of operations",
      "tell interested parties about the venture",
      "provide information for the operations manager",
      "tell potential suppliers what is expected of them"]),

    ("When considering starting up a business, a business plan can",
     "provide direction, prove feasibility and attract money",
     ["provide direction only", "prove feasibility only", "attract money only",
      "replace the need for market research"]),

    ("Responsibility for planning a new venture rests on (i) consulting organisations "
     "with an established track record in new venture planning, such as Empretech (ii) "
     "universities with Entrepreneurship Centres such as KNUST School of Business (iii) "
     "the entrepreneur who has the vision and motivation and can therefore articulate the "
     "necessary information effectively",
     "iii only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),

    ("A feasibility plan should be prepared by (i) the entrepreneur alone (ii) a "
     "consultant in consultation with the entrepreneur (iii) the entrepreneur in "
     "consultation with specialists",
     "iii only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),

    ("A feasibility plan is a written document (i) which often integrates fundamental "
     "areas of business such as operations, marketing, finance and human resources (ii) "
     "that describes all the relevant external and internal elements involved in starting "
     "a new venture (iii) prepared by the entrepreneur",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("The model for developing a new entrepreneurial venture encompasses a feasibility "
     "plan which is (i) a summary of all the areas covered in the business plan (ii) a "
     "holistic business plan which covers all the segments in a typical plan of an "
     "existing company (iii) a pragmatic business plan reflecting the philosophy that "
     "entrepreneurs should do the planning necessary to ensure the feasibility of a "
     "venture without becoming overwhelmed in the process",
     "iii only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "ii and iii only are correct"]),

    ("The perspectives that should be considered when writing a business plan are (i) the "
     "perspective of the entrepreneur (ii) the marketing perspective (iii) the investor "
     "perspective",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Before an entrepreneur commits time and effort to do a business plan, he or she "
     "should see if there are any possible barriers to success. Information gathered "
     "should focus on (i) the market, finance and operations or manufacturing (ii) "
     "business concept and the entrepreneurial team (iii) goals and objectives of the "
     "venture, finance and product or service",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("One of the initial important elements of information needed by an entrepreneur to "
     "help him or her take decisions is (i) the market potential for the product(s) or "
     "service(s) (ii) basic operational needs such as manufacturing or operations and "
     "labour (iii) an evaluation of the profitability of the venture",
     "i only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "iii only is correct"]),

    ("The executive summary is the part of the plan that is written (i) to stimulate the "
     "interest of the reader (ii) in a concise and convincing manner covering the key "
     "points in a business plan (iii) after the whole plan is written",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("The difference between the venture definition in the executive summary and the "
     "business concept in the main body of the business plan is that",
     "the venture definition names the business and states why it was founded, while the "
     "business concept covers the business evolution and the nature of market demand",
     ["the venture definition is essentially a summary of the business concept",
      "the business concept includes the nature of the business and its technological profile",
      "the venture definition describes the technological profile of the venture",
      "the business concept states only why the business was founded"]),

    ("The introductory or cover page of a business plan should contain information on the "
     "business and should include",
     "a confidentiality clause",
     ["location of business", "the executive summary", "financial summary",
      "the full market research report"]),

    ("The introductory or cover page of a business plan should contain information on the "
     "business and should include (i) name and address of the business and the amount of "
     "financing required (ii) a statement of confidentiality of the report and the name "
     "and contacts of the entrepreneurs (iii) a brief description of the business concept",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("The common elements of a business plan include",
     "Executive Summary",
     ["Abstract", "Introduction", "Literature Review", "Product design"]),

    ("The organisational plan is the part of the business plan that describes",
     "the organogram of the venture",
     ["the physical layout of the facility", "the venture's form of ownership",
      "the mission and vision of the venture",
      "the context in which the organisation exists"]),

    ("Environmental and industry analysis of a business plan deals with (i) assessment of "
     "the location of the venture and its immediate area (ii) assessment of competitive "
     "strategies and industry trends (iii) assessment of external uncontrollable variables "
     "that may impact the business",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("For ventures that manufacture, design or sell products, as well as for service firms "
     "that require capital equipment, the manufacturing or operations section of the "
     "business plan is important. It should contain among others (i) leadership and the "
     "entrepreneurial team (ii) facilities and inventory (iii) operations and human "
     "resources",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("What type of information should be put in the appendix of a business plan write-up?",
     "Resumes of partners, facility layouts and partnership agreements",
     ["Marketing brochure with price list only",
      "Marketing brochure with price list and resumes of partners",
      "Partnership agreements and facility layouts only",
      "Partnership agreements and financial documentation"]),

    ("Many copies of a business plan are circulated and this can pose a security problem "
     "that can be countered by",
     "a non-disclosure statement",
     ["signing an agreement", "giving a verbal warning against stealing",
      "getting a declaration from the recipient",
      "hiding all vital information in the plan"]),

    ("Conditions that can render the most effective business plans out-of-date include",
     "changes in the market and the industry",
     ["changes in the life of the entrepreneur", "changes in competing businesses",
      "changes in cash flow", "changes in the entrepreneur's personal network"]),

    ("The most effective business plans can become out-of-date if conditions change. The "
     "conditions that can change the direction of a business plan are (i) poor "
     "articulation of the business concept (ii) loss or addition of key members of the "
     "team (iii) new location",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "ii and iii only are correct"]),

    ("Some business plans fail because (i) goals set by the entrepreneurs are unreasonable "
     "and unmeasurable (ii) the entrepreneur has not made a total commitment to the "
     "business (iii) the entrepreneur has no experience in the planned business",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Entrepreneurs can be described in terms of (i) experience and family background "
     "(ii) personal characteristics and skills (iii) successfully incubating a business",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    # -- added 2026: found in the 2007/2008 paper, previously missing --
    ("The information needed to develop the financial section of a business plan is "
     "gotten from, among other things, (i) the product and service description "
     "(ii) the operations or manufacturing segment (iii) the market research and "
     "analysis and market plan segments",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct",
      "ii and iii only are correct", "i only is correct"]),
]

# ---------------------------------------------------------------------------
# SET 4 - Stages of the venture and the start-up
# ---------------------------------------------------------------------------
SET4 = [
    ("Which stage describes the assembly of resources and organising the new venture for "
     "opening?",
     "Pre-start-up",
     ["Start-up", "Early growth", "Later growth", "Maturity"]),

    ("This type of growth model is concerned with the initial business operations",
     "Start-up",
     ["Pre-start-up", "Early growth", "Later growth", "Maturity"]),

    ("In which type of growth model does reality shock set in as the entrepreneur "
     "positions the business to compete in the real world?",
     "Start-up",
     ["Pre-start-up", "Early growth", "Later growth", "Maturity"]),

    ("The stage in which the venture has been initially successful and is growing at a "
     "healthy rate is",
     "Early growth",
     ["Pre-start-up", "Start-up", "Later growth", "Maturity"]),

    ("The stage in which the enterprise is established and the venture is professionally "
     "managed is",
     "Later growth",
     ["Pre-start-up", "Start-up", "Early growth", "Idea germination"]),

    ("Pre-start-up activities for new ventures include",
     "product or market survey",
     ["positioning the venture", "taking the company public",
      "keeping the rate of growth within a comfort limit",
      "professionalising the management team"]),

    ("There are two benchmark considerations for the start-up stage of any venture and "
     "they are",
     "meeting operating objectives and positioning the venture for long-term growth",
     ["surviving and attaining projected sales",
      "creating a vision and mission of the venture",
      "attaining projected sales and realising incremental growth",
      "making a profit and achieving long-term growth"]),

    ("Start-up operating objectives are",
     "sales, revenue, growth and position",
     ["production, sales, growth and profit",
      "growth, stability, sales and revenue",
      "adequate inventories, revenue, profits and sales",
      "position, growth, sales and stability"]),

    ("Measuring the progress of the business in the start-up stage is very important. The "
     "entrepreneur should",
     "make a 12 months schedule to see if the plan has been successfully achieved",
     ["determine the points at which decisions should be made",
      "on a frequent basis, check on the performance of the business",
      "check on other information such as inventory management and collection of accounts "
      "receivable",
      "delegate the monitoring to the board of advisors"]),

    ("Prior to start-up, entrepreneurs can reduce financial burdens by",
     "planning assets carefully",
     ["reducing the scope of work to be done",
      "cutting down on the planned capacity",
      "reducing the number of workers",
      "paying employees low salaries because it is a start-up venture"]),

    ("Financial planning in the pre-start-up stage will not necessarily be extensive but "
     "it has to be based on",
     "verifiable information",
     ["market research", "information from professional sources", "forecasts of profits",
      "financial statement analysis"]),
]

# ---------------------------------------------------------------------------
# SET 5 - Market research and the marketing plan
# ---------------------------------------------------------------------------
SET5 = [
    ("A market segment on which a business can choose to concentrate its efforts is known "
     "as a(n)",
     "market niche",
     ["economic zone", "shopping mall", "window of opportunity", "e-market"]),

    ("A market niche is a carefully defined segment of a broader market that defines the "
     "________ of a product or service to create a distinct marketing focus.",
     "positioning",
     ["existence", "placement", "location", "options"]),

    ("Setting up the specifications of one's primary clients can be described as a(n)",
     "customer scenario",
     ["telephone directory", "market survey", "biographical data",
      "demographic information"]),

    ("The objective of market research and analysis is to establish that a ________ exists "
     "for the proposed venture",
     "market",
     ["customer", "product", "competitor", "place"]),

    ("Market research and analysis activities include",
     "identify potential customers, evaluate markets, analyse competitors and describe "
     "assumptions",
     ["identify potential customers, analyse competitors and evaluate markets",
      "description of a customer profile",
      "product or service, its pricing, promotions and distribution",
      "product or service, its pricing, promotions and distribution, services and "
      "warranties described and marketing leadership roles defined"]),

    ("The market research culminates in a ________ that establishes the volume and revenue "
     "expected from business operations.",
     "sales forecast",
     ["financial statement", "market plan", "customer scenario", "market responsibilities"]),

    ("The results of good market research include (i) a well defined sales forecast (ii) a "
     "good estimate of revenue (iii) well defined investment needs",
     "i only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "iii only is correct"]),

    ("The main difference between market research analysis and market plan in a business "
     "plan is",
     "market research gathers the information and market plan then uses it in a marketing "
     "strategy to attract customers",
     ["market plan gathers the information and market research then uses it in a marketing "
      "strategy",
      "market research designs and conducts surveys and existing and potential markets are "
      "described in market plan",
      "all of them describe the market characteristics",
      "all of them describe the market proposal"]),

    ("The market plan tried to respond to the question",
     "who is the customer and where is he or she located?",
     ["where have we been and where are we going?",
      "where have we been, where are we going and how do we get there?",
      "where are the products going to be sold?",
      "where are the products going to be made?"]),

    ("The ________ describes an entrepreneur's intended strategy.",
     "market plan",
     ["distribution network", "operations", "promotions", "financial documentation"]),

    ("Marketing research activities that are undertaken after a new venture opens its "
     "doors for business is called",
     "competitive analysis",
     ["market planning", "marketing and sales", "competitive rivalry",
      "ending market research"]),

    ("A competitive analysis is marketing research (i) in the pre-start-up stage (ii) in "
     "the early growth stage (iii) in the start-up stage",
     "i only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "iii only is correct"]),

    ("The marketing functions include",
     "Product, Price, Distribution and Promotion",
     ["Process, Product and distribution", "Product Design, Promotion and Packaging",
      "Distribution, advertisement and packaging", "Product Design, Process and Promotion"]),

    ("An expanded view of a company's product includes",
     "function, form, packaging characteristics and service after sales support",
     ["function, form and packaging characteristics", "labelling, design and function",
      "safety and use information, labelling and design",
      "packaging, labelling and warranty terms"]),

    ("The planned process of determining prices and how prices can be changed in the field "
     "for unusual circumstances is known as",
     "pricing policy",
     ["price setting", "price discounting", "costing process", "sales commission"]),

    ("A broad term applied to marketing tactics that serve to attract customers or inform "
     "them of a product or service is known as",
     "promotion",
     ["advertisement", "publicity", "personal selling", "reduction sales"]),

    ("A careful selection of promotional methods consistent with a grand marketing strategy "
     "is called",
     "promotional mix",
     ["mixed marketing", "advertisement", "publicity", "public relations"]),

    ("As a start-up business, advertising is a vital part of your concerns in your quest to "
     "compete. Advertising will seek to (i) make a satisfied customer (ii) sell to someone "
     "even if they cannot afford to (iii) convince someone to walk in your door",
     "iii only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),

    ("Marketing Communications or Integrated Marketing Communications seeks to (i) "
     "consolidate all communications to present an individual, focussed marketing, sales or "
     "image message (ii) use an assortment of communications forms to deliver a variety of "
     "messages about the product, service or company (iii) develop a product, establish a "
     "price for it, communicate information about it and coordinate its distribution",
     "i only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "iii only is correct"]),

    ("Integrating promotion into the marketing mix seeks to (i) increase sales (ii) build "
     "recognition (iii) build consumer loyalty",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("A marketing plan is implemented through a",
     "marketing program",
     ["marketing activities", "marketing research", "marketing implementation",
      "marketing audit"]),

    ("Marketing Plan for a new venture (i) establishes how the entrepreneur will "
     "effectively compete and operate in the market (ii) describes the customer and the "
     "market (iii) comes out with solid data on projected sales",
     "i only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "iii only is correct"]),

    ("Marketing plans are ineffective or fail in meeting marketing goals for different "
     "reasons which include",
     "lack of a real plan, lack of adequate situation analysis, unrealistic goals and "
     "unanticipated competitive moves",
     ["lack of a real plan only", "lack of adequate situation analysis only",
      "unrealistic goals only", "unanticipated competitive moves only"]),

    ("A distribution system is (i) the process of taking materials through the production "
     "process (ii) the physical process of getting goods to market (iii) the process of "
     "locating services",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),

    ("The types of distribution channels that exist are",
     "consumer, industrial and service",
     ["consumer only", "industrial only", "service only", "consumer and industrial only"]),

    ("The infrastructure of a marketing plan is often built solely on a firm's ________ "
     "system.",
     "distribution",
     ["promotion", "product", "price", "warranty"]),

    ("Developing a clear profile of potential customers includes looking at their (i) age "
     "and sex (ii) income status (iii) locating the potential customer base",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    # -- added 2026: found in the 2007/2008 paper, previously missing --
    ("Used as a catchall term, product in marketing terms includes (i) the business "
     "concept, such as fast-food franchising (ii) physical objects or services being "
     "sold, together with packaging, image, brand name and warranty (iii) physical "
     "attributes that influence consumers perceptions, such as colours, shapes, sizes "
     "and materials",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct",
      "ii and iii only are correct", "i only is correct"]),

    ("As part of a market plan, a marketing strategy provides guidelines for the "
     "entrepreneur concerning (i) a marketing program which addresses the marketing "
     "activities (ii) expected results, allocation of resources and responsibilities "
     "for marketing (iii) ways in which the enterprise will be controlled",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct",
      "ii and iii only are correct", "i only is correct"]),
]

# ---------------------------------------------------------------------------
# SET 6 - Intellectual property and business law
# ---------------------------------------------------------------------------
SET6 = [
    ("A grant of a property right by a government to an inventor is called a",
     "patent",
     ["trade mark", "copyright", "service mark", "disclosure document"]),

    ("A patent search is done to determine",
     "if an inventor's creation already exists and remains actively protected under the law",
     ["patent summaries for prior claims or inventions",
      "the basic fees for a patent application",
      "what oaths and declarations have to be made with respect to a patent being sought",
      "the major sections of a patent filing document"]),

    ("A Disclosure Document, if filed by an entrepreneur, becomes important when",
     "a patent infringement has occurred",
     ["registering a company", "personal expense items are tax deductible",
      "two entrepreneurs are filing for patents on similar inventions",
      "a patent is published and becomes accessible to the public for review"]),

    ("A Disclosure Document is (i) the same as a patent (ii) a statement to the patent "
     "office by the inventor declaring the intent to patent an idea (iii) a brief "
     "description of the business concept",
     "ii only is correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "iii only is correct"]),

    ("The requirements for a successful utility patent grant include (i) that the inventor "
     "has taken personal investment risks (ii) proving that the creation is that of the "
     "person making the application (iii) the creation must be useful and new",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),

    ("A plant patent is given for (i) 17 years (ii) hybrid roses (iii) food grains",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),

    ("A trademark",
     "may be a particular sound, a word, a symbol, a design or a slogan, and can last "
     "indefinitely",
     ["may be a particular sound only", "may be a word or symbol only",
      "may be a word, a design or a slogan only", "can last indefinitely but must be a word"]),

    ("Filing of trade mark registrations meets these form requirements",
     "completion of the written form and payment of fee, drawing of the mark and five "
     "specimens showing actual use, and publication in the Trade Mark Official Gazette",
     ["completion of the written form and payment of fee only",
      "drawing of the mark and five specimens showing the actual use of the mark only",
      "publication in the Trade Mark Official Gazette only",
      "completion of the written form and payment of fee, plus the drawing and specimens only"]),

    ("Contracts are an important part of the transactions that an entrepreneur will make. "
     "The guidelines to follow include (i) describing the transaction in detail (ii) "
     "obtaining the signatures of the people with whom business is being done (iii) oral "
     "agreements are invalid for deals over one year",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("The best protection against product liability is (i) to produce zero defects in the "
     "products (ii) to produce safe products (iii) to warn customers of potential hazards",
     "ii and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i and iii only are correct",
      "i only is correct"]),
]

# ---------------------------------------------------------------------------
# SET 7 - Organising the new venture and legal forms of ownership
# ---------------------------------------------------------------------------
SET7 = [
    ("A person who is involved in a voluntary association with one or more other "
     "individuals and has operational responsibilities is called a",
     "General partner",
     ["Sole Partner", "Limited partner", "Sole proprietor", "Silent partner"]),

    ("A person or company that originates a business system and provides a package of "
     "services, products, training, inventory and support to individual owners in return "
     "for a fee and royalties is a",
     "Franchisor",
     ["Sole proprietor", "Franchisee", "Stakeholder", "Corporation"]),

    ("A business system created by a contract between a parent company and an acquiring "
     "business owner, giving the acquiring owner the right to sell goods or services, to "
     "use certain products, names or brands or to manufacture certain products is called a",
     "franchise",
     ["corporation", "franchisee", "franchisor", "general partnership"]),

    ("A legal form of business created through law that empowers a business as a legal "
     "entity and has a perpetual life unimpeded by the biological lifespan of investors is a",
     "corporation",
     ["company", "partnership", "franchise", "limited partnership"]),

    ("A legal organisation created through investments by two or more companies to pursue "
     "a commercial activity is known as a",
     "joint venture",
     ["partnership", "corporation", "limited liability company", "franchise"]),

    ("Selecting a legal form of business involves a decision with at least three important "
     "criteria, namely",
     "preferences of the entrepreneur, profile of the enterprise, and advantages and "
     "disadvantages of the legal business entity",
     ["preferences of the entrepreneur, taxation issues and profile of the enterprise",
      "management issues, profile of the enterprise and succession issues",
      "financing issues, management issues and profile of the enterprise",
      "taxation issues and succession issues"]),

    ("The main disadvantage of a sole proprietorship is",
     "unlimited legal and financial liability",
     ["the business ends with the owner's death",
      "the business assets are personal assets",
      "personal expense items are tax deductible",
      "income is undifferentiated from other income"]),

    ("Which of the following is an advantage of owning a sole proprietorship?",
     "easy to set up",
     ["lack of continuity", "limited resources", "unlimited liability",
      "few fringe benefits"]),

    ("Compared to other legal forms of business, the sole proprietorship has the singular "
     "advantage of simplicity. Other advantages include (i) autonomy of control, decision "
     "making and administration (ii) expanded network of contacts for assessing resources "
     "(iii) inexpensive as a form of business and self directing",
     "i and iii only are correct",
     ["i, ii and iii are correct", "i and ii only are correct", "i only is correct",
      "iii only is correct"]),

    ("A partnership, as a legal form of business, has certain disadvantages which include "
     "(i) business ends with the death or withdrawal of any partner (ii) unlimited legal "
     "liability for business by all parties (iii) limited access to external resources",
     "i and ii only are correct",
     ["i, ii and iii are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("Limited partners enjoy certain advantages over general partners that include (i) "
     "exemption from management responsibility (ii) profit and losses passed through to all "
     "partners (iii) investment can be sold or assigned",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("A disadvantage of owning a closely held corporation is",
     "expensive to start",
     ["transfer of ownership", "limited liability", "increased access to resources",
      "perpetual life"]),

    ("A formal board of directors is required by law only for",
     "incorporated companies",
     ["sole proprietorships", "partnerships", "limited liability companies",
      "master limited partnerships"]),

    ("The membership of a Board of Directors for a new venture should be",
     "5 to 9",
     ["5 to 7", "5 to 12", "6 to 12", "4 to 14"]),

    ("A board of advisors serves a new venture in an advisory capacity. An example is",
     "a lawyer, a banker, an accountant and an advertising agent",
     ["an advertising agent and a market researcher", "the manager and the accountant",
      "the shareholders and the officers", "the operations manager and the sales team"]),

    ("Directors of new ventures fulfil important roles beyond their decision-making duties "
     "that include (i) serving as members of an expanded social network (ii) mentors and "
     "professional advisors (iii) disturbance handlers and resource allocators",
     # 2005 official key: B, i and ii only. ME 492 2025 NOTES lists the roles as
     # mentors, professional advisers and members of an expanded social network.
     # Disturbance handling and resource allocation are not among them.
     "i and ii only are correct",
     ["i, ii and iii are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    ("The entrepreneurial team is a very vital part of the management team of a new "
     "venture. It is responsible for",
     "building an organisation, giving identity to the venture, focusing on operational "
     "issues and immediate problems, and guiding the venture through change",
     ["building an organisation only", "giving identity to the venture only",
      "focusing on operational issues and immediate problems only",
      "guiding the venture through change only"]),

    ("The responsibilities of the founder are",
     "defining their business and identifying human resource requirements",
     ["being responsible for the functional areas and managing the venture",
      "providing guidance and direction",
      "getting financing for the venture and setting the pace for development",
      "supervising employees and handling disturbances"]),

    ("After the legal form of business has been decided by the entrepreneur, the task of "
     "designing the organisation begins. The first step is to decide on the",
     "organisational structure",
     ["selection criteria", "training", "job analysis", "job specification"]),

    ("The organisation must identify the major activities required to operate it "
     "effectively. This is done through",
     "job analysis",
     ["job description", "job specification", "selection criteria", "performance appraisal"]),

    ("Individuals within someone's immediate circle of daily relationships is known as",
     "personal network",
     ["loose ties", "associations", "social network", "the entrepreneurial team"]),
]

# ---------------------------------------------------------------------------
# SET 8 - Financing the new venture
# ---------------------------------------------------------------------------
SET8 = [
    ("Money needed to purchase such physical facilities as buildings and equipment is "
     "referred to as",
     "fixed capital",
     ["working capital", "lending capital", "fluid capital", "venture capital"]),

    ("Money used to pay the rent and utility bills, to purchase inventories, and to cover "
     "payroll expenses is referred to as",
     "working capital",
     ["lending capital", "fluid capital", "fixed capital", "seed capital"]),

    ("Which of the following is money held in reserve for emergency situations, usually in "
     "the form of cash or disposable securities such as stocks, bonds and certificates of "
     "deposit?",
     "fluid capital",
     ["working capital", "lending capital", "fixed capital", "replacement capital"]),

    ("Lending institutions provide entrepreneurs with short term loans primarily for",
     "working capital",
     ["lending capital", "fluid capital", "fixed capital", "replacement capital"]),

    ("Entrepreneurs use ________ to purchase major fixed capital investments such as "
     "buildings and land.",
     "long-term financing",
     ["short-term financing", "intermediate term financing",
      "intermediate and long term financing", "trade credit"]),

    ("If short term financing is used by a new venture, the funds are repaid from",
     "sales and profits",
     ["dividend", "fixed assets", "cash budget", "capital"]),

    ("By far the most frequently used source of short-term funds by the entrepreneur when "
     "collateral is available is",
     "commercial bank",
     ["venture capital", "personal funds", "development capital", "trade credit"]),

    ("Which of the following is intended for higher risks such as start up situations?",
     "venture capital",
     ["development capital", "replacement capital", "owners capital", "working capital"]),

    ("Investors who look for businesses that offer extremely high growth and profit "
     "potential, have a willingness to exchange equity, and show potential to cash out in "
     "five years are called",
     "Venture capitalists",
     ["Private placement specialists", "International Procurement Organisations agents",
      "Commercial bankers", "Angel employees"]),

    ("Asset-based financing refers to",
     "debt financing",
     ["equity financing", "internal funds", "external funds", "retained earnings"]),

    ("Which of the following does not require collateral and offers the investor some form "
     "of ownership position in the venture?",
     "equity financing",
     ["debt financing", "vendor capital", "common stock", "trade credit"]),

    ("Government grants for a new business can be referred to as",
     "external fund",
     ["debt financing", "equity financing", "internal fund", "retained earnings"]),

    ("________ are the least expensive funds in terms of cost and control, and also are "
     "absolutely essential in attracting outside funding, particularly from banks, private "
     "investors and venture capitalists.",
     "Personal funds",
     ["Funds from family and friends", "Retained earnings", "Government grants",
      "Venture capital"]),

    ("Long term debt is frequently used to purchase some asset such as a piece of "
     "machinery, land or a building, with part of the value of the asset, usually from "
     "________ percent of the total value, being used as collateral.",
     "50 to 80",
     ["40 to 60", "50 to 75", "70 to 90", "60 to 85"]),

    ("When interest rates are low, ________ financing allows the entrepreneur to retain a "
     "larger ownership portion in the venture and have a greater return on equity.",
     "debt",
     ["internal", "external", "equity", "vendor"]),

    ("________ is the term commonly used to describe the ordinary share capital of a "
     "business.",
     "Equity",
     ["Asset", "Liability", "Bond", "Net worth"]),

    ("________ represents the amount owners have invested and or retained from the venture "
     "operations",
     "net worth",
     ["liability", "asset", "investment", "dividend"]),

    ("The component of equity in a business representing accumulated profits in excess of "
     "losses and payments to owners is referred to as",
     "retained earnings",
     ["dividend", "preferred stock", "common stock", "net worth"]),

    ("An obligation arising from the purchase of goods or services on credit is referred to "
     "as",
     "account payable",
     ["account receivable", "accumulated account", "note", "covenant"]),

    ("Money due from an individual or another business as payment for the performance of "
     "services or the sale of goods on credit is known as",
     "account receivable",
     ["account payable", "accumulated account", "note", "retained earnings"]),

    ("________ is the integration and synchronisation of the various financial activities "
     "of a business in order that all its functions can work towards its common objectives.",
     "Financial co-ordination",
     ["Financial control", "Financial planning", "Financial organising", "Budgeting"]),

    ("Restrictions to loan agreements are called",
     "covenants",
     ["intrusions", "collateral", "guarantees", "indentures"]),

    ("Cash flow equals",
     "receipts minus disbursements",
     ["receipts plus owner's equity", "liabilities minus expenses",
      "liabilities plus owner's equity", "revenue minus retained earnings"]),

    ("Determining which source of funding entrepreneurs use depends on the following except",
     "money portability",
     ["the nature and size of the business",
      "the type of financing the entrepreneur needs",
      "the entrepreneur's particular financial condition",
      "whether the funds are needed for short, intermediate or long term credit"]),

    ("Lenders to a new venture typically focus on aspects of credit character which include "
     "(i) cash flow (ii) collateral (iii) equity contribution",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct", "i only is correct",
      "iii only is correct"]),

    # -- added 2026: found in the Canvas paper, previously missing --
    ("Resources expected to produce current and future benefits are referred to as",
     "assets",
     ["capital", "liabilities", "shareholding", "net worth"]),
]

# ---------------------------------------------------------------------------
# SET 9 - Budgeting, the master budget and pro forma statements
# ---------------------------------------------------------------------------
SET9 = [
    ("________ is a process that involves co-ordinating the finances of all areas of the "
     "new venture.",
     "Budgeting",
     ["Cost accounting", "Financial accounting", "Management accounting",
      "Strategic planning"]),

    ("________ involves deciding which market niche should be profitable.",
     "Strategic planning",
     ["Operating budgeting", "Capital budgeting", "Sales forecasting",
      "Tactical budgeting"]),

    ("Which of the following involves making decisions such as whether to buy or lease "
     "equipment?",
     "capital budgeting",
     ["strategic planning", "operating budgeting", "tactical budgeting",
      "sales forecasting"]),

    ("Which of the following budgets is expected to be more specific?",
     "operating budgeting",
     ["tactical budgeting", "capital budgeting", "strategic planning",
      "financial statement budgeting"]),

    ("The three major budget categories in the master budget consist of operating budgets, "
     "capital budgets and",
     "financial statement budgets",
     ["strategic plans", "tactical budgets", "cash budgets", "pro forma statements"]),

    ("The master budget normally covers a",
     "one-year time span",
     ["five year time span", "three year time span", "three month time span",
      "six month time span"]),

    ("The budgeting process normally begins with the preparation of",
     "operating budgets",
     ["capital budgets", "financial statement budgets", "strategic budgets",
      "pro forma statements"]),

    ("The first step in the preparation of the operating budget is",
     "sales forecast",
     ["cash requirements", "inventory forecast", "purchases forecast",
      "capital expenditure forecast"]),

    ("The composition of the numerous separate but interdependent departmental budgets that "
     "cover a wide range of operating and financial factors such as sales, production, "
     "manufacturing expenses and administrative expenses is known as",
     "master budget",
     ["operating budget", "capital budget", "pro forma statements", "cash budget"]),

    ("Perpetual or continuous budgeting utilises",
     "a 12-month reporting period",
     ["a 3-month reporting period", "a 6-month reporting period",
      "a 3-year reporting period", "a 5-year reporting period"]),

    ("________ budgets are intended to provide a basis for evaluating expenditures that "
     "will impact the business for more than one year.",
     "Capital",
     ["Operating", "Strategic", "Frontline", "Tactical"]),

    ("Budgeted financial statements prepared from information in the master budget refer to",
     "pro forma statements",
     ["operating budget statements", "participative budget statements",
      "budget committee statements", "cash flow statements"]),

    ("A budget is",
     "prepared primarily as a planning function, administered as a control function, and a "
     "statement of expected results or requirements expressed in financial or numerical terms",
     ["prepared primarily as a planning function only",
      "administered as a control function only",
      "a statement of expected results or requirements expressed in financial or numerical "
      "terms only",
      "an audited record of past financial performance"]),

    ("Which of the following is true?",
     "information contained in the operating budgets is used to prepare the financial "
     "statement budgets",
     ["information contained in the financial statement budgets is used to prepare the "
      "operating budgets",
      "information contained in the tactical budgets is used to prepare the operating budgets",
      "information contained in the operating budgets is used to prepare the strategic budgets",
      "information contained in the cash budget is used to prepare the sales budget"]),

    ("Pro forma income statements are",
     "projected net profits calculated from projected revenues and projected costs and "
     "expenses",
     ["projected cash available gotten from projected cash accumulated and projected "
      "disbursements",
      "summaries of projected assets, liabilities and net worth",
      "summaries of projected net profits, assets, liabilities and net worth",
      "volumes of sales where the venture makes neither a profit nor a loss"]),

    ("________ summarises the projected assets, liabilities and equity of the new venture.",
     "Pro forma balance sheet",
     ["Pro forma income statement", "Pro forma cash flow",
      "Pro forma accounting statement", "Cash budget"]),

    ("What are the main segments of a pro forma balance sheet?",
     "Assets, liabilities and owners equity",
     ["Owners equity and retained earnings", "Fixed assets", "Current liabilities",
      "Revenues, costs and expenses"]),

    ("Projected cash available calculated from projected cash accumulations minus projected "
     "cash disbursements refers to",
     "pro forma cash flow",
     ["cash budget", "sales budget", "pro forma income", "pro forma balance sheet"]),

    ("In the preparation of the pro forma income statement, the entrepreneur must first "
     "develop a",
     "Sales budget",
     ["Cash flow statement", "Sales revenue projection", "Selling and administrative "
      "statement", "Material inventory schedule"]),

    ("Before developing the pro forma income statement, the entrepreneur should prepare the",
     "capital and operating budgets",
     ["strategic plan and operating budgets", "strategic plan and capital budgets",
      "tactical and strategic budgets", "cash budget and sales forecast"]),

    ("A prediction of what a company's financial statements will look like at the end of "
     "the forecast period is called",
     "a pro forma statement",
     ["a forecast statement", "a balance sheet", "a future statement",
      "an income statement"]),

    ("Which of the following statements is referred to as a summary of operations?",
     "income statement",
     ["balance sheet", "statement of cash flows", "statement of retained earnings",
      "pro forma balance sheet"]),

    ("Depending on the nature of a business, a manufacturing or operation plan may not be "
     "required in the business plan, but for ventures that require capital equipment this "
     "section is important and should be made up of",
     "operations, human resources, facilities, inventory and related issues",
     ["facilities, inventory and operations",
      "equipment, technology, raw materials, human resources and operations",
      "legal and insurance, operations and related issues",
      "vendor relations, operations, suppliers and related issues"]),

    ("Which of the following represents a long-term solvency ratio?",
     "debt to equity ratio",
     ["return on equity", "equity ratio", "assets turnover ratio", "current ratio"]),

    # -- added 2026: found in the 2007/2008 and Canvas papers, previously missing --
    ("In preparing the pro forma balance sheet, the entrepreneur will require the use of "
     "(i) pro forma income and cash flow statements (ii) operations and sales budgets "
     "(iii) capital budgets prepared under different scenarios",
     "i, ii and iii are correct",
     ["i and ii only are correct", "i and iii only are correct",
      "ii and iii only are correct", "i only is correct"]),

    ("A statement of estimated income and expenses over a specified period of time is "
     "known as a",
     "budget",
     ["operating budget", "capital budget", "master budget", "financial statement"]),

    ("Which of the following is a formal plan expressed in numerical terms?",
     "budget",
     ["performance evaluation", "financial statement", "production schedule",
      "proposal"]),

    ("Administration plans generally cover a period of",
     "less than 1 year",
     ["five years or less", "more than 5 years", "more than 10 years",
      "exactly 3 years"]),
]

# ---------------------------------------------------------------------------
# SET 10 - Calculations (sales budget, growth, cash budget)
# ---------------------------------------------------------------------------
SET10 = [
    ("Topsy Turvy Company Ltd sells furniture. It had a beginning balance of $40,000 in "
     "accounts receivable on 1 October and normally collects 100 percent of accounts "
     "receivable in the month following the month of sale. Cash sales are $15,000, $17,250 "
     "and $19,838, and sales on account are $45,000, $51,750 and $59,513 for October, "
     "November and December respectively. Determine the accounts receivable for October.",
     "$40,000",
     ["$75,000", "$55,000", "$45,000", "$15,000"]),

    ("Using the Topsy Turvy data (beginning accounts receivable $40,000; sales on account "
     "of $45,000, $51,750 and $59,513 for October, November and December), determine the "
     "accounts receivable for November.",
     "$45,000",
     ["$62,250", "$17,500", "$61,250", "$69,000"]),

    ("Using the Topsy Turvy data (sales on account of $45,000, $51,750 and $59,513 for "
     "October, November and December), determine the accounts receivable for December.",
     "$51,750",
     ["$72,300", "$79,351", "$66,274", "$54,450"]),

    ("Using the Topsy Turvy data (cash sales of $15,000, $17,250 and $19,838 for October, "
     "November and December), determine the budgeted cash sales for October.",
     "$15,000",
     ["$65,000", "$45,000", "$55,000", "$60,000"]),

    ("Using the Topsy Turvy data (cash sales of $15,000, $17,250 and $19,838 for October, "
     "November and December), determine the budgeted cash sales for December.",
     "$19,838",
     ["$71,588", "$79,351", "$59,513", "$73,200"]),

    ("Topsy Turvy Company Ltd collects 100 percent of accounts receivable in the month "
     "following the month of sale. Sales on account are $45,000, $51,750 and $59,513 for "
     "October, November and December. Determine the amount of accounts receivable that "
     "will appear on the company's fourth quarter pro forma balance sheet.",
     "$59,513",
     ["$79,351", "$51,750", "$19,838", "$45,000"]),

    ("Topsy Turvy Company Ltd has total budgeted sales of $60,000, $69,000 and $79,351 for "
     "October, November and December. Determine the amount of sales revenue that will "
     "appear on the company's fourth quarter pro forma income statement.",
     "$208,351",
     ["$188,838", "$156,263", "$52,088", "$19,838"]),

    ("Kaneapa Company Ltd had a beginning balance of $60,000 in accounts receivable on 1 "
     "October and collects 100 percent of accounts receivable in the month following the "
     "month of sale. Sales on account are $45,000, $49,500 and $54,450 for October, "
     "November and December. Determine the accounts receivable for November.",
     "$45,000",
     ["$67,000", "$71,500", "$82,000", "$105,000"]),

    ("Kaneapa Company Ltd has cash sales of $20,000, $22,000 and $24,200 for October, "
     "November and December. Determine the budgeted cash sales for November.",
     "$22,000",
     ["$67,000", "$49,500", "$71,500", "$82,000"]),

    ("Dandy Electronics Company Ltd has no accounts receivable on 1 October. Its sales on "
     "account are GH¢337,500, GH¢421,875 and GH¢527,344 for October, November and December, "
     "and total budgeted collections are GH¢787,500, GH¢1,321,875 and GH¢1,652,344. "
     "Determine the accounts receivable for November.",
     "GH¢337,500",
     ["GH¢984,375", "GH¢900,000", "GH¢787,500", "GH¢421,875"]),

    ("Dandy Electronics Company Ltd has sales on account of GH¢337,500, GH¢421,875 and "
     "GH¢527,344 for October, November and December. Determine the amount of accounts "
     "receivable that will appear on the company's fourth quarter pro forma balance sheet.",
     "GH¢527,344",
     ["GH¢652,344", "GH¢421,875", "GH¢1,757,813", "GH¢337,500"]),

    ("Dandy Electronics Company Ltd has total budgeted sales of GH¢1,125,000, GH¢1,406,250 "
     "and GH¢1,757,813 for October, November and December. Determine the amount of sales "
     "revenue that will appear on the company's fourth quarter pro forma income statement.",
     "GH¢4,289,063",
     ["GH¢1,652,344", "GH¢1,757,813", "GH¢3,761,719", "GH¢2,531,250"]),

    ("Dandy Electronics Company Ltd has total budgeted sales of GH¢1,125,000, GH¢1,406,250 "
     "and GH¢1,757,813 for October, November and December. Compute the expected increase in "
     "sales per month during November and December.",
     "25 percent",
     ["40 percent", "30 percent", "20 percent", "35 percent"]),

    ("GoldCom Corporation has three divisions preparing a sales budget. First quarter sales "
     "are East $520,000, West $740,000 and South $340,000. Growth expectations per quarter "
     "are 2 percent for East, 3 percent for West and 5 percent for South. Determine the "
     "sales in the fourth quarter for the West Division.",
     "$808,618",
     ["$840,924", "$551,828", "$393,593", "$762,200"]),

    ("GoldCom Corporation has first quarter sales of East $520,000, West $740,000 and South "
     "$340,000, with quarterly growth of 2 percent, 3 percent and 5 percent respectively. "
     "Determine the amount of sales revenue that will appear on the company's fourth "
     "quarter pro forma income statement.",
     "$1,754,039",
     ["$1,649,600", "$1,700,924", "$1,826,326", "$1,600,000"]),

    ("Hokus Pokus Company Ltd has three districts. First quarter sales are Kumasi $650,000, "
     "Accra $880,000 and Cape Coast $420,000. Growth expectations per quarter are 4 percent "
     "for Kumasi, 5 percent for Accra and 10 percent for Cape Coast. Determine the sales in "
     "the fourth quarter for the Accra District.",
     "$1,018,710",
     ["$924,000", "$970,200", "$1,069,646", "$1,161,000"]),

    ("Hokus Pokus Company Ltd has first quarter sales of Kumasi $650,000, Accra $880,000 "
     "and Cape Coast $420,000, with quarterly growth of 4 percent, 5 percent and 10 percent "
     "respectively. Determine the amount of sales revenue that will appear on the company's "
     "fourth quarter pro forma income statement.",
     "$2,308,892",
     ["$1,649,600", "$1,749,872", "$2,452,326", "$1,950,000"]),

    ("Osagyefo Clothing Company Ltd wants a cash cushion of GH¢40,000 before the interest "
     "payment at the end of each month. Its July ending cash balance is GH¢34,000 and "
     "August cash receipts are GH¢486,000. Compute the total cash available for August.",
     "GH¢520,000",
     ["GH¢525,000", "GH¢496,250", "GH¢485,000", "GH¢540,000"]),

    ("Osagyefo Clothing Company Ltd has an August ending cash balance of GH¢31,000 and "
     "September cash receipts of GH¢749,000. Compute the total cash available for September.",
     "GH¢780,000",
     ["GH¢749,000", "GH¢775,000", "GH¢795,000", "GH¢718,000"]),

    ("Osagyefo Clothing Company Ltd has total cash available of GH¢520,000 for August and "
     "total budgeted disbursements of GH¢540,000. Determine the cash shortage for August.",
     "GH¢20,000",
     ["GH¢40,000", "GH¢65,000", "GH¢80,000", "GH¢60,000"]),

    ("Osagyefo Clothing Company Ltd has total cash available of GH¢780,000 for September "
     "and total budgeted disbursements of GH¢632,000. Determine the cash surplus for "
     "September.",
     "GH¢148,000",
     ["GH¢105,000", "GH¢120,500", "GH¢80,000", "GH¢188,000"]),

    ("Osagyefo Clothing Company Ltd has an August cash shortage of GH¢20,000 and wants to "
     "keep a cash cushion of GH¢40,000. Calculate the amount to be borrowed for August.",
     "GH¢60,000",
     ["GH¢90,000", "GH¢40,000", "GH¢120,000", "GH¢20,000"]),

    ("Osagyefo Clothing Company Ltd has a September cash surplus of GH¢148,000 and wants to "
     "keep a cash cushion of GH¢40,000. Calculate the amount to be repaid for September.",
     "GH¢108,000",
     ["GH¢92,000", "GH¢65,500", "GH¢40,000", "GH¢148,000"]),

    ("Osagyefo Clothing Company Ltd is charged interest at 5 percent per month. Its loan "
     "balances after financing are GH¢120,000 in July, GH¢180,000 in August and GH¢72,000 "
     "in September. Compute the total amount of interest expense for the third quarter.",
     "GH¢18,600",
     ["GH¢18,000", "GH¢16,200", "GH¢15,400", "GH¢21,600"]),

    ("Birdy-Birdy's Jewellery Shop wants a cash cushion of GH¢9,000 before the interest "
     "payment at the end of each month. Its July ending cash balance is GH¢7,139 and August "
     "cash receipts are GH¢180,000. Compute the total cash available for August.",
     "GH¢187,139",
     ["GH¢100,440", "GH¢163,718", "GH¢190,225", "GH¢180,000"]),

    ("Birdy-Birdy's Jewellery Shop has an August ending cash balance of GH¢7,214 and "
     "September cash receipts of GH¢216,000. Compute the total cash available for September.",
     "GH¢223,214",
     ["GH¢440,400", "GH¢229,226", "GH¢189,440", "GH¢216,000"]),

    ("Birdy-Birdy's Jewellery Shop has total cash available of GH¢187,139 for August and "
     "total budgeted disbursements of GH¢174,400. Determine the cash surplus for August.",
     "GH¢12,739",
     ["GH¢19,558", "GH¢25,387", "GH¢17,125", "GH¢9,000"]),

    ("Birdy-Birdy's Jewellery Shop has a September cash surplus of GH¢23,198 and wants to "
     "keep a cash cushion of GH¢9,000. Calculate the amount to be repaid for September.",
     "GH¢14,198",
     ["GH¢17,312", "GH¢19,851", "GH¢27,324", "GH¢23,198"]),

    ("Birdy-Birdy's Jewellery Shop is charged interest at 2 percent per month. Its loan "
     "balances after financing are GH¢93,060 in July, GH¢89,321 in August and GH¢75,123 in "
     "September. Compute the total amount of interest expense for the third quarter.",
     "GH¢5,150",
     ["GH¢2,230", "GH¢6,590", "GH¢7,340", "GH¢4,650"]),

    ("Birdy-Birdy's Jewellery Shop has September total cash available of GH¢223,214, total "
     "disbursements of GH¢200,016, a repayment of GH¢14,198 and interest of GH¢1,502. "
     "Compute the ending cash balance for the month of September.",
     "GH¢7,498",
     ["GH¢7,356", "GH¢7,532", "GH¢7,667", "GH¢9,000"]),
]

# ---------------------------------------------------------------------------
# SET 11 - The "because" statement section
# ---------------------------------------------------------------------------
BECAUSE_OPTIONS = [
    "both statements are TRUE and the second is a correct explanation of the first",
    "both statements are TRUE and the second is NOT a correct explanation of the first",
    "the first statement is TRUE and the second is FALSE",
    "the first statement is FALSE and the second is TRUE",
    "both statements are FALSE",
]


def because(s1, s2, answer_index):
    """Build a 'because' item. answer_index is 0..4 matching BECAUSE_OPTIONS."""
    stem = (f"Consider the two statements below. S1: {s1} BECAUSE S2: {s2} "
            "Select the correct response.")
    correct = BECAUSE_OPTIONS[answer_index]
    distractors = [o for i, o in enumerate(BECAUSE_OPTIONS) if i != answer_index]
    return (stem, correct, distractors)


SET11 = [
    because("Entrepreneurs dealing in low tech products should focus on products that can "
            "be made easily, marketed quickly, and terminated with a minimum of effort.",
            "Patents cannot protect low tech products and they can be copied or easily "
            "replicated by competitors.", 2),

    because("Entrepreneurs have to be inventive geniuses to pursue mid-tech innovations.",
            "Mid-tech products presume the application of new knowledge.", 4),

    because("Differentiating high-tech from mid-tech products is largely a matter of "
            "perception.",
            "What is a high-tech product to some may be a mid-tech product to others.", 0),

    because("New ventures establish in a market niche.",
            "Companies try to establish segmentation strategies so that efficient use of "
            "resources can be achieved without ambiguity.", 0),

    because("Market research is a fundamental part of planning a new venture.",
            "A market research will establish primarily if demand exists for a product or "
            "service.", 0),

    because("Feasibility plans are best prepared by specialists.",
            "Specialists, such as financial experts, know how to operate businesses.", 4),

    because("Prices for goods and services must coincide with strategies that reinforce an "
            "entrepreneur's business and reputation.",
            "Prices of products and services communicate perceptual messages to consumers.",
            0),

    because("Seed financing is needed prior to or during start-up of a new venture.",
            "Seed financing is needed to underwrite operations, assets or business "
            "development.", 0),

    because("Intrapreneur is a contrived word meaning a person who pursues an innovation, "
            "becoming a champion for its development within an organisation.",
            "The word is from intra-company entrepreneur.", 0),

    because("A good way to fail quickly in a new business is to start without a clear "
            "vision.",
            "A business without a clear vision shows a lack of understanding of marketing "
            "issues.", 0),

    because("Planning is a process that never ends for a new venture.",
            "Businesses evolve from early start-up to a final growth stage if planning is "
            "done well in the beginning.", 0),

    because("Most technical entrepreneurs tend to start businesses closely related to what "
            "they did in previous career positions.",
            "The success of entrepreneurs is based on a business ideology which is defined "
            "as a system of beliefs about how one conducts an enterprise.", 0),

    because("There are more male entrepreneurs than female entrepreneurs.",
            "Men tend to launch ventures early in their lives, but women tend to become "
            "entrepreneurs after their children are grown.", 0),

    because("Market potential is critically influenced by the timing of new products or "
            "services.",
            "Timing pertains to when products or services are introduced, how they are "
            "priced, how they are distributed and how they are promoted.", 0),

    because("An extraordinary change is taking place as services which used to be done by "
            "government workers are now being privatised in Ghana and elsewhere in the "
            "world.",
            "Abrupt changes take place in the composition of populations and create the "
            "need for new programmes and services.", 0),

    because("All financial forecasts and projections are based on a number of financial "
            "assumptions.",
            "The outcomes of future events are not predictable.", 0),

    because("Investors put greater emphasis on the entrepreneurial team than on the "
            "business concept.",
            "This has become an axiom common among venture capitalists who will buy into an "
            "A team with a B product faster than they will buy into a B team with an A "
            "product.", 1),

    because("Inventors often place more emphasis on the entrepreneur's character than "
            "lenders and often spend much more time conducting background checks.",
            "Inventors provide large sums of money in the form of equity that they will be "
            "cashing out in a year or two.", 4),
]

# ---------------------------------------------------------------------------
ALL_QUESTIONS = (SET1 + SET2 + SET3 + SET4 + SET5 + SET6 + SET7 + SET8
                 + SET9 + SET10 + SET11)
OUTPUT_FILE = "compiled.json"


ROMAN_PART = re.compile(r"\s*\((i|ii|iii|iv|v|vi)\)\s*")


def format_parts(text):
    """Put each (i) (ii) (iii) part of a stem on its own line."""
    if "(i)" not in text:
        return text
    return ROMAN_PART.sub(lambda m: "\n(" + m.group(1) + ") ", text).strip()


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def balanced_positions(count, slots, rng):
    """Return `count` slot indices spread as evenly as possible over `slots`."""
    per_slot, remainder = divmod(count, slots)
    positions = []
    for slot in range(slots):
        positions += [slot] * (per_slot + (1 if slot < remainder else 0))
    rng.shuffle(positions)
    return positions


def main():
    rng = random.Random(492)  # reproducible key placement

    # Questions carry either 4 or 5 options. Balance the key position within
    # each group so no option slot is over-represented.
    groups = {}
    for idx, item in enumerate(ALL_QUESTIONS):
        n_opts = len(item[2]) + 1
        groups.setdefault(n_opts, []).append(idx)

    position_for = {}
    for n_opts, indices in sorted(groups.items()):
        for idx, pos in zip(indices, balanced_positions(len(indices), n_opts, rng)):
            position_for[idx] = pos

    summary = {}
    records = []
    missing = []
    for idx, (q_text, correct, distractors) in enumerate(ALL_QUESTIONS):
        pos = position_for[idx]
        options = build_options(distractors, correct, pos)
        assert options[pos] == correct
        assert len(set(options)) == len(options), q_text[:60]
        summary[pos] = summary.get(pos, 0) + 1
        number = idx + 1
        record = {
            "question_number": number,
            "question_text": format_parts(q_text),
            "options": options,
            "correct_answer": [correct],
        }
        entry = EXPLANATIONS.get(number)
        if entry:
            stem_prefix, why, source = entry
            # Guard against a reordered set silently pairing the wrong text.
            assert " ".join(q_text.split()).startswith(stem_prefix), number
            record["explanation"] = why
            record["source"] = source
        else:
            missing.append(number)
        record["verified"] = verification(number)
        records.append(record)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)
    print(f"Wrote {OUTPUT_FILE}: {len(records)} questions")
    if missing:
        print(f"  no explanation yet for {len(missing)}: {missing[:12]}...")
    else:
        print("  every question carries an explanation")

    counts = {}
    for n_opts, indices in sorted(groups.items()):
        counts[n_opts] = len(indices)
    print("\nOptions per question:")
    for n_opts, n in sorted(counts.items()):
        print(f"  {n_opts} options: {n} questions")

    total = sum(summary.values())
    print("\nKey distribution (option slot -> count):")
    for slot in sorted(summary):
        share = summary[slot] / total
        print(f"  slot {chr(65 + slot)}: {summary[slot]} ({share:.0%})")
    print(f"  total: {total}")

    print("\nQuestions per set:")
    for name, group in [("Entrepreneurship & free enterprise", SET1),
                        ("Creativity & innovation", SET2),
                        ("Business planning & feasibility", SET3),
                        ("Venture stages & start-up", SET4),
                        ("Market research & marketing plan", SET5),
                        ("Intellectual property & law", SET6),
                        ("Organising & legal forms", SET7),
                        ("Financing the new venture", SET8),
                        ("Budgeting & pro forma statements", SET9),
                        ("Calculations", SET10),
                        ("'Because' statements", SET11)]:
        print(f"  {name}: {len(group)}")


if __name__ == "__main__":
    main()
