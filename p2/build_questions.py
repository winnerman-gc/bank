#!/usr/bin/env python3
"""
Build the Telecommunications Policy & Regulation PAST-PAPER practice bank.

Source material:
  - p2/Policy.pdf  (photographs of a past examination paper for the TE 452 /
    TE 462 Policy & Regulation course; "Section A" is 60 shuffled multiple-choice
    questions, "Section B" is 4 essay questions).

Unlike the other MCQ banks in this repo (which are freshly authored and have their
option order balanced by a script), this file is a faithful TRANSCRIPTION of a real
past paper.  For that reason:

  * The original options (a)-(e) are preserved verbatim and in their original order.
    (The website reshuffles option display order per-question at run time, just like
    the sibling sites, so the source order here is only the source of truth.)
  * The correct answer for each question was determined independently from the course
    lecture decks in ../policy/ (TE 452 - 1&2, TE 462 - Framework for Regulation,
    TE 462 - Licensing Telecommunication Services) -- NOT from the answers circled on
    the exam photos, many of which are wrong.

Questions Q12, Q20, Q21, Q31, Q32 and Q33 are omitted: those pages were not captured
in the photographs.  Q13, Q22 and Q34 had their stems cut off at a page top; their
stems are reconstructed from the visible options + course material and are marked
[stem reconstructed] below.

Output JSON matches the format used by the other practice sites:

    {
      "question_number": 1,
      "question_text": "...",
      "options": ["...", ...],           # original (a)-(e) order
      "correct_answer": ["..."]
    }
"""
import json

