#!/usr/bin/env python3
"""
Build "Set 3": the TE 462 Telecommunication Policy MID-SEMESTER exam
(Fourth Year, March 2018, setter K. A. Opare) — 40 shuffled MCQs.

Source: "new doc 2019-01-23 18.24.pdf" — a clean CamScanner scan of the paper
in which the intended answers are highlighted in yellow (a partial answer key;
some questions were left un-highlighted).

Like Set 1, this is a faithful TRANSCRIPTION (original (a)-(e) options preserved in
order; the site reshuffles display order). Correct answers were taken from the
paper's highlighted key where present, and otherwise determined from the course
lecture decks in ../policy/. Notably, the paper's key confirmed FALSE for the
"supply … each time the market opens" item and (d) for "a market can be described
as", which corrected two Set 1 answers; and it left the supply-elasticity,
"common sense" and de-regulated-industry items un-highlighted — the same three
this project had already flagged as genuinely uncertain.

Entry: (number, question_text, [options], correct_answer, explanation)
"""
import json

QUESTIONS = [
    (1,
     "WTO aims at",
     ["establishing rules for domestic trade", "restricting trade practices",
      "liberalising international trade", "encouraging entrepreneurs",
      "None of the above"],
     "liberalising international trade",
     "'The WTO … regulates international trade,' opening telecom markets to "
     "competition and investment — it liberalises international (not domestic) trade."),

    (2,
     "All the following are rules or guidelines contained in the WTO Reference Paper "
     "on Regulation EXCEPT",
     ["There should be a regulatory body independent of governments and operating "
      "companies",
      "Licensing criteria should be publicly available and transparent",
      "The regulator should allocate scarce resources fairly between operators",
      "Regulation should provide for interconnection between major operators",
      "None of the above"],
     "There should be a regulatory body independent of governments and operating "
     "companies",
     "The Reference Paper requires a regulator 'independent of operating companies "
     "(but not necessarily of governments)'. So requiring independence from governments "
     "as well overstates it — that option is the exception; (b), (c) and (d) are "
     "genuine Reference-Paper principles."),

    (3,
     "Characteristics of ______ include the removal of exclusive rights from monopoly "
     "firms and award of licences for all new services on a competitive basis.",
     ["regulation", "privatization", "liberalization", "de-regulation", "reformation"],
     "liberalization",
     "Liberalization = 'the removal of exclusive rights from the former monopoly … and "
     "the award of licences for all new services on a competitive basis.'"),

    (4,
     "In a de-regulated industry, market forces are allowed to work with no external "
     "intervention.",
     ["TRUE", "FALSE"],
     "TRUE",
     "The deck equates the terms: 'industries with zero regulation … are also said to "
     "be completely deregulated (i.e. regulation has been completely removed),' with no "
     "external intervention. (The mid-sem key left this un-highlighted, so confirm with "
     "your lecturer.)"),

    (5,
     "The process of transition from a monopoly market to a competitive one is referred "
     "to as ______.",
     ["regulation", "privatization", "liberalization", "de-regulation", "reformation"],
     "liberalization",
     "'Liberalization … represents the process of transition from a monopoly market to "
     "a competitive one.'"),

    (6,
     "Two linear equations A and B represent two supply curves. A has a slope of 2 "
     "while B has a slope of 3. Which of the two equations represent a more elastic "
     "supply?",
     ["A", "B", "All of the above", "None of the above", "Cannot be determined"],
     "A",
     "Under the usual convention a flatter supply curve (smaller slope in the "
     "price–quantity plane) is more elastic, so A (slope 2) is taken as more elastic "
     "than B. NB: slope alone doesn't strictly fix supply elasticity — the mid-sem key "
     "left this un-highlighted, so verify the intended answer."),

    (7,
     "The following are instruments of regulation EXCEPT",
     ["regulations", "resolutions", "decisions", "policies", "None of the above"],
     "None of the above",
     "The decks list regulations, decisions, policies AND resolutions all as regulatory "
     "instruments, so every option is an instrument and none is the exception."),

    (8,
     "______ refers to the intervention by governments in markets in order to achieve "
     "certain outcomes in those markets.",
     ["regulation", "privatization", "liberalization", "de-regulation", "policy"],
     "regulation",
     "'Regulation … refers to the intervention by governments in markets in order to "
     "achieve certain outcomes in those markets.'"),

    (9,
     "Supply is the quantity of a good sellers wish to sell each time the market opens.",
     ["TRUE", "FALSE"],
     "FALSE",
     "FALSE. Supply is the whole price–quantity relationship (the supply schedule / "
     "curve), not one fixed amount. The deck calls the amount sellers will sell at a "
     "given price the 'quantity supplied'. (Highlighted FALSE in the mid-sem key.)"),

    (10,
     "Which form of regulation establishes a common and legally enforceable platform "
     "for all businesses within a sector?",
     ["Competition regulation", "Public policy regulation", "Business regulation",
      "Technical standardisation", "Business standardisation"],
     "Technical standardisation",
     "'Technical standardisation … establishes a common and legally enforceable "
     "platform for all businesses within a sector.'"),

    (11,
     "A market can accurately be described as",
     ["a place to buy things", "a place to sell things",
      "the process by which prices adjust to reconcile the allocation of resources",
      "a place where buyers and sellers meet"],
     "a place where buyers and sellers meet",
     "The deck defines a market as 'a group of buyers and sellers of a particular good "
     "or service' — i.e. where buyers and sellers meet. (Highlighted (d) in the mid-sem "
     "key.)"),

    (12,
     "______ regulation states, in advance, a rule that a company must obey.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-ante",
     "A rule stated in advance that a company must obey is ex-ante regulation "
     "(ex ante = 'before certain issues arise')."),

    (13,
     "Which one of the following does NOT occur in perfect competition?",
     ["There are many buyers.",
      "Firms and buyers are completely informed about the prices of the products of "
      "each firm in the industry.",
      "There are significant restrictions on entry into the industry.",
      "Firms already in the industry have no advantage over potential new entrants.",
      "No single firm can exert a significant influence on the market price of the "
      "good."],
     "There are significant restrictions on entry into the industry.",
     "Perfect competition has free entry, so 'significant restrictions on entry' does "
     "NOT occur; the other options all do."),

    (14,
     "An increase in consumer income will increase demand for a/an ______ but decrease "
     "demand for a/an ______.",
     ["substitute good, inferior good", "normal good, inferior good",
      "inferior good, normal good", "normal good, complementary good"],
     "normal good, inferior good",
     "For a normal good, demand rises as income rises; for an inferior good, demand "
     "falls as income rises. So income up → more of a normal good, less of an inferior "
     "good."),

    (15,
     "The factors that encouraged the monopoly paradigm in the telecommunication "
     "sector can be categorized as",
     ["social, political and economic", "political and economic",
      "social and political", "social and economic", "None of the above"],
     "political and economic",
     "The deck names exactly two factors behind the state-monopoly era: Economic "
     "(natural monopoly) and Political (state control). 'Social' is not listed."),

    (16,
     "Which of the following is NOT a widely accepted regulatory objective in the "
     "telecommunication sector?",
     ["Foster competitive markets to promote local entrepreneurial initiative",
      "Protect consumer rights, including privacy rights",
      "Promote universal access to basic telecommunications services",
      "Optimize use of scarce resources",
      "Create a favourable climate to promote investment to expand telecommunications "
      "networks"],
     "Foster competitive markets to promote local entrepreneurial initiative",
     "The deck's objective is to foster competitive markets to promote efficient "
     "supply, quality, advanced services and efficient prices — NOT 'local "
     "entrepreneurial initiative'. The other four are listed objectives verbatim."),

    (17,
     "What type of rule is referred to as 'common sense' regulation?",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post",
     "Inferred: 'common-sense' regulation best fits ex-post — general principles "
     "applied with judgment after the fact. NB: the phrase is not verbatim in the decks "
     "and the mid-sem key left it un-highlighted, so confirm with your lecturer."),

    (18,
     "The mission of the UN specialized agency responsible for issues concerning "
     "information and communication technologies includes all of the following EXCEPT",
     ["coordinating the shared global use of the radio spectrum",
      "promoting international cooperation in assigning satellite orbits",
      "working to improve telecommunication infrastructure in the developing world",
      "assisting in the development and coordination of worldwide technical standards",
      "None of the above"],
     "None of the above",
     "The deck gives the ITU mission as exactly these four, so all are included and "
     "none is the exception."),

    (19,
     "Perfect competition occurs in a market where there are many firms each selling",
     ["a unique product", "a capital intensive product", "a similar product",
      "an identical product", "a competitive product"],
     "an identical product",
     "Under perfect competition 'the goods offered for sale are all exactly the same' "
     "— i.e. an identical (homogeneous) product."),

    (20,
     "The maxim 'hear the other side' is expressed in Latin as",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "Audi alteram partem",
     "'Hear the other side' is the maxim audi alteram partem — the fair-hearing rule."),

    (21,
     "Which of these entities is responsible for policy implementation in the "
     "telecommunication sector in most developed market economies?",
     ["The ministry in charge of the telecommunication sector",
      "The national telecommunication regulator", "Mobile network operators",
      "The courts of law", "The police"],
     "The national telecommunication regulator",
     "Policy-making is the ministry's (political) role; 'regulation focuses on "
     "translating the objectives of policy decisions into practical measures' — so the "
     "independent national regulator implements policy. (Un-highlighted in the key.)"),

    (22,
     "Which of the following is FALSE about an industry with one monopoly firm?",
     ["Higher prices are experienced", "Supply is low", "Production is inefficient",
      "Inferior goods are produced", "None of the above"],
     "Inferior goods are produced",
     "The deck lists exactly three monopoly harms: lower output (low supply), higher "
     "price, and less-efficient/higher-cost production. 'Inferior goods are produced' is "
     "not one of them — so it is the false statement."),

    (23,
     "Which of these sectors manages the international radio frequency spectrum and "
     "satellite orbit resources?",
     ["ITU-R", "ITU-T", "ITU-D", "ITU-S", "None of the above"],
     "ITU-R",
     "'ITU-R (Radiocommunication) … manages the international radio frequency spectrum "
     "and satellite orbit resources.'"),

    (24,
     "______ regulation gives regulation its power to react reasonably in unforeseen "
     "circumstances.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post",
     "Reacting reasonably to unforeseen circumstances is ex-post regulation — you "
     "respond after events occur, unlike fixed ex-ante rules."),

    (25,
     "In the mixed economy",
     ["economic problems are solved by the government and market",
      "economic decisions are made by the private sector and free market",
      "economic allocation is achieved by the 'invisible hand'",
      "economic questions are solved by government departments"],
     "economic problems are solved by the government and market",
     "A mixed economy blends command and market: 'Command measures, blended with "
     "market economies, create the mixed economies,' with governments intervening to "
     "correct market failure."),

    (26,
     "Which of these sectors helps spread equitable, sustainable and affordable access "
     "to information and communication technologies (ICT)?",
     ["ITU-R", "ITU-T", "ITU-D", "ITU-S", "None of the above"],
     "ITU-D",
     "'ITU-D (Development) … helps spread equitable, sustainable and affordable access "
     "to information and communication technologies (ICT).'"),

    (27,
     "The specialized agency of the United Nations (UN) responsible for issues that "
     "concern information and communication technologies is",
     ["International Telecommunications Union", "International Telecommunication Union",
      "Institute of Electrical and Electronics Engineers",
      "Institute of Electrical and Electronic Engineers", "World Trade Organization"],
     "International Telecommunication Union",
     "The UN's ICT agency is the International Telecommunication Union (ITU) — note the "
     "official name uses the singular 'Telecommunication'."),

    (28,
     "Which of these types of economies is vulnerable to managerial corruption?",
     ["Traditional", "Command", "Market", "All of the above", "None of the above"],
     "Command",
     "The deck: the command economy 'fails because of … vulnerability to managerial "
     "corruption' (and the intractable complexity of central control)."),

    (29,
     "The principles of good regulatory decision-making include all of the following "
     "EXCEPT",
     ["Transparency", "Objectivism", "Professionalism", "All of the above",
      "None of the above"],
     "None of the above",
     "Transparency, Objectivity and Professionalism are all listed principles, so none "
     "of the three is an exception."),

    (30,
     "A change in price can cause a shift of a demand curve.",
     ["TRUE", "FALSE"],
     "FALSE",
     "FALSE. A change in the good's own price is a movement ALONG the demand curve. The "
     "curve only shifts when income, prices of related goods, taste, expectations or the "
     "number of buyers change."),

    (31,
     "A command economy decides resource allocation by government planning.",
     ["TRUE", "FALSE"],
     "TRUE",
     "TRUE. 'In a command economy a powerful agent (usually the government) determines "
     "what people will produce, earn and consume.'"),

    (32,
     "What type of rules are vulnerable to becoming dated or inappropriate in a "
     "fast-moving high technology industry?",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-ante",
     "Ex-ante rules are fixed in advance, so in a fast-moving high-tech industry they "
     "quickly become dated or inappropriate."),

    (33,
     "If a price increase of good A increases the quantity demanded of good B, then "
     "good B is a",
     ["substitute good", "complementary good", "inferior", "normal"],
     "substitute good",
     "If A's price rises and B's quantity demanded rises, buyers are switching from A "
     "to B — they are substitutes (positive cross-price relationship)."),

    (34,
     "What type of rule is being applied if a regulator states, 'You must not indulge "
     "in anti-competitive practice', but determines whether a breach has taken place "
     "after the event?",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post",
     "Determining whether a breach occurred AFTER the event is ex-post regulation "
     "(ex post = 'after some issues have already occurred')."),

    (35,
     "Opponents of ______ regulation believe that it gives regulators the combined "
     "functions of lawmaker, policeman, judge, jury and executioner.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-ante",
     "Inferred: this classic criticism — one body that writes the rules, enforces them "
     "and judges breaches — is levelled at ex-ante (prescriptive, sector-specific) "
     "regulation, as opposed to ex-post competition law adjudicated by the courts. NB: "
     "not stated verbatim in the decks and un-highlighted in the key, so confirm."),

    (36,
     "Price ceilings are imposed to increase price above the free market equilibrium "
     "price.",
     ["TRUE", "FALSE"],
     "FALSE",
     "FALSE. A price ceiling holds the price BELOW equilibrium (a maximum price); it is "
     "a price FLOOR that keeps price above equilibrium."),

    (37,
     "The principle ______ ensures that no person can judge a case in which they have "
     "an interest.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "nemo judex in sua causa debet esse",
     "'No one should be a judge in their own cause' is the maxim nemo judex in sua "
     "causa debet esse — the rule against bias."),

    (38,
     "The role of regulators changes as markets become more competitive.",
     ["TRUE", "FALSE"],
     "TRUE",
     "TRUE — as competition develops the regulator's role shifts (lighter-touch / more "
     "ex-post competition oversight)."),

    (39,
     "Which of these sectors standardizes global telecommunications (except for radio)?",
     ["ITU-R", "ITU-T", "ITU-D", "ITU-S", "None of the above"],
     "ITU-T",
     "'ITU-T (Standardization) … standardizes global telecommunications (except for "
     "radio)'; radio is ITU-R's job."),

    (40,
     "By concentrating action on proven grievances rather than on compliance with "
     "finely detailed rules, ______ regulation is potentially efficient regulation.",
     ["ex-parte", "ex-ante", "ex-post", "Audi alteram partem",
      "nemo judex in sua causa debet esse"],
     "ex-post",
     "Ex-post regulation acts on proven grievances after the fact instead of via finely "
     "detailed pre-set rules; the deck notes 'intrusion can be lessened by the use of "
     "ex-post rules.'"),
]

OUTPUT_FILE = "compiled_3.json"


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
