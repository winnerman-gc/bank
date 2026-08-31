# -*- coding: utf-8 -*-
"""Rebalanced option sets for deck_study_c.py, questions 81 to 120.

Same discipline as options_study_a.py and options_study_b.py: a narrow length
band across all four options, the correct one deliberately not the longest in
most questions, and no absolutes or hedges confined to one side.

REPLACEMENTS[question_number] = (correct, [d1, d2, d3])
"""

REPLACEMENTS = {

    # ---- Deck 17: eRACH ----
    81: ("It cannot choose which base station to use, yet the best choice keeps changing",
         ["It is unable to operate above a certain limit on the permitted transmit power level",
          "It requires the number of contending devices to be known ahead of deployment",
          "It depends on a wired connection running between neighbouring base stations"]),

    82: ("Terminals never talk to each other, yet independent learning produces order",
         ["The network broadcasts an access schedule that the terminals are to then follow",
          "Terminals negotiate directly with their neighbours before they transmit",
          "Coordination appears only once a central controller has been introduced"]),

    83: ("Applications tolerate collisions and delay differently, so one setting cannot suit all",
         ["Conformance rules require the resulting collision rate to remain configurable",
          "The satellite payload is unable to support any single fixed access policy",
          "Training would fail to converge without an adjustable parameter to tune"]),

    84: ("Predicted position is one of only two inputs, so error corrupts the whole view",
         ["The terminal must first report its own position to the serving satellite",
          "Positioning error changes which preamble the terminal ends up selecting",
          "The satellite cannot compute any reward without first having an accurate position"]),

    85: ("A protocol whose design assumptions fail gives way to one that adapts instead",
         ["Satellite networks need far more preambles than any terrestrial pool provides",
          "Central coordination is preferable to distributed decision-making here",
          "Machine learning is required by the specification for satellite access"]),

    # ---- Deck 18: RIS ----
    86: ("A satellite needs a clear view, and an obstruction removes the link outright",
         ["The satellite beam is far too wide to serve individual users at all efficiently",
          "The satellite is unable to form enough beams for every user within its cell",
          "Atmospheric absorption removes the link entirely at the higher frequencies"]),

    87: ("Each element sets its own phase, so reflections reinforce in one direction",
         ["Each element amplifies the incident signal before it is re-radiated back outward",
          "The surface rotates mechanically so as to face the intended receiver below",
          "The surface converts the signal to another frequency before reflecting it"]),

    88: ("The two hops multiply rather than add, so the combined loss is severe",
         ["The surface must exceed the wavelength of the incident signal to reflect it",
          "A large surface is needed to dissipate the heat that its controller makes",
          "Regulations set a minimum aperture for anything reflecting satellite signals"]),

    89: ("It measures nothing itself, so the channel must be estimated some other way",
         ["It cannot be assigned an identity of its own within the serving network",
          "It cannot confirm that its reflection actually reached the intended user",
          "It cannot be reconfigured at all once it has been installed onto a building wall"]),

    90: ("It supplies a second distinct path, so another spatial stream becomes possible",
         ["It doubles the bandwidth that is available along the existing direct path",
          "It lets the satellite reuse the same frequency across two adjacent beams at once",
          "It compresses the data being carried before it is reflected onward to a user"]),

    # ---- Deck 21: uplink synchronisation without GNSS ----
    91: ("Devices sit at different distances, so uncorrected arrivals would overlap",
         ["The uplink is carried on a different carrier frequency from the downlink",
          "The receiver processes uplink and downlink in physically separate hardware",
          "Regulations require a guard period to be left between adjacent transmissions"]),

    92: ("It computes from position and orbit, so without a fix there is nothing to use",
         ["The navigation receiver also supplies the frequency reference used by the device",
          "The satellite cannot broadcast its orbit without a navigation-derived stamp",
          "The device is unable to decode the downlink without navigation-derived timing"]),

    93: ("Motion changes the delay, so tracking arrival drift reveals it without position",
         ["The satellite broadcasts its own clock drift for the device to then mirror locally",
          "Oscillator drift within the device is proportional to the propagation delay",
          "Arrival-time drift is removed entirely by lengthening the guard interval"]),

    94: ("It models a smoothly evolving quantity, refining it and predicting through gaps",
         ["It requires no further measurements at all once it has been initialised",
          "It guarantees the estimate will converge within a single transmission slot",
          "It removes the need for the network to send out any corrections whatsoever at all"]),

    95: ("One value suits one place, so its error grows across a wide footprint",
         ["It can only be transmitted once during each pass of the serving satellite",
          "It requires that every device already hold a valid navigation position fix",
          "It cannot be updated at all as the satellite moves along its orbital track"]),

    # ---- Deck 22: deep reinforcement learning for SAGIN ----
    96: ("Three tiers are managed as one system rather than as separate networks",
         ["Every satellite in the constellation also carries an Earth observation payload",
          "Ground stations are replaced entirely by a layer of aerial relay platforms",
          "Each of the three tiers operates within its own separate frequency allocation"]),

    97: ("Conditions shift and choices constrain later ones, unlike a fixed problem",
         ["Conventional optimisation is unable to handle more than two network tiers",
          "Reinforcement learning needs far less training data than conventional methods",
          "Conventional optimisation cannot be implemented on satellite-grade hardware"]),

    98: ("Some choices pick from a list and others set a value, needing different methods",
         ["Some of them run aboard the satellite while the others need ground-based hardware",
          "Some are standardised by 3GPP while the remainder are vendor extensions",
          "Some are able to work with only one tier of the network at any given time"]),

    99: ("Platforms differ in what they allow varying, so the decisions differ too",
         ["Each tier is operated by a separate organisation with its own set of policies",
          "Each tier makes use of a radio access technology incompatible with the others",
          "Each tier serves a distinct set of users that does not overlap with the rest"]),

    100: ("It is large, will not hold still, and demands decisions faster than it learns",
          ["Training data cannot be gathered from any networks that are already operational",
           "The reward function cannot be defined at all for a multi-tier architecture",
           "Reinforcement learning is unable to handle continuous action spaces well"]),

    # ---- Deck 23: HARQ ----
    101: ("The failed copy is kept and combined, so both attempts contribute to decoding",
          ["It retransmits automatically without ever waiting for any acknowledgement at all",
           "It corrects every error outright without ever needing a retransmission",
           "It applies error correction only after a first retransmission has failed"]),

    102: ("Every process waits for its acknowledgement, so none is left free for new data",
          ["The receiver buffer overflows long before any acknowledgement is able to arrive back",
           "Acknowledgements expire and are discarded whenever they are delayed too long",
           "The receiver cannot decode a packet that arrives after a long enough delay"]),

    103: ("Hidden waiting grows only with the count, and the round trip can exceed it",
          ["Additional processes cannot be addressed by the existing signalling format",
           "Additional processes raise the rate of collision on the shared uplink channel",
           "Additional processes require a correspondingly longer cyclic prefix per symbol"]),

    104: ("It turns a delay problem into a capacity one, spending redundancy in advance",
          ["Errors become impossible once the acknowledgement mechanism is switched off",
           "The satellite keeps a copy and retransmits it without ever being asked to",
           "The receiver corrects every error using the soft information it has stored"]),

    105: ("A processing payload ends the link aboard, so the loop covers one hop only",
          ["A processing payload removes the need for any retransmission whatsoever",
           "A repeating payload retransmits from its own buffer without the ground",
           "A processing payload moves recovery up to a higher layer automatically"]),

    # ---- Deck 24: network digital twinning ----
    106: ("It is continuously updated from the real system, so it tracks the current state",
          ["It runs faster than real time, whereas a simulation runs slower than real time",
           "It models only the physical layer, whereas a simulation covers every layer",
           "It is built after deployment, whereas a simulation is built well before deployment"]),

    107: ("Links form and break continuously, so the network is never what was last seen",
          ["Its satellites make use of radio interfaces incompatible with one another",
           "Its ground stations are too few in number to monitor every satellite flown",
           "Its orbits are unpredictable and so cannot be computed reliably in advance"]),

    108: ("Several futures are simulated and compared before one is committed to",
          ["It responds to a change in the network faster than a control loop manages",
           "It removes the need to gather any data from the real network at all",
           "It guarantees that whichever decision is chosen will be the optimal one"]),

    109: ("Its outputs drive the real network, so a wrong model gives confident errors",
          ["An inaccurate model consumes more bandwidth in order to stay synchronised",
           "An inaccurate model cannot be migrated from one satellite to another one",
           "An inaccurate model prevents the twin from being encrypted end to end"]),

    110: ("Local decisions need detail and speed, global ones need breadth instead",
          ["A single model would exceed the storage available at any one ground station",
           "Hierarchy is required before the twin can be encrypted from end to end",
           "Each orbital plane has to be modelled by a separate operating organisation"]),

    # ---- Predictive handover (unnumbered deck) ----
    111: ("On the ground the user moves past fixed towers; in orbit the cell moves",
          ["In orbit the user must select the serving satellite manually each session",
           "In orbit handovers occur only when the user is themselves actually moving",
           "In orbit the satellite performs the handover without informing the device"]),

    112: ("The decision returns after the satellite has already moved a long way",
          ["Satellite receivers are unable to measure signal strength with any accuracy",
           "Terrestrial networks make no use of signal strength triggers of any kind",
           "The satellite cannot store the measurement report while it is in motion"]),

    113: ("It arranges targets and conditions ahead, but the conditions stay fixed rules",
          ["It removes the need for the device to measure, but adds signalling instead",
           "It lets the device choose its target, but only among terrestrial cells",
           "It removes handover failures outright, but raises the interruption time"]),

    114: ("Choosing now affects later options, so the best immediate pick may not win",
          ["Because several devices have to be handed over in a strictly fixed sequence",
           "Because each individual handover requires several messages to be completed",
           "Because the device must reselect a cell before it is able to hand over"]),

    115: ("Coordinating many devices balances load that per-connection choices create",
          ["It allows handovers to be carried out without any signalling being needed",
           "It removes the need for orbital prediction to be performed at all",
           "It guarantees that not one device will experience any interruption"]),

    # ---- Trajectory optimization (unnumbered deck) ----
    116: ("Its coverage stops responding to where users are, so mobility buys nothing",
          ["A fixed route causes the platform to use more energy than hovering would",
           "A fixed route prevents the platform from forming any directional beams",
           "A fixed route places the platform outside the licensed airspace corridor"]),

    117: ("Where it goes now decides what is reachable later, so the horizon is long",
          ["It requires no training data of any kind before it can be deployed",
           "It yields one optimal trajectory that never has to be revised again",
           "It runs wholly on the ground, so the platform carries no computation"]),

    118: ("Coverage against energy, delay and interference, which oppose each other",
          ["Coverage against altitude, which is capped by aviation regulation",
           "Coverage against the number of platforms that have been deployed",
           "Coverage against the bandwidth that is allocated to each single user"]),

    119: ("Altitude fixes coverage, endurance and latency together for each tier",
          ["Each altitude band is allocated a different frequency by the regulator",
           "Each platform type uses a radio access technology unlike the others",
           "Each platform type is operated by an entirely different organisation"]),

    120: ("Airspace regulation, which constrains flight whatever the capability",
          ["Battery capacity, which bounds how long a platform is able to stay aloft",
           "Computational complexity, which bounds how quickly decisions are made",
           "Weather, which affects both radio propagation and the ability to fly"]),
}