# Each entry: (exam_number, question_text, [options in original a-e order], correct_answer)
QUESTIONS = [
    (1,
     "The factors that encouraged the monopoly paradigm in the telecommunication "
     "sector can be categorized as",
     ["social, political and economic",
      "political and economic",
      "social and political",
      "social and economic",
      "None of the above"],
     "political and economic"),

    (2,
     "WTO aims at",
     ["establishing rules for domestic trade",
      "restricting trade practices",
      "liberalising international trade",
      "encouraging entrepreneurs",
      "None of the above"],
     "liberalising international trade"),

    (3,
     "Accounting separation enables regulators to examine whether a dominant operator "
     "is favouring its own retail business over its competitors.",
     ["TRUE", "FALSE"],
     "TRUE"),

    (4,
     "The following are instruments of regulation EXCEPT",
     ["regulations", "resolutions", "decisions", "policies", "None of the above"],
     "None of the above"),

    (5,
     "The availability of affordable communications services for all citizens on a "
     "personal basis is ______.",
     ["Universal Access", "Universal Achievement", "Universal Assess",
      "Universal Service", "None of the above"],
     "Universal Service"),

    (6,
     "A license which sets out identical terms of operation for all businesses "
     "operating in a particular market segment can be referred to as "
     "(I) individual operator  (II) class license  (III) general authorisation",
     ["I or II", "I or III", "II or III", "I, II or III", "None of the above"],
     "II or III"),

    (7,
     "The principles of good regulatory decision-making include all of the following "
     "EXCEPT",
     ["Transparency", "Objectivism", "Professionalism",
      "All of the above", "None of the above"],
     "None of the above"),

    (8,
     "Which of the following is/are true about individuals in the Bottom of the "
     "Pyramid markets?  (I) They are unable to spend significant sums of money.  "
     "(II) They have often been considered commercially unviable by large companies.",
     ["I only", "II only", "Both I and II", "None of the above"],
     "Both I and II"),

    (9,
     "What type of rules are vulnerable to becoming dated or inappropriate in a "
     "fast-moving high technology industry?",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-ante"),

    (10,
     "Which of these sectors helps spread equitable, sustainable and affordable "
     "access to information and communication technologies (ICT)?",
     ["ITU-R", "ITU-T", "ITU-D", "ITU-S", "None of the above"],
     "ITU-D"),

    (11,
     "Which of the following is not one of the grounds on which a regulator's "
     "decision may be appealed?",
     ["law", "procedure", "logic", "authority", "None of the above"],
     "authority"),

    (13,
     "[stem reconstructed] The body responsible for the technical and economic "
     "regulation of the telecommunication sector (as distinct from policy-making) is",
     ["The ministry in charge of the telecommunication sector",
      "The national telecommunication regulator",
      "Mobile network operators",
      "The courts of law",
      "The police"],
     "The national telecommunication regulator"),

    (14,
     "The mission of the UN specialized agency responsible for issues concerning "
     "information and communication technologies includes all of the following EXCEPT",
     ["coordinating the shared global use of the radio spectrum",
      "promoting international cooperation in assigning satellite orbits",
      "working to improve telecommunication infrastructure in the developing world",
      "assisting in the development of technical standards",
      "None of the above"],
     "None of the above"),

    (15,
     "Which of the following is FALSE about an industry with one monopoly firm?",
     ["Higher prices are experienced",
      "Supply is low",
      "Production is inefficient",
      "Inferior goods are produced",
      "None of the above"],
     "Inferior goods are produced"),

    (16,
     "The area within the Access Model which captures population and geographical "
     "areas which are still unserved, but in which services would be profitable, is "
     "referred to as the",
     ["True Access Gap", "Current Network Reach and Access", "Smart Subsidy Zone",
      "Market Efficiency Gap", "None of the above"],
     "Market Efficiency Gap"),

    (17,
     "By concentrating action on proven grievances rather than on compliance with "
     "finely detailed rules, ______ regulation is potentially efficient.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post"),

    (18,
     "The area within the Access Model in which services cannot be provided "
     "profitably is referred to as",
     ["True Access Gap", "Current Network Reach and Access", "Smart Subsidy Zone",
      "Market Efficiency Gap", "None of the above"],
     "True Access Gap"),

    (19,
     "All the following are basic forms of regulation, EXCEPT",
     ["Technical standardisation", "Public policy regulation", "Competition regulation",
      "Consumer protection regulation", "None of the above"],
     "Consumer protection regulation"),

    (22,
     "[stem reconstructed] Which of these sectors manages the international "
     "radio-frequency spectrum and satellite orbit resources?",
     ["ITU-R", "ITU-T", "ITU-D", "ITU-S", "None of the above"],
     "ITU-R"),

    (23,
     "An increase in price will cause a supply curve to shift to the left.",
     ["TRUE", "FALSE"],
     "FALSE"),

    (24,
     "Licences may be issued to achieve all of the following objectives EXCEPT",
     ["To regulate the provision of an essential public service",
      "To encourage privatization",
      "To allocate scarce resources",
      "To generate revenue for government",
      "None of the above"],
     "None of the above"),

    (25,
     "Supply is the quantity of a good sellers wish to sell each time the market opens.",
     ["TRUE", "FALSE"],
     "FALSE"),

    (26,
     "The role of regulators changes as markets become more competitive.",
     ["TRUE", "FALSE"],
     "TRUE"),

    (27,
     "What type of rule is referred to as 'common sense' regulation?",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post"),

    (28,
     "Which of the following types of licences simplify regulation?",
     ["Individual operator licences", "Class licences", "Intermediate licences",
      "Consultative licences", "None of the above"],
     "Class licences"),

    (29,
     "The specialized agency of the United Nations (UN) responsible for issues that "
     "concern information and communication technologies is",
     ["International Telecommunications Union",
      "International Telecommunication Union",
      "Institute of Electrical and Electronics Engineers",
      "Institute of Electrical and Electronic Engineers",
      "World Trade Organization"],
     "International Telecommunication Union"),

    (30,
     "Which of these sectors standardizes global telecommunications (except for radio)?",
     ["ITU-R", "ITU-T", "ITU-D", "ITU-S", "None of the above"],
     "ITU-T"),

    (34,
     "[stem reconstructed] The gap between those who have access to modern "
     "information and communication technologies and those who do not is referred to "
     "as the ______.",
     ["digital divide", "digital dividend", "white space", "spectral efficiency",
      "None of the above"],
     "digital divide"),

    (35,
     "Which one of the following does NOT occur in perfect competition?",
     ["There are many buyers.",
      "Firms and buyers are completely informed about the prices of the products of "
      "each firm in the industry.",
      "There are significant restrictions on entry into the industry.",
      "Firms already in the industry have no advantage over potential new entrants.",
      "No single firm can exert a significant influence on the price of the good."],
     "There are significant restrictions on entry into the industry."),

    (36,
     "What type of rule is being applied if a regulator states, 'You must not indulge "
     "in anti-competitive practice', but determines whether a breach has taken place "
     "after the event?",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post"),

    (37,
     "Two linear equations A and B represent two supply curves. A has a slope of 2 "
     "while B has a slope of 3. Which of the two equations represent a more elastic "
     "supply?",
     ["A", "B", "All of the above", "None of the above", "Cannot be determined"],
     "A"),

    (38,
     "All of the following are universal access policy objectives EXCEPT",
     ["To permit full participation in 21st Century society",
      "To promote national political, economic and cultural cohesion",
      "To allocate scarce resources",
      "To promote economic development",
      "None of the above"],
     "To allocate scarce resources"),

    (39,
     "Which of the following refers to the radio spectrum released in the process of "
     "digital television transition?",
     ["digital divide", "digital dividend", "white space", "spectral efficiency",
      "None of the above"],
     "digital dividend"),

    (40,
     "In industries with ______, market forces are allowed to work with no external "
     "intervention.",
     ["co-regulation", "zero regulation", "formal regulation", "self-regulation",
      "None of the above"],
     "zero regulation"),

    (41,
     "The availability of affordable communications services for all citizens within "
     "the community in which they live but not necessarily on an individual basis is "
     "______.",
     ["Universal Access", "Universal Achievement", "Universal Assess",
      "Universal Service", "None of the above"],
     "Universal Access"),

    (42,
     "The principle ______ ensures that no person can judge a case in which they have "
     "an interest.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "nemo judex in sua causa debet esse"),

    (43,
     "Which of these types of economies is vulnerable to managerial corruption?",
     ["Traditional", "Command", "Market", "All of the above", "None of the above"],
     "Command"),

    (44,
     "Price ceilings are imposed to increase price above the free market equilibrium "
     "price.",
     ["TRUE", "FALSE"],
     "FALSE"),

    (45,
     "The maxim 'hear the other side' is expressed in Latin as",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "Audi alteram partem"),

    (46,
     "Perfect competition occurs in a market where there are many firms each selling",
     ["a unique product", "a capital intensive product", "a similar product",
      "an identical product", "a competitive product"],
     "an identical product"),

    (47,
     "If a price increase of good A increases the quantity demanded of good B, then "
     "good B is a",
     ["substitute good", "complementary good", "inferior good", "normal good"],
     "substitute good"),

    (48,
     "Which form of regulation establishes a common and legally enforceable platform "
     "for all businesses within a sector?",
     ["Competition regulation", "Public policy regulation", "Business regulation",
      "Technical standardisation", "Business standardisation"],
     "Technical standardisation"),

    (49,
     "In a de-regulated industry, market forces are allowed to work with no external "
     "intervention.",
     ["TRUE", "FALSE"],
     "TRUE"),

    (50,
     "______ regulation states, in advance, a rule that a company must obey.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-ante"),

    (51,
     "Which type of regulation is vulnerable to role ambiguity among the different "
     "actors in an industry?",
     ["co-regulation", "zero regulation", "formal regulation", "self-regulation",
      "None of the above"],
     "co-regulation"),

    (52,
     "Which of the following types of licences are used primarily where there is "
     "likely to be market dominance?",
     ["Individual operator licences", "Class licences", "Intermediate licences",
      "Consultative licences", "None of the above"],
     "Individual operator licences"),

    (53,
     "Which of the following best describe(s) guidelines?  (I) They are informal "
     "documents.  (II) They are drafted in legal language.",
     ["I only", "II only", "Both I and II", "None of the above"],
     "I only"),

    (54,
     "Characteristics of ______ include the removal of exclusive rights from monopoly "
     "firms and award of licences for all new services on a competitive basis.",
     ["regulation", "privatization", "liberalization", "de-regulation", "reformation"],
     "liberalization"),

    (55,
     "______ refers to the intervention by governments in those markets in order to "
     "achieve certain outcomes.",
     ["regulation", "privatization", "liberalization", "de-regulation", "policy"],
     "regulation"),

    (56,
     "A market can accurately be described as",
     ["a place to buy things",
      "a place to sell things",
      "the process by which prices adjust to reconcile the allocation of resources",
      "a place where buyers and sellers meet"],
     "a place where buyers and sellers meet"),

    (57,
     "The area within the Access Model which captures high population density and "
     "higher-income citizens which have historically been well served is referred to "
     "as the",
     ["True Access Gap", "Current Network Reach and Access", "Smart Subsidy Zone",
      "Market Efficiency Gap", "None of the above"],
     "Current Network Reach and Access"),

    (58,
     "______ regulation gives regulation its power to react reasonably in unforeseen "
     "circumstances.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post"),

    (59,
     "In the mixed economy",
     ["economic problems are solved by the government and market",
      "economic decisions are made by the private sector and free market",
      "economic allocation is achieved by the 'invisible hand'",
      "economic questions are solved by government departments"],
     "economic problems are solved by the government and market"),

    (60,
     "Which of the following is NOT a widely accepted regulatory objective in the "
     "telecommunication sector?",
     ["Foster competitive markets to promote local entrepreneurial initiative",
      "Protect consumer rights, including privacy rights",
      "Promote universal access to basic telecommunications services",
      "Optimize use of scarce resources",
      "Create a favourable climate to promote investment to expand telecommunications "
      "networks"],
     "Foster competitive markets to promote local entrepreneurial initiative"),
]

OUTPUT_FILE = "compiled.json"

# Per-question "insight" shown behind the lamp icon on the site (and in the PDF).
# Grounded in the lecture decks in ../policy/ wherever the concept appears there;
# a few (access-gap model, BoP, digital divide/dividend, supply-slope elasticity,
# "common sense" regulation) are standard course material not stated verbatim in
# those three decks and are marked "inferred"/"standard" so they can be checked.
EXPLANATIONS = {
    1: "The decks name exactly two factors behind the state-monopoly era: Economic "
       "(very high network cost + low demand → natural monopoly) and Political "
       "(governments kept control, treating telecoms like the state post office). "
       "'Social' is not listed.",
    2: "The WTO 'regulates international trade', and its Basic Telecommunications "
       "Agreement opens telecom markets to competition and investment — i.e. it "
       "liberalises international (not domestic) trade.",
    3: "Accounting separation forces a vertically-integrated dominant operator to keep "
       "separate wholesale/retail accounts, so the regulator can see whether it is "
       "cross-subsidising or favouring its own retail arm over rivals. (Standard "
       "competition-safeguard concept.)",
    4: "The decks list regulations, decisions, policies AND resolutions all as "
       "regulatory instruments ('regulations, decisions, orders, decrees, rules, "
       "policies, notices, resolutions'). Every option is an instrument, so none is "
       "the exception.",
    5: "Universal Service = availability on an individual/personal (household) basis; "
       "Universal Access = a shared/community basis. 'Personal basis' → Universal "
       "Service. (Compare Q41.)",
    6: "A class licence / general authorisation 'sets out identical terms of operation "
       "for all businesses operating in a particular market segment', so both II and "
       "III describe it.",
    7: "The principles of good regulatory decision-making listed are Transparency, "
       "Objectivity, Professionalism, Efficiency and Independence — so all three "
       "options are genuine principles and none is the exception.",
    8: "Bottom-of-the-Pyramid individuals have low individual purchasing power (can't "
       "spend large sums each) AND were historically judged commercially unviable by "
       "big firms — yet collectively form a huge market. Both statements are true. "
       "(Standard BoP concept.)",
    9: "Ex-ante rules are fixed in advance, so in a fast-moving high-tech industry they "
       "quickly become dated or inappropriate. (ex ante = 'before certain issues "
       "arise'.)",
    10: "ITU-D (Development) 'helps spread equitable, sustainable and affordable access "
        "to information and communication technologies (ICT).'",
    11: "The deck lists the grounds of appeal as law (illegality), procedure "
        "(misadministration), logic (irrationality) and the substance of the action. "
        "'Authority' is NOT among them, so it is the odd one out. Note: 'logic' IS a "
        "valid ground.",
    13: "Policy-making is the ministry's job; the technocratic, day-to-day regulation "
        "of the sector is done by the independent national regulator (the decks stress "
        "the regulator should be separate from the ministry). NB: this stem was cut off "
        "in the photo — if it actually asked about policy-making, the answer would "
        "be the ministry.",
    14: "The deck gives the ITU mission as exactly these four: shared use of the radio "
        "spectrum, satellite-orbit assignment, telecom infrastructure in the developing "
        "world, and worldwide technical standards. All four are included, so none is the "
        "exception.",
    15: "The deck says a monopoly causes exactly three harms: lower output (low supply), "
        "higher price, and less-efficient/higher-cost production. 'Inferior goods are "
        "produced' is not one of them — so it is the false statement.",
    16: "In the access-gap model the Market Efficiency Gap is the area that is "
        "commercially viable (would be profitable) but not yet served — closeable "
        "by market reforms rather than subsidy.",
    17: "Ex-post regulation acts on proven grievances after the fact instead of via "
        "finely detailed pre-set rules; the deck notes 'intrusion can be lessened by "
        "the use of ex-post rules.'",
    18: "The True Access Gap is the area where service cannot be provided profitably at "
        "all — it needs subsidy / universal-access funding, unlike the Market "
        "Efficiency Gap.",
    19: "Regulation takes three basic forms: technical standardisation, public policy "
        "regulation and competition regulation. Consumer-protection regulation is not "
        "one of these three, so it is the exception.",
    22: "ITU-R (Radiocommunication) 'manages the international radio-frequency spectrum "
        "and satellite orbit resources.' (Stem was cut off in the photo, but the options "
        "fix it.)",
    23: "A price change causes a movement ALONG the supply curve, not a shift. The curve "
        "only shifts when input prices, technology, expectations or the number of sellers "
        "change — so this is FALSE.",
    24: "Every option is a listed licensing objective — provision of an essential "
        "public service, privatization/commercialization, allocation of scarce resources, "
        "and generating government revenue. So none is the exception.",
    25: "FALSE. Supply is the whole price–quantity relationship (the supply schedule / "
        "curve), not a single fixed amount. The deck calls the amount sellers will sell "
        "at a given price the 'quantity supplied'; describing supply as one quantity "
        "'each time the market opens' is inaccurate. (The 2018 mid-sem answer key marks "
        "this FALSE.)",
    26: "TRUE — as competition develops the regulator's role shifts (lighter-touch / "
        "more ex-post competition oversight); a regulator picks among zero/self/co/formal "
        "styles by what is appropriate.",
    27: "Inferred: 'common-sense' regulation best fits ex-post — general principles "
        "applied with judgment after the fact, rather than detailed rules set in advance. "
        "NB: the phrase is not used verbatim in the provided decks, so confirm with your "
        "lecturer.",
    28: "Class licences (general authorisations) 'simplify regulation, help ensure a "
        "level playing field, and are more flexible' — the deck's exact wording.",
    29: "The UN's ICT agency is the International Telecommunication Union (ITU) — the "
        "official name uses the singular 'Telecommunication' (option a's plural "
        "'Telecommunications' is the trap).",
    30: "ITU-T (Standardization) 'standardizes global telecommunications (except for "
        "radio)'; radio is ITU-R's job.",
    34: "Inferred (standard): the digital divide is the gap between those who have access "
        "to modern ICT and those who do not. (Stem was cut off in the photo.) Don't "
        "confuse it with the digital dividend (Q39).",
    35: "Perfect competition has free entry, so 'significant restrictions on entry' does "
        "NOT occur. The other options (many buyers, perfect information, no incumbent "
        "advantage, price-taking) all do occur.",
    36: "Determining whether a breach occurred AFTER the event is ex-post regulation "
        "(ex post = 'after some issues have already occurred').",
    37: "Under the usual convention a flatter supply curve (smaller slope in the "
        "price–quantity plane) is more elastic, so A (slope 2) is taken as more "
        "elastic than B (slope 3). NB: strictly, slope alone doesn't fix supply "
        "elasticity (it also depends on the intercept / reference price), so verify the "
        "intended answer.",
    38: "Allocating scarce resources (spectrum, numbers, rights of way) is a "
        "licensing/regulatory objective, not a universal-access objective — so it "
        "is the exception here.",
    39: "The digital dividend is the spectrum freed up when broadcasting switches from "
        "analogue to digital TV. (Contrast the digital divide, Q34.)",
    40: "The deck's exact sentence: 'In industries with zero regulation (no regulation), "
        "market forces are allowed to work with no external intervention.'",
    41: "Universal Access = availability on a shared/community basis (not necessarily to "
        "each individual). 'Within the community … not necessarily on an individual "
        "basis' → Universal Access. (Compare Q5.)",
    42: "'No one should be a judge in their own cause' is the maxim nemo judex in sua "
        "causa debet esse — the rule against bias ('justice must be seen to be "
        "done').",
    43: "The deck: the command economy 'fails because of … vulnerability to "
        "managerial corruption' (and the intractable complexity of central control).",
    44: "A price ceiling holds the price BELOW equilibrium (a maximum price); it is a "
        "price FLOOR that keeps price above equilibrium. So the statement is FALSE.",
    45: "'Hear the other side' is the maxim audi alteram partem — the fair-hearing "
        "rule.",
    46: "Perfect competition requires that 'the goods offered for sale are all exactly "
        "the same' — i.e. an identical (homogeneous) product.",
    47: "If A's price rises and B's quantity demanded rises, buyers are switching from A "
        "to B — they are substitutes (positive cross-price relationship).",
    48: "Technical standardisation 'establishes a common and legally enforceable platform "
        "for all businesses within a sector' — the deck's exact definition.",
    49: "The deck equates the terms: 'industries with zero regulation … are also "
        "said to be completely deregulated (i.e. regulation has been completely "
        "removed),' with market forces working with no external intervention. So this "
        "reads as TRUE. (The exam sheet circled FALSE — treat with care and "
        "confirm.)",
    50: "A rule stated in advance that a company must obey is ex-ante regulation "
        "(ex ante = 'before certain issues arise').",
    51: "The deck: 'co-regulation is vulnerable to role ambiguity and the differing "
        "player perceptions of what the others will do.'",
    52: "Individual operator licences are used 'primarily where … there is likely "
        "to be market dominance' (also limited licences / specific spectrum) — the "
        "deck's exact wording.",
    53: "'Guidelines are informal documents that do not … possess a legal status' "
        "and are 'usually presented in user-friendly language'. So (I) is true and (II) "
        "is false — legal language is used for determinations/consents, not "
        "guidelines.",
    54: "Liberalization = 'the removal of exclusive rights from the former monopoly … "
        "and the award of licences for all new services on a competitive basis' — "
        "the deck's exact description.",
    55: "Regulation 'refers to the intervention by governments in markets in order to "
        "achieve certain outcomes' — the deck's exact definition.",
    56: "The deck defines a market as 'a group of buyers and sellers of a particular "
        "good or service' — i.e. where buyers and sellers meet. (The 2018 mid-sem "
        "answer key marks (d) 'a place where buyers and sellers meet'.)",
    57: "'Current Network Reach and Access' is the already-well-served area (high "
        "density, higher income) that the market has already reached.",
    58: "Reacting reasonably to unforeseen circumstances is ex-post regulation — you "
        "respond after events occur, unlike fixed ex-ante rules.",
    59: "A mixed economy blends command and market: 'Command measures, blended with "
        "market economies, create the mixed economies,' with governments intervening to "
        "correct market failure.",
    60: "The deck's widely-accepted objectives foster competitive markets to promote "
        "efficient supply, quality, advanced services and efficient prices — NOT "
        "'local entrepreneurial initiative'. The other four options are listed objectives "
        "verbatim, so (a) is the odd one out.",
}


def main():
    records = []
    for exam_no, q_text, options, correct in QUESTIONS:
        assert correct in options, f"correct answer not in options for Q{exam_no}"
        assert len(options) == len(set(options)), f"duplicate options in Q{exam_no}"
        assert exam_no in EXPLANATIONS, f"missing explanation for Q{exam_no}"
        records.append({
            "question_number": exam_no,
            "question_text": q_text,
            "options": options,
            "correct_answer": [correct],
            "explanation": EXPLANATIONS[exam_no],
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)
    print(f"Wrote {OUTPUT_FILE}: {len(records)} questions")

    # sanity summary
    nums = [r["question_number"] for r in records]
    missing = [n for n in range(1, 61) if n not in nums]
    print(f"Exam numbers covered: {len(nums)} of 60")
    print(f"Not captured (omitted): {missing}")


if __name__ == "__main__":
    main()
