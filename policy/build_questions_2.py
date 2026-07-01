#!/usr/bin/env python3
"""
Build the Telecommunications Policy & Regulation MCQ bank — Part 2.

Source material (same slide decks as Part 1):
  - TE 452 - 1&2.pdf  (Background to regulation; Overview of telecom regulation)
  - TE 462 - Framework for Regulation.pdf
  - TE 462 - Licensing Telecommunication Services.pdf

Each question is (question_text, correct_answer, [distractor, distractor, distractor]).
Output JSON: compiled_2.json
"""
import json
import random

# ---------------------------------------------------------------------------
# SET 5 - Market Economics & Fundamentals (Part 2)  (TE 452)
# ---------------------------------------------------------------------------
SET5 = [
    ("When the price of a mobile voice call rises by 10 percent and, as a result, the "
     "demand for SMS messages increases by 15 percent, the cross-price elasticity of "
     "demand between calls and SMS is positive. This indicates the two services are:",
     "Substitute goods — consumers switch from calls to SMS as calls become more expensive",
     ["Complementary goods — consumers buy more of both when the price of calls rises",
      "Independent goods — the demand for SMS is unrelated to the price of calls",
      "Inferior goods — the demand for SMS falls as consumer incomes rise"]),

    ("When consumer incomes rise by 10 percent and demand for broadband services rises "
     "by 18 percent, the income elasticity of demand for broadband is greater than one. "
     "This classifies broadband as:",
     "A luxury (income-elastic) good, whose demand rises proportionally faster than income",
     ["A necessity (income-inelastic) good, whose demand barely changes with income",
      "An inferior good, whose demand falls as income rises",
      "A Giffen good, whose demand rises as its own price rises"]),

    ("In a competitive telecom market, consumer surplus represents:",
     "The difference between what consumers are willing to pay for a service and what they actually pay",
     ["The extra profit that a firm earns by charging a price above its costs",
      "The reduction in quantity demanded caused by a price increase",
      "The share of tax burden borne by consumers after a new excise tax"]),

    ("When a monopolist restricts output below the socially efficient level and raises "
     "the price, the economic loss to society compared with the competitive outcome "
     "is called:",
     "Deadweight loss",
     ["Consumer surplus",
      "Producer surplus",
      "Tax incidence"]),

    ("A mobile platform operator charges low prices to consumers to attract a large user "
     "base, and then charges higher prices to businesses that wish to reach those consumers "
     "through advertising or app stores. This business model is characteristic of:",
     "A two-sided (or multi-sided) market, where the platform intermediates two distinct customer groups",
     ["A perfectly competitive market where all firms charge the same price",
      "A natural monopoly that must be regulated to prevent excessive pricing",
      "A command economy where the state sets prices for different groups"]),

    ("A social messaging application becomes more valuable to each new user as more people "
     "already use it, because more connections are possible. Economists call this phenomenon:",
     "A positive network externality (or network effect)",
     ["A negative externality, where each new user imposes costs on existing users",
      "Economies of scale, where average costs fall as output rises",
      "Price discrimination, where different users are charged different prices"]),

    ("A mobile subscriber who has accumulated loyalty points, contacts stored in a "
     "proprietary format, and a memorable number that cannot be easily ported faces "
     "high switching costs. High switching costs benefit the incumbent operator primarily by:",
     "Reducing the competitive pressure it faces, since subscribers find it costly to move to rivals",
     ["Lowering the average cost of serving each subscriber",
      "Increasing the incentive for new firms to enter the market",
      "Automatically transferring subscribers to competing networks"]),

    ("A fixed-line operator has laid fibre-optic cable across an entire city. This "
     "investment is largely non-recoverable if the operator exits the market. "
     "Such costs are termed:",
     "Sunk costs",
     ["Variable costs, which change with the volume of traffic carried",
      "Opportunity costs, which represent the next-best foregone alternative",
      "External costs, which are imposed on parties outside the transaction"]),

    ("A firm whose average cost per subscriber falls steadily as it adds more subscribers "
     "is said to exhibit:",
     "Economies of scale",
     ["Diseconomies of scale, where average cost rises as output increases",
      "Constant returns to scale, where average cost does not change with output",
      "Diminishing marginal utility, where each extra unit provides less satisfaction"]),

    ("In a contestable market, even a single firm may price competitively because:",
     "The threat of potential entry by rivals constrains the incumbent from raising prices above competitive levels",
     ["The government fixes prices at the competitive level by decree",
      "The incumbent voluntarily limits profits out of social responsibility",
      "Sunk costs are so high that entry and exit are both impossible"]),

    ("A telecommunications firm that charges each customer exactly their maximum "
     "willingness to pay, thereby extracting all consumer surplus, is practising:",
     "First-degree (or perfect) price discrimination",
     ["Second-degree price discrimination, where prices vary by volume consumed",
      "Third-degree price discrimination, where prices vary by customer group",
      "Predatory pricing, where prices are set below cost to drive rivals out"]),

    ("A mobile operator offers the same data plan at one price to residential customers "
     "and a lower price to students, based on the observation that students are more "
     "price-sensitive. This is an example of:",
     "Third-degree price discrimination, segmenting customers by group elasticity",
     ["First-degree price discrimination, where each buyer pays their unique reservation price",
      "Second-degree price discrimination, where prices depend on quantity purchased",
      "Uniform pricing, because the plan content is identical"]),

    ("A broadband provider charges subscribers a fixed monthly access fee and then an "
     "additional per-gigabyte usage charge on top. This pricing structure is called:",
     "A two-part tariff",
     ["A flat rate, where a single monthly fee covers all usage",
      "Predatory pricing, aimed at driving rivals from the market",
      "Resale pricing, where the provider buys wholesale and marks up the price"]),

    ("The Lerner index measures market power as (Price minus Marginal Cost) divided by "
     "Price. A Lerner index of zero indicates:",
     "No market power — the firm is pricing at marginal cost, consistent with perfect competition",
     ["Maximum market power — the firm is pricing infinitely above marginal cost",
      "A natural monopoly — only one efficient firm can serve the market",
      "Government pricing — prices are set by regulatory decree"]),

    ("Allocative efficiency in a market is achieved when:",
     "Goods and services are produced in the quantities that consumers value them, at prices that reflect true costs",
     ["A single firm is large enough to minimise average cost",
      "All producers use the most technically advanced equipment available",
      "The government controls the price of every product in the economy"]),

    ("An operator is productively efficient when it:",
     "Produces its output at the lowest possible cost, given current technology and input prices",
     ["Sets its prices equal to those charged by its nearest competitor",
      "Allocates its output in proportion to the incomes of its customers",
      "Earns a rate of return exactly equal to the market rate of interest"]),

    ("A regulatory policy that sacrifices short-term competition concerns in order to "
     "encourage investment in next-generation infrastructure is prioritising:",
     "Dynamic efficiency — the ability of the market to innovate and improve over time",
     ["Allocative efficiency — matching quantities produced to consumer preferences",
      "Productive efficiency — minimising the cost of current output",
      "Regulatory capture — the regulator acting in the interest of the regulated firm"]),

    ("A mobile market with three operators, each aware that its pricing decisions will "
     "provoke a response from the other two, is best described as an:",
     "Oligopoly",
     ["Perfect competition, where no single firm influences price",
      "Natural monopoly, where a single firm serves the whole market at least cost",
      "Monopsony, where a single buyer faces many sellers"]),

    ("An incumbent operator temporarily prices a service below its cost of provision "
     "with the intention of forcing a new entrant out of the market, after which it "
     "plans to raise prices. This behaviour is known as:",
     "Predatory pricing",
     ["Penetration pricing, aimed at legitimately building market share",
      "Marginal cost pricing, required of regulated dominant firms",
      "Price discrimination, charging different buyers different prices"]),

    ("A telecom operator sells broadband, mobile and television services together at a "
     "combined price lower than the sum of their individual prices, requiring customers "
     "to subscribe to all three. This commercial strategy is called:",
     "Bundling",
     ["Disaggregated resale, where services are sold separately at wholesale",
      "Co-location, where competitors share the operator's physical infrastructure",
      "Resale, where an operator buys wholesale services and retails them"]),

    ("Regulators use the Herfindahl-Hirschman Index (HHI) to measure market "
     "concentration. An HHI approaching 10,000 indicates:",
     "A highly concentrated market approaching a single-firm monopoly",
     ["A perfectly competitive market with many equal-sized firms",
      "A market in which the two largest firms each hold exactly 50% of shares",
      "A market too fragmented to warrant any regulatory oversight"]),

    ("In mobile markets, spectrum licences granted to a limited number of operators "
     "create a barrier to entry because:",
     "A new firm cannot launch a mobile network without spectrum, which is scarce and tightly regulated",
     ["Spectrum licences automatically grant the holder a permanent monopoly",
      "Any firm may use spectrum freely once it registers with the ITU",
      "Spectrum is an unlimited resource that requires no management"]),

    ("Under rate-of-return regulation the regulator sets the allowed profit level, "
     "while under price-cap regulation it sets a ceiling on prices. A main advantage "
     "of price-cap regulation over rate-of-return is that it:",
     "Gives the firm an incentive to cut costs, since it keeps any efficiency gains as extra profit",
     ["Guarantees that the firm will always earn at least its cost of capital",
      "Eliminates the need for the regulator to collect any financial data",
      "Prevents any variation in prices, providing consumers with certainty"]),

    ("A mobile operator that also owns the towers its competitors must use is said to "
     "be vertically integrated. A regulatory concern with vertical integration is that "
     "the firm may:",
     "Favour its own downstream retail operations by providing rivals with degraded or overpriced access to the towers",
     ["Be unable to price its retail services competitively without subsidies",
      "Automatically reduce the quality of its own retail services",
      "Lose all market power once it becomes vertically integrated"]),

    ("Economic theory defines a public good as one that is non-rival and non-excludable. "
     "A broadcast radio signal most closely resembles:",
     "A public good",
     ["A private good, because the broadcaster can charge for each listener",
      "A club good, because it is non-rival but perfectly excludable",
      "A common resource, because use by one person diminishes supply for others"]),
]

