# -*- coding: utf-8 -*-
"""Rebalanced option sets for deck_study_b.py, questions 41 to 80.

Same discipline as options_study_a.py: a narrow length band across all four
options, the correct one deliberately not the longest in most questions, and
no absolutes or hedges confined to one side.

REPLACEMENTS[question_number] = (correct, [d1, d2, d3])
"""

REPLACEMENTS = {

    # ---- Deck 9: ISAC ----
    41: ("One waveform, one front end and one band carry both functions at the same time",
         ["Sensing results are carried as ordinary payload data across the communication link",
          "The radar function operates only during intervals when the data link sits idle",
          "The two payloads share a power supply and a common thermal control subsystem"]),

    42: ("It holds position relative to the ground, so almost no radial motion is present",
         ["Its transmit frequency is too high for any Doppler processing chain to resolve it",
          "Its returned signal is far too weak by the time it reaches the ground station",
          "Its orbit is published well in advance, so measuring it serves no useful purpose"]),

    43: ("Several viewing angles on one target, resolving geometry a single view leaves open",
         ["A stronger echo, since the reflected energy is collected at several places at once",
          "Freedom from needing any prior knowledge of the waveform that was originally transmitted",
          "Immunity to the Doppler shift imposed on the signal along its reflected path"]),

    44: ("Raw returns must go to the ground, so the answer comes back a round trip later",
         ["Limited processing obliges the receiver to integrate over a much longer dwell time",
          "Limited processing requires the waveform itself to be transmitted more slowly",
          "Limited processing means echoes are stored until the next pass over a gateway"]),

    45: ("Better spectral efficiency, since no separate allocation is held for sensing",
         ["The ability to track passive objects that transmit nothing of their own accord",
          "The ability to map a changing environment in real time and predict outages",
          "The ability to hold coverage when the ground infrastructure has been destroyed"]),

    # ---- Deck 10: AI-native Open RAN ----
    46: ("The decisions differ in how quickly they must be made, so each gets its own rate",
         ["One of them governs the uplink direction and the other governs the downlink",
          "One of them is standardised while the other remains a vendor-specific extension",
          "One of them runs on the ground while the other one has to run aboard the satellite"]),

    47: ("Standard interfaces let units come from different vendors and admit outside software",
         ["Processing moves entirely into the radio unit, which reduces backhaul demand",
          "The core network becomes unnecessary, since the units interconnect directly",
          "Radio functions are replaced by satellite functions across the whole network"]),

    48: ("The inner one improves the network; the outer one sells access to AI over it",
         ["The inner one runs on the ground while the outer one runs aboard the satellite",
          "The inner one is real-time while the outer one operates on a slower control loop",
          "The inner one handles the user plane while the outer one handles control signalling"]),

    49: ("The splits assume a link of fixed, known length, which orbital motion violates",
         ["Open interfaces have no field in which orbital ephemeris data could be carried",
          "Cloud infrastructure of this kind cannot be deployed aboard a moving platform",
          "Control applications must be recompiled separately for every orbital plane flown"]),

    50: ("It weighs several factors at once, where a threshold watches a single variable",
         ["It carries out the handover itself far faster than any threshold rule manages to do",
          "It removes the need for the device to report any measurements to the network",
          "It guarantees that no handover attempt will fail once the decision is taken"]),

    # ---- Deck 11: federated learning for CSI ----
    51: ("Only the receiver observes the path, so the transmitter must be told what arrived",
         ["The satellite lacks the processing capability needed to measure its own downlink channel",
          "Conformance rules oblige the device to confirm the channel before transmitting",
          "The satellite measures the uplink instead and infers the downlink from that"]),

    52: ("The channel it describes has already changed, so its content is wrong on arrival",
         ["It is queued behind higher-priority traffic and therefore arrives out of order",
          "It must be decoded on the ground before the network is able to apply it at all usefully",
          "The device measures the channel only once, when it first attaches to the cell"]),

    53: ("A path is shaped by its surroundings, so the pattern identifies a location",
         ["Reports carry the subscriber identity in a header that is transmitted in clear",
          "Reports are transmitted without any encryption being applied to protect them",
          "Reports disclose which applications the subscriber happens to be running"]),

    54: ("Training happens on the device and only the learned update is ever sent onward",
         ["Each device trains a wholly separate model that is never combined with others",
          "Training is carried out aboard the satellite on measurements it gathers itself",
          "A single global model is distributed once and is never revised after deployment"]),

    55: ("Geometry and past beams predict the choice, so one measurement confirms it",
         ["The device chooses its own beam and does not inform the network of the choice",
          "The beam is fixed when the connection is set up and is never changed afterwards",
          "Every beam is used at once and whichever gives the best result is then retained"]),

    # ---- Deck 12: AI-driven beam control ----
    56: ("The cell moves at orbital speed, so the ground it covers has already shifted",
         ["User devices move faster than any plan can realistically be recomputed for them",
          "Subcarrier spacing changes as the elevation angle to the satellite changes",
          "Beam weights are lost each time the satellite passes into the Earth's shadow"]),

    57: ("Some signals must appear at fixed times, so the schedule works around them",
         ["Signalling consumes considerably more power than an equivalent data transmission",
          "Signalling has to be carried on a separate carrier frequency from user traffic",
          "Signalling can only be transmitted while the satellite is close to its zenith"]),

    58: ("There are fewer beams than cells, so covering them all means visiting in turn",
         ["Continuous illumination of a single cell would exceed the permitted emission limits",
          "Beams must be rested at intervals so that amplifier heating can be managed",
          "Devices are able to receive only during discrete intervals that are scheduled"]),

    59: ("Some arrangements exchange results repeatedly, which a long link makes costly",
         ["Models trained across two sides cannot be standardised by any existing body",
          "Only the satellite side holds enough gathered data for training to be possible",
          "Two-sided training requires that both ends run identical processing hardware"]),

    60: ("Beams are narrow, so aiming one wrongly removes service rather than degrading it",
         ["A wrong prediction corrupts the model and so degrades all of the later decisions too",
          "A wrong prediction causes the satellite to lose synchronisation with the ground",
          "A wrong prediction obliges every device in the cell to re-acquire the carrier"]),

    # ---- Deck 13: GPS and Galileo ----
    61: ("The receiver clock offset is a fourth unknown and needs a fourth measurement",
         ["The fourth resolves an ambiguity between two points that three spheres leave open",
          "The fourth supplies a redundant measurement by which satellite faults are detected",
          "The fourth carries the ionospheric correction that the other three cannot supply"]),

    62: ("Distance is time multiplied by the speed of light, so tiny errors become large",
         ["The satellites must stay synchronised with each other so their signals do not collide",
          "The receiver must predict when each satellite will next become visible to it",
          "The navigation message remains valid only for a strictly limited period"]),

    63: ("One receiver tracks both, nearly doubling satellites and improving the geometry",
         ["The two systems are able to share a single ground control infrastructure between them",
          "One system corrects the clock errors of the other directly while in orbit",
          "The two systems must coordinate their transmissions so as not to interfere"]),

    64: ("Dilution of precision, which adds nothing of its own but magnifies the rest",
         ["Multipath, which arises near the receiver rather than out in the constellation",
          "Ionospheric delay, which varies with the time of day and with the latitude",
          "Receiver noise, which depends on hardware quality rather than the environment"]),

    65: ("Each compares an observed position with surveyed truth and shares the difference",
         ["Each rebroadcasts an amplified copy of the original constellation signal",
          "Each depends on carrier-phase measurements rather than on code measurements",
          "Each requires a geostationary satellite through which corrections are relayed"]),

    # ---- Deck 14: post-quantum cryptography ----
    66: ("Public-key exchange and signatures, whose hard problems a quantum machine solves",
         ["Symmetric encryption, since a quantum machine tests every key simultaneously",
          "Hash functions, since a quantum machine is able to invert them directly",
          "The physical layer, since a quantum machine can demodulate any waveform sent"]),

    67: ("Traffic recorded today is decrypted later, so long-lived secrets are exposed now",
         ["Quantum machines already break the key lengths that are currently deployed",
          "The algorithms in question have been withdrawn from the relevant standards",
          "Satellites already in orbit are using algorithms that are known to be broken"]),

    68: ("Keys and signatures grow, and satellite capacity is scarce and costly to spend",
         ["Satellite links impose a hard maximum packet size that larger keys will exceed",
          "The key must be retransmitted alongside every packet sent over a satellite link",
          "Satellite links carry no error correction, so larger keys are corrupted often"]),

    69: ("The session survives if either scheme holds, covering both kinds of failure",
         ["It halves the computational cost compared with running either one of them alone",
          "It allows older equipment to connect without any modification being needed",
          "It is mandated by regulation for the duration of the transitional period"]),

    70: ("Service lives are long and upgrading in orbit is impractical once launched",
         ["Space systems are not permitted to receive any software updates while in orbit",
          "Radiation effects prevent more than one algorithm being stored at any time",
          "International agreement fixes which algorithms a given satellite may use"]),

    # ---- Deck 15: Doppler shift estimation ----
    71: ("Only motion along the line of sight counts, and that peaks low and vanishes overhead",
         ["Atmospheric refraction is strongest near the horizon and is absent overhead",
          "The satellite travels fastest near the horizon and slowest at its zenith point",
          "Path loss is greatest near the horizon, and that broadens the received spectrum"]),

    72: ("Subcarriers separate only while each peak sits on its neighbours' nulls",
         ["The offset shortens the cyclic prefix below the delay spread of the channel",
          "The offset inverts the constellation mapping applied on every subcarrier",
          "The offset makes frame timing drift outside the permitted transmission window"]),

    73: ("Every later step needs the position, so losing the fix denies access entirely",
         ["Navigation receivers cannot operate on the frequencies that NTN services use",
          "Navigation signals cannot be received at the same time as the device transmits",
          "Navigation receivers need a subscription that not every device actually holds"]),

    74: ("The two leave different signatures, so each needs its own kind of measurement",
         ["One part affects the uplink direction while the other part affects the downlink",
          "Conformance rules require the two components to be reported to the network",
          "Only the fractional part varies as the satellite moves along its orbital path"]),

    75: ("It follows an underlying trajectory, so the estimate survives brief interruptions",
         ["It requires no reference signals of any kind once it has been initialised",
          "It removes the need for any initial position information to be supplied",
          "It removes the offset outright rather than merely producing an estimate of it"]),

    # ---- Deck 16: network slicing ----
    76: ("How traffic is treated, so each slice behaves as though it had its own network",
         ["The satellite footprint, into a set of smaller geographic service areas",
          "The frequency band, into fixed sub-bands that are allocated to each operator",
          "The core network, into separate control-plane and user-plane installations"]),

    77: ("Low-latency service, whose defining bound is smaller than the round trip itself",
         ["Enhanced broadband, because its throughput target cannot be reached from orbit at all",
          "Machine-type communication, because too many devices must be supported at once",
          "None of them, because slicing isolates a service from the underlying delay"]),

    78: ("One payload and one spectrum pool serve every slice, so hardware cannot be split",
         ["Standards forbid physical separation from being used in non-terrestrial systems",
          "Slice identifiers are stripped from traffic as it crosses the gateway link",
          "Satellites are unable to run virtualisation software while they are in orbit"]),

    79: ("Reserved capacity is withheld whether used or not, on a power-limited payload",
         ["An idle slice continues to draw transmit power at its full allocated rate regardless",
          "Capacity once reserved to a slice cannot be released back for other traffic",
          "An idle slice generates signalling traffic in proportion to its reserved size"]),

    80: ("Policy is planned from predicted motion rather than from a fixed cell plan",
         ["Slices are assigned according to the orbital altitude of the serving satellite",
          "Each orbital plane in the constellation is allocated a dedicated slice of its own",
          "The orchestration function itself runs aboard the satellite rather than on ground"]),
}
