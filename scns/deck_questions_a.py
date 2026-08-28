# -*- coding: utf-8 -*-
"""TE 456 question data, groups 1 to 8.

Format per question:
    (stem, correct_answer, [distractor, distractor, distractor], explanation)

See build_questions.py for how these are compiled.
"""

DECKS = [
    {
        "topic": "Timing advance and frequency offset compensation in LEO NTN",
        "source": "Group 1 deck, slides 2 to 9",
        "questions": [
            (
                "A user device computes its timing advance from satellite ephemeris and its own GNSS position, and applies it before sending its first preamble. Which stage of the correction chain is this?",
                "Open-loop timing advance",
                [
                    "Closed-loop frequency offset compensation",
                    "The Timing Advance command procedure",
                    "Residual tracking by the numerically controlled oscillator",
                ],
                "Open loop means proactive: the device predicts the correction from geometry it already knows, and applies it before it has ever transmitted. The closed loop only starts once the network has measured a real uplink.",
            ),
            (
                "Why can closed-loop timing advance never remove the timing error completely?",
                "The correction is based on geometry that is at least one round trip old",
                [
                    "The MAC control element cannot carry a large enough correction value",
                    "The base station measures arrival time with limited resolution only",
                    "The satellite clock and the device clock use different time references",
                ],
                "Feedback always trails the true geometry by at least one round trip. On a LEO link the geometry moves during that round trip, so a residual error is left behind no matter how accurate the measurement was.",
            ),
            (
                "In a transparent payload the end-to-end Doppler is roughly double that of the service link alone. What causes the doubling?",
                "The feeder link between the satellite and the gateway adds its own shift",
                [
                    "The uplink and the downlink carriers are at different frequencies",
                    "The signal is sampled twice, once on board and once at the gateway",
                    "Inter-satellite links re-transmit the signal to a second spacecraft",
                ],
                "A transparent payload does not demodulate. The signal crosses the service link and then the feeder link, and each moving segment contributes a Doppler shift, so the two add.",
            ),
            (
                "The device predicts Doppler as fD = (Vr / c) x fc. What does Vr stand for?",
                "The component of relative velocity along the line of sight",
                [
                    "The full orbital speed of the satellite",
                    "The ground speed of the user device",
                    "The rate at which the elevation angle is changing",
                ],
                "Doppler responds only to the closing or opening rate along the line of sight. At the zenith of a pass the satellite is moving fast but almost none of that motion is radial, so the shift crosses zero.",
            ),
            (
                "Which pair of inputs does the open-loop stage need before the device has transmitted anything at all?",
                "Satellite ephemeris and the device's own GNSS position",
                [
                    "A Timing Advance command and an AFC error estimate",
                    "Received signal strength and the current beam identity",
                    "Feeder link Doppler and the gateway clock offset",
                ],
                "Two positions give a range, and a range gives a delay and a radial velocity. Everything else in the list is either a measurement the network has not made yet or a quantity the device cannot see.",
            ),
            (
                "A stale ephemeris file degrades performance. Which stage suffers first and worst?",
                "The open loop, because its prediction is built on the orbit data",
                [
                    "The closed loop, because the correction command becomes invalid",
                    "Neither, because GNSS timing overrides the ephemeris",
                    "Both equally, because they share the same estimate",
                ],
                "The open loop is pure prediction from the orbit, so bad orbit data corrupts it directly. The closed loop measures the real signal, so it is the stage that partly rescues a stale prediction.",
            ),
            (
                "What is the stated cost of issuing timing advance commands and AFC updates frequently?",
                "Uplink and downlink capacity is spent that could otherwise carry data",
                [
                    "The device battery drains faster than the payload can support",
                    "The satellite must carry a larger soft buffer",
                    "The cyclic prefix must be lengthened for every user",
                ],
                "Corrections are signalling, and signalling occupies the same radio resources as user traffic. Correcting more often buys accuracy and pays for it in throughput.",
            ),
            (
                "Which correction is the network side, rather than the device side, responsible for?",
                "Feeder link Doppler and the residual measurement",
                [
                    "Service link Doppler pre-compensation",
                    "The initial timing advance before the first PRACH",
                    "The GNSS position fix used in the open loop",
                ],
                "The split follows what each end can observe. The device sees its own service link and pre-corrects it. Only the network sees the feeder link and the residual error in the arriving signal.",
            ),
            (
                "Compared with a terrestrial cell link, the round-trip time on a LEO link is best described as:",
                "Long and fast-changing",
                [
                    "Short and stable",
                    "Long but essentially constant over a pass",
                    "Short but highly variable",
                ],
                "Both properties matter. Length alone could be absorbed by a fixed offset. It is the fact that the length keeps changing during a pass that forces a continuous correction loop.",
            ),
            (
                "Which statement captures the design pattern shared by timing advance and frequency offset compensation?",
                "Predict from known geometry, then refine from real measurement",
                [
                    "Measure first, then predict the next value from the measurement history",
                    "Let the network compute everything and broadcast one common value",
                    "Avoid prediction entirely and rely on a long cyclic prefix",
                ],
                "This is the open-loop then closed-loop pattern stated in the conclusion. Prediction gets the device close enough to be heard at all; measurement closes the remaining gap.",
            ),
        ],
    },
    {
        "topic": "UAV-enhanced 3D beamforming for rural 5G NTN",
        "source": "Group 2 deck, slides 2 to 8",
        "questions": [
            (
                "Why does a UAV base station need beam steering in elevation, when a terrestrial macro cell largely does not?",
                "The users lie below the platform, so the useful angles are vertical as well as horizontal",
                [
                    "Elevation steering is required to reduce Doppler on the feeder link",
                    "Regulations cap the azimuth beamwidth of airborne transmitters",
                    "Elevation steering compensates for the rotation of the Earth",
                ],
                "A tower stands among its users, so the interesting variation is horizontal. A UAV hovers above them, so the angle down to a user changes with range, and elevation becomes a real steering axis.",
            ),
            (
                "What is the main engineering reason for choosing hybrid beamforming rather than fully digital beamforming on a UAV?",
                "It uses fewer RF chains than antenna elements, which saves size, weight and power",
                [
                    "It gives a wider beam, which tolerates platform tilt better",
                    "It removes the need for any baseband processing on board",
                    "It allows the UAV to serve users on more than one carrier frequency",
                ],
                "A fully digital array needs one RF chain per element. Hybrid beamforming puts a digital precoder behind an analog phase-shift network, so a large array is driven by a small number of chains, which is what an aircraft can lift and power.",
            ),
            (
                "The control loop runs sense, optimize, act, learn. Which weakness does this loop introduce?",
                "Convergence takes time, so link quality dips during fast movement",
                [
                    "It cannot handle users that stay in one place for long periods",
                    "It requires every user device to run the same learning model",
                    "It prevents the UAV from changing altitude once deployed",
                ],
                "A closed learning loop is always chasing the state it last observed. When the geometry changes faster than the loop converges, the beam is briefly aimed at where the users were rather than where they are.",
            ),
            (
                "Predictive beam tracking is preferred over repeated exhaustive beam search mainly because:",
                "It holds alignment without the overhead of re-searching every beam",
                [
                    "Exhaustive search cannot find the correct beam at high elevation angles",
                    "Prediction removes the need for a phase-shift network",
                    "Exhaustive search is forbidden by the 3GPP NTN specification",
                ],
                "Sweeping every beam costs time and signalling on every update. Predicting the next weights from the motion already observed reaches the same alignment for a fraction of that overhead.",
            ),
            (
                "In the multi-tier backhaul, what carries traffic out of the target area?",
                "Inter-UAV mesh links leading up to a HAPS or satellite feeder link",
                [
                    "A new fibre spur laid to the nearest terrestrial exchange",
                    "A dedicated ground tower built at the edge of the coverage zone",
                    "Direct device-to-device relaying between the rural user terminals",
                ],
                "The whole point is to avoid building anything on the ground. UAVs relay to each other and then upward, so no fibre and no tower is needed inside the target area.",
            ),
            (
                "Altitude is treated as a decision variable rather than a fixed setting. Which trade-off does it control?",
                "Line-of-sight probability against path loss",
                [
                    "Transmit power against receiver noise figure",
                    "Beam count against subcarrier spacing",
                    "Backhaul latency against onboard storage",
                ],
                "Climbing improves the chance of a clear path over terrain and buildings, and at the same time lengthens every link. The best altitude is wherever those two effects balance for the terrain below.",
            ),
            (
                "Which limitation is described as competing directly with the UAV's endurance?",
                "The power drawn by the beamforming hardware and the AI control loop",
                [
                    "The weight of the antenna array on its own",
                    "The bandwidth reserved for the feeder link",
                    "The time taken to compute the digital precoder weights",
                ],
                "On an aircraft the payload and the propulsion draw from one battery. Every watt spent on phase shifters and inference is a watt not spent staying airborne.",
            ),
            (
                "Backhaul fragility is listed as a risk. What is the specific failure mode?",
                "One weak link in the chain degrades coverage for everything downstream of it",
                [
                    "Two UAVs transmit on the same beam and interfere",
                    "The satellite feeder link exceeds its power flux density mask",
                    "The mesh loses time synchronisation and the beams misalign",
                ],
                "A multi-tier mesh is a chain of dependencies. A UAV that relays through a neighbour inherits that neighbour's problems, so a single weak hop cascades outward.",
            ),
            (
                "Which of these is given as a real-world application of the approach?",
                "Temporary coverage for festivals and other large events",
                [
                    "Precision timing distribution for financial trading networks",
                    "Space debris tracking from a UAV-borne radar",
                    "Inter-continental undersea cable protection monitoring",
                ],
                "The listed cases are rural education and distance learning, temporary event coverage, border surveillance and post-disaster response. All four share a need for coverage that appears and then goes away.",
            ),
            (
                "The conclusion argues that the binding constraint is system-level. What does that mean in practice?",
                "Altitude, beam accuracy, terrain and backhaul have to be optimized together",
                [
                    "The UAV must be replaced by a HAPS for the system to work",
                    "Only the weakest single radio link needs to be improved",
                    "The AI model must be trained on data from the exact deployment site",
                ],
                "Improving one variable in isolation moves the bottleneck rather than removing it. Flying higher helps line of sight and hurts path loss, so the variables have to be solved jointly.",
            ),
        ],
    },
    {
        "topic": "Machine learning for RACH optimization in NTN",
        "source": "Group 3 deck, slides 2 to 12",
        "questions": [
            (
                "Why is the four-step RACH handshake especially costly over a satellite link?",
                "The four messages amount to two full satellite round trips before any data moves",
                [
                    "Each of the four messages must be encrypted separately",
                    "The preamble has to be repeated once per orbital plane",
                    "The base station cannot process message 3 while in view of the user",
                ],
                "Messages 1 and 2 are one round trip and messages 3 and 4 are another. On the ground that is about a millisecond. Over a satellite it is tens of milliseconds spent before a single byte of user data has been sent.",
            ),
            (
                "Differential delay across a narrow LEO beam is about 650 microseconds, and the longest protective cyclic prefix is 684 microseconds. What does that imply?",
                "Only about 34 microseconds of margin remains, and wider beams erase it",
                [
                    "The cyclic prefix is comfortably oversized for LEO operation",
                    "Differential delay can be ignored because it sits below the prefix length",
                    "Two preambles must be sent, one for the centre and one for the edge",
                ],
                "The two figures nearly cancel. The guard barely covers the spread today, so any wider beam or higher orbit pushes edge preambles outside the window entirely.",
            ),
            (
                "What happens when two devices pick the same PRACH preamble?",
                "A collision occurs, and both devices must retry one round trip later",
                [
                    "The network serves the stronger device and silently drops the weaker one",
                    "The preambles combine and the base station decodes both correctly",
                    "The base station shortens the backoff window for both devices",
                ],
                "The preamble is the only thing distinguishing one attempt from another, so identical preambles are indistinguishable. Both attempts fail and both devices pay a full round trip to try again.",
            ),
            (
                "Doppler over one LEO pass swings from about +48 kHz to about -48 kHz. What does this do to the RACH?",
                "The preamble is smeared, so correlation at the receiver degrades",
                [
                    "The device is barred from transmitting during the sign reversal",
                    "The random access response arrives on the wrong subcarrier",
                    "The cyclic prefix is stretched by the frequency change",
                ],
                "Preamble detection is a correlation against a known shape. A frequency offset that moves during the preamble distorts that shape, so the correlation peak drops and detections are missed.",
            ),
            (
                "In the learning loop, what does the reward signal combine?",
                "Success, delay and energy",
                [
                    "Beam index, elevation angle and slant range",
                    "Collision count, subcarrier spacing and preamble length",
                    "Throughput, ephemeris age and satellite battery state",
                ],
                "The reward has to express what a good access attempt looks like: it got through, it did not take long, and it did not cost much power. The policy is then tuned to maximise that combination.",
            ),
            (
                "The predictive or ephemeris-aided family is described differently from the other two. Why?",
                "It is deterministic geometry, and it is the Release 17 baseline that a learned policy must beat",
                [
                    "It runs only on the satellite and never on the device",
                    "It requires far more training data than the other families",
                    "It has been shown to perform worse than fixed 3GPP parameters",
                ],
                "Supervised learning and reinforcement learning both learn from data. Pre-compensating from a known orbit learns nothing; it computes. That makes it the benchmark rather than a competing learned method.",
            ),
            (
                "Reinforcement learning is applied to which RACH parameters?",
                "The barring probability, the backoff window and the preamble pool split",
                [
                    "The carrier frequency and the subcarrier spacing",
                    "The cyclic prefix length and the guard period",
                    "The number of HARQ processes and the soft buffer size",
                ],
                "These are the contention controls, the values a network operator would otherwise fix at design time. They are exactly the knobs a policy can turn in response to observed load.",
            ),
            (
                "The reported eRACH result includes a factor of 4.94. What does it measure?",
                "The increase in collision rate, which is the cost paid for the gain",
                [
                    "The improvement in throughput over fixed rules",
                    "The reduction in access delay",
                    "The growth in the number of devices that can be served",
                ],
                "The gains quoted are +31.2 percent and +54.6 percent throughput and 1.49 times lower delay. The 4.94 figure runs the other way: the learned policy is more aggressive, so it collides more often.",
            ),
            (
                "Why is heat listed as an onboard limitation separate from power?",
                "Onboard inference generates heat with no way to vent it in vacuum",
                [
                    "Heat corrupts the stored neural network weights",
                    "Thermal noise raises the false preamble detection rate",
                    "Heat causes the solar panels to lose efficiency during eclipse",
                ],
                "On the ground a processor sheds heat into the air. In vacuum there is no convection, so the only path is radiation, and continuous inference produces heat faster than a small payload can radiate it.",
            ),
            (
                "Which design-process limitation makes regulatory approval difficult?",
                "A black-box policy is hard to certify against 3GPP conformance",
                [
                    "The scarcity of real NTN random-access traces",
                    "The gap between simulated and real channels",
                    "The cost of running simulations across many orbital geometries",
                ],
                "The other three are engineering obstacles that better data or more compute would ease. Certification is different: a learned policy has no fixed behaviour to test against a written specification.",
            ),
        ],
    },
    {
        "topic": "GPS signal integration and augmentation in 5G-NTN",
        "source": "Group 4 deck, slides 2 to 16",
        "questions": [
            (
                "What is the essential difference between DGPS and PPP?",
                "DGPS needs a nearby surveyed base station, and PPP does not",
                [
                    "DGPS uses carrier phase while PPP uses code measurements only",
                    "DGPS corrects the ionosphere while PPP corrects the troposphere",
                    "DGPS works globally while PPP is limited to a single country",
                ],
                "PPP takes precise orbit and clock products computed by a global monitoring network, so the receiver needs no local reference. DGPS depends on a base station close enough to share the same errors.",
            ),
            (
                "In DGPS, how is the correction value derived?",
                "From the difference between the base station's surveyed position and its GPS-computed position",
                [
                    "From the carrier phase difference between two satellites in view",
                    "From a model of ionospheric delay held at the master station",
                    "From averaging the positions reported by all nearby rovers",
                ],
                "The base station already knows exactly where it is. Any disagreement between that truth and what GPS reports is the current error, and that error is what gets broadcast to nearby receivers.",
            ),
            (
                "Which technique reaches centimetre-level accuracy by using carrier-phase measurements between a base and a rover?",
                "RTK",
                [
                    "SBAS",
                    "DGPS",
                    "PPP",
                ],
                "RTK is quoted at 1 to 2 cm. Carrier phase resolves position to a fraction of a wavelength, which is far finer than the code measurements DGPS relies on.",
            ),
            (
                "In SBAS, what does the geostationary satellite actually do?",
                "It broadcasts the correction messages that were computed on the ground",
                [
                    "It measures the GPS errors directly using its own receiver",
                    "It replaces a failed GPS satellite in the constellation",
                    "It relays the user position back to the master control station",
                ],
                "The errors are detected by surveyed reference stations and turned into correction messages by a master control station. The GEO satellite is only the broadcast channel that carries them over a wide area.",
            ),
            (
                "A node transmits a positioning signal, the device replies, and the node halves the measured delay. Which technique is this?",
                "Round Trip Time",
                [
                    "Time of Arrival",
                    "Angle of Arrival",
                    "Trilateration from ephemeris",
                ],
                "The halving is the giveaway. Measuring a two-way delay and dividing by two removes the need for the transmitter and the receiver to share a clock, which is what a one-way Time of Arrival measurement would require.",
            ),
            (
                "Angle of Arrival needs something that Time of Arrival does not. What?",
                "An antenna array able to resolve the direction the signal came from",
                [
                    "A precisely synchronised clock at the transmitter",
                    "Knowledge of the satellite ephemeris",
                    "A carrier-phase capable receiver",
                ],
                "AoA works on direction rather than distance, and direction is recovered from the phase differences across the elements of an array. A single antenna cannot tell you where a signal came from.",
            ),
            (
                "Why is 5G-NTN a useful complement to GPS in urban canyons and indoors?",
                "NTN platforms supply extra measurements where the sky view is blocked",
                [
                    "NTN signals are transmitted at a much lower carrier frequency",
                    "NTN removes the need for trilateration entirely",
                    "NTN satellites orbit lower and therefore penetrate buildings",
                ],
                "GPS fails in those places because too few satellites are visible. Adding ToA, AoA and RTT measurements from NTN platforms restores enough observations to solve for position.",
            ),
            (
                "SBAS is stated to improve accuracy from what range to what range?",
                "From 5 to 10 metres down to about 1 to 2 metres",
                [
                    "From 1 to 3 metres down to about 20 centimetres",
                    "From 20 metres down to about 5 metres",
                    "From 1 to 2 metres down to about 1 to 2 centimetres",
                ],
                "SBAS sits in the middle of the augmentation ladder. DGPS reaches 1 to 3 m, PPP about 5 to 20 cm after convergence, and RTK 1 to 2 cm.",
            ),
            (
                "Which statement about the user segment of GPS is correct?",
                "It consists of the receivers and the devices or people using them",
                [
                    "It uploads corrected navigation messages to the satellites",
                    "It monitors satellite health and flags faulty spacecraft",
                    "It transmits a ranging signal back to the constellation",
                ],
                "The user segment only listens. Uploading corrections and monitoring health are control segment jobs, and no GPS receiver transmits anything back to the satellites.",
            ),
            (
                "Why does the presentation argue that the two systems must be combined?",
                "Neither GPS alone nor 5G alone gives good positioning in every condition",
                [
                    "GPS can provide time but not position",
                    "5G-NTN cannot measure distance without GPS assistance",
                    "Augmentation schemes only work when both systems are present",
                ],
                "GPS is strong under open sky and weak in canyons, tunnels and indoors. 5G-NTN covers places terrestrial networks cannot. The hybrid exists because the two failure modes do not overlap.",
            ),
        ],
    },
    {
        "topic": "HAPS-based disaster recovery with 5G core integration",
        "source": "Group 5 deck, slides 3 to 11",
        "questions": [
            (
                "Why can an ordinary unmodified smartphone attach to a HAPS, when it cannot attach directly to most satellites?",
                "A HAPS is a standard 5G base station flown at altitude, so the link budget closes to a handset",
                [
                    "A HAPS transmits on unlicensed spectrum that all phones already support",
                    "A HAPS uses a modulation scheme designed specifically for handsets",
                    "Satellites do not implement the 5G NR air interface at all",
                ],
                "The deciding factor is distance. At about 20 km the path loss is small enough that a normal phone closes the link, which the deck quotes as roughly 28 dB better than a 500 km LEO.",
            ),
            (
                "What does the local-breakout UPF on the HAPS payload achieve?",
                "Responder traffic can be switched locally and never leaves the disaster zone",
                [
                    "It authenticates responders without contacting the ground core",
                    "It stores traffic until the ground network is restored",
                    "It removes the need for a feeder link to the gateway",
                ],
                "The User Plane Function is where user traffic is routed. Putting one on the platform means two responders in the same area can talk through the HAPS alone, without a round trip to the ground core.",
            ),
            (
                "Which functions stay on the ground 5G core even with a regenerative HAPS payload?",
                "Authentication and session management, and routing to external networks",
                [
                    "Radio resource control and scheduling",
                    "Local user-plane switching between responders",
                    "Beamforming weight computation for the service link",
                ],
                "The AMF and the SMF stay on the ground. The payload carries the gNB and a breakout UPF, so it handles the radio and local traffic, but subscriber authentication and external routing remain a core function.",
            ),
            (
                "How does HAPS end-to-end latency compare with GEO in the quoted table?",
                "HAPS is roughly fifty times lower",
                [
                    "Roughly the same, since both are line-of-sight links",
                    "HAPS is around one order of magnitude lower",
                    "HAPS is higher because of the extra gateway hop",
                ],
                "The table gives 1 to 10 ms for HAPS against 480 to 560 ms for GEO. Comparing the middle of each range puts the ratio near fifty.",
            ),
            (
                "What link-budget advantage is quoted for a 20 km HAPS over a 500 km LEO for direct-to-smartphone service?",
                "About 28 dB",
                [
                    "About 3 dB",
                    "About 12 dB",
                    "About 60 dB",
                ],
                "The figure follows from the range ratio. Being twenty-five times closer buys roughly 28 dB of path loss, which is what makes an unmodified handset viable.",
            ),
            (
                "Which challenge belongs to the Ka-band feeder link rather than the service link?",
                "Rain fade, which has to be handled with site diversity",
                [
                    "Station-keeping against stratospheric winds",
                    "Airspace clearance for the platform",
                    "Sharing one platform's capacity across the whole footprint",
                ],
                "Rain attenuation grows sharply with frequency, so a 20 to 30 GHz feeder link is vulnerable in a way the lower-frequency service link is not. Site diversity answers it by having a second gateway in different weather.",
            ),
            (
                "A single HAPS covers a 50 to 100 km radius. What does that mean for capacity?",
                "One platform's capacity is shared across that entire footprint",
                [
                    "Capacity scales automatically with the radius covered",
                    "The radius must be reduced before the data rate can rise",
                    "Coverage beyond 50 km requires a second feeder link",
                ],
                "Coverage and capacity are different quantities. A wide footprint is an advantage for reach and a disadvantage for throughput per user, because every user inside it draws on the same payload.",
            ),
            (
                "Why is deployment speed the decisive advantage of HAPS in disaster response?",
                "It can be flown in hours or days, with no launch campaign",
                [
                    "The platform can be recovered and reused after the event",
                    "It needs no gateway on the ground",
                    "It operates in spectrum permanently reserved for emergencies",
                ],
                "A satellite has to be built, scheduled and launched. Disaster response is measured in hours, and a platform that can be in the air the same day is the only one that arrives while it still matters.",
            ),
            (
                "Endurance is listed as an open problem. What figure is quoted?",
                "12 days is the current airship record",
                [
                    "12 hours is the current airship record",
                    "12 weeks is the current airship record",
                    "12 months is the current airship record",
                ],
                "Twelve days is long enough for an emergency deployment and far short of permanent infrastructure, which is why the deck calls HAPS a temporary layer by design.",
            ),
            (
                "The conclusion attaches a condition to the claim that HAPS restores coverage. What is it?",
                "Backhaul must survive through a gateway, a satellite or another HAPS",
                [
                    "The terrestrial towers must be only partially damaged",
                    "The handsets must be upgraded to support NTN",
                    "The disaster zone must be smaller than 50 km across",
                ],
                "A HAPS restores the radio access network, not the transport behind it. Without a surviving path to the core, the platform can connect phones to each other locally but not to anything beyond the zone.",
            ),
        ],
    },
    {
        "topic": "Multi-connectivity and session continuity across TN-NTN links",
        "source": "Group 6 deck, slides 3 to 19",
        "questions": [
            (
                "What distinguishes make-before-break handover from a conventional handover?",
                "The new link is established before the old one is released",
                [
                    "The old link is released before the new one is established",
                    "Both links are released and the device re-attaches from idle",
                    "The handover is decided by the device rather than the network",
                ],
                "A conventional handover has a gap between releasing one link and acquiring the next. Overlapping the two removes that gap, which is what stops the session from dropping.",
            ),
            (
                "A device is attached to a 5G base station and a LEO satellite at the same time. Which technology enables that?",
                "Multi-Radio Dual Connectivity",
                [
                    "Access Traffic Steering, Switching and Splitting",
                    "Network slicing",
                    "Multi-Access Edge Computing",
                ],
                "MR-DC is the mechanism that lets one device hold simultaneous connections over two different radio accesses. ATSSS then decides what traffic to send over which of them.",
            ),
            (
                "ATSSS and MR-DC are related but distinct. What does ATSSS add?",
                "It decides how traffic is routed and balanced across the connections",
                [
                    "It creates the simultaneous radio connections in the first place",
                    "It authenticates the device on each access network separately",
                    "It predicts when a handover will become necessary",
                ],
                "MR-DC provides the pipes and ATSSS provides the policy. Steering, switching and splitting are three ways of dividing a traffic flow across pipes that already exist.",
            ),
            (
                "Which challenge is matched with intelligent routing as its solution?",
                "Latency differences between the access types",
                [
                    "Frequent handovers",
                    "Link failures",
                    "Session interruption",
                ],
                "A satellite path and a terrestrial path have very different delays. Routing intelligently means sending delay-sensitive traffic down the short path and bulk traffic down the long one.",
            ),
            (
                "Why does MEC help specifically during mobility?",
                "It processes data closer to the user, so latency stays low as the link changes",
                [
                    "It removes the need for a satellite feeder link",
                    "It stores the session context so the device need not re-authenticate",
                    "It selects which satellite the device should connect to next",
                ],
                "Edge computing shortens the path between the user and the application. When the access link is switching between terrestrial and satellite, keeping the compute nearby limits how much the round trip can grow.",
            ),
            (
                "How is session continuity defined?",
                "An ongoing session is preserved while the underlying link changes",
                [
                    "A device stays attached to one satellite for a whole pass",
                    "A fixed data rate is reserved for the duration of a call",
                    "Both terrestrial and satellite links are always kept available",
                ],
                "Continuity is about the session surviving, not about the link staying still. The benefits listed follow from that: no repeated logins, no data loss and a stable experience.",
            ),
            (
                "How does network slicing contribute to seamless connectivity?",
                "It gives each application a dedicated virtual network with consistent quality of service",
                [
                    "It reduces the number of handovers a device must perform",
                    "It splits a single session across two carriers to raise throughput",
                    "It pre-computes the beam weights for the satellite link",
                ],
                "Slicing isolates services from one another, so a latency-critical application keeps its guarantees even when the network beneath it changes access type or comes under load.",
            ),
            (
                "Which benefit belongs to multi-connectivity rather than to session continuity?",
                "Load balancing and a backup path if one link fails",
                [
                    "No repeated logins",
                    "No data loss during a link change",
                    "A stable experience for the end user",
                ],
                "Load balancing and redundancy require two links running at once, which is what multi-connectivity provides. The other three are what continuity delivers once the link does change.",
            ),
            (
                "Frequent handovers are listed as an NTN challenge. What causes them?",
                "LEO satellites sweep across the sky, so the serving cell keeps changing",
                [
                    "The high altitude of the satellite platform",
                    "Congestion in the terrestrial network",
                    "The mismatch in latency between the two access types",
                ],
                "In a terrestrial network the user moves past fixed towers. In a LEO network the tower itself moves, so even a stationary user is handed over every few minutes.",
            ),
            (
                "AI-assisted mobility management turns the handover from reactive into proactive. How?",
                "By predicting user movement and network conditions ahead of time",
                [
                    "By raising the signal strength threshold that triggers a handover",
                    "By handing over to the satellite whenever the terrestrial link weakens",
                    "By keeping the device on the terrestrial link for as long as possible",
                ],
                "A reactive handover waits for a measurement to cross a threshold. Predicting the movement lets the network prepare the target in advance, so the switch happens before the link degrades.",
            ),
        ],
    },
    {
        "topic": "Spectrum sharing and interference management between 5G NTN and TN",
        "source": "Group 7 deck, slides 3 to 14",
        "questions": [
            (
                "A PFD mask is expressed as a function of elevation angle. Why does the elevation angle matter?",
                "It determines how much satellite energy reaches a terrestrial receiver at the surface",
                [
                    "The satellite transmits more power at low elevation",
                    "Doppler shift is largest at high elevation angles",
                    "The terrestrial base station antenna tilts with elevation",
                ],
                "A beam arriving steeply from overhead spreads its energy differently from one arriving near the horizon, and terrestrial antennas discriminate against those angles differently. The regulatory limit therefore has to be angle dependent.",
            ),
            (
                "What does EPFD add beyond an ordinary PFD limit?",
                "It accounts for the aggregate interference from a whole constellation",
                [
                    "It applies the limit to the uplink as well as the downlink",
                    "It converts the limit into a time-averaged rather than a peak value",
                    "It extends the limit to adjacent bands as well as the co-channel band",
                ],
                "A single spacecraft can comply while a constellation of hundreds, all visible at once, still swamps a terrestrial receiver. EPFD is the equivalent limit applied to the summed contribution.",
            ),
            (
                "Null-steering suppresses interference without simply reducing transmit power. How?",
                "It places a null in the radiation pattern toward the victim receiver",
                [
                    "It narrows the main lobe until it misses the victim receiver",
                    "It shifts the beam into an adjacent frequency band",
                    "It reduces the number of active antenna elements",
                ],
                "An adaptive array can shape its pattern, not just point it. Steering a null at the victim removes energy in that one direction while the main lobe keeps serving its intended users at full power.",
            ),
            (
                "Which interference mechanism arises purely from the speed of LEO satellites?",
                "Doppler-induced spreading",
                [
                    "Co-channel interference",
                    "Adjacent-band leakage",
                    "Cross-border coexistence",
                ],
                "The other three exist for a stationary satellite too. Only spectral smearing from a rapidly changing frequency offset is a direct consequence of orbital velocity.",
            ),
            (
                "In the uplink interference scenario, who is the victim?",
                "The satellite receiver, reached by a terrestrial user's transmission",
                [
                    "A terrestrial user equipment inside the satellite footprint",
                    "The terrestrial base station, reached by the satellite downlink",
                    "The gateway earth station on the feeder link",
                ],
                "Direction defines the victim. On the downlink the satellite beam spills into the terrestrial cell and a ground user suffers. On the uplink the terrestrial transmission rises into the satellite and the satellite suffers.",
            ),
            (
                "Which approach sits underneath dynamic spectrum sharing rather than beside it?",
                "Cognitive sensing",
                [
                    "Exclusive or licensed allocation",
                    "Static co-primary sharing",
                    "Geographic separation using exclusion zones",
                ],
                "The tree has four top-level approaches. Dynamic spectrum sharing then branches into power control, adaptive beamforming, cognitive sensing and AI/ML-based allocation.",
            ),
            (
                "Which 3GPP release is identified as the first NTN specification?",
                "Release 17",
                [
                    "Release 15",
                    "Release 18",
                    "Release 20",
                ],
                "Releases 15 and 16 were study items. Release 17 in 2022 is where NR-NTN and NB-IoT or eMTC over satellite were first specified rather than merely studied.",
            ),
            (
                "Why is cross-border regulation listed as an open challenge?",
                "Different countries have to agree on the same PFD rules",
                [
                    "Satellites cannot switch frequency as they cross a border",
                    "Terrestrial operators are not licensed to serve foreign users",
                    "Doppler shift changes as the satellite crosses a boundary",
                ],
                "A beam does not stop at a national boundary, but spectrum regulation does. Two neighbouring administrations with different limits leave the operator with no single rule to comply with.",
            ),
            (
                "When are guard bands and guard time slots used?",
                "When co-channel sharing between NTN and TN is not workable",
                [
                    "When the satellite must reduce its power flux density",
                    "When the constellation exceeds its EPFD budget",
                    "When the terrestrial network is congested",
                ],
                "Guard resources are the fallback. They separate the two systems in frequency or in time and give up the efficiency that sharing the same resources would have provided.",
            ),
            (
                "The takeaways name one direction as the clear road to 6G. Which?",
                "AI/ML-driven dynamic spectrum sharing",
                [
                    "Exclusive licensed allocation for NTN",
                    "Wider guard bands between NTN and TN",
                    "Moving all NTN traffic into Ka-band",
                ],
                "The other three all work by keeping the systems apart, which wastes spectrum. Learning to share the same spectrum in real time is what the deck identifies as the path forward.",
            ),
        ],
    },
    {
        "topic": "Mobility management and handover optimization in 5G NTN",
        "source": "Group 8 deck, slides 4 to 14",
        "questions": [
            (
                "Which RRC state keeps the UE context stored in the network while the connection itself is released?",
                "RRC INACTIVE",
                [
                    "RRC CONNECTED",
                    "RRC IDLE",
                    "RRC SETUP",
                ],
                "INACTIVE is the middle state and it exists to make resuming cheap. IDLE keeps no context, so returning to CONNECTED from IDLE needs a full RRC setup.",
            ),
            (
                "Why is a purely signal-strength-based handover trigger inadequate in NTN?",
                "The satellite keeps moving, so the measurement is out of date by the time it is acted on",
                [
                    "Satellites do not transmit reference signals that can be measured",
                    "Signal strength cannot be measured through the ionosphere",
                    "The device has no way to report measurements on the uplink",
                ],
                "A measurement report has to travel to the network and a decision has to travel back. Over a satellite link that takes long enough for the geometry that justified the report to have changed.",
            ),
            (
                "A time-based trigger fires at a predicted moment. Where does the prediction come from?",
                "Satellite ephemeris and orbit data",
                [
                    "The historical measurement log stored in the device",
                    "The current network load at the target satellite",
                    "The rate of change of the received signal strength",
                ],
                "Orbits are deterministic, so the time at which a given satellite will fall below a usable elevation can be computed in advance rather than waited for.",
            ),
            (
                "What distinguishes conditional handover from a location-based trigger on its own?",
                "Several conditions have to be satisfied together before it fires",
                [
                    "It uses no location information at all",
                    "It is executed by the device without network involvement",
                    "It always hands over to a beam on the same satellite",
                ],
                "Location is one of the conditions in the set, alongside link quality, time to degradation and target load. Requiring all of them at once is what cuts unnecessary handovers.",
            ),
            (
                "Which condition in the conditional handover set concerns the target rather than the radio link?",
                "The target satellite's load is below a maximum",
                [
                    "Target SINR exceeds serving SINR plus a hysteresis margin",
                    "Time to link degradation is below a threshold",
                    "The UE is inside the target coverage area",
                ],
                "Load is a capacity property of the target cell, not a property of the radio path. Checking it stops the network from handing a device onto a satellite that is already full.",
            ),
            (
                "How does beam-based handover differ from satellite handover?",
                "The device switches between spot beams of the same satellite",
                [
                    "The device has to change carrier frequency",
                    "It is triggered only by time and never by location",
                    "It removes the need for a timing advance update",
                ],
                "A single satellite projects many spot beams, and the footprint of each sweeps across the ground. A user can leave one beam and enter another without ever changing satellite.",
            ),
            (
                "Reserving resources at the target satellite before a handover carries which specific cost?",
                "Capacity is wasted whenever the handover does not actually take place",
                [
                    "The device battery drains from continuous location fixing",
                    "Doppler pre-compensation becomes impossible",
                    "The RRC state has to fall back to IDLE",
                ],
                "Preparing in advance means committing resources on a prediction. Every prediction that does not come true has held capacity idle that could have served someone else.",
            ),
            (
                "Why does a location-based trigger drain the device battery?",
                "The device has to keep obtaining position fixes",
                [
                    "It requires the device to stay in RRC CONNECTED at all times",
                    "It doubles the number of transmit chains in use",
                    "It forces the device to measure every visible satellite",
                ],
                "Knowing when a geographic boundary has been crossed means knowing where you are continuously. A GNSS receiver running all the time is a significant, constant power draw.",
            ),
            (
                "Make-before-break is described as adding hardware complexity. Why?",
                "The device has to support two simultaneous links",
                [
                    "The device has to store the full ephemeris of the constellation",
                    "The satellite has to carry an additional soft buffer",
                    "The device has to run an AI model in real time",
                ],
                "Holding the old link while the new one comes up means two active radio connections at once, which needs the receive and transmit hardware to support both.",
            ),
            (
                "How does the conclusion characterise the overall shift in NTN mobility management?",
                "From reactive and signal-based to predictive and ephemeris-driven",
                [
                    "From ephemeris-driven to measurement-driven",
                    "From network-controlled to device-controlled",
                    "From beam-based to satellite-based handover",
                ],
                "The old model waits for a measurement to degrade. The new one exploits the fact that satellite motion is known in advance, and pays for that with signalling, battery and reserved capacity.",
            ),
        ],
    },
]
