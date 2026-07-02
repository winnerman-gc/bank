#!/usr/bin/env python3
"""
Build the Telecommunications Policy & Regulation MCQ banks.

Source material (extracted from the slide decks in this folder):
  - TE 452 - 1&2.pdf  (Background to regulation; Overview of telecom regulation)
  - TE 462 - Framework for Regulation.pdf
  - TE 462 - Licensing Telecommunication Services.pdf

Each question is authored as (question_text, correct_answer, [distractor, distractor, distractor]).
The script places the correct answer at a balanced, pseudo-random position among the
four options so that, across the whole bank, the key (A/B/C/D) is evenly distributed.
Output JSON matches the format used by the other practice sites in this repository:

    {
      "question_number": 1,
      "question_text": "...",
      "options": ["...", "...", "...", "..."],
      "correct_answer": ["..."]
    }
"""
import json
import random

# ---------------------------------------------------------------------------
# SET 1 - Market Economics & Fundamentals  (Background to Regulation, TE 452)
# ---------------------------------------------------------------------------
SET1 = [
    ("A mobile operator lowers the monthly price of its data bundle and observes that "
     "the total quantity of bundles subscribers buy rises. Which principle does this most "
     "directly illustrate?",
     "The law of demand, where quantity demanded rises as price falls, other things equal",
     ["The law of supply, where quantity supplied rises as price falls in the short run",
      "A rightward shift of the demand curve caused by the price reduction",
      "An increase in demand elasticity that automatically raises total revenue"]),

    ("An analyst notes that the quantity of broadband demanded changed solely because the "
     "price of broadband itself changed, with incomes and tastes unchanged. This is best "
     "described as:",
     "A movement along the existing demand curve",
     ["A rightward shift of the entire demand curve",
      "A leftward shift of the entire demand curve",
      "A change in the position of the supply curve"]),

    ("When the price of fresh yoghurt rises sharply, many buyers switch to alternatives such "
     "as Fanyogo or Fanice instead. In demand analysis these alternatives are best classified as:",
     "Substitute goods",
     ["Complementary goods",
      "Inferior goods",
      "Giffen goods"]),

    ("Among the many determinants of the quantity demanded of a good, economic theory "
     "identifies one variable as central to the basic demand relationship. That variable is the:",
     "Price of the good itself",
     ["Number of sellers operating in the market",
      "Cost of the inputs used in production",
      "Level of technology available to producers"]),

    ("At higher prices a telecom equipment vendor finds it profitable to offer more units, "
     "while at lower prices it offers fewer. This relationship between price and quantity "
     "offered is captured by the:",
     "Law of supply",
     ["Law of demand",
      "Law of diminishing marginal utility",
      "Principle of tax incidence"]),

    ("The market supply curve is drawn holding input costs constant. If the price of a key "
     "input such as sugar falls for ice-cream makers, the most likely result is that the "
     "supply curve:",
     "Shifts to the right, as producers supply more at each price",
     ["Shifts to the left, as producers supply less at each price",
      "Becomes perfectly vertical at the equilibrium quantity",
      "Stays fixed while only quantity demanded increases"]),

    ("Demand for a particular good is described as elastic. This means that:",
     "Quantity demanded responds substantially to a change in the good's price",
     ["Quantity demanded barely responds to a change in the good's price",
      "Quantity supplied responds substantially to a change in the good's price",
      "Price remains fixed regardless of changes in quantity demanded"]),

    ("A regulator studies a service that consumers treat as a necessity with few substitutes, "
     "so a price increase changes the quantity bought only slightly. Demand for this service "
     "is best described as:",
     "Inelastic",
     ["Elastic",
      "Perfectly elastic",
      "Unit elastic"]),

    ("On a standard supply-and-demand diagram, the single point at which the supply curve and "
     "the demand curve intersect determines the:",
     "Equilibrium price and equilibrium quantity",
     ["Price ceiling and the resulting shortage",
      "Price floor and the resulting surplus",
      "Tax incidence borne by buyers and sellers"]),

    ("To keep a service affordable, a government sets a maximum legal price below the market "
     "equilibrium price. Standard analysis predicts this price ceiling will most likely create:",
     "A shortage, because quantity demanded exceeds quantity supplied",
     ["A surplus, because quantity supplied exceeds quantity demanded",
      "A new stable equilibrium exactly at the controlled price",
      "An increase in supply that quickly eliminates excess demand"]),

    ("A government sets a minimum legal price above the market equilibrium to protect "
     "suppliers. The most likely consequence of this price floor is:",
     "A surplus, because quantity supplied exceeds quantity demanded",
     ["A shortage, because quantity demanded exceeds quantity supplied",
      "An immediate return of the market to its equilibrium",
      "A reduction in quantity supplied below the quantity demanded"]),

    ("In public finance, the term tax incidence refers specifically to:",
     "How the burden of a tax is distributed among the participants in a market",
     ["The statutory tax rate that a government formally sets out in legislation",
      "The total amount of revenue that a government collects from levying the tax",
      "The administrative cost a government incurs in collecting and enforcing the tax"]),

    ("When a per-unit tax is imposed on the sellers of a good, the standard model represents "
     "its initial effect as:",
     "A leftward (upward) shift of the supply curve",
     ["A rightward shift of the supply curve",
      "A leftward shift of the demand curve",
      "A rotation that makes the demand curve more elastic"]),

    ("Two markets face an identical per-unit tax. In Market A demand is highly inelastic; in "
     "Market B demand is highly elastic. Compared with sellers, buyers will tend to bear the "
     "larger share of the tax in:",
     "Market A, where demand is inelastic",
     ["Market B, where demand is elastic",
      "Both markets equally, regardless of elasticity",
      "Neither market, because sellers always remit the tax"]),

    ("An economic system in which production and allocation follow long-standing customary "
     "patterns and local leaders have the ultimate say is best described as a:",
     "Traditional economy, based on inherited customs and social roles",
     ["Command economy, directed by a central government authority",
      "Market economy, coordinated primarily through prices and competition",
      "Mixed economy, blending market forces with state intervention"]),

    ("Twentieth-century experience suggests that a command economy tends to fail largely "
     "because:",
     "A central authority cannot efficiently gather and act on the information needed to allocate resources",
     ["Prices adjust too quickly for producers to keep pace with rapidly shifting demand",
      "Private firms refuse to compete once the state withdraws support and guaranteed contracts",
      "Consumers are given so many product choices that planners cannot coordinate production"]),

    ("A mixed economy is best characterised as one in which:",
     "Markets allocate most resources while governments intervene to correct market failures",
     ["A central planner sets all prices, wages and output levels across the whole economy",
      "Custom and tradition determine nearly all economic decisions, with no market pricing",
      "Market forces operate freely with no government involvement of any kind whatsoever"]),

    ("Advocates argue that a market economy can be self-optimising because, when individuals "
     "are free to pursue their own interests, the system tends to:",
     "Settle at a stable equilibrium of supply, consumption and prices",
     ["Eliminate the need for any property rights, contracts or enforcement mechanisms",
      "Guarantee an equal distribution of income across the whole of society",
      "Prevent monopolies from ever arising in any industry whatsoever"]),

    ("In a perfectly competitive market each individual buyer and seller is assumed to be a "
     "price taker. This assumption follows from the fact that:",
     "There are so many participants that no single one can influence the market price",
     ["A single dominant firm sets the price that every other participant follows",
      "The government fixes the price at which every trade in the market must occur",
      "Buyers and sellers openly collude with one another to maintain a single common price"]),

    ("Compared with a competitive industry, a profit-maximising monopoly is generally "
     "expected to:",
     "Produce less output and charge a higher price",
     ["Produce more output and charge a lower price",
      "Produce the same output but at a lower cost",
      "Charge a lower price while expanding total output"]),

    ("An industry is termed a natural monopoly when:",
     "A single firm can supply the whole market at lower cost than two or more firms could",
     ["Two or more competing firms can always supply the market more cheaply than one",
      "The government simply bans all but one licensed firm from entering the market",
      "Firms in the industry naturally collude to behave as though they were one"]),

    ("Where a genuine natural monopoly exists, a government wishing to avoid wasteful "
     "duplication of infrastructure may reasonably choose to:",
     "Tolerate the single firm but subject it to regulation",
     ["Force several firms to compete regardless of cost",
      "Withdraw entirely and leave the market unregulated",
      "Nationalise every competing firm in the wider economy"]),

    ("Within the logic of a market economy, the primary justification for governments "
     "intervening through regulators and other institutions is that:",
     "Markets can fail, and intervention may correct such failures",
     ["Markets always allocate resources perfectly without help",
      "Government planning is inherently superior to all markets",
      "Competition should be eliminated to simplify oversight"]),

    ("An economist distinguishes a change in demand from a change in quantity demanded. A "
     "change in demand (a shift of the curve) is caused by:",
     "A change in a determinant other than the good's own price, such as income or tastes",
     ["A change in the good's own price alone, holding all else constant",
      "A movement to a different point along the same, unchanged demand curve",
      "A simultaneous change in supply that happens to exactly offset any change in demand"]),

    ("One reason a monopoly is considered socially harmful is that its output is typically "
     "produced:",
     "Less efficiently and at a higher cost than under competition",
     ["More efficiently and at a lower cost than under competition",
      "At exactly the competitive level of cost and efficiency",
      "Only when it is directly subsidised by the government"]),
]

