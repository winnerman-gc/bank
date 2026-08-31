# -*- coding: utf-8 -*-
"""TE 456 question data, groups 9 to 16.

Format per question:
    (stem, correct_answer, [distractor, distractor, distractor], explanation)

See build_questions.py for how these are compiled."""

DECKS = [
    {
        "topic": 'ISAC-enabled non-terrestrial networks for 6G',
        "source": 'Group 9 deck, slides 2 to 11',
        "questions": [
            (
                'What is the defining feature of Integrated Sensing and Communication?',
                'One waveform, one RF front end and one slice of spectrum serve both '
                'functions',
                [
                    'A radar payload is flown alongside a communication payload on one '
                    'satellite',
                    'Sensing data is carried as payload traffic over the communication link',
                    'A communication link switches between data and radar modes in turn',
                ],
                'The integration is in the hardware and the waveform, not in the '
                'packaging. Two payloads on one bus, or time-sharing one link, both keep '
                'the functions separate; ISAC does not.',
            ),
            (
                'Why is a GEO satellite ranged rather than tracked by Doppler?',
                'GEO shows almost no Doppler because it is nearly stationary relative to '
                'the ground',
                [
                    'GEO satellites transmit at a frequency too high for Doppler processing',
                    'GEO Doppler is masked by ionospheric scintillation',
                    'GEO orbits are known exactly, so no tracking is needed at all',
                ],
                'Doppler needs relative radial motion. A geostationary satellite holds '
                'its position over a point on the ground, so the shift is close to zero '
                'and there is no signature to track.',
            ),
            (
                'In a multistatic ISAC configuration, what is the arrangement?',
                'One transmission is received by several nodes across the constellation',
                [
                    'Each satellite transmits and listens for its own echo',
                    'One satellite transmits and a single second satellite receives the '
                    'reflection',
                    'The ground station transmits and the satellites all receive',
                ],
                'The deck shows one transmitter and receivers Rx1 through Rx4 all '
                'catching the same echo. Many viewing angles on one target is what turns '
                'the constellation itself into a radar.',
            ),
            (
                'Self-interference is a problem in which geometry, and why?',
                'Monostatic, because the receiver must hear a faint echo through its own '
                'loud transmitter',
                [
                    'Bistatic, because the two nodes are not synchronised',
                    'Multistatic, because several echoes arrive at once',
                    'All three equally, because the waveform is shared',
                ],
                'Sharing one aperture means transmitting and receiving at the same time '
                'and place. The returning echo is many orders of magnitude weaker than '
                'the outgoing signal sitting on top of it.',
            ),
            (
                'Roughly how much cancellation is quoted as necessary for the monostatic '
                'case?',
                'More than 70 dB',
                [
                    'More than 20 dB',
                    'More than 40 dB',
                    'More than 120 dB',
                ],
                'The deck specifies more than 70 dB of combined analog and digital '
                'cancellation, and notes that it has to be achieved on a moving payload, '
                'which makes it harder still.',
            ),
            (
                'What is the principal challenge that bistatic and multistatic operation '
                'introduces, and that monostatic avoids?',
                'Time and phase synchronisation across independent nodes',
                [
                    'Self-interference between transmit and receive',
                    'The need for a joint waveform design',
                    'The absence of a native ISAC standard',
                ],
                'One aperture shares one clock by construction. Splitting transmit from '
                'receive across separate spacecraft means those spacecraft have to agree '
                'on time and phase to sub-microsecond accuracy.',
            ),
            (
                'Why does limited onboard power and compute add latency to ISAC over NTN?',
                'Processing is pushed down to the ground rather than done on board',
                [
                    'The waveform has to be transmitted at a lower rate',
                    'The receiver must integrate over a longer dwell time',
                    'The satellite must store echoes until it passes a gateway',
                ],
                'If the payload cannot process the returns itself, the raw data has to be '
                'downlinked and processed on the ground, and the answer comes back a full '
                'round trip later.',
            ),
            (
                'Which advantage follows directly from not needing dedicated sensing '
                'spectrum?',
                'Enhanced spectral efficiency and reduced congestion',
                [
                    'High-precision localization',
                    'Extreme disaster resilience',
                    'Real-time environment mapping',
                ],
                'Conventional radar occupies a band that carries no data. Folding the '
                'sensing into the communication waveform frees that allocation, which is '
                'a spectrum-efficiency gain rather than a capability gain.',
            ),
            (
                'In the maritime use case, what is meant by one beam doing two jobs?',
                'The beam tracks ships and reads sea state while also serving broadband',
                [
                    'The beam serves two vessels at the same time',
                    'The beam alternates between uplink and downlink',
                    'The beam covers both the coastline and the open ocean',
                ],
                'The two jobs are sensing and communication, not two users or two '
                'directions. Over water there are no towers, so the same beam has to earn '
                'its place twice.',
            ),
            (
                'DebriSense-THz is quoted with which performance figure?',
                '95 to 99 percent classification accuracy at 5 THz',
                [
                    '70 dB of interference cancellation at 5 THz',
                    'Sub-microsecond synchronisation at 5 THz',
                    '95 to 99 percent spectral efficiency gain at 5 THz',
                ],
                'The figure belongs to the space situational awareness use case: '
                'detecting, tracking and classifying orbiting debris, where '
                'classification accuracy is the metric that matters.',
            ),
        ],
    },
    {
        "topic": 'AI-native Open RAN for NTN',
        "source": 'Group 10 deck, slides 3 to 13',
        "questions": [
            (
                'What separates the Non-RT RIC from the Near-RT RIC?',
                'The Non-RT RIC runs loops slower than one second and the Near-RT RIC '
                'faster than one second',
                [
                    'The Non-RT RIC runs on the satellite and the Near-RT RIC on the ground',
                    'The Non-RT RIC handles user data and the Near-RT RIC handles control '
                    'signalling',
                    'The Non-RT RIC is vendor-specific and the Near-RT RIC is open',
                ],
                'The split is by control-loop timescale. Slow work such as policy and '
                'model training goes above one second; fast optimisation through xApps '
                'goes below it.',
            ),
            (
                'Which functions sit in the O-CU-CP?',
                'RRC and PDCP',
                [
                    'RLC and MAC',
                    'SDAP and PDCP',
                    'High-PHY and Low-PHY',
                ],
                'The control-plane half of the central unit carries RRC together with '
                'PDCP. SDAP with PDCP is the user-plane half, and RLC with MAC belongs to '
                'the distributed unit.',
            ),
            (
                'What is the main structural difference between traditional RAN and Open RAN?',
                'Open RAN splits the chain into functions that may come from different '
                'vendors',
                [
                    'Open RAN removes the need for a core network',
                    'Open RAN places all processing in the radio unit',
                    'Open RAN uses satellites instead of ground towers',
                ],
                "A traditional RAN is a single vendor's baseband unit and radio unit "
                'joined by proprietary interfaces. Open RAN standardises those interfaces '
                'so O-CU, O-DU and O-RU can be sourced separately.',
            ),
            (
                'In the AI-RAN model, which layer covers AI hardware, AI software and AI '
                'integration used to improve the network itself?',
                'AI-for-RAN',
                [
                    'AI-on-RAN',
                    'AI-and-RAN',
                    'AI-over-RAN',
                ],
                'The three layers are concentric. AI-for-RAN is the innermost and points '
                'inward at the network. AI-and-RAN shares infrastructure, and AI-on-RAN '
                'sells services outward over the network.',
            ),
            (
                'AI-on-RAN is best described as:',
                'Delivering AI services to customers over the network',
                [
                    'Using AI to optimize scheduling inside the base station',
                    'Sharing infrastructure between AI workloads and RAN workloads',
                    'Training AI models on the satellite payload',
                ],
                'It is the outermost layer, covering the marketplace platform, developer '
                'tools and global access. The network becomes the delivery channel for AI '
                'rather than the thing being optimised.',
            ),
            (
                'Which component actually allocates satellite beams and resources to user '
                'devices in the described NTN pipeline?',
                'xApps running on the Near-RT RIC',
                [
                    'The Service Management and Orchestration framework',
                    'rApps running on the Non-RT RIC',
                    'The O-RU on board the satellite',
                ],
                'The machine learning engine predicts and optimises, but the allocation '
                'itself is a fast control action, and fast control actions are what xApps '
                'on the Near-RT RIC exist to perform.',
            ),
            (
                'Why does satellite mobility create a problem for Open RAN specifically?',
                'O-RAN interfaces assume a static fronthaul with predictable latency',
                [
                    'Open interfaces cannot carry ephemeris data',
                    'The O-Cloud cannot be deployed on a moving platform',
                    'xApps must be recompiled for each orbital plane',
                ],
                'The functional splits were designed for a fibre run of known length '
                'between a baseband unit and a radio unit. A moving satellite changes '
                'that path length continuously, which breaks the timing assumption.',
            ),
            (
                'The RIC placement question in NTN is a choice between:',
                'The ground segment and the satellite',
                [
                    'The core network and the radio unit',
                    'The Non-RT RIC and the Near-RT RIC',
                    'A single vendor and multiple vendors',
                ],
                'Putting the RIC on the ground keeps compute cheap and adds a round trip '
                'to every decision. Putting it on the satellite removes the round trip '
                'and spends scarce onboard power.',
            ),
            (
                'Which AI application is described as using signal strength, network load '
                'and user motion together?',
                'Intelligent handover',
                [
                    'Beam optimization',
                    'Self-optimizing network operations',
                    'Functional split selection',
                ],
                'Those three inputs feed the handover decision, so the network can choose '
                'the best target satellite along an intelligent prediction path rather '
                'than reacting to one measurement.',
            ),
            (
                'The claim that resource optimization gets harder after deployment rests '
                'on which fact?',
                'The geometry keeps changing once the constellation is flying',
                [
                    'The constellation grows over time as more satellites are launched',
                    'The AI model degrades as its training data ages',
                    'Open interfaces cannot be updated after deployment',
                ],
                'A terrestrial network is planned once and then largely holds still. A '
                'constellation never holds still, so the optimisation problem is re-posed '
                'continuously rather than solved at planning time.',
            ),
        ],
    },
    {
        "topic": 'Federated learning for CSI feedback and beam management in LEO NTN',
        "source": 'Group 11 deck, slides 2 to 12',
        "questions": [
            (
                'What does channel state information tell the satellite, and why does it '
                'have to be reported?',
                'How the radio path changes the signal, which the satellite needs before '
                'it can aim a beam',
                [
                    'Which satellite the device intends to hand over to next',
                    "The device's GNSS position, so the beam can be pointed at it",
                    'How much buffer the device has left for incoming data',
                ],
                'CSI describes the channel in strength and timing. The satellite cannot '
                'observe the downlink channel itself, so the device has to measure it and '
                'report it back before precoding is possible.',
            ),
            (
                'In the conventional cycle the device measures, quantises, reports and '
                'the gNB precodes. What is the stated cost of that cycle?',
                'The report must be repeated often, and its cost grows with antennas, '
                'users and report rate',
                [
                    'Each report has to be acknowledged by the satellite before the next one',
                    'The device has to re-authenticate at the start of every reporting cycle',
                    'Quantisation forces the device to transmit at maximum power',
                ],
                'The report is small on its own but it is sent constantly, by every user, '
                'and it grows with the size of the antenna array. Multiplied out, it '
                'becomes the dominant uplink load.',
            ),
            (
                'Challenge one is that the report is stale on arrival. What makes it stale?',
                'The satellite moves at about 7.5 km/s, so the channel changes between '
                'measurement and use',
                [
                    'The report is queued behind higher-priority traffic in the uplink buffer',
                    'The codebook entry has to be looked up on the ground before use',
                    'The device only measures the channel once per connection',
                ],
                'The deck lays the timeline out as measure, send, arrive, applied. The '
                'interval over which the channel stays valid is shorter than the '
                'measure-to-use delay, so the report describes a channel that has gone.',
            ),
            (
                'Challenge two is that the data needed to fix the problem is private. Why '
                'is CSI private?',
                'A channel measurement is nearly unique to one place, so it identifies '
                'where a user is',
                [
                    'CSI reports include the subscriber identity in the header',
                    'The codebook index reveals which services the user is running',
                    'CSI is transmitted without ciphering on the uplink',
                ],
                'The deck shows a measured CSI grid being turned back into a position. '
                'The multipath signature of a location acts as a fingerprint, so '
                'collecting raw CSI centrally exposes subscriber location.',
            ),
            (
                'What does the learned encoder achieve, and what compression ratios are '
                'quoted?',
                'It compresses the CSI into a short codeword, at ratios from 1/16 to 1/64',
                [
                    'It removes the need for any uplink report at all',
                    'It encrypts the CSI so the aggregator cannot read it, at ratios from '
                    '1/2 to 1/8',
                    'It predicts the next CSI report, at ratios from 1/4 to 1/16',
                ],
                'An autoencoder is trained as a pair: an encoder on the device and a '
                'decoder at the gateway. Only the codeword crosses the link, which is '
                'where the 1/16 to 1/64 saving comes from.',
            ),
            (
                'Why must the encoder and the decoder be trained together as one pair?',
                'The decoder has to learn to invert the specific representation that the '
                'encoder produces',
                [
                    "Training them separately would exceed the device's memory budget",
                    '3GPP requires joint training for all air-interface models',
                    'Separate training would make the codeword longer than the raw report',
                ],
                'The codeword is not a standard format. It is whatever internal '
                'representation the encoder settles on, so only a decoder trained '
                'alongside it can reconstruct the channel from it.',
            ),
            (
                'What is the defining property of federated learning in this design?',
                'Model updates cross the link while the raw CSI never leaves the device',
                [
                    'Each device trains a completely separate model that is never combined',
                    'Training happens only on the satellite, using data it collects itself',
                    'The global model is broadcast but never updated after deployment',
                ],
                'Devices train locally on their own data and send only the resulting '
                'updates. The aggregator averages those updates, so it improves a shared '
                "model without ever holding anyone's raw measurements.",
            ),
            (
                'Which algorithms are named as what the aggregator runs?',
                'FedAvg, FedProx, SCAFFOLD and FedAdam',
                [
                    'DQN, DDPG, PPO and SAC',
                    'FedAvg, Q-learning, LSTM and SGD',
                    'AES, Kyber, Dilithium and SHA-256',
                ],
                'These are federated aggregation methods: FedAvg is the baseline, FedProx '
                'handles uneven data, SCAFFOLD corrects drift and FedAdam is an adaptive '
                'server. The other lists are reinforcement learning and cryptography.',
            ),
            (
                'Where does putting the aggregator on the satellite sit in the trade-off?',
                'It is the fastest option and it costs onboard power',
                [
                    'It is the slowest option but it uses no onboard power',
                    'It removes the need for secure aggregation',
                    'It stops the satellite from being visible for longer than a few minutes',
                ],
                'Ground-assisted aggregation makes every round cross the whole link. '
                'Aggregating on the satellite removes that trip, which is why it is '
                'fastest, and spends scarce payload power doing it.',
            ),
            (
                'Applying the same idea to beam management replaces an exhaustive sweep '
                'with what?',
                'A predictor fed by ephemeris and past beams that outputs the best beam '
                'directly',
                [
                    'A fixed beam schedule computed once at deployment',
                    'A request to the user device to nominate its preferred beam',
                    'A random beam selection that is corrected by the closed loop',
                ],
                'In the sweep the device measures every beam and reports the best. With a '
                'predictor it measures once to confirm the prediction, which is where the '
                'reporting overhead is saved.',
            ),
        ],
    },
    {
        "topic": 'AI-driven dynamic beam control for LEO 5G-NTN',
        "source": 'Group 12 deck, slides 3 to 14',
        "questions": [
            (
                'Why does a fixed beam plan go out of date within seconds in a LEO network?',
                'The cell itself moves at orbital speed, so the footprint has shifted',
                [
                    'The user devices move too fast for a fixed plan to track',
                    'The subcarrier spacing changes as the elevation angle changes',
                    'Beam weights are erased whenever the satellite passes into eclipse',
                ],
                'In a terrestrial network the cell is fixed and the users move. In LEO '
                'the reverse dominates: the beam footprint sweeps the ground at '
                'kilometres per second, so any plan set in advance is stale immediately.',
            ),
            (
                'The deck shows some cells at high demand and others at low or no demand '
                'under a uniform power allocation. What problem does this illustrate?',
                'Highly dynamic and uneven traffic wastes resources on empty cells',
                [
                    'Co-channel interference between adjacent beams',
                    'Timing misalignment between the SSB and the PRACH',
                    'Doppler spreading across the beam footprint',
                ],
                'Applying the same power to all cells means the busy cells are '
                'underserved while the empty ones consume payload resources that produce '
                'nothing.',
            ),
            (
                'In the scheduling conflict shown, two cells both need the beam during '
                'mandatory signalling. What is the consequence?',
                'One of the cells is left with a coverage hole',
                [
                    'Both cells receive the beam at half power',
                    'The satellite defers the signalling to the next orbit',
                    'The devices in both cells fall back to a terrestrial carrier',
                ],
                'SSB and PRACH occupancy is fixed by the standard, so the beam cannot '
                'serve both cells at that instant. Whichever cell loses the contest is '
                'not covered when it needs to be.',
            ),
            (
                'Under spatial-domain beam control, what is user-beam mapping for?',
                'Grouping users by location so co-channel interference across adjacent '
                'beams is minimised',
                [
                    'Assigning each user a unique preamble within the beam',
                    'Deciding which users are handed over to the next satellite',
                    'Matching each user to a network slice',
                ],
                'How users are grouped into beams decides which of them end up sharing a '
                'frequency with a neighbouring beam. Grouping by location keeps reuse '
                'distances sensible.',
            ),
            (
                'What is footprint shaping intended to compensate for?',
                'Changing slant range as the satellite moves from horizon to zenith',
                [
                    'Rain fade on the feeder link',
                    'The reversal of Doppler sign at the zenith',
                    'Uneven battery discharge across the payload',
                ],
                'A beam of fixed angular width covers a much larger and more distorted '
                'ground area near the horizon than overhead. Widening or narrowing it '
                'keeps the covered area consistent through the pass.',
            ),
            (
                'Beam hopping is a time-domain technique. What does it do?',
                'It time-multiplexes physical beams across several ground cells to serve '
                'sporadic demand',
                [
                    'It moves a beam to a new frequency when interference is detected',
                    'It switches a user between two satellites without a handover',
                    'It reshapes the beam as the slant range changes',
                ],
                'With fewer beams than cells, the way to serve them all is to visit each '
                'in turn. Cells with more traffic are visited more often, which is how '
                'sporadic demand is met efficiently.',
            ),
            (
                'What is signalling alignment concerned with?',
                'Reserving the 3GPP-defined slots for synchronisation and broadcast so '
                'they do not collide with data',
                [
                    "Aligning the beam boresight with the user's GNSS position",
                    'Matching the uplink and downlink frame timing at the gateway',
                    'Synchronising the phase of the elements in the antenna array',
                ],
                'Signals such as the SSB have to appear at defined times. The hopping '
                'schedule must work around those reservations rather than through them.',
            ),
            (
                'In the 3GPP AI execution models, what characterises Type 3?',
                'Separate training at two sides, with a training dataset shared between them',
                [
                    'Joint training at one side only',
                    'Joint training at two sides using forward activation and backward '
                    'gradient',
                    'Training performed entirely on the satellite payload',
                ],
                'Type 1 trains at one side. Type 2 trains jointly across both sides by '
                'exchanging activations and gradients. Type 3 keeps the training separate '
                'and shares a dataset instead.',
            ),
            (
                'Which limitation is stated as making a beam prediction error highly visible?',
                'An incorrect prediction cuts coverage completely and causes a visible outage',
                [
                    'A wrong prediction raises the collision rate on the RACH',
                    'A wrong prediction forces the satellite into a safe mode',
                    'A wrong prediction increases the reporting overhead on the uplink',
                ],
                'Beams are narrow and directional. Aiming one at the wrong place does not '
                'merely degrade service in that cell, it removes it, and the users there '
                'see a complete outage.',
            ),
            (
                'What does the conclusion identify as the central engineering trade-off '
                'of AI-driven beam control?',
                'Efficiency is bought with onboard computing power',
                [
                    'Coverage is bought with additional spectrum',
                    'Latency is bought with a longer cyclic prefix',
                    'Reliability is bought with a larger constellation',
                ],
                'Steering beams where capacity is actually needed raises efficiency, and '
                'the prediction that makes it possible has to run on a payload with a '
                'hard power and thermal budget.',
            ),
        ],
    },
    {
        "topic": 'GPS and Galileo',
        "source": 'Group 13 deck, slides 3 to 31',
        "questions": [
            (
                'A GNSS receiver needs a minimum of four satellites rather than three. '
                'What does the fourth one resolve?',
                "The receiver's own clock bias",
                [
                    'The ambiguity between two candidate points in space',
                    'The ionospheric delay along each path',
                    'The identity of the constellation being tracked',
                ],
                'Three ranges fix a point in three dimensions if the clocks agree. A '
                'consumer receiver has no atomic clock, so its offset is a fourth unknown '
                'and needs a fourth equation.',
            ),
            (
                'Why is a pseudorange called pseudo?',
                "It contains the receiver's time-synchronisation error, so it is not the "
                'true physical distance',
                [
                    'It is measured to a predicted satellite position rather than the '
                    'real one',
                    'It is derived from carrier phase rather than from the ranging code',
                    'It is an average over several satellites rather than a single '
                    'measurement',
                ],
                'The receiver converts travel time into distance using its own imperfect '
                'clock. That clock error appears in the result as an offset common to '
                'every satellite, which is what the fourth measurement removes.',
            ),
            (
                'A one microsecond clock error produces roughly what positioning error on '
                'the ground?',
                'About 300 metres',
                [
                    'About 3 metres',
                    'About 30 metres',
                    'About 3 kilometres',
                ],
                'Distance is the speed of light multiplied by time, and light travels '
                'about 300 metres in a microsecond. This is why the satellites carry '
                'atomic clocks accurate to nanoseconds.',
            ),
            (
                'How do GPS satellites share the same frequencies without interfering?',
                'Each transmits a unique pseudo-random noise code, so the receiver '
                'separates them by code',
                [
                    'Each transmits in a different time slot on a rotating schedule',
                    'Each is allocated a narrow sub-band within the L1 carrier',
                    'Each transmits only when it is above a set elevation angle',
                ],
                'This is code division multiple access. All the satellites occupy the '
                'same spectrum at once, and the receiver correlates against a known PRN '
                'code to pull out one satellite at a time.',
            ),
            (
                'Ephemeris and almanac data are both broadcast. What is the difference?',
                "Ephemeris gives one satellite's precise orbit and is valid about four "
                'hours; the almanac gives approximate data for all satellites',
                [
                    'Ephemeris gives the clock correction and the almanac gives the orbit',
                    'Ephemeris is encrypted for military users and the almanac is open',
                    'Ephemeris is broadcast by GPS and the almanac by Galileo',
                ],
                'The almanac is coarse and covers the whole constellation, which is what '
                'lets a receiver work out which satellites to look for. The ephemeris is '
                'precise, applies to the transmitting satellite and expires quickly.',
            ),
            (
                'Which pair of orbital figures correctly separates GPS from Galileo?',
                'GPS about 20,200 km in 6 planes; Galileo 23,222 km in 3 planes',
                [
                    'GPS 23,222 km in 3 planes; Galileo about 20,200 km in 6 planes',
                    'GPS about 20,200 km in 3 planes; Galileo 35,786 km in 6 planes',
                    'Both about 20,200 km, but GPS in 6 planes and Galileo in 12',
                ],
                'Galileo flies higher and uses fewer, more populated planes, with a '
                '24/3/1 Walker design. The altitude difference is also why the periods '
                'differ, about 12 hours against about 14 hours 5 minutes.',
            ),
            (
                'GPS L1 and Galileo E1 are both at 1575.42 MHz. What does that make possible?',
                'A single receiver chip can track both constellations',
                [
                    'The two systems can share one control segment',
                    'Galileo can correct GPS clock errors directly in orbit',
                    'The two systems must coordinate their transmissions in time',
                ],
                'Sharing the band and a compatible signal structure means one front end '
                'and one correlator bank serve both. That roughly doubles the satellites '
                'in view and lowers dilution of precision.',
            ),
            (
                'Which error source is described as amplifying all the others rather than '
                'adding its own delay?',
                'Geometric dilution of precision',
                [
                    'Ionospheric delay',
                    'Multipath',
                    'Receiver noise and hardware imperfection',
                ],
                'Dilution of precision is about satellite geometry. Poorly spread '
                'satellites make the position solution ill-conditioned, so whatever '
                'ranging errors exist are magnified in the result.',
            ),
            (
                'Which error source is largest, and what is its quoted range?',
                'Tropospheric delay, at about 2 to 25 metres',
                [
                    'Ionospheric delay, at about 1 to 2 metres',
                    'Multipath, at about 5 to 15 metres',
                    'Satellite clock and ephemeris error, at up to 1 metre',
                ],
                'The quoted figures are ionosphere 5 to 15 m, troposphere 2 to 25 m, '
                'multipath up to about 1 m, clock and ephemeris 1 to 2 m and receiver '
                'noise under 1 m. The troposphere has the widest top end, worst near the '
                'horizon.',
            ),
            (
                "Galileo's open service accuracy is quoted as better than GPS's "
                'traditional single-frequency figure. What is credited for the '
                'improvement?',
                'Dual and multi-frequency signals plus OSNMA authentication, reaching '
                'about 20 cm with HAS',
                [
                    'A larger constellation of 32 operational satellites',
                    'A lower orbit that shortens the signal path',
                    'An encrypted military code available to civilian users',
                ],
                'The table quotes about 5 m for GPS single-frequency against under 1 m '
                'dual-frequency for Galileo. Multi-frequency operation cancels '
                'ionospheric delay, which is the dominant correctable error.',
            ),
        ],
    },
    {
        "topic": 'Post-quantum cryptography for non-terrestrial networks',
        "source": 'Group 14 deck, slides 3 to 13',
        "questions": [
            (
                'Which algorithm is the specific threat to RSA and ECC, and what does it do?',
                "Shor's algorithm, which factors large primes efficiently on a quantum "
                'computer',
                [
                    "Grover's algorithm, which reverses a hash function directly",
                    "Shor's algorithm, which brute-forces a symmetric key in linear time",
                    "Grover's algorithm, which solves the discrete logarithm in constant time",
                ],
                'RSA and ECC rest on problems that are hard for classical computers. '
                "Shor's algorithm solves exactly those problems, which is why the "
                'public-key layer, not the symmetric layer, is the urgent one.',
            ),
            (
                'What is the harvest now, decrypt later threat?',
                'Traffic intercepted today is stored and decrypted once a quantum '
                'computer exists',
                [
                    'A quantum computer decrypts traffic in real time as it is transmitted',
                    'Keys are stolen now and reused against future sessions',
                    'Encrypted data is corrupted now so it cannot be recovered later',
                ],
                'It makes the threat present rather than future. Data with a long secrecy '
                'lifetime is already at risk, because the attacker only needs to record '
                'it now and wait.',
            ),
            (
                'Which two algorithms are named as the post-quantum replacements?',
                'CRYSTALS-Kyber and CRYSTALS-Dilithium',
                [
                    'RSA-4096 and ECC-521',
                    'AES-256 and SHA-256',
                    'IPsec and DTLS',
                ],
                'Kyber is the key encapsulation mechanism, standardised as NIST FIPS 203, '
                'and Dilithium is the signature scheme. The others in the list are either '
                'the vulnerable primitives or transport protocols.',
            ),
            (
                'Why is bandwidth overhead a bigger problem for PQC on a satellite link '
                'than on the ground?',
                'PQC keys and signatures are far larger than RSA or ECC, and satellite '
                'capacity is limited and expensive',
                [
                    'Satellite links cannot carry packets above a fixed maximum size',
                    'PQC requires the key to be retransmitted on every packet',
                    'Satellite links have no error correction, so larger keys corrupt '
                    'more often',
                ],
                'The size increase is the same everywhere. What differs is the cost of '
                'carrying it: on a satellite link every extra byte competes with revenue '
                'traffic on a scarce resource.',
            ),
            (
                'Why does propagation delay hurt PQC handshakes in particular?',
                'Multi-round-trip key exchanges multiply an already long round-trip time',
                [
                    'The keys expire before they reach the far end',
                    'The satellite cannot buffer a handshake for longer than one pass',
                    'Delay causes the signature timestamp to fall outside its validity window',
                ],
                'A handshake that needs several exchanges pays the round-trip cost once '
                'per exchange. On a link where one round trip is already long, that '
                'multiplication dominates setup and re-keying time.',
            ),
            (
                'What makes onboard compute a constraint for PQC specifically?',
                'Satellite payloads use radiation-hardened, lower-power processors on '
                'tight energy budgets',
                [
                    'Satellite processors cannot execute lattice arithmetic at all',
                    'Onboard memory is erased whenever the satellite passes through eclipse',
                    'Radiation-hardened processors cannot store private keys securely',
                ],
                'Radiation hardening trades performance for reliability, so a space '
                'processor is generations behind a ground server. PQC is more demanding '
                'than the ECC and RSA primitives it replaces.',
            ),
            (
                'Which resolution is proposed for migrating without abandoning existing '
                'security?',
                'Hybrid cryptographic handshakes',
                [
                    'Disabling encryption on the feeder link',
                    'Moving all key exchange to the ground segment',
                    'Replacing AES with a longer symmetric key',
                ],
                'A hybrid handshake runs a classical and a post-quantum exchange '
                'together, so the session stays secure if either one holds. That is what '
                'IETF RFC 9370 provides for in IKEv2.',
            ),
            (
                'Subscriber identity privacy, primary authentication and air-interface '
                'ciphering are described as protecting which link?',
                'The service link between the handset and the satellite',
                [
                    'The feeder link between the satellite and the ground station',
                    'The inter-satellite link within the constellation',
                    'The connection between the gateway and the 5G core',
                ],
                'Those three are the handset-facing mechanisms. The feeder link is '
                'protected instead by IPsec tunnels, DTLS for fast signalling and NDS/IP '
                'at the ground station.',
            ),
            (
                'Which mechanisms are named as protecting the path from the gateway to '
                'the core?',
                'Service-based architecture security, GTP-U encryption and cross-network '
                'integrity',
                [
                    'Subscriber identity privacy, primary authentication and '
                    'air-interface ciphering',
                    'IPsec tunnels, DTLS and NDS/IP border protection',
                    'Kyber key encapsulation, Dilithium signatures and AES-256',
                ],
                "Once traffic is on the ground it moves through the core's own "
                'service-based architecture. SBI security, GTP-U tunnel encryption and '
                'integrity stamps on system messages guard that segment.',
            ),
            (
                'What does the conclusion identify as the reason PQC adoption is '
                'essential for space networks?',
                '5G NTNs run on standard classical cryptography today, which quantum '
                'computing threatens',
                [
                    'Satellite links are already broken by existing classical attacks',
                    'Post-quantum algorithms are faster than RSA on space processors',
                    '3GPP has already mandated PQC in Release 17',
                ],
                'The argument is about exposure, not about current failure. The '
                'cryptography in use today is sound against classical attack and '
                'vulnerable to a quantum one, and satellites are hard to upgrade after '
                'launch.',
            ),
        ],
    },
    {
        "topic": 'Doppler shift estimation in 5G NR non-terrestrial networks',
        "source": 'Group 15 deck, slides 3 to 14',
        "questions": [
            (
                'For an S-band LEO satellite at 600 km, what is the quoted peak Doppler '
                'shift and where in the pass does the shift cross zero?',
                'Up to about plus or minus 48 kHz, crossing zero at the zenith',
                [
                    'Up to about plus or minus 48 kHz, crossing zero at the horizon',
                    'Up to about plus or minus 5 kHz, crossing zero at the zenith',
                    'Up to about plus or minus 500 kHz, crossing zero at the horizon',
                ],
                'The shift is largest approaching the horizon, where the satellite is '
                'closing fastest along the line of sight, and passes through zero '
                'overhead, where the radial component vanishes.',
            ),
            (
                'Why does a transparent architecture suffer a doubled Doppler impact?',
                'Both the service link and the feeder link are Doppler-affected',
                [
                    'The signal is transmitted twice, once by the satellite and once by '
                    'the gateway',
                    'The uplink and downlink Doppler shifts have the same sign and add',
                    'The bent-pipe repeater doubles the carrier frequency',
                ],
                'A regenerative payload demodulates on board, so Doppler is confined to '
                'the service link and the digital backhaul is clean. A transparent '
                'payload passes the signal through, so the two segments accumulate.',
            ),
            (
                'What does an uncompensated Doppler shift do to an OFDM signal?',
                'It destroys subcarrier orthogonality and causes inter-carrier interference',
                [
                    'It shortens the cyclic prefix below the delay spread',
                    'It inverts the constellation mapping on every subcarrier',
                    'It causes the frame timing to drift out of the transmission window',
                ],
                "OFDM works because each subcarrier peak sits on its neighbours' zero "
                'crossings. A frequency offset moves the peaks off those nulls, so each '
                'subcarrier leaks into the ones beside it.',
            ),
            (
                'On the downlink, one common signal is broadcast to all users in a beam. '
                'Why do they not all see the same Doppler shift?',
                'Each user has a different local elevation angle to the satellite',
                [
                    "Each user's receiver applies a different local oscillator correction",
                    'The satellite transmits at a different frequency to each user',
                    'Users at the beam edge receive a delayed copy of the signal',
                ],
                'Doppler depends on the radial component of velocity, which depends on '
                'where the user sits in the beam. The deck shows users at plus 40 kHz, 0 '
                'and minus 40 kHz within one footprint.',
            ),
            (
                'What system assumption does the 3GPP Release 17 baseline make?',
                'Every NTN user device carries an active GNSS receiver',
                [
                    'Every NTN user device has a stable atomic reference oscillator',
                    'The satellite payload is always regenerative',
                    'The network broadcasts a single common Doppler value per beam',
                ],
                'The Release 17 workflow is ephemeris broadcast, UE self-positioning, '
                'Doppler calculation, uplink pre-compensation. Every step after the first '
                'depends on the device knowing its own position from GNSS.',
            ),
            (
                'Which of the following is given as a reason GNSS-assisted methods fail '
                'in practice?',
                'GNSS signals at about minus 130 dBm fall over in urban canyons, indoors '
                'and under foliage',
                [
                    'GNSS satellites and NTN satellites use incompatible frequency bands',
                    'GNSS ephemeris cannot be broadcast over an NTN downlink',
                    'GNSS position fixes are too coarse to compute a Doppler shift',
                ],
                'The four failure reasons are environmental vulnerability, susceptibility '
                'to jamming and spoofing, low-cost IoT devices lacking GNSS chipsets, and '
                'oscillator error mixing with true Doppler.',
            ),
            (
                'Total Doppler is split as an integer subcarrier shift plus a fractional '
                'shift. What bounds the fractional part?',
                'Its magnitude is less than 0.5 of the subcarrier spacing',
                [
                    'Its magnitude is less than one full subcarrier spacing',
                    'Its magnitude is less than 0.5 of the carrier frequency',
                    'It is bounded by the length of the cyclic prefix',
                ],
                'Beyond half a subcarrier the offset is better described as the next '
                'integer shift. Splitting the problem this way lets a coarse method find '
                'the integer and a fine method find the remainder.',
            ),
            (
                'How is the fractional Doppler recovered from the cyclic prefix?',
                "The cyclic prefix repeats the symbol's last samples, so a "
                'complex-conjugate product gives a phase angle',
                [
                    'The cyclic prefix carries a pilot tone at a known frequency',
                    'The cyclic prefix is correlated against the PSS and SSS sequences',
                    'The cyclic prefix length is measured and compared with the nominal value',
                ],
                'Because the prefix is an exact copy of the symbol tail, multiplying the '
                'signal by a delayed conjugate of itself yields a phase difference that '
                'is proportional to the frequency offset.',
            ),
            (
                'How is the integer Doppler shift recovered?',
                'By frequency-domain cross-correlation of PSS and SSS over a sliding '
                'frequency search grid',
                [
                    'By reading the value from the ephemeris broadcast in SIB19',
                    'By measuring the phase rotation across the cyclic prefix',
                    'By comparing the arrival time of two consecutive frames',
                ],
                'The synchronisation signals are known sequences, so searching across '
                'candidate frequency offsets and taking the strongest correlation '
                'identifies which whole subcarrier the signal has moved by.',
            ),
            (
                'In the trade-off table, which method has no GNSS dependency and the '
                'lowest pilot overhead?',
                'Cross-correlation on the cyclic prefix, which is already being transmitted',
                [
                    'The Release 17 GNSS method, which needs a fairly minimal pilot overhead',
                    'Multi-frequency pilots, which are carried on the DM-RS resources',
                    'Kalman filter tracking, which needs no GNSS seed whatsoever',
                ],
                'The cyclic prefix is already in every symbol, so exploiting it adds '
                'nothing to the transmission. Multi-frequency pilots are also GNSS-free '
                'but spend DM-RS resources, and EKF tracking may take an initial GNSS '
                'seed.',
            ),
        ],
    },
    {
        "topic": 'Network slicing in non-terrestrial networks',
        "source": 'Group 16 deck, slides 3 to 10',
        "questions": [
            (
                'What is network slicing?',
                'Several virtual networks over one shared physical network, tuned end to end',
                [
                    'Dividing the satellite footprint into a set of smaller geographic cells',
                    'Splitting the available frequency band into fixed sub-bands per operator',
                    'Separating the control plane from the user plane within the core network',
                ],
                'The physical resources, that is spectrum, payload, transport and core '
                'compute, stay shared. What is divided is the logical treatment, so each '
                'slice behaves like a network of its own.',
            ),
            (
                'Which slice types match which service profiles?',
                'SST 1 eMBB wide bandwidth, SST 2 URLLC priority queueing, SST 3 mMTC '
                'small packets',
                [
                    'SST 1 URLLC low latency, SST 2 mMTC tiny packets, SST 3 eMBB wide '
                    'bandwidth pipe',
                    'SST 1 mMTC small packets, SST 2 eMBB wide bandwidth, SST 3 URLLC low '
                    'latency',
                    'SST 1 eMBB wide bandwidth, SST 2 mMTC small packets, SST 3 URLLC low '
                    'latency',
                ],
                'eMBB is the wide, delay-tolerant pipe for video and broadband. URLLC '
                'needs short queues and guaranteed priority. mMTC is store-and-forward '
                'for huge numbers of tiny IoT packets.',
            ),
            (
                'Round-trip delay is quoted as 25.8 ms for a 600 km LEO and 541 ms for '
                'GEO. What does that break?',
                'A one millisecond low-latency guarantee cannot be honoured at all',
                [
                    'The broadband slice is unable to reach its stated throughput target',
                    'The machine-type slice cannot support enough simultaneous devices',
                    'The slice identifier cannot be carried within the packet header',
                ],
                'URLLC is defined by a latency bound of about 1 ms on a terrestrial cell. '
                'Physics puts the satellite round trip an order of magnitude or more '
                'above that before any processing is added.',
            ),
            (
                'Why is hard isolation between slices not available on a satellite payload?',
                'One payload and one spectrum pool are shared, so isolation stays logical',
                [
                    'Standards forbid physical isolation from being used in '
                    'non-terrestrial systems',
                    'The slice identifier is stripped as traffic crosses the feeder link',
                    'Satellites are unable to run virtualisation software while in orbit',
                ],
                'On the ground a tenant can be given dedicated hardware. A satellite '
                'cannot carry duplicate payloads for each slice, so separation is '
                'enforced in software over shared resources.',
            ),
            (
                'In what sense does an NTN slice sit on a cell that will not stay still?',
                'A beam is visible for minutes, so the slice re-anchors to a new satellite',
                [
                    'User devices move between the cells faster than a slice can be '
                    'reconfigured',
                    'The slice identifier changes each time the satellite switches its beam',
                    'The cell footprint shrinks as the satellite approaches the horizon line',
                ],
                'In terrestrial 5G a slice is pinned to a fixed cell and a fixed fibre '
                'path. In NTN the radio cell moves out of view within minutes, so the '
                'anchoring has to be recomputed continuously.',
            ),
            (
                'What does it mean that the topology re-wires itself?',
                'Feeder switchover and inter-satellite re-routing change the path mid-session',
                [
                    'The constellation gains and loses satellites while it is in operation',
                    'The user device keeps switching between terrestrial and satellite '
                    'access types',
                    'Core network functions migrate between one data centre and another',
                ],
                "Both the radio cell and the transport path are in motion. A slice's "
                'transport segment therefore keeps changing underneath it, which is not '
                'something terrestrial slicing has to handle.',
            ),
            (
                'In the proposed management chain, which function handles the beam and '
                'the scheduler?',
                'The radio subnet manager, covering the beam and the scheduler',
                [
                    'The customer-facing manager, which captures the customer intent',
                    'The end-to-end slice manager, which spans the whole network',
                    'The core and transport subnet manager, covering both of those',
                ],
                'The chain runs CSMF for customer intent, NSMF for the end-to-end slice, '
                'then two subnet managers: one for the radio segment including beam and '
                'scheduler, and one for core and transport.',
            ),
            (
                'The orchestration is described as orbit-aware. What does that mean?',
                'Policy follows ephemeris and handover timing, not a static cell plan',
                [
                    'Slices are allocated according to the altitude of the serving satellite',
                    'Each orbital plane in the constellation is given its own dedicated slice',
                    'The orchestrator itself runs aboard the satellite rather than on ground',
                ],
                'Because the cell and the transport path move predictably, the '
                "orchestrator can plan against the constellation's known motion. The "
                'summary puts it as planning from ephemeris, not from a static cell plan.',
            ),
            (
                'Which cost is paired with the benefit of strict isolation between tenants?',
                'Capacity fenced off for an idle slice is wasted on a limited payload',
                [
                    'Slice headers and per-slice buffering inflate packets on a long link',
                    'Agreements must be recomputed at each handover and feeder switchover',
                    'A regenerative core function per slice makes heat the platform '
                    'cannot shed',
                ],
                'Each benefit in the deck has its own cost. Isolation reserves capacity '
                'whether or not it is used, and on a payload with a hard power budget '
                'idle reserved capacity is pure loss.',
            ),
            (
                'The summary states that every gain has a price. How is that price '
                'characterised?',
                'Isolation costs capacity and signalling on a power and delay limited link',
                [
                    'Slicing requires a larger constellation to deliver equivalent coverage',
                    'Slicing pushes user traffic through the ground core rather than onboard',
                    'Slicing rules out the use of regenerative payloads across the '
                    'constellation',
                ],
                'The deck frames slicing in NTN as a budgeting exercise. The idea is the '
                'same as on the ground, but the physics is harder and every logical '
                'guarantee is drawn from a scarce physical budget.',
            ),
        ],
    },
]
