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
     ["The statutory rate at which a tax is officially levied",
      "The total revenue a government collects from a tax",
      "The administrative cost of collecting and enforcing a tax"]),

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
     "Traditional economy",
     ["Command economy",
      "Market economy",
      "Mixed economy"]),

    ("Twentieth-century experience suggests that a command economy tends to fail largely "
     "because:",
     "A central authority cannot efficiently gather and act on the information needed to allocate resources",
     ["Prices adjust too quickly for producers to keep pace with demand",
      "Private firms refuse to compete once the state withdraws",
      "Consumers are given too many choices to coordinate production"]),

    ("A mixed economy is best characterised as one in which:",
     "Markets allocate most resources while governments intervene to correct market failures",
     ["A central planner sets all prices, wages and output levels",
      "Custom and tradition determine nearly all economic decisions",
      "Market forces operate with no government involvement of any kind"]),

    ("Advocates argue that a market economy can be self-optimising because, when individuals "
     "are free to pursue their own interests, the system tends to:",
     "Settle at a stable equilibrium of supply, consumption and prices",
     ["Eliminate the need for any property rights or contracts",
      "Guarantee an equal distribution of income across society",
      "Prevent monopolies from ever arising in any industry"]),

    ("In a perfectly competitive market each individual buyer and seller is assumed to be a "
     "price taker. This assumption follows from the fact that:",
     "There are so many participants that no single one can influence the market price",
     ["A single dominant firm sets the price that all others follow",
      "The government fixes the price at which all trades must occur",
      "Buyers and sellers collude to maintain a common price"]),

    ("Compared with a competitive industry, a profit-maximising monopoly is generally "
     "expected to:",
     "Produce less output and charge a higher price",
     ["Produce more output and charge a lower price",
      "Produce the same output but at a lower cost",
      "Charge a lower price while expanding total output"]),

    ("An industry is termed a natural monopoly when:",
     "A single firm can supply the whole market at lower cost than two or more firms could",
     ["Two firms can always supply the market more cheaply than one",
      "The government legally bans all but one firm from entering",
      "Firms naturally collude to behave as though they were one"]),

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
     ["A change in the good's own price alone",
      "Movement to a different point on the same demand curve",
      "A simultaneous and exactly offsetting change in supply"]),

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
     ["Were barred by treaty from licensing any private firm",
      "Lacked any ministry capable of running a postal service",
      "Preferred to auction spectrum to the highest private bidder"]),

    ("In telecommunications, liberalization is best defined as:",
     "The process of transition from a monopoly market to a competitive one",
     ["The transfer of an operator's ownership from the state to private hands",
      "The intervention of government to achieve specific market outcomes",
      "The setting of technical standards common to all operators"]),

    ("A central element of liberalization is the removal of exclusivities from the former "
     "monopoly fixed-network operator, commonly called the incumbent. The direct effect of "
     "removing these exclusivities is to:",
     "Allow new entrants to compete in services that were previously monopolised",
     ["Transfer the incumbent's shares to private investors",
      "Guarantee the incumbent a permanently protected market",
      "Impose price caps on every service the incumbent offers"]),

    ("Privatization in the telecom sector refers to:",
     "The transfer of ownership of an operator from the state to the private sector",
     ["The transition of a market from monopoly to competition",
      "The imposition of universal-service obligations on operators",
      "The creation of an independent national regulatory authority"]),

    ("Governments have privatized incumbent operators in different ways. Selling a stake to a "
     "single strategic investor, rather than via a broad public share sale, has been the more "
     "common approach in:",
     "Developing countries",
     ["Highly industrialised countries",
      "Countries that have no incumbent operator",
      "Countries that retained a full state monopoly"]),

    ("A country opens its mobile market to several competing firms but keeps the incumbent "
     "fixed-line operator fully state-owned. This situation is best described as:",
     "Liberalization without privatization of the incumbent",
     ["Privatization without liberalization",
      "Both full liberalization and full privatization",
      "Neither liberalization nor privatization"]),

    ("In the context of the telecom sector, regulation is best defined as:",
     "Government intervention in markets to achieve certain desired outcomes",
     ["The complete removal of government from market activity",
      "The transfer of state assets into private ownership",
      "The voluntary self-policing of firms with no oversight"]),

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
     ["Guarantee the dominant firm protection from all competitors",
      "Withdraw oversight so the market can correct itself",
      "Fix every operator's retail prices at identical levels"]),

    ("Which statement best captures the distinction between policy and law as drawn in the "
     "course material?",
     "Law can compel or prohibit behaviour, whereas policy merely guides actions toward a desired outcome",
     ["Policy can compel behaviour, whereas law only offers guidance",
      "Policy and law are identical and fully interchangeable terms",
      "Regulation sets broad goals while policy enforces them in court"]),

    ("In the policy-to-practice chain, regulation is primarily concerned with:",
     "Translating the objectives of policy decisions into practical rules and decisions",
     ["Setting the broad long-term vision before any policy exists",
      "Replacing the need for any underlying legislation",
      "Auditing the personal finances of government ministers"]),

    ("In many countries before reform, a single ministry or government unit often acted "
     "simultaneously as:",
     "Policy maker, policy implementer and operator of the telephone service",
     ["An independent regulator fully separated from the operator",
      "A purely commercial firm with no policy responsibilities",
      "A neutral standards body with no operational role"]),

    ("The International Telecommunication Union (ITU) is best described as:",
     "A specialised agency of the United Nations responsible for information and communication technology issues",
     ["A private consortium of the world's largest mobile operators",
      "A regional trade bloc that sets tariffs on telecom equipment",
      "A commercial standards firm owned by equipment vendors"]),

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
     ["Allocates radio spectrum directly to individual operators",
      "Sets the retail tariffs that operators may charge consumers",
      "Issues operating licences to individual carriers in member states"]),

    ("One of the six basic principles of the WTO Reference Paper on Regulation is that:",
     "There should be a regulatory body independent of operating companies",
     ["The dominant operator should also serve as the regulator",
      "Licensing criteria should be kept confidential from competitors",
      "Scarce resources should be reserved for the incumbent operator"]),

    ("The WTO Reference Paper requires telecom regulators to be independent of operating "
     "companies. On independence from government, the material indicates that regulators are:",
     "Not necessarily independent of governments, though greater independence is often regarded as better",
     ["Required to be wholly controlled by the relevant ministry",
      "Required to be completely independent of government in every respect",
      "Required to be jointly owned by the operators they regulate"]),
]

