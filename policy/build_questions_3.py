#!/usr/bin/env python3
"""
Build the Telecommunications Policy & Regulation MCQ bank - Part 3.

Modelled on Part 1 (build_questions.py): the same four themed areas and the same
conceptual / applied-scenario style, with a fresh set of 100 questions drawn from
the same slide decks:
  - TE 452 - 1&2.pdf  (Background to regulation; Overview of telecom regulation)
  - TE 462 - Framework for Regulation.pdf
  - TE 462 - Licensing Telecommunication Services.pdf

Each question is authored as (question_text, correct_answer, [distractor, distractor, distractor]).
Distractors are written to avoid answer-guessability tells: options are kept close
in length (the correct answer is not systematically the longest) and distractors do
not lean on absolutist wording (always / never / only / entirely ...). The script
places the correct answer at a balanced, reproducible position so the key (A/B/C/D)
is evenly distributed. Output JSON: compiled_3.json
"""
import json
import random

# ---------------------------------------------------------------------------
# SET 1 - Market Economics & Fundamentals  (Background to Regulation, TE 452)
# ---------------------------------------------------------------------------
SET1 = [
    ("A streaming operator raises the monthly price of its video subscription and finds that "
     "the number of active subscriptions falls, with incomes and tastes unchanged. This "
     "outcome most directly illustrates:",
     "The law of demand, where a higher price reduces the quantity demanded, other things equal",
     ["The law of supply, where a higher price raises the quantity firms are willing to supply",
      "A leftward shift of the demand curve brought about by the change in the good's own price",
      "A rise in demand elasticity that pushes the operator's total revenue upward as price rises"]),

    ("Average household incomes in a region rise and, at every price, subscribers now buy more "
     "fixed broadband than before. For broadband treated as a normal good, this is best shown on "
     "a diagram as:",
     "A rightward shift of the entire demand curve",
     ["A movement upward along the existing demand curve",
      "A movement downward along the existing demand curve",
      "A leftward shift of the entire supply curve"]),

    ("Subscribers tend to buy a smartphone handset and a mobile data bundle together, so a fall "
     "in handset prices raises the quantity of data bundles bought. In demand analysis the two "
     "products are best classified as:",
     "Complementary goods",
     ["Substitute goods",
      "Inferior goods",
      "Independent goods"]),

    ("The market supply curve for a good is drawn holding other influences constant. Among the "
     "determinants of the quantity supplied, the variable placed at the centre of the basic "
     "supply relationship is the:",
     "Price of the good itself",
     ["Level of consumer income in the market",
      "Prices of goods that consumers regard as substitutes",
      "Tastes and preferences of the buyers in the market"]),

    ("A component manufacturer offers more units for sale as the market price rises and fewer as "
     "it falls, with technology and input costs unchanged. This positive price-quantity "
     "relationship is captured by the:",
     "Law of supply",
     ["Law of demand",
      "Principle of diminishing marginal returns",
      "Concept of consumer surplus"]),

    ("Engineers introduce a cheaper production technique that lowers the cost of making network "
     "routers. Holding the market price constant, standard analysis predicts that the supply "
     "curve for routers will:",
     "Shift to the right, as producers offer more at each price",
     ["Shift to the left, as producers offer less at each price",
      "Rotate until it becomes perfectly vertical at the old quantity",
      "Stay fixed while buyers move downward along the demand curve"]),

    ("Regulators observe that when the price of a basic voice service rises by 10 percent the "
     "quantity demanded falls by just 2 percent. The demand for this service is best described "
     "as:",
     "Inelastic, because quantity demanded responds little to the price change",
     ["Elastic, because quantity demanded responds sharply to the price change",
      "Unit elastic, because quantity demanded falls in step with the price change",
      "Perfectly elastic, because quantity demanded collapses to zero after the change"]),

    ("For a service with many close substitutes, a small price increase leads consumers to cut "
     "back their purchases sharply. The demand for such a service is best described as:",
     "Elastic",
     ["Inelastic",
      "Perfectly inelastic",
      "Unit elastic"]),

    ("At the current market price of a good, the quantity that suppliers offer exceeds the "
     "quantity that buyers wish to purchase. Standard analysis predicts that the price will "
     "tend to:",
     "Fall toward the equilibrium, clearing the excess supply",
     ["Rise further above the equilibrium, widening the excess supply",
      "Stay fixed, since a surplus has no effect on the market price",
      "Fall below the equilibrium and settle at a lasting shortage"]),

    ("To keep a service affordable, a regulator caps its retail price below the market "
     "equilibrium and holds it there. Standard analysis predicts that this binding price ceiling "
     "will most likely produce:",
     "A shortage, because quantity demanded exceeds quantity supplied at the capped price",
     ["A surplus, because quantity supplied exceeds quantity demanded at the capped price",
      "A fresh equilibrium that settles exactly at the level of the capped price",
      "A rise in supply large enough to remove the gap between demand and supply"]),

    ("A government guarantees producers a minimum price set above the market equilibrium and "
     "commits to hold it there. The most likely consequence of this binding price floor is:",
     "A surplus, because quantity supplied exceeds quantity demanded at the floor price",
     ["A shortage, because quantity demanded exceeds quantity supplied at the floor price",
      "A swift movement of the market back to its original equilibrium price",
      "A fall in the quantity supplied to a level beneath the quantity demanded"]),

    ("In public finance, the phrase tax incidence is used specifically to describe:",
     "How the economic burden of a tax ends up divided between buyers and sellers",
     ["The statutory rate that lawmakers write into the text of the tax legislation",
      "The total revenue a government expects to raise from imposing the tax",
      "The paperwork and collection costs a tax authority bears in administering the tax"]),

    ("A per-unit tax is levied on the buyers of a good rather than on its sellers. In the "
     "standard supply-and-demand model, the initial effect is represented as:",
     "A leftward (downward) shift of the demand curve",
     ["A rightward shift of the demand curve",
      "A leftward shift of the supply curve",
      "A rotation that makes the supply curve more elastic"]),

    ("An identical per-unit tax is placed on two goods. Good X has highly elastic demand while "
     "good Y has highly inelastic demand. Compared with buyers, sellers will tend to bear the "
     "larger share of the tax on:",
     "Good X, where demand is elastic",
     ["Good Y, where demand is inelastic",
      "Both goods in equal proportion, whatever the elasticities",
      "Neither good, since the duty to remit the tax rests with buyers"]),

    ("An economy in which a central authority owns the major resources and directs what is "
     "produced, how, and for whom, is best described as a:",
     "Command economy, coordinated by central planning",
     ["Traditional economy, coordinated by inherited custom",
      "Market economy, coordinated mainly through prices",
      "Mixed economy, blending markets with state action"]),

    ("An economy in which production methods and the allocation of goods follow inherited "
     "customs, with community elders having the final say, is best described as a:",
     "Traditional economy",
     ["Command economy",
      "Market economy",
      "Mixed economy"]),

    ("Supporters of the market economy argue that when buyers and sellers each pursue their own "
     "interest, competition and prices tend to guide resources toward valued uses. This "
     "coordinating tendency is often referred to as the:",
     "Invisible hand of the market",
     ["Central plan of the state",
      "Fixed rule of inherited custom",
      "Visible hand of the regulator"]),

    ("A defining assumption of a perfectly competitive market is that:",
     "Many firms sell an essentially identical product, so no single firm sets the price",
     ["A few large firms sell differentiated products and shade prices to match rivals",
      "A single firm supplies the whole market and searches for its profit-maximising price",
      "The state sets a common price that all the firms in the market then charge"]),

    ("Because a monopolist faces the whole market demand curve rather than a going market price, "
     "it is best described as a:",
     "Price maker, which chooses price and quantity along the demand curve",
     ["Price taker, which accepts the price set by the wider market",
      "Quantity taker, which accepts an output level fixed by its rivals",
      "Cost taker, which accepts input prices dictated by the regulator"]),

    ("An industry is described as a natural monopoly when, over the relevant range of output:",
     "One firm can serve the whole market at lower cost than several firms could, owing to economies of scale",
     ["Several competing firms can serve the market more cheaply than one, owing to rivalry",
      "The state licenses a single firm and bars new entrants from the market by statute",
      "Firms coordinate their output so that the market behaves as though one firm supplied it, even while rivals remain active"]),

    ("Where a genuine natural monopoly supplies an essential service, a common regulatory "
     "response is to allow the single firm to remain but to:",
     "Regulate its prices and conduct so outcomes move closer to the competitive result",
     ["Require several firms to duplicate the network regardless of the added cost",
      "Step back from oversight and let the firm price the service as it sees fit",
      "Take the firm and its rivals across the economy into full public ownership"]),

    ("A factory sells its output cheaply but discharges untreated waste that harms downstream "
     "communities whose losses it does not pay for. This gap between private and social cost is "
     "an example of a market failure known as a:",
     "Negative externality",
     ["Positive externality",
      "Public good",
      "Price ceiling"]),

    ("On a supply-and-demand diagram, the area between the demand curve and the market price, up "
     "to the quantity traded, measures:",
     "Consumer surplus, the gain buyers get above what they actually pay",
     ["Producer surplus, the gain sellers get above their marginal cost",
      "Tax revenue, the amount the government raises from the market",
      "Deadweight loss, the value of trades that fail to take place"]),

    ("Compared with the competitive outcome, a profit-maximising monopoly restricts output and "
     "raises price. The value of the mutually beneficial trades that are lost as a result is "
     "referred to as the:",
     "Deadweight loss caused by the monopoly",
     ["Producer surplus captured by the monopoly",
      "Consumer surplus retained by the buyers",
      "Tax incidence shared across the market"]),

    ("Because society's resources are limited while people's wants are not, every choice to use "
     "resources one way forgoes the next-best alternative. Economists call the value of that "
     "forgone alternative the:",
     "Opportunity cost of the choice",
     ["Marginal revenue of the choice",
      "Sunk cost of the choice",
      "Fixed cost of the choice"]),
]

