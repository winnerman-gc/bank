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
      "An inferior good, whose overall demand actually falls whenever income rises",
      "A Giffen good, whose quantity demanded oddly rises as its own price increases"]),

    ("In a competitive telecom market, consumer surplus represents:",
     "The difference between what consumers are willing to pay for a service and what they actually pay",
     ["The extra profit that a firm earns by charging a price that is well above its own costs",
      "The overall reduction in quantity demanded that is caused by a sudden increase in price",
      "The specific share of the tax burden that is borne by consumers after a new excise tax"]),

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
     ["A perfectly competitive market in which every single firm charges exactly the same price",
      "A natural monopoly that must be tightly regulated in order to prevent excessive pricing",
      "A command economy where the state directly sets prices for different consumer groups"]),

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
     ["Lowering the average operational cost of serving each and every individual subscriber",
      "Increasing the incentive for entirely new firms to aggressively enter the market",
      "Automatically transferring all existing subscribers over to competing rival networks"]),

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
     ["The government directly fixes all market prices at the competitive level by official decree",
      "The incumbent operator voluntarily limits its own profits purely out of social responsibility",
      "Sunk costs throughout the industry are so high that entry and exit are both entirely impossible"]),

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
     ["Maximum market power — the firm is pricing infinitely far above marginal cost",
      "A natural monopoly — only one efficient firm can ever serve the whole market",
      "Government-mandated pricing — all prices are set directly by regulatory decree"]),

    ("Allocative efficiency in a market is achieved when:",
     "Goods and services are produced in the quantities that consumers value them, at prices that reflect true costs",
     ["A single dominant firm is large enough to minimise its own average cost of production",
      "All producers throughout the industry use the most technically advanced equipment available",
      "The government directly controls the price of every single product across the whole economy"]),

    ("An operator is productively efficient when it:",
     "Produces its output at the lowest possible cost, given current technology and input prices",
     ["Sets its retail prices exactly equal to those charged by its nearest competitor",
      "Allocates its output strictly in proportion to the annual incomes of its individual customers",
      "Earns a rate of return that is exactly equal to the prevailing market rate of interest"]),

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
     ["Spectrum licences automatically and permanently grant their holder a legal monopoly",
      "Any firm may use spectrum completely freely once it simply registers with the ITU",
      "Spectrum is generally treated as an unlimited resource that requires no active management"]),

    ("Under rate-of-return regulation the regulator sets the allowed profit level, "
     "while under price-cap regulation it sets a ceiling on prices. A main advantage "
     "of price-cap regulation over rate-of-return is that it:",
     "Gives the firm an incentive to cut costs, since it keeps any efficiency gains as extra profit",
     ["Guarantees that the regulated firm will always earn at least its own cost of capital",
      "Eliminates the need for the regulator to ever collect any detailed financial data",
      "Prevents any variation in prices at all, thereby providing consumers with full certainty"]),

    ("A mobile operator that also owns the towers its competitors must use is said to "
     "be vertically integrated. A regulatory concern with vertical integration is that "
     "the firm may:",
     "Favour its own downstream retail operations by providing rivals with degraded or overpriced access to the towers",
     ["Be entirely unable to price its own retail services competitively without government subsidies",
      "Automatically and permanently reduce the overall quality of all of its own retail services",
      "Automatically lose absolutely all of its market power the moment it becomes vertically integrated"]),

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
     ["The telecom regulator itself formally divides its own internal functions into several entirely separate government departments",
      "All competing operators active in the market are required to fully share their customer databases with one another at all times",
      "The government privatises the incumbent operator by selling off all of its shares directly to members of the general public"]),

    ("Accounting separation requires a vertically integrated operator to:",
     "Keep separate financial accounts for its wholesale network and its retail service divisions, as though they were independent entities",
     ["Physically and legally split its wholesale and retail operations into two entirely separate, independently managed companies",
      "Share the whole of its detailed internal financial accounts freely with every single one of its many rival operators",
      "File completely identical financial statements for absolutely every single country in which it happens to operate"]),

    ("A universal service obligation (USO) in telecommunications is best defined as:",
     "A regulatory requirement that certain basic services are made available to all citizens at an affordable price, regardless of location",
     ["A requirement that every single licensed operator offer every service it currently provides completely free of charge to all",
      "An international treaty that permanently and completely prevents any signatory country from restricting its own telecom market",
      "A licence condition that strictly and permanently prohibits any dominant firm from ever raising its own retail prices"]),

    ("When the provision of universal service is commercially unviable in high-cost "
     "rural areas, regulators commonly establish:",
     "A universal service fund financed by levies on operators in proportion to their revenues",
     ["A regulated price floor that prevents operators from discounting their services in profitable urban areas",
      "A mandatory transfer of spectrum rights from profitable operators to unprofitable rural operators",
      "A direct legal obligation requiring consumers themselves to subsidise rural service providers"]),

    ("Market failure due to information asymmetry occurs when:",
     "One side of a market has substantially more information than the other, preventing efficient transactions",
     ["Both buyers and sellers happen to have exactly identical information about the product's quality",
      "The government itself has more information than the market does about the optimal quantities to produce",
      "A single firm has permanently lower costs than its rivals due to proprietary technology it owns"]),

    ("A positive externality exists when:",
     "A transaction between a buyer and seller generates benefits for third parties who are not part of the transaction",
     ["A firm knowingly imposes ongoing costs on the whole of society that it does not itself ever bear or pay for",
      "A government tax deliberately corrects an existing, persistent over-supply of some particular harmful good",
      "A monopoly firm simply charges its customers a retail price that sits above the competitive market price"]),

    ("Ex-ante regulation differs from ex-post regulation in that ex-ante:",
     "Rules are set in advance to shape market behaviour before problems arise, rather than reacting to them after the fact",
     ["Intervention by the regulator occurs only after a breach has already been detected and formally proven",
      "Regulators choose to rely exclusively on general competition law rather than any sector-specific rules",
      "Firms remain entirely free to set their own commercial terms until a formal complaint is eventually received"]),

    ("An operator designated as having Significant Market Power (SMP) is one that:",
     "Enjoys a position of economic strength that allows it to behave to an appreciable extent independently of competitors, customers and consumers",
     ["Simply holds an operating licence that happens to run for a term of fewer than five years in total duration",
      "Has annual revenues that consistently fall below the national regulatory authority's own official reporting threshold",
      "Operates exclusively within remote rural areas where it faces absolutely no urban competition whatsoever from any rival"]),

    ("Before assessing whether an operator has SMP, a regulator must first define the "
     "relevant market. The relevant product market is defined as:",
     "The smallest set of products that are close enough substitutes to constrain each other's prices",
     ["All of the products offered by every single licensed operator throughout the whole country",
      "Whatever products the regulator personally decides to regulate for its own policy reasons",
      "Only the services that are covered by the dominant operator's own individual licence"]),

    ("A 'bottleneck' facility in telecommunications is one that:",
     "Is essential for reaching end customers, and which competitors cannot duplicate economically, giving the owner market power",
     ["Is simply located at the exact geographic centre of the national telecommunications network as a whole",
      "Can only ever be used by the incumbent operator under the specific terms written into its own licence",
      "Is shared voluntarily by all of the operators in the market under a formal co-regulation agreement"]),

    ("Local loop unbundling (LLU) allows:",
     "Alternative operators to rent the physical copper or fibre pair between the exchange and a customer's premises from the incumbent, at regulated prices",
     ["The incumbent operator to freely use rival operators' own transmission equipment entirely free of any charge whatsoever",
      "Individual consumers to personally and permanently own the physical cable that connects their own premises to the exchange",
      "Operators to resell each other's retail services to customers without ever having to own any network infrastructure of their own at all"]),

    ("Tariff rebalancing in the telecom sector typically refers to:",
     "Adjusting prices so that each service covers its cost, reducing cross-subsidies — for instance, raising local call prices and lowering international prices",
     ["Increasing every single category of retail price uniformly across the board simply to reflect the annual rate of inflation",
      "Transferring spectrum licence charges away entirely from mobile operators and onto fixed-line operators instead, without exception",
      "Setting completely identical retail prices for every operator regardless of each one's own underlying cost structure or size"]),

    ("An operator is likely to retain structural dominance even after market liberalisation "
     "largely because it:",
     "Controls legacy infrastructure (such as the local loop or backhaul) that new entrants cannot easily or economically replicate",
     ["Has already lost the great majority of its existing subscribers to newly entering rival firms in the market",
      "Holds an operating licence that just happened to be issued only after the wider market was first opened",
      "Offers absolutely no retail services of any kind at all in the newly opened, fully competitive market"]),

    ("A regulatory impact assessment (RIA) is designed to:",
     "Estimate the costs and benefits of a proposed regulatory intervention before it is implemented, to ensure its net effect is positive",
     ["Audit the detailed financial accounts of a regulated company only after it has already committed a breach",
      "Determine the precise size of the fine to impose on an operator that has been found guilty of market abuse",
      "Formally replace the entire public consultation process with a single, short written internal report instead"]),

    ("A light-touch regulatory approach is typically characterised by:",
     "Minimal intervention, with the regulator stepping in only when there is clear market failure or a specific complaint",
     ["Detailed, highly prescriptive rules that govern every single aspect of an operator's day-to-day behaviour",
      "The outright nationalisation of the dominant operator, carried out purely to prevent any future price abuses",
      "Prohibiting all forms of competition entirely, purely in order to protect the existing natural monopoly"]),

    ("Functional separation requires a dominant operator to:",
     "Operate its wholesale access network as a functionally separate business unit with independent management and systems, even if ownership remains unified",
     ["Sell off its entire network infrastructure outright to a genuinely independent, unrelated third-party company at market value",
      "Provide exactly identical wholesale prices to retail rivals and to its own retail division well before any formal separation occurs",
      "Establish a completely separate universal service fund that is financed entirely from its own revenues alone, with no outside support"]),

    ("The main argument in favour of infrastructure competition (multiple physical "
     "networks) over service competition (multiple retailers on one network) is that it:",
     "Leads to greater dynamic efficiency and innovation as firms compete across multiple layers of the value chain",
     ["Reduces the total overall cost of building broadband networks across the entire country",
      "Is always readily achievable even in rural areas where only a single network is commercially viable",
      "Eliminates absolutely any need for access regulation once the physical networks have been built"]),

    ("Regulators have intervened in international roaming markets because:",
     "Roaming charges were often far above cost, exploiting consumers who had no practical ability to switch provider while abroad",
     ["Roaming agreements freely negotiated between operators are explicitly and permanently prohibited under the WTO BTA",
      "The ITU formally and strictly requires that all international calls be routed through a single central global hub",
      "Overall consumer demand for roaming services was historically simply too low to justify any commercial provision"]),

    ("When a regulator performs a cost-benefit analysis of a proposed remedy, it should "
     "compare:",
     "The direct costs imposed on industry and consumers against the economic benefits of correcting the market failure",
     ["The regulator's own administrative budget against the total annual revenue of the dominant operator",
      "The average income of rural subscribers against the average income of urban subscribers",
      "The current market share held by each operator against the overall national average"]),

    ("A multi-sector regulator that oversees telecoms, energy and water simultaneously "
     "may have the advantage of:",
     "Applying consistent regulatory principles across sectors and avoiding conflicts between sector-specific agencies",
     ["Focusing its exclusive expertise narrowly on just a single industry's own unique technical characteristics",
      "Having a considerably larger administrative staff available to investigate each and every individual complaint",
      "Operating independently of government in a way that separate, sector-specific bodies simply never can"]),

    ("When two large mobile operators propose to merge, reducing the number of national "
     "operators from four to three, the regulator's primary competition concern is "
     "likely to be:",
     "A reduction in competitive pressure that could lead to higher prices or lower investment",
     ["An immediate and unavoidable increase in spectrum licence costs for the newly merged entity",
      "A risk that the newly merged entity will be entirely unable to recover its licence costs",
      "A formal requirement that the smaller merged operator buy out the regulator itself"]),

    ("The main advantage of sector-specific telecom regulation over reliance on general "
     "competition law is that:",
     "Sector-specific rules can be calibrated to the industry's technical characteristics and applied proactively, without waiting for a market abuse to occur",
     ["Competition law always reaches exactly the same practical outcome as dedicated sector-specific regulation would in every case",
      "Sector regulation is inherently more flexible simply because it has no prescribed rules of any kind at all to follow",
      "Competition authorities are formally and permanently forbidden from ever intervening in telecom markets under any circumstances"]),

    ("Asymmetric regulation imposes obligations on the dominant operator that are not "
     "applied to smaller rivals. The justification for this asymmetry is that:",
     "Only the dominant operator has the market power to harm competition or consumers in ways that the market itself cannot correct",
     ["Smaller operators are simply managed better overall and therefore need considerably fewer rules imposed on them",
      "All operators active in the market should be regulated in exactly the same way regardless of their market share",
      "Asymmetric regulation of this specific kind is required by the WTO Reference Paper in absolutely all cases"]),

    ("Periodic market reviews, in which the regulator reassesses which operators have "
     "SMP and what remedies apply, serve primarily to:",
     "Ensure that regulatory obligations remain proportionate as market conditions evolve, and are removed when no longer needed",
     ["Permanently and steadily increase the regulatory obligations placed on all operators in the market over time",
      "Allow the regulator to raise additional annual licence fees specifically from the dominant operators alone",
      "Transfer ownership of the incumbent operator back to the state if effective competition ever fails to develop"]),

    ("Regulatory forbearance occurs when a regulator:",
     "Deliberately refrains from exercising its available powers in a market, on the grounds that competition is sufficient",
     ["Simply fails to apply its own regulations properly due to administrative error or chronic under-resourcing",
      "Is formally prevented from intervening at all by a court injunction that was obtained by the operator itself",
      "Deliberately increases the overall stringency of its regulation in response to changing market conditions"]),
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
     ["The regulator will often over-spend heavily on enforcement against politically connected firms",
      "Operators will demand the right to audit the regulator's own accounts directly and regularly",
      "The regulator will automatically become independent of both the government and the operators"]),

    ("Which of the following is a mechanism that makes a regulator accountable without "
     "compromising its independence?",
     "A requirement to publish an annual report explaining its decisions to the legislature and public",
     ["Allowing the responsible minister to personally reverse any decision that the regulator makes",
      "Requiring the regulated operator itself to formally sign off on all regulatory decisions made",
      "Permitting the regulator to operate freely without any published criteria of any kind at all"]),

    ("Transparency in regulation requires that:",
     "The criteria, process and reasoning behind regulatory decisions are publicly available so that affected parties can understand and challenge them",
     ["All correspondence between the regulator and the operators it regulates must be kept strictly confidential at all times",
      "The regulator shares only its bare final decisions with the public, without ever publishing any of its underlying reasoning",
      "Consultation documents produced by the regulator are circulated only ever to the single dominant operator in the market"]),

    ("Regulatory certainty is valued by investors primarily because:",
     "Predictable rules reduce the risk premium they require when committing long-term capital to network infrastructure",
     ["Certain, stable rules always and automatically lead to permanently lower retail prices for all consumers",
      "Regulatory certainty entirely prevents any operator from ever being able to enter or exit the market",
      "Certain rules completely eliminate the need for any formal licencing process to exist at all"]),

    ("Under RPI-X price-cap regulation, if RPI is the retail price index and X is an "
     "efficiency factor, operators are required to:",
     "Reduce their regulated prices in real terms by X per cent per year, passing efficiency gains to consumers",
     ["Increase their regulated prices by the full RPI each year regardless of their own internal cost savings",
      "Keep all of their regulated prices fixed in nominal terms indefinitely, regardless of ongoing inflation",
      "Set their prices at exactly the rate of inflation minus whatever government subsidy happens to apply"]),

    ("A high X factor in a price-cap formula (RPI-X) implies:",
     "The regulator expects the operator to achieve large efficiency savings and requires it to pass them on to consumers quickly",
     ["The regulator simply expects the wider market to become steadily less competitive over the coming years",
      "The regulated operator will instead receive a direct subsidy equal to X per cent of its total annual revenues",
      "The entire price cap will automatically be removed once exactly X years of regulation have fully passed"]),

    ("A well-known drawback of rate-of-return (RoR) regulation is that it may create "
     "an incentive for the regulated firm to:",
     "Over-invest in capital (the Averch-Johnson effect), because profit is calculated as a percentage of the asset base",
     ["Under-invest entirely in new infrastructure simply in order to avoid attracting any regulatory scrutiny",
      "Reduce its retail prices below cost specifically in order to deliberately drive its rivals out of the market",
      "Resist any and all technological change that would require it to undertake new capital spending"]),

    ("A licence condition requiring a mobile operator to achieve a minimum 95 percent "
     "population coverage and a maximum 2-second call-setup delay is an example of:",
     "Quality-of-service (QoS) regulation imposing minimum performance standards",
     ["Price-cap regulation limiting how much the operator may charge",
      "Accounting separation requiring separate financial records",
      "Structural separation requiring distinct ownership of the access network"]),

    ("A regulator that requires a dominant operator to submit annual regulatory accounts "
     "broken down by network element cost, retail revenue and margin is using:",
     "Accounting separation to improve cost transparency and detect potential cross-subsidies",
     ["Structural separation to legally require the creation of two entirely distinct companies",
      "A formal price-cap review carried out specifically to determine the operator's new X factor",
      "A formal market review carried out specifically to define the relevant product market"]),

    ("A regulatory sandbox allows:",
     "Firms to test innovative products or business models in a controlled environment with relaxed rules, subject to safeguards",
     ["Operators to voluntarily exclude themselves from all forms of regulation for a fixed set period of time",
      "Governments to informally test new regulatory agencies before they are ever formally established in law",
      "Regulators to freely impose considerably higher fines than the underlying law would normally ever permit"]),

    ("A sunset clause in a regulatory instrument provides that:",
     "The regulation automatically expires after a set time unless the regulator actively decides to renew it",
     ["The regulated firm concerned must fully upgrade its network before a specified statutory deadline arrives",
      "The sitting regulator personally must resign from office once its own five-year term formally ends",
      "All obligations under the licence are instead phased in gradually over a period of several years"]),

    ("During a periodic market review, if the regulator finds that effective competition "
     "has developed and the dominant operator no longer has SMP, the appropriate "
     "response is to:",
     "Remove or relax the sector-specific obligations previously imposed on that operator",
     ["Impose considerably stricter conditions specifically to safeguard the competition that has newly emerged",
      "Transfer the operator's own spectrum holdings directly to a separate, state-owned entity instead",
      "Launch a full formal inquiry to determine whether outright re-nationalisation of the firm is needed"]),

    ("When an interconnection agreement cannot be reached through commercial negotiation, "
     "most regulatory frameworks allow either party to:",
     "Refer the dispute to the regulator for binding arbitration or determination",
     ["Withdraw services to the rival operator until an agreement is reached",
      "Seek damages from the rival's shareholders in a consumer court",
      "Delay interconnection indefinitely without incurring any penalty"]),

    ("Regulatory risk, from the perspective of an investor in telecoms infrastructure, "
     "refers to:",
     "The risk that the regulator will change the rules in ways that reduce the expected return on invested capital",
     ["The physical risk that network equipment might be seriously damaged by extreme weather events",
      "The risk that existing subscribers will switch to rival operators once new services are launched",
      "The risk that competition law will legally prohibit the operator from charging cost-based prices"]),

    ("Monitoring and enforcement are distinct regulatory activities. Monitoring is "
     "primarily concerned with:",
     "Collecting data and tracking compliance with regulatory obligations before a breach has occurred",
     ["Imposing fines and other penalties on firms that have already formally breached their own licences",
      "Deciding in the first place what specific obligations should be imposed on operators generally",
      "Publishing detailed annual reports covering the regulator's own internal financial performance"]),

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
     ["Replace every single one of the formal licence conditions with purely non-binding voluntary commitments instead",
      "Allow the regulator to freely impose fines for any breach whatsoever without ever following any form of due process",
      "Transfer all regulatory responsibility for the matter entirely over to the ordinary courts of law instead"]),

    ("When a regulator proposes a new interconnection pricing methodology, best practice "
     "requires it to publish a consultation document and allow a period for:",
     "Operators, consumers and other interested parties to comment before the methodology is finalised",
     ["The responsible government minister to formally approve the document before it is sent to any operator",
      "The single dominant operator alone to veto any proposals that it personally finds commercially disadvantageous",
      "The courts to formally pre-approve the methodology as being legally valid before it is even published"]),

    ("In developing economies, one frequently cited obstacle to effective regulation is:",
     "The knowledge and information gap between the regulator and the companies it regulates, due to limited technical and financial expertise in the regulatory body",
     ["An overall excess of regulatory staff who collectively impose unnecessary administrative burdens on every single licensed operator",
      "The outright and total refusal of incumbent operators to obey the law at all, under absolutely any circumstances whatsoever",
      "The complete and total absence of any legislation whatsoever enabling the creation of a regulatory body in the very first place"]),

    ("Why are licence conditions a particularly powerful regulatory instrument compared "
     "with general guidelines?",
     "Because they are legally binding on the licence holder and breach can result in enforcement action or licence revocation",
     ["Because informal guidelines are only ever published after a court order, while formal licences are much quicker",
      "Because binding licence conditions apply automatically to every single firm across every sector of the economy",
      "Because non-binding guidelines must first be approved by the ITU, whereas formal licences never need to be"]),

    ("A regulatory requirement for operators to maintain a formal written complaint "
     "procedure and respond within a set number of days is designed to:",
     "Ensure consumers have an accessible redress mechanism and operators take service quality seriously",
     ["Prevent ordinary consumers from ever taking their complaints directly to a court or independent tribunal",
      "Transfer consumer protection responsibilities entirely away from the regulator and over to the operator instead",
      "Allow the operator to legitimately charge consumers a fee for the internal processing of their complaints"]),

    ("Regulators in smaller markets often benchmark their rules and tariff levels against "
     "those in comparable countries. The primary purpose of such benchmarking is to:",
     "Draw on evidence from multiple markets to set well-informed, defensible regulatory parameters in the absence of sufficient domestic data",
     ["Simply copy the exact rules used by the single largest economy, entirely regardless of local market conditions back at home",
      "Entirely replace the whole of the national public consultation process with a purely international one instead altogether",
      "Allow individual operators themselves to freely choose whichever country's regulatory framework they personally would prefer"]),

    ("In most countries, the telecommunications regulatory framework assigns the "
     "legislature (parliament) the role of:",
     "Enacting the primary legislation that establishes the regulatory body and confers its powers",
     ["Setting all wholesale interconnection prices individually on a strict case-by-case basis each time",
      "Issuing individual operator licences directly and personally managing all spectrum allocation decisions",
      "Investigating each and every individual consumer complaint about operators' billing practices"]),

    ("An independent regulatory authority is often governed by a multi-member board "
     "rather than a single regulator. The main benefit of a board structure is that:",
     "Decisions represent a range of views and are less vulnerable to the bias or capture of any single individual",
     ["A multi-member board can issue licences considerably faster because each member simply signs separately",
      "Individual board members are personally and legally liable for regulatory decisions, which deters bias",
      "A multi-member board structure does not require any underlying legislation at all in order to be established"]),
]