# ---------------------------------------------------------------------------
# SET 3 - Framework for Regulation  (TE 462)
# ---------------------------------------------------------------------------
SET3 = [
    ("According to the framework for regulation, the laws passed by governments to enable "
     "regulation typically:",
     "Appoint regulatory bodies and confer on them powers to take action",
     ["Guarantee monopoly status to the incumbent operator",
      "Remove all accountability requirements from regulators",
      "Fix the retail prices of every regulated service"]),

    ("Which option best lists the categories of law that bear specifically on the "
     "telecommunications services industry?",
     "Sector-specific telecom law, competition and fair-trading law, and other relevant law such as privacy",
     ["Criminal law, maritime law and constitutional law only",
      "Tax law, employment law and intellectual-property law only",
      "Banking law, insurance law and environmental law only"]),

    ("Provisions enacted by bodies such as ECOWAS or the WTO take force in a member or "
     "signatory country when they are:",
     "Transposed into national law in accordance with treaty obligations",
     ["Published on the regional body's website",
      "Approved by a majority of the country's operators",
      "Adopted automatically without any national action"]),

    ("The framework notes that the function of regulation may be split between two or more "
     "bodies. A risk a country must manage when doing so is that:",
     "Poorly designed division of functions can lead to disagreements and slow decision-making",
     ["A single regulator will inevitably capture the entire market",
      "Operators will be unable to obtain any licence at all",
      "Spectrum will automatically be allocated free of charge"]),

    ("Listed in increasing order of intrusiveness, the styles of regulation are:",
     "Zero regulation, self-regulation, co-regulation, formal regulation",
     ["Formal regulation, co-regulation, self-regulation, zero regulation",
      "Self-regulation, zero regulation, formal regulation, co-regulation",
      "Co-regulation, formal regulation, zero regulation, self-regulation"]),

    ("An industry described as operating under zero regulation is one in which:",
     "Market forces are allowed to work with no external intervention",
     ["A regulator intervenes minutely in daily operations",
      "Firms jointly agree binding rules under a watchdog",
      "Prices are set directly by a government ministry"]),

    ("Self-regulation, in which the players in an industry regulate themselves, tends to be "
     "MOST effective when:",
     "There is a high convergence of interest among the stakeholders",
     ["There are strong commercial conflicts between the players",
      "A single firm dominates and distrusts all the others",
      "The regulator intervenes in every operational decision"]),

    ("A frequently cited benefit of self-regulation is that:",
     "Companies usually understand their own businesses better than an external regulator does",
     ["It removes all costs of regulation from consumers and industry",
      "It guarantees that no company will ever act opportunistically",
      "It eliminates the need for any underlying legislation"]),

    ("Co-regulation is best described as an arrangement in which:",
     "The regulator joins industry players in a joint forum rather than regulating purely from outside",
     ["Firms operate with no oversight of any kind",
      "The regulator dictates every technical and pricing decision",
      "A foreign body assumes all regulatory authority"]),

    ("While potentially very successful, co-regulation is particularly vulnerable to:",
     "Role ambiguity and differing perceptions of what each player will do",
     ["An immediate and total loss of all regulatory powers",
      "The automatic capture of the regulator by consumers",
      "A legal prohibition on any form of industry collaboration"]),

    ("Regulation is described as intrusive when the regulator:",
     "Intervenes often and minutely in the day-to-day running of a company's business",
     ["Lays down only general principles and leaves methods to firms",
      "Withdraws entirely and lets market forces operate",
      "Limits itself to publishing non-binding guidelines"]),

    ("One reason intrusive regulation is considered undesirable is that:",
     "The regulator effectively becomes a proxy manager of the industry, weakening operators' freedom",
     ["It always reduces the total cost of administering regulation",
      "It guarantees that competitive market forces will prevail",
      "It removes the regulator's responsibility for outcomes"]),

    ("A good regulator is advised to make regulation pervasive rather than intrusive. This "
     "means regulation should:",
     "Influence operators broadly while letting them manage their own affairs within the spirit of the rules",
     ["Dictate the precise technical solution for every operator",
      "Have as little impact as possible on companies in the market",
      "Apply to only a single dominant operator at a time"]),

    ("The main instruments through which regulation is accomplished include authorizations, "
     "rules, determinations, consents and:",
     "Guidelines",
     ["Share buy-backs",
      "Spectrum auctions",
      "Corporate tax assessments"]),

    ("A system of authorization may issue specific authorizations and general authorizations. "
     "These correspond respectively to:",
     "Individual operator licences and class licences",
     ["Spectrum licences and numbering plans",
      "Price caps and interconnection orders",
      "Consents and determinations"]),

    ("Determinations are instruments of ongoing regulation that, in effect:",
     "Elaborate the rules, for example in the periodic review of price controls",
     ["Permanently revoke an operator's licence without appeal",
      "Replace the underlying legislation entirely",
      "Carry no legal force and are merely advisory"]),

    ("A consent is best understood as:",
     "A negative determination that formally relieves an operator from complying with a requirement",
     ["An order that imposes an additional obligation on an operator",
      "An informal guideline that carries no legal status",
      "A penalty levied for breach of a licence condition"]),

    ("Guidelines differ from rules and determinations in that guidelines:",
     "Do not in themselves possess legal status and are usually written in user-friendly language",
     ["Have greater legal force than the licence conditions themselves",
      "Can be issued only by the courts after a successful appeal",
      "Automatically revoke a licence the moment they are breached"]),

    ("A key reason regulators consult widely before finalising instruments is that "
     "consultation:",
     "Gives industry ownership and pre-knowledge of decisions and enriches decision-making",
     ["Transfers formal decision-making power to the consulted parties",
      "Removes the regulator's obligation to justify its decisions",
      "Guarantees that no party will ever appeal the outcome"]),

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
     ["Operators are legally barred from contributing any funds",
      "Regulators are funded solely by fines collected from consumers",
      "Funding comes entirely from international donor agencies"]),

    ("The concept of regulatory hazard refers to the fact that:",
     "Regulatory power, if exercised unwisely, can distort markets and damage the industry it serves",
     ["Regulators are physically endangered when inspecting networks",
      "Regulation always removes all risk from the telecom market",
      "Operators face no consequences for breaching the rules"]),

    ("Regulatory capture occurs when:",
     "The regulator identifies too closely with, and so serves the interests of, the industry it regulates",
     ["The regulator becomes paralysed and issues no decisions at all",
      "Operators are captured and run directly by the regulator",
      "Consumers take over the day-to-day running of the regulator"]),

    ("The information asymmetry, or knowledge gap, that regulators face arises because:",
     "The companies being regulated usually know far more about the business than the regulator does",
     ["Regulators are legally forbidden from collecting any data",
      "Consumers deliberately conceal their preferences from the regulator",
      "Operators are required to share none of their financial records"]),
]