# ---------------------------------------------------------------------------
# SET 2 - Sector Reform & Regulatory Foundations  (TE 452)
# ---------------------------------------------------------------------------
SET2 = [
    ("In many countries before the 1980s, telephone services were run by a government post and "
     "telecommunications administration (a PTT). This arrangement meant the service was "
     "typically provided by:",
     "A state-owned monopoly",
     ["A group of competing private carriers",
      "A set of independent regional cooperatives",
      "A foreign-owned equipment consortium"]),

    ("A frequently cited economic reason for the early telecom monopoly was that the high fixed "
     "cost of building a network, set against limited demand, made it hard for a second entrant "
     "to recover its outlay. This gave the industry the character of a:",
     "Natural monopoly",
     ["Perfectly contestable market",
      "Fully deregulated open market",
      "Traditional subsistence economy"]),

    ("Beyond economics, a political reason governments kept telecommunications in state hands "
     "was that they:",
     "Regarded communications as strategically sensitive and wished to keep them under state control",
     ["Were barred by an international postal treaty from licensing a private telephone operator",
      "Had no ministry with the technical means to oversee a basic national postal service",
      "Preferred to sell radio-spectrum rights straight to the highest private bidder of the day"]),

    ("In the telecom sector, the term liberalization is best understood as:",
     "The move from a monopoly market toward one open to competition",
     ["The sale of a state operator's ownership to private shareholders",
      "The setting of shared technical standards across the operators",
      "The intervention of the state to reach particular market outcomes"]),

    ("When a regulator removes the incumbent's exclusive rights to provide certain services, the "
     "most direct effect of that step is to:",
     "Let new entrants offer services that had been reserved for the incumbent",
     ["Move ownership of the incumbent's shares into private investors' hands",
      "Grant the incumbent a longer, protected and exclusive market position",
      "Fix a strict cap on the retail price of each of the incumbent's services"]),

    ("In the telecom sector, the term privatization refers specifically to:",
     "Moving the ownership of an operator from the state to private hands",
     ["Opening a monopoly market to competition from new entrants",
      "Placing universal-service duties on the licensed operators",
      "Establishing a new and independent national regulatory body to supervise the sector"]),

    ("A broad public offering of shares to many investors, rather than a sale to a single "
     "strategic buyer, has been the more common route to privatizing an incumbent in:",
     "Highly industrialised countries",
     ["Developing countries with thin capital markets",
      "Countries that never had an incumbent operator",
      "Countries retaining a full state telephone monopoly"]),

    ("A country sells a majority stake in its incumbent fixed-line operator to private investors "
     "but continues to grant that operator exclusive rights over fixed services. This is best "
     "described as:",
     "Privatization of the incumbent without liberalization of the market",
     ["Liberalization of the market without privatization of the incumbent",
      "Both full liberalization and full privatization together",
      "Neither privatization of the incumbent nor liberalization of the market"]),

    ("In the context of the telecom sector, regulation is best defined as:",
     "Government intervention in a market to bring about particular desired outcomes",
     ["The full withdrawal of the government from the market's activity",
      "The transfer of state-owned network assets into private ownership",
      "The routine self-policing of firms that operate without external oversight of their conduct"]),

    ("Regulation is often said to take three basic forms. Setting common interconnection and "
     "equipment standards that let different operators' networks work together is an example "
     "of:",
     "Technical standardization",
     ["Public policy regulation",
      "Competition regulation",
      "Voluntary self-regulation"]),

    ("Requiring operators to carry emergency calls and to meet content rules judged to serve the "
     "public interest is an example of which basic form of regulation?",
     "Public policy regulation",
     ["Technical standardization",
      "Competition regulation",
      "Co-regulation"]),

    ("The basic form of regulation aimed at establishing and preserving fair rivalry between "
     "firms, and fair dealing between firms and their customers, is:",
     "Competition regulation",
     ["Technical standardization",
      "Public policy regulation",
      "Zero regulation"]),

    ("Although telecom regulation can take several forms, the central focus of contemporary "
     "regulation of the telecommunications services industry is:",
     "The creation and maintenance of effective, competitive markets",
     ["The harmonising of accounting standards across unrelated industries",
      "The control of socially sensitive products such as alcohol",
      "The removal of private ownership from the telecom sector"]),

    ("A widely recognised objective of telecom regulation is to protect the interests of "
     "consumers, for example by:",
     "Addressing poor service quality and unfair terms that individual users struggle to resist",
     ["Securing a fixed profit margin for each of the licensed operators",
      "Steering connectivity toward the most commercially attractive urban districts of the country",
      "Holding back new operators that might enter and disturb the market"]),

    ("Where competitive markets are absent or have failed, a recognised objective is for the "
     "regulator to:",
     "Guard against abuses of market power, such as excessive pricing by a dominant firm",
     ["Shelter the dominant firm from the entry of potential competitors",
      "Pull back from oversight and let the market repair itself unaided",
      "Set every operator's retail prices at one identical level right across the national market"]),

    ("Which statement best captures the distinction between policy and law drawn in the course "
     "material?",
     "Law can compel or forbid conduct, whereas policy sets a direction that guides action toward a goal",
     ["Policy can compel or forbid conduct, whereas law merely offers broad guidance that binds no one",
      "Policy and law mean the same thing, so the two terms can be swapped freely",
      "Policy sets the long-term vision while law simply enforces it through the courts"]),

    ("Within the policy-to-practice chain, the role of regulation is chiefly to:",
     "Turn the objectives set by policy into practical rules, decisions and day-to-day oversight",
     ["Define the broad, long-term national vision that takes shape well before policy itself is formed",
      "Take the place of the underlying legislation and statutory authority",
      "Review the personal finances of government ministers each year"]),

    ("A frequently noted problem in the pre-reform arrangement was that one government body "
     "often acted at the same time as policy maker, regulator and operator of the telephone "
     "service. The main concern with this was that it:",
     "Created conflicts of interest that made even-handed treatment of rivals difficult",
     ["Left the day-to-day running of the telephone service without effective government supervision",
      "Prevented the state from raising revenue through licence fees",
      "Handed effective control of the sector to foreign carriers"]),

    ("The International Telecommunication Union (ITU) is best described as:",
     "A United Nations specialised agency dealing with information and communication technologies",
     ["A private club funded by the world's largest mobile network operators",
      "A regional trade bloc that negotiates import tariffs on telecom equipment on behalf of its members",
      "A commercial standards firm owned and directed by major equipment vendors"]),

    ("Coordinating the international radio-frequency spectrum and satellite-orbit resources is "
     "the responsibility of which ITU sector?",
     "ITU-R (Radiocommunication)",
     ["ITU-T (Standardization)",
      "ITU-D (Development)",
      "ITU-P (Policy)"]),

    ("Developing the technical standards that let telecommunications networks and services "
     "interwork globally, apart from radio matters, is the responsibility of:",
     "ITU-T (Standardization)",
     ["ITU-R (Radiocommunication)",
      "ITU-D (Development)",
      "ITU-S (Spectrum)"]),

    ("Helping to widen equitable, sustainable and affordable access to ICTs, especially in "
     "developing countries, is the principal role of:",
     "ITU-D (Development)",
     ["ITU-R (Radiocommunication)",
      "ITU-T (Standardization)",
      "ITU-A (Access)"]),

    ("The World Trade Organization's Agreement on Basic Telecommunications (the BTA) is chiefly "
     "concerned with:",
     "Setting out rules for competition and encouraging open investment in telecoms across countries",
     ["Assigning radio spectrum directly to individual operators in each member state",
      "Fixing the maximum retail tariffs that operators may charge their subscribers",
      "Granting individual operating licences directly to the carriers within each member state's market"]),

    ("One of the six basic principles of the WTO Reference Paper on Regulation is that "
     "interconnection with a major supplier should be:",
     "Provided on non-discriminatory terms, at cost-oriented rates and at reasonable request",
     ["Arranged privately between the largest carriers, on terms they keep confidential",
      "Offered at whatever price the major supplier judges the market will bear",
      "Reserved for operators that the incumbent selects as suitable partners"]),

    ("On the question of regulatory independence, the WTO Reference Paper and the course "
     "material indicate that a regulator should be independent of operators, while independence "
     "from government is:",
     "Not strictly required, though a greater degree of it is generally regarded as desirable",
     ["Required by law, so the regulator must sit inside the sponsoring ministry",
      "Required by law, so the regulator must be formally separate from government in all respects",
      "Arranged so that the regulated operators jointly own and direct the regulator"]),
]