# ---------------------------------------------------------------------------
# SET 6 - Sector Reform & Regulatory Foundations (Part 2)  (TE 452)
# ---------------------------------------------------------------------------
SET6 = [
    ("Structural separation in a telecom market means:",
     "The monopoly infrastructure (such as the local loop) is owned by a separate company from the retail service providers that use it",
     ["The regulator divides its own functions into separate departments",
      "Competing operators are required to share their customer databases",
      "The government privatises the incumbent by selling shares to the public"]),

    ("Accounting separation requires a vertically integrated operator to:",
     "Keep separate financial accounts for its wholesale network and its retail service divisions, as though they were independent entities",
     ["Physically split its wholesale and retail operations into separate companies",
      "Share its full financial accounts freely with all rival operators",
      "File identical financial statements for every country in which it operates"]),

    ("A universal service obligation (USO) in telecommunications is best defined as:",
     "A regulatory requirement that certain basic services are made available to all citizens at an affordable price, regardless of location",
     ["A requirement that every operator offer every service it provides for free",
      "An international treaty that prevents any country from restricting telecoms",
      "A licence condition that prohibits dominant firms from raising prices"]),

    ("When the provision of universal service is commercially unviable in high-cost "
     "rural areas, regulators commonly establish:",
     "A universal service fund financed by levies on operators in proportion to their revenues",
     ["A price floor that prevents operators from discounting in profitable areas",
      "A transfer of spectrum rights from profitable to unprofitable operators",
      "A legal obligation for consumers to subsidise rural providers directly"]),

    ("Market failure due to information asymmetry occurs when:",
     "One side of a market has substantially more information than the other, preventing efficient transactions",
     ["Both buyers and sellers have identical information about product quality",
      "The government has more information than the market about optimal quantities",
      "A firm has lower costs than its rivals due to proprietary technology"]),

    ("A positive externality exists when:",
     "A transaction between a buyer and seller generates benefits for third parties who are not part of the transaction",
     ["A firm imposes costs on society that it does not itself bear",
      "A government tax corrects an over-supply of a harmful good",
      "A monopoly charges a price above the competitive market price"]),

    ("Ex-ante regulation differs from ex-post regulation in that ex-ante:",
     "Rules are set in advance to shape market behaviour before problems arise, rather than reacting to them after the fact",
     ["Intervention occurs only after a breach has been detected and proven",
      "Regulators rely exclusively on competition law rather than sector-specific rules",
      "Firms are free to set their own terms until a complaint is received"]),

    ("An operator designated as having Significant Market Power (SMP) is one that:",
     "Enjoys a position of economic strength that allows it to behave to an appreciable extent independently of competitors, customers and consumers",
     ["Holds a licence for fewer than five years",
      "Has annual revenues below the national regulatory authority's threshold",
      "Operates exclusively in rural areas with no urban competition"]),

    ("Before assessing whether an operator has SMP, a regulator must first define the "
     "relevant market. The relevant product market is defined as:",
     "The smallest set of products that are close enough substitutes to constrain each other's prices",
     ["All products offered by every licensed operator in the country",
      "Products that the regulator decides to regulate for policy reasons",
      "The services covered by the dominant operator's individual licence"]),

    ("A 'bottleneck' facility in telecommunications is one that:",
     "Is essential for reaching end customers, and which competitors cannot duplicate economically, giving the owner market power",
     ["Is located at the geographic centre of the national network",
      "Can only be used by the incumbent operator under its licence terms",
      "Is shared voluntarily by all operators under a co-regulation agreement"]),

    ("Local loop unbundling (LLU) allows:",
     "Alternative operators to rent the physical copper or fibre pair between the exchange and a customer's premises from the incumbent, at regulated prices",
     ["The incumbent to use rival operators' transmission equipment free of charge",
      "Consumers to own the physical cable connecting them to the exchange",
      "Operators to resell each other's retail services without owning infrastructure"]),

    ("Tariff rebalancing in the telecom sector typically refers to:",
     "Adjusting prices so that each service covers its cost, reducing cross-subsidies — for instance, raising local call prices and lowering international prices",
     ["Increasing all retail prices uniformly to reflect inflation",
      "Transferring spectrum charges from mobile to fixed-line operators",
      "Setting identical prices for all operators regardless of their cost structures"]),

    ("An operator is likely to retain structural dominance even after market liberalisation "
     "largely because it:",
     "Controls legacy infrastructure (such as the local loop or backhaul) that new entrants cannot easily or economically replicate",
     ["Has already lost most of its subscribers to new entrants",
      "Holds a licence that was issued after market opening",
      "Offers no retail services in the newly competitive market"]),

    ("A regulatory impact assessment (RIA) is designed to:",
     "Estimate the costs and benefits of a proposed regulatory intervention before it is implemented, to ensure its net effect is positive",
     ["Audit the financial accounts of a regulated company after a breach",
      "Determine the fine to impose on an operator found guilty of market abuse",
      "Replace the consultation process with a written report"]),

    ("A light-touch regulatory approach is typically characterised by:",
     "Minimal intervention, with the regulator stepping in only when there is clear market failure or a specific complaint",
     ["Detailed prescriptive rules governing every aspect of operator behaviour",
      "Nationalisation of the dominant operator to prevent price abuses",
      "Prohibiting competition in order to protect the natural monopoly"]),

    ("Functional separation requires a dominant operator to:",
     "Operate its wholesale access network as a functionally separate business unit with independent management and systems, even if ownership remains unified",
     ["Sell its network infrastructure to an independent company",
      "Provide identical prices to retail rivals and its own retail division before separation",
      "Establish a separate universal service fund from its own revenues"]),

    ("The main argument in favour of infrastructure competition (multiple physical "
     "networks) over service competition (multiple retailers on one network) is that it:",
     "Leads to greater dynamic efficiency and innovation as firms compete across multiple layers of the value chain",
     ["Reduces the total cost of building broadband networks across the country",
      "Is always achievable in rural areas where only one network is viable",
      "Eliminates any need for access regulation once networks are built"]),

    ("Regulators have intervened in international roaming markets because:",
     "Roaming charges were often far above cost, exploiting consumers who had no practical ability to switch provider while abroad",
     ["Roaming agreements between operators are prohibited under the WTO BTA",
      "The ITU requires all international calls to be routed through a single hub",
      "Consumer demand for roaming was too low to justify commercial provision"]),

    ("When a regulator performs a cost-benefit analysis of a proposed remedy, it should "
     "compare:",
     "The direct costs imposed on industry and consumers against the economic benefits of correcting the market failure",
     ["The regulator's own administrative budget against the revenue of the dominant operator",
      "The income of rural subscribers against that of urban subscribers",
      "The current market share of each operator against the national average"]),

    ("A multi-sector regulator that oversees telecoms, energy and water simultaneously "
     "may have the advantage of:",
     "Applying consistent regulatory principles across sectors and avoiding conflicts between sector-specific agencies",
     ["Focusing exclusive expertise on a single industry's unique characteristics",
      "Having a larger staff available to investigate each individual complaint",
      "Operating independently of government in a way sector-specific bodies cannot"]),

    ("When two large mobile operators propose to merge, reducing the number of national "
     "operators from four to three, the regulator's primary competition concern is "
     "likely to be:",
     "A reduction in competitive pressure that could lead to higher prices or lower investment",
     ["An immediate increase in spectrum costs for the merged entity",
      "A risk that the merged entity will be unable to recover its licence costs",
      "A requirement that the smaller merged operator buy out the regulator"]),

    ("The main advantage of sector-specific telecom regulation over reliance on general "
     "competition law is that:",
     "Sector-specific rules can be calibrated to the industry's technical characteristics and applied proactively, without waiting for a market abuse to occur",
     ["Competition law always reaches the same outcome as sector regulation",
      "Sector regulation is more flexible because it has no prescribed rules",
      "Competition authorities are forbidden from intervening in telecom markets"]),

    ("Asymmetric regulation imposes obligations on the dominant operator that are not "
     "applied to smaller rivals. The justification for this asymmetry is that:",
     "Only the dominant operator has the market power to harm competition or consumers in ways that the market itself cannot correct",
     ["Smaller operators are better managed and therefore need fewer rules",
      "All operators should be regulated equally regardless of their market share",
      "Asymmetric regulation is required by the WTO Reference Paper in all cases"]),

    ("Periodic market reviews, in which the regulator reassesses which operators have "
     "SMP and what remedies apply, serve primarily to:",
     "Ensure that regulatory obligations remain proportionate as market conditions evolve, and are removed when no longer needed",
     ["Permanently increase the obligations placed on all operators over time",
      "Allow the regulator to raise additional licence fees from dominant operators",
      "Transfer ownership of the incumbent to the state if competition fails"]),

    ("Regulatory forbearance occurs when a regulator:",
     "Deliberately refrains from exercising its available powers in a market, on the grounds that competition is sufficient",
     ["Fails to apply its regulations due to administrative error or under-resourcing",
      "Is prevented from intervening by a court injunction from the operator",
      "Increases the stringency of regulation in response to market conditions"]),
]