# ---------------------------------------------------------------------------
# SET 4 - Licensing, Scarce Resources & Interconnection  (TE 462)
# ---------------------------------------------------------------------------
SET4 = [
    ("Regulators issue licences to companies primarily to authorise them to:",
     "Operate telecommunications networks and provide telecommunications services",
     ["Manufacture and export telecommunications equipment",
      "Set the national monetary policy for the sector",
      "Audit the financial accounts of rival operators"]),

    ("Beyond granting permission to operate, a telecommunications licence characteristically "
     "specifies:",
     "What facilities a company may deploy, what services it may offer, and how it must interact with other businesses",
     ["The retail prices that every other operator must charge",
      "The internal staffing structure of the regulator itself",
      "The personal tax obligations of the company's directors"]),

    ("In addition to facilities and services, major licences may govern access to scarce "
     "resources such as spectrum and numbers, and commonly require companies to pay:",
     "Upfront fees when the licence is awarded and annual payments thereafter",
     ["A fixed share of profits to every competing operator",
      "Nothing, since licences are always granted free of charge",
      "A one-time deposit that is fully refunded on expiry"]),

    ("Historically, telecom licences were allocated separately for different sub-markets, for "
     "example fixed networks, mobile networks or paging. The main characteristic of this "
     "approach was that licences:",
     "Differentiated between specific technologies and services",
     ["Were technology- and service-neutral by design",
      "Imposed identical terms across every market segment",
      "Were never tied to any particular type of service"]),

    ("Recent technological convergence, which lets different platforms deliver a wider range "
     "of services, has prompted some regulators to move toward:",
     "Technology- and service-neutral licensing",
     ["Stricter technology-specific licensing for each platform",
      "The complete abolition of all forms of licensing",
      "Permanent exclusive licences for incumbent operators"]),

    ("A technology-neutral licence to provide a telephone service is one that:",
     "Lets the company choose whether to use a fixed network or a particular wireless technology",
     ["Requires the company to use a specified fixed-line technology",
      "Forbids the company from offering any voice service at all",
      "Mandates a single government-approved equipment vendor"]),

    ("The two main types of licence awarded to telecom companies are:",
     "Individual operator licences and class licences (general authorizations)",
     ["Spectrum licences and numbering licences",
      "Import licences and export licences",
      "Provisional licences and probationary licences"]),

    ("Individual operator licences are used primarily where:",
     "The number of licences is limited, dominance is likely, or specific resources such as spectrum must be allocated",
     ["The market segment has unlimited room for new entrants",
      "No scarce resources of any kind are involved",
      "Identical terms are wanted for every business in the segment"]),

    ("Class licences (general authorizations) are characterised by the fact that they:",
     "Set out identical terms of operation for all businesses in a market segment, such as ISPs",
     ["Are tailored individually to one named operator",
      "Are reserved exclusively for the incumbent operator",
      "Apply only where radio spectrum must be allocated"]),

    ("A current trend favours replacing individual operator licences with general "
     "authorizations wherever possible because doing so:",
     "Simplifies regulation, helps ensure a level playing field, and is more flexible to market change",
     ["Maximises the upfront revenue collected from each operator",
      "Guarantees the incumbent a protected monopoly position",
      "Eliminates the need for any regulator in the sector"]),

    ("One licensing objective treats basic telecommunications as an essential public service. "
     "This justifies:",
     "Retaining some controls to ensure services are provided in the public interest",
     ["Removing all oversight once the market is privatised",
      "Reserving service provision for a single state monopoly forever",
      "Allowing operators to serve only the most profitable customers"]),

    ("Network roll-out and service-coverage obligations are often written into licences to "
     "advance which licensing objective?",
     "Expansion of networks and services, and universal service",
     ["Generation of one-time government auction revenue",
      "Protection of the incumbent from any competition",
      "Standardisation of company accounting practices"]),

    ("When a state-owned incumbent is privatized, a licence is necessary because it:",
     "Specifies what the investor is buying and what the government expects from the operator",
     ["Transfers ownership of the regulator to the investor",
      "Guarantees the investor permanent freedom from regulation",
      "Removes the operator's obligation to serve any customers"]),

    ("Licensing can be used to regulate market structure, most directly by:",
     "Determining the number of operators licensed to provide services",
     ["Fixing the wholesale price of every network input",
      "Setting the wages paid to operators' employees",
      "Selecting the equipment vendors operators must use"]),

    ("Licence conditions intended to create a level playing field and limit incumbents' abuse "
     "of dominance are generally referred to as:",
     "Anti-competitive safeguards or fair-trading conditions",
     ["Universal-service obligations",
      "Spectrum-refarming provisions",
      "Tariff-rebalancing schedules"]),

    ("Finite resources such as radio spectrum, numbers and rights of way should, as a "
     "licensing objective, be allocated:",
     "Between operators fairly, efficiently and in the public interest",
     ["Entirely to the operator with the longest history",
      "On a first-come basis with no regard to efficiency",
      "Only to operators owned by the national government"]),

    ("Licensing can generate government revenue in two characteristic ways:",
     "One-time revenues from auctions and continuing revenue from annual licence fees",
     ["Confiscation of operator profits and seizure of their assets",
      "Personal income taxes levied on the regulator's own staff",
      "Mandatory donations collected from international agencies"]),

    ("Consumer-protection conditions in telecom licences commonly address matters such as:",
     "Billing practices, complaint mechanisms and mandatory services like emergency calls",
     ["The internal share structure of the operator",
      "The personal credit ratings of company directors",
      "The choice of the regulator's external auditors"]),

    ("By clearly defining the rights and obligations of the operator and the regulator, a "
     "licence advances the objective of:",
     "Regulatory certainty, which builds confidence and helps attract investment",
     ["Spectrum refarming across competing operators",
      "Eliminating the regulator's discretion entirely",
      "Guaranteeing every operator an equal market share"]),

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
     ["There are physically only a few thousand digits in existence",
      "Each number requires its own dedicated radio frequency",
      "A given number can be used by only one country worldwide"]),

    ("Number portability is a mechanism by which:",
     "The subscriber, rather than the operator, owns the number and can take it when switching providers",
     ["The operator permanently owns every number it issues",
      "Numbers are auctioned to the highest-bidding operator",
      "Subscribers must change numbers each time they switch providers"]),

    ("In allocating spectrum, a regulator may auction it to the highest bidder or allocate it "
     "at low cost. Allocating spectrum at low cost is typically intended to:",
     "Reduce prices or encourage the rollout of new services",
     ["Maximise the one-time revenue collected by the government",
      "Guarantee that only one operator can ever use the band",
      "Remove the need to manage interference between users"]),

    ("A primary reason spectrum must be allocated through agreements such as licences, rather "
     "than used freely, is to:",
     "Ensure it is properly distributed and that users do not interfere with one another",
     ["Increase the number of digits available for telephone numbers",
      "Allow every operator to broadcast on any frequency it wishes",
      "Remove the need for any international coordination of frequencies"]),

    ("The core principle of interconnection is that:",
     "Everyone should be able to communicate with everyone else, regardless of which network they subscribe to",
     ["Each operator should keep its subscribers isolated from rivals' networks",
      "Only operators of an equal size are required to interconnect",
      "Interconnection is required only between international carriers"]),
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
