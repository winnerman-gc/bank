# -*- coding: utf-8 -*-
"""Rebalanced option sets for deck_study_a.py, questions 1 to 40.

Authored so that the correct option cannot be picked on shape alone:

  - all four options sit within a narrow length band
  - the correct option is deliberately NOT the longest in most questions
  - absolute words (all, always, never, only) are not confined to distractors
  - hedges (may, typically, generally) are not confined to the correct option

REPLACEMENTS[question_number] = (correct, [d1, d2, d3])
"""

REPLACEMENTS = {

    # ---- Deck 1: timing advance and frequency offset compensation ----
    1: ("Distance creates a timing error and velocity a frequency error, needing separate fixes",
        ["One correction serves the uplink while an independent one serves the downlink path",
         "The device applies one and the satellite applies the other, dividing the processing load",
         "One compensates the service link and the other compensates atmospheric absorption"]),

    2: ("Orbital motion is deterministic, so the geometry follows from published ephemeris",
        ["The satellite emits a pilot tone that the device measures to derive its own correction",
         "The network broadcasts a single correction value that holds across the entire beam",
         "The device assumes a worst-case delay and corrects for that fixed amount instead"]),

    3: ("Prediction inherits any error in its inputs, so a residual remains and must be measured",
        ["The closed loop supersedes the open loop once the first connection is established",
         "The open loop covers the downlink only, so the uplink must be corrected by measurement alone",
         "Conformance rules require every applied correction to be confirmed by the network"]),

    4: ("A transparent payload crosses both moving segments, so their shifts accumulate",
        ["A transparent payload transmits at higher power, which broadens the received spectrum",
         "A regenerative payload selects a lower carrier frequency, reducing the observed shift",
         "A transparent payload applies no correction, so the residual error grows across a pass"]),

    5: ("Corrections are signalling, and signalling spends the capacity that would carry traffic",
        ["Each correction obliges the device to re-acquire the satellite before it can transmit again",
         "Frequent correction shortens the cyclic prefix available to protect each symbol",
         "The satellite must buffer each correction until its next contact with a gateway"]),

    # ---- Deck 2: UAV 3D beamforming ----
    6: ("A tower costs much the same whether it serves thousands or dozens, so density decides",
        ["Rural spectrum allocations are too narrow to carry a 5G channel at any useful bandwidth",
         "Rural terrain reflects signals in ways that a 5G equaliser is unable to resolve",
         "Rural users request higher sustained data rates than urban users typically request"]),

    7: ("The platform sits above its users, so the angle down to one changes with range",
        ["Aviation rules cap the azimuth beamwidth that an airborne transmitter may radiate",
         "Elevation steering is what compensates for Doppler shift on the feeder link path",
         "Steering in elevation is how the beam is kept clear of controlled airspace corridors"]),

    8: ("It drives a large array from few radio chains, keeping size, weight and power flyable",
        ["It widens the beam, so that platform tilt is tolerated without any tracking being needed",
         "It removes baseband processing from the platform, so no computer has to be carried",
         "It lets a single beam serve two carrier frequencies at once, doubling the capacity"]),

    9: ("Climbing improves line of sight and lengthens every link, so the two effects oppose",
        ["Spectrum licensing restricts the altitudes at which a platform is permitted to operate",
         "Greater altitude raises the Doppler shift observed on the service link to the users",
         "Greater altitude reduces the number of separate beams the antenna array can form"]),

    10: ("The variables trade against each other, so improving one relocates the bottleneck",
         ["The weakest single radio link determines overall performance in any layered system",
          "Regulatory limits are written against the whole system rather than its components",
          "The learned model must be retrained whenever any one component is changed or moved"]),

    # ---- Deck 3: machine learning for RACH ----
    11: ("It precedes all data and is built from round trips whose cost scales with link delay",
         ["It is the one procedure using the uplink, which carries the weakest link budget in NTN",
          "It depends on satellite ephemeris, which has not been acquired at device power-up",
          "It is the one procedure left unprotected by any forward error correction coding"]),

    12: ("Edge devices are further away, so their preambles fall outside the protective guard",
         ["Edge devices transmit at higher power, which saturates the satellite receiver front end",
          "Edge devices see a Doppler shift of opposite sign to those at the centre of the beam",
          "Edge devices are assigned a different preamble sequence set from those at the centre"]),

    13: ("Detection correlates against a known shape, which a moving offset distorts",
         ["It moves the preamble onto a subcarrier that is reserved for control signalling use",
          "It causes the preamble to arrive before the reception window has opened to receive it",
          "It raises the transmit power required beyond what a handset is able to produce"]),

    14: ("The ephemeris-aided one, which computes from geometry and forms the baseline to beat",
         ["The supervised one, since classifying a preamble is not considered learning at all",
          "The reinforcement one, since it applies fixed rules already set out by the standard",
          "None of them, since all three derive their behaviour from data gathered during operation"]),

    15: ("Inference competes for fixed power, makes heat, and may decide too late to be useful",
         ["A learned policy cannot be updated at all once the satellite has reached its orbit",
          "A learned policy needs continuous connectivity to a training server on the ground",
          "A learned policy is fundamentally incompatible with an OFDM-based air interface"]),

    # ---- Deck 4: GPS integration and augmentation ----
    16: ("Their failure modes differ, so conditions defeating one still permit the other",
         ["Both share a signal structure, so their range measurements can simply be averaged",
          "The terrestrial side supplies the precise clock that a navigation receiver lacks",
          "One of them supplies position while the other supplies velocity and heading data"]),

    17: ("Measuring there and back on one clock removes the need for the ends to be synchronised",
         ["It doubles the received energy, which improves the accuracy of the resulting range estimate",
          "It identifies which satellite a given signal came from before ranging against it",
          "It cancels the delay contributed by the atmosphere along the measured signal path"]),

    18: ("Each compares an observed position against surveyed truth and shares the difference",
         ["Each rebroadcasts an amplified copy of the original signal from the constellation",
          "Each depends on carrier-phase rather than code measurements to reach its accuracy",
          "Each requires a geostationary satellite in order to distribute its correction messages"]),

    19: ("Receivers only listen, so users are unlimited and no receiver is ever tracked",
         ["Receivers transmit briefly during acquisition and then fall silent for the session",
          "Receivers transmit to the control segment but never to the satellites themselves",
          "Receivers transmit at very low power so as not to interfere with the constellation"]),

    20: ("It removes errors arising in the satellites and atmosphere, which a receiver cannot see",
         ["It increases the number of navigation satellites that remain visible at a given location",
          "It replaces the trilateration solution with a directly measured position instead",
          "It removes the need to solve for the receiver clock bias as a fourth unknown"]),

    # ---- Deck 5: HAPS disaster recovery ----
    21: ("It is close enough that an ordinary handset antenna and power can close the link",
         ["It broadcasts on unlicensed spectrum that every commercial handset already supports",
          "It uses a waveform designed for handset access rather than for satellite terminals",
          "Orbiting satellites do not implement the 5G air interface that handsets expect"]),

    22: ("Traffic between local users is switched aboard, needing no surviving path to the core",
         ["Responders can be authenticated on the platform without contacting the ground core",
          "Traffic is stored aboard the platform until the terrestrial network is restored",
          "The platform no longer requires any feeder link to a gateway on the ground below"]),

    23: ("Altitude sets both at once and in opposite directions, being close but seeing less",
         ["It operates at a lower carrier frequency than any of the orbital alternatives do",
          "Its regenerative payload processes traffic faster than any orbital payload manages to",
          "It serves fewer simultaneous users, so the queuing component of delay stays lower"]),

    24: ("Rain attenuation rises steeply with frequency, and the gateway link sits high in band",
         ["The feeder link is longer, so it traverses a greater depth of the atmosphere",
          "The feeder link uses a narrower beam, which rain scatters far more readily",
          "The feeder link carries no error correction coding to protect it against fades"]),

    25: ("It bridges an interval until permanent infrastructure returns, so speed beats endurance",
         ["Its equipment degrades too quickly at altitude for any permanent deployment",
          "Aviation rules forbid continuous operation beyond a fixed authorised period",
          "Its available capacity is insufficient to serve a settled population over any long period"]),

    # ---- Deck 6: multi-connectivity and session continuity ----
    26: ("Each fails where the other copes, so together they span more conditions than either",
         ["Satellite access becomes cheaper to operate once terrestrial coverage is in place",
          "Operators are obliged by their licence conditions to provide both access types",
          "Terrestrial networks are unable to interface with the 5G core network architecture"]),

    27: ("One concerns how many links exist now; the other surviving a change of link",
         ["One applies to satellite access and the other applies to terrestrial access only",
          "One is a radio-layer function while the other is implemented at the physical layer",
          "One depends on network slicing while the other depends on edge computing support"]),

    28: ("One provides the paths; the other decides which traffic uses which path and how much",
         ["One runs inside the core network while the other runs in the radio access network",
          "One applies to downlink traffic while the other applies to uplink traffic only",
          "One is standardised by 3GPP while the other remains a vendor-specific extension"]),

    29: ("It removes the interval with no usable link, which is when packets and sessions drop",
         ["It lets the network compare both links directly before committing to either one",
          "It halves the total signalling needed to carry the transition through to its completion",
          "It allows the device to authenticate on the new link before releasing the old one"]),

    30: ("Handover becomes routine rather than exceptional, so its per-event cost dominates",
         ["Handover must be performed by the device itself rather than by the serving network",
          "Handover can no longer make any use of signal strength measurements whatsoever",
          "Handover must be deferred until the device has no active session in progress"]),

    # ---- Deck 7: spectrum sharing and interference ----
    31: ("Allocations overlap and footprints coincide, so a receiver sits inside both systems",
         ["Satellites radiate at powers exceeding the limits that terrestrial rules permit",
          "Terrestrial receivers lack the filtering needed to reject an incoming satellite signal",
          "The two systems use waveforms that are unable to coexist within a single band"]),

    32: ("Arrival angle governs how much energy a terrestrial antenna actually admits",
         ["Satellites radiate more power when they are positioned low toward the horizon",
          "Atmospheric absorption varies with elevation, which changes the power emitted",
          "Elevation angle determines which national jurisdiction the beam is falling within"]),

    33: ("It reshapes the pattern to suppress one direction while the main lobe is unaffected",
         ["It reduces power only during the intervals when the victim receiver is transmitting",
          "It relocates the beam onto a different frequency whenever it approaches a victim",
          "It reduces the count of active antenna elements so that total emission falls"]),

    34: ("A beam crosses borders but regulatory authority does not, so rules may conflict",
         ["Satellites are unable to retune quickly enough while crossing a national boundary",
          "Doppler shift changes discontinuously at the moment a boundary is crossed",
          "International links are obliged to adopt a different modulation scheme entirely"]),

    35: ("Separation guarantees peace by leaving capacity unused, which scarcity makes costly",
         ["Guard bands between services are prohibited under current international regulation",
          "Learning-based methods remove interference outright rather than merely reducing it",
          "Guard bands are impossible to implement within the constraints of a satellite payload"]),

    # ---- Deck 8: mobility management and handover ----
    36: ("Keeping the context allows a fast resume without the power cost of staying connected",
         ["It permits the device to send data without first obtaining a scheduling grant",
          "It is a mandatory precondition before any device is permitted to perform a handover",
          "It allows the network to page the device on a frequency other than its serving one"]),

    37: ("The decision returns on information that has aged while the geometry moved on",
         ["Satellites do not transmit any reference signal whose strength could be measured",
          "Signal strength cannot be measured with accuracy through the ionospheric layer",
          "The device lacks the uplink capacity needed to send measurement reports at all"]),

    38: ("It suppresses switches that are justified on one measure but poor decisions overall",
         ["It lets the handover be carried out by the device without the network taking part",
          "It removes the requirement for the device to know its own geographic position",
          "It guarantees that the handover will complete without any interruption occurring"]),

    39: ("Resources are committed on a prediction, so a wrong one holds capacity for nobody",
         ["Preparation obliges the device to maintain two active radio links simultaneously",
          "Preparation prevents the target from admitting any other device while it waits",
          "Preparation forces the device into an idle state for the duration of the transition"]),

    40: ("From reacting to measured degradation toward anticipating it from known motion",
         ["From network-controlled handover toward handover controlled by the device itself",
          "From hard handover between satellites toward soft handover between adjacent beams",
          "From triggers based on frequency offset toward triggers based on received power"]),
}