# ---------------------------------------------------------------------------
# SET 3 - Framework for Regulation  (TE 462)
# ---------------------------------------------------------------------------
SET3 = [
    ("Within the framework for regulation, the laws that governments pass to enable regulation "
     "characteristically:",
     "Establish regulatory bodies and grant them powers to act",
     ["Guarantee the incumbent a lasting and protected monopoly position",
      "Strip regulators of their duties to report and account for decisions",
      "Set the retail price of each regulated service across the country"]),

    ("Which option best lists the categories of law that bear specifically on the "
     "telecommunications services industry?",
     "Sector-specific telecom law, competition and fair-trading law, and other relevant law such as privacy",
     ["Maritime law, constitutional law and the criminal law of the state",
      "General tax law, ordinary employment law and the intellectual-property law of everyday commercial dealings",
      "Banking law, insurance law and environmental law from other sectors"]),

    ("Measures agreed by a regional body such as ECOWAS, or by the WTO, take legal effect within "
     "a member or signatory country once they are:",
     "Transposed into national law in line with the treaty obligations",
     ["Posted on the regional body's official public website",
      "Endorsed by a majority vote of the country's licensed operators",
      "Agreed at the regional level, taking effect at that same moment"]),

    ("The framework notes that regulatory functions may be split between two or more bodies. A "
     "risk a country must manage when it does so is that:",
     "A poorly designed split of functions can breed disputes and slow the making of decisions",
     ["A single national regulator will end up capturing the whole market for itself",
      "Operators will find it much harder to obtain a licence from the divided bodies",
      "Spectrum will end up handed to operators free of charge under the divided regulatory arrangement"]),

    ("Ranked from the least to the most intrusive, the recognised styles of regulation run:",
     "Zero regulation, self-regulation, co-regulation, formal regulation",
     ["Formal regulation, co-regulation, self-regulation, zero regulation",
      "Self-regulation, zero regulation, formal regulation, co-regulation",
      "Co-regulation, formal regulation, zero regulation, self-regulation"]),

    ("An industry said to operate under zero regulation is one in which:",
     "Market forces are left to work without outside intervention",
     ["A regulator supervises the firm's daily operations in fine detail",
      "The firms jointly set binding rules under an industry watchdog",
      "A government ministry sets the prices at which firms must sell"]),

    ("Self-regulation, in which the players in an industry set and police their own rules, tends "
     "to work best when:",
     "The stakeholders share a strong convergence of interest",
     ["The players are locked in sharp commercial conflict with one another",
      "One firm dominates the sector and mistrusts its smaller rivals",
      "A regulator steps into the industry's routine operating decisions"]),

    ("A commonly cited advantage of self-regulation is that:",
     "Firms usually understand their own business better than an outside regulator would",
     ["It lifts the administrative cost of oversight from consumers and the industry alike",
      "It keeps firms from behaving opportunistically toward their competitors",
      "It removes the need for underlying legislation or a licensing regime"]),

    ("Co-regulation is best described as an arrangement in which:",
     "The regulator works alongside industry players in a joint forum rather than ruling from outside",
     ["Firms run their own affairs with little external oversight of their conduct",
      "A distant regulator dictates the firms' technical and pricing choices from outside the industry forum",
      "A foreign body takes over the domestic regulatory authority for the sector"]),

    ("Although it can be very effective, co-regulation is particularly exposed to:",
     "Role ambiguity, where the players hold differing views of who will do what",
     ["A sudden and wholesale loss of the regulator's formal legal powers overnight",
      "The capture of the regulator by organised consumer groups",
      "A blanket legal ban on collaboration of this kind between firms"]),

    ("Regulation is described as intrusive when the regulator:",
     "Intervenes frequently and in fine detail in a company's day-to-day operations",
     ["Sets out broad principles and leaves the methods to the firms themselves",
      "Steps back from the market and lets market forces work unaided",
      "Confines itself to issuing occasional, non-binding guidance"]),

    ("A reason intrusive regulation is generally viewed as undesirable is that:",
     "The regulator drifts into acting as a proxy manager of the industry, weakening operators' freedom",
     ["It sharply lowers the total cost of supervising the whole industry closely",
      "It assumes competition will deliver good outcomes without any oversight",
      "It shifts responsibility for poor market outcomes from the regulator across onto the operating firms"]),

    ("Good practice suggests regulation should be pervasive rather than intrusive, meaning it "
     "should:",
     "Shape operators' behaviour broadly while letting them run their own affairs within the rules",
     ["Prescribe the exact technical solution each operator is required to adopt",
      "Have as little day-to-day effect on companies' operations as can be managed",
      "Apply narrowly to just one dominant operator while leaving the other firms in the market untouched"]),

    ("Among the main instruments through which regulation is carried out are authorizations, "
     "rules, determinations, consents and:",
     "Guidelines",
     ["Share buy-backs",
      "Dividend payments",
      "Corporate tax returns"]),

    ("A system of authorization may grant specific authorizations and general authorizations, "
     "which correspond respectively to:",
     "Individual operator licences and class licences",
     ["Spectrum assignments and national numbering plans",
      "Price-cap orders and interconnection determinations",
      "Formal consents and published regulatory guidelines"]),

    ("Determinations are instruments of ongoing regulation whose function is essentially to:",
     "Flesh out the rules, for example when price controls are reviewed periodically",
     ["Cancel an operator's licence at once, with no route of appeal against the decision",
      "Overturn the underlying legislation suddenly and without prior notice",
      "Offer advice that carries no legal weight and binds no one",
      ]),

    ("Within the instruments of regulation, a consent is best understood as:",
     "A negative determination that releases an operator from meeting a particular requirement",
     ["An order that places a fresh additional obligation on the particular operator concerned in the matter",
      "An informal note that carries no legal standing in practice",
      "A financial penalty imposed on an operator for breaching a licence term"]),

    ("Guidelines differ from rules and determinations in that guidelines:",
     "Carry no legal force in themselves and are usually written in plain, accessible language",
     ["Bind operators more tightly than the formal conditions attached to their own operating licences",
      "Are issued by the courts following a successful appeal by an operator",
      "Cancel a licence at the very moment the operator is found to breach them"]),

    ("A key reason regulators consult widely before finalising their instruments is that "
     "consultation:",
     "Gives industry ownership of, and early sight of, decisions and improves their quality",
     ["Transfers the formal power of decision straight to the parties that are being consulted",
      "Relieves the regulator of its duty to give reasons for a decision",
      "Discourages the consulted parties from appealing the final outcome"]),

    ("An appeal against a regulator's action may be brought on the grounds of law (illegality), "
     "procedure (misadministration) or:",
     "Logic (irrationality)",
     ["Profitability (loss of revenue)",
      "Popularity (public disapproval)",
      "Timing (administrative delay)"]),

    ("Which of the following is a recognised enforcement power a regulator may use against an "
     "operator that breaks the rules?",
     "Imposing fines, issuing compliance orders, or in serious cases revoking the licence",
     ["Seizing ownership of a competitor's shareholding",
      "Personally setting the salaries paid to each of the operator's own board of directors",
      "Barring the operator's customers from switching providers"]),

    ("On the funding of national regulatory authorities, the typical arrangement is that:",
     "Government carries the primary responsibility but usually recovers the cost from industry through fees",
     ["Operators are barred by law from contributing to the regulator's budget",
      "The regulator supports itself mainly on the fines it collects from ordinary telecom subscribers each year",
      "The budget comes chiefly from foreign donor agencies and aid grants"]),

    ("The idea of regulatory hazard captures the concern that:",
     "Regulatory power, if used unwisely, can distort markets and damage the industry it oversees",
     ["Regulators face genuine physical danger to themselves when they inspect live network sites in the field",
      "Regulation strips most of the commercial risk out of the telecom market",
      "Operators face no consequences for repeatedly breaching the rules"]),

    ("Regulatory capture is said to occur when:",
     "The regulator comes to identify with the industry it oversees and serves that industry's interests",
     ["The regulator becomes gridlocked and stops issuing decisions for a long spell",
      "Individual operators are taken over and then run directly by the regulator acting as their outright owner",
      "Consumers step in and take charge of the regulator's day-to-day running"]),

    ("The information asymmetry that regulators face arises mainly because:",
     "The firms being regulated usually know far more about their business than the regulator does",
     ["Regulators are forbidden by statute from gathering the operators' detailed cost and operating data",
      "Consumers deliberately hide their true preferences from the regulator",
      "Operators are obliged by statute to withhold their internal financial records"]),
]

