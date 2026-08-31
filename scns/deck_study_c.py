# -*- coding: utf-8 -*-
"""TE 456 study-bank question data, groups 17 to 24.

Two decks in this range carry no group number on their title slide and are
listed under their topic.

Five questions per deck. Format per question:
    (stem, correct_answer, [d1, d2, d3], explanation, teach)

Concept-focused: why a mechanism exists, what it trades against, and how it
connects to the rest of the course.

See build_study_questions.py for how these are compiled.
"""

DECKS = [
    {
        "topic": "eRACH, a learned random access protocol for LEO networks",
        "source": "Group 17 deck",
        "questions": [
            (
                "Why does a random access protocol designed for terrestrial towers fail in a low-orbit constellation?",
                "It has no notion of choosing which base station to associate with, yet in orbit the best choice changes continuously",
                [
                    "It cannot operate above a certain transmit power limit",
                    "It requires a fixed number of devices to be known in advance",
                    "It depends on a wired connection between base stations",
                ],
                "A terrestrial device attaches to whichever tower it is near, and that answer changes slowly. In orbit the serving satellite is moving, so association becomes a decision the protocol was never designed to make.",
                "THE ASSUMPTION BEING VIOLATED: terrestrial random access assumes a stationary base station. Under that assumption, which cell to use is nearly a fixed answer, so the protocol concerns itself only with WHEN to transmit, not WHERE. "
                "WHAT CHANGES IN ORBIT: satellites move quickly, so the best satellite to reach changes on a short timescale. The association question becomes live, and the standard protocol has no mechanism to answer it. "
                "THE OTHER TWO FAILURES follow from the environment rather than the design. Propagation delay, even in a low orbit, is long enough that protocols built on listening before transmitting or waiting for acknowledgement become slow and waste attempts on retransmissions that were not needed. And because preambles are chosen at random, many devices attempting access at once collide, wasting bandwidth and adding delay. "
                "WHY THIS MATTERS BEYOND THIS DECK: a recurring theme is that terrestrial protocols encode assumptions about geometry and delay. Identifying the encoded assumption is usually the fastest route to explaining why a mechanism fails in a non-terrestrial setting.",
            ),
            (
                "What does it mean for coordinated behaviour to be described as emergent in this protocol?",
                "Terminals never communicate with one another, yet independent learning produces a pattern of access that behaves as though it were coordinated",
                [
                    "The network broadcasts a schedule that terminals then follow",
                    "Terminals negotiate directly with their neighbours before transmitting",
                    "Coordination appears only after a central controller is added",
                ],
                "Each terminal learns purely from its own experience. The orderly spreading of access attempts is a by-product of many independent policies adapting, not the result of any exchanged message.",
                "THE DESIGN CONSTRAINT: coordinating access normally requires either a central scheduler or messages between devices. Both are expensive over a satellite link, the first because it adds a round trip, the second because devices cannot easily hear one another. "
                "WHAT IS DONE INSTEAD: each terminal observes only what it can see for itself, and adapts its own behaviour. Over many repetitions, terminals that keep colliding learn to shift their attempts, and the population settles into a pattern that avoids collisions without any of them having agreed to anything. "
                "WHY THE RESULT IS INTERESTING: coordination normally implies communication. Here the shared environment does the work, because each terminal's experience of collisions carries information about what the others are doing. The environment is the communication channel. "
                "WHAT EACH TERMINAL OBSERVES: the expected position of the satellite, which is available because orbits are predictable, and whether its own last attempt collided. From those two it decides whether to transmit now and which satellite to aim at, or to wait for a better opportunity.",
            ),
            (
                "Why is the ability to trade between competing objectives built into the protocol rather than fixed?",
                "Different applications tolerate collisions and delay differently, so the same policy cannot be optimal for all of them",
                [
                    "Regulations require the collision rate to be configurable",
                    "The satellite payload cannot support a single fixed policy",
                    "Training would not converge without an adjustable parameter",
                ],
                "A policy tuned purely for throughput accepts more collisions; one tuned to avoid collisions achieves less throughput. Which is preferable depends on the traffic being carried.",
                "THE OBJECTIVES CONFLICT: pushing for maximum throughput means transmitting aggressively, which causes more collisions. Avoiding collisions means being cautious, which leaves capacity unused. There is no setting that maximises both. "
                "WHY A TUNABLE TRADE-OFF IS THE RIGHT ANSWER: a broadband service and a sensor network want different points on that curve. Rather than choosing one, the protocol exposes the balance as a parameter so a deployment can select according to its traffic. "
                "THE HONEST ACCOUNTING: the reported gains in throughput and access delay are real, and they are accompanied by a substantially higher collision rate. Reading a result table for what it concedes as well as what it claims is the analytical habit being taught here, and it applies to every performance claim in this course. "
                "THE OTHER LIMITATIONS. Running a learned policy costs computation, which competes with the platform's power budget. And because the policy acts on predicted satellite position, error in that prediction feeds directly into its decisions, though the protocol is reported to be robust to such error.",
            ),
            (
                "Why does the protocol's dependence on predicted satellite position create a distinct kind of vulnerability?",
                "One of only two inputs to the decision is the expected satellite position, so an error in that prediction corrupts the policy's view of the world",
                [
                    "The terminal must transmit its own position to the satellite first",
                    "Positioning error changes which preamble the terminal selects",
                    "The satellite cannot compute a reward without an accurate position",
                ],
                "A policy acts on what it observes. If the geometry it believes in is wrong, its decisions about when and where to transmit are made on a false picture, however good the policy itself is.",
                "THE STRUCTURE OF THE VULNERABILITY: the terminal decides using two observations, its expected view of the satellite and the outcome of its last attempt. Halve that input set by corrupting one, and the decision quality falls regardless of how well the policy was trained. "
                "WHY THIS IS A GENERAL PROPERTY OF LEARNED SYSTEMS: a policy is a mapping from observations to actions. It has no independent access to reality, so it cannot detect that its inputs are wrong. This is why input quality matters as much as model quality, and it parallels the way open-loop timing correction inherits any error in its ephemeris and position inputs. "
                "WHAT THE DECK REPORTS: the protocol is robust to orbital positioning error, meaning performance degrades gracefully rather than collapsing. That is a useful property to be able to claim, and it is worth noting that robustness to input error is a design goal in its own right, not a free consequence of using learning. "
                "THE COMPUTATIONAL CONSTRAINT sits alongside it: a learned policy must run within a size, weight and power budget, which is the same limitation that constrains every AI proposal in this course.",
            ),
            (
                "What is the general form of the argument this deck makes?",
                "A protocol whose fixed design assumptions no longer hold can be replaced by a policy that adapts to the conditions it actually encounters",
                [
                    "Satellite networks require more preambles than terrestrial networks provide",
                    "Central coordination is always preferable to distributed decision-making",
                    "Machine learning is required by the specification for non-terrestrial access",
                ],
                "The protocol failed because its design-time assumptions about a stationary base station and short delays no longer apply. Learning substitutes values read from live behaviour for values fixed in advance.",
                "THE ARGUMENT IN ITS GENERAL FORM, which recurs across several decks: a protocol embodies decisions made at design time, under assumptions about the environment. When the environment changes enough, those decisions become wrong, and the choice is either to re-tune them for the new environment or to make them adaptive. "
                "WHY ADAPTATION IS ATTRACTIVE HERE: the environment does not merely differ from the terrestrial case, it keeps changing. Satellite geometry, the number of contending devices and the traffic pattern all vary, so any single re-tuned value would also be wrong much of the time. "
                "WHY IT IS NOT AUTOMATICALLY THE RIGHT ANSWER: adaptation costs computation, requires training data, and produces a system whose behaviour is harder to verify. Against those costs, the deterministic alternative of pre-computing corrections from known orbital geometry is already available and already standardised. "
                "THE HONEST QUESTION, and the one worth being able to pose: does the learned approach beat the deterministic baseline by enough to justify its overhead? Being able to state both sides distinguishes an evaluative answer from a descriptive one.",
            ),
        ],
    },
    {
        "topic": "RIS-enhanced NTN for coverage and capacity in 6G",
        "source": "Group 18 deck",
        "questions": [
            (
                "What problem is a reconfigurable surface introduced to solve?",
                "A satellite needs a clear view of the user, and an obstruction removes the link entirely rather than merely weakening it",
                [
                    "The satellite beam is too wide to serve individual users efficiently",
                    "The satellite cannot form enough beams for all users in a cell",
                    "Atmospheric absorption removes the link at high frequencies",
                ],
                "Blockage is a binary failure, not a gradual one. Where a building or terrain feature stands between satellite and user, there is no link at all, and the link budget was already tight before the obstruction.",
                "WHY BLOCKAGE IS DIFFERENT FROM WEAK SIGNAL: a weak link can be improved with more power, better coding or a longer integration time. A blocked link cannot, because the signal does not arrive at all. The remedy must create a path rather than strengthen one. "
                "WHY IT MATTERS PARTICULARLY IN A SATELLITE CONTEXT: the link budget is already marginal because of distance, so there is no margin to spend overcoming an obstruction. Terrestrially, enough power can sometimes push a signal through or around an obstacle; from orbit that reserve does not exist. "
                "THE PROPOSED ANSWER: place a surface where it can see both the satellite and the user, and use it to redirect energy around the obstruction. The user is served by a reflected path rather than a direct one. "
                "WHY THIS IS ARCHITECTURALLY UNUSUAL: the surface is not a transmitter or a receiver. It adds no power and originates no signal. It only changes the direction in which incident energy is reflected, which is what makes it cheap and what limits what it can achieve.",
            ),
            (
                "How does a passive surface steer a reflection without any transmitter?",
                "Each element applies its own phase shift, so the reflected wavefronts reinforce in one chosen direction and cancel elsewhere",
                [
                    "Each element amplifies the incident signal before re-radiating it",
                    "The surface rotates mechanically to face the intended receiver",
                    "The surface converts the signal to a different frequency before reflecting it",
                ],
                "Controlling the relative phase across an aperture decides where reflected waves add constructively. That is beamforming, and it requires no power amplification, only phase control.",
                "THE MECHANISM: an incident wave arrives across the whole surface. If every element re-radiated with the same phase, the reflection would go where simple geometry dictates. By adjusting each element's phase individually, the re-radiated wavefronts can be made to add up in a chosen direction instead. "
                "WHY NO TRANSMITTER IS NEEDED: the energy comes from the incident wave. The surface is redistributing energy it did not generate, which is why it can be low-power and lightweight. A controller sets the element phases; it does not feed them signal. "
                "THE VARIANTS AND WHAT DISTINGUISHES THEM. A purely passive surface only adjusts phase. An active variant adds amplification per element, which addresses the loss problem at the cost of power and complexity. Hybrid designs amplify only some elements. Some designs offer continuous phase control at higher hardware cost, others a small number of discrete phase states more cheaply, and some are designed to behave differently across frequency so one surface can serve multiple bands. "
                "THE COMMON THREAD: each variant trades control precision or gain against power, cost and complexity, which is the same shape of decision as hybrid beamforming on an aerial platform.",
            ),
            (
                "Why must a reflecting surface be physically large and positioned close to one end of the link?",
                "The two hops multiply rather than add, so the combined loss is far more severe than a single path of the same total length",
                [
                    "The surface must exceed the wavelength of the incident signal to reflect it",
                    "A large surface is needed to dissipate heat generated by the controller",
                    "Regulations impose a minimum aperture for reflecting satellite signals",
                ],
                "In a relay the two hops are separate links, each with its own budget. In a passive reflection the losses compound, so the only remedies are a very large aperture and short distance at one end.",
                "THE CRITICAL DISTINCTION, and the one most often missed: a RELAY receives, processes and re-transmits, so each hop is an independent link with its own power budget. A passive REFLECTOR does not regenerate, so the signal experiences the loss of the first path and then the loss of the second, and the effects compound. "
                "WHY THAT IS SO PUNISHING: path loss is already severe from orbit. Compounding two such losses produces a link budget that a small surface cannot close. "
                "THE TWO CONSEQUENCES: the surface must be large, meaning many elements, to gather and redirect enough energy; and it must be close to either the transmitter or the receiver, so that at least one of the two hops is short. A surface placed midway between two distant endpoints is the worst possible arrangement. "
                "THE PARALLEL WORTH DRAWING: this is the same reasoning that explains why a regenerative satellite payload does not accumulate Doppler across both link segments while a transparent one does. Whether impairments compound depends on whether the intermediate node regenerates the signal.",
            ),
            (
                "Why does a purely passive surface create a control problem that a relay does not?",
                "It cannot measure anything itself, so the channel must be estimated by other means before its element phases can be computed",
                [
                    "It cannot be assigned an identity within the network",
                    "It cannot verify that its reflection reached the intended user",
                    "It cannot be reconfigured once it has been installed",
                ],
                "Setting the phases requires knowing the channel from transmitter to surface and from surface to user. A device that only reflects contributes no measurements toward determining either.",
                "THE CIRCULARITY AT THE HEART OF THE PROBLEM: to steer the reflection correctly you must know the channel; to measure the channel you normally need a receiver; and the surface deliberately has none, because being passive is what makes it cheap. "
                "WHAT FOLLOWS: the channel must be inferred from measurements taken elsewhere, which adds complexity to the wider system even though the surface itself is simple. The apparent economy of a passive device is partly transferred to the infrastructure around it. "
                "THE SECOND CONTROL BURDEN: because the satellite is moving, the correct phase configuration changes continuously. The surface must be reconfigured repeatedly, which means a control channel and a computation running somewhere, again outside the surface itself. "
                "A FURTHER SUBTLETY: once a surface is large relative to its distance from the user, the usual assumption that arriving waves are effectively planar no longer holds, and the simple distance-based model used to compute phases becomes inaccurate. This is a case where the fix for one problem, making the surface large, undermines an assumption relied upon elsewhere.",
            ),
            (
                "How does such a surface add capacity as well as coverage?",
                "It provides a second, distinct propagation path, which allows an additional spatial stream to be carried",
                [
                    "It doubles the bandwidth available on the existing path",
                    "It allows the satellite to reuse the same frequency in adjacent beams",
                    "It compresses the data before reflecting it onward",
                ],
                "Coverage comes from creating a path where none existed. Capacity comes from that path being independent of the direct one, which adds a dimension the channel can carry a stream on.",
                "TWO DISTINCT BENEFITS FROM ONE MECHANISM. "
                "COVERAGE: where the direct path is blocked, the reflected path is the only path, so the surface is the difference between service and none. "
                "CAPACITY: where a direct path already exists, the reflected path is an ADDITIONAL and geometrically distinct route. Multiple-antenna systems carry several parallel streams by exploiting differences between propagation paths, so adding a distinct path adds a dimension in which a stream can be carried. "
                "WHY THE SECOND IS EASY TO MISS: it is tempting to think of a reflector purely as a way around obstacles. Its value where no obstacle exists comes from path diversity rather than from reach. "
                "THE STATUS OF THE TECHNOLOGY: it is a candidate for future systems rather than part of any released standard. That matters for how it should be discussed. Its behaviour is understood in principle; what is not settled is how it would be controlled, addressed and integrated into a standardised network, and those integration questions are usually what determine whether a promising technique is deployed.",
            ),
        ],
    },
    {
        "topic": "Uplink time synchronization for NTN without GNSS",
        "source": "Group 21 deck",
        "questions": [
            (
                "Why must uplink transmissions be advanced in time at all?",
                "Devices sit at different distances from the receiver, so without correction their transmissions would arrive at different times and overlap",
                [
                    "Because the uplink uses a different carrier frequency from the downlink",
                    "Because the receiver processes uplink and downlink in separate hardware",
                    "Because regulations require a guard period between transmissions",
                ],
                "Shared uplink access depends on transmissions from different devices arriving within their allotted intervals. Since propagation delay varies with distance, each device must transmit early by its own delay.",
                "THE UNDERLYING REQUIREMENT: several devices share the uplink by transmitting in defined intervals. That only works if their signals ARRIVE in the right intervals, and arrival time depends on how far each device is from the receiver. "
                "THE CORRECTION: instruct each device to transmit early by an amount matching its own propagation delay, so that despite differing distances, all transmissions arrive aligned. "
                "HOW IT WORKS TERRESTRIALLY: the base station measures when a device's signal arrives relative to when it should have, and commands an adjustment. This is straightforward because terrestrial delays are small and change slowly, so the measurement remains valid long enough to be useful. "
                "WHY THE SAME APPROACH DOES NOT TRANSFER: in orbit the delays are orders of magnitude larger and change continuously as the satellite moves. The measurement-and-command loop is both too slow and quickly outdated, which is what the rest of the deck addresses.",
            ),
            (
                "Why does removing the navigation receiver break the standard scheme so completely?",
                "The device computes its correction from its own position and the satellite's published orbit, so without a position fix the computation cannot begin",
                [
                    "The navigation receiver also supplies the device's frequency reference",
                    "The satellite cannot broadcast its orbit without a navigation timestamp",
                    "The device cannot decode the downlink without navigation timing",
                ],
                "The standard approach is geometric: two positions give a distance, and a distance gives a delay. Remove one of the two positions and there is nothing to compute from.",
                "THE STANDARD ARRANGEMENT combines two contributions. A part broadcast by the network, which is common to the whole beam, and a part the device computes for itself from its own position and the satellite's orbit. A measured correction from the network then trims what remains. "
                "WHAT FAILS WITHOUT A POSITION FIX: the self-computed part. The device does not know where it is relative to the satellite, so it cannot determine its propagation delay, and therefore cannot set an initial correction. "
                "WHY FALLING BACK ON MEASUREMENT ALONE IS NOT SUFFICIENT: a measured correction can only refine an estimate that is already close enough for the signal to be received in the first place. With no starting estimate the transmission arrives far outside the expected window, where there is nothing for the receiver to measure. The loop cannot start. "
                "THE CONCEPTUAL POINT: this is a bootstrapping problem. Feedback control requires an initial condition within its capture range, and the standard scheme obtains that initial condition from navigation data. Remove it and something else must supply it.",
            ),
            (
                "What is the key insight behind estimating the correction from the downlink signal alone?",
                "Satellite motion changes the propagation delay over time, so tracking how downlink arrival times drift reveals the delay without knowing position",
                [
                    "The satellite broadcasts its own clock drift for the device to mirror",
                    "Oscillator drift in the device is proportional to the propagation delay",
                    "Arrival-time drift can be removed by lengthening the guard interval",
                ],
                "The device cannot measure absolute distance, but it can observe how the arrival time of successive downlink slots shifts. That drift is produced by the changing range, so it carries the information needed.",
                "THE SHIFT IN APPROACH: instead of computing the delay from geometry, infer it from an observable consequence of the geometry changing. "
                "WHY IT WORKS: as the satellite moves, the distance changes, so successive downlink transmissions arrive progressively earlier or later. That drift is directly caused by the changing range, so measuring the drift over time gives information about the range without ever knowing the absolute position. "
                "WHY THIS IS ELEGANT: it removes the dependency on an external system by extracting information already present in a signal the device is receiving anyway. The same instinct appears in Doppler estimation, where the offset is recovered from redundancy already built into the transmitted symbols rather than from added reference signals. "
                "THE PRINCIPLE WORTH GENERALISING: when a quantity cannot be measured directly, look for something that varies with it and can be measured. Rates of change are often observable when absolute values are not.",
            ),
            (
                "Why does a filter-based approach suit this estimation problem particularly well?",
                "It maintains a running estimate of a quantity that evolves smoothly, refining it with each measurement and predicting through gaps",
                [
                    "It requires no measurements at all once initialised",
                    "It guarantees the estimate converges within one slot",
                    "It removes the need for the network to send any corrections",
                ],
                "The distance to a satellite changes smoothly and predictably. A filter that models that evolution can combine noisy measurements into a better estimate than any single measurement provides.",
                "WHY THE PROBLEM SUITS FILTERING: the quantity being estimated does not jump around. It follows a smooth trajectory dictated by orbital motion. A filter that models how a quantity evolves, and corrects that model with each new observation, extracts more from noisy data than treating each measurement independently. "
                "THE PRACTICAL BENEFITS: noise in individual measurements is smoothed out; the estimate continues to be available through brief interruptions, since the model can predict forward; and convergence from a poor initial guess is rapid, because each measurement contributes. "
                "THE COSTS: greater computation than a direct calculation, and reliance on the assumed model being right. A filter tracking a trajectory the system is not actually following will produce confident and wrong answers, which is a more dangerous failure than an obviously noisy estimate. "
                "THE SAME TECHNIQUE APPEARS ELSEWHERE in the course, tracking frequency offset through signal occlusions. Recognising it as one method applied to two problems, rather than two separate topics, reduces what has to be learned.",
            ),
            (
                "What is the essential limitation of broadcasting a single common correction to a whole beam?",
                "One value can be accurate only where it was computed for, so its error grows with distance from that reference point across a wide footprint",
                [
                    "It can only be transmitted once per orbital pass",
                    "It requires every device to already hold a position fix",
                    "It cannot be updated as the satellite moves",
                ],
                "The correct value varies across the coverage area, because devices at different points are at different distances. A single broadcast number is right in one place and progressively wrong away from it.",
                "THE GEOMETRIC ARGUMENT: propagation delay depends on distance to the satellite, and that distance is not the same for every device in a beam. A device near the centre of the footprint is closer than one near the edge. A single value cannot be correct for both. "
                "WHY IT IS USEFUL ANYWAY: it requires nothing from the device, no position fix and no measurement, and it gets every device approximately right. As a starting estimate that a feedback loop can then refine, approximately right is precisely what is needed, because it solves the bootstrapping problem. "
                "HOW THE FEEDBACK LOOP COMPLETES IT: the network observes whether a device's transmission arrived early, late or within the expected window, and instructs it to adjust accordingly. Repeating this converges on correct alignment. "
                "THE OVERALL STRUCTURE, and the answer to the deck's central question: several methods can supply the initial estimate that navigation data would otherwise provide, whether by inference from downlink drift, by filtering, or by broadcast approximation. The dependency in the standard scheme is a design choice, not a physical necessity, which is what the deck sets out to show.",
            ),
        ],
    },
    {
        "topic": "Deep reinforcement learning for space-air-ground resource allocation",
        "source": "Group 22 deck",
        "questions": [
            (
                "What characterises a space-air-ground integrated network, as distinct from a satellite network with a ground segment?",
                "Satellites, aerial platforms and terrestrial infrastructure are managed together as one layered system rather than as separate networks",
                [
                    "Every satellite also carries an Earth observation payload",
                    "Ground stations are replaced entirely by aerial relays",
                    "Each layer operates on a separate frequency allocation",
                ],
                "The defining feature is unified management across all three tiers. A satellite network with a ground segment still treats them as distinct systems with their own control.",
                "THE ARCHITECTURAL CLAIM: three tiers, spaceborne, airborne and terrestrial, coordinated as a single system with a common view of resources rather than as independent networks that happen to interconnect. "
                "WHY UNIFY THEM: each tier has complementary strengths. Satellites offer wide coverage and long delay; aerial platforms offer moderate coverage with much lower delay; terrestrial infrastructure offers high capacity over small areas. A user's best server depends on where they are and what they need, and only a unified view can make that choice. "
                "WHAT MAKES IT HARD: the resource allocation problem now spans tiers with very different characteristics, and users can potentially be served by any of them. The decision space is far larger than for any single tier alone. "
                "THE THREE STANDING CONSTRAINTS: spectrum is scarce and shared, so allocations interfere; onboard power and energy are limited on every platform that flies; and demand is uneven and constantly shifting. All three are resource problems, which is why resource allocation is the framing the deck adopts.",
            ),
            (
                "Why is reinforcement learning proposed for this problem rather than a conventional optimisation method?",
                "The environment changes continuously and decisions have consequences that unfold over time, so a policy that learns from interaction suits it better than solving a fixed problem instance",
                [
                    "Conventional optimisation cannot handle more than two network tiers",
                    "Reinforcement learning requires less data than conventional methods",
                    "Conventional optimisation cannot be implemented on satellite hardware",
                ],
                "Classical optimisation solves a stated problem whose parameters are known and fixed. Here the parameters change continuously and today's allocation affects tomorrow's options, which is the setting reinforcement learning addresses.",
                "WHAT DISTINGUISHES THIS FROM A STANDARD OPTIMISATION PROBLEM. "
                "The parameters do not hold still: topology, demand and channel conditions all change while the problem is being solved. A solution computed for the state observed a moment ago may already be stale. "
                "Decisions are sequential: allocating a resource now constrains what is available later, so the best immediate choice is not always the best overall choice. Optimising each instant independently can perform worse than a policy that accepts a lesser immediate gain. "
                "WHY LEARNING FROM INTERACTION FITS: rather than solving the problem afresh each time, a policy is learned that maps observed conditions to actions, and improves through the consequences of its own decisions. Once learned, applying it is fast, which matters when decisions must be made continuously. "
                "THE FRAMEWORK: the agent observes the STATE, which is the current picture of available power, bandwidth and channel conditions; takes an ACTION, allocating channels, setting power and selecting which platform serves whom; and receives a REWARD reflecting service quality, user experience and how efficiently spectrum was used. The reward defines what good allocation means, so its design is a modelling decision, not a detail.",
            ),
            (
                "Why do different reinforcement learning algorithms suit different parts of the allocation problem?",
                "Some decisions are choices among discrete options and others are continuous values, and the algorithms differ in which they can represent",
                [
                    "Some algorithms run on the satellite while others require ground hardware",
                    "Some algorithms are standardised by 3GPP and others are not",
                    "Some algorithms work only with a single network tier",
                ],
                "Selecting which channel to use is a discrete choice; setting an exact power level is a continuous one. Methods that output a choice from a list cannot express a real-valued setting, and vice versa.",
                "THE DISTINCTION THAT ORGANISES THE ALGORITHMS: what kind of thing the policy must output. "
                "DISCRETE DECISIONS pick one option from a finite set, such as which channel or which access point. Value-based methods that score each option and pick the best suit this naturally. "
                "CONTINUOUS DECISIONS produce a real number, such as a precise transmit power. A method that scores a finite list cannot express this, so a different family is needed that outputs the value directly. "
                "OTHER PRACTICAL DIFFERENCES: some methods prioritise stable, incremental improvement, which matters when erratic behaviour during learning would disrupt a live network. Others explore more aggressively and handle several competing objectives at once, which suits problems where the reward balances multiple concerns. "
                "THE POINT WORTH TAKING: algorithm selection follows from the shape of the decision, not from which method is generally best. Being able to say why a particular family fits a particular sub-problem is more valuable than listing names.",
            ),
            (
                "Why does each tier of the network present a different allocation problem?",
                "The platforms differ in what can be varied, so the decisions available at each tier are not the same",
                [
                    "Each tier is operated by a different organisation with its own policy",
                    "Each tier uses an incompatible radio access technology",
                    "Each tier serves a distinct and non-overlapping set of users",
                ],
                "A satellite's position is fixed by its orbit while an aerial platform's is not, so position becomes a decision variable in one tier and not the other. The available actions differ accordingly.",
                "WHAT VARIES BY TIER, and it is the set of controllable variables rather than the objective. "
                "IN ORBIT the position is determined by the orbit and cannot be chosen. What can be varied is how beams are directed and scheduled, how spectrum and power are apportioned, and which channels serve which users. "
                "AT AERIAL ALTITUDE position becomes controllable, so where to place the platform joins the decision set alongside spectrum and power. Onboard computing resources may also be allocated, since these platforms can host processing. "
                "FOR SMALLER AERIAL PLATFORMS position control extends to three-dimensional placement and to route planning, since energy spent flying competes with energy spent communicating, making trajectory itself a resource decision. "
                "ON THE GROUND the question becomes where computation should happen, whether locally, at an aerial platform, or via satellite to a distant data centre. "
                "THE UNIFYING VIEW: every tier is allocating scarce resources against shifting demand, but the levers available differ, which is why one policy cannot simply be reused across all of them.",
            ),
            (
                "What makes learning-based allocation difficult in this setting specifically?",
                "The environment is large, will not hold still long enough for a policy to settle, and demands decisions faster than learning naturally converges",
                [
                    "Training data cannot be collected from operational networks",
                    "The reward function cannot be defined for multi-tier networks",
                    "Reinforcement learning cannot handle continuous action spaces",
                ],
                "Scale, non-stationarity and timing pressure combine. Each is manageable alone; together they define the difficulty.",
                "THREE COMPOUNDING DIFFICULTIES. "
                "SCALE: the number of platforms, users and resources produces a very large space of possible situations and actions, so a policy must generalise rather than memorise. "
                "NON-STATIONARITY: learning normally assumes the environment is stable enough for experience to remain relevant. High mobility means the situation is continuously changing, so what was learned may no longer apply, and the target is moving while it is being learned. "
                "TIMING: allocation decisions have deadlines set by the network, while learning converges on its own timescale. A policy that would eventually be excellent is of no use if decisions are needed now. "
                "WHY THEY INTERACT BADLY: a large space normally needs more experience to learn from, non-stationarity shortens how long experience stays valid, and the deadline limits how long can be spent. Each difficulty makes the others worse. "
                "THE OVERALL ARGUMENT: multi-tier networks have resource demands that change faster and across more dimensions than traditional management methods handle, and learning-based allocation offers continuous adaptation. The costs are the three difficulties above, together with the onboard power and certification constraints that apply to every learned system in this course.",
            ),
        ],
    },
    {
        "topic": "HARQ mechanisms and limitations in NTN",
        "source": "Group 23 deck",
        "questions": [
            (
                "What distinguishes hybrid retransmission from either retransmission or error correction used alone?",
                "The failed copy is retained and combined with the retransmission, so both attempts contribute to decoding rather than the first being discarded",
                [
                    "It retransmits automatically without waiting for any acknowledgement",
                    "It corrects all errors without ever needing a retransmission",
                    "It applies error correction only after a retransmission has failed",
                ],
                "Plain retransmission throws away the corrupted copy. Combining means the information in the failed attempt is not wasted, so the two together can succeed where either alone would fail.",
                "THREE APPROACHES TO RELIABILITY, and the third is a genuine combination rather than a sequence. "
                "RETRANSMISSION alone: the receiver detects an error, requests a repeat, and discards the corrupted copy. Simple, and wasteful of the information the failed copy contained. "
                "ERROR CORRECTION alone: redundancy is added in advance so errors can be corrected without a repeat. This costs capacity on every transmission, including the ones that would have succeeded anyway. "
                "THE HYBRID: send data with error correction, and if decoding fails, RETAIN the failed attempt. When the retransmission arrives, combine the two. The failed copy was not worthless; it was merely insufficient on its own. "
                "TWO WAYS TO COMBINE. Repeating the same coded packet and adding the two receptions together effectively raises the signal quality. Alternatively, sending DIFFERENT redundancy the second time supplies parity that was omitted from the first, so the combined result is protected by a stronger code than either transmission carried alone. The second makes better use of the retransmission; the first is simpler.",
            ),
            (
                "Why does a long round-trip time stall the retransmission pipeline rather than merely slowing it?",
                "Each parallel process is held from transmission until its acknowledgement returns, so a long round trip occupies every process and leaves none free for new data",
                [
                    "The receiver's buffer overflows before the acknowledgement can arrive",
                    "Acknowledgements expire and are discarded if delayed too long",
                    "The receiver cannot decode a packet that arrives after a long delay",
                ],
                "Throughput is maintained by running several processes in parallel while each waits. If the wait is long enough that all processes are occupied simultaneously, transmission halts entirely.",
                "HOW THE PIPELINE NORMALLY WORKS: while one transmission waits for its acknowledgement, others proceed in parallel using separate processes. This keeps the link busy despite each individual exchange involving a wait. The number of parallel processes determines how much waiting can be hidden. "
                "WHERE IT BREAKS: the total waiting that can be concealed is the number of processes multiplied by how long each occupies one. When the round trip exceeds that product, every process is simultaneously waiting, none is free, and no new data can be sent. Throughput does not degrade gradually; it stops. "
                "WHY THIS IS A THRESHOLD RATHER THAN A GRADIENT: up to the limit, parallelism hides the delay completely. Beyond it, the mechanism provides nothing. That is what makes it a stall rather than a slowdown. "
                "THE ARCHITECTURAL FACTOR: where the base station sits determines how far the acknowledgement must travel. If it is on the ground, the loop crosses both the user link and the gateway link. If it is aboard the satellite, the loop closes over the user link alone, which is substantially shorter.",
            ),
            (
                "Why does increasing the number of parallel processes not fully solve the problem?",
                "The waiting that can be hidden grows only in proportion to the process count, and the round trip can exceed what any practical number covers",
                [
                    "Additional processes cannot be addressed by the existing signalling",
                    "Additional processes increase the collision rate on the uplink",
                    "Additional processes require a longer cyclic prefix",
                ],
                "More processes hide more waiting, but each additional one costs receiver memory, and the delay to be covered can still exceed what a realistic count provides.",
                "THE ARITHMETIC OF THE FIX: doubling the process count doubles the delay that can be concealed. That is a real improvement and a bounded one, because the delay is set by orbital geometry and does not shrink. "
                "THE COST: every process in flight requires the receiver to retain the corresponding failed copy for later combining. Memory therefore scales with the process count, and receiver memory is not free, particularly aboard a satellite. "
                "WHY OTHER MEASURES ARE ALSO NEEDED: if more processes alone were sufficient the story would end there. Because it is not, the alternatives become necessary. "
                "REMOVE THE WAIT ENTIRELY by not requesting acknowledgement at all, relying instead on strong forward error correction or repeated transmission. Nothing is waited for, so nothing stalls, and the cost is capacity spent on redundancy whether or not it was needed, plus no confirmation that delivery succeeded. "
                "MOVE RECOVERY TO A HIGHER LAYER so the lower layers never wait. Recovery still happens, more slowly, but the pipeline keeps moving. "
                "The pattern across all three: each removes the stall by giving up something else, whether memory, capacity or recovery speed.",
            ),
            (
                "Why is disabling acknowledgement a reasonable option rather than an obvious loss of reliability?",
                "It converts a delay problem into a capacity problem, spending redundancy in advance instead of waiting to discover what failed",
                [
                    "Errors become impossible once acknowledgement is disabled",
                    "The satellite retains a copy and retransmits without being asked",
                    "The receiver corrects all errors using its stored soft information",
                ],
                "Feedback lets you send only the redundancy actually needed, at the cost of waiting to find out. Removing feedback means committing redundancy up front, which costs capacity but nothing in time.",
                "THE TRADE STATED PLAINLY: feedback is a way of learning what went wrong so you can send exactly the right correction. It is efficient in capacity and expensive in time. Adding redundancy in advance is the reverse, expensive in capacity and free in time. "
                "WHY THE BALANCE SHIFTS IN ORBIT: on a short link, waiting is cheap, so feedback is clearly the better choice. On a long link, waiting is expensive enough to stall the pipeline, and spending capacity on redundancy becomes the better bargain. "
                "WHAT IS ACTUALLY GIVEN UP: not reliability itself, but the confirmation that delivery succeeded and the efficiency of correcting only what failed. Reliability is maintained by other means. "
                "THE FULL SET OF TRADE-OFFS across the adaptations: more parallel processes buy throughput with memory; longer timers avoid false alarms and slow the detection of genuine failures; removing feedback keeps data flowing and delays error recovery; and placing processing aboard the satellite gives the shortest loop at the highest cost in payload complexity, power and mass. "
                "THE HABIT WORTH FORMING: for any proposed fix here, name the resource it spends. None of them is free.",
            ),
            (
                "How does the choice between a repeating and a processing payload change the retransmission loop?",
                "A processing payload terminates the radio link on board, so the acknowledgement loop covers only the user link instead of the whole ground path",
                [
                    "A processing payload removes the need for retransmission entirely",
                    "A repeating payload retransmits from its own buffer without involving the ground",
                    "A processing payload moves recovery to a higher protocol layer automatically",
                ],
                "A repeating payload leaves the base station on the ground, so the acknowledgement must cross both link segments. A processing payload puts the base station in orbit and halves the geometry the loop must traverse.",
                "WHY PAYLOAD ARCHITECTURE DETERMINES THE SEVERITY OF THE PROBLEM: the stall depends on the round-trip time, and the round-trip time depends on where the endpoint of the radio protocol sits. "
                "A REPEATING PAYLOAD amplifies and forwards without demodulating, so the base station remains on the ground and the loop runs from user to satellite to gateway and back. This is the longest possible loop and the worst case for stalling. "
                "A PROCESSING PAYLOAD hosts the base station in orbit, so the loop closes over the user link alone. That is the shortest loop available and correspondingly the least prone to stalling. "
                "THE COST: onboard processing requires power, mass, thermal capacity and complexity that a simple repeater does not. Improving the loop is paid for in payload capability, which is the most expensive resource in the system. "
                "A NUANCE WORTH CARRYING: a partial split, where only the lower protocol layers fly and the higher ones remain on the ground, shortens the loop for the mechanisms handled in orbit while leaving those handled on the ground with the original long delay. Where a function sits determines the delay it experiences, so a payload is not simply processing or not.",
            ),
        ],
    },
    {
        "topic": "Network digital twinning for 3D satellite constellation optimization",
        "source": "Group 24 deck",
        "questions": [
            (
                "What distinguishes a digital twin from a simulation model?",
                "It is continuously updated with data from the real system, so it tracks the current state rather than representing a designed one",
                [
                    "It runs faster than real time, whereas a simulation runs slower",
                    "It models only the physical layer, whereas a simulation models all layers",
                    "It is built after deployment, whereas a simulation is built beforehand",
                ],
                "The defining property is the live link back to reality. A model that is not continuously updated describes a system as designed or imagined, not as it currently is.",
                "THE DISTINCTION MATTERS because it determines what the model can be used for. "
                "A SIMULATION represents a system under assumed conditions. It is invaluable for design and for exploring scenarios, and it does not claim to describe any particular moment. "
                "A DIGITAL TWIN is continuously synchronised with the real system, so it represents the CURRENT state. That makes it usable for operational decisions, because a decision tested in the twin is being tested against conditions that actually hold. "
                "WHY THE DISTINCTION IS ALSO THE MAIN COST: keeping a twin synchronised requires a continuous stream of telemetry from the real system. On a network where capacity is scarce, that stream competes with user traffic, so fidelity is bought with bandwidth. "
                "WHY IT SUITS A CONSTELLATION: satellite networks are dynamic, difficult to observe directly, and expensive to experiment on. A synchronised model allows options to be evaluated without disturbing the live system, which is worth a great deal when the live system is in orbit and cannot be easily corrected.",
            ),
            (
                "What makes a large satellite constellation difficult to manage by conventional means?",
                "Its topology changes continuously as satellites move and links form and break, so the network being managed is never the one that was last observed",
                [
                    "Its satellites use incompatible radio interfaces",
                    "Its ground stations are too few to monitor every satellite",
                    "Its orbits are unpredictable and cannot be computed in advance",
                ],
                "Conventional management assumes a network whose structure is stable between changes. Here the structure changes continuously, so any picture of it is immediately out of date.",
                "THE MANAGEMENT PROBLEM: routing, resource allocation and fault handling all assume knowledge of the network's structure. That assumption holds when the structure changes occasionally and holds still between changes. "
                "WHY IT FAILS HERE: satellites move continuously relative to each other and to the ground, so the links between them and to ground stations are formed and broken constantly. There is no stable structure to plan against. "
                "THE CONSEQUENCES that follow: routes become unstable, allocating resources is harder because the topology they are allocated over is shifting, faults are slower to detect because normal behaviour is itself changing, and operating costs rise because more intervention is required. "
                "THE ADDITIONAL CONSTRAINTS: long propagation delays mean control decisions are acted on late; onboard resources are limited so satellites cannot compensate with local computation; and physical access after launch is effectively impossible, so mistakes are expensive. "
                "THE PROPOSED RESPONSE: maintain a synchronised model of the network and use it to evaluate decisions before applying them, which is possible because orbital motion, unlike the failures it produces, is predictable.",
            ),
            (
                "What does a digital twin add over a conventional control loop that senses and reacts?",
                "Multiple possible futures can be simulated and compared before one is committed to the live network",
                [
                    "It responds to changes faster than a control loop can",
                    "It removes the need to collect data from the real network",
                    "It guarantees that the chosen decision is optimal",
                ],
                "A control loop acts on the current state and observes the result. A twin allows options to be tested in the model first, so the comparison happens before commitment rather than after.",
                "THE OPERATING CYCLE: collect current data from the network; synchronise the model with it; simulate several possible future conditions or candidate decisions; evaluate the options against each other; and deploy the best one to the real network. Results then feed back to improve the process. "
                "WHERE THE VALUE LIES: in the simulate-and-evaluate step. A conventional loop discovers whether a decision was good by making it. A twin allows candidates to be compared without the live network experiencing the poor ones. "
                "WHY THAT MATTERS PARTICULARLY IN ORBIT: experimentation on a live constellation is costly and slow to reverse. A decision that degrades service is felt by users before it can be undone. "
                "THE CLAIMED BENEFITS follow from this: lower latency and better routing, because options are compared rather than discovered; faster fault detection, because deviation between the model and reality is itself a signal; and reduced operating cost, because fewer corrective interventions are needed. "
                "THE PREREQUISITE, worth stating: this only works if the model is accurate. A twin that has drifted from reality confidently recommends decisions for a network that does not exist.",
            ),
            (
                "Why is the accuracy of the model itself listed as a limitation rather than an implementation detail?",
                "Decisions computed in the model are applied to the real network, so a model that is wrong produces confidently wrong operational decisions",
                [
                    "An inaccurate model consumes more bandwidth to synchronise",
                    "An inaccurate model cannot be migrated between satellites",
                    "An inaccurate model prevents the twin from being encrypted",
                ],
                "The twin is not a passive display. Its outputs drive changes to the live system, so errors in it propagate directly into network behaviour.",
                "WHY THIS DESERVES SEPARATE ATTENTION: a monitoring tool that is inaccurate misleads an operator, who may notice. A twin whose outputs are applied automatically does not offer that check, so its errors become network behaviour without anyone assessing them. "
                "THE SECURITY CONSEQUENCE follows directly and is often stated as a separate concern: because the twin influences the real network, an attacker who compromises the twin gains influence over the constellation without touching it. The model becomes an attack surface precisely because it is trusted. "
                "THE OTHER LIMITATIONS, grouped by kind. COMPUTATIONAL: simulating a large constellation demands substantial processing. SYNCHRONISATION: keeping the model current consumes bandwidth continuously, so fidelity trades against capacity. MIGRATION: because a twin models a physical thing that moves, it must follow that thing as the serving infrastructure changes, which adds machinery the terrestrial case does not need. "
                "THE COMMON THREAD: every benefit rests on the model matching reality, and every limitation is ultimately about the cost or the difficulty of maintaining that match.",
            ),
            (
                "Why is the twin organised hierarchically rather than as a single model of the whole network?",
                "Local decisions need fast, detailed views of a small area while global decisions need a broad view, and no single model serves both well",
                [
                    "A single model would exceed the storage available on any ground station",
                    "Hierarchy is required for the twin to be encrypted end to end",
                    "Each orbital plane must be modelled by a separate organisation",
                ],
                "Different decisions need different scope and different timeliness. Splitting the model lets local views stay fast and detailed while a global view handles decisions that span the network.",
                "THE ORGANISING PRINCIPLE: match the scope of the model to the scope of the decision. "
                "LOCAL DECISIONS, such as allocating radio resources, directing beams and diagnosing faults at a particular station, need detail about a small area and need it quickly. A model held near where those decisions are made serves them best. "
                "GLOBAL DECISIONS, such as network-wide routing, verifying overall behaviour, planning traffic and partitioning the network into services, need a broad view and can tolerate more latency. A central model serves those. "
                "WHY NOT ONE MODEL: a single model detailed enough for local decisions and broad enough for global ones would be expensive to maintain and slow to query, and most of its detail would be irrelevant to any given decision. "
                "THE PARALLEL WORTH DRAWING: this is the same separation of concerns that appears in the radio access architecture, where time-critical functions sit close to the radio and computation-heavy functions sit where resources are plentiful. The recurring principle is that placement should follow from latency sensitivity and resource cost, and recognising it once makes several architectures easier to reconstruct.",
            ),
        ],
    },
    {
        "topic": "AI-driven predictive handover for high-mobility LEO networks",
        "source": "Unnumbered deck, AI-Driven Predictive Handover Management",
        "questions": [
            (
                "What is the fundamental difference between mobility in a terrestrial network and in a low-orbit one?",
                "On the ground the user moves past fixed towers; in orbit the serving cell itself moves across the sky",
                [
                    "In orbit the user must select the satellite manually before each session",
                    "In orbit handovers occur only when the user is physically moving",
                    "In orbit the satellite performs the handover without informing the device",
                ],
                "The thing that moves is reversed. That single inversion produces every other difficulty, because a stationary user is still handed over repeatedly.",
                "THE INVERSION AND ITS CONSEQUENCES: because the cell moves rather than the user, handover stops being an occasional event triggered by user behaviour and becomes a constant, unavoidable feature of the network. A device that never moves still changes serving satellite every few minutes. "
                "WHY THAT CHANGES THE ENGINEERING: a procedure invoked occasionally can afford to be expensive. One invoked continuously cannot, because its cost is multiplied by a very large number of events. Signalling overhead, interruption time and failure probability all become first-order concerns. "
                "THE PROBLEMS THAT FOLLOW. Poorly timed switches leave brief gaps where data cannot flow. Because many devices share a satellite, they all need to switch at nearly the same moment when it sets, producing a surge of signalling. An unconfident system may switch back and forth between two satellites, wasting effort and degrading the connection. And every handover consumes signalling capacity and satellite processing that is already limited. "
                "The last point is worth noting: the cost is borne partly by the satellite, whose power and processing are the scarcest resources in the system.",
            ),
            (
                "Why is reacting to a weakening signal riskier over a satellite link than over a terrestrial one?",
                "By the time the report reaches the network and a decision returns, the satellite has moved far enough that the decision rests on outdated information",
                [
                    "Satellite receivers cannot measure signal strength accurately",
                    "Terrestrial networks do not use signal strength triggers at all",
                    "The satellite cannot store the measurement while in motion",
                ],
                "A reactive loop assumes the world changes slowly relative to the decision. Over a satellite link the loop is long and the geometry changes quickly, so both factors work against it.",
                "THE REACTIVE SEQUENCE: the device measures signal strength, notices it weakening, reports that to the network, the network arranges a handover, and the switch happens after the problem has already appeared. "
                "WHY IT WORKS TERRESTRIALLY: towers do not move, so the only unpredictable element is radio propagation. The decision loop is short, and the situation that prompted the report is usually still true when the decision returns. "
                "WHY IT FAILS IN ORBIT: the loop is long because the link is long, and the geometry changes quickly because the satellite is moving. The decision therefore arrives based on a situation that has passed. "
                "THE KEY INSIGHT THAT ENABLES THE ALTERNATIVE: unlike radio fading, satellite motion is NOT unpredictable. It follows well-known laws, the same physics used to predict eclipses and plan launches. So rise, culmination and set times can be computed ahead of the event, which means the need for a handover can be known long before any signal weakens. "
                "This is the same predict-rather-than-measure principle that underlies timing correction, Doppler compensation and beam selection elsewhere in the course.",
            ),
            (
                "What does conditional handover improve on, and what does it still leave unsolved?",
                "It removes the last-minute negotiation by arranging backup targets and switching conditions in advance, but the conditions themselves remain relatively simple and fixed",
                [
                    "It removes the need for the device to measure anything, but adds signalling",
                    "It allows the device to choose its target, but only among terrestrial cells",
                    "It eliminates handover failures entirely, but increases interruption time",
                ],
                "Preparing in advance removes delay from the moment of switching, which is a genuine improvement. What remains is that the trigger conditions are pre-set rules rather than adaptive judgements.",
                "WHAT CONDITIONAL HANDOVER CHANGES: rather than negotiating when the need arises, the network tells the device in advance which satellites are candidates and under what conditions to switch. The device then monitors and switches autonomously when the conditions are met. This removes back-and-forth signalling at precisely the busiest, most time-critical moment. "
                "WHAT IT DOES NOT CHANGE: the conditions are fixed rules set in advance. They cannot weigh factors against one another, adapt to changing congestion, or learn from what worked previously. "
                "WHERE LEARNING ADDS VALUE ON TOP: it can learn patterns from accumulated data, forecast how signal quality and congestion will develop, weigh several factors simultaneously, and choose both which satellite and when. The claimed outcomes are fewer unnecessary switches, lower failure risk, smoother transitions and better use of limited resources. "
                "THE STRUCTURE WORTH NOTING: conditional handover is described as the solid foundation and learning as building on top of it, not replacing it. That is a more defensible position than presenting the two as alternatives, and it is worth adopting in an answer.",
            ),
            (
                "Why is handover framed as a sequential decision problem rather than a single choice?",
                "Choosing a target now affects what options are available later, so the best long-term outcome may not follow from the best immediate choice",
                [
                    "Because several devices must be handed over in a fixed sequence",
                    "Because each handover requires several messages to complete",
                    "Because the device must reselect a cell before it can hand over",
                ],
                "Handing over to the strongest satellite now may lead to another handover shortly afterwards. Optimising each decision independently can produce a worse overall outcome than accepting a lesser immediate choice.",
                "THE SEQUENTIAL STRUCTURE: a satellite that currently offers the strongest signal may be about to set, so switching to it means switching again very soon. A slightly weaker satellite that will remain visible longer may be the better choice despite looking worse at this instant. "
                "WHY THAT REQUIRES A DIFFERENT KIND OF DECISION: a rule that picks the best current option cannot express this reasoning, because the relevant information concerns the future rather than the present. "
                "HOW IT IS FORMULATED: the decision is treated as a policy that maps an observed situation to an action, learned so as to maximise outcomes over time rather than at each instant. The observation includes current and predicted link quality, geometry, network load and history. The action is which satellite to move to, or to stay. The objective balances link quality against the costs of switching, so frequent handovers and failures are penalised. "
                "THE PRACTICAL PAYOFF CLAIMED: removing the measurement-report step entirely by predicting the appropriate action directly, which lowers access delay and reduces the number of devices switching simultaneously.",
            ),
            (
                "Why is a network-wide view of handover valuable beyond optimising each connection individually?",
                "Coordinating across many devices and satellites balances load and avoids congestion that per-connection decisions would create",
                [
                    "It allows handovers to be executed without any signalling",
                    "It removes the need for orbital prediction",
                    "It guarantees that no device experiences an interruption",
                ],
                "Each device choosing its own best target independently can send many onto the same satellite. Coordinating the pattern of handovers prevents that congestion.",
                "THE COORDINATION ARGUMENT, best understood through the air-traffic analogy the deck uses: a controller does not evaluate each aircraft in isolation, but sequences all of them onto runways so that the whole system flows without overload. "
                "WHY PER-CONNECTION OPTIMISATION IS INSUFFICIENT: if every device independently selects the satellite that looks best to it, many will select the same one, and it becomes congested. Each decision was locally correct and the collective outcome is poor. This is a general property of independent optimisation over shared resources. "
                "WHAT A GLOBAL VIEW ADDS: modelling devices, satellites and links together allows a handover pattern to be chosen that balances load across satellites and avoids congestion, even if that means some devices are not assigned their individually preferred target. "
                "THE LAYERED PICTURE the deck assembles: forecasting predicts future link quality; a learned policy decides per device; and a network-wide optimisation ensures those decisions are collectively sensible. Each layer addresses a limitation of the one below, which is a useful way to present the argument. "
                "THE COST, consistent with every other AI proposal here: computation on a platform constrained by size, weight and power, generating heat that is difficult to shed and running on hardware far less capable than a ground server.",
            ),
        ],
    },
    {
        "topic": "AI-assisted trajectory optimization of UAV and HAPS platforms",
        "source": "Unnumbered deck, AI-Assisted Trajectory Optimization",
        "questions": [
            (
                "Why does a mobile aerial platform following a fixed route behave much like a fixed tower?",
                "Its coverage no longer responds to where users actually are, so the ability to move provides no benefit",
                [
                    "A fixed route causes the platform to consume more energy than hovering",
                    "A fixed route prevents the platform from forming directional beams",
                    "A fixed route places the platform outside licensed airspace",
                ],
                "Mobility is only valuable if it is used to respond to demand. A predetermined path is a static deployment that happens to be in motion.",
                "THE ARGUMENT: the advantage of an aerial platform is that it can be where the users are. If its path is decided in advance and never adapts, that advantage is discarded, and it inherits the weaknesses of fixed infrastructure while adding the costs of flight. "
                "WHAT FOLLOWS: the interesting question is not whether to use aerial platforms but how their movement should be decided, which is why trajectory becomes the subject rather than deployment. "
                "THE PROBLEMS WITH STATIC DEPLOYMENT that motivate this: coverage does not match uneven and shifting user distribution; gaps appear where no platform is positioned; platforms may interfere with one another; energy is limited so wasteful positioning is costly; and users move while the deployment does not. "
                "THE FRAMING WORTH TAKING: this is a resource allocation problem where position is the resource being allocated. That places it alongside beam allocation and spectrum allocation elsewhere in the course, rather than treating it as a separate topic about aircraft.",
            ),
            (
                "Why is reinforcement learning suited to trajectory planning specifically?",
                "Where the platform goes now determines what is reachable later, so the objective is long-term performance rather than the best immediate position",
                [
                    "It requires no training data of any kind",
                    "It produces a single optimal trajectory that never needs revision",
                    "It runs entirely on the ground, so the platform needs no computation",
                ],
                "Movement is sequential and constrained. A platform cannot teleport, so each position choice restricts the next, which is exactly the setting where optimising each step independently performs poorly.",
                "WHY THE PROBLEM IS SEQUENTIAL: flying toward one cluster of users means flying away from another, and the platform's next options are constrained by where it is now. Choosing the best position for the current instant, repeatedly, can produce a path that serves no one well, oscillating between clusters and spending its energy travelling. "
                "WHAT LEARNING FROM INTERACTION PROVIDES: a policy that maps the observed situation to a movement decision, trained to maximise performance accumulated over time rather than at each moment. It can also adapt as user distribution changes, which a precomputed path cannot. "
                "WHAT THE PLATFORM OBSERVES: where users are, what signal quality they are experiencing, how much energy remains, what traffic is being demanded, what obstacles and terrain constrain propagation, weather conditions, and the quality of its connection back to the wider network. "
                "WHY THAT LIST MATTERS: it spans radio conditions, platform health, demand and the physical environment, because a good position depends on all four. This is what distinguishes the problem from ordinary beam steering, where only the radio situation is at stake.",
            ),
            (
                "What must the objective balance, and why can coverage not simply be maximised?",
                "Coverage must be weighed against energy, delay and interference, because the position that serves most users may be unsustainable or disruptive",
                [
                    "Coverage must be weighed against altitude, which is capped by regulation",
                    "Coverage must be weighed against the number of platforms deployed",
                    "Coverage must be weighed against the bandwidth allocated to each user",
                ],
                "Maximising coverage alone would drive the platform to positions it cannot sustain or that interfere with neighbours. The constraints must be part of the objective rather than checked afterwards.",
                "WHY A SINGLE OBJECTIVE FAILS: a policy rewarded only for covering users would fly to whatever position covers most, regardless of the energy required to get there or remain, and regardless of the interference caused to other platforms. It would perform excellently by its own measure and poorly in practice. "
                "WHAT THE OBJECTIVE INCLUDES: covering more users, achieving higher throughput and lower latency, while penalising energy consumption and interference. Undesirable outcomes such as coverage gaps, signal blockage, excessive energy use and weak connections back to the network are penalised explicitly. "
                "THE DESIGN LESSON: in a learned system the objective is where the engineering judgement lives. A policy optimises exactly what it is rewarded for, so anything omitted from the objective will be sacrificed. Specifying the objective is a modelling decision requiring care, not a routine step. "
                "THE PARALLEL: this is the same issue as designing the reward for random access, where success, delay and energy must all appear, or the objective will be met in an unintended way.",
            ),
            (
                "Why do the platforms in this architecture occupy distinct roles rather than being interchangeable?",
                "Altitude determines coverage area, endurance and latency together, so platforms at different heights suit different jobs",
                [
                    "Each altitude is allocated a different frequency band by regulation",
                    "Each platform type uses an incompatible radio access technology",
                    "Each platform type is operated by a different organisation",
                ],
                "Altitude sets several properties simultaneously. A higher platform covers more ground and adds delay; a lower one is more agile and covers less.",
                "THE LAYERED PICTURE and what determines each layer's role. "
                "SATELLITES provide the widest coverage and the longest delay, so they suit wide-area service and backhaul rather than responsive local capacity. "
                "HIGH-ALTITUDE PLATFORMS are quasi-stationary and cover a large region, acting as aerial base stations and providing backhaul for platforms below them. They sit between satellites and low-altitude platforms in both coverage and latency. "
                "LOW-ALTITUDE PLATFORMS are the most agile and cover the smallest area, so they suit on-demand capacity at hotspots or disaster sites where the need is concentrated and temporary. "
                "TERRESTRIAL INFRASTRUCTURE provides the highest capacity over the smallest area, where density justifies it. "
                "WHY THE LAYERING IS NOT ARBITRARY: altitude simultaneously fixes footprint, delay and typically endurance, so it is not a free parameter to be chosen per deployment. Each tier is the natural answer to a different combination of coverage, responsiveness and persistence, which is why they complement rather than compete.",
            ),
            (
                "Which limitation on this approach is not technical in nature?",
                "Airspace regulation, which constrains where and how platforms may fly regardless of their capability",
                [
                    "Battery capacity, which limits how long a platform can remain aloft",
                    "Computational complexity, which limits how quickly decisions can be made",
                    "Weather, which affects both propagation and flight",
                ],
                "The others are engineering constraints that better technology could ease. Airspace authorisation is an administrative constraint that no amount of engineering resolves.",
                "SEPARATING THE KINDS OF LIMITATION is the skill being tested, and it applies well beyond this deck. "
                "TECHNICAL LIMITS can in principle be pushed back by better engineering: battery capacity bounds endurance; computational complexity bounds how sophisticated the decision-making can be onboard; weather affects both propagation and the ability to fly. "
                "NON-TECHNICAL LIMITS cannot. Airspace regulation determines where platforms may operate, and is decided by aviation authorities on grounds of safety rather than communications performance. Security concerns similarly involve policy and trust rather than only engineering. "
                "WHY THIS DISTINCTION IS WORTH DRAWING IN AN ANSWER: it identifies which obstacles a research programme can address and which require a different kind of effort. It also appears elsewhere in the course, in cross-border spectrum coordination and in certifying learned systems against written specifications. "
                "THE OVERALL CLAIM: learning improves trajectory planning, intelligent mobility improves three-dimensional coverage, and the platform decides for itself and keeps improving. The claim concerns how decisions are made, not the removal of constraints, and battery capacity and regulation remain real limits either way.",
            ),
        ],
    },
]
