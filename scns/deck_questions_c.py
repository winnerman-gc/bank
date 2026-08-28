# -*- coding: utf-8 -*-
"""TE 456 question data, groups 17 to 24.

Two decks in this range carry no group number on their title slide. They are
listed under their topic, in the position the file order puts them.

Format per question:
    (stem, correct_answer, [distractor, distractor, distractor], explanation)

See build_questions.py for how these are compiled.
"""

DECKS = [
    {
        "topic": "eRACH, a learned random access protocol for LEO networks",
        "source": "Group 17 deck, slides 3 to 8",
        "questions": [
            (
                "What makes the topology of a LEO network non-stationary from the point of view of random access?",
                "Satellites move at about 7.6 km/s, so the best satellite to connect to changes every few milliseconds",
                [
                    "The number of satellites in view changes as the constellation is expanded",
                    "Ground terminals move between beams faster than the network can track",
                    "The preamble set is re-randomised by the network at every access window",
                ],
                "Standard RACH assumes a fixed tower and has no notion of which base station to associate with. In LEO that choice exists, it matters, and it changes continuously.",
            ),
            (
                "What is the quoted one-way propagation delay for LEO, and why does it matter for acknowledgement-based protocols?",
                "1 to 5 ms, which makes CSMA/CA and acknowledgement schemes slow and prone to wasted retransmissions",
                [
                    "1 to 5 ms, which is short enough that acknowledgement schemes work unchanged",
                    "20 to 60 ms, which forces every protocol to abandon acknowledgements entirely",
                    "under 1 ms, so the delay affects throughput but not protocol design",
                ],
                "Even LEO's relatively short delay is long compared with the time a terrestrial protocol expects to wait. Protocols built on listen-then-send or send-then-acknowledge degrade under it.",
            ),
            (
                "In eRACH, what does each ground terminal observe locally?",
                "The expected satellite position from the known orbit, and whether its last attempt collided",
                [
                    "The queue length and preamble choice of every neighbouring terminal",
                    "A schedule broadcast by the network at the start of each access window",
                    "The aggregate collision rate measured across the whole beam",
                ],
                "The design point is that terminals do not talk to each other. Each has only what it can see for itself: predictable geometry, and the outcome of its own last attempt.",
            ),
            (
                "What decision does the actor-critic network make at each terminal?",
                "Whether to access now and which satellite to use, or to back off and wait",
                [
                    "Which preamble index to select from the shared pool",
                    "How much transmit power to apply to the preamble",
                    "Whether to use the terrestrial network instead of the satellite",
                ],
                "The action space combines timing and association. Choosing when to transmit and which satellite to aim at is precisely what standard RACH leaves unspecified in a moving constellation.",
            ),
            (
                "What does emergent mean in the name emergent RACH?",
                "The coordinated access pattern arises from independent learning, with no coordination signalling",
                [
                    "The protocol emerges from the 3GPP standardisation process over several releases",
                    "The satellite emerges into view and broadcasts the access schedule",
                    "New preambles are generated on demand as devices join the network",
                ],
                "Terminals never communicate with each other. Over many orbital cycles they nonetheless learn to spread their attempts apart, so the coordination is a product of learning rather than of messaging.",
            ),
            (
                "Which quantitative result is reported for eRACH against standard RACH?",
                "54.6 percent higher throughput and about twice lower access delay",
                [
                    "31.2 percent higher throughput and about four times lower access delay",
                    "54.6 percent lower collision rate and about twice higher throughput",
                    "Twice the throughput and 54.6 percent lower access delay",
                ],
                "The summary cites Table II of the source paper. The gain is achieved with no inter-device coordination, which is the point being made.",
            ),
            (
                "What does the parameter rho control in eRACH?",
                "The balance between maximising throughput and avoiding collisions",
                [
                    "The learning rate of the actor-critic network",
                    "The number of satellites a terminal may consider",
                    "The length of the backoff window in milliseconds",
                ],
                "Rho equals 0 tunes for throughput and rho equals 2 tunes for collision avoidance. That lets one protocol serve application classes with different tolerances.",
            ),
            (
                "Which challenge concerns the hardware rather than the algorithm?",
                "High computational complexity against size, weight and power constraints",
                [
                    "Sensitivity to satellite positioning accuracy",
                    "A higher collision tolerance than standard RACH",
                    "The absence of inter-device coordination",
                ],
                "Running a neural policy on a terminal or a payload costs compute, and both are budget-limited. The other two are properties of how the learned policy behaves.",
            ),
            (
                "Why is sensitivity to satellite positioning accuracy a concern for eRACH?",
                "One of the two local observations is the expected satellite position, so an error corrupts the policy input",
                [
                    "The terminal must report its own position to the satellite before access",
                    "Positioning error changes the preamble that the terminal selects",
                    "The satellite cannot compute the reward without an accurate position",
                ],
                "The policy acts on what it observes. If the predicted geometry is wrong, the decision about when and where to transmit is made on a false picture. The deck notes the protocol is nonetheless robust to such errors.",
            ),
            (
                "What is the headline problem statement in the conclusion?",
                "Standard RACH ignores satellite mobility, which produces high collision rates and long access delays",
                [
                    "Standard RACH cannot operate at all above a certain orbital velocity",
                    "LEO constellations have too few preambles for the number of devices",
                    "Multi-agent learning is required by the 3GPP NTN specification",
                ],
                "The deck frames the gap as a mismatch: a protocol designed for stationary towers is being used where the tower moves, and the resulting collisions and delays are the symptom.",
            ),
        ],
    },
    {
        "topic": "RIS-enhanced NTN for coverage and capacity in 6G",
        "source": "Group 18 deck, slides 2 to 10",
        "questions": [
            (
                "What is the coverage problem that a reconfigurable intelligent surface is meant to solve?",
                "A satellite needs a clear view of the user, and a building or a hill removes the link completely",
                [
                    "The satellite beam is too wide to serve individual users efficiently",
                    "The satellite cannot generate enough beams for all the users in a cell",
                    "Atmospheric absorption removes the link at high frequencies",
                ],
                "The deck shows a user in a building's shadow with no line of sight. The link budget is already tight, so a blocked path is not a degraded link, it is no link.",
            ),
            (
                "How does a RIS steer a reflection without any RF chain?",
                "Each element applies its own phase shift, so the reflected waves add up in one chosen direction",
                [
                    "Each element amplifies the incident signal before re-radiating it",
                    "The surface physically rotates to face the intended receiver",
                    "The surface converts the signal to a different frequency before reflecting it",
                ],
                "This is passive beamforming. Controlling the relative phase across the aperture decides where the reflected wavefronts interfere constructively, and none of it requires a transmitter.",
            ),
            (
                "What distinguishes an active RIS from a passive RIS?",
                "Each element is connected to an amplifier and an RF chain, so amplitude as well as phase can be controlled",
                [
                    "It uses discrete rather than continuous phase shifts",
                    "It responds differently at different frequencies",
                    "It is mounted on the satellite rather than on a building",
                ],
                "A passive RIS only adjusts phase, and sometimes amplitude, of what it reflects. An active RIS adds gain, which costs power and complexity but relieves the multiplied path loss.",
            ),
            (
                "Which RIS type uses discrete phase shifts such as 1-bit values of 0 or 180 degrees?",
                "Digital RIS",
                [
                    "Tunable analog RIS",
                    "Hybrid RIS",
                    "Frequency-selective RIS",
                ],
                "Digital RIS quantises the phase into a small number of states, which lowers complexity and cost. Tunable analog RIS uses varactors to give continuous phase at higher hardware cost.",
            ),
            (
                "Which RIS type is suited to wideband and multi-band operation?",
                "Frequency-selective RIS, whose elements respond differently across frequency",
                [
                    "Passive RIS, because it introduces no frequency-dependent gain",
                    "Hybrid RIS, because it mixes passive and active elements",
                    "Digital RIS, because 1-bit control is frequency independent",
                ],
                "Giving elements a designed frequency response lets one surface manipulate several bands at once, which a single fixed phase profile cannot do.",
            ),
            (
                "Why must a RIS panel be large, and why must it be close to one end of the link?",
                "The two hops multiply rather than add, so the combined path loss is severe",
                [
                    "The panel must be larger than the wavelength of the incident signal",
                    "A large panel is needed to dissipate the heat from the controller",
                    "Regulations require a minimum aperture for reflecting satellite signals",
                ],
                "In a relay the two hops are separate links. In a passive reflection the losses compound, so the only remedies are a very large aperture and placing the surface near the transmitter or the receiver.",
            ),
            (
                "The deck states that a passive surface cannot measure anything itself. What problem does that create?",
                "The channel has to be estimated by other means before the phases can be computed",
                [
                    "The surface cannot be assigned an identity in the network",
                    "The surface cannot verify that its reflection reached the user",
                    "The surface cannot be updated once it has been installed",
                ],
                "Setting the phases requires knowing the channel from the transmitter to the surface and from the surface to the user. A device that only reflects contributes no measurements toward that.",
            ),
            (
                "What is the near-field effect listed among the limitations?",
                "A large panel breaks the simple distance model that far-field design assumes",
                [
                    "The panel heats the surrounding structure at close range",
                    "The panel reflects into its own controller at short distances",
                    "The panel cannot be used indoors because of wall reflections",
                ],
                "Standard beamforming assumes a plane wave across the aperture. When the aperture is large relative to the distance, the wavefront is curved and the plane-wave approximation fails.",
            ),
            (
                "How does a RIS add capacity as well as coverage?",
                "It provides a second path, so a second spatial stream becomes possible",
                [
                    "It doubles the bandwidth available on the existing path",
                    "It allows the satellite to reuse the same frequency in adjacent beams",
                    "It compresses the data before reflecting it onward",
                ],
                "Coverage comes from building a path where none existed. Capacity comes from that path being distinct from the direct one, which gives the channel matrix another dimension to carry a stream on.",
            ),
            (
                "What is the stated standardisation status of RIS?",
                "A candidate for 6G, not present in any released standard",
                [
                    "Specified in 3GPP Release 18 as part of 5G-Advanced",
                    "Standardised by the ITU for satellite use only",
                    "Withdrawn from standardisation after Release 17 study items",
                ],
                "The deck is explicit that RIS is still before standardisation. It is presented as a promising technique rather than a deployable specification.",
            ),
        ],
    },
    {
        "topic": "Uplink time synchronization for NTN without GNSS",
        "source": "Group 21 deck, slides 3 to 11",
        "questions": [
            (
                "What system configuration does the deck assume throughout?",
                "5G NR with a regenerative payload carrying an onboard gNodeB, in LEO, with CP-OFDM on the uplink",
                [
                    "5G NR with a transparent bent-pipe payload, in GEO, with SC-FDMA on the uplink",
                    "LTE with a regenerative payload in MEO, with CP-OFDM on the uplink",
                    "5G NR with a transparent payload in LEO, with OFDMA on the downlink only",
                ],
                "The assumption matters because a regenerative payload puts the base station in orbit, so the timing reference the device must align to is on the satellite itself.",
            ),
            (
                "In the Release 17 dual-loop architecture, what are the three timing advance components?",
                "A network-broadcast common part, a UE-computed part from GNSS and ephemeris, and a closed-loop adjustment",
                [
                    "An open-loop part, a closed-loop part and a Doppler pre-compensation part",
                    "A service link part, a feeder link part and an inter-satellite link part",
                    "A coarse part, a fine part and a fractional part",
                ],
                "TA common is broadcast and covers what is shared across the beam. TA UE is the device's own geometry. TA adj is the residual correction signalled by the gNB after measurement.",
            ),
            (
                "Without GNSS, which part of the Release 17 scheme fails first?",
                "The open-loop equation, because the device does not know its position relative to the satellite",
                [
                    "The closed loop, because the gNB can no longer measure arrival time",
                    "The common broadcast, because the network cannot compute it",
                    "The cyclic prefix, because it can no longer absorb the delay spread",
                ],
                "The device is described as a blind UE. It cannot compute a propagation delay from geometry it cannot observe, so it has no basis for its initial timing advance.",
            ),
            (
                "Why is falling back to closed-loop signalling alone not sufficient?",
                "The first transmissions arrive with timing errors far larger than the cyclic prefix",
                [
                    "The closed loop only corrects frequency, not timing",
                    "The gNB cannot send a timing advance command to an unsynchronised device",
                    "The closed loop requires a GNSS timestamp in every command",
                ],
                "A closed loop can only refine an estimate that is already close enough to be received. With no starting estimate the signal lands outside the reception window and there is nothing to measure.",
            ),
            (
                "What is the key insight behind GNSS-time-free drift compensation?",
                "Satellite motion changes the propagation delay, so tracking downlink arrival-time drift reveals the timing advance",
                [
                    "The satellite broadcasts its own clock drift, which the device mirrors",
                    "Clock drift in the device oscillator is proportional to the propagation delay",
                    "Arrival-time drift can be removed entirely by lengthening the cyclic prefix",
                ],
                "The device cannot measure absolute distance, but it can watch how the arrival time of successive downlink slots shifts. That drift is produced by the changing range, so it carries the information needed.",
            ),
            (
                "In the Extended Kalman Filter method, what does the state vector contain?",
                "UE latitude, satellite longitude and the UE-to-satellite distance",
                [
                    "UE velocity, satellite velocity and the relative Doppler shift",
                    "Timing advance, frequency offset and oscillator drift rate",
                    "Beam index, elevation angle and slant range",
                ],
                "The filter estimates the geometry the device cannot observe directly, and the timing advance follows from the estimated distance rather than from a GNSS fix.",
            ),
            (
                "What is the stated strength of the EKF approach?",
                "Robust performance with rapid convergence to accurate values",
                [
                    "Zero computational cost on the user device",
                    "Complete independence from the downlink signal",
                    "Guaranteed accuracy at the beam edge and the beam centre alike",
                ],
                "The filter runs a predict-then-update cycle, so each new measurement refines the estimate. That is what lets it converge quickly from a poor starting point.",
            ),
            (
                "What is the trade-off in the network-provided common timing advance method?",
                "A user near the beam centre gets an accurate value, while a user near the beam edge can be significantly off",
                [
                    "It is accurate for LEO but fails entirely for GEO beams",
                    "It is accurate at first but drifts as the satellite moves",
                    "It works only for devices that already have a GNSS fix",
                ],
                "One broadcast value cannot describe every point in a footprint. It is correct where it was computed for, and its error grows with distance from that reference point.",
            ),
            (
                "In the timing advance feedback loop, what does the gNB actually measure?",
                "Whether the uplink arrived too early, too late, or inside the expected reception window",
                [
                    "The Doppler shift of the arriving uplink carrier",
                    "The received power of the uplink relative to a target",
                    "The number of retransmissions the device has attempted",
                ],
                "The expected reception window covers one uplink slot. The gNB classifies the arrival against that window and sends an increase, decrease or keep command accordingly, looping until alignment holds.",
            ),
            (
                "What is the overall conclusion of the deck?",
                "Alternative methods allow uplink synchronization without GNSS",
                [
                    "GNSS is unavoidable for NTN uplink synchronization",
                    "Uplink synchronization is unnecessary with a regenerative payload",
                    "GNSS can be replaced only by an onboard atomic clock in the device",
                ],
                "The deck presents four methods, each avoiding the GNSS dependency in a different way, and concludes that the Release 17 assumption is a design choice rather than a physical necessity.",
            ),
        ],
    },
    {
        "topic": "Deep reinforcement learning for space-air-ground 6G resource allocation",
        "source": "Group 22 deck, slides 2 to 14",
        "questions": [
            (
                "What is a space-air-ground integrated network?",
                "A layered network combining satellites, aerial platforms and terrestrial infrastructure under one system",
                [
                    "A satellite constellation that also carries an Earth observation payload",
                    "A terrestrial network whose backhaul is provided by satellite",
                    "A network in which every user device can act as a relay",
                ],
                "The deck shows space, aerial and ground operation centres feeding one 6G core. The point is that all three tiers are managed together rather than as separate networks.",
            ),
            (
                "What is resource allocation in a SAGIN, and why is it needed?",
                "Distributing limited communication and computing resources among users and platforms so the network stays fast and fair",
                [
                    "Assigning each satellite a fixed share of the available spectrum at launch",
                    "Deciding which ground stations will serve which orbital planes",
                    "Allocating storage on board each satellite for buffered traffic",
                ],
                "Resources are scarce and demand keeps moving. Sharing them intelligently is what keeps performance and fairness acceptable as the geometry and the traffic change.",
            ),
            (
                "Which three challenges are listed for SAGIN 6G NTN?",
                "Spectrum scarcity and interference, limited onboard power and energy, and uneven shifting user demand",
                [
                    "Orbital debris, launch cost and regulatory approval",
                    "Handover failure, packet loss and jitter",
                    "Key distribution, authentication and privacy leakage",
                ],
                "All three are resource problems. There is not enough spectrum, not enough power, and the demand that has to be served with them will not stay still.",
            ),
            (
                "In the general DRL model, what constitutes the state?",
                "Available power, bandwidth, SINR and channel state information",
                [
                    "The reward accumulated over the previous episode",
                    "The set of actions the agent has not yet tried",
                    "The orbital elements of every satellite in the constellation",
                ],
                "The state is what the agent observes about the environment before acting. Here that is the current resource and channel picture that the allocation decision has to be made from.",
            ),
            (
                "What does the action consist of in this framework?",
                "Channel allocation, power control and access point selection",
                [
                    "Handover execution and beam shaping only",
                    "Reward shaping and policy update",
                    "Ephemeris broadcast and timing advance signalling",
                ],
                "The action is the decision the policy controller emits. Those three levers are what actually change how resources are distributed in the network.",
            ),
            (
                "What is the reward built from?",
                "Quality of service, quality of experience and spectrum efficiency",
                [
                    "Collision rate, access delay and energy per bit",
                    "Throughput, latency and orbital altitude",
                    "Coverage area, satellite count and handover rate",
                ],
                "The reward defines what good allocation means. Combining service quality, experienced quality and efficient spectrum use captures both the user's view and the operator's view.",
            ),
            (
                "Which algorithm is described as choosing from a list of fixed options, such as which channel to use?",
                "Deep Q-Network",
                [
                    "Deep Deterministic Policy Gradient",
                    "Proximal Policy Optimization",
                    "Soft Actor-Critic",
                ],
                "DQN works over a discrete action set. Continuous quantities such as an exact power level need DDPG or a similar method that outputs a real value rather than a choice.",
            ),
            (
                "Which algorithm is described as fine-tuning exact values such as a precise power level?",
                "Deep Deterministic Policy Gradient",
                [
                    "Deep Q-Network",
                    "Proximal Policy Optimization",
                    "Twin Delayed DDPG",
                ],
                "DDPG is the continuous-control counterpart to DQN. PPO is described as learning a stable strategy step by step, and SAC or TD3 as exploring boldly while converging reliably.",
            ),
            (
                "In the HAPS tier, which three allocation tasks are named?",
                "Position allocation, dynamic spectrum and power distribution, and edge server compute provisioning",
                [
                    "Beam hopping, spectrum provisioning and transmit power allocation",
                    "Drone 3D location assignment, channel estimation and anti-interference management",
                    "Offloading, terrestrial base station selection and cloud routing",
                ],
                "Each tier has its own task list. Beam hopping and frequency assignment belong to the space tier, and 3D location assignment belongs to the UAV tier.",
            ),
            (
                "Which three challenges are listed for DRL-based SAGIN resource allocation?",
                "Scalability, non-stationarity from high mobility, and real-time deadlines against slow learning",
                [
                    "Scarce training data, the sim-to-real gap and certification",
                    "Self-interference, synchronisation and onboard compute",
                    "Bandwidth overhead, handshake latency and radiation-hardened processors",
                ],
                "The environment is large, it will not hold still long enough for a policy to settle, and decisions are needed faster than learning naturally converges. Those three are what make the problem hard.",
            ),
        ],
    },
    {
        "topic": "HARQ mechanisms and limitations in NTN",
        "source": "Group 23 deck, slides 2 to 14",
        "questions": [
            (
                "How does HARQ differ from ARQ and from forward error correction alone?",
                "It combines forward error correction with retransmission and soft combining of the failed copy",
                [
                    "It retransmits automatically without waiting for an acknowledgement",
                    "It corrects errors without any retransmission at all",
                    "It applies error correction only after a retransmission has failed",
                ],
                "ARQ waits for an acknowledgement and resends. FEC adds redundancy and decodes without resending. HARQ does both, and crucially keeps the failed copy so the two receptions can be combined.",
            ),
            (
                "In chase combining, what does the transmitter send on the retransmission?",
                "The same coded packet again, which the receiver combines with the stored soft bits",
                [
                    "A different set of parity bits from the same encoder",
                    "Only the systematic bits, without any parity",
                    "A shorter packet containing just the bits that failed",
                ],
                "The receiver keeps the soft bits from the first attempt rather than discarding them. Adding a second identical copy raises the effective signal-to-noise ratio enough to decode.",
            ),
            (
                "What distinguishes incremental redundancy from chase combining?",
                "The retransmission carries different parity bits, so previously punctured bits are now sent",
                [
                    "The retransmission is sent at a higher power level",
                    "The receiver discards the first copy before decoding the second",
                    "The retransmission uses a different modulation scheme",
                ],
                "The first transmission punctures some parity bits to raise the code rate. The retransmission supplies those bits, so the combined packet is protected by a lower-rate, stronger code.",
            ),
            (
                "Why does long round-trip time stall the HARQ pipeline in NTN?",
                "Every process stays occupied waiting for its acknowledgement, so no free process remains for new data",
                [
                    "The soft buffer overflows before the acknowledgement arrives",
                    "The acknowledgement expires and is discarded by the receiver",
                    "The receiver cannot decode a packet that arrives after a long delay",
                ],
                "A HARQ process is held from transmission until its acknowledgement returns. On a short terrestrial link they are released quickly. Over a 30 ms to 500 ms round trip they all fill up and transmission stops.",
            ),
            (
                "How many HARQ processes does 5G use by default, and what does the NTN adaptation raise that to?",
                "16 by default, raised to up to 32 for NTN",
                [
                    "8 by default, raised to up to 16 for NTN",
                    "16 by default, raised to up to 64 for NTN",
                    "32 by default, raised to up to 64 for NTN",
                ],
                "More parallel processes keep the pipe full while earlier ones wait for acknowledgements. The cost is proportionally more soft buffer memory in the receiver.",
            ),
            (
                "What is feedback-less HARQ operation, and what does it rely on instead?",
                "The device sends no ACK or NACK, and the link relies on strong forward error correction or blind retransmission",
                [
                    "The device sends only NACKs, never ACKs, to halve the feedback load",
                    "Feedback is sent to the gateway rather than to the satellite",
                    "Feedback is delayed until the end of the satellite pass",
                ],
                "Removing the acknowledgement removes the waiting, which is what caused the stall. The redundancy has to be added in advance instead, because there is no longer any signal telling the sender what failed.",
            ),
            (
                "In HARQ-less operation, where is error recovery performed?",
                "At the RLC layer or above, which is slower but avoids stalling MAC and PHY",
                [
                    "At the physical layer, using a stronger modulation scheme",
                    "At the application layer, by requesting the file again",
                    "On the satellite, which retransmits from its own buffer",
                ],
                "The MAC and PHY stop waiting for HARQ feedback entirely. Recovery still happens, but a layer up, which trades slower error recovery for a pipeline that keeps moving.",
            ),
            (
                "Which trade-off pair is stated correctly?",
                "More HARQ processes give higher throughput and require more memory",
                [
                    "Longer timers give faster failure detection and use less memory",
                    "Disabling feedback gives faster error recovery and fewer false alarms",
                    "Onboard processing gives the slowest loop at the lowest satellite cost",
                ],
                "The four trade-offs are: more processes buy throughput with memory; longer timers avoid false alarms but slow failure detection; disabling feedback keeps flow constant but delays recovery; onboard processing gives the fastest loop at the highest satellite cost.",
            ),
            (
                "In a transparent payload, where does the gNB sit relative to the HARQ loop?",
                "On the ground at the gateway, so the HARQ loop crosses both the service and feeder links",
                [
                    "On the satellite, so the HARQ loop covers only the service link",
                    "In the 5G core, so the loop crosses the N6 interface",
                    "Split between the satellite and the gateway, one process each",
                ],
                "A transparent satellite is a repeater. The base station is at the gateway, so an acknowledgement travels user to satellite to gateway and back, which is the longest possible loop.",
            ),
            (
                "What does a regenerative payload change about the HARQ loop?",
                "The gNB is on the satellite, so the loop closes over the service link alone",
                [
                    "The loop is removed entirely because errors are corrected on board",
                    "The loop is extended to include the inter-satellite link",
                    "The loop moves to the RLC layer automatically",
                ],
                "Putting the base station in orbit halves the geometry the acknowledgement has to cross. That is the fastest loop, and the deck notes it is also the highest satellite cost.",
            ),
        ],
    },
    {
        "topic": "Network digital twinning for 3D satellite constellation optimization",
        "source": "Group 24 deck, slides 3 to 9",
        "questions": [
            (
                "What is a network digital twin?",
                "A virtual replica of the physical network that is continuously updated with real-world data",
                [
                    "A backup constellation held in reserve for failover",
                    "A simulation model built once during the design phase",
                    "A duplicate of the network's control software running on the ground",
                ],
                "The defining property is the live link back to reality. A model that is not continuously updated is a simulation; the continuous update is what makes it a twin.",
            ),
            (
                "Which of these is listed as a challenge that makes a 6G NTN constellation hard to manage?",
                "Rapid topology changes, as links between satellites and ground stations are created and broken",
                [
                    "The gradual decay of orbits over the mission lifetime",
                    "The limited number of ground stations licensed worldwide",
                    "The fixed bandwidth allocation agreed at constellation design",
                ],
                "The six challenges are constant mobility, rapid topology change, long propagation delay, limited onboard resources, frequent handovers and high deployment and maintenance cost.",
            ),
            (
                "What are the stated consequences of those challenges?",
                "Increased latency, routing instability, resource allocation difficulty, reduced QoS, slow fault detection and higher operational cost",
                [
                    "Orbital debris, collision risk and end-of-life disposal cost",
                    "Spectrum interference, cross-border regulation and licensing delay",
                    "Key compromise, replay attacks and identity exposure",
                ],
                "The consequence row follows directly from the challenge row: a network that changes every second is hard to route through, hard to allocate for and hard to diagnose.",
            ),
            (
                "In the hierarchical digital twin architecture, what does the network control centre hold?",
                "A global controller and a central digital twin covering the whole network",
                [
                    "An edge digital twin for each ground station",
                    "The physical satellites and their telemetry links",
                    "A local controller managing beam and radio resource allocation",
                ],
                "The hierarchy runs from edge twins at the ground stations, through local controllers, up to a central twin and a global controller at the network control centre.",
            ),
            (
                "Which functions belong to the local controller at a ground station?",
                "Beam allocation, radio resource allocation, data processing and fault diagnosis",
                [
                    "Network verification, slicing and global optimization",
                    "Traffic engineering and global network modelling",
                    "Orbit determination and ephemeris broadcast",
                ],
                "The split is by scope. Local controllers handle what happens at one station, while the global controller handles network verification, slicing, traffic engineering and whole-network optimisation.",
            ),
            (
                "What are the five steps by which digital twinning optimizes a constellation?",
                "Collect real-time data, synchronize the twin, simulate future conditions, evaluate options, deploy the best decision",
                [
                    "Observe, decide, act, learn, repeat",
                    "Sense, optimize, act, learn, verify",
                    "Predict, measure, correct, verify, log",
                ],
                "The distinguishing step is simulating multiple futures before committing to one. That is what a twin adds over a plain control loop: decisions are tested in the model rather than on the live network.",
            ),
            (
                "Which benefits are attributed to the digital twin approach?",
                "Lower latency, better routing, faster fault detection and reduced operational cost",
                [
                    "Higher orbital altitude, wider coverage and longer satellite life",
                    "Stronger encryption, better authentication and privacy protection",
                    "Larger constellations, cheaper launches and faster deployment",
                ],
                "All four follow from being able to test a decision before applying it: better routes are found, faults are noticed sooner, and fewer costly interventions are needed on the real network.",
            ),
            (
                "Why is DT migration complexity listed as a limitation?",
                "Digital twins have to migrate as the satellites they model move",
                [
                    "Twins must be re-certified whenever the network software is updated",
                    "Twins cannot be transferred between different vendors' platforms",
                    "Twins lose their history whenever they are moved",
                ],
                "A twin is anchored to the physical thing it mirrors. When that thing is in orbit and the serving infrastructure changes, the twin has to follow it, which adds machinery the ground case does not need.",
            ),
            (
                "Why is synchronization overhead a real cost rather than an implementation detail?",
                "Keeping the physical and digital networks in step consumes bandwidth",
                [
                    "Synchronization requires an atomic clock on every satellite",
                    "The twin cannot run while synchronization is in progress",
                    "Synchronization errors accumulate and cannot be corrected",
                ],
                "The twin is only useful while it matches reality, and matching reality means a continuous stream of telemetry. On a link where capacity is scarce, that stream competes with user traffic.",
            ),
            (
                "What is the security concern raised about digital twins?",
                "A compromised twin could be exploited to disrupt network operations",
                [
                    "The twin stores subscriber data that could be exposed",
                    "The twin's synchronization traffic cannot be encrypted",
                    "The twin can be used to locate satellites for physical attack",
                ],
                "The twin is not a passive mirror. Decisions computed in it are deployed to the physical network, so an attacker who controls the twin gains influence over the real constellation.",
            ),
        ],
    },
    {
        "topic": "AI-driven predictive handover for high-mobility LEO networks",
        "source": "Unnumbered deck, AI-Driven Predictive Handover Management, slides 4 to 16",
        "questions": [
            (
                "How does the handover situation in a LEO network differ from a terrestrial one?",
                "On a normal mobile network you move past towers; on LEO the tower itself moves across the sky",
                [
                    "On LEO the user must select the satellite manually before each session",
                    "On LEO handovers happen only when the user physically moves",
                    "On LEO the handover is performed by the satellite without informing the device",
                ],
                "This is the root of every other problem in the deck. A stationary user still gets handed over every few minutes, because the coverage is what is moving.",
            ),
            (
                "What is a handover storm?",
                "Many devices sharing one satellite all need to switch at nearly the same time",
                [
                    "A single device switching repeatedly between two satellites",
                    "A burst of signalling caused by a satellite failure",
                    "Handovers triggered by atmospheric interference during a storm",
                ],
                "The deck likens it to every shopper reaching the same checkout at once. Because they all share one satellite, they all lose it together, and the signalling arrives in one spike.",
            ),
            (
                "What is the ping-pong effect, and what causes it?",
                "A device flips repeatedly between two satellites because the system is not confident in its decision",
                [
                    "A device alternates between the uplink and downlink of the same satellite",
                    "An acknowledgement bounces between the satellite and the gateway",
                    "A beam sweeps back and forth across the same ground cell",
                ],
                "Each flip costs signalling and interrupts the connection, so the effect wastes effort and degrades service without ever improving the link.",
            ),
            (
                "Why is a reactive handover riskier in a satellite network than on the ground?",
                "By the time the weak-signal warning reaches the network and a decision returns, the satellite has already moved a meaningful distance",
                [
                    "Satellite receivers cannot measure signal strength accurately",
                    "Ground networks do not use signal-strength triggers at all",
                    "The satellite cannot store the measurement report while in motion",
                ],
                "The deck contrasts a fixed tower, where only the radio signal is unpredictable, with a satellite, where the geometry itself changes during the decision. The decision arrives based on outdated information.",
            ),
            (
                "What is the key insight that makes a proactive approach possible?",
                "A satellite's flight path follows fixed, well-known laws of orbital motion, so it can be predicted",
                [
                    "Users follow predictable daily movement patterns",
                    "Radio interference in space is lower and therefore more stable",
                    "Satellites broadcast their planned handover schedule in advance",
                ],
                "The deck notes the same physics is used to predict eclipses and plan rocket launches. Rise, culmination and set times can all be computed ahead of the event.",
            ),
            (
                "What does conditional handover give the device, and what is its stated limitation?",
                "Backup satellites and switching conditions arranged in advance, but the conditions are relatively simple and fixed",
                [
                    "A predicted handover time, but no backup target",
                    "A fully learned policy, but no fallback if prediction fails",
                    "A guaranteed target satellite, but only for stationary users",
                ],
                "Conditional handover removes the last-minute negotiation, which is a real improvement. The deck positions AI as filling the remaining gap by making those trigger conditions adaptive rather than fixed.",
            ),
            (
                "Layer 1 forecasts trajectory and channel quality. Which two approaches are named?",
                "Forecasting physical quantities using propagation models such as SGP4, or forecasting the RSRP time series with CNN plus LSTM models",
                [
                    "Forecasting user demand with a Markov chain, or forecasting load with a Kalman filter",
                    "Forecasting orbital decay with numerical integration, or forecasting weather with a neural network",
                    "Forecasting beam occupancy with a scheduler, or forecasting handover counts with regression",
                ],
                "The first predicts elevation angle, slant range, Doppler and path loss from known orbital mechanics. The second skips the physics and predicts the measured signal series directly.",
            ),
            (
                "In Layer 2 the handover is formulated as a Markov Decision Process. What is the action?",
                "Choosing a target satellite, or staying with the current one",
                [
                    "Deciding whether to send a measurement report",
                    "Setting the transmit power for the next uplink slot",
                    "Selecting which beam of the serving satellite to use",
                ],
                "State is the current and predicted link and geometry. Action is the association decision. Reward balances link quality against handover cost, penalising frequent handovers and failures.",
            ),
            (
                "How does DHO differ from the legacy protocol in the comparison shown?",
                "It removes the measurement report step entirely and predicts the handover action directly",
                [
                    "It adds a second measurement report to improve confidence",
                    "It moves the handover decision from the network to the device",
                    "It replaces the reward function with a fixed threshold",
                ],
                "The legacy sequence is measure, report, decide, hand over. DHO observes, decides and hands over, which is where the lower access delay and lower collision rate come from.",
            ),
            (
                "Layer 3 is compared to an air-traffic controller. What does that analogy convey?",
                "It optimises the handover pattern across all users and satellites at once, rather than one connection in isolation",
                [
                    "It gives priority to aviation users over other traffic",
                    "It routes each device along a fixed corridor through the constellation",
                    "It hands control of the decision to a human operator on the ground",
                ],
                "A controller sequences many aircraft onto runways so the whole system flows. The graph-based scheduler does the same for handovers, balancing load and avoiding congestion network-wide.",
            ),
        ],
    },
    {
        "topic": "AI-assisted trajectory optimization of UAV and HAPS platforms",
        "source": "Unnumbered deck, AI-Assisted Trajectory Optimization, slides 3 to 11",
        "questions": [
            (
                "What problem does AI-assisted trajectory optimization address in a 6G NTN?",
                "Static deployment produces poor coverage, high latency and network congestion in areas that are hard to serve",
                [
                    "Satellites cannot be launched into the orbits that 6G requires",
                    "Terrestrial base stations cannot support 6G modulation schemes",
                    "UAVs cannot legally operate in the same airspace as aircraft",
                ],
                "The platforms can move, but if they follow fixed paths they behave like fixed towers. Letting AI place and move them is what turns mobility into an advantage.",
            ),
            (
                "Which of these is listed as a 3D coverage challenge for current UAV and HAPS deployment?",
                "Static trajectories that do not adapt to where users actually are",
                [
                    "The inability of UAVs to operate above 20 km altitude",
                    "The lack of a standardised air interface for aerial platforms",
                    "Excessive spectrum allocated to aerial platforms",
                ],
                "The six listed challenges are static trajectories, uneven user distribution, coverage holes, high interference, energy limitations and dynamic user mobility.",
            ),
            (
                "In the deck's terms, how do artificial intelligence and machine learning relate?",
                "Machine learning is a branch of AI in which machines learn from data instead of being explicitly programmed",
                [
                    "Artificial intelligence is a branch of machine learning focused on autonomy",
                    "They are two names for the same set of techniques",
                    "Machine learning applies only to supervised problems, AI to unsupervised ones",
                ],
                "AI is the broad goal of machines performing human-like tasks. Machine learning is the specific approach of improving performance from data rather than from hand-written rules.",
            ),
            (
                "Why is deep reinforcement learning chosen for this problem?",
                "It learns by interacting with the environment, adapts to changing user locations and optimizes long-term reward",
                [
                    "It requires no training data of any kind",
                    "It produces a fixed optimal trajectory that never needs updating",
                    "It runs entirely on the ground, so the platform needs no compute",
                ],
                "Trajectory planning is sequential: where you go now changes what is available later. Optimising long-term reward rather than the immediate step is exactly what reinforcement learning does.",
            ),
            (
                "Which of these does the platform collect as part of its state?",
                "User locations, signal strength, battery level, traffic demand, obstacles, weather and backhaul link quality",
                [
                    "Preamble collisions, backoff windows and barring probabilities",
                    "Ephemeris, timing advance and Doppler shift",
                    "Slice identifiers, QoS flows and session contexts",
                ],
                "The state has to cover everything that should influence where the platform flies next, which is why it spans radio conditions, platform health, demand and the physical environment.",
            ),
            (
                "What does the reward function balance?",
                "Maximising coverage while minimising energy, delay and interference",
                [
                    "Maximising altitude while minimising flight time",
                    "Maximising throughput while minimising the number of platforms",
                    "Maximising battery life while minimising the number of users served",
                ],
                "Coverage alone would send the platform to an unsustainable position. The three penalties keep the solution within what the platform can physically sustain and what the network can tolerate.",
            ),
            (
                "Which outcomes earn a positive reward?",
                "More users covered, higher throughput, lower latency, lower interference and lower energy use",
                [
                    "Higher altitude, wider beams and longer flight duration",
                    "Fewer handovers, fewer beams and lower bandwidth use",
                    "More platforms deployed and larger coverage radius",
                ],
                "The positive terms are the service outcomes the network wants. The negative terms are coverage holes, signal blockage, high interference, excessive battery use and weak backhaul.",
            ),
            (
                "In the layered architecture, what role do HAPS platforms play?",
                "Quasi-stationary platforms at about 20 km that act as aerial base stations and provide backhaul for UAVs",
                [
                    "Low-altitude platforms that provide on-demand coverage of hotspots",
                    "Orbital platforms that provide wide-area broadcast services",
                    "Ground platforms that aggregate traffic from the terrestrial network",
                ],
                "The architecture stacks satellites for wide-area coverage, HAPS at about 20 km covering hundreds of kilometres, and low-altitude UAVs providing flexible on-demand capacity below.",
            ),
            (
                "Which is listed among the challenges of the approach?",
                "Airspace regulation",
                [
                    "The absence of any suitable learning algorithm",
                    "The inability to measure signal strength from an aerial platform",
                    "The lack of demand for coverage in remote areas",
                ],
                "The five challenges are battery limitations, AI computational complexity, airspace regulations, security and weather effects. Several are non-technical constraints on an otherwise workable technique.",
            ),
            (
                "What does the conclusion claim reinforcement learning enables?",
                "Autonomous, adaptive decision-making that improves coverage, energy efficiency and quality of service",
                [
                    "The removal of all terrestrial infrastructure from the network",
                    "A single fixed trajectory that is optimal for every deployment",
                    "Coverage guarantees that do not depend on battery capacity",
                ],
                "The claim is about how the decision is made, not about removing constraints. The platform decides for itself and keeps improving, and battery and regulation remain real limits.",
            ),
        ],
    },
]