# ---------------------------------------------------------------------------
# SET 7 - Framework for Regulation (Part 2)  (TE 462)
# ---------------------------------------------------------------------------
SET7 = [
    ("Regulatory independence from the regulated industry encompasses institutional, "
     "financial and operational dimensions. Which dimension is concerned with ensuring "
     "regulators are not housed within the same organisation as operators?",
     "Institutional independence",
     ["Financial independence",
      "Operational independence",
      "Political independence"]),

    ("A key risk where the regulator's annual budget is set entirely at the government's "
     "discretion is that:",
     "The regulator may be starved of resources as an indirect way of constraining its activity",
     ["The regulator will over-spend on enforcement against politically connected firms",
      "Operators will demand to audit the regulator's accounts directly",
      "The regulator will become independent of both government and operators"]),

    ("Which of the following is a mechanism that makes a regulator accountable without "
     "compromising its independence?",
     "A requirement to publish an annual report explaining its decisions to the legislature and public",
     ["Allowing the minister to reverse any decision the regulator makes",
      "Requiring the regulated operator to sign off on all regulatory decisions",
      "Permitting the regulator to operate without any published criteria"]),

    ("Transparency in regulation requires that:",
     "The criteria, process and reasoning behind regulatory decisions are publicly available so that affected parties can understand and challenge them",
     ["All correspondence between the regulator and operators be kept confidential",
      "The regulator shares only its final decisions, without publishing its reasoning",
      "Consultation documents are circulated only to the dominant operator"]),

    ("Regulatory certainty is valued by investors primarily because:",
     "Predictable rules reduce the risk premium they require when committing long-term capital to network infrastructure",
     ["Certain rules always lead to lower retail prices for consumers",
      "Certainty prevents any operator from ever entering or exiting the market",
      "Certain rules eliminate the need for any formal licencing process"]),

    ("Under RPI-X price-cap regulation, if RPI is the retail price index and X is an "
     "efficiency factor, operators are required to:",
     "Reduce their regulated prices in real terms by X per cent per year, passing efficiency gains to consumers",
     ["Increase their prices by RPI each year regardless of their own cost savings",
      "Keep prices fixed in nominal terms regardless of inflation",
      "Set prices at exactly the rate of inflation minus any government subsidy"]),

    ("A high X factor in a price-cap formula (RPI-X) implies:",
     "The regulator expects the operator to achieve large efficiency savings and requires it to pass them on to consumers quickly",
     ["The regulator expects the market to become less competitive over time",
      "The operator will receive a subsidy equal to X per cent of its revenues",
      "The price cap will be removed once X years of regulation have passed"]),

    ("A well-known drawback of rate-of-return (RoR) regulation is that it may create "
     "an incentive for the regulated firm to:",
     "Over-invest in capital (the Averch-Johnson effect), because profit is calculated as a percentage of the asset base",
     ["Under-invest entirely to avoid regulatory scrutiny",
      "Reduce prices below cost in order to drive rivals out of the market",
      "Resist any technological change that would require new capital spending"]),

    ("A licence condition requiring a mobile operator to achieve a minimum 95 percent "
     "population coverage and a maximum 2-second call-setup delay is an example of:",
     "Quality-of-service (QoS) regulation imposing minimum performance standards",
     ["Price-cap regulation limiting how much the operator may charge",
      "Accounting separation requiring separate financial records",
      "Structural separation requiring distinct ownership of the access network"]),

    ("A regulator that requires a dominant operator to submit annual regulatory accounts "
     "broken down by network element cost, retail revenue and margin is using:",
     "Accounting separation to improve cost transparency and detect potential cross-subsidies",
     ["Structural separation to require two legally distinct companies",
      "A price-cap review to determine the new X factor",
      "A market review to define the relevant product market"]),

    ("A regulatory sandbox allows:",
     "Firms to test innovative products or business models in a controlled environment with relaxed rules, subject to safeguards",
     ["Operators to exclude themselves from all regulation for a set period",
      "Governments to test new regulatory agencies before formally establishing them",
      "Regulators to impose higher fines than the law would normally permit"]),

    ("A sunset clause in a regulatory instrument provides that:",
     "The regulation automatically expires after a set time unless the regulator actively decides to renew it",
     ["The regulated firm must upgrade its network before a specified deadline",
      "The regulator must resign once its five-year term of office ends",
      "Obligations are phased in gradually over a multi-year period"]),

    ("During a periodic market review, if the regulator finds that effective competition "
     "has developed and the dominant operator no longer has SMP, the appropriate "
     "response is to:",
     "Remove or relax the sector-specific obligations previously imposed on that operator",
     ["Impose stricter conditions to safeguard the competition that has emerged",
      "Transfer the operator's spectrum to a state-owned entity",
      "Launch a formal inquiry to determine whether re-nationalisation is needed"]),

    ("When an interconnection agreement cannot be reached through commercial negotiation, "
     "most regulatory frameworks allow either party to:",
     "Refer the dispute to the regulator for binding arbitration or determination",
     ["Withdraw services to the rival operator until an agreement is reached",
      "Seek damages from the rival's shareholders in a consumer court",
      "Delay interconnection indefinitely without incurring any penalty"]),

    ("Regulatory risk, from the perspective of an investor in telecoms infrastructure, "
     "refers to:",
     "The risk that the regulator will change the rules in ways that reduce the expected return on invested capital",
     ["The physical risk that network equipment will be damaged by extreme weather",
      "The risk that subscribers will switch operators when new services are launched",
      "The risk that competition law will prohibit the operator from charging cost-based prices"]),

    ("Monitoring and enforcement are distinct regulatory activities. Monitoring is "
     "primarily concerned with:",
     "Collecting data and tracking compliance with regulatory obligations before a breach has occurred",
     ["Imposing fines and penalties on firms that have already breached their licences",
      "Deciding what obligations to impose on operators in the first place",
      "Publishing annual reports on the regulator's own financial performance"]),

    ("A regulator that responds to a minor licence breach with an informal warning, "
     "escalating to a formal compliance notice and then a fine if the breach persists, "
     "is applying:",
     "A graduated (or proportionate) enforcement approach",
     ["Regulatory capture, whereby the regulator avoids penalising the industry",
      "Co-regulation, where the industry jointly decides on the appropriate penalty",
      "Zero regulation, since no immediate fine is imposed on the first breach"]),

    ("A voluntary code of practice adopted by operators without legislative force "
     "serves primarily to:",
     "Establish baseline standards of consumer treatment that operators commit to publicly, creating reputational incentives for compliance",
     ["Replace all formal licence conditions with non-binding commitments",
      "Allow the regulator to impose fines for any breach without due process",
      "Transfer regulatory responsibility entirely to the courts"]),

    ("When a regulator proposes a new interconnection pricing methodology, best practice "
     "requires it to publish a consultation document and allow a period for:",
     "Operators, consumers and other interested parties to comment before the methodology is finalised",
     ["The minister to approve the document before it is sent to any operator",
      "The dominant operator to veto any proposals it finds commercially disadvantageous",
      "Courts to pre-approve the methodology as legally valid before publication"]),

    ("In developing economies, one frequently cited obstacle to effective regulation is:",
     "The knowledge and information gap between the regulator and the companies it regulates, due to limited technical and financial expertise in the regulatory body",
     ["An excess of regulatory staff who impose unnecessary burdens on operators",
      "The refusal of incumbent operators to obey the law under any circumstances",
      "The absence of any legislation enabling the creation of a regulatory body"]),

    ("Why are licence conditions a particularly powerful regulatory instrument compared "
     "with general guidelines?",
     "Because they are legally binding on the licence holder and breach can result in enforcement action or licence revocation",
     ["Because guidelines are published only after a court order, while licences are quicker",
      "Because licence conditions apply to all firms in every sector of the economy",
      "Because guidelines must be approved by the ITU, whereas licences do not"]),

    ("A regulatory requirement for operators to maintain a formal written complaint "
     "procedure and respond within a set number of days is designed to:",
     "Ensure consumers have an accessible redress mechanism and operators take service quality seriously",
     ["Prevent consumers from taking complaints directly to a court or tribunal",
      "Transfer consumer protection responsibilities from the regulator to the operator",
      "Allow the operator to charge consumers for the processing of complaints"]),

    ("Regulators in smaller markets often benchmark their rules and tariff levels against "
     "those in comparable countries. The primary purpose of such benchmarking is to:",
     "Draw on evidence from multiple markets to set well-informed, defensible regulatory parameters in the absence of sufficient domestic data",
     ["Copy the rules of the largest economy regardless of local market conditions",
      "Replace the national consultation process with an international one",
      "Allow operators to choose which country's regulatory framework they prefer"]),

    ("In most countries, the telecommunications regulatory framework assigns the "
     "legislature (parliament) the role of:",
     "Enacting the primary legislation that establishes the regulatory body and confers its powers",
     ["Setting wholesale interconnection prices on a case-by-case basis",
      "Issuing individual operator licences and managing spectrum allocation",
      "Investigating consumer complaints about billing practices"]),

    ("An independent regulatory authority is often governed by a multi-member board "
     "rather than a single regulator. The main benefit of a board structure is that:",
     "Decisions represent a range of views and are less vulnerable to the bias or capture of any single individual",
     ["A board can issue licences faster because each member signs separately",
      "Board members are personally liable for regulatory decisions, deterring bias",
      "A multi-member board does not require any legislation to establish"]),
]