# ---------------------------------------------------------------------------
# SET 2 - Sector Reform & Regulatory Foundations  (TE 452)
# ---------------------------------------------------------------------------
SET2 = [
    ("Before the 1980s, telecommunications services in most countries were typically "
     "provided by:",
     "State-owned monopolies",
     ["Numerous competing private operators",
      "Independent regional cooperatives",
      "Foreign-owned multinational consortia"]),

    ("A factor underpinning the pre-1980s telecom monopoly paradigm was economic: high "
     "network build costs and low demand meant a second operator could not easily recover "
     "its costs. This gave the industry the character of a:",
     "Natural monopoly",
     ["Perfectly contestable market",
      "Fully deregulated free market",
      "Command-economy consumer good"]),

    ("A political factor behind early state telecom monopolies was that governments:",
     "Wished to retain state control over communications, often treating them as an extension of postal networks",
     ["Were legally barred by international postal treaty from ever licensing a private telecom firm",
      "Lacked any government ministry with the technical capacity to run even a basic postal service",
      "Preferred to auction off spectrum rights directly to the highest-bidding private investor"]),

    ("In telecommunications, liberalization is best defined as:",
     "The process of transition from a monopoly market to a competitive one",
     ["The transfer of an operator's ownership from the state to private hands",
      "The intervention of government to achieve specific market outcomes",
      "The setting of technical standards common to all operators"]),

    ("A central element of liberalization is the removal of exclusivities from the former "
     "monopoly fixed-network operator, commonly called the incumbent. The direct effect of "
     "removing these exclusivities is to:",
     "Allow new entrants to compete in services that were previously monopolised",
     ["Transfer ownership of the incumbent's shares to a group of private investors",
      "Guarantee the incumbent a permanently protected and exclusive market position",
      "Impose strict price caps on every single service the incumbent operator offers"]),

    ("Privatization in the telecom sector refers to:",
     "The transfer of ownership of an operator from the state to the private sector",
     ["The transition of an entire market from monopoly toward open competition",
      "The imposition of universal-service obligations on all licensed operators",
      "The creation of a wholly independent national regulatory authority"]),

    ("Governments have privatized incumbent operators in different ways. Selling a stake to a "
     "single strategic investor, rather than via a broad public share sale, has been the more "
     "common approach in:",
     "Developing countries",
     ["Highly industrialised countries",
      "Countries that have no incumbent operator",
      "Countries that retained a full state monopoly"]),

    ("A country opens its mobile market to several competing firms but keeps the incumbent "
     "fixed-line operator fully state-owned. This situation is best described as:",
     "Liberalization of the market without privatization of the incumbent operator",
     ["Privatization of the incumbent operator without any market liberalization",
      "Both full market liberalization and full privatization of the incumbent",
      "Neither market liberalization nor privatization of the incumbent at all"]),

    ("In the context of the telecom sector, regulation is best defined as:",
     "Government intervention in markets to achieve certain desired outcomes",
     ["The complete and permanent removal of government from all market activity",
      "The wholesale transfer of state-owned assets into full private ownership",
      "The voluntary self-policing of firms with absolutely no external oversight"]),

    ("Regulation is sometimes said to take three basic forms. The form that establishes a "
     "common, legally enforceable platform for all businesses, such as rules governing "
     "electrical supply or company accounting, is:",
     "Technical standardization",
     ["Competition regulation",
      "Public policy regulation",
      "Voluntary self-regulation"]),

    ("Legislation that controls the supply of goods such as alcohol, gambling or pornography "
     "because doing so is believed to serve the public interest is an example of:",
     "Public policy regulation",
     ["Technical standardization",
      "Competition regulation",
      "Co-regulation"]),

    ("The form of regulation that seeks to create and maintain fair competitive relationships "
     "between businesses, and between businesses and consumers, is:",
     "Competition regulation",
     ["Technical standardization",
      "Public policy regulation",
      "Zero regulation"]),

    ("Although telecom regulation can take all three basic forms, the principal focus of "
     "contemporary regulation of the telecommunications services industry is:",
     "The creation, nourishment and maintenance of competitive markets",
     ["The standardisation of accounting rules across all industries",
      "The control of socially sensitive goods such as gambling",
      "The elimination of private ownership from the sector"]),

    ("Among the widely accepted regulatory objectives in the telecom sector is the aim to:",
     "Promote universal access to basic telecommunications services",
     ["Guarantee a fixed profit margin to every licensed operator",
      "Restrict connectivity to commercially attractive urban areas",
      "Prevent any new operators from entering the market"]),

    ("A recognised regulatory objective is that, where competitive markets do not exist or "
     "have failed, the regulator should:",
     "Prevent abuses of market power such as excessive pricing by dominant firms",
     ["Guarantee the dominant firm full protection from all potential competitors",
      "Withdraw all regulatory oversight and let the market correct itself unaided",
      "Fix every operator's retail prices at exactly identical levels nationwide"]),

    ("Which statement best captures the distinction between policy and law as drawn in the "
     "course material?",
     "Law can compel or prohibit behaviour, whereas policy merely guides actions toward a desired outcome",
     ["Policy can compel or prohibit behaviour, whereas law only ever offers non-binding guidance",
      "Policy and law are identical concepts, so the two terms may always be used interchangeably",
      "Regulation sets the broad long-term goals while policy enforces them through the courts"]),

    ("In the policy-to-practice chain, regulation is primarily concerned with:",
     "Translating the objectives of policy decisions into practical rules and decisions",
     ["Setting the broad, long-term national vision that exists prior to any policy",
      "Replacing the need for any underlying legislation or statutory authority",
      "Auditing the personal finances of individual government ministers each year"]),

    ("In many countries before reform, a single ministry or government unit often acted "
     "simultaneously as:",
     "Policy maker, policy implementer and operator of the telephone service",
     ["An independent regulator that is fully separated from the operator",
      "A purely commercial firm with no policy responsibilities whatsoever",
      "A neutral standards body with no operational role in the sector"]),

    ("The International Telecommunication Union (ITU) is best described as:",
     "A specialised agency of the United Nations responsible for information and communication technology issues",
     ["A private consortium formed and funded by the world's largest mobile network operators worldwide",
      "A regional trade bloc that negotiates import tariffs on telecommunications equipment for its members",
      "A commercial standards-setting firm that is owned and controlled by major equipment vendors"]),

    ("Within the ITU's three-sector structure, the sector that manages the international "
     "radio-frequency spectrum and satellite-orbit resources is:",
     "ITU-R (Radiocommunication)",
     ["ITU-T (Standardization)",
      "ITU-D (Development)",
      "ITU-P (Policy)"]),

    ("The ITU sector responsible for standardizing global telecommunications, except for "
     "radio matters, is:",
     "ITU-T (Standardization)",
     ["ITU-R (Radiocommunication)",
      "ITU-D (Development)",
      "ITU-S (Spectrum)"]),

    ("Helping to spread equitable, sustainable and affordable access to ICTs is the principal "
     "role of which ITU sector?",
     "ITU-D (Development)",
     ["ITU-R (Radiocommunication)",
      "ITU-T (Standardization)",
      "ITU-A (Access)"]),

    ("The World Trade Organization's Agreement on Basic Telecommunications (the BTA) "
     "primarily:",
     "Establishes rules for competition and promotes open investment in telecoms across countries",
     ["Allocates radio spectrum directly to individual telecom operators in each member state",
      "Sets the maximum retail tariffs that operators may charge their consumers directly",
      "Issues operating licences directly to individual carriers within each member state"]),

    ("One of the six basic principles of the WTO Reference Paper on Regulation is that:",
     "There should be a regulatory body independent of operating companies",
     ["The dominant operator should also serve as the regulator",
      "Licensing criteria should be kept confidential from competitors",
      "Scarce resources should be reserved for the incumbent operator"]),

    ("The WTO Reference Paper requires telecom regulators to be independent of operating "
     "companies. On independence from government, the material indicates that regulators are:",
     "Not necessarily independent of governments, though greater independence is often regarded as better",
     ["Required by law to be wholly controlled and directed by the relevant government ministry",
      "Required by law to be completely and formally independent of government in every respect",
      "Required by law to be jointly owned and controlled by the operators that they regulate"]),
]

