#!/usr/bin/env python3
"""
Build "Set 2" for the Policy & Regulation practice site: 50 ADDITIONAL questions.

Unlike Set 1 (build_questions.py), which is a verbatim transcription of the past
paper, Set 2 is newly authored to match the style and patterns of that paper
(fill-in-the-blank, TRUE/FALSE, "EXCEPT", "which is NOT", Roman-numeral combos,
the ex-ante/ex-post/Latin-maxim family, and "None/All of the above" options).

Every question and its insight is grounded in the course lecture decks in
../policy/:
  - TE 452 - 1&2 (economics of markets; reforms; regulatory overview; ITU/WTO)
  - TE 462 - Framework for Regulation (styles of regulation; instruments; appeal)
  - TE 462 - Licensing Telecommunication Services (licence types & objectives)

Output JSON matches the site format, including the "explanation" (lamp) field.
Options are written in a natural order; the website reshuffles option display
order per question at run time.

Entry: (number, question_text, [options], correct_answer, explanation)
"""
import json

QUESTIONS = [
    # ---------------- The economics of markets (TE 452) ----------------
    (1,
     "According to the Law of Demand, other things being equal, when the price of a "
     "good rises, the quantity demanded of that good",
     ["rises", "falls", "stays exactly the same", "rises then falls",
      "None of the above"],
     "falls",
     "Law of Demand: 'when the price of a good rises, the quantity demanded of the "
     "good falls, and when the price falls, the quantity demanded rises.'"),

    (2,
     "Which of the following would shift the demand curve rather than cause a movement "
     "along it?",
     ["a change in the good's own price", "a change in consumers' income",
      "a change in the quantity supplied", "a change in the equilibrium quantity",
      "None of the above"],
     "a change in consumers' income",
     "The deck lists demand-curve shifters as income, prices of related goods, taste, "
     "expectations and the number of buyers. A change in the good's own price is a "
     "movement along the curve, not a shift."),

    (3,
     "According to the Law of Supply, when the price of a good rises, the quantity "
     "supplied of the good also rises.",
     ["TRUE", "FALSE"],
     "TRUE",
     "Law of Supply: 'when the price of a good rises, the quantity supplied of the "
     "good also rises, and when the price falls, the quantity supplied falls as well.'"),

    (4,
     "All of the following can shift the supply curve EXCEPT",
     ["input prices", "technology", "the price of the good itself",
      "the number of sellers", "expectations"],
     "the price of the good itself",
     "Supply-curve shifters are input prices, technology, expectations and the number "
     "of sellers. A change in the good's own price is a movement along the supply "
     "curve, not a shift."),

    (5,
     "The single point at which the supply and demand curves intersect gives the",
     ["ceiling price", "equilibrium price", "floor price", "reservation price",
      "None of the above"],
     "equilibrium price",
     "'Equilibrium is the one point at which the supply and demand curves intersect. "
     "The price at this intersection is called the equilibrium price.'"),

    (6,
     "A government intervention that keeps a price below its market equilibrium is "
     "called a price",
     ["floor", "ceiling", "band", "peg", "None of the above"],
     "ceiling",
     "'Prices below the market equilibrium … such policy interventions are called "
     "price ceilings, because they prevent the price from rising as high as it may "
     "have gone.'"),

    (7,
     "A price floor is a government control that keeps the price ______ its market "
     "equilibrium value.",
     ["below", "above", "equal to", "independent of", "None of the above"],
     "above",
     "'The opposite [of a ceiling] is a price floor, by which the government keeps the "
     "price above its market equilibrium value.'"),

    (8,
     "______ refers to how the burden of a tax is distributed among the various people "
     "who make up the economy.",
     ["Tax incidence", "Tax elasticity", "Tax equilibrium", "Tax neutrality",
      "None of the above"],
     "Tax incidence",
     "'Tax incidence refers to how the burden of a tax is distributed among the "
     "various people who make up the economy.'"),

    (9,
     "In a ______ economy, a powerful agent (usually the government) determines what "
     "people will produce, earn and consume.",
     ["traditional", "command", "market", "mixed", "None of the above"],
     "command",
     "'In a command economy a powerful agent (usually the government) determines what "
     "people will produce, earn and consume.'"),

    (10,
     "Which type of economy is typical of tribal societies, where economic affairs "
     "follow a customary pattern and local leaders have the final say on allocation?",
     ["Market", "Command", "Traditional", "Mixed", "None of the above"],
     "Traditional",
     "'Traditional economies are typical of tribal societies … economic affairs "
     "follow a customary pattern … local leaders have the ultimate say in matters of "
     "allocation.'"),

    (11,
     "Twentieth-century experience shows the command economy fails because of "
     "(I) the intractable complexity of the control task  (II) vulnerability to "
     "managerial corruption.",
     ["I only", "II only", "Both I and II", "Neither I nor II"],
     "Both I and II",
     "The deck gives both: the command economy 'fails because of the intractable "
     "complexity of the control task [and] vulnerability to managerial corruption.'"),

    (12,
     "For a market to be perfectly competitive, the goods offered for sale must be",
     ["branded and differentiated", "all exactly the same", "of varying quality",
      "protected by patents", "None of the above"],
     "all exactly the same",
     "Under perfect competition 'the goods offered for sale are all exactly the same', "
     "and no single buyer or seller has any influence over the market price."),

    # ---------------- Monopoly & sector reforms (TE 452) ----------------
    (13,
     "A firm that has no competitors in its industry is called a",
     ["monopsony", "monopoly", "oligopoly", "cartel", "None of the above"],
     "monopoly",
     "'A firm that has no competitors in its industry is called a monopoly.'"),

    (14,
     "A ______ monopoly exists when a single firm can supply a good to an entire "
     "market at a lower cost than could two or more firms.",
     ["legal", "natural", "temporary", "statutory", "None of the above"],
     "natural",
     "'An industry is a natural monopoly when a single firm can supply a good or "
     "service to an entire market at a lower cost than could two or more.'"),

    (15,
     "Which of the following is cited as an example of a natural monopoly?",
     ["water supply", "power distribution", "telecommunications", "All of the above",
      "None of the above"],
     "All of the above",
     "'Examples of natural monopolies include water supply, power distribution, "
     "telecommunications.'"),

    (16,
     "Governments deliberately create monopolies by issuing ______, which give "
     "inventors the right to sell and market their inventions.",
     ["licences", "patents", "subsidies", "tariffs", "None of the above"],
     "patents",
     "'Governments issue patents, which give monopoly rights to inventors to sell and "
     "market their inventions.'"),

    (17,
     "The process of transition from a monopoly market to a competitive one is called",
     ["privatization", "liberalization", "standardization", "commercialization",
      "None of the above"],
     "liberalization",
     "'Liberalization … represents the process of transition from a monopoly market "
     "to a competitive one.'"),

    (18,
     "The transfer of ownership of a business from the state to the private sector is "
     "called",
     ["liberalization", "privatization", "regulation", "nationalization",
      "None of the above"],
     "privatization",
     "'Privatization … is the transfer of ownership of a business from the state to "
     "the private sector.'"),

    (19,
     "The former monopoly fixed-network operator, from which exclusive rights are "
     "removed during liberalization, is usually called the",
     ["incumbent", "entrant", "licensee", "regulator", "None of the above"],
     "incumbent",
     "Liberalization means 'the removal of exclusive rights … from the former "
     "monopoly fixed network operator, which is often called the incumbent.'"),

    (20,
     "Before the 1980s, telecommunications services were provided mainly by",
     ["private start-ups", "state-owned monopolies", "foreign investors",
      "competitive markets", "None of the above"],
     "state-owned monopolies",
     "'The Telecommunication Sector before the 1980s: Telecoms services were provided "
     "by state-owned monopolies.'"),

    # ---------------- Regulatory overview (TE 452) ----------------
    (21,
     "The principal focus of contemporary regulation of the telecommunications "
     "services industry is the creation, nourishment and maintenance of",
     ["state monopolies", "competitive markets", "fixed retail prices",
      "universal ownership", "None of the above"],
     "competitive markets",
     "'The principal focus for contemporary regulation of the telecommunications "
     "services industry is the creation, nourishment and maintenance of competitive "
     "markets.'"),

    (22,
     "Which basic form of regulation seeks to create and maintain fair competitive "
     "relationships between businesses, and between businesses and consumers?",
     ["Technical standardization", "Public policy regulation", "Competition regulation",
      "Self-regulation", "None of the above"],
     "Competition regulation",
     "'Competition regulation … seeks to create and maintain fair competitive "
     "relationships between businesses, and between businesses and consumers.'"),

    (23,
     "Public policy regulation seeks to achieve objectives because they are believed "
     "to be in the",
     ["interest of operators", "public interest", "regulator's interest",
      "global interest", "None of the above"],
     "public interest",
     "'Public policy regulation … seeks to achieve objectives because they are "
     "believed to be in the public interest.'"),

    (24,
     "Policy-making is primarily a matter of ______ decision-making, whereas "
     "regulation is much more technocratic.",
     ["technical", "political", "judicial", "commercial", "None of the above"],
     "political",
     "'Whereas policy making is primarily a matter of political decision making, "
     "regulation is much more technocratic.'"),

    (25,
     "Which of the following is NOT listed among the principles of good regulatory "
     "decision-making?",
     ["Transparency", "Objectivity", "Secrecy", "Efficiency", "Independence"],
     "Secrecy",
     "The principles listed are Transparency, Objectivity, Professionalism, Efficiency "
     "and Independence. Secrecy is not among them — transparency is its opposite."),

    (26,
     "The two 'fundamental rules' of procedural fairness noted in the deck are audi "
     "alteram partem and",
     ["nemo judex in sua causa debet esse", "res ipsa loquitur", "caveat emptor",
      "pacta sunt servanda", "None of the above"],
     "nemo judex in sua causa debet esse",
     "The two fundamental rules are audi alteram partem ('hear the other side') and "
     "'do not be a judge in your own case' — nemo judex in sua causa debet esse."),

    (27,
     "The main instruments of regulation include authorizations, rules, "
     "determinations, consents and",
     ["guidelines", "statutes", "patents", "tariffs", "None of the above"],
     "guidelines",
     "'The main instruments of regulation include authorizations, rules, "
     "determinations, consents and guidelines.'"),

    # ---------------- International agencies (TE 452) ----------------
    (28,
     "Which international organization regulates international trade and issued the "
     "Reference Paper on Regulation?",
     ["ITU", "WTO", "ATU", "WATRA", "None of the above"],
     "WTO",
     "'The World Trade Organization (WTO) is an inter-governmental organization which "
     "regulates international trade,' and its agreement includes a Reference Paper on "
     "Regulation."),

    (29,
     "Adherence to how many basic principles does the WTO Reference Paper on "
     "Regulation require?",
     ["three", "four", "six", "ten", "None of the above"],
     "six",
     "'They require adherence to six basic principles' — e.g. an independent "
     "regulator, anti-competitive safeguards, transparent licensing, interconnection, "
     "neutral universal-access obligations, and fair allocation of scarce resources."),

    (30,
     "The WTO Reference Paper says a telecoms regulator should be independent of "
     "operating companies, but not necessarily of",
     ["governments", "consumers", "the ITU", "the courts", "None of the above"],
     "governments",
     "'Telecoms regulators should be independent of operating companies (but not "
     "necessarily of governments).'"),

    (31,
     "The International Telecommunication Union (ITU) is a specialized agency of the",
     ["European Union", "United Nations", "African Union", "World Bank",
      "None of the above"],
     "United Nations",
     "'ITU is a specialized agency of the United Nations (UN) responsible for issues "
     "that concern information and communication technologies.'"),

    (32,
     "Which of the following is NOT one of the three sectors of the ITU?",
     ["ITU-R", "ITU-T", "ITU-D", "ITU-S", "None of the above"],
     "ITU-S",
     "The ITU has three sectors: Radiocommunication (ITU-R), Standardization (ITU-T) "
     "and Development (ITU-D). There is no 'ITU-S'."),

    (33,
     "Which body is the West African Telecommunications Regulators Association?",
     ["ATU", "WATRA", "ECOWAS", "ITU-D", "None of the above"],
     "WATRA",
     "The deck lists international bodies including the 'West African "
     "Telecommunications Regulators Association (WATRA)'."),

    # ---------------- Styles of regulation & intrusion (TE 462) ----------------
    (34,
     "Which regulatory style is the LEAST intrusive?",
     ["Formal regulation", "Co-regulation", "Self-regulation", "Zero regulation",
      "None of the above"],
     "Zero regulation",
     "In increasing order of intrusiveness the styles are zero regulation, "
     "self-regulation, co-regulation, then formal (external) regulation — so zero "
     "regulation is least intrusive."),

    (35,
     "Which regulatory style is the MOST intrusive (most severe)?",
     ["Zero regulation", "Self-regulation", "Co-regulation", "Formal regulation",
      "None of the above"],
     "Formal regulation",
     "The order of increasing severity is zero → self → co → formal regulation, so "
     "formal (external) regulation is the most intrusive."),

    (36,
     "Pure ______ applies when the players in an industry regulate themselves.",
     ["co-regulation", "self-regulation", "zero regulation", "formal regulation",
      "None of the above"],
     "self-regulation",
     "'Pure self-regulation applies when the players in an industry regulate "
     "themselves.'"),

    (37,
     "Which of the following is given as a benefit of self-regulation?",
     ["companies usually know their businesses better than an external regulator",
      "it shifts regulatory costs onto taxpayers",
      "it works best when commercial conflicts are strong",
      "it removes the industry's need for a watchdog",
      "None of the above"],
     "companies usually know their businesses better than an external regulator",
     "Benefits listed include that 'companies usually know their businesses better "
     "than an external regulator', and that internalizing regulation minimizes the "
     "costs ultimately borne by industry and consumers."),

    (38,
     "Self-regulation is most effective when there is",
     ["strong commercial conflict between players",
      "high convergence of interest between stakeholders",
      "an absence of any shared interest", "frequent litigation",
      "None of the above"],
     "high convergence of interest between stakeholders",
     "Self-regulation is 'most effective when there is high convergence of interest "
     "between stakeholders [and] least effective when there are strong commercial "
     "conflicts.'"),

    (39,
     "Which style is a hybrid in which the regulator joins the industry players in a "
     "joint forum instead of regulating purely from outside?",
     ["Zero regulation", "Self-regulation", "Co-regulation", "Formal regulation",
      "None of the above"],
     "Co-regulation",
     "'Co-regulation is a hybrid option … [where] the regulator joins the industry "
     "players to work with them, as a participant in a joint forum.'"),

    (40,
     "Co-regulation blends together which two styles of regulation?",
     ["zero and formal regulation", "formal and self-regulation",
      "self and zero regulation", "traditional and command regulation",
      "None of the above"],
     "formal and self-regulation",
     "'Co-regulation … blends formal and self-regulation together.'"),

    (41,
     "Intrusion can be lessened by using ex-post rules and by regulating ______ "
     "instead of individual prices.",
     ["price floors", "price baskets", "retail tariffs", "spectrum fees",
      "None of the above"],
     "price baskets",
     "'Intrusion can be lessened by the use of ex-post rules and by regulating price "
     "baskets instead of individual prices.'"),

    (42,
     "Good regulation should be ______ rather than intrusive, allowing operators to "
     "manage their own affairs within the spirit of the regulation.",
     ["minimal", "pervasive", "invisible", "punitive", "None of the above"],
     "pervasive",
     "'Regulation should be pervasive rather than intrusive, to allow operators to "
     "manage their affairs, as they know best but within the spirit of the "
     "regulation.'"),

    # ---------------- Instruments, process & appeal (TE 462) ----------------
    (43,
     "Fundamental to any system of regulation is a system of ______, where an "
     "undertaking needs permission to participate in a regulated market.",
     ["enforcement", "authorization", "consultation", "adjudication",
      "None of the above"],
     "authorization",
     "'Fundamental to any system of regulation is a system of authorization, where an "
     "undertaking needs permission to participate in a regulated market.'"),

    (44,
     "A ______ is a negative determination by which an authorized operator is formally "
     "relieved from the need to comply with a requirement.",
     ["guideline", "consent", "licence", "rule", "None of the above"],
     "consent",
     "'A consent is a negative determination by which an authorized operator is "
     "formally relieved from the need to comply with a requirement.'"),

    (45,
     "Because they have legal force, determinations and consents are drafted in ______ "
     "language.",
     ["user-friendly", "legal", "technical", "plain", "None of the above"],
     "legal",
     "'Because they have legal force, determinations and consents are drafted in legal "
     "language' — unlike guidelines, which are user-friendly."),

    (46,
     "All of the following are typical stages in a regulatory consultation EXCEPT",
     ["notification and invitations to contribute",
      "publication of consultation papers", "conduct of consultative meetings",
      "issue of a memorandum with the final instruments",
      "immediate revocation of an operator's licence"],
     "immediate revocation of an operator's licence",
     "Consultation stages are notification/invitations, publication of consultation "
     "papers, consultative meetings (with iteration), and a memorandum with the final "
     "legal instruments. Licence revocation is an enforcement action, not a "
     "consultation stage."),

    # ---------------- Licensing (TE 462) ----------------
    (47,
     "Companies pay for licences through upfront fees and ______ payments.",
     ["one-time", "annual", "hourly", "voluntary", "None of the above"],
     "annual",
     "'Companies pay fees for licenses, which may include both upfront fees, when a "
     "license is awarded, and annual payments.'"),

    (48,
     "A licence that does not tie an operator to a specific technology or service is "
     "described as a ______ licence.",
     ["class", "technology- and service-neutral", "provisional", "spectrum",
      "None of the above"],
     "technology- and service-neutral",
     "'Some regulators have … moved towards technology- and service-neutral "
     "licensing,' e.g. permitting a telephone service without specifying a fixed or "
     "wireless technology."),

    (49,
     "Licence conditions that establish a 'level playing field' and limit an "
     "incumbent's abuse of a dominant position are generally referred to as",
     ["universal service obligations", "anti-competitive safeguards", "spectrum caps",
      "interconnection charges", "None of the above"],
     "anti-competitive safeguards",
     "Such conditions 'are generally referred to in licenses as \"anti-competitive "
     "safeguards\" or \"fair trading conditions\".'"),

    (50,
     "Which of the following is NOT one of the finite (scarce) resources used in "
     "operating a telecommunications service?",
     ["radio spectrum", "telephone numbers", "rights of way", "customer goodwill",
      "None of the above"],
     "customer goodwill",
     "The finite/scarce resources listed are radio spectrum, numbers and rights of "
     "way. 'Customer goodwill' is not one of them."),
]

OUTPUT_FILE = "compiled_2.json"


def main():
    records = []
    seen = set()
    for num, q_text, options, correct, explanation in QUESTIONS:
        assert num not in seen, f"duplicate number {num}"
        seen.add(num)
        assert correct in options, f"correct answer not in options for Q{num}"
        assert len(options) == len(set(options)), f"duplicate options in Q{num}"
        assert explanation.strip(), f"missing explanation for Q{num}"
        records.append({
            "question_number": num,
            "question_text": q_text,
            "options": options,
            "correct_answer": [correct],
            "explanation": explanation,
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)
    print(f"Wrote {OUTPUT_FILE}: {len(records)} questions")


if __name__ == "__main__":
    main()
