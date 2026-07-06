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
     "logic"),

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
     "TRUE"),

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
     "FALSE"),

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
     "the process by which prices adjust to reconcile the allocation of resources"),

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


def main():
    records = []
    for exam_no, q_text, options, correct in QUESTIONS:
        assert correct in options, f"correct answer not in options for Q{exam_no}"
        assert len(options) == len(set(options)), f"duplicate options in Q{exam_no}"
        records.append({
            "question_number": exam_no,
            "question_text": q_text,
            "options": options,
            "correct_answer": [correct],
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