# ---------------------------------------------------------------------------
# SET 3 - Framework for Regulation  (TE 462)
# ---------------------------------------------------------------------------
SET3 = [
    ("According to the framework for regulation, the laws passed by governments to enable "
     "regulation typically:",
     "Appoint regulatory bodies and confer on them powers to take action",
     ["Guarantee permanent monopoly status to the incumbent state operator",
      "Remove all accountability and reporting requirements from regulators",
      "Fix the retail prices of every single regulated service nationwide"]),

    ("Which option best lists the categories of law that bear specifically on the "
     "telecommunications services industry?",
     "Sector-specific telecom law, competition and fair-trading law, and other relevant law such as privacy",
     ["Criminal law, international maritime law and constitutional law only, excluding all else",
      "Tax law, general employment law and intellectual-property law only, and nothing further",
      "Banking law, insurance law and environmental law only, excluding any other category"]),

    ("Provisions enacted by bodies such as ECOWAS or the WTO take force in a member or "
     "signatory country when they are:",
     "Transposed into national law in accordance with treaty obligations",
     ["Simply published on the regional body's official website",
      "Approved by a majority vote of the country's licensed operators",
      "Adopted automatically the moment they are agreed upon regionally"]),

    ("The framework notes that the function of regulation may be split between two or more "
     "bodies. A risk a country must manage when doing so is that:",
     "Poorly designed division of functions can lead to disagreements and slow decision-making",
     ["A single national regulator will inevitably end up capturing the entire market",
      "Operators will find themselves completely unable to obtain any licence at all",
      "Spectrum will automatically be allocated to all operators entirely free of charge"]),

    ("Listed in increasing order of intrusiveness, the styles of regulation are:",
     "Zero regulation, self-regulation, co-regulation, formal regulation",
     ["Formal regulation, co-regulation, self-regulation, zero regulation",
      "Self-regulation, zero regulation, formal regulation, co-regulation",
      "Co-regulation, formal regulation, zero regulation, self-regulation"]),

    ("An industry described as operating under zero regulation is one in which:",
     "Market forces are allowed to work with no external intervention",
     ["A regulator intervenes minutely in the firm's daily operations",
      "Firms jointly agree binding rules under an industry watchdog",
      "Prices are set directly and solely by a government ministry"]),

    ("Self-regulation, in which the players in an industry regulate themselves, tends to be "
     "MOST effective when:",
     "There is a high convergence of interest among the stakeholders",
     ["There are strong commercial conflicts between the players",
      "A single firm dominates and distrusts all the others",
      "The regulator intervenes in every operational decision"]),

    ("A frequently cited benefit of self-regulation is that:",
     "Companies usually understand their own businesses better than an external regulator does",
     ["It removes all administrative costs of regulation from consumers and industry",
      "It guarantees that no company will ever act opportunistically toward rivals",
      "It eliminates the need for any underlying legislation or licensing regime"]),

    ("Co-regulation is best described as an arrangement in which:",
     "The regulator joins industry players in a joint forum rather than regulating purely from outside",
     ["Firms operate entirely independently with no external oversight of any kind whatsoever",
      "The regulator alone dictates every technical and pricing decision unilaterally",
      "A foreign international body simply assumes all domestic regulatory authority"]),

    ("While potentially very successful, co-regulation is particularly vulnerable to:",
     "Role ambiguity and differing perceptions of what each player will do",
     ["An immediate and total loss of all formal regulatory powers",
      "The automatic capture of the regulator by consumer groups",
      "A blanket legal prohibition on any form of industry collaboration"]),

    ("Regulation is described as intrusive when the regulator:",
     "Intervenes often and minutely in the day-to-day running of a company's business",
     ["Lays down only general principles and leaves the methods to firms themselves",
      "Withdraws entirely from the market and lets market forces operate unaided",
      "Limits itself only to publishing occasional, non-binding guidelines"]),

    ("One reason intrusive regulation is considered undesirable is that:",
     "The regulator effectively becomes a proxy manager of the industry, weakening operators' freedom",
     ["It always sharply reduces the total administrative cost of regulating the industry",
      "It guarantees that competitive market forces will always prevail entirely unaided",
      "It completely removes the regulator's responsibility for any market outcomes at all"]),

    ("A good regulator is advised to make regulation pervasive rather than intrusive. This "
     "means regulation should:",
     "Influence operators broadly while letting them manage their own affairs within the spirit of the rules",
     ["Dictate the exact, precise technical solution required of every single licensed operator",
      "Have as little practical impact as possible on any of the companies operating in the market",
      "Apply narrowly to only a single dominant operator in the market, ignoring all the rest"]),

    ("The main instruments through which regulation is accomplished include authorizations, "
     "rules, determinations, consents and:",
     "Guidelines",
     ["Share buy-backs",
      "Spectrum auctions",
      "Corporate tax assessments"]),

    ("A system of authorization may issue specific authorizations and general authorizations. "
     "These correspond respectively to:",
     "Individual operator licences and class licences",
     ["Spectrum licences and national numbering plans",
      "Regulatory price caps and interconnection orders",
      "Formal consents and regulatory determinations"]),

    ("Determinations are instruments of ongoing regulation that, in effect:",
     "Elaborate the rules, for example in the periodic review of price controls",
     ["Permanently revoke an operator's licence without any right of appeal",
      "Replace the underlying legislation entirely and without warning",
      "Carry no legal force at all and are merely advisory in nature"]),

    ("A consent is best understood as:",
     "A negative determination that formally relieves an operator from complying with a requirement",
     ["An order that formally imposes an additional new obligation on the operator concerned",
      "An informal guideline document that carries no legal status whatsoever in practice",
      "A formal financial penalty levied against an operator for breach of a licence condition"]),

    ("Guidelines differ from rules and determinations in that guidelines:",
     "Do not in themselves possess legal status and are usually written in user-friendly language",
     ["Have far greater binding legal force than the licence conditions do themselves",
      "Can be issued only by the courts, and only following a successful appeal process",
      "Automatically and permanently revoke a licence the very moment they are breached"]),

    ("A key reason regulators consult widely before finalising instruments is that "
     "consultation:",
     "Gives industry ownership and pre-knowledge of decisions and enriches decision-making",
     ["Transfers all formal decision-making power directly to the consulted parties",
      "Entirely removes the regulator's legal obligation to justify its decisions",
      "Guarantees that no consulted party will ever appeal the final regulatory outcome"]),

    ("An appeal against a regulator's action may be brought on the grounds of law "
     "(illegality), procedure (misadministration) or:",
     "Logic (irrationality)",
     ["Profitability (commercial loss)",
      "Popularity (public disapproval)",
      "Convenience (administrative delay)"]),

    ("Which of the following is a recognised enforcement power available to a regulator "
     "dealing with rule breaches?",
     "Revoking a licence, or imposing fines and compliance orders",
     ["Seizing ownership of a competitor's shares",
      "Setting the personal salaries of company directors",
      "Banning the company's customers from switching providers"]),

    ("Regarding the funding of national regulatory authorities, the typical arrangement is "
     "that:",
     "Governments assume primary responsibility but usually pass the cost onto industry through fees",
     ["Operators are always legally barred from contributing any funds to the regulator at all",
      "Regulators are funded entirely by fines collected from ordinary telecom consumers",
      "Funding comes entirely from international donor agencies and foreign aid grants"]),

    ("The concept of regulatory hazard refers to the fact that:",
     "Regulatory power, if exercised unwisely, can distort markets and damage the industry it serves",
     ["Regulators personally face genuine physical danger when inspecting live telecom networks",
      "Regulation always removes every last trace of risk from the telecom market entirely",
      "Operators face absolutely no consequences whatsoever for repeatedly breaching the rules"]),

    ("Regulatory capture occurs when:",
     "The regulator identifies too closely with, and so serves the interests of, the industry it regulates",
     ["The regulator becomes completely paralysed and simply stops issuing any decisions at all",
      "Individual operators are captured and then run directly by the regulator itself as owner",
      "Ordinary consumers themselves take over the entire day-to-day running of the regulator"]),

    ("The information asymmetry, or knowledge gap, that regulators face arises because:",
     "The companies being regulated usually know far more about the business than the regulator does",
     ["Regulators are always legally forbidden from collecting any operational data at all",
      "Consumers deliberately conceal their true preferences from the regulator entirely",
      "Operators are always legally required to share none of their internal financial records"]),
]

