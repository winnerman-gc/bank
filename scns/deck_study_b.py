# -*- coding: utf-8 -*-
"""TE 456 study-bank question data, groups 9 to 16.

Five questions per deck. Format per question:
    (stem, correct_answer, [d1, d2, d3], explanation, teach)

Concept-focused: why a mechanism exists, what it trades against, and how it
connects to the rest of the course. Figures appear only where the magnitude is
itself the point.

See build_study_questions.py for how these are compiled."""

DECKS = [
    {
        "topic": 'ISAC-enabled non-terrestrial networks for 6G',
        "source": 'Group 9 deck',
        "questions": [
            (
                'What distinguishes integrated sensing and communication from simply '
                'flying a radar alongside a communication payload?',
                'One waveform, one front end and one band carry both functions at the '
                'same time',
                [
                    'Sensing results are carried as ordinary payload data across the '
                    'communication link',
                    'The radar function operates only during intervals when the data link '
                    'sits idle',
                    'The two payloads share a power supply and a common thermal control '
                    'subsystem',
                ],
                'Integration is in the signal and the hardware chain. Two payloads on one '
                'bus, or alternating between modes, keep the functions separate and gain '
                'none of the efficiency.',
                'THE DEFINING PROPERTY: one waveform doing two jobs simultaneously. The '
                'signal that carries data is the same signal whose reflections reveal the '
                'environment. WHY THAT IS WORTH DOING: a conventional radar occupies '
                'spectrum that carries no information and hardware that serves no other '
                'purpose. Folding sensing into a communication waveform recovers both, '
                'which matters most where mass, power and spectrum are all scarce, that '
                'is, in orbit. THREE DESIGN STANCES, distinguished by which function the '
                'waveform is optimised for. A sensing-first design accepts a weaker data '
                'link. A communication-first design extracts whatever sensing it can from '
                'a signal not designed for it. A joint design optimises for both from the '
                'start and is the hardest to do well. WHY SATELLITES ARE A NATURAL HOST: '
                'they already sense implicitly, since ground networks recover a '
                "satellite's position and velocity from the Doppler on its signal. "
                "Integrated sensing generalises this from measuring the satellite's own "
                'motion to measuring external targets and the surrounding environment.',
            ),
            (
                'Why can a geostationary satellite not be located by the same Doppler '
                'method used for a low-orbit satellite?',
                'It holds position relative to the ground, so almost no radial motion is '
                'present',
                [
                    'Its transmit frequency is too high for any Doppler processing chain '
                    'to resolve it',
                    'Its returned signal is far too weak by the time it reaches the '
                    'ground station',
                    'Its orbit is published well in advance, so measuring it serves no '
                    'useful purpose',
                ],
                'Doppler requires relative motion along the line of sight. A satellite '
                'that stays above the same point produces essentially none, so the '
                'measurement yields nothing and distance must be measured instead.',
                'THE SAME PHYSICS SEEN TWICE, and it is worth holding both readings '
                'together. IN THE DOPPLER AND CHALLENGES MATERIAL, near-zero '
                'geostationary Doppler is CONVENIENT: there is little frequency error to '
                'compensate, so synchronisation is far easier than in a low orbit. HERE '
                'IT IS INCONVENIENT: the same absence of motion removes the observable '
                'that would have located the satellite, so ranging must be used instead. '
                'THE GENERALISABLE IDEA: a Doppler shift is INFORMATION as well as an '
                'impairment. Whether it helps or hurts depends entirely on whether you '
                'are trying to communicate through it or to measure with it. Low orbit '
                'gives strong signatures and hard synchronisation; geostationary orbit '
                'gives easy synchronisation and no signature. Recognising that an effect '
                'can be a nuisance in one subsystem and a resource in another is a habit '
                'worth carrying into the rest of the course, and it explains why the same '
                'orbital properties appear as advantages in some decks and disadvantages '
                'in others.',
            ),
            (
                'What does distributing the receivers across several platforms buy, '
                'compared with transmitting and listening at one platform?',
                'Several viewing angles on one target, resolving geometry a single view '
                'leaves open',
                [
                    'A stronger echo, since the reflected energy is collected at several '
                    'places at once',
                    'Freedom from needing any prior knowledge of the waveform that was '
                    'originally transmitted',
                    'Immunity to the Doppler shift imposed on the signal along its '
                    'reflected path',
                ],
                'Each receiver observes the target from a different direction, and '
                'combining those observations recovers information about position and '
                'shape that one direction leaves ambiguous.',
                'THREE GEOMETRIES, best understood as a progression in how transmit and '
                'receive are separated. CO-LOCATED: one platform transmits and listens '
                'for its own echo, sharing a single aperture. SEPARATED PAIR: one '
                'platform illuminates the target and a different one receives the '
                'reflection. DISTRIBUTED: one transmission is observed by many receivers '
                'across the constellation, so the constellation itself functions as a '
                'radar. THE TRADE THAT DEFINES THE CHOICE, and this is the concept rather '
                'than the taxonomy. Sharing one aperture means transmitting and receiving '
                'at the same instant in the same place, so the receiver must detect a '
                'very faint echo while its own transmitter is running. That is a severe '
                'dynamic-range problem requiring extensive cancellation, and it is harder '
                'still on a moving platform. Separating transmit from receive removes '
                'that problem entirely and introduces a different one: independent '
                'platforms must agree on time and phase to very fine precision, because '
                'combining their observations depends on knowing exactly when each was '
                'made. So neither arrangement is free. One trades synchronisation for '
                'self-interference, the other trades self-interference for '
                'synchronisation, and the right choice depends on which is easier to '
                'engineer in a given system.',
            ),
            (
                'Why does limited onboard processing capability translate into higher '
                'latency for a sensing function?',
                'Raw returns must go to the ground, so the answer comes back a round trip '
                'later',
                [
                    'Limited processing obliges the receiver to integrate over a much '
                    'longer dwell time',
                    'Limited processing requires the waveform itself to be transmitted '
                    'more slowly',
                    'Limited processing means echoes are stored until the next pass over '
                    'a gateway',
                ],
                'Where the computation happens determines how far the data must travel '
                'before an answer exists. Moving processing to the ground adds the link '
                'delay to every result.',
                'THE RECURRING TENSION between onboard and ground processing, which '
                'appears in almost every deck involving computation in space. ONBOARD '
                'PROCESSING gives short latency, because the answer is produced where the '
                'data is collected, and costs power and thermal capacity on a platform '
                'with very little of either. GROUND PROCESSING gives effectively '
                'unlimited computation and costs a round trip, because raw data must be '
                'downlinked and the result returned. WHY IT MATTERS PARTICULARLY FOR '
                'SENSING: many sensing applications are only useful if the result arrives '
                'while the situation still holds. A detection reported after the target '
                'has moved has limited value, so latency is not merely an inconvenience '
                'but can invalidate the function. THE OTHER STANDING OBSTACLES. The '
                'waveform must satisfy two objectives that pull in different directions, '
                'and long delay, large frequency offsets and intermittent visibility make '
                'that harder in orbit than on the ground. And there is no established '
                'standard for this over non-terrestrial links, so implementations cannot '
                'yet interoperate. The absence of a standard is worth noting as a '
                'distinct category of obstacle: it is not solved by better engineering, '
                'only by an agreement.',
            ),
            (
                'Which benefit of integrated sensing follows from spectrum reuse rather '
                'than from any new sensing capability?',
                'Better spectral efficiency, since no separate allocation is held for sensing',
                [
                    'The ability to track passive objects that transmit nothing of their '
                    'own accord',
                    'The ability to map a changing environment in real time and predict '
                    'outages',
                    'The ability to hold coverage when the ground infrastructure has been '
                    'destroyed',
                ],
                'The other benefits are things the system can now do. This one is a '
                'saving in a resource that was previously consumed by a dedicated radar '
                'allocation.',
                'SEPARATING THE TWO KINDS OF BENEFIT is the discipline being tested here, '
                'and it applies well beyond this deck. EFFICIENCY BENEFITS arise from '
                'doing the same work with fewer resources. Sharing one front end reduces '
                'mass, power and cost; sharing spectrum frees an allocation that a '
                'dedicated radar would have consumed. Nothing new is possible, but the '
                'same result costs less. CAPABILITY BENEFITS arise from being able to do '
                'something previously impractical. Tracking objects that do not transmit; '
                'building a live picture of an environment; providing sensing where no '
                'ground infrastructure exists; using what is sensed to steer beams and so '
                'avoid signalling overhead. WHY THE DISTINCTION MATTERS IN AN ANSWER: an '
                'efficiency argument and a capability argument justify a technology to '
                'different audiences and are defeated by different counter-arguments. If '
                'asked to justify integrated sensing, giving both is stronger than giving '
                'several examples of one. THE USE CASES SHARE A PATTERN worth stating: '
                'they all place a sensing need where infrastructure is absent, whether '
                'over open water, over a disaster area, or in orbit itself.',
            ),
        ],
    },
    {
        "topic": 'AI-native Open RAN for NTN',
        "source": 'Group 10 deck',
        "questions": [
            (
                'Why is the intelligence layer of a disaggregated radio access network '
                'split into two controllers?',
                'The decisions differ in how quickly they must be made, so each gets its '
                'own rate',
                [
                    'One of them governs the uplink direction and the other governs the '
                    'downlink',
                    'One of them is standardised while the other remains a '
                    'vendor-specific extension',
                    'One of them runs on the ground while the other one has to run aboard '
                    'the satellite',
                ],
                'Training a model and acting on its output have very different timing '
                'requirements. Forcing both into one loop would either make training '
                'rushed or make control sluggish.',
                'THE SPLIT IS BY TIMESCALE, not by function or location, and '
                'understanding why is more useful than remembering which is which. SLOW '
                'DECISIONS include policy setting and model training. These involve large '
                'amounts of data, tolerate latency well, and would be wasteful to repeat '
                'frequently. FAST DECISIONS include per-user resource and beam '
                'allocation. These must complete within the interval they apply to, or '
                'the situation has changed before the decision lands. WHY SEPARATE THEM: '
                'a single control loop must run at the speed of its fastest requirement, '
                'which would make training impractically rushed, or at the speed of its '
                'slowest, which would make control useless. Splitting lets each operate '
                'at its natural rate, with the slow layer supplying policy that the fast '
                'layer applies. THE ENABLING CONDITION is disaggregation itself: breaking '
                'the base station into separately deployable functions joined by '
                'standardised interfaces is what allows third-party software to control '
                "someone else's radio hardware. Without open interfaces the intelligence "
                'layer could not exist, which is why the two ideas arrive together.',
            ),
            (
                'What does disaggregating the base station into separately sourced units '
                'actually change?',
                'Standard interfaces let units come from different vendors and admit '
                'outside software',
                [
                    'Processing moves entirely into the radio unit, which reduces '
                    'backhaul demand',
                    'The core network becomes unnecessary, since the units interconnect '
                    'directly',
                    'Radio functions are replaced by satellite functions across the whole '
                    'network',
                ],
                "A traditional base station is one vendor's equipment joined by "
                'proprietary interfaces. Standardising those interfaces allows both '
                'multi-vendor supply and external control.',
                'THE COMMERCIAL ARGUMENT is vendor choice: a network operator can source '
                'the central unit, the distributed unit and the radio unit separately '
                'rather than buying a single integrated product. THE TECHNICAL '
                'CONSEQUENCE MATTERS MORE for this course. Once interfaces are '
                'standardised and documented, software written by someone other than the '
                'equipment vendor can observe and control the radio. That is the '
                'precondition for the intelligence layer, and it is why openness and '
                'programmability are discussed together rather than separately. THE THREE '
                'IDEAS THE DECK CONNECTS: the radio access network as the infrastructure '
                'linking devices to the core; machine learning as models that observe '
                'network data and make or recommend decisions; and non-terrestrial '
                'platforms as an extension of coverage beyond the ground. The claim is '
                'that the first must be open before the second can be applied to the '
                'third. A useful check on any architecture argument: ask what the change '
                'makes POSSIBLE that was previously impossible, rather than what it makes '
                'cheaper. Here, the answer is external programmability.',
            ),
            (
                'The AI-RAN concept is described as concentric layers. What distinguishes '
                'the outermost from the innermost?',
                'The inner one improves the network; the outer one sells access to AI over it',
                [
                    'The inner one runs on the ground while the outer one runs aboard the '
                    'satellite',
                    'The inner one is real-time while the outer one operates on a slower '
                    'control loop',
                    'The inner one handles the user plane while the outer one handles '
                    'control signalling',
                ],
                'The layers differ in which is the beneficiary. In one, AI serves the '
                'network. In the other, the network serves AI, acting as a delivery '
                'channel.',
                'THREE LAYERS, distinguished by the direction the benefit flows, which is '
                'the concept rather than the names. INNERMOST: artificial intelligence '
                'applied to the network, improving how the radio access network itself '
                'operates. Hardware, software and integration all serve network '
                'performance. MIDDLE: artificial intelligence alongside the network, '
                'where AI workloads and network workloads share the same infrastructure. '
                'This raises questions of partner integration and, importantly, security '
                'isolation, since two very different workloads now share hardware. '
                'OUTERMOST: artificial intelligence delivered over the network, where the '
                'network is the channel by which AI services reach customers. Here the '
                'network is not being optimised at all; it is being sold as a delivery '
                'mechanism. WHY THE PROGRESSION IS INTERESTING: it moves from a purely '
                'technical use, through an infrastructure-sharing arrangement, to a '
                'commercial product. Each step widens who benefits, and each introduces '
                'obligations the previous one did not, most obviously isolation between '
                'tenants once infrastructure is shared.',
            ),
            (
                'Why does satellite mobility create a difficulty for open radio access '
                'networks specifically, beyond the general problems of non-terrestrial '
                'links?',
                'The splits assume a link of fixed, known length, which orbital motion '
                'violates',
                [
                    'Open interfaces have no field in which orbital ephemeris data could '
                    'be carried',
                    'Cloud infrastructure of this kind cannot be deployed aboard a moving '
                    'platform',
                    'Control applications must be recompiled separately for every orbital '
                    'plane flown',
                ],
                'Splitting a base station into separate units means the interfaces '
                'between them carry timing-sensitive traffic. Those interfaces were '
                'specified assuming a fixed link, typically fibre of known length.',
                'WHY THIS IS AN ARCHITECTURE PROBLEM, not merely a delay problem. A '
                'monolithic base station keeps its internal timing entirely within one '
                'box. Disaggregating it exposes previously internal interfaces to a real '
                'transmission link, and the timing tolerances on those interfaces were '
                'written on the assumption that the link is short, fixed and predictable. '
                'PUT A UNIT IN ORBIT and none of those assumptions hold. The distance '
                'changes continuously, so the delay across the interface changes '
                'continuously, and the timing budget the split relied on is violated. THE '
                'OTHER TWO CHALLENGES follow related logic. Where to place the controller '
                'is a genuine dilemma: on the ground it is cheap to run and adds a round '
                'trip to every decision; on the satellite it removes the round trip and '
                'consumes scarce onboard power. And resource optimisation becomes HARDER '
                'after deployment rather than easier, which inverts normal experience. A '
                'terrestrial network is planned once and then holds still, so '
                'understanding accumulates. A constellation never holds still, so the '
                "problem is continuously re-posed and yesterday's solution expires. That "
                'counter-intuitive point is the most likely discussion question from this '
                'deck.',
            ),
            (
                'Why is an AI-driven handover decision able to improve on a threshold rule?',
                'It weighs several factors at once, where a threshold watches a single '
                'variable',
                [
                    'It carries out the handover itself far faster than any threshold '
                    'rule manages to do',
                    'It removes the need for the device to report any measurements to the '
                    'network',
                    'It guarantees that no handover attempt will fail once the decision '
                    'is taken',
                ],
                'A threshold compares one measured quantity against one value. A learned '
                'policy can combine several inputs, including predicted ones, into a '
                'single decision.',
                'THE LIMITATION OF A THRESHOLD RULE: it is simple, predictable and cheap, '
                'and it can only respond to the one quantity it watches. If the best '
                'decision depends on several factors interacting, a threshold cannot '
                'express it. WHAT A LEARNED POLICY ADDS: it can weigh current radio '
                'quality against how loaded the candidate target is, against where the '
                'user is heading, and against how soon the current link will degrade. '
                'Those factors can conflict, and resolving conflicts is exactly what a '
                'threshold cannot do. WHY THIS SUITS NON-TERRESTRIAL NETWORKS '
                'PARTICULARLY: signal strength alone carries little information there, '
                'because distance to the satellite dominates path loss and varies little '
                'across a cell. A decision rule that watches only signal strength '
                'therefore has very little to work with, whereas geometry and load carry '
                'real information. THE COST, which any complete answer should include: a '
                'learned policy consumes computation, requires training data that may not '
                'exist for a new constellation, and is difficult to certify against a '
                'written specification because it has no fixed behaviour to test. The '
                'gain is real and so is the overhead.',
            ),
        ],
    },
    {
        "topic": 'Federated learning for CSI feedback and beam management in LEO NTN',
        "source": 'Group 11 deck',
        "questions": [
            (
                'Why must a device report channel information at all, rather than the '
                'satellite measuring it directly?',
                'Only the receiver observes the path, so the transmitter must be told '
                'what arrived',
                [
                    'The satellite lacks the processing capability needed to measure its '
                    'own downlink channel',
                    'Conformance rules oblige the device to confirm the channel before '
                    'transmitting',
                    'The satellite measures the uplink instead and infers the downlink '
                    'from that',
                ],
                'A transmitter cannot observe the effect of the path on a signal it has '
                'not received. Only the far end sees what arrived, so shaping a beam '
                'depends on feedback from the far end.',
                'THE FUNDAMENTAL ASYMMETRY: the transmitter knows what it sent, and the '
                'receiver knows what arrived. The difference between them is the channel, '
                'and only the receiver is in a position to observe it. WHY IT IS NEEDED: '
                'aiming a beam at a user, or choosing how to encode across several '
                'antennas, requires knowing how the path will alter the signal. Without '
                'that knowledge the transmitter must be conservative, which wastes '
                'capacity. WHY IT BECOMES A PROBLEM: the report is small individually but '
                'must be sent by every device, in every beam, repeatedly. Its total cost '
                'grows with the number of antennas, the number of users and how often it '
                'is sent. An apparently trivial control message becomes the dominant '
                'uplink load once multiplied out. THE GENERAL LESSON: overhead that is '
                'negligible per instance can dominate at scale, and identifying that kind '
                'of cost is a recurring analytical move in this course. The same '
                'reasoning explains why signalling overhead matters so much in mobility '
                'management, where each handover is cheap but they happen constantly.',
            ),
            (
                'Why is a channel report described as stale by the time it is used, and '
                'what makes that different from simply being late?',
                'The channel it describes has already changed, so its content is wrong on '
                'arrival',
                [
                    'It is queued behind higher-priority traffic and therefore arrives '
                    'out of order',
                    'It must be decoded on the ground before the network is able to apply '
                    'it at all usefully',
                    'The device measures the channel only once, when it first attaches to '
                    'the cell',
                ],
                'Lateness would still leave the information valid. Here the validity '
                'window of the measurement is shorter than the time taken to deliver and '
                'use it, so the content itself is wrong on arrival.',
                'THE TIMELINE THAT MATTERS: the device measures, sends, the report '
                'arrives, and the network applies it. Alongside that runs a separate and '
                'shorter interval, which is how long the channel remains approximately '
                'what was measured. THE FAILURE: when the second interval is shorter than '
                'the first, the report describes a channel that has already changed. This '
                'is qualitatively different from late data. Late but valid information '
                'can still be used; invalid information cannot, no matter how promptly it '
                'arrives. WHY LOW ORBIT CAUSES IT: the satellite is moving quickly '
                'relative to the ground, so the geometry, and therefore the channel, '
                'changes rapidly. The delivery time is simultaneously long because the '
                'link is long. Both factors work against the report. WHY MAKING THE LINK '
                'FASTER DOES NOT FULLY SOLVE IT: the round trip is bounded by distance '
                'and the speed of light. Compressing the report helps by shortening '
                'transmission time, and predicting rather than reporting helps by '
                'removing the dependency, which is why both appear as remedies.',
            ),
            (
                'Why does a channel measurement raise a privacy concern that a throughput '
                'measurement does not?',
                'A path is shaped by its surroundings, so the pattern identifies a location',
                [
                    'Reports carry the subscriber identity in a header that is '
                    'transmitted in clear',
                    'Reports are transmitted without any encryption being applied to '
                    'protect them',
                    'Reports disclose which applications the subscriber happens to be running',
                ],
                'Reflections and obstructions differ from place to place, so the pattern '
                'a receiver observes is characteristic of where it is standing and can be '
                'inverted to recover position.',
                'WHY A CHANNEL IS IDENTIFYING: the signal reaching a receiver is the sum '
                'of paths shaped by the buildings, terrain and objects around it. That '
                'combination is close to unique to a location, so the measured pattern '
                'can be matched back to a position. THE CONSEQUENCE FOR TRAINING: '
                'improving the system with machine learning requires data, and the '
                'obvious way to obtain it is to collect measurements centrally. But a '
                'central store of channel measurements is effectively a store of '
                'subscriber locations, which creates exactly the exposure that ought to '
                'be avoided. THE TENSION THAT DEFINES THE DECK: the fix for stale reports '
                'needs data, and the natural way to gather that data creates a privacy '
                'problem. The two challenges are not independent, and any solution must '
                'address both together. THE RESOLUTION, in principle: train where the '
                'data already is, and move only what has been learned rather than what '
                'was observed. Understanding why that structure is necessary matters more '
                'than the names of the algorithms that implement it.',
            ),
            (
                'What is the defining property of the federated approach used to resolve '
                'that tension?',
                'Training happens on the device and only the learned update is ever sent '
                'onward',
                [
                    'Each device trains a wholly separate model that is never combined '
                    'with others',
                    'Training is carried out aboard the satellite on measurements it '
                    'gathers itself',
                    'A single global model is distributed once and is never revised after '
                    'deployment',
                ],
                'The distinction is between sharing observations and sharing what was '
                'learned from them. Aggregating updates improves a common model without '
                'any party holding the underlying data.',
                'THE STRUCTURE: each device trains locally on data it already has. It '
                'sends only the resulting model update. An aggregator combines the '
                'updates from many devices into an improved shared model and distributes '
                'it back. The raw measurements never cross the boundary. WHY THIS '
                'ADDRESSES THE PRIVACY PROBLEM: no single party ever holds a collection '
                'of location-revealing measurements, because the measurements stay where '
                'they were taken. WHAT IT COSTS, and a complete answer needs this half. '
                'Every training round crosses the full link, so the round-trip delay is '
                'paid repeatedly. Model updates can be large, sometimes larger than the '
                'reports the scheme was intended to save. Local training consumes device '
                'energy. Devices drop out mid-round, since a satellite is visible only '
                'briefly. And privacy protections such as added noise reduce accuracy. '
                'WHERE THE AGGREGATOR SITS is itself a trade: on the ground every round '
                'crosses the whole link; on the satellite rounds are faster but consume '
                'onboard power; a hierarchical arrangement averages partially at '
                'intermediate points to reduce the number of full rounds. This is the '
                'same onboard-versus-ground tension that appears throughout the course.',
            ),
            (
                'How does the same underlying idea apply to selecting a beam?',
                'Geometry and past beams predict the choice, so one measurement confirms it',
                [
                    'The device chooses its own beam and does not inform the network of '
                    'the choice',
                    'The beam is fixed when the connection is set up and is never changed '
                    'afterwards',
                    'Every beam is used at once and whichever gives the best result is '
                    'then retained',
                ],
                'Exhaustive search costs a measurement and a report per candidate. '
                'Prediction replaces that with one confirmation, and the saving comes '
                'from not measuring what can be inferred.',
                'THE COMMON PRINCIPLE ACROSS BOTH HALVES OF THE DECK: replace measurement '
                'and reporting with prediction wherever the underlying process is '
                'predictable enough to support it. FOR CHANNEL REPORTING, prediction and '
                'compression reduce what must be sent. FOR BEAM SELECTION, prediction '
                'reduces how many candidates must be tried. An exhaustive sweep measures '
                'every beam and reports the best, which costs time and uplink capacity '
                'proportional to the number of beams. Using orbital geometry and past '
                'beam history, a predictor can propose the likely best beam, and a single '
                'measurement confirms it. WHY IT WORKS HERE: satellite motion is '
                'deterministic, so which beam should serve a user is largely a geometric '
                'question with a computable answer. This is the same '
                'predict-rather-than-measure argument that underpins timing advance, '
                'Doppler compensation and predictive handover. WHERE IT MATTERS MOST: '
                'deployments with the tightest uplink budgets or the least energy to '
                'spend on reporting, which is why direct-to-device and large-scale sensor '
                'applications are the strongest cases.',
            ),
        ],
    },
    {
        "topic": 'AI-driven dynamic beam control for LEO 5G-NTN',
        "source": 'Group 12 deck',
        "questions": [
            (
                'Why does a fixed beam plan become invalid so quickly in a low-orbit network?',
                'The cell moves at orbital speed, so the ground it covers has already shifted',
                [
                    'User devices move faster than any plan can realistically be '
                    'recomputed for them',
                    'Subcarrier spacing changes as the elevation angle to the satellite '
                    'changes',
                    'Beam weights are lost each time the satellite passes into the '
                    "Earth's shadow",
                ],
                'In a terrestrial network the cell is fixed and users move within it. In '
                'low orbit the reverse dominates, since the footprint sweeps across the '
                'ground continuously.',
                'THE INVERSION worth internalising: terrestrial planning assumes fixed '
                'cells and mobile users, so a plan can be made once and adjusted '
                'occasionally. In low orbit the cell is the thing that moves, and it '
                'moves at orbital speed. WHY THAT BREAKS PLANNING RATHER THAN JUST '
                'COMPLICATING IT: a plan describes which resources serve which area. If '
                "the area a beam covers changes continuously, the plan's assumptions "
                'expire almost immediately, so planning must become a continuous process '
                'rather than a periodic one. THE RESOURCE CONSTRAINT THAT MAKES IT '
                'MATTER: a payload can form far fewer beams than there are cells to '
                'serve. If beams were plentiful, every cell could simply have one and the '
                'planning problem would largely vanish. Scarcity is what forces beams to '
                'be allocated, and allocation is what must be recomputed as the geometry '
                'changes. THE DEMAND SIDE: traffic is uneven and shifting. Under a '
                'uniform allocation, some cells are congested while others receive power '
                'that produces nothing. Matching a scarce resource to uneven and moving '
                'demand is the actual problem being solved.',
            ),
            (
                'Why do mandatory signalling requirements constrain how freely beams can '
                'be scheduled?',
                'Some signals must appear at fixed times, so the schedule works around them',
                [
                    'Signalling consumes considerably more power than an equivalent data '
                    'transmission',
                    'Signalling has to be carried on a separate carrier frequency from '
                    'user traffic',
                    'Signalling can only be transmitted while the satellite is close to '
                    'its zenith',
                ],
                'Some transmissions have their timing fixed by the standard so devices '
                'know when to look for them. Those slots are not available to be '
                'rescheduled, whatever the traffic situation.',
                'WHY CERTAIN SIGNALS CANNOT MOVE: devices that are not yet connected must '
                'be able to find the network. They can only do that if the signals they '
                'search for appear at predictable times, so those timings are fixed by '
                'the standard rather than chosen by the scheduler. THE CONFLICT THAT '
                'RESULTS: if two cells both require the beam during a mandatory '
                'signalling occasion, and the payload cannot serve both, one of them goes '
                'uncovered at exactly the moment devices there are trying to find the '
                'network. This is a hard scheduling constraint rather than a performance '
                'preference. THE TWO DOMAINS IN WHICH BEAMS ARE CONTROLLED. In the '
                'SPATIAL domain: steering and tracking to keep footprints aligned as the '
                'satellite moves; grouping users by location so that adjacent beams '
                'interfere less; and reshaping beam width to compensate for the fact that '
                'a beam of fixed angular width covers a much larger and more distorted '
                'ground area near the horizon than directly below. In the TIME domain: '
                'visiting cells in turn so that a small number of beams can serve many '
                'cells; reserving the fixed signalling occasions; and forecasting demand '
                'so that visits can be scheduled in advance rather than reactively.',
            ),
            (
                'Why is time-multiplexing beams across cells necessary rather than merely '
                'convenient?',
                'There are fewer beams than cells, so covering them all means visiting in '
                'turn',
                [
                    'Continuous illumination of a single cell would exceed the permitted '
                    'emission limits',
                    'Beams must be rested at intervals so that amplifier heating can be '
                    'managed',
                    'Devices are able to receive only during discrete intervals that are '
                    'scheduled',
                ],
                'The constraint is resource scarcity on the payload. If beams outnumbered '
                'cells there would be no need to share them in time at all.',
                'THE ARITHMETIC OF THE CONSTRAINT: a payload of limited mass and power '
                "can form a limited number of beams. A satellite's footprint contains "
                'many more cells than that. Sharing beams across cells in time is '
                'therefore forced, not chosen. WHAT MAKES IT EFFICIENT RATHER THAN MERELY '
                'NECESSARY: cells do not need equal service. Visiting busy cells more '
                "often and quiet cells less often matches the beam's time to where demand "
                'actually is. Uniform visiting would waste the scarce resource on cells '
                'that have nothing to send. WHY PREDICTION HELPS: if future demand can be '
                'forecast from historical patterns, visits can be scheduled in advance '
                'rather than in response to observed congestion. Reacting to congestion '
                'means the congestion has already occurred; anticipating it means it may '
                'not. THE GENERAL PATTERN, which recurs throughout the course: when a '
                'resource is scarce and demand is uneven and moving, the value lies in '
                'matching allocation to demand in advance, and the ability to do so '
                'depends on whether the demand and the geometry are predictable.',
            ),
            (
                'Why does the way a model is trained across two sides of a link matter in '
                'a non-terrestrial setting?',
                'Some arrangements exchange results repeatedly, which a long link makes '
                'costly',
                [
                    'Models trained across two sides cannot be standardised by any '
                    'existing body',
                    'Only the satellite side holds enough gathered data for training to '
                    'be possible',
                    'Two-sided training requires that both ends run identical processing '
                    'hardware',
                ],
                'Training arrangements differ in how tightly the two ends must cooperate. '
                'Tightly coupled schemes exchange information repeatedly during training, '
                'and each exchange pays the link delay.',
                'THREE ARRANGEMENTS, distinguished by how much must cross the link during '
                'training. TRAINING AT ONE SIDE ONLY: simplest, since only one party '
                'trains and nothing needs to be exchanged mid-process. JOINT TRAINING '
                'ACROSS BOTH SIDES: the tightest coupling, requiring intermediate results '
                'to pass back and forth repeatedly as training proceeds. This assumes a '
                'fast, cheap link between the two ends. SEPARATE TRAINING WITH A SHARED '
                'DATASET: looser, since data is exchanged once rather than intermediate '
                'results continuously. WHY THE DISTINCTION MATTERS HERE: a satellite link '
                'is precisely the case where repeated exchange is expensive. The '
                'arrangement that is most attractive on a fast terrestrial connection is '
                'the least attractive across a long link, so the choice of training model '
                'is constrained by the deployment rather than by machine learning '
                'considerations alone. This is a good example of a general point: '
                'techniques developed under one set of assumptions about connectivity do '
                'not transfer unchanged to a setting where those assumptions fail.',
            ),
            (
                'Why is an incorrect beam prediction more damaging than an incorrect '
                'scheduling decision in a wide-beam system?',
                'Beams are narrow, so aiming one wrongly removes service rather than '
                'degrading it',
                [
                    'A wrong prediction corrupts the model and so degrades all of the '
                    'later decisions too',
                    'A wrong prediction causes the satellite to lose synchronisation with '
                    'the ground',
                    'A wrong prediction obliges every device in the cell to re-acquire '
                    'the carrier',
                ],
                'Directionality makes the failure mode binary rather than gradual. Energy '
                'aimed elsewhere is not weaker service, it is no service.',
                'THE FAILURE MODE IS THE POINT: with a broad, low-gain transmission, a '
                'suboptimal decision degrades quality. With a narrow, high-gain beam, a '
                'wrong decision means the energy went somewhere else entirely, and the '
                'intended users receive nothing. Highly directional systems convert '
                'graceful degradation into outage. WHY THIS RAISES THE STAKES FOR '
                'PREDICTION: a predictive system is being trusted to aim something that '
                'has no tolerance for being aimed wrongly. The accuracy requirement is '
                'therefore set by the consequence of error, not by average performance. '
                'THE RELATED PRACTICAL DIFFICULTY: models must be trained before they can '
                'be validated in the environment they will operate in. A system deployed '
                'on day one relies on models trained in simulation, and simulated orbital '
                'conditions may not match reality. THE CENTRAL TRADE the deck concludes '
                'on: steering beams to where capacity is actually needed raises '
                'efficiency, and the prediction that makes it possible must run on a '
                'payload with a hard power and thermal budget. Efficiency is bought with '
                'onboard computation, and that is the engineering decision at the heart '
                'of the topic.',
            ),
        ],
    },
    {
        "topic": 'GPS and Galileo',
        "source": 'Group 13 deck',
        "questions": [
            (
                'Why does a satellite navigation receiver need a fourth satellite when '
                'three ranges would fix a point in space?',
                'The receiver clock offset is a fourth unknown and needs a fourth measurement',
                [
                    'The fourth resolves an ambiguity between two points that three '
                    'spheres leave open',
                    'The fourth supplies a redundant measurement by which satellite '
                    'faults are detected',
                    'The fourth carries the ionospheric correction that the other three '
                    'cannot supply',
                ],
                "Three ranges would suffice if the receiver's clock agreed exactly with "
                "the satellites'. It does not, and that disagreement is an additional "
                'unknown requiring an additional measurement.',
                'THE COUNTING ARGUMENT: position in three dimensions is three unknowns. '
                'Ranging depends on measuring travel time, which requires knowing when '
                'the signal left and when it arrived. The satellites carry precise '
                'clocks, but a consumer receiver cannot, so its clock error is a fourth '
                'unknown. Four unknowns require four independent measurements. WHY THIS '
                'IS ELEGANT RATHER THAN MERELY AWKWARD: the clock error is COMMON to '
                'every measurement, since the same receiver clock times all of them. A '
                'single additional observation therefore resolves it for all satellites '
                'at once, which is why the requirement is four rather than six. WHAT '
                'FOLLOWS PRACTICALLY: a navigation receiver obtains precise time as a '
                'by-product of obtaining position. This is why satellite navigation '
                'underpins timing for telecommunications, power grids and financial '
                'systems, and it explains why a positioning system appears in a '
                'communications course at all. WHY THE MEASUREMENT IS CALLED A '
                'PSEUDORANGE: it is computed from an imperfect clock, so it is not the '
                'true geometric distance until the clock error has been solved for.',
            ),
            (
                'Why does clock accuracy dominate the design of a satellite navigation '
                'system?',
                'Distance is time multiplied by the speed of light, so tiny errors become '
                'large',
                [
                    'The satellites must stay synchronised with each other so their '
                    'signals do not collide',
                    'The receiver must predict when each satellite will next become '
                    'visible to it',
                    'The navigation message remains valid only for a strictly limited period',
                ],
                'Light travels a great distance in a very short time, so the conversion '
                'from time to distance amplifies any timing error enormously. That is why '
                'the satellites carry atomic clocks and why their drift is corrected '
                'continuously.',
                'THE AMPLIFICATION IS THE WHOLE PROBLEM: because the constant of '
                'proportionality between time and distance is the speed of light, a '
                'timing error that would be trivial in almost any other engineering '
                'context becomes a serious position error here. Errors at the level of '
                'millionths of a second correspond to hundreds of metres. WHAT FOLLOWS '
                'ARCHITECTURALLY. Satellites carry atomic clocks, because nothing less '
                'stable would suffice. A ground control network continuously monitors and '
                'corrects their drift, because even atomic clocks drift enough to matter. '
                'And the receiver solves for its own clock error rather than attempting '
                'to carry an accurate clock, because equipping every receiver with an '
                'atomic standard would be absurd. HOW MANY SATELLITES SHARE ONE '
                'FREQUENCY: all of them transmit on the same frequencies, distinguished '
                'by unique codes rather than by frequency or time slots. The receiver '
                'separates them by correlating against each code in turn, which also '
                'means an unlimited number of receivers can operate without consuming any '
                'system capacity. WHAT THE SIGNAL CARRIES: identification, precise '
                'timing, detailed orbit information for the transmitting satellite, and '
                'coarse orbit information for the whole constellation so a receiver can '
                'work out which satellites to look for.',
            ),
            (
                'What is the practical significance of two independent constellations '
                'sharing a civil frequency and a compatible signal design?',
                'One receiver tracks both, nearly doubling satellites and improving the '
                'geometry',
                [
                    'The two systems are able to share a single ground control '
                    'infrastructure between them',
                    'One system corrects the clock errors of the other directly while in '
                    'orbit',
                    'The two systems must coordinate their transmissions so as not to '
                    'interfere',
                ],
                'Compatibility means one receiver front end and one processing chain '
                'serve both. More satellites in view improves the spread of directions, '
                'which conditions the solution better.',
                'WHY MORE SATELLITES HELPS BEYOND REDUNDANCY: the accuracy of a position '
                'solution depends not only on how good each range measurement is, but on '
                'how the satellites are DISTRIBUTED across the sky. Satellites clustered '
                'together give a poorly conditioned solution in which measurement errors '
                'are magnified; satellites well spread give a well conditioned one. THIS '
                'IS THE CONCEPT OF DILUTION OF PRECISION, and it is different in kind '
                'from other error sources. It contributes no error of its own; it '
                'AMPLIFIES whatever errors already exist. So improving geometry improves '
                'accuracy even when every individual measurement is unchanged. WHY IT '
                'MATTERS MOST WHERE THE SKY IS OBSTRUCTED: in an urban canyon or under '
                'trees, many satellites are hidden and those remaining may be poorly '
                'spread. Doubling the population available makes it far more likely that '
                'a well-spread subset remains visible. THE OTHER BENEFITS follow from the '
                'same fact: faster and more reliable fixes in obstructed conditions, and '
                'resilience, since interference or degradation affecting one system '
                'leaves the other operating. Modern receivers routinely track several '
                'constellations at once for these reasons.',
            ),
            (
                'Which category of navigation error is different in kind from the others, '
                'and why?',
                'Dilution of precision, which adds nothing of its own but magnifies the rest',
                [
                    'Multipath, which arises near the receiver rather than out in the '
                    'constellation',
                    'Ionospheric delay, which varies with the time of day and with the '
                    'latitude',
                    'Receiver noise, which depends on hardware quality rather than the '
                    'environment',
                ],
                'The other sources each add a delay or a distortion. Dilution of '
                'precision is a property of satellite geometry that determines how '
                'strongly those errors propagate into the final position.',
                'GROUPING THE ERROR SOURCES BY ORIGIN is more useful than memorising '
                'magnitudes. PROPAGATION errors arise in the atmosphere, where the signal '
                'is slowed and bent. These dominate under most conditions and are worse '
                'at low elevation angles, because the path through the atmosphere is '
                'longer. SPACE SEGMENT errors arise from small drifts in satellite clocks '
                'and imperfections in predicted orbits. LOCAL errors arise near the '
                'receiver, most importantly reflection from nearby surfaces, which is '
                'site-specific and therefore cannot be corrected by information shared '
                'from elsewhere. RECEIVER errors arise from thermal noise and hardware '
                'imperfection, and are typically smallest. GEOMETRY is the exception: it '
                'adds nothing but scales everything. WHY THIS GROUPING IS USEFUL: it '
                'predicts which errors augmentation can remove. Propagation and '
                'space-segment errors are broadly common to receivers in a region, so a '
                'reference station can measure and share them. Local reflection is not '
                'shared and cannot be corrected this way. Geometry is improved by more '
                'satellites, not by corrections.',
            ),
            (
                'What do augmentation systems have in common regardless of the accuracy '
                'they achieve?',
                'Each compares an observed position with surveyed truth and shares the '
                'difference',
                [
                    'Each rebroadcasts an amplified copy of the original constellation signal',
                    'Each depends on carrier-phase measurements rather than on code '
                    'measurements',
                    'Each requires a geostationary satellite through which corrections '
                    'are relayed',
                ],
                'The shared mechanism is comparison against known truth. A station whose '
                'true position is already surveyed can attribute any discrepancy to error '
                'and share that measurement.',
                'THE UNIFYING PRINCIPLE: navigation errors are largely COMMON to '
                'receivers in the same region, because they arise from satellite clocks, '
                'orbit prediction and atmospheric conditions along similar paths. What '
                'one receiver measures is therefore useful to its neighbours. HOW THE '
                'SCHEMES DIFFER, conceptually. Some rely on a LOCAL reference station, '
                'which limits their range because the common-error assumption weakens '
                'with distance. Some compute corrections from a GLOBAL network and need '
                'no local station, at the cost of a convergence period before full '
                'accuracy is reached. Some improve the DELIVERY channel, using a '
                'wide-area broadcast to reach many receivers at once. And some change the '
                'OBSERVABLE itself, using carrier phase rather than code, which resolves '
                'position far more finely. WHY THE ACCURACY LADDER LOOKS AS IT DOES: '
                'schemes correcting code measurements reach the metre level, because that '
                'is the resolution of the underlying observable. Schemes exploiting '
                'carrier phase reach the centimetre level, because the observable is '
                'finer. The ordering follows from the physics, not from the '
                'sophistication of the correction. WHAT AUGMENTATION CANNOT FIX: local '
                'reflections, which differ from receiver to receiver, and poor geometry, '
                'which needs more satellites rather than better corrections.',
            ),
        ],
    },
    {
        "topic": 'Post-quantum cryptography for non-terrestrial networks',
        "source": 'Group 14 deck',
        "questions": [
            (
                'Which part of the current cryptographic stack does quantum computing '
                'most urgently threaten, and why?',
                'Public-key exchange and signatures, whose hard problems a quantum '
                'machine solves',
                [
                    'Symmetric encryption, since a quantum machine tests every key '
                    'simultaneously',
                    'Hash functions, since a quantum machine is able to invert them directly',
                    'The physical layer, since a quantum machine can demodulate any '
                    'waveform sent',
                ],
                'Public-key security depends on problems that are hard classically and '
                'tractable on a quantum computer. Symmetric and hash primitives are '
                'weakened but not broken in the same decisive way.',
                'WHERE THE THREAT IS CONCENTRATED, and getting this right matters because '
                'the naive answer is that quantum computing breaks all encryption. '
                'PUBLIC-KEY ALGORITHMS rest on specific mathematical problems believed '
                'hard for classical computers. A quantum algorithm solves exactly those '
                'problems efficiently, so the security assumption fails outright rather '
                'than merely weakening. These algorithms perform key exchange and '
                'authentication. SYMMETRIC ALGORITHMS AND HASH FUNCTIONS are affected '
                'differently and less severely, and can generally be strengthened by '
                'increasing key or output size rather than replaced. WHY THE DISTINCTION '
                'DRIVES THE MIGRATION: the urgent task is replacing the asymmetric layer, '
                'since that is where the failure is total. THE REPLACEMENTS are built on '
                'different mathematical foundations, chosen because no efficient quantum '
                'algorithm is known against them. Two roles must be filled: establishing '
                'a shared key, and producing signatures that authenticate. Both have been '
                'standardised, which is what allows migration to begin before the threat '
                'materialises.',
            ),
            (
                'Why is the threat described as present rather than future?',
                'Traffic recorded today is decrypted later, so long-lived secrets are '
                'exposed now',
                [
                    'Quantum machines already break the key lengths that are currently '
                    'deployed',
                    'The algorithms in question have been withdrawn from the relevant '
                    'standards',
                    'Satellites already in orbit are using algorithms that are known to '
                    'be broken',
                ],
                'An adversary needs only to record traffic today and wait. Any data whose '
                'confidentiality must outlast the arrival of quantum computing is '
                'therefore at risk immediately.',
                'THE HARVEST-NOW-DECRYPT-LATER ARGUMENT is the most important idea in '
                'this deck, because it determines the timing of the response. The naive '
                'view is that migration can wait until quantum computers exist. That view '
                'fails because interception and decryption need not happen at the same '
                'time. Traffic captured today can be stored indefinitely and decrypted '
                'whenever the capability arrives. WHAT FOLLOWS: the relevant question is '
                'not when quantum computers will exist, but how long your data must '
                'remain secret. If the secrecy lifetime extends past the expected arrival '
                'of the capability, the data is at risk now. WHY THIS BITES PARTICULARLY '
                'HARD IN SPACE: satellites have long service lives and cannot easily be '
                'upgraded after launch. A platform launched today with only classical '
                'cryptography may still be operating when the threat materialises, and by '
                'then it may be impossible to change. THE PRACTICAL CONSEQUENCE: the '
                'decision must be made before the threat is demonstrated, which is '
                'unusual in engineering and makes the argument for early migration a risk '
                'argument rather than a response to observed failure.',
            ),
            (
                'Why is the size of post-quantum keys and signatures a more serious issue '
                'on a satellite link than on a terrestrial one?',
                'Keys and signatures grow, and satellite capacity is scarce and costly to '
                'spend',
                [
                    'Satellite links impose a hard maximum packet size that larger keys '
                    'will exceed',
                    'The key must be retransmitted alongside every packet sent over a '
                    'satellite link',
                    'Satellite links carry no error correction, so larger keys are '
                    'corrupted often',
                ],
                'The overhead is a fixed property of the algorithms. What differs is the '
                'value of the capacity it consumes, and on a satellite link that capacity '
                'is the constrained resource.',
                'THE GENERAL PRINCIPLE: an overhead that is negligible where a resource '
                'is plentiful can be significant where it is scarce. The algorithms are '
                'not worse in space; the environment values what they consume more '
                'highly. THREE ENVIRONMENTAL OBSTACLES, none of which concerns the '
                'cryptography being weaker in orbit. CAPACITY: larger keys and signatures '
                'consume link capacity that is limited and costly. COMPUTATION: satellite '
                'processors are chosen for radiation tolerance rather than speed, so they '
                'lag ground hardware considerably, and the new algorithms are more '
                'demanding than those they replace. DELAY: a key exchange requiring '
                'several sequential exchanges pays the round-trip delay once per '
                'exchange, and on a long link that multiplication dominates connection '
                'setup and re-keying. WHY THE THIRD IS THE MOST INTERESTING: it is the '
                'same structural problem as the random access procedure, where a '
                'handshake of dependent exchanges becomes expensive purely because of '
                'link delay. Recognising that shape lets you predict which protocols will '
                'struggle in a non-terrestrial setting before analysing them in detail.',
            ),
            (
                'Why is running a classical and a post-quantum exchange together a '
                'sensible migration strategy?',
                'The session survives if either scheme holds, covering both kinds of failure',
                [
                    'It halves the computational cost compared with running either one of '
                    'them alone',
                    'It allows older equipment to connect without any modification being '
                    'needed',
                    'It is mandated by regulation for the duration of the transitional period',
                ],
                'The new algorithms are less battle-tested than the ones they replace. '
                'Combining them means an adversary must defeat both, so neither a quantum '
                'computer nor a flaw in the new scheme is sufficient alone.',
                'THE RISK BEING MANAGED is often overlooked. The obvious risk is that '
                'classical algorithms fall to quantum computing. The less obvious one is '
                'that the new algorithms, being newer and less scrutinised, may contain '
                'weaknesses not yet discovered. WHY A HYBRID ADDRESSES BOTH: if the '
                'session key depends on both exchanges, an attacker must break both. A '
                'quantum computer defeats only the classical half; a flaw in the new '
                'scheme defeats only the other half. Security survives either failure '
                'alone. THE COST is doing both, in computation and in the bytes '
                'exchanged, on links where both are constrained. That is a deliberate and '
                'reasonable price during a transition. THE BROADER SECURITY CONTEXT: the '
                'different link segments of a non-terrestrial network are protected by '
                'different mechanisms, because they face different threats. The link to '
                'the handset must protect subscriber identity and authenticate the device '
                'over a broadcast medium. The link between satellite and ground station '
                'and the connections within the ground network are protected by '
                'tunnelling and integrity mechanisms appropriate to their own exposure. '
                'Migration must consider each segment rather than treating the system as '
                'one uniform link.',
            ),
            (
                'What makes cryptographic agility particularly difficult for space systems?',
                'Service lives are long and upgrading in orbit is impractical once launched',
                [
                    'Space systems are not permitted to receive any software updates '
                    'while in orbit',
                    'Radiation effects prevent more than one algorithm being stored at '
                    'any time',
                    'International agreement fixes which algorithms a given satellite may use',
                ],
                'The ability to change algorithms later is limited by physical access. A '
                'platform designed around one set of assumptions may still be operating '
                'long after those assumptions have failed.',
                'WHY THIS COMPOUNDS THE HARVEST-NOW PROBLEM: the two arguments reinforce '
                'each other. Data captured today may be decrypted later, and a satellite '
                'launched today may still be generating that data when the capability '
                'arrives, without any practical means of being changed. WHAT THIS IMPLIES '
                'FOR DESIGN: cryptographic choices for space systems must anticipate the '
                "threat environment across the platform's whole service life, not merely "
                'its launch date. That is a longer horizon than most terrestrial systems '
                'require, where equipment is replaced or updated more readily. WHY IT '
                'ARGUES FOR AGILITY WHERE POSSIBLE: designing so that algorithms can be '
                'replaced by software update, rather than being fixed in hardware, '
                'preserves the ability to respond. Where that is not possible, the '
                'conservative choice is to over-provision security at design time. THE '
                'OVERALL ARGUMENT of the deck, stated as reasoning rather than as a '
                'conclusion to recite: current systems rely on cryptography that is sound '
                'against classical attack and vulnerable to a quantum one; the exposure '
                'begins as soon as traffic is recorded rather than when the attack '
                'becomes possible; and space platforms are the hardest to change once '
                'deployed. Together these justify migrating before the threat is '
                'demonstrated.',
            ),
        ],
    },
    {
        "topic": 'Doppler shift estimation in 5G NR non-terrestrial networks',
        "source": 'Group 15 deck',
        "questions": [
            (
                'Why does the Doppler shift on a satellite pass reach its extremes near '
                'the horizon and vanish overhead?',
                'Only motion along the line of sight counts, and that peaks low and '
                'vanishes overhead',
                [
                    'Atmospheric refraction is strongest near the horizon and is absent '
                    'overhead',
                    'The satellite travels fastest near the horizon and slowest at its '
                    'zenith point',
                    'Path loss is greatest near the horizon, and that broadens the '
                    'received spectrum',
                ],
                "The satellite's speed is essentially constant through the pass. What "
                'changes is the geometry: near the horizon it is closing almost directly '
                'toward the user, and overhead it is moving almost entirely across the '
                'line of sight.',
                'THE GEOMETRIC ARGUMENT, which explains the shape of every Doppler curve '
                'in the course. A frequency shift is produced by motion that changes the '
                'distance between transmitter and receiver. Motion perpendicular to the '
                'line of sight changes no distance and produces no shift. THROUGH A PASS: '
                'as the satellite rises, it is approaching almost directly, so the radial '
                'component is large and positive. As it passes overhead, its motion is '
                'almost entirely transverse, so the radial component crosses zero. As it '
                'sets, it is receding almost directly, so the shift is large and '
                'negative. A SECOND, LESS OBVIOUS CONSEQUENCE: the RATE at which the '
                'shift changes behaves oppositely. The shift changes most rapidly around '
                'the zenith, precisely where its magnitude is smallest. So the largest '
                'offset and the fastest-changing offset occur at different points in the '
                'pass, and a compensation scheme must handle both. WHY GEOSTATIONARY IS '
                'DIFFERENT: a satellite that holds position relative to the ground has '
                'almost no relative motion, so it produces almost no shift. The frequency '
                'problem is characteristic of low orbits, not of satellites in general.',
            ),
            (
                'Why does an uncompensated frequency offset damage an OFDM signal so '
                'severely?',
                "Subcarriers separate only while each peak sits on its neighbours' nulls",
                [
                    'The offset shortens the cyclic prefix below the delay spread of the '
                    'channel',
                    'The offset inverts the constellation mapping applied on every subcarrier',
                    'The offset makes frame timing drift outside the permitted '
                    'transmission window',
                ],
                'Orthogonality is a frequency-alignment property. Shifting the whole set '
                'of subcarriers moves each peak off the point where its neighbours '
                'contribute zero, so they begin to interfere with one another.',
                'WHY OFDM IS ARRANGED AS IT IS: subcarriers are packed close together and '
                'deliberately overlap, with no guard bands between them. This is far more '
                'spectrally efficient than separating them, and it works because at the '
                'exact centre frequency of each subcarrier, every other subcarrier '
                'contributes exactly zero. WHAT ORTHOGONALITY DEPENDS ON: that '
                'cancellation holds only at those precise frequencies. It is a property '
                'of alignment, not a property of the signals in isolation. WHY A DOPPLER '
                'SHIFT IS THEREFORE SO DAMAGING: it moves the entire set of subcarriers '
                'relative to where the receiver expects them. The receiver samples where '
                'the nulls used to be, and finds that neighbouring subcarriers now '
                'contribute energy there. Each subcarrier leaks into the others, which is '
                'inter-carrier interference. WHY THE PAYLOAD TYPE CHANGES THE MAGNITUDE: '
                'if the satellite does not demodulate, the signal traverses both the user '
                'link and the gateway link, and both are affected by motion, so the '
                'shifts accumulate. If the satellite demodulates on board, the user-link '
                'shift is terminated there and does not propagate further.',
            ),
            (
                'Why does making the standard approach depend on a navigation receiver in '
                'every device create a systemic weakness?',
                'Every later step needs the position, so losing the fix denies access '
                'entirely',
                [
                    'Navigation receivers cannot operate on the frequencies that NTN '
                    'services use',
                    'Navigation signals cannot be received at the same time as the device '
                    'transmits',
                    'Navigation receivers need a subscription that not every device '
                    'actually holds',
                ],
                "The scheme computes the correction from the device's position and the "
                "satellite's published orbit. Without a position fix the computation "
                'cannot begin, so the dependency becomes a single point of failure.',
                'THE STANDARD APPROACH IN OUTLINE: the satellite broadcasts its orbital '
                'position and velocity; the device determines its own coordinates from a '
                'navigation fix; from the two it computes the expected frequency offset; '
                'and it pre-corrects its transmission accordingly. WHERE THE FRAGILITY '
                'LIES: every step after the first depends on the second. The elegance of '
                'the scheme is also its weakness, since it converts network access into a '
                'dependency on a separate system. WHY THAT DEPENDENCY IS UNRELIABLE IN '
                'PRACTICE. Navigation signals arriving from distant satellites are '
                'extremely weak, so obstruction by buildings, foliage or structures '
                'removes the fix. They are correspondingly easy to jam or spoof, which '
                "places the dependency under an adversary's control. Low-cost devices, "
                'exactly those a mass-market service would target, may not include a '
                'navigation receiver at all. And the offset a device measures mixes true '
                'motion-induced shift with drift in its own local oscillator, so even a '
                'device with a fix cannot cleanly separate the two causes. WHAT MOTIVATES '
                'THE ALTERNATIVES: each addresses one of these failures, and the general '
                'approach is to estimate the offset from the received signal itself '
                'rather than computing it from external position information.',
            ),
            (
                'Why is the frequency offset separated into a whole-subcarrier part and a '
                'fractional part?',
                'The two leave different signatures, so each needs its own kind of '
                'measurement',
                [
                    'One part affects the uplink direction while the other part affects '
                    'the downlink',
                    'Conformance rules require the two components to be reported to the '
                    'network',
                    'Only the fractional part varies as the satellite moves along its '
                    'orbital path',
                ],
                'A shift of a whole number of subcarrier spacings and a shift of a '
                'fraction of one leave different signatures, so estimating each requires '
                'exploiting a different property of the signal.',
                'WHY THE SPLIT IS NATURAL: subcarriers are regularly spaced, so a shift '
                "of exactly one spacing moves each subcarrier onto its neighbour's "
                'position. Such a shift is not detectable by examining the relationship '
                'between adjacent subcarriers, because that relationship looks unchanged. '
                'Only the fractional part disturbs it. RECOVERING THE FRACTIONAL PART: a '
                'portion of each transmitted symbol is repeated deliberately, as a guard '
                'against timing spread. Because it is an exact repeat, comparing the '
                'repeated portion with the original reveals a phase difference that is '
                'proportional to the frequency offset. This costs nothing extra, since '
                'the repetition is already present in every symbol. RECOVERING THE '
                'WHOLE-SUBCARRIER PART: the synchronisation signals are known sequences '
                'at known positions, so searching across candidate whole-subcarrier '
                'shifts and taking the best match identifies how far the signal has '
                'moved. THE PRINCIPLE WORTH GENERALISING: when a quantity cannot be '
                'measured directly, look for redundancy already present in the signal. '
                'Exploiting structure that exists for another purpose is cheaper than '
                'adding new reference signals, which is why methods based on existing '
                'structure have the lowest overhead of the alternatives.',
            ),
            (
                'What advantage does predictive tracking offer over methods that estimate '
                'the offset from each measurement independently?',
                'It follows an underlying trajectory, so the estimate survives brief '
                'interruptions',
                [
                    'It requires no reference signals of any kind once it has been '
                    'initialised',
                    'It removes the need for any initial position information to be supplied',
                    'It removes the offset outright rather than merely producing an '
                    'estimate of it',
                ],
                'A tracking filter models how the quantity evolves, so it can continue '
                'predicting when observations are momentarily unavailable and it smooths '
                'measurement noise.',
                'THE DIFFERENCE BETWEEN ESTIMATING AND TRACKING: an independent estimate '
                'uses only the current observation, so it is as noisy as that observation '
                'and fails entirely when the observation is missing. A tracking filter '
                'maintains a model of how the quantity is changing, uses each observation '
                'to refine that model, and can predict forward when observations stop. '
                'WHY THIS SUITS THE PROBLEM: the offset does not vary arbitrarily. It '
                'follows a smooth trajectory determined by orbital geometry, so a filter '
                'that models satellite position, velocity and acceleration, together with '
                "drift in the device's own oscillator, is modelling something that "
                'genuinely behaves that way. THE PRACTICAL BENEFIT: brief signal '
                'blockages, which are common for a user moving among buildings or '
                'foliage, no longer cause loss of lock, because the filter continues '
                'predicting through the gap. THE COSTS: greater computational load than '
                'an algebraic calculation, and reliance on the model being correct. A '
                'filter tracking a trajectory the system is not actually following will '
                'confidently produce wrong answers. THE COMPARISON ACROSS ALL THE '
                'APPROACHES: they trade dependence on external systems, overhead in '
                'transmitted reference signals, computational cost, and robustness to '
                'interference. No single method wins on all four, which is why several '
                'coexist.',
            ),
        ],
    },
    {
        "topic": 'Network slicing in non-terrestrial networks',
        "source": 'Group 16 deck',
        "questions": [
            (
                'What does network slicing actually divide, given that the physical '
                'resources remain shared?',
                'How traffic is treated, so each slice behaves as though it had its own '
                'network',
                [
                    'The satellite footprint, into a set of smaller geographic service areas',
                    'The frequency band, into fixed sub-bands that are allocated to each '
                    'operator',
                    'The core network, into separate control-plane and user-plane '
                    'installations',
                ],
                'Spectrum, payload, transport and core compute stay shared. What is '
                'partitioned is how traffic is scheduled, queued and prioritised, so each '
                'slice behaves as though it had its own network.',
                'THE CENTRAL IDEA: one physical network, several logical networks, each '
                'configured end to end for a different kind of service. The partition is '
                'in behaviour rather than in hardware. WHY IT IS NEEDED: different '
                'services want incompatible things. A video service wants a wide pipe and '
                'tolerates delay. A control or safety application wants guaranteed low '
                'delay and sends very little. A sensor population sends tiny messages '
                'from enormous numbers of devices. Optimising one network for all three '
                'is impossible, so the network is made to present a different face to '
                'each. WHY IT SUITS A SATELLITE PARTICULARLY: a single platform must '
                'serve all these services simultaneously, and it cannot be duplicated. '
                'Slicing lets one scarce asset behave like several tailored networks, '
                'which is more valuable in orbit than on the ground where additional '
                'capacity can simply be built. THE ENABLING TECHNOLOGY is virtualisation, '
                'which is what allows logical separation without physical separation.',
            ),
            (
                'Which service class does the propagation delay of a satellite link make '
                'impossible to support in the usual sense?',
                'Low-latency service, whose defining bound is smaller than the round trip '
                'itself',
                [
                    'Enhanced broadband, because its throughput target cannot be reached '
                    'from orbit at all',
                    'Machine-type communication, because too many devices must be '
                    'supported at once',
                    'None of them, because slicing isolates a service from the underlying '
                    'delay',
                ],
                'The low-latency class is defined by a delay bound of around a '
                'millisecond. Physics places the satellite round trip well above that '
                'before any processing is added.',
                'WHY THIS IS A HARD LIMIT RATHER THAN AN ENGINEERING CHALLENGE: the delay '
                'comes from distance and the speed of light. No amount of processing '
                'improvement, scheduling cleverness or protocol design reduces it. A '
                'latency guarantee smaller than the propagation time cannot be met by any '
                'implementation. WHAT THAT MEANS IN PRACTICE: the service class can still '
                'exist over a satellite link, but its guarantee must be restated. A slice '
                'can offer priority scheduling, short queues and reliability, while its '
                'absolute latency bound is set by the orbit rather than by the network. '
                'Selling it under the terrestrial definition would be dishonest. WHY THIS '
                'IS WORTH UNDERSTANDING GENERALLY: several 5G service definitions encode '
                'assumptions about scale that non-terrestrial deployment violates. '
                'Recognising which requirements are physically bounded, and which are '
                'merely difficult, is the useful distinction. THE OTHER CLASSES SURVIVE '
                'BETTER: a wide, delay-tolerant pipe is unaffected in kind, and a '
                'store-and-forward sensor service is barely affected at all, since it was '
                'never latency-sensitive.',
            ),
            (
                'Why must isolation between slices be logical rather than physical on a '
                'satellite?',
                'One payload and one spectrum pool serve every slice, so hardware cannot '
                'be split',
                [
                    'Standards forbid physical separation from being used in '
                    'non-terrestrial systems',
                    'Slice identifiers are stripped from traffic as it crosses the '
                    'gateway link',
                    'Satellites are unable to run virtualisation software while they are '
                    'in orbit',
                ],
                'On the ground a tenant demanding strict isolation can be given separate '
                'equipment. A satellite cannot carry duplicate payloads per slice, so '
                'separation must be enforced in software over shared resources.',
                'THE CONSTRAINT THAT FORCES THIS: everything aboard costs mass and power, '
                'both of which are strictly limited. Duplicating hardware per tenant is '
                'not an option in the way it is in a terrestrial data centre or base '
                'station. WHAT LOGICAL ISOLATION MEANS: separation is enforced by '
                'scheduling and configuration rather than by physical partition. It can '
                'be made strong, but it is a software guarantee over shared hardware, and '
                'it is worth being honest about that distinction when a tenant asks for '
                'isolation. THE THREE OTHER STRUCTURAL DIFFICULTIES, all following from '
                'motion rather than from scarcity. The radio cell does not stay still, so '
                'a slice anchored to a cell must be re-anchored to a new satellite every '
                'few minutes. The transport path re-configures itself as gateway '
                'connections change and traffic is re-routed between satellites, so the '
                "slice's underlying path changes mid-session. And service agreements must "
                'therefore be re-established repeatedly rather than configured once. THE '
                'CONTRAST WITH TERRESTRIAL SLICING: there, a slice is pinned to a fixed '
                'cell and a fixed transport path, and can be configured and left alone. '
                'In orbit, both the cell and the path are in continuous motion, which is '
                'why orchestration must be driven by predicted geometry rather than by a '
                'static plan.',
            ),
            (
                'Why does guaranteeing capacity to a slice that is not currently using it '
                'constitute a real cost in orbit?',
                'Reserved capacity is withheld whether used or not, on a power-limited '
                'payload',
                [
                    'An idle slice continues to draw transmit power at its full allocated '
                    'rate regardless',
                    'Capacity once reserved to a slice cannot be released back for other '
                    'traffic',
                    'An idle slice generates signalling traffic in proportion to its '
                    'reserved size',
                ],
                'Isolation means fencing resources off. On a platform with a hard power '
                'and capacity budget, fenced-off capacity that goes unused is a direct '
                'loss rather than an accounting formality.',
                'THE TRADE AT THE HEART OF SLICING: isolation and efficiency oppose each '
                'other. Strong guarantees require reserving resources, and reserved '
                'resources cannot be reassigned to whoever needs them most at that '
                'moment. On the ground this is tolerable because capacity can be added; '
                'in orbit it cannot. THE OTHER COSTS, each paired with the benefit that '
                'causes it. Per-slice identifiers, buffering and separate keys add '
                'overhead to every packet on a link that is already long and '
                'capacity-limited. Re-establishing service agreements at every handover '
                'and gateway change generates heavy control signalling. Moving core '
                'functions aboard, which is what allows local handling, consumes power '
                'and generates heat the platform may struggle to shed. And a slice that '
                'spans a network operator, a satellite owner and a regulator raises the '
                'question of who is accountable for the end-to-end guarantee, which '
                'remains unresolved. THE HABIT WORTH FORMING: for each benefit slicing '
                'offers, identify the resource it is drawn from. Presenting slicing as '
                'free capability is the weakest possible answer.',
            ),
            (
                'What is meant by describing orchestration in a non-terrestrial network '
                'as orbit-aware?',
                'Policy is planned from predicted motion rather than from a fixed cell plan',
                [
                    'Slices are assigned according to the orbital altitude of the serving '
                    'satellite',
                    'Each orbital plane in the constellation is allocated a dedicated '
                    'slice of its own',
                    'The orchestration function itself runs aboard the satellite rather '
                    'than on ground',
                ],
                'Because the cell and the transport path move predictably, the management '
                "system can plan against the constellation's known future geometry "
                'instead of reacting to changes as they occur.',
                'WHY A STATIC PLAN FAILS: terrestrial orchestration configures a slice '
                'across a known cell and a known transport path, and that configuration '
                'remains valid indefinitely. In orbit neither remains valid for more than '
                'a few minutes. WHAT REPLACES IT: because orbital motion is '
                'deterministic, the times at which a slice must be re-anchored, and the '
                'points at which its transport path will change, can be computed in '
                'advance. Orchestration can therefore schedule those changes rather than '
                'discover them. WHY THIS IS THE SAME IDEA SEEN ELSEWHERE: predictive '
                'handover, ephemeris-based timing correction, and predicted beam '
                'selection all rest on the same property, that satellite motion is known '
                'in advance. Slicing applies it at the management layer rather than the '
                'radio layer, but the underlying justification is identical. THE '
                'MANAGEMENT STRUCTURE follows the usual pattern of decomposition: '
                'customer requirements are captured, translated into an end-to-end slice, '
                'and then delegated to managers responsible for the radio segment and for '
                'the core and transport segments respectively. Each layer handles what it '
                'can see, which is the same separation-of-concerns principle that appears '
                'in the radio access architecture.',
            ),
        ],
    },
]