# ---------------------------------------------------------------------------
# SET 8 - Licensing, Scarce Resources & Interconnection (Part 2)  (TE 462)
# ---------------------------------------------------------------------------
SET8 = [
    ("Spectrum refarming refers to the process of:",
     "Reassigning spectrum bands previously used by one technology (e.g. 2G) to a newer, more spectrally efficient technology (e.g. 4G or 5G)",
     ["Allocating entirely new spectrum bands that were only very recently discovered through satellite observation work",
      "Transferring spectrum rights permanently between two or more entire countries under a formal, signed ITU agreement",
      "Increasing the total amount of MHz available within a given band simply by reducing the size of its guard bands further"]),

    ("In spectrum secondary trading, spectrum rights are:",
     "Transferred or leased from one licence holder to another through market transactions, subject to regulator approval",
     ["Returned automatically to the government for free reallocation once they are no longer needed by anyone",
      "Auctioned directly by the ITU itself to the single highest bidder across every one of its member states",
      "Allocated automatically to whichever operator happens to have the longest network operating history"]),

    ("Cognitive radio technology enables more efficient spectrum use primarily by:",
     "Allowing devices to sense and opportunistically use spectrum bands that are temporarily idle, without causing harmful interference to primary users",
     ["Physically expanding the total radio spectrum available worldwide by opening up entirely new, previously unused frequency ranges",
      "Requiring every single operator in the market to permanently share just one licensed frequency band between all of them",
      "Replacing all existing licensed spectrum bands entirely with unlicensed, licence-exempt bands for every kind of telecom service"]),

    ("A regulator may impose spectrum caps (or spectrum limits) on individual operators "
     "in order to:",
     "Prevent any single operator from acquiring so much spectrum that it can disadvantage rivals, particularly in auctions",
     ["Guarantee that every single operator in the market ends up holding exactly the same amount of spectrum",
      "Reduce the total overall amount of spectrum that is consumed by all operators across the whole country",
      "Allow the incumbent operator to hold onto all of the remaining spectrum once liberalisation has occurred"]),

    ("When a country's radio transmissions could cause interference to services in a "
     "neighbouring country, the coordination process is managed through:",
     "Bilateral and multilateral agreements, guided by the ITU Radio Regulations",
     ["The World Trade Organization's Basic Telecommunications Agreement, negotiated between member states",
      "A dedicated telecommunications sub-committee that operates under the UN Security Council itself",
      "The National Regulatory Authority of the affected country acting entirely on its own, unilaterally"]),

    ("In the E.164 international numbering plan, a full international telephone number "
     "comprises:",
     "A country code followed by the national (significant) number, with the total not exceeding 15 digits",
     ["A network code followed directly by a subscriber number, with an overall minimum of ten digits",
      "A two-letter country prefix followed by both an area code and a separate subscriber number",
      "A six-digit operator code followed directly by the individual subscriber's own national number"]),

    ("Non-geographic numbers differ from geographic numbers in that they:",
     "Are not tied to a specific physical location, and are used for services such as freephone, premium-rate, or shared-cost calls",
     ["Can only ever be assigned to mobile subscribers specifically, and never at all to any fixed-line operator",
      "Must always begin with the full international country code of whichever network originally originates the call",
      "Are reserved exclusively and permanently for the sole use of emergency services alone, in every single country"]),

    ("A freephone (toll-free) service number is one where:",
     "The cost of the call is borne by the called party (the business) rather than the calling consumer",
     ["Neither the caller nor the called party pays anything at all, as the government fully subsidises the call",
      "The caller instead pays a considerably higher-than-standard rate, which the operator itself then retains",
      "The number in question is available only to emergency services and hospitals, and to no one else"]),

    ("Premium-rate service numbers expose consumers to the risk of high unintended "
     "charges. A common regulatory response is to:",
     "Require clear price disclosure before the consumer connects and impose a maximum per-minute or per-call cap",
     ["Prohibit the use of premium-rate numbers entirely and completely across the whole market",
      "Require that all premium-rate calls be paid for fully in advance by the calling consumer",
      "Allow operators to freely set their own premium rates without any disclosure obligation whatsoever"]),

    ("Short codes (e.g. 3- to 6-digit numbers) are administered by national regulators "
     "because:",
     "They are a scarce resource — their brevity limits how many exist — and must be allocated fairly across competing service providers",
     ["Short codes are instead allocated by the ITU to each individual country as part of the wider E.164 plan",
      "Short codes are effectively infinite in overall supply and therefore require no formal administration at all",
      "Short codes can only ever be used by government agencies and by telecom regulators themselves"]),

    ("In a standard telephone call, the originating operator is the one that:",
     "Carries the call from the calling subscriber and delivers it to the network of the terminating operator",
     ["Receives the call on behalf of the called subscriber and is the one that rings their phone",
      "Issues the specific number at which the called party can ultimately be reached by others",
      "Determines the final retail price that is actually charged to the called party themselves"]),

    ("Mobile termination rates (MTRs) are regulated in many countries because:",
     "The terminating operator has a monopoly over access to its own subscribers, allowing it to charge above-cost rates to originating operators",
     ["Mobile operators in general charge their own subscribers far too little money for all of their incoming calls received",
      "The ITU formally and explicitly mandates that all mobile termination rates be set at zero in every single member state",
      "Mobile termination rates of this kind are only ever paid directly by the government, and are never paid by any operator"]),

    ("Long-run incremental cost (LRIC) is used as a basis for regulated interconnection "
     "prices because:",
     "It reflects the efficient forward-looking cost of providing the specific service, excluding costs unrelated to the traffic being terminated",
     ["It simply measures the actual historic accounting cost that the operator has already spent at some point in the past",
      "It guarantees the regulated operator a fixed, government-mandated profit margin specifically on interconnection traffic",
      "It is simply the specific costing model that the WTO officially prefers for use in all cross-border interconnection"]),

    ("Retail-minus pricing sets the wholesale access price at:",
     "The incumbent's retail price minus the retail costs (marketing, billing, etc.) it avoids when selling wholesale, ensuring viable retail competition",
     ["A wholesale access price set quite deliberately well above the incumbent's own retail price in order to deter competitive entry",
      "Zero, on the basis that all wholesale network access should always be provided completely free of any charge whatsoever to anyone",
      "The full and complete cost of building an entirely new, fully competing rival network completely from scratch every single time"]),

    ("Domestic roaming agreements allow a mobile operator to:",
     "Provide services to its subscribers in geographic areas it does not cover, by using the network of another domestic operator",
     ["Offer its own subscribers entirely free calls whenever they make any international visit to a partner country",
      "Permanently use a foreign operator's own spectrum inside its national borders without any time limit",
      "Charge its subscribers a noticeably lower price whenever they happen to be in their home region"]),

    ("Regulators impose wholesale roaming caps on visited-network operators. The effect "
     "of a wholesale roaming cap is to:",
     "Limit the price that visited-network operators may charge the home-network operator, which can then pass lower retail prices to travelling subscribers",
     ["Prevent home-network operators from ever being able to sign any roaming agreements with other operators at all, under any circumstances",
      "Allow subscribers to freely use absolutely any network they personally wish, without ever needing any operator permission whatsoever",
      "Set the exact retail price that is charged to consumers by the home operator directly and entirely unilaterally, without exception"]),

    ("A Mobile Virtual Network Operator (MVNO) differs from a full Mobile Network "
     "Operator (MNO) in that an MVNO:",
     "Does not own radio spectrum or a radio access network, and instead buys wholesale network access from an MNO to sell services to end customers",
     ["Owns its own radio spectrum and base stations outright, but simply does not maintain any retail customer base at all",
      "Operates exclusively within remote rural areas where full MNOs happen to have absolutely no network coverage whatsoever",
      "Is licensed under a general class licence that is not subject to any conditions at all, quite unlike a full MNO"]),

    ("Passive infrastructure sharing involves operators sharing:",
     "Physical structures such as towers, masts, ducts and shelters, without sharing the active radio or transmission equipment",
     ["The exact same radio frequencies and active antennas installed together on one single, shared cell site",
      "Spectrum licences themselves, so that both operators end up transmitting together on one single common frequency band",
      "Customer billing systems and subscriber management platforms used internally and separately by each individual operator"]),

    ("Radio Access Network (RAN) sharing goes beyond passive sharing in that operators "
     "share:",
     "The active radio equipment (antennas, transceivers, controllers) in addition to towers and other physical structures",
     ["Only the masts and shelters themselves, and not any of the associated electronic equipment at all",
      "Core network elements such as the central switching and routing infrastructure used by each operator",
      "Spectrum licences, so that every operator taking part in the shared RAN uses one single frequency band"]),

    ("Net neutrality is the principle that:",
     "Internet service providers must treat all internet traffic equally, without discriminating based on source, destination or content type",
     ["Only officially neutral third parties are ever permitted to operate any internet exchange points at all",
      "Internet service providers must offer completely free access to official government websites specifically and exclusively",
      "Content companies must instead pay individual consumers directly for the privilege of consuming their own online services"]),

    ("In mobile number portability (MNP), the 'losing' operator is:",
     "The operator from which the subscriber is porting away — the one that currently holds the number",
     ["The operator that is actively gaining the subscriber who wishes to keep hold of their existing number",
      "The operator responsible for routing the ported call once the entire porting process is complete",
      "The operator that centrally administers the national number portability database on behalf of all"]),

    ("Regulators that set maximum porting timelines (e.g. one working day) do so "
     "primarily to:",
     "Prevent operators from using slow porting processes to discourage subscribers from switching",
     ["Allow operators to complete all technical work before the customer is aware of the port",
      "Ensure that porting requests are always processed in the order received",
      "Limit the number of porting requests an operator must handle per month"]),

    ("A short licence duration (e.g. five years) compared with a long one (e.g. twenty "
     "years) gives the regulator more:",
     "Opportunities to revise the licence conditions as market and technology conditions change",
     ["Greater certainty for investors who specifically need predictable returns over a much longer period",
      "More time before any formal regulatory review of the operator's own conduct is ever required",
      "Additional spectrum allocation rights that can then be distributed out to brand-new entrants"]),

    ("When renewing a licence, a regulator may attach new or revised conditions. The "
     "main constraint on this power is that:",
     "New conditions must be proportionate, justified by current market circumstances, and the operator must have fair notice and an opportunity to respond",
     ["No new conditions of any kind may ever be added to an existing licence once it has originally been granted to any operator at all",
      "Only the ITU itself may ever formally approve any new conditions that happen to be added at the time of a licence renewal",
      "The national government treasury must always separately approve each and every single new condition for its own fiscal impact"]),

    ("A regulatory requirement that all licensed operators connect emergency calls free "
     "of charge, even when a subscriber has no credit, is justified on the basis that:",
     "Emergency call access is a fundamental public interest obligation that overrides commercial pricing considerations",
     ["Emergency calls actually generate significant revenue that fully offsets their own zero-price status",
      "The WTO's Basic Telecommunications Agreement explicitly prohibits any charge for emergency service calls",
      "Subscribers who personally call emergency services are later refunded directly by the government itself"]),
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