# ---------------------------------------------------------------------------
# SET 4 - Licensing, Scarce Resources & Interconnection  (TE 462)
# ---------------------------------------------------------------------------
SET4 = [
    ("Regulators issue licences to companies primarily to authorise them to:",
     "Operate telecommunications networks and provide telecommunications services",
     ["Manufacture and export telecommunications equipment internationally",
      "Set the national monetary and fiscal policy for the entire economy",
      "Audit the financial accounts of every single rival operator each year"]),

    ("Beyond granting permission to operate, a telecommunications licence characteristically "
     "specifies:",
     "What facilities a company may deploy, what services it may offer, and how it must interact with other businesses",
     ["The exact retail prices that every other licensed operator in the country must charge consumers",
      "The complete internal staffing structure and organisational chart of the regulator itself",
      "The personal income tax obligations of each of the company's individual board directors"]),

    ("In addition to facilities and services, major licences may govern access to scarce "
     "resources such as spectrum and numbers, and commonly require companies to pay:",
     "Upfront fees when the licence is awarded and annual payments thereafter",
     ["A fixed share of annual profits paid to every competing operator",
      "Nothing at all, since licences are always granted completely free of charge",
      "A single one-time deposit that is always fully refunded upon expiry"]),

    ("Historically, telecom licences were allocated separately for different sub-markets, for "
     "example fixed networks, mobile networks or paging. The main characteristic of this "
     "approach was that licences:",
     "Differentiated between specific technologies and services",
     ["Were completely technology- and service-neutral by design",
      "Imposed identical licence terms across every single market segment",
      "Were never tied to any particular type of technology or service"]),

    ("Recent technological convergence, which lets different platforms deliver a wider range "
     "of services, has prompted some regulators to move toward:",
     "Technology- and service-neutral licensing",
     ["Stricter technology-specific licensing for each platform",
      "The complete abolition of all forms of licensing",
      "Permanent exclusive licences for incumbent operators"]),

    ("A technology-neutral licence to provide a telephone service is one that:",
     "Lets the company choose whether to use a fixed network or a particular wireless technology",
     ["Requires the company to use one single, specified fixed-line technology only",
      "Strictly forbids the company from offering any form of voice service at all",
      "Mandates the exclusive use of a single, government-approved equipment vendor only"]),

    ("The two main types of licence awarded to telecom companies are:",
     "Individual operator licences and class licences (general authorizations)",
     ["Spectrum-specific licences and separate telephone numbering licences",
      "International import licences and international export licences",
      "Short-term provisional licences and longer-term probationary licences"]),

    ("Individual operator licences are used primarily where:",
     "The number of licences is limited, dominance is likely, or specific resources such as spectrum must be allocated",
     ["The market segment has essentially unlimited room for any number of new entrants to join",
      "Absolutely no scarce resources of any kind whatsoever are ever involved in that segment",
      "Perfectly identical terms are wanted for every single business operating in that market segment"]),

    ("Class licences (general authorizations) are characterised by the fact that they:",
     "Set out identical terms of operation for all businesses in a market segment, such as ISPs",
     ["Are always tailored individually to just one single, specifically named operator",
      "Are reserved exclusively for use by the former state incumbent operator",
      "Apply only in the specific cases where radio spectrum must be allocated"]),

    ("A current trend favours replacing individual operator licences with general "
     "authorizations wherever possible because doing so:",
     "Simplifies regulation, helps ensure a level playing field, and is more flexible to market change",
     ["Maximises the one-time upfront revenue collected from each and every individual operator",
      "Permanently guarantees the incumbent a fully protected monopoly position",
      "Completely eliminates the need for any independent regulator in the sector whatsoever"]),

    ("One licensing objective treats basic telecommunications as an essential public service. "
     "This justifies:",
     "Retaining some controls to ensure services are provided in the public interest",
     ["Removing all regulatory oversight the moment the market is privatised",
      "Reserving service provision for a single state monopoly forever",
      "Allowing operators to serve only the most profitable customers"]),

    ("Network roll-out and service-coverage obligations are often written into licences to "
     "advance which licensing objective?",
     "Expansion of networks and services, and universal service",
     ["Generation of one-time government spectrum auction revenue",
      "Protection of the incumbent operator from any competition",
      "Standardisation of company accounting and reporting practices"]),

    ("When a state-owned incumbent is privatized, a licence is necessary because it:",
     "Specifies what the investor is buying and what the government expects from the operator",
     ["Transfers full legal ownership and operational control of the regulator to the investor",
      "Guarantees the investor complete and permanent freedom from all regulation",
      "Entirely removes the operator's obligation to serve any customers at all"]),

    ("Licensing can be used to regulate market structure, most directly by:",
     "Determining the number of operators licensed to provide services",
     ["Fixing the wholesale price of every single network input",
      "Setting the wages paid to all of an operator's employees",
      "Selecting which equipment vendors operators must always use"]),

    ("Licence conditions intended to create a level playing field and limit incumbents' abuse "
     "of dominance are generally referred to as:",
     "Anti-competitive safeguards or fair-trading conditions",
     ["Universal-service obligations for underserved regions",
      "Spectrum-refarming and reallocation provisions",
      "Tariff-rebalancing and price-adjustment schedules"]),

    ("Finite resources such as radio spectrum, numbers and rights of way should, as a "
     "licensing objective, be allocated:",
     "Between operators fairly, efficiently and in the public interest",
     ["Entirely to whichever operator has the longest operating history",
      "Purely on a first-come basis with no regard to efficiency at all",
      "Only to operators that are owned by the national government"]),

    ("Licensing can generate government revenue in two characteristic ways:",
     "One-time revenues from auctions and continuing revenue from annual licence fees",
     ["Confiscation of operator profits and outright seizure of their assets",
      "Personal income taxes levied directly on the regulator's own staff",
      "Mandatory donations collected annually from international agencies"]),

    ("Consumer-protection conditions in telecom licences commonly address matters such as:",
     "Billing practices, complaint mechanisms and mandatory services like emergency calls",
     ["The detailed internal share structure of the operator's holding company",
      "The personal credit ratings of each of the company's individual board directors",
      "The choice of which external auditors are used by the regulator itself"]),

    ("By clearly defining the rights and obligations of the operator and the regulator, a "
     "licence advances the objective of:",
     "Regulatory certainty, which builds confidence and helps attract investment",
     ["Spectrum refarming carried out across all competing operators",
      "Eliminating the regulator's discretion entirely and permanently",
      "Guaranteeing every single operator an exactly equal market share"]),

    ("Radio spectrum is a scarce resource whose international allocation is governed by rules "
     "intended to maximise its use while minimising cross-border interference. These rules "
     "are managed by the:",
     "International Telecommunication Union (ITU)",
     ["World Trade Organization (WTO)",
      "Economic Community of West African States (ECOWAS)",
      "Individual operators within each country"]),

    ("Although telephone numbers are in principle infinite, they are treated as a scarce "
     "resource partly because:",
     "People can hold only a limited number of digits in short-term memory, and numbers must be allocated in meaningful blocks",
     ["There are physically only a very small, fixed number of usable digits in existence worldwide",
      "Each individual telephone number requires its own permanently dedicated radio frequency to function",
      "A given telephone number can only ever be assigned to and used by one single country worldwide"]),

    ("Number portability is a mechanism by which:",
     "The subscriber, rather than the operator, owns the number and can take it when switching providers",
     ["The operator permanently and exclusively owns every telephone number that it ever issues",
      "Numbers are periodically auctioned off to whichever operator happens to bid the highest",
      "Subscribers must always change their number each time they switch to a completely new provider"]),

    ("In allocating spectrum, a regulator may auction it to the highest bidder or allocate it "
     "at low cost. Allocating spectrum at low cost is typically intended to:",
     "Reduce prices or encourage the rollout of new services",
     ["Maximise the one-time revenue collected by the government",
      "Guarantee that only one operator can ever use the band",
      "Remove the need to manage interference between users"]),

    ("A primary reason spectrum must be allocated through agreements such as licences, rather "
     "than used freely, is to:",
     "Ensure it is properly distributed and that users do not interfere with one another",
     ["Increase the total number of digits available for telephone numbers nationally",
      "Allow every single licensed operator to broadcast on any frequency it wishes",
      "Remove the need for any international coordination of frequencies at all"]),

    ("The core principle of interconnection is that:",
     "Everyone should be able to communicate with everyone else, regardless of which network they subscribe to",
     ["Each operator should deliberately keep its subscribers isolated from rivals' networks",
      "Only operators of a roughly similar size are ever legally required to interconnect",
      "Interconnection is legally required only between the largest international carriers"]),
]