# ---------------------------------------------------------------------------
# SET 8 - Licensing, Scarce Resources & Interconnection (Part 2)  (TE 462)
# ---------------------------------------------------------------------------
SET8 = [
    ("Spectrum refarming refers to the process of:",
     "Reassigning spectrum bands previously used by one technology (e.g. 2G) to a newer, more spectrally efficient technology (e.g. 4G or 5G)",
     ["Allocating new spectrum bands discovered through satellite observation",
      "Transferring spectrum rights between countries under an ITU agreement",
      "Increasing the MHz available in a band by reducing guard bands"]),

    ("In spectrum secondary trading, spectrum rights are:",
     "Transferred or leased from one licence holder to another through market transactions, subject to regulator approval",
     ["Returned to the government for free reallocation when no longer needed",
      "Auctioned by the ITU to the highest bidder across all member states",
      "Allocated automatically to the operator with the longest network history"]),

    ("Cognitive radio technology enables more efficient spectrum use primarily by:",
     "Allowing devices to sense and opportunistically use spectrum bands that are temporarily idle, without causing harmful interference to primary users",
     ["Physically expanding the radio spectrum by using new frequency ranges",
      "Requiring all operators to share a single licensed frequency band permanently",
      "Replacing licensed spectrum with licence-exempt bands for all services"]),

    ("A regulator may impose spectrum caps (or spectrum limits) on individual operators "
     "in order to:",
     "Prevent any single operator from acquiring so much spectrum that it can disadvantage rivals, particularly in auctions",
     ["Guarantee that each operator holds exactly the same amount of spectrum",
      "Reduce the total amount of spectrum consumed across the country",
      "Allow the incumbent to hold all remaining spectrum after a liberalisation"]),

    ("When a country's radio transmissions could cause interference to services in a "
     "neighbouring country, the coordination process is managed through:",
     "Bilateral and multilateral agreements, guided by the ITU Radio Regulations",
     ["The WTO Basic Telecommunications Agreement",
      "The UN Security Council's telecommunications sub-committee",
      "The National Regulatory Authority acting unilaterally"]),

    ("In the E.164 international numbering plan, a full international telephone number "
     "comprises:",
     "A country code followed by the national (significant) number, with the total not exceeding 15 digits",
     ["A network code followed by a subscriber number, with a minimum of 10 digits",
      "A two-letter country prefix followed by an area code and subscriber number",
      "A six-digit operator code followed by the subscriber's national number"]),

    ("Non-geographic numbers differ from geographic numbers in that they:",
     "Are not tied to a specific physical location, and are used for services such as freephone, premium-rate, or shared-cost calls",
     ["Can only be assigned to mobile subscribers, not to fixed-line operators",
      "Must begin with the international country code of the originating network",
      "Are reserved exclusively for emergency services"]),

    ("A freephone (toll-free) service number is one where:",
     "The cost of the call is borne by the called party (the business) rather than the calling consumer",
     ["Neither the caller nor the called party pays, as the government subsidises the call",
      "The caller pays a higher-than-standard rate which the operator retains",
      "The number is available only to emergency services and hospitals"]),

    ("Premium-rate service numbers expose consumers to the risk of high unintended "
     "charges. A common regulatory response is to:",
     "Require clear price disclosure before the consumer connects and impose a maximum per-minute or per-call cap",
     ["Prohibit the use of premium-rate numbers entirely across the market",
      "Require all premium calls to be paid in advance by the calling consumer",
      "Allow operators to set premium rates without any disclosure obligation"]),

    ("Short codes (e.g. 3- to 6-digit numbers) are administered by national regulators "
     "because:",
     "They are a scarce resource — their brevity limits how many exist — and must be allocated fairly across competing service providers",
     ["Short codes are allocated by the ITU to each country as part of the E.164 plan",
      "Short codes are infinite in supply and require no formal administration",
      "Short codes can only be used by government agencies and regulators"]),

    ("In a standard telephone call, the originating operator is the one that:",
     "Carries the call from the calling subscriber and delivers it to the network of the terminating operator",
     ["Receives the call on behalf of the called subscriber and rings their phone",
      "Issues the number at which the called party is reached",
      "Determines the retail price charged to the called party"]),

    ("Mobile termination rates (MTRs) are regulated in many countries because:",
     "The terminating operator has a monopoly over access to its own subscribers, allowing it to charge above-cost rates to originating operators",
     ["Mobile operators charge subscribers too little for incoming calls",
      "The ITU mandates that MTRs be set at zero in all member states",
      "MTRs are only paid by the government, not by operators"]),

    ("Long-run incremental cost (LRIC) is used as a basis for regulated interconnection "
     "prices because:",
     "It reflects the efficient forward-looking cost of providing the specific service, excluding costs unrelated to the traffic being terminated",
     ["It measures the actual historic cost that the operator has already spent",
      "It guarantees the operator a fixed profit margin on interconnection",
      "It is the model preferred by the WTO for all cross-border interconnection"]),

    ("Retail-minus pricing sets the wholesale access price at:",
     "The incumbent's retail price minus the retail costs (marketing, billing, etc.) it avoids when selling wholesale, ensuring viable retail competition",
     ["A price above the incumbent's retail price to deter competitive entry",
      "Zero, on the basis that access should be provided free of charge",
      "The cost of building a competing network from scratch"]),

    ("Domestic roaming agreements allow a mobile operator to:",
     "Provide services to its subscribers in geographic areas it does not cover, by using the network of another domestic operator",
     ["Offer its subscribers free calls on any international visit to a partner country",
      "Use a foreign operator's spectrum inside national borders permanently",
      "Charge subscribers a lower price when they are in their home region"]),

    ("Regulators impose wholesale roaming caps on visited-network operators. The effect "
     "of a wholesale roaming cap is to:",
     "Limit the price that visited-network operators may charge the home-network operator, which can then pass lower retail prices to travelling subscribers",
     ["Prevent home-network operators from signing any roaming agreements at all",
      "Allow subscribers to use any network freely without operator permission",
      "Set the retail price charged to consumers by the home operator directly"]),

    ("A Mobile Virtual Network Operator (MVNO) differs from a full Mobile Network "
     "Operator (MNO) in that an MVNO:",
     "Does not own radio spectrum or a radio access network, and instead buys wholesale network access from an MNO to sell services to end customers",
     ["Owns spectrum and base stations but does not have a retail customer base",
      "Operates exclusively in rural areas where MNOs have no coverage",
      "Is licensed under a class licence that is not subject to any conditions"]),

    ("Passive infrastructure sharing involves operators sharing:",
     "Physical structures such as towers, masts, ducts and shelters, without sharing the active radio or transmission equipment",
     ["The same radio frequencies and active antennas on a single cell site",
      "Spectrum licences so that both operators transmit on a common band",
      "Customer billing systems and subscriber management platforms"]),

    ("Radio Access Network (RAN) sharing goes beyond passive sharing in that operators "
     "share:",
     "The active radio equipment (antennas, transceivers, controllers) in addition to towers and other physical structures",
     ["Only masts and shelters, not any electronic equipment",
      "Core network elements such as switching and routing infrastructure",
      "Spectrum licences, so all shared-RAN operators use a single frequency band"]),

    ("Net neutrality is the principle that:",
     "Internet service providers must treat all internet traffic equally, without discriminating based on source, destination or content type",
     ["Only neutral parties may operate internet exchange points",
      "Internet providers must offer free access to government websites",
      "Content companies must pay consumers directly for consuming their services"]),

    ("In mobile number portability (MNP), the 'losing' operator is:",
     "The operator from which the subscriber is porting away — the one that currently holds the number",
     ["The operator that is gaining the subscriber who wishes to keep their number",
      "The operator that routes the ported call once the port is complete",
      "The operator that administers the national number portability database"]),

    ("Regulators that set maximum porting timelines (e.g. one working day) do so "
     "primarily to:",
     "Prevent operators from using slow porting processes to discourage subscribers from switching",
     ["Allow operators to complete all technical work before the customer is aware of the port",
      "Ensure that porting requests are always processed in the order received",
      "Limit the number of porting requests an operator must handle per month"]),

    ("A short licence duration (e.g. five years) compared with a long one (e.g. twenty "
     "years) gives the regulator more:",
     "Opportunities to revise the licence conditions as market and technology conditions change",
     ["Certainty for investors who need predictable returns over a longer period",
      "Time before any regulatory review of the operator's conduct is required",
      "Spectrum allocation rights to distribute to new entrants"]),

    ("When renewing a licence, a regulator may attach new or revised conditions. The "
     "main constraint on this power is that:",
     "New conditions must be proportionate, justified by current market circumstances, and the operator must have fair notice and an opportunity to respond",
     ["No new conditions may ever be added to an existing licence once originally granted",
      "Only the ITU may approve conditions added at the time of renewal",
      "The government treasury must approve each new condition for its fiscal impact"]),

    ("A regulatory requirement that all licensed operators connect emergency calls free "
     "of charge, even when a subscriber has no credit, is justified on the basis that:",
     "Emergency call access is a fundamental public interest obligation that overrides commercial pricing considerations",
     ["Emergency calls generate significant revenue that offsets their zero-price status",
      "The WTO BTA prohibits any charge for calls to emergency services",
      "Subscribers who call emergency services are refunded by the government"]),
]

# All 100 Part-2 questions compiled into a single bank.
ALL_QUESTIONS = SET5 + SET6 + SET7 + SET8
OUTPUT_FILE = "compiled_2.json"


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def main():
    rng = random.Random(463)  # different seed from Part 1
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
