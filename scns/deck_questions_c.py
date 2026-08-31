# -*- coding: utf-8 -*-
"""TE 456 question data, groups 17 to 24.

Two decks in this range carry no group number on their title slide. They are
listed under their topic, in the position the file order puts them.

Format per question:
    (stem, correct_answer, [distractor, distractor, distractor], explanation)

See build_questions.py for how these are compiled."""

DECKS = [
    {
        "topic": 'eRACH, a learned random access protocol for LEO networks',
        "source": 'Group 17 deck, slides 3 to 8',
        "questions": [
            (
                'What makes the topology of a LEO network non-stationary from the point '
                'of view of random access?',
                'Satellites move fast, so the best one to reach changes within milliseconds',
                [
                    'The count of satellites in view changes as the constellation is expanded',
                    'Ground terminals move between the beams faster than the network can '
                    'track them',
                    'The preamble set is re-randomised by the network at each access window',
                ],
                'Standard RACH assumes a fixed tower and has no notion of which base '
                'station to associate with. In LEO that choice exists, it matters, and it '
                'changes continuously.',
            ),
            (
                'What is the quoted one-way propagation delay for LEO, and why does it '
                'matter for acknowledgement-based protocols?',
                '1 to 5 ms, which makes acknowledgement schemes slow and wasteful of retries',
                [
                    '1 to 5 ms, which is short enough for acknowledgement schemes to work '
                    'as is',
                    '20 to 60 ms, which forces most protocols to abandon acknowledgements '
                    'outright',
                    'Under 1 ms, so delay affects throughput but not the design of a protocol',
                ],
                "Even LEO's relatively short delay is long compared with the time a "
                'terrestrial protocol expects to wait. Protocols built on '
                'listen-then-send or send-then-acknowledge degrade under it.',
            ),
            (
                'In eRACH, what does each ground terminal observe locally?',
                'Where the satellite should be, and whether its own last attempt collided',
                [
                    'The queue length and preamble choice of each neighbouring terminal',
                    'A schedule the network broadcasts at the start of each access window',
                    'The aggregate collision rate as measured across the whole spot beam',
                ],
                'The design point is that terminals do not talk to each other. Each has '
                'only what it can see for itself: predictable geometry, and the outcome '
                'of its own last attempt.',
            ),
            (
                'What decision does the actor-critic network make at each terminal?',
                'Whether to access now and which satellite, or to back off and wait',
                [
                    'Which preamble index to select from the pool shared across terminals',
                    'How much transmit power should be applied to the outgoing preamble',
                    'Whether to use the terrestrial network in place of the satellite one',
                ],
                'The action space combines timing and association. Choosing when to '
                'transmit and which satellite to aim at is precisely what standard RACH '
                'leaves unspecified in a moving constellation.',
            ),
            (
                'What does emergent mean in the name emergent RACH?',
                'The access pattern arises from independent learning, with no signalling',
                [
                    'The protocol emerged from the standardisation process over several '
                    'releases',
                    'The satellite emerges into view and then broadcasts the access schedule',
                    'New preambles are generated on demand as further devices join the '
                    'network',
                ],
                'Terminals never communicate with each other. Over many orbital cycles '
                'they nonetheless learn to spread their attempts apart, so the '
                'coordination is a product of learning rather than of messaging.',
            ),
            (
                'Which quantitative result is reported for eRACH against standard RACH?',
                'About 55 percent higher throughput and near twice lower access delay',
                [
                    'About 31 percent higher throughput and near four times lower access '
                    'delay',
                    'About 55 percent lower collision rate and near twice higher throughput',
                    'Twice the throughput and about 55 percent lower access delay overall',
                ],
                'The summary cites Table II of the source paper. The gain is achieved '
                'with no inter-device coordination, which is the point being made.',
            ),
            (
                'What does the parameter rho control in eRACH?',
                'The balance between maximising throughput and avoiding collisions',
                [
                    'The learning rate applied to the actor-critic network during training',
                    'The number of candidate satellites a terminal is allowed to consider',
                    'The length of the backoff window, expressed in whole milliseconds',
                ],
                'Rho equals 0 tunes for throughput and rho equals 2 tunes for collision '
                'avoidance. That lets one protocol serve application classes with '
                'different tolerances.',
            ),
            (
                'Which challenge concerns the hardware rather than the algorithm?',
                'Computational complexity set against size, weight and power limits',
                [
                    'Sensitivity to the accuracy of the predicted satellite position',
                    'A collision tolerance higher than that of the standard protocol',
                    'The absence of any coordination between neighbouring devices',
                ],
                'Running a neural policy on a terminal or a payload costs compute, and '
                'both are budget-limited. The other two are properties of how the learned '
                'policy behaves.',
            ),
            (
                'Why is sensitivity to satellite positioning accuracy a concern for eRACH?',
                'Expected position is one of two inputs, so error corrupts the policy',
                [
                    'The terminal must report its own position before it is granted access',
                    'Positioning error changes which preamble the terminal ends up choosing',
                    'The satellite cannot compute a reward without an accurate position fix',
                ],
                'The policy acts on what it observes. If the predicted geometry is wrong, '
                'the decision about when and where to transmit is made on a false '
                'picture. The deck notes the protocol is nonetheless robust to such '
                'errors.',
            ),
            (
                'What is the headline problem statement in the conclusion?',
                'Standard access ignores satellite mobility, so collisions and delay rise',
                [
                    'Standard access cannot operate beyond a certain orbital velocity '
                    'threshold',
                    'Constellations have far too few preambles for the number of devices '
                    'served',
                    'Multi-agent learning is required by the specification for NTN access',
                ],
                'The deck frames the gap as a mismatch: a protocol designed for '
                'stationary towers is being used where the tower moves, and the resulting '
                'collisions and delays are the symptom.',
            ),
        ],
    },
    {
        "topic": 'RIS-enhanced NTN for coverage and capacity in 6G',
        "source": 'Group 18 deck, slides 2 to 10',
        "questions": [
            (
                'What is the coverage problem that a reconfigurable intelligent surface '
                'is meant to solve?',
                'A satellite needs a clear view, and an obstruction removes the link entirely',
                [
                    'The satellite beam is too wide to serve individual users efficiently',
                    'The satellite cannot generate enough beams for the users in its cell',
                    'Atmospheric absorption removes the link at the higher frequencies used',
                ],
                "The deck shows a user in a building's shadow with no line of sight. The "
                'link budget is already tight, so a blocked path is not a degraded link, '
                'it is no link.',
            ),
            (
                'How does a RIS steer a reflection without any RF chain?',
                'Each element sets its own phase, so the reflections add in one direction',
                [
                    'Each element amplifies the incident signal before it is re-radiated',
                    'The surface rotates physically so as to face the intended receiver',
                    'The surface shifts the signal to another frequency before reflecting',
                ],
                'This is passive beamforming. Controlling the relative phase across the '
                'aperture decides where the reflected wavefronts interfere '
                'constructively, and none of it requires a transmitter.',
            ),
            (
                'What distinguishes an active RIS from a passive RIS?',
                'Each element has an amplifier, so amplitude as well as phase is set',
                [
                    'It applies discrete phase steps rather than continuous phase control',
                    'It responds differently across the frequencies within a wide band',
                    'It is mounted on the satellite itself rather than on a building',
                ],
                'A passive RIS only adjusts phase, and sometimes amplitude, of what it '
                'reflects. An active RIS adds gain, which costs power and complexity but '
                'relieves the multiplied path loss.',
            ),
            (
                'Which RIS type uses discrete phase shifts such as 1-bit values of 0 or '
                '180 degrees?',
                'Digital RIS, using a small number of fixed discrete phase states',
                [
                    'Tunable analog RIS, using varactors for continuous phase',
                    'Hybrid RIS, mixing passive elements with amplified ones',
                    'Frequency-selective RIS, responding across several bands',
                ],
                'Digital RIS quantises the phase into a small number of states, which '
                'lowers complexity and cost. Tunable analog RIS uses varactors to give '
                'continuous phase at higher hardware cost.',
            ),
            (
                'Which RIS type is suited to wideband and multi-band operation?',
                'Frequency-selective RIS, whose elements vary across frequency',
                [
                    'Passive RIS, because it introduces no gain that varies with frequency',
                    'Hybrid RIS, because it mixes passive elements with active ones',
                    'Digital RIS, because a 1-bit phase control is frequency independent',
                ],
                'Giving elements a designed frequency response lets one surface '
                'manipulate several bands at once, which a single fixed phase profile '
                'cannot do.',
            ),
            (
                'Why must a RIS panel be large, and why must it be close to one end of '
                'the link?',
                'The two hops multiply rather than add, so combined loss is severe',
                [
                    'The panel must exceed the wavelength of the incident signal to work',
                    'A large panel is needed to dissipate heat produced by its controller',
                    'Regulations set a minimum aperture for reflecting satellite signals',
                ],
                'In a relay the two hops are separate links. In a passive reflection the '
                'losses compound, so the only remedies are a very large aperture and '
                'placing the surface near the transmitter or the receiver.',
            ),
            (
                'The deck states that a passive surface cannot measure anything itself. '
                'What problem does that create?',
                'The channel must be estimated elsewhere before the phases are computed',
                [
                    'The surface cannot be given an identity of its own in the network',
                    'The surface cannot confirm its reflection reached the intended user',
                    'The surface cannot be updated once it has been installed anywhere',
                ],
                'Setting the phases requires knowing the channel from the transmitter to '
                'the surface and from the surface to the user. A device that only '
                'reflects contributes no measurements toward that.',
            ),
            (
                'What is the near-field effect listed among the limitations?',
                'A large panel breaks the simple distance model far-field assumes',
                [
                    'The panel heats the surrounding structure when used at close range',
                    'The panel reflects into its own controller over short distances',
                    'The panel cannot be used indoors because of reflections off walls',
                ],
                'Standard beamforming assumes a plane wave across the aperture. When the '
                'aperture is large relative to the distance, the wavefront is curved and '
                'the plane-wave approximation fails.',
            ),
            (
                'How does a RIS add capacity as well as coverage?',
                'It gives a second path, so another spatial stream becomes possible',
                [
                    'It doubles the bandwidth that is made available on the existing path',
                    'It lets the satellite reuse one frequency across adjacent beams',
                    'It compresses the data being carried before reflecting it onward',
                ],
                'Coverage comes from building a path where none existed. Capacity comes '
                'from that path being distinct from the direct one, which gives the '
                'channel matrix another dimension to carry a stream on.',
            ),
            (
                'What is the stated standardisation status of RIS?',
                'A candidate for 6G, not yet present in any released standard',
                [
                    'Specified in Release 18 as a part of the 5G-Advanced work',
                    'Standardised by the ITU for satellite applications alone',
                    'Withdrawn from standardisation after Release 17 studies',
                ],
                'The deck is explicit that RIS is still before standardisation. It is '
                'presented as a promising technique rather than a deployable '
                'specification.',
            ),
        ],
    },
    {
        "topic": 'Uplink time synchronization for NTN without GNSS',
        "source": 'Group 21 deck, slides 3 to 11',
        "questions": [
            (
                'What system configuration does the deck assume throughout?',
                '5G NR, regenerative payload with onboard base station, LEO, CP-OFDM uplink',
                [
                    '5G NR, transparent bent-pipe payload, GEO orbit, with SC-FDMA on the '
                    'uplink',
                    'LTE, regenerative payload in MEO orbit, with CP-OFDM used on the uplink',
                    '5G NR, transparent payload in LEO, with OFDMA on the downlink alone',
                ],
                'The assumption matters because a regenerative payload puts the base '
                'station in orbit, so the timing reference the device must align to is on '
                'the satellite itself.',
            ),
            (
                'In the Release 17 dual-loop architecture, what are the three timing '
                'advance components?',
                'A broadcast common part, a device-computed part, and a measured trim',
                [
                    'An open-loop part, a closed-loop part, and a Doppler pre-compensation',
                    'A service link part, a feeder link part, and an inter-satellite part',
                    'A coarse part, a fine part, and a fractional subcarrier correction',
                ],
                'TA common is broadcast and covers what is shared across the beam. TA UE '
                "is the device's own geometry. TA adj is the residual correction "
                'signalled by the gNB after measurement.',
            ),
            (
                'Without GNSS, which part of the Release 17 scheme fails first?',
                'The open-loop calculation, since the device cannot locate itself',
                [
                    'The closed loop, since the base station can no longer measure arrival',
                    'The common broadcast, since the network is unable to compute a value',
                    'The cyclic prefix, since it can no longer absorb the delay spread',
                ],
                'The device is described as a blind UE. It cannot compute a propagation '
                'delay from geometry it cannot observe, so it has no basis for its '
                'initial timing advance.',
            ),
            (
                'Why is falling back to closed-loop signalling alone not sufficient?',
                'First transmissions land far outside the window, so nothing is ever measured',
                [
                    'The closed loop corrects frequency error but not any of the timing error',
                    'The base station cannot address a command to an unsynchronised device',
                    'The closed loop requires a navigation timestamp inside each command',
                ],
                'A closed loop can only refine an estimate that is already close enough '
                'to be received. With no starting estimate the signal lands outside the '
                'reception window and there is nothing to measure.',
            ),
            (
                'What is the key insight behind GNSS-time-free drift compensation?',
                'Motion changes the delay, so arrival drift reveals the correction',
                [
                    'The satellite broadcasts its own clock drift for the device to copy',
                    'Oscillator drift in the device is proportional to propagation delay',
                    'Arrival drift is removed by simply lengthening the cyclic prefix',
                ],
                'The device cannot measure absolute distance, but it can watch how the '
                'arrival time of successive downlink slots shifts. That drift is produced '
                'by the changing range, so it carries the information needed.',
            ),
            (
                'In the Extended Kalman Filter method, what does the state vector contain?',
                'Device latitude, satellite longitude and the distance between the two',
                [
                    'Device velocity, satellite velocity and the relative Doppler shift',
                    'Timing advance, frequency offset and the oscillator drift rate',
                    'Beam index, elevation angle to the satellite and the slant range',
                ],
                'The filter estimates the geometry the device cannot observe directly, '
                'and the timing advance follows from the estimated distance rather than '
                'from a GNSS fix.',
            ),
            (
                'What is the stated strength of the EKF approach?',
                'Robust performance, converging quickly onto accurate values',
                [
                    'Zero computational cost incurred on the user device itself',
                    'Complete independence from the received downlink signal',
                    'Equal accuracy at the beam edge and at the beam centre',
                ],
                'The filter runs a predict-then-update cycle, so each new measurement '
                'refines the estimate. That is what lets it converge quickly from a poor '
                'starting point.',
            ),
            (
                'What is the trade-off in the network-provided common timing advance method?',
                'Accurate near the beam centre, and well off out near the beam edge',
                [
                    'Accurate for low orbits, but failing badly for geostationary',
                    'Accurate at first, but drifting away as the satellite moves on',
                    'Working only for devices that already hold a navigation fix',
                ],
                'One broadcast value cannot describe every point in a footprint. It is '
                'correct where it was computed for, and its error grows with distance '
                'from that reference point.',
            ),
            (
                'In the timing advance feedback loop, what does the gNB actually measure?',
                'Whether the uplink arrived early, late, or inside the window',
                [
                    'The Doppler shift carried by the arriving uplink carrier signal',
                    'The received power of the uplink measured against a target',
                    'The number of retransmissions the device has already tried',
                ],
                'The expected reception window covers one uplink slot. The gNB classifies '
                'the arrival against that window and sends an increase, decrease or keep '
                'command accordingly, looping until alignment holds.',
            ),
            (
                'What is the overall conclusion of the deck?',
                'Alternative methods allow uplink synchronisation without GNSS',
                [
                    'GNSS is unavoidable for uplink synchronisation in any NTN',
                    'Uplink synchronisation is unnecessary with an onboard base station',
                    'GNSS is replaced by an atomic clock placed inside each device',
                ],
                'The deck presents four methods, each avoiding the GNSS dependency in a '
                'different way, and concludes that the Release 17 assumption is a design '
                'choice rather than a physical necessity.',
            ),
        ],
    },
    {
        "topic": 'Deep reinforcement learning for space-air-ground 6G resource allocation',
        "source": 'Group 22 deck, slides 2 to 14',
        "questions": [
            (
                'What is a space-air-ground integrated network?',
                'Satellites, aerial platforms and ground infrastructure as one system',
                [
                    'A satellite constellation that also carries an Earth observation payload',
                    'A terrestrial network whose backhaul happens to be over satellite',
                    'A network in which each user device is able to act as a relay',
                ],
                'The deck shows space, aerial and ground operation centres feeding one 6G '
                'core. The point is that all three tiers are managed together rather than '
                'as separate networks.',
            ),
            (
                'What is resource allocation in a SAGIN, and why is it needed?',
                'Sharing limited link and compute resources so service stays fair',
                [
                    'Giving each satellite a fixed share of the spectrum at launch time',
                    'Deciding which ground stations will serve which orbital planes',
                    'Allocating onboard storage for traffic that has been buffered',
                ],
                'Resources are scarce and demand keeps moving. Sharing them intelligently '
                'is what keeps performance and fairness acceptable as the geometry and '
                'the traffic change.',
            ),
            (
                'Which three challenges are listed for SAGIN 6G NTN?',
                'Scarce spectrum, limited onboard energy, and shifting user demand',
                [
                    'Orbital debris, the cost of launch, and gaining regulatory approval',
                    'Handover failure, loss of packets, and jitter on the delivered stream',
                    'Key distribution, device authentication, and leakage of private data',
                ],
                'All three are resource problems. There is not enough spectrum, not '
                'enough power, and the demand that has to be served with them will not '
                'stay still.',
            ),
            (
                'In the general DRL model, what constitutes the state?',
                'Available power, bandwidth, signal quality and channel information',
                [
                    'The total reward accumulated over the course of the previous episode',
                    'The set of actions that the agent has not yet attempted to take',
                    'The orbital elements of each satellite within the constellation',
                ],
                'The state is what the agent observes about the environment before '
                'acting. Here that is the current resource and channel picture that the '
                'allocation decision has to be made from.',
            ),
            (
                'What does the action consist of in this framework?',
                'Channel allocation, power control and selection of an access point',
                [
                    'Execution of a handover and the shaping of a beam, and nothing else',
                    'Shaping of the reward signal and updating of the learned policy',
                    'Broadcast of ephemeris and signalling of the timing advance value',
                ],
                'The action is the decision the policy controller emits. Those three '
                'levers are what actually change how resources are distributed in the '
                'network.',
            ),
            (
                'What is the reward built from?',
                'Service quality, experienced quality, and efficient use of spectrum',
                [
                    'Rate of collision, delay before access, and the energy spent per bit',
                    'Achieved throughput, end-to-end latency, and the orbital altitude',
                    'Area of coverage, count of satellites, and the rate of handover',
                ],
                'The reward defines what good allocation means. Combining service '
                'quality, experienced quality and efficient spectrum use captures both '
                "the user's view and the operator's view.",
            ),
            (
                'Which algorithm is described as choosing from a list of fixed options, '
                'such as which channel to use?',
                'Deep Q-Network, which scores each option and picks the best',
                [
                    'Deterministic policy gradient, which outputs a real value',
                    'Proximal policy optimisation, which updates conservatively',
                    'Soft actor-critic, which explores widely while converging reliably',
                ],
                'DQN works over a discrete action set. Continuous quantities such as an '
                'exact power level need DDPG or a similar method that outputs a real '
                'value rather than a choice.',
            ),
            (
                'Which algorithm is described as fine-tuning exact values such as a '
                'precise power level?',
                'Deterministic policy gradient, giving a continuous output',
                [
                    'Deep Q-Network, which selects from among a set of discrete choices',
                    'Proximal policy optimisation, which updates step by step',
                    'Twin delayed variant, which reduces overestimation error',
                ],
                'DDPG is the continuous-control counterpart to DQN. PPO is described as '
                'learning a stable strategy step by step, and SAC or TD3 as exploring '
                'boldly while converging reliably.',
            ),
            (
                'In the HAPS tier, which three allocation tasks are named?',
                'Position placement, spectrum and power sharing, and edge computing',
                [
                    'Beam hopping, spectrum provisioning, and allocation of transmit power',
                    'Drone placement in three dimensions, channel estimation, interference',
                    'Traffic offloading, base station selection, and routing to the cloud',
                ],
                'Each tier has its own task list. Beam hopping and frequency assignment '
                'belong to the space tier, and 3D location assignment belongs to the UAV '
                'tier.',
            ),
            (
                'Which three challenges are listed for DRL-based SAGIN resource allocation?',
                'Scale, an environment that will not hold still, and hard deadlines',
                [
                    'Scarce training data, the simulation gap, and certification of policy',
                    'Self-interference, node synchronisation, and onboard compute limits',
                    'Bandwidth overhead, handshake latency, and hardened slow processors',
                ],
                'The environment is large, it will not hold still long enough for a '
                'policy to settle, and decisions are needed faster than learning '
                'naturally converges. Those three are what make the problem hard.',
            ),
        ],
    },
    {
        "topic": 'HARQ mechanisms and limitations in NTN',
        "source": 'Group 23 deck, slides 2 to 14',
        "questions": [
            (
                'How does HARQ differ from ARQ and from forward error correction alone?',
                'It keeps the failed copy and combines it with the retransmission',
                [
                    'It retransmits automatically without waiting for any acknowledgement',
                    'It corrects errors outright without ever needing a retransmission',
                    'It applies correction only after a first retransmission has failed',
                ],
                'ARQ waits for an acknowledgement and resends. FEC adds redundancy and '
                'decodes without resending. HARQ does both, and crucially keeps the '
                'failed copy so the two receptions can be combined.',
            ),
            (
                'In chase combining, what does the transmitter send on the retransmission?',
                'The same coded packet again, combined with the stored soft bits',
                [
                    'A different set of parity bits produced by that very same encoder',
                    'Just the systematic bits, without any of the parity bits sent',
                    'A shorter packet holding just the bits that failed to decode',
                ],
                'The receiver keeps the soft bits from the first attempt rather than '
                'discarding them. Adding a second identical copy raises the effective '
                'signal-to-noise ratio enough to decode.',
            ),
            (
                'What distinguishes incremental redundancy from chase combining?',
                'Different parity is sent, so punctured bits now reach the receiver',
                [
                    'The retransmission is sent at a noticeably higher power level',
                    'The receiver discards the first copy before decoding the second',
                    'The retransmission is carried using an entirely different modulation',
                ],
                'The first transmission punctures some parity bits to raise the code '
                'rate. The retransmission supplies those bits, so the combined packet is '
                'protected by a lower-rate, stronger code.',
            ),
            (
                'Why does long round-trip time stall the HARQ pipeline in NTN?',
                'Every process waits on its acknowledgement, so none is left free',
                [
                    'The soft buffer overflows before the acknowledgement can arrive',
                    'The acknowledgement expires and is then discarded by the receiver',
                    'The receiver cannot decode a packet arriving after a long delay',
                ],
                'A HARQ process is held from transmission until its acknowledgement '
                'returns. On a short terrestrial link they are released quickly. Over a '
                '30 ms to 500 ms round trip they all fill up and transmission stops.',
            ),
            (
                'How many HARQ processes does 5G use by default, and what does the NTN '
                'adaptation raise that to?',
                '16 by default, raised to as many as 32 for non-terrestrial use',
                [
                    '8 by default, raised to as many as 16 for non-terrestrial use',
                    '16 by default, raised to as many as 64 for any non-terrestrial use',
                    '32 by default, raised to as many as 64 for non-terrestrial use',
                ],
                'More parallel processes keep the pipe full while earlier ones wait for '
                'acknowledgements. The cost is proportionally more soft buffer memory in '
                'the receiver.',
            ),
            (
                'What is feedback-less HARQ operation, and what does it rely on instead?',
                'No acknowledgement is sent, so strong coding carries the load',
                [
                    'Just negative acknowledgements are sent, halving the feedback load',
                    'Feedback is sent to the gateway rather than to the satellite',
                    "Feedback is deferred until the end of the satellite's pass",
                ],
                'Removing the acknowledgement removes the waiting, which is what caused '
                'the stall. The redundancy has to be added in advance instead, because '
                'there is no longer any signal telling the sender what failed.',
            ),
            (
                'In HARQ-less operation, where is error recovery performed?',
                'At the link control layer, slower but without stalling the pipe',
                [
                    'At the physical layer, by using a more robust modulation scheme',
                    'At the application layer, by requesting the whole file once more',
                    'On the satellite, which retransmits from a buffer of its own',
                ],
                'The MAC and PHY stop waiting for HARQ feedback entirely. Recovery still '
                'happens, but a layer up, which trades slower error recovery for a '
                'pipeline that keeps moving.',
            ),
            (
                'Which trade-off pair is stated correctly?',
                'More processes raise throughput and call for more memory',
                [
                    'Longer timers speed failure detection and use less memory',
                    'Disabling feedback speeds recovery and avoids false alarms',
                    'Onboard processing gives the slowest loop at the lowest cost',
                ],
                'The four trade-offs are: more processes buy throughput with memory; '
                'longer timers avoid false alarms but slow failure detection; disabling '
                'feedback keeps flow constant but delays recovery; onboard processing '
                'gives the fastest loop at the highest satellite cost.',
            ),
            (
                'In a transparent payload, where does the gNB sit relative to the HARQ loop?',
                'On the ground, so the loop crosses service and feeder links',
                [
                    'On the satellite, so the loop covers just the service link',
                    'Inside the core network, so the loop crosses to the internet',
                    'Split across satellite and gateway, one process on each side',
                ],
                'A transparent satellite is a repeater. The base station is at the '
                'gateway, so an acknowledgement travels user to satellite to gateway and '
                'back, which is the longest possible loop.',
            ),
            (
                'What does a regenerative payload change about the HARQ loop?',
                'The station is aboard, so the loop closes over the service link',
                [
                    'The loop disappears, since errors are corrected while on board',
                    'The loop is extended to take in the inter-satellite link as well',
                    'The loop is moved up to the link control layer automatically',
                ],
                'Putting the base station in orbit halves the geometry the '
                'acknowledgement has to cross. That is the fastest loop, and the deck '
                'notes it is also the highest satellite cost.',
            ),
        ],
    },
    {
        "topic": 'Network digital twinning for 3D satellite constellation optimization',
        "source": 'Group 24 deck, slides 3 to 9',
        "questions": [
            (
                'What is a network digital twin?',
                'A virtual replica continuously updated from real-world data',
                [
                    'A backup constellation held in reserve in case of a failover',
                    'A simulation model built once during the design phase only',
                    'A duplicate of the control software running on the ground',
                ],
                'The defining property is the live link back to reality. A model that is '
                'not continuously updated is a simulation; the continuous update is what '
                'makes it a twin.',
            ),
            (
                'Which of these is listed as a challenge that makes a 6G NTN '
                'constellation hard to manage?',
                'Rapid topology change, as links are created and broken',
                [
                    'The gradual decay of orbits across the mission lifetime',
                    'The limited number of ground stations licensed globally',
                    'The fixed bandwidth agreed at constellation design time',
                ],
                'The six challenges are constant mobility, rapid topology change, long '
                'propagation delay, limited onboard resources, frequent handovers and '
                'high deployment and maintenance cost.',
            ),
            (
                'What are the stated consequences of those challenges?',
                'Higher latency, unstable routing, slow fault detection, more cost',
                [
                    'Orbital debris, the risk of collision, and end-of-life disposal cost',
                    'Spectrum interference, cross-border rules, and licensing delay',
                    'Compromised keys, replay attacks, and exposure of identities',
                ],
                'The consequence row follows directly from the challenge row: a network '
                'that changes every second is hard to route through, hard to allocate for '
                'and hard to diagnose.',
            ),
            (
                'In the hierarchical digital twin architecture, what does the network '
                'control centre hold?',
                'A global controller and a central twin of the whole network',
                [
                    'An edge twin maintained for each individual ground station',
                    'The physical satellites together with their telemetry links',
                    'A local controller managing beam and radio resource allocation',
                ],
                'The hierarchy runs from edge twins at the ground stations, through local '
                'controllers, up to a central twin and a global controller at the network '
                'control centre.',
            ),
            (
                'Which functions belong to the local controller at a ground station?',
                'Beam and radio allocation, data processing, and fault diagnosis',
                [
                    'Network verification, slice management, global optimisation',
                    'Traffic engineering and modelling of the network as a whole',
                    'Orbit determination and the broadcast of ephemeris to users',
                ],
                'The split is by scope. Local controllers handle what happens at one '
                'station, while the global controller handles network verification, '
                'slicing, traffic engineering and whole-network optimisation.',
            ),
            (
                'What are the five steps by which digital twinning optimizes a constellation?',
                'Collect, synchronise, simulate futures, evaluate, and then deploy',
                [
                    'Observe, decide, act, learn, and then repeat the entire cycle',
                    'Sense, optimise, act, learn, and finally verify the outcome',
                    'Predict, measure, correct, verify, and log for later review',
                ],
                'The distinguishing step is simulating multiple futures before committing '
                'to one. That is what a twin adds over a plain control loop: decisions '
                'are tested in the model rather than on the live network.',
            ),
            (
                'Which benefits are attributed to the digital twin approach?',
                'Lower latency, better routing, faster faults, lower cost',
                [
                    'Higher orbits, wider coverage, and a longer satellite life',
                    'Stronger encryption, better authentication, more privacy',
                    'Larger constellations, cheaper launch, faster deployment',
                ],
                'All four follow from being able to test a decision before applying it: '
                'better routes are found, faults are noticed sooner, and fewer costly '
                'interventions are needed on the real network.',
            ),
            (
                'Why is DT migration complexity listed as a limitation?',
                'Twins must migrate as the satellites they model keep moving',
                [
                    'Twins need re-certifying whenever network software is updated',
                    'Twins cannot be transferred between different vendor platforms',
                    'Twins lose their accumulated history whenever they are moved',
                ],
                'A twin is anchored to the physical thing it mirrors. When that thing is '
                'in orbit and the serving infrastructure changes, the twin has to follow '
                'it, which adds machinery the ground case does not need.',
            ),
            (
                'Why is synchronization overhead a real cost rather than an '
                'implementation detail?',
                'Keeping model and network in step consumes link bandwidth',
                [
                    'Synchronisation requires an atomic clock on each satellite',
                    'The twin cannot run at all while synchronisation is running',
                    'Synchronisation errors accumulate and cannot be corrected',
                ],
                'The twin is only useful while it matches reality, and matching reality '
                'means a continuous stream of telemetry. On a link where capacity is '
                'scarce, that stream competes with user traffic.',
            ),
            (
                'What is the security concern raised about digital twins?',
                'A compromised twin could be used to disrupt the real network',
                [
                    'The twin holds subscriber data that could be exposed by leak',
                    "The twin's synchronisation traffic cannot be encrypted at all",
                    'The twin can be used to locate satellites for physical attack',
                ],
                'The twin is not a passive mirror. Decisions computed in it are deployed '
                'to the physical network, so an attacker who controls the twin gains '
                'influence over the real constellation.',
            ),
        ],
    },
    {
        "topic": 'AI-driven predictive handover for high-mobility LEO networks',
        "source": 'Unnumbered deck, AI-Driven Predictive Handover Management, slides 4 to 16',
        "questions": [
            (
                'How does the handover situation in a LEO network differ from a '
                'terrestrial one?',
                'On the ground you pass towers; in orbit the tower passes you',
                [
                    'In orbit the user selects the satellite manually each session',
                    'In orbit handovers occur only when the user physically moves',
                    'In orbit the satellite hands over without telling the device',
                ],
                'This is the root of every other problem in the deck. A stationary user '
                'still gets handed over every few minutes, because the coverage is what '
                'is moving.',
            ),
            (
                'What is a handover storm?',
                'Many devices on one satellite must switch at nearly one time',
                [
                    'A single device switching repeatedly between two satellites',
                    'A burst of signalling brought on by the failure of a satellite',
                    'Handovers triggered by atmospheric interference during storms',
                ],
                'The deck likens it to every shopper reaching the same checkout at once. '
                'Because they all share one satellite, they all lose it together, and the '
                'signalling arrives in one spike.',
            ),
            (
                'What is the ping-pong effect, and what causes it?',
                'A device flips between two satellites because confidence is low',
                [
                    'A device alternates between uplink and downlink of one satellite',
                    'An acknowledgement bounces between the satellite and the gateway',
                    'A beam sweeps back and forth across the very same ground cell',
                ],
                'Each flip costs signalling and interrupts the connection, so the effect '
                'wastes effort and degrades service without ever improving the link.',
            ),
            (
                'Why is a reactive handover riskier in a satellite network than on the '
                'ground?',
                'The decision returns after the satellite has already moved on',
                [
                    'Satellite receivers cannot measure signal strength accurately',
                    'Ground networks make no use of signal-strength triggers at all',
                    'The satellite cannot store a measurement report while moving',
                ],
                'The deck contrasts a fixed tower, where only the radio signal is '
                'unpredictable, with a satellite, where the geometry itself changes '
                'during the decision. The decision arrives based on outdated information.',
            ),
            (
                'What is the key insight that makes a proactive approach possible?',
                "A satellite's flight path follows fixed laws and is therefore predictable",
                [
                    'Users follow movement patterns that repeat closely from day to day',
                    'Radio interference in space is lower and so is more stable',
                    'Satellites broadcast their planned handover schedule ahead',
                ],
                'The deck notes the same physics is used to predict eclipses and plan '
                'rocket launches. Rise, culmination and set times can all be computed '
                'ahead of the event.',
            ),
            (
                'What does conditional handover give the device, and what is its stated '
                'limitation?',
                'Backups and conditions set ahead, but the conditions are fixed',
                [
                    'A predicted handover time, but no backup target is provided',
                    'A fully learned policy, but no fallback if prediction fails',
                    'A guaranteed target satellite, but only for users that are stationary',
                ],
                'Conditional handover removes the last-minute negotiation, which is a '
                'real improvement. The deck positions AI as filling the remaining gap by '
                'making those trigger conditions adaptive rather than fixed.',
            ),
            (
                'Layer 1 forecasts trajectory and channel quality. Which two approaches '
                'are named?',
                'Forecast physical quantities from orbit models, or forecast signal series',
                [
                    'Forecast user demand with a Markov chain, or forecast load with a filter',
                    'Forecast orbital decay numerically, or forecast weather with a network',
                    'Forecast beam occupancy with a scheduler, or handover counts by '
                    'regression',
                ],
                'The first predicts elevation angle, slant range, Doppler and path loss '
                'from known orbital mechanics. The second skips the physics and predicts '
                'the measured signal series directly.',
            ),
            (
                'In Layer 2 the handover is formulated as a Markov Decision Process. What '
                'is the action?',
                'Choosing a target satellite, or staying with the current one',
                [
                    'Deciding whether or not to send a measurement report now',
                    'Setting the transmit power to use for the next uplink slot',
                    'Selecting which beam of the serving satellite ought to be used',
                ],
                'State is the current and predicted link and geometry. Action is the '
                'association decision. Reward balances link quality against handover '
                'cost, penalising frequent handovers and failures.',
            ),
            (
                'How does DHO differ from the legacy protocol in the comparison shown?',
                'It drops the measurement report and predicts the action directly',
                [
                    'It adds a second measurement report in order to raise the confidence',
                    'It moves the handover decision from the network to the device',
                    'It replaces the reward function with a simple fixed threshold',
                ],
                'The legacy sequence is measure, report, decide, hand over. DHO observes, '
                'decides and hands over, which is where the lower access delay and lower '
                'collision rate come from.',
            ),
            (
                'Layer 3 is compared to an air-traffic controller. What does that analogy '
                'convey?',
                'It optimises handovers across all users rather than one link',
                [
                    'It gives priority to aviation users ahead of all other traffic',
                    'It routes each device down a fixed corridor through the sky',
                    'It hands the decision to a human operator on the ground below',
                ],
                'A controller sequences many aircraft onto runways so the whole system '
                'flows. The graph-based scheduler does the same for handovers, balancing '
                'load and avoiding congestion network-wide.',
            ),
        ],
    },
    {
        "topic": 'AI-assisted trajectory optimization of UAV and HAPS platforms',
        "source": 'Unnumbered deck, AI-Assisted Trajectory Optimization, slides 3 to 11',
        "questions": [
            (
                'What problem does AI-assisted trajectory optimization address in a 6G NTN?',
                'Static deployment gives poor coverage, high delay and congestion',
                [
                    'Satellites cannot be launched into any of the orbits that 6G requires',
                    'Terrestrial stations cannot support the 6G modulation schemes',
                    'Drones are barred from operating in the same airspace as aircraft',
                ],
                'The platforms can move, but if they follow fixed paths they behave like '
                'fixed towers. Letting AI place and move them is what turns mobility into '
                'an advantage.',
            ),
            (
                'Which of these is listed as a 3D coverage challenge for current UAV and '
                'HAPS deployment?',
                'Static trajectories that do not adapt to where users actually are',
                [
                    'The inability of any drone to operate above about 20 km of altitude',
                    'The lack of a standardised air interface for aerial platforms',
                    'An excessive amount of spectrum allocated to aerial platforms',
                ],
                'The six listed challenges are static trajectories, uneven user '
                'distribution, coverage holes, high interference, energy limitations and '
                'dynamic user mobility.',
            ),
            (
                "In the deck's terms, how do artificial intelligence and machine learning "
                'relate?',
                'Machine learning is a branch of AI that learns from the data',
                [
                    'Artificial intelligence is a branch of machine learning',
                    'They are two different names for one set of techniques',
                    'Machine learning covers supervised problems, AI the rest',
                ],
                'AI is the broad goal of machines performing human-like tasks. Machine '
                'learning is the specific approach of improving performance from data '
                'rather than from hand-written rules.',
            ),
            (
                'Why is deep reinforcement learning chosen for this problem?',
                'It learns by interaction, adapts, and optimises long-term reward',
                [
                    'It requires no training data of any kind at any point before deployment',
                    'It yields one fixed trajectory that avoids needing updates',
                    'It runs on the ground, so the platform carries no compute',
                ],
                'Trajectory planning is sequential: where you go now changes what is '
                'available later. Optimising long-term reward rather than the immediate '
                'step is exactly what reinforcement learning does.',
            ),
            (
                'Which of these does the platform collect as part of its state?',
                'User positions, signal, battery, demand, obstacles and weather',
                [
                    'Preamble collisions, backoff windows and the barring probabilities',
                    'Ephemeris data, the timing advance and the Doppler shift value',
                    'Slice identifiers, quality flows and the session context data',
                ],
                'The state has to cover everything that should influence where the '
                'platform flies next, which is why it spans radio conditions, platform '
                'health, demand and the physical environment.',
            ),
            (
                'What does the reward function balance?',
                'Coverage against energy, against delay and against interference',
                [
                    'Altitude against the total flight time available to the platform',
                    'Throughput against the number of platforms that are deployed',
                    'Battery life against the number of users that can be served',
                ],
                'Coverage alone would send the platform to an unsustainable position. The '
                'three penalties keep the solution within what the platform can '
                'physically sustain and what the network can tolerate.',
            ),
            (
                'Which outcomes earn a positive reward?',
                'More users covered, higher rate, lower delay and less energy',
                [
                    'Higher altitude, wider beams and a longer duration of flight',
                    'Fewer handovers, fewer beams and lower use of the bandwidth',
                    'More platforms deployed and a larger radius of ground coverage',
                ],
                'The positive terms are the service outcomes the network wants. The '
                'negative terms are coverage holes, signal blockage, high interference, '
                'excessive battery use and weak backhaul.',
            ),
            (
                'In the layered architecture, what role do HAPS platforms play?',
                'Quasi-stationary at about 20 km, serving users and backhauling',
                [
                    'Low-altitude platforms giving coverage of hotspots when it is needed',
                    'Orbital platforms providing wide-area broadcast services',
                    'Ground platforms aggregating traffic from the fixed network',
                ],
                'The architecture stacks satellites for wide-area coverage, HAPS at about '
                '20 km covering hundreds of kilometres, and low-altitude UAVs providing '
                'flexible on-demand capacity below.',
            ),
            (
                'Which is listed among the challenges of the approach?',
                'Airspace regulation, which limits where a platform is flown',
                [
                    'The absence of any learning algorithm suited to the problem',
                    'The inability to measure signal strength from a flying platform',
                    'The lack of demand for any coverage across remote regions',
                ],
                'The five challenges are battery limitations, AI computational '
                'complexity, airspace regulations, security and weather effects. Several '
                'are non-technical constraints on an otherwise workable technique.',
            ),
            (
                'What does the conclusion claim reinforcement learning enables?',
                'Autonomous adaptive decisions improving coverage and efficiency',
                [
                    'The removal of all the terrestrial infrastructure from the network',
                    'One fixed trajectory that proves optimal for every deployment',
                    'Coverage guarantees that do not depend on battery capacity',
                ],
                'The claim is about how the decision is made, not about removing '
                'constraints. The platform decides for itself and keeps improving, and '
                'battery and regulation remain real limits.',
            ),
        ],
    },
]