# All 100 questions are compiled, in thematic order, into a single bank.
ALL_QUESTIONS = SET1 + SET2 + SET3 + SET4
OUTPUT_FILE = "compiled.json"


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def main():
    rng = random.Random(462)  # reproducible key placement
    n = len(ALL_QUESTIONS)

    # Balanced key positions: exactly 25 of each slot across the 100 questions.
    per_slot, remainder = divmod(n, 4)
    positions = []
    for slot in range(4):
        positions += [slot] * (per_slot + (1 if slot < remainder else 0))
    rng.shuffle(positions)

    summary = {0: 0, 1: 0, 2: 0, 3: 0}
    records = []
    for idx, (q_text, correct, distractors) in enumerate(ALL_QUESTIONS):
        pos = positions[idx]
        options = build_options(distractors, correct, pos)
        assert options[pos] == correct
        assert len(options) == 4 and len(set(options)) == 4, q_text[:40]
        summary[pos] += 1
        records.append({
            "question_number": idx + 1,
            "question_text": q_text,
            "options": options,
            "correct_answer": [correct],
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)
    print(f"Wrote {OUTPUT_FILE}: {len(records)} questions")

    total = sum(summary.values())
    print("\nKey distribution (option slot -> count):")
    for slot in range(4):
        print(f"  slot {chr(65 + slot)}: {summary[slot]} ({summary[slot] / total:.0%})")
    print(f"  total: {total}")


if __name__ == "__main__":
    main()