# ---------------------------------------------------------------------------
# SET 4 - Licensing, Scarce Resources & Interconnection  (TE 462)
# ---------------------------------------------------------------------------
SET4 = [
    ("Regulators grant licences to companies mainly in order to authorise them to:",
     "Operate telecommunications networks and provide telecommunications services",
     ["Manufacture and export telecommunications equipment to buyers in other markets",
      "Set the country's monetary and fiscal policy for the wider economy",
      "Audit the financial accounts of competing operators each year"]),

    ("Beyond granting permission to operate, a telecommunications licence characteristically "
     "sets out:",
     "The facilities a company may deploy, the services it may offer, and how it deals with other operators",
     ["The exact retail prices that every other operator in the country must charge",
      "The internal staffing structure and the full organisation chart of the sector's own regulatory authority",
      "The personal income-tax liabilities of the company's individual directors"]),

    ("For major licences that also govern access to scarce resources such as spectrum and "
     "numbers, operators are commonly required to pay:",
     "An upfront fee when the licence is awarded, followed by annual payments",
     ["A fixed share of yearly profits handed to the competing operators",
      "No payment, since major licences are usually granted free of charge",
      "A one-off refundable deposit returned in full when the licence expires"]),

    ("Historically, telecom licences were issued separately for different sub-markets such as "
     "fixed, mobile or paging services. The defining feature of that approach was that the "
     "licences:",
     "Drew distinctions between particular technologies and services",
     ["Were designed to be broadly technology- and service-neutral",
      "Applied identical terms across each and every market segment",
      "Were rarely tied to a specific technology or class of service"]),

    ("The convergence of technologies, which lets different platforms deliver overlapping "
     "services, has led some regulators to shift toward:",
     "Technology- and service-neutral licensing",
     ["Tighter technology-specific licensing for each platform",
      "The withdrawal of the licensing regime altogether",
      "Long, protected exclusive licences for the incumbents"]),

    ("A technology-neutral licence to provide a telephone service is one that:",
     "Leaves the operator free to choose between a fixed network and a wireless technology",
     ["Obliges the operator to use one particular government-specified fixed access technology",
      "Prevents the operator from offering any voice service of its own",
      "Requires the operator to buy from a single approved equipment vendor"]),

    ("The two main categories of licence awarded to telecom companies are:",
     "Individual operator licences and class licences (general authorizations)",
     ["Spectrum-only licences and separate telephone-numbering licences",
      "Import licences and export licences for telecom equipment",
      "Short-term provisional licences and longer-term probationary trial licences"]),

    ("Individual operator licences are used chiefly where:",
     "Licences are limited in number, dominance is likely, or scarce resources such as spectrum must be assigned",
     ["The market segment has ample room for many further new entrants",
      "The segment involves no scarce technical resources of any kind",
      "The particular market segment has ample room for many further new entrants to join and compete on equal terms"]),

    ("Class licences (general authorizations) are characterised by the fact that they:",
     "Apply the same terms of operation to all businesses in a segment, such as internet service providers",
     ["Are tailored individually to a single, specifically named operator within the market segment concerned",
      "Are reserved for the use of the former state incumbent operator",
      "Apply in the cases where radio spectrum has to be assigned"]),

    ("A current trend favours replacing individual operator licences with general authorizations "
     "where practical, because doing so:",
     "Simplifies regulation, supports a level playing field, and adapts more readily to market change",
     ["Maximises the one-off upfront revenue that the state collects from each licensed operator at the award stage",
      "Locks in the incumbent's protected position for a long period",
      "Removes the need for an independent regulator in the sector"]),

    ("One licensing objective treats basic telecommunications as an essential public service. "
     "This is used to justify:",
     "Keeping some controls so that services are provided in the public interest",
     ["Lifting regulatory oversight the moment the market is privatised",
      "Reserving service provision for a single state-owned monopoly for the long term",
      "Letting operators serve just the most profitable customers"]),

    ("Network roll-out targets and coverage obligations are often written into licences chiefly "
     "to advance which licensing objective?",
     "The expansion of networks and services, and universal service",
     ["The raising of one-off government revenue from spectrum auctions",
      "The shielding of the incumbent operator from new competition",
      "The harmonising of company accounting and reporting practices"]),

    ("When a state-owned incumbent is privatized, a licence remains necessary because it:",
     "Sets out what the investor is buying and what the government expects the operator to do",
     ["Transfers full legal ownership and operational control of the regulator across to the investor",
      "Assures the investor of lasting freedom from future regulation",
      "Lifts the operator's duty to serve less profitable customers"]),

    ("Licensing can be used to shape the structure of a market most directly by:",
     "Deciding how many operators are licensed to provide a given service",
     ["Fixing the wholesale price of each input used on the network",
      "Setting the wages that an operator pays its own employees",
      "Choosing the equipment vendors that operators are required to use"]),

    ("Licence conditions intended to create a level playing field and to curb an incumbent's "
     "abuse of dominance are usually referred to as:",
     "Anti-competitive safeguards, or fair-trading conditions",
     ["Universal-service obligations for underserved regions",
      "Spectrum-refarming and reallocation provisions",
      "Tariff-rebalancing and price-adjustment schedules"]),

    ("As a licensing objective, finite resources such as radio spectrum, numbers and rights of "
     "way should be allocated:",
     "Between operators fairly, efficiently and in the public interest",
     ["In full to whichever operator has the longest trading history",
      "On a first-come basis with little regard to how efficiently they are used",
      "To the operators that happen to be owned by the state"]),

    ("Licensing generates government revenue in two characteristic ways:",
     "One-off revenue from auctions and continuing revenue from annual licence fees",
     ["Seizure of operator profits and the taking of their network assets by the state",
      "Personal income taxes levied directly on the regulator's own staff",
      "Yearly donations collected from international agencies and donors"]),

    ("Consumer-protection conditions in telecom licences commonly deal with matters such as:",
     "Billing accuracy, complaint-handling arrangements and required services such as emergency calls",
     ["The internal shareholding structure of the operator's parent holding company and its subsidiaries",
      "The personal credit ratings of the operator's individual directors",
      "The choice of external auditors used by the regulator itself"]),

    ("By setting out clearly the rights and duties of the operator and the regulator, a licence "
     "advances the objective of:",
     "Regulatory certainty, which builds confidence and helps attract investment",
     ["Spectrum refarming carried out across the competing operators",
      "The removal of the regulator's remaining discretion over its own day-to-day decisions",
      "An exactly equal share of the national market for each operator"]),

    ("The international allocation of radio spectrum, designed to maximise its use while limiting "
     "cross-border interference, is coordinated by the:",
     "International Telecommunication Union (ITU)",
     ["World Trade Organization (WTO)",
      "Economic Community of West African States (ECOWAS)",
      "Association of the operators within each country"]),

    ("Although telephone numbers are in principle plentiful, they are treated as a scarce "
     "resource partly because:",
     "People can recall only a limited string of digits, and numbers must be issued in meaningful blocks",
     ["There is a small and strictly fixed stock of usable telephone-number digits in existence around the world",
      "Each telephone number needs its own dedicated radio frequency to work",
      "A given number can be assigned to just one country across the world"]),

    ("Number portability is a mechanism by which:",
     "The subscriber effectively owns the number and can carry it when switching providers",
     ["The operator keeps lasting ownership of the telephone numbers that it issues to its subscribers",
      "Numbers are auctioned off periodically to whichever operator bids the most",
      "Subscribers take a new number each time they move to a different provider"]),

    ("A regulator may auction spectrum to the highest bidder or assign it at a low administered "
     "price. Assigning spectrum at a low price is typically intended to:",
     "Lower prices for users or encourage the rollout of new services",
     ["Maximise the one-off revenue the government collects",
      "Set aside the band for the use of a single operator",
      "Remove the practical need to manage radio interference between competing users"]),

    ("A primary reason spectrum is assigned through instruments such as licences, rather than "
     "used freely, is to:",
     "Ensure it is distributed sensibly and that users do not interfere with one another",
     ["Increase the stock of digits available for telephone numbers nationally",
      "Let each operator broadcast on whichever radio frequency it happens to prefer at the time",
      "Remove the need for any coordination of frequencies across borders"]),

    ("The core principle of interconnection is that:",
     "Everyone should be able to communicate with everyone else, whichever network they belong to",
     ["Each operator should deliberately keep its own subscribers walled off from the networks of rivals",
      "Operators of a broadly similar size are the ones required to interconnect",
      "Interconnection is required between the largest international carriers"]),
]

# All 100 questions are compiled, in thematic order, into a single bank.
ALL_QUESTIONS = SET1 + SET2 + SET3 + SET4
OUTPUT_FILE = "compiled_3.json"


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def main():
    rng = random.Random(463)  # reproducible key placement
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
