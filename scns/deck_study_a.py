# -*- coding: utf-8 -*-
"""TE 456 study-bank question data, groups 1 to 8.

Five questions per deck. Format per question:
    (stem, correct_answer, [d1, d2, d3], explanation, teach)

These target the CONCEPTS a deck teaches: why a mechanism exists, what it trades
against, and how it connects to the rest of the course. They deliberately avoid
testing recall of quoted figures or of a conclusion slide's wording. Numbers
appear only where the magnitude is the point being made.

See build_study_questions.py for how these are compiled.
"""

DECKS = [
    {
        "topic": "Timing advance and frequency offset compensation in LEO NTN",
        "source": "Group 1 deck",
        "questions": [
            (
                "Why does a LEO link need two separate corrections rather than one?",
                "Distance produces a timing error and relative velocity produces a frequency error, and neither mechanism can fix the other's problem",
                [
                    "One corrects the uplink and the other corrects the downlink",
                    "One is applied by the device and the other by the satellite, purely for load sharing",
                    "One handles the service link and the other handles atmospheric attenuation",
                ],
                "The two faults have different physical causes and act on different quantities. A timing correction shifts when you transmit; it cannot shift what frequency you transmit at.",
                "Two properties of a LEO orbit each cause their own fault. "
                "DISTANCE causes a timing problem. An uplink has to land inside a narrow window at the base station, and the further away the satellite is, the earlier the device must transmit for its signal to arrive on time. The correction is TIMING ADVANCE. "
                "VELOCITY causes a frequency problem. The satellite closes on the user and then recedes, so the received carrier is shifted up and then down. The correction is FREQUENCY OFFSET COMPENSATION. "
                "WHY THEY CANNOT BE MERGED: they act on different axes. Timing advance decides WHEN you transmit; frequency compensation decides AT WHAT FREQUENCY. Confusing the two is a common error, and it returns as a marked point in the challenges material, where legacy timing advance is shown to be incapable of addressing Doppler for exactly this reason. "
                "The deeper idea is that on a terrestrial link neither correction is interesting: the tower does not move, so distance is stable and velocity is negligible. Both mechanisms exist because the base station itself is in motion.",
            ),
            (
                "What makes an open-loop correction possible at all, before the device has ever transmitted?",
                "Orbital motion is deterministic, so the geometry can be computed in advance from ephemeris and the device's own position",
                [
                    "The satellite transmits a pilot tone that the device measures directly",
                    "The network broadcasts a correction that is valid everywhere in the beam",
                    "The device assumes a worst-case delay and corrects for that",
                ],
                "You cannot measure a link you have not used yet. What you can do is calculate it, and that is only possible because the satellite's path obeys known laws rather than being random.",
                "This is the single most transferable idea in the NTN material, and it recurs in handover, in Doppler estimation, and in beam control. "
                "THE INSIGHT: radio fading is unpredictable, but ORBITAL MOTION IS NOT. A satellite's position and velocity at any future instant follow from published ephemeris. So instead of waiting to observe a problem, the system can compute what the problem will be and correct in advance. "
                "WHAT THE DEVICE NEEDS: the satellite's position, from broadcast ephemeris, and its own position, from GNSS. Two positions give a range, and a range gives both a propagation delay and a rate of change of that range. Delay feeds the timing correction; rate of change feeds the frequency correction. "
                "WHY THE RADIAL COMPONENT MATTERS: only motion ALONG the line of sight produces a frequency shift. This is why the shift is largest when a satellite is low on the horizon, closing almost directly toward the user, and falls to nothing when it passes overhead, where its motion is almost entirely across the line of sight. Understanding this geometry explains the shape of every Doppler curve in the course.",
            ),
            (
                "Why is a closed loop still needed if the open loop can predict the correction?",
                "Prediction is only as good as its inputs, so a residual error always remains and must be measured and removed",
                [
                    "The closed loop replaces the open loop once the connection is established",
                    "The open loop only works for the downlink, so the uplink needs measurement",
                    "Regulations require every correction to be confirmed by the network",
                ],
                "Ephemeris ages, GNSS fixes have error, and oscillators drift. The open loop gets the device close enough to be received at all; measurement closes the remaining gap.",
                "THE TWO-STAGE PATTERN is the thing to understand, not the individual steps. "
                "STAGE ONE, OPEN LOOP, is proactive and geometric. It works from known quantities and applies a correction before any transmission. Its accuracy is bounded by how good those known quantities are. "
                "STAGE TWO, CLOSED LOOP, is reactive and empirical. The network observes how early or late the uplink actually arrived, and returns a correction. For frequency, a tracking loop continuously trims the residual offset. "
                "WHY BOTH ARE NECESSARY: without the open loop the first transmission would miss the reception window entirely, and a closed loop cannot correct a signal it never received. Without the closed loop the residual error from imperfect prediction would accumulate. "
                "THE UNAVOIDABLE LIMIT: feedback describes geometry that has already happened. On a link where the round trip is long and the geometry moves during it, the correction is always slightly out of date. This is why the residual can be made small but never zero, and it is the same reason reactive handover fails in NTN.",
            ),
            (
                "Why does the payload type change the size of the Doppler problem, not just where it is processed?",
                "A transparent payload passes the signal through both moving link segments, so their shifts accumulate, whereas a regenerative payload terminates one of them on board",
                [
                    "A transparent payload transmits at a higher power, which widens the spectrum",
                    "A regenerative payload uses a lower carrier frequency, which reduces the shift",
                    "A transparent payload cannot apply any correction, so the error grows over time",
                ],
                "Doppler is produced by relative motion on each segment. If the signal is never demodulated, it crosses both segments and picks up a contribution from each.",
                "TWO LINK SEGMENTS: the SERVICE LINK between user and satellite, and the FEEDER LINK between satellite and gateway. Both have relative motion, so both generate Doppler. "
                "TRANSPARENT, or bent-pipe: the satellite amplifies and frequency-translates but does not demodulate. The signal therefore traverses both moving segments as a single continuous waveform, and the two shifts ADD. "
                "REGENERATIVE: the satellite demodulates on board, which TERMINATES the service link there. The information is recovered as bits and re-transmitted, so no service-link Doppler survives into the feeder link. "
                "THE GENERAL PRINCIPLE: whether an impairment accumulates across a relay depends on whether the relay regenerates the signal or merely repeats it. The same logic explains why a bent-pipe also amplifies the noise it received, while a regenerative payload can clean the signal by decoding and re-encoding. "
                "THE DIVISION OF CORRECTION LABOUR follows from what each end can observe. The device can compute its own service link from its own position; only the network sees the feeder link and the residual in the arriving signal.",
            ),
            (
                "What is the fundamental cost of running these corrections frequently?",
                "Corrections are signalling, and signalling consumes the same radio resources that would otherwise carry user data",
                [
                    "Each correction requires the device to re-acquire the satellite",
                    "Frequent corrections shorten the usable cyclic prefix",
                    "The satellite must store each correction until the next pass",
                ],
                "Accuracy and throughput are drawn from the same budget. Correcting more often improves alignment and reduces the capacity left for traffic.",
                "THE TRADE-OFF is the concept worth carrying, because the same shape appears throughout the course. "
                "Every correction command occupies air-interface resources. So the update rate is not a free parameter: correcting more often buys accuracy and spends throughput. An engineer chooses a point on that curve rather than maximising one end of it. "
                "THE OTHER LIMITS, grouped by kind rather than listed. HARDWARE: the device needs a better GNSS receiver, a wider RF front end and a more capable baseband than a terrestrial handset, which raises unit cost. TIMING: closed-loop feedback inherently trails reality, so some residual survives. INPUT QUALITY: open-loop prediction inherits any error in the GNSS fix or staleness in the ephemeris, so the correction can be no better than the data it was computed from. "
                "THE CONCEPTUAL SUMMARY of the whole approach: predict from known geometry, then refine from real measurement. Recognising that pattern lets you reconstruct the mechanism rather than memorise it, and it generalises to timing, to frequency, and to handover.",
            ),
        ],
    },
    {
        "topic": "UAV-enhanced 3D beamforming for rural 5G NTN",
        "source": "Group 2 deck",
        "questions": [
            (
                "Why is the rural coverage problem economic rather than technical?",
                "A tower costs roughly the same whether it serves thousands or dozens of users, so sparse populations cannot justify fixed infrastructure",
                [
                    "Rural spectrum allocations are too narrow for 5G to operate",
                    "Rural terrain reflects radio signals in ways 5G cannot equalise",
                    "Rural users demand higher data rates than urban users",
                ],
                "The radio engineering to cover a rural area is well understood. What fails is the business case, because cost per user rises as density falls.",
                "FRAMING THE PROBLEM CORRECTLY changes what counts as a solution. If rural coverage were a radio problem, the answer would be more power or better antennas. Because it is a cost-per-user problem, the answer is infrastructure that does not have to be permanently dedicated to a low-density area. "
                "THE PROPOSAL: fly the base station rather than build it. A UAV carrying a radio payload acts as an aerial base station, serving users below and reaching the core through a terrestrial or satellite link. Because it flies, it can be present only when and where demand exists, and moved elsewhere afterwards. "
                "WHY THIS SUITS THE LISTED APPLICATIONS: rural schooling, temporary events, border surveillance and disaster response all share a demand profile that appears and then disappears. That is precisely the case where permanent infrastructure is uneconomic and a mobile platform is not. "
                "The transferable lesson is that identifying whether a constraint is physical or economic determines which solution space is worth searching.",
            ),
            (
                "Why does an airborne base station need beam steering in elevation when a ground tower largely does not?",
                "The platform sits above its users, so the angle down to a user changes substantially with range",
                [
                    "Airborne transmitters are required by regulation to limit azimuth beamwidth",
                    "Elevation steering is needed to compensate for Doppler on the service link",
                    "Elevation steering keeps the beam clear of aviation corridors",
                ],
                "A tower stands among its users, so most of the useful variation is horizontal. From above, distance and elevation angle are coupled, which makes the vertical axis a real steering dimension.",
                "THE GEOMETRIC ARGUMENT: for a ground tower, users at different distances are all roughly at the same elevation, near the horizon, so steering in azimuth captures most of the benefit. For a platform overhead, a nearby user is almost directly below and a distant user is near the horizon, so elevation carries as much information as azimuth. "
                "WHAT 3D BEAMFORMING BUYS: directing energy in both azimuth and elevation improves coverage, signal quality and spectrum efficiency together, because power is concentrated where users are instead of being spread over ground that has none. "
                "THE COMPLICATION the platform introduces: it moves and tilts. A beam correctly aimed one moment points at empty ground the next. So the same mobility that makes the platform useful also makes alignment a continuous problem rather than a one-time configuration. "
                "This tension, where the property that solves one problem creates another, is worth recognising as a pattern; it recurs in LEO handover and in beam control.",
            ),
            (
                "What is the engineering reason hybrid beamforming suits an aerial platform?",
                "It drives a large antenna array from far fewer radio chains, keeping size, weight and power within what an aircraft can carry",
                [
                    "It produces a wider beam that tolerates platform tilt without tracking",
                    "It eliminates the need for any baseband processing on the platform",
                    "It allows one beam to serve two carrier frequencies simultaneously",
                ],
                "A fully digital array needs one radio chain per element, which is unliftable at useful aperture sizes. Hybrid places an analog phase-shift network between the digital precoder and the array.",
                "THE CONSTRAINT THAT DECIDES THE ARCHITECTURE is size, weight and power, usually abbreviated SWaP. Anything that flies is limited by what it can lift and power, and this constraint decides more design questions in this course than any other. "
                "THE PROBLEM: beam directivity improves with aperture, so you want many antenna elements. But a fully digital array needs a separate radio chain per element, and radio chains are heavy and power-hungry. "
                "THE COMPROMISE: a digital precoder feeds an analog phase-shift network, which feeds the array. Phase shifters are cheap and light compared with radio chains, so a large aperture can be driven by a small number of chains. You lose some flexibility relative to fully digital control and gain the ability to fly at all. "
                "PREDICTIVE TRACKING as the companion idea: rather than re-searching every beam whenever alignment drifts, the weights are updated from motion already observed. Searching costs time and signalling on every update; predicting achieves the same alignment far more cheaply. The same predict-rather-than-measure logic appears in handover and in Doppler compensation.",
            ),
            (
                "Why is altitude treated as a variable to be optimised rather than simply maximised?",
                "Climbing improves the chance of a clear line of sight but lengthens every link, so the two effects oppose one another",
                [
                    "Higher altitudes are restricted by spectrum licensing rules",
                    "Higher altitudes increase Doppler shift on the service link",
                    "Higher altitudes reduce the number of beams the array can form",
                ],
                "Line-of-sight probability and path loss both increase with altitude, and they act in opposite directions on link quality. The best altitude balances them for the terrain below.",
                "THE TRADE-OFF: from higher up, fewer hills and buildings block the path, so more users have a clear line of sight. But every user is also further away, so every link loses more power. Neither effect dominates universally; the balance depends on terrain roughness and user distribution. "
                "WHY THIS MATTERS CONCEPTUALLY: it is an example of a design variable with an interior optimum rather than a monotonic best value. Recognising these prevents the common error of assuming more of a good thing is always better. "
                "THE CONTROL LOOP that manages it: sense the channel and user state, optimise position and beam weights, act by repositioning and steering, learn by updating the model. "
                "THE WEAKNESS OF ANY SUCH LOOP: it always acts on the state it last observed. When the geometry changes faster than the loop converges, the system is aimed at where things were rather than where they are, producing brief quality dips during fast movement. That limitation is intrinsic to closed-loop control under motion and is not fixed by a better algorithm alone.",
            ),
            (
                "Why does the deck argue the binding constraint is system-level rather than any single link?",
                "The design variables trade against each other, so improving one in isolation relocates the bottleneck instead of removing it",
                [
                    "Because the weakest radio link always dominates overall performance",
                    "Because regulatory limits apply to the system as a whole rather than to components",
                    "Because the AI model must be retrained whenever any component changes",
                ],
                "Altitude, beam accuracy, terrain and backhaul are coupled. Optimising one while holding the others fixed simply moves where the limit sits.",
                "THE SYSTEMS ARGUMENT: fly higher and you improve line of sight while worsening path loss. Add radio chains and you sharpen the beam while shortening flight time. Extend the mesh and you widen coverage while adding hops that can each fail. Every improvement is drawn from a shared budget. "
                "POWER is the clearest illustration. The beamforming hardware and the control loop draw from the same source as propulsion, so processing capability and flight endurance are in direct competition. This is a stronger constraint than it first appears, because it means computation is not free even when the hardware is already aboard. "
                "BACKHAUL FRAGILITY is the second systemic weakness: relaying through neighbouring platforms to a satellite means each node inherits the problems of the one it depends on, so a single weak hop degrades everything downstream. "
                "THE CONCEPTUAL TAKEAWAY: in a system of coupled constraints, component-level optimisation is not sufficient, and the right question is where the joint optimum lies rather than how good any one part can be made.",
            ),
        ],
    },
    {
        "topic": "Machine learning for RACH optimization in NTN",
        "source": "Group 3 deck",
        "questions": [
            (
                "Why is random access the first mechanism that non-terrestrial networks break?",
                "It is the procedure a device must complete before any data can flow, and it is built from multiple round trips whose cost scales with link delay",
                [
                    "It is the only procedure that uses the uplink, which is weakest in NTN",
                    "It relies on satellite ephemeris, which is unavailable at power-up",
                    "It is the only procedure not protected by error correction coding",
                ],
                "Nothing else can happen until random access completes, and its handshake structure means link delay is paid several times over before a single byte of user data moves.",
                "WHY THE STRUCTURE MATTERS MORE THAN THE STEPS: the procedure is a handshake, meaning each message depends on the previous one having arrived. Dependent exchanges cannot be pipelined, so their total cost is the number of exchanges multiplied by the link delay. On a terrestrial link that product is negligible; over a satellite it becomes the dominant setup cost. "
                "THE DEEPER POINT: a protocol designed when delay was effectively free encodes that assumption in its structure. Making the link faster does not help, because the problem is the number of dependent round trips, not the speed of any one. "
                "THE FOUR ENVIRONMENTAL PROBLEMS that compound it: long delay makes every retry expensive; Doppler distorts the preamble the receiver is trying to detect; contention causes collisions because preambles are chosen at random; and differential delay spreads arrival times across a wide beam footprint. "
                "Recognising that the RACH is a dependency chain, rather than merely a slow procedure, is what explains why the fixes take the form they do.",
            ),
            (
                "Why does differential delay across a beam threaten preamble detection?",
                "Devices at the beam edge are further away than those at the centre, so their preambles arrive outside the guard interval that protects the reception window",
                [
                    "Devices at the beam edge transmit at higher power, saturating the receiver",
                    "Devices at the beam edge experience a different Doppler sign from those at the centre",
                    "Devices at the beam edge use a different preamble sequence set",
                ],
                "A wide footprint means a wide spread of path lengths. The cyclic prefix absorbs a bounded amount of that spread, and beyond that bound arrivals fall outside the window entirely.",
                "THE GEOMETRY: a satellite beam illuminates a large area, and a user at the edge of that area is measurably further from the satellite than one directly beneath it. That difference in path length becomes a difference in arrival time. "
                "WHY A GUARD INTERVAL EXISTS: the cyclic prefix absorbs timing spread so that arrivals which are slightly early or late still fall inside the correct window. It is sized for the spread expected in the environment it was designed for. "
                "THE NTN PROBLEM: the guard was sized for terrestrial cells, where path-length differences are small. Across a satellite beam the spread approaches the guard's capacity, leaving very little margin. Widening the beam or raising the orbit increases the spread further and consumes what remains. "
                "THE CONCEPTUAL POINT worth carrying: many 5G parameters encode an assumption about scale. Cyclic prefix length assumes a cell radius; subcarrier spacing assumes a maximum velocity; timer values assume a maximum delay. NTN violates several of these assumptions at once, which is why so many separate parameters need revisiting rather than one.",
            ),
            (
                "Why does a changing Doppler shift degrade preamble detection specifically?",
                "Detection works by correlating against a known sequence shape, and a frequency offset that moves during the preamble distorts that shape",
                [
                    "It shifts the preamble onto a subcarrier reserved for control signalling",
                    "It causes the preamble to arrive before the reception window opens",
                    "It increases the transmit power required beyond the device's capability",
                ],
                "Correlation assumes the received signal resembles the reference. An offset that is itself changing across the preamble smears it, lowering the correlation peak and causing missed detections.",
                "HOW DETECTION WORKS: the receiver correlates what it received against the known preamble sequence, and declares a detection when the correlation peak exceeds a threshold. This is robust to noise precisely because correlation accumulates the signal and averages the noise. "
                "WHAT BREAKS IT: correlation depends on the received waveform having the expected shape. A constant frequency offset already reduces the peak; an offset that CHANGES during the preamble smears it further, because different parts of the sequence are shifted by different amounts. "
                "WHY NTN MAKES THIS WORSE: the shift is not merely large, it varies through a pass, reversing sign as the satellite goes from approaching to receding. So both the offset and its rate of change matter, and it is the rate that distinguishes this from a simple calibration problem. "
                "CONTENTION, the companion failure: preambles are selected at random from a pool, so two devices can choose the same one. Because the preamble is the only thing distinguishing one attempt from another, identical choices are indistinguishable and both attempts fail. Notice this is a design consequence, not an environmental one, and it becomes severe in NTN only because a single beam serves so many devices.",
            ),
            (
                "Three families of technique are proposed. Which is not machine learning, and why does that matter?",
                "The ephemeris-aided approach, which computes from known geometry and therefore forms the baseline any learned method must outperform",
                [
                    "The supervised approach, because classification is not considered learning",
                    "The reinforcement approach, because it follows fixed standardised rules",
                    "None of them, since all three are learned from data",
                ],
                "Supervised and reinforcement methods learn from data. Pre-compensating from a published orbit calculates rather than learns, which makes it the benchmark rather than a competitor.",
                "THREE APPROACHES, distinguished by where their knowledge comes from. "
                "SUPERVISED OR DEEP LEARNING learns a mapping from labelled examples, applied to detecting preambles and estimating timing and frequency offsets at the receiver. "
                "REINFORCEMENT LEARNING learns a policy from the consequences of its own actions, applied to the contention controls: how aggressively to bar access, how long devices should back off, and how the preamble pool is divided. These are exactly the values an operator would otherwise fix at design time. "
                "EPHEMERIS-AIDED PREDICTION computes. The orbit is known, so delay and Doppler can be pre-compensated and access occasions pre-allocated without any training at all. "
                "WHY THE DISTINCTION MATTERS: the third approach is already standardised, so it is the baseline. A learned policy that merely matches it has bought nothing while adding training cost, inference cost and certification difficulty. The honest question is not whether learning works, but whether it beats deterministic geometry by enough to justify its overhead. "
                "THE CLOSED LOOP that learning runs in: observe collisions and load, decide the next settings, act by applying them, and learn from a reward that balances success, delay and energy.",
            ),
            (
                "What is the characteristic cost of moving a learned policy onto a satellite payload?",
                "Inference competes for a fixed power budget and generates heat that is hard to shed in vacuum, while control decisions may be stale by the time they take effect",
                [
                    "Learned policies cannot be updated once the satellite is launched",
                    "Learned policies require continuous connectivity to a ground training server",
                    "Learned policies are incompatible with the OFDM waveform",
                ],
                "Onboard computation is bounded by power and thermal limits rather than by algorithm quality, and the control loop still has to close across a long link.",
                "THE ONBOARD CONSTRAINTS, which apply to every AI proposal in this course and are worth learning once. "
                "POWER: a payload runs on a fixed solar budget, so computation competes directly with the communication function the satellite exists to perform. "
                "HEAT: on the ground a processor sheds heat into air. In vacuum the only path is radiation, so sustained computation produces heat faster than a small platform can radiate it. "
                "CONTROL-LOOP LATENCY: by the time a decision is computed and applied, the beam may be serving different users, so the decision can be correct for a situation that has passed. "
                "THE DESIGN-PROCESS CONSTRAINTS, which are different in kind. Training data is scarce because no large public set of real NTN access traces exists. A policy tuned on a simplified channel may behave differently in orbit, the simulation-to-reality gap. And a learned policy is difficult to certify against a written conformance specification, because it has no fixed behaviour to test. "
                "That last obstacle is regulatory rather than technical, and no amount of additional data resolves it, which is why it is often the binding constraint in practice.",
            ),
        ],
    },
    {
        "topic": "GPS signal integration and augmentation in 5G-NTN",
        "source": "Group 4 deck",
        "questions": [
            (
                "Why does combining GPS with 5G-NTN produce better positioning than either alone?",
                "Their failure modes do not overlap, so the conditions that defeat one are conditions the other can still operate in",
                [
                    "Both use the same signal structure, so their measurements can be averaged",
                    "5G-NTN provides the clock that GPS receivers otherwise lack",
                    "GPS supplies position while 5G-NTN supplies velocity",
                ],
                "GPS is strong under open sky and weak wherever the sky is blocked. NTN platforms reach places terrestrial infrastructure cannot. Combining systems only helps when their weaknesses differ.",
                "WHY GPS FAILS WHERE IT DOES: it needs a clear view of enough satellites. Urban canyons, dense forest, tunnels and building interiors all obstruct that view, so the receiver loses the observations it needs to solve for position. This is a geometry and signal-strength problem, not an accuracy problem. "
                "THE PRINCIPLE OF COMBINING SYSTEMS: redundancy only buys reliability when the redundant elements fail under different conditions. Two systems that fail together provide no benefit. GPS and NTN qualify because one is defeated by sky obstruction and the other is not. "
                "WHAT NTN CONTRIBUTES: additional measurements taken from platforms above the Earth, which supply observations when GNSS observations are scarce. These are complementary inputs to the same position solution rather than a replacement for it. "
                "THE ARCHITECTURAL RESULT is a hybrid system, and the general form of the argument, that complementary failure modes justify integration, is the same one used for combining terrestrial and non-terrestrial access in the multi-connectivity material.",
            ),
            (
                "Why does a round-trip measurement remove a requirement that a one-way measurement imposes?",
                "Measuring there and back and halving the result cancels the need for the two ends to share a synchronised clock",
                [
                    "It doubles the effective signal power, improving the accuracy of the estimate",
                    "It allows the receiver to identify which satellite the signal came from",
                    "It removes the effect of atmospheric delay on the measurement",
                ],
                "A one-way timing measurement requires both ends to agree on time, since it compares a departure instant against an arrival instant. A two-way measurement is taken entirely against one clock.",
                "THREE MEASUREMENT TYPES and what each fundamentally requires. "
                "TIME OF ARRIVAL measures travel time and converts it to distance. It requires SYNCHRONISED CLOCKS, because a departure time recorded at one end is compared with an arrival time recorded at the other. Any clock offset appears directly as a distance error. "
                "ANGLE OF ARRIVAL measures the direction a signal came from, and locates the device where direction lines from several nodes intersect. It requires an ANTENNA ARRAY, because direction is recovered from phase differences across elements, and a single antenna cannot provide it. "
                "ROUND TRIP TIME measures the total there-and-back delay and halves it. Because both the start and the stop are recorded on the SAME clock, no synchronisation between the two ends is needed. "
                "THE CONCEPTUAL LESSON: each technique buys accuracy with a different currency, whether clock synchronisation, antenna hardware or link overhead. Choosing between them is a question of which resource is available, not which is most accurate in the abstract. The same reasoning explains why GNSS itself solves for receiver clock bias as a fourth unknown rather than requiring receivers to carry atomic clocks.",
            ),
            (
                "What do all satellite augmentation systems have in common, whatever their accuracy?",
                "They compare a measured position against a precisely known truth to estimate the current error, then distribute that correction",
                [
                    "They all rebroadcast a stronger copy of the original GNSS signal",
                    "They all rely on carrier-phase rather than code measurements",
                    "They all require a geostationary satellite to deliver corrections",
                ],
                "The common mechanism is comparison against known truth. A station whose true coordinates are already surveyed can attribute any disagreement to error and share that estimate.",
                "THE UNIFYING IDEA: GNSS errors are largely COMMON to receivers in the same region, because they arise from satellite clock drift, orbit prediction error and atmospheric delay along similar paths. Anything measurable at one location is therefore useful at nearby locations. "
                "HOW THE SCHEMES DIFFER, conceptually rather than by their numbers. Some use a LOCAL reference station and are limited to receivers near it, since the shared-error assumption weakens with distance. Some compute corrections from a GLOBAL monitoring network and need no local station at all, at the cost of a convergence period before full accuracy is reached. Some improve the DELIVERY channel, using a wide-area broadcast to reach many receivers cheaply. And some change the MEASUREMENT itself, using carrier phase rather than code, which resolves position to a fraction of a wavelength and yields the finest accuracy available. "
                "WHY THE ACCURACY LADDER LOOKS AS IT DOES: schemes that correct code measurements reach the metre level, while those that exploit carrier phase reach the centimetre level, because the underlying observable is finer. Understanding that distinction explains the ordering without memorising the figures.",
            ),
            (
                "Why is the GPS user segment purely passive, and what follows from that?",
                "Receivers only listen, so the system serves unlimited users without consuming satellite capacity and cannot track any individual receiver",
                [
                    "Receivers transmit only during initial acquisition, then fall silent",
                    "Receivers transmit to the control segment but not to the space segment",
                    "Receivers transmit at very low power to avoid interfering with the constellation",
                ],
                "Because nothing is sent back, no satellite resource is consumed per user and the constellation has no knowledge of who is receiving.",
                "THE THREE SEGMENTS by function. The SPACE SEGMENT transmits signals that let a receiver determine location, speed and time. The CONTROL SEGMENT monitors and manages the constellation, computing corrections and uploading them. The USER SEGMENT receives and computes. "
                "WHY PASSIVITY IS ARCHITECTURALLY IMPORTANT, and this is the examinable insight rather than the segment list itself. "
                "SCALABILITY: since no satellite capacity is consumed per receiver, the system supports unlimited simultaneous users. A cellular network cannot do this, because every device consumes scheduled resources. "
                "PRIVACY: the constellation cannot know who is using it or where they are, because it receives nothing. Any tracking must occur elsewhere in the system. "
                "THE CONTRAST WITH NTN COMMUNICATION: an NTN link is two-way and therefore capacity-limited per user, which is why cell size, resource sharing and contention matter there and do not arise in GNSS. Holding both models in mind clarifies why the two systems face such different constraints despite both being satellite-based.",
            ),
            (
                "Conceptually, what does augmentation add that a better receiver cannot?",
                "It removes errors that originate outside the receiver, in the satellites and the atmosphere, which no amount of receiver quality can observe alone",
                [
                    "It increases the number of satellites visible from a given location",
                    "It replaces the trilateration solution with a direct position measurement",
                    "It eliminates the need to solve for receiver clock bias",
                ],
                "The dominant GNSS errors are not receiver noise. They come from clock drift, orbit prediction and atmospheric delay, and a single receiver has no independent way to measure them.",
                "WHERE GNSS ERROR ACTUALLY COMES FROM, grouped by origin. "
                "PROPAGATION: the ionosphere and troposphere slow and bend the signal, and these dominate under most conditions. Tropospheric effects worsen at low elevation angles because the path through the atmosphere is longer. "
                "SPACE SEGMENT: small clock drift and orbit prediction error. "
                "LOCAL ENVIRONMENT: multipath, where the signal reflects before arriving, which is site-specific and therefore not correctable by external augmentation. "
                "RECEIVER: thermal noise and hardware imperfection, typically the smallest contributor. "
                "GEOMETRY: dilution of precision, which is different in kind. It adds no delay of its own but AMPLIFIES every other error, because poorly spread satellites make the position solution ill-conditioned. This is why more satellites in view improves accuracy even when each individual measurement is unchanged. "
                "THE CONCLUSION THAT FOLLOWS: improving the receiver addresses only the smallest error terms. Correcting the propagation and space-segment terms requires external information, which is exactly what augmentation supplies, and improving geometry requires more satellites, which is what multi-constellation operation supplies.",
            ),
        ],
    },
    {
        "topic": "HAPS-based disaster recovery with 5G core integration",
        "source": "Group 5 deck",
        "questions": [
            (
                "Why can an unmodified handset work with a stratospheric platform but generally not with a satellite?",
                "The platform is close enough that the link budget closes to a normal phone antenna and transmit power",
                [
                    "The platform transmits on unlicensed spectrum that all handsets support",
                    "The platform uses a waveform designed specifically for handset access",
                    "Satellites do not implement the 5G air interface",
                ],
                "Path loss grows with distance, and a stratospheric platform is orders of magnitude closer than any orbit. That difference is what brings the link within reach of an ordinary phone.",
                "THE DECISIVE VARIABLE IS DISTANCE. A handset has a small antenna and limited transmit power, which sets a hard limit on the path loss it can overcome. A platform at stratospheric altitude is close enough to stay inside that limit; an orbiting satellite generally is not, which is why direct-to-device from orbit is difficult and requires special measures. "
                "THE ARCHITECTURAL CONSEQUENCE: because no special terminal or dish is needed, the platform serves people carrying the phones they already own. In a disaster that is the whole point, since victims cannot be issued satellite terminals. "
                "WHAT THE PLATFORM ACTUALLY IS: a standard base station flown at altitude, not a satellite payload. It behaves like a very tall tower rather than like a spacecraft, which is why the handset does not need to know anything unusual. "
                "IT IS ALSO TEMPORARY BY DESIGN, deployed when the ground network fails and withdrawn once service returns. Understanding it as a stopgap rather than permanent infrastructure explains why rapid deployment matters more than endurance in its design priorities.",
            ),
            (
                "Why does placing a user-plane function on the platform matter during a disaster?",
                "Traffic between users in the affected area can be switched locally without depending on a surviving path to the ground core",
                [
                    "It allows responders to be authenticated without contacting the ground network",
                    "It stores traffic until the terrestrial network is restored",
                    "It removes the need for any feeder link to a gateway",
                ],
                "The user-plane function is where traffic is routed. Hosting one aboard means two responders in the same area can communicate through the platform alone.",
                "THE SPLIT BETWEEN WHAT FLIES AND WHAT STAYS is decided by latency sensitivity and by resource cost. "
                "ON THE PLATFORM: the base station functions and a local traffic-routing function. These are latency-critical and must be near the users. "
                "ON THE GROUND: subscriber authentication, session management and routing to external networks. These are not latency-critical and belong where compute and power are cheap. "
                "WHY THIS MATTERS OPERATIONALLY: local routing means responders can talk to each other even if the connection to the wider network is degraded. Communication within the disaster zone is exactly the traffic that matters most in the first hours, and it becomes independent of infrastructure that may not have survived. "
                "THE LIMIT OF THAT INDEPENDENCE, and the condition the conclusion attaches: the platform restores the radio access network, not the transport behind it. Without a surviving path to the core, users can reach each other but not anything beyond the zone. Distinguishing access from transport is the concept being tested.",
            ),
            (
                "Conceptually, why does a stratospheric platform beat every orbital option on latency and lose to them on coverage?",
                "Both properties follow from altitude: being close shortens the propagation path and simultaneously narrows the area visible from the platform",
                [
                    "Because it uses a lower carrier frequency than orbital systems",
                    "Because its regenerative payload processes traffic faster than a satellite's",
                    "Because it serves fewer users, so queuing delay is lower",
                ],
                "Altitude sets both quantities at once and in opposite directions. Lower means shorter delay and a smaller footprint; higher means longer delay and a larger footprint.",
                "ONE VARIABLE, TWO CONSEQUENCES. Propagation delay is proportional to distance, so a lower platform always wins on latency. Coverage footprint grows with altitude, because a higher vantage point sees further, so a higher platform always wins on area. These cannot be optimised independently. "
                "WHERE EACH PLATFORM SITS: a stratospheric platform is far closer than any orbit and therefore offers the lowest delay and the smallest footprint. Low orbit is further and wider. Geostationary orbit is furthest and widest, with delay large enough to be noticeable in conversation. "
                "THE THIRD AXIS, DEPLOYMENT SPEED, breaks the pattern and is why this platform suits disasters. An orbital asset must be built and launched on a schedule measured in months or years. An atmospheric platform can be flown on the timescale of the emergency itself. "
                "COVERAGE IS NOT CAPACITY, and this distinction is worth holding separately. A wide footprint helps reach and hurts throughput per user, because everyone inside it shares one payload. So a large coverage area is an advantage for finding users and a disadvantage for serving them.",
            ),
            (
                "Why does the choice of a high-frequency feeder link introduce a weather dependency that the service link does not have?",
                "Rain attenuation increases sharply with frequency, so a high-frequency gateway link is vulnerable in conditions that barely affect a lower-frequency user link",
                [
                    "The feeder link is longer, so it passes through more atmosphere",
                    "The feeder link uses a narrower beam, which rain scatters more easily",
                    "The feeder link has no error correction coding applied",
                ],
                "The vulnerability follows from the frequency choice rather than the link's role. Attenuation by rain rises steeply with frequency, so bands chosen for capacity are the ones most affected.",
                "WHY A HIGH FREQUENCY IS CHOSEN ANYWAY: bandwidth is more plentiful at higher frequencies, and the feeder link must carry the aggregated traffic of every user the platform serves. It needs capacity that lower bands cannot supply. "
                "THE COST OF THAT CHOICE: rain attenuation grows steeply with frequency. The service link, operating lower for handset compatibility, is largely unaffected by weather that can seriously degrade the feeder link. "
                "THE STANDARD MITIGATION is site diversity: provide more than one gateway, geographically separated, so that heavy rain over one is unlikely to coincide with heavy rain over another. The concept generalises, since it answers a correlated-failure problem by ensuring the failures are uncorrelated. "
                "THE OTHER OPEN PROBLEMS, grouped by type. PHYSICAL: keeping station against stratospheric winds, and endurance limits on how long a platform can remain aloft. REGULATORY: emergency spectrum authorisation and airspace clearance, which are administrative obstacles rather than engineering ones and can be slower to resolve. SYSTEM: coordinating interference and handover with the terrestrial network that is being supplemented.",
            ),
            (
                "What general principle explains why a platform is described as a temporary layer by design?",
                "It is deployed to restore a capability that has failed and withdrawn once the permanent infrastructure returns, so endurance matters less than speed of deployment",
                [
                    "Its equipment degrades too quickly in the stratosphere for permanent use",
                    "Regulations forbid continuous operation beyond a fixed period",
                    "Its capacity is insufficient to serve a population indefinitely",
                ],
                "The design targets a gap in time rather than a gap in coverage. That changes which characteristics matter, promoting rapid deployment above long endurance.",
                "WHY THE FRAMING CHANGES THE ENGINEERING: if the platform were permanent infrastructure, endurance would be the dominant requirement and a twelve-day flight limit would be disqualifying. Because it is a stopgap covering the interval between infrastructure failing and being repaired, the relevant question is whether it can arrive quickly and last long enough to bridge that interval. "
                "THIS EXPLAINS THE PRIORITY ORDER in the design. Rapid deployment is essential. Compatibility with existing handsets is essential, since the user population cannot be re-equipped. Endurance is a limitation to be managed rather than a requirement to be met. "
                "THE SAME REASONING applies to the aerial platforms in the rural coverage material, where demand appears and disappears, and it is worth recognising as a category: infrastructure justified by the temporary nature of the need rather than by cost per unit of permanent capacity. "
                "APPLICATIONS follow the same profile: earthquakes, floods, wildfires, search and rescue, remote emergencies and military operations, all situations defined by a sudden need that later subsides.",
            ),
        ],
    },
    {
        "topic": "Multi-connectivity and session continuity across TN-NTN links",
        "source": "Group 6 deck",
        "questions": [
            (
                "What is the underlying argument for integrating terrestrial and non-terrestrial networks rather than choosing one?",
                "Each fails under conditions the other tolerates, so combining them covers a wider range of situations than either can alone",
                [
                    "Non-terrestrial networks are cheaper once terrestrial coverage exists",
                    "Regulations require operators to provide both access types",
                    "Terrestrial networks cannot support the 5G core architecture",
                ],
                "Terrestrial networks leave coverage gaps and fail in disasters; non-terrestrial networks cover those gaps but suffer frequent handovers and higher latency. The weaknesses are complementary.",
                "THE COMPLEMENTARY-WEAKNESS ARGUMENT, which recurs across this course. "
                "TERRESTRIAL fails on COVERAGE, since towers are uneconomic in sparse areas and absent over oceans, and on RESILIENCE, since disasters destroy the infrastructure precisely when it is needed. "
                "NON-TERRESTRIAL fails on LATENCY, because altitude imposes propagation delay, and on MOBILITY, because moving satellites force frequent handovers even for stationary users. "
                "NEITHER WEAKNESS IS SHARED, which is the condition that makes integration worthwhile. Two systems failing under the same conditions provide no combined benefit. "
                "THE PROBLEM-TO-SOLUTION MAPPING is the structure worth learning: frequent handovers are answered by predicting them rather than reacting; latency differences by routing traffic according to which path suits it; link failures by holding more than one link; congestion by steering traffic between links; and session interruption by overlapping the old and new links during a transition. Each solution attacks a specific named weakness rather than being a general improvement.",
            ),
            (
                "How do multi-connectivity and session continuity differ conceptually?",
                "Multi-connectivity concerns how many links exist at once; session continuity concerns whether a session survives when the link beneath it is replaced",
                [
                    "Multi-connectivity applies to satellite links and session continuity to terrestrial links",
                    "Multi-connectivity is a radio-layer function and session continuity a physical-layer function",
                    "Multi-connectivity requires slicing while session continuity requires edge computing",
                ],
                "One is a property of the present moment, describing simultaneous connections. The other is a property of a transition, describing what survives a change.",
                "THE DISTINCTION MATTERS because the two deliver different benefits and are often confused. "
                "MULTI-CONNECTIVITY gives redundancy and capacity NOW: because more than one link is live, traffic can be balanced across them, throughput can be aggregated, and a failure of one leaves the other carrying the session. These benefits all require two links to exist simultaneously. "
                "SESSION CONTINUITY gives survival ACROSS A CHANGE: the session persists when the underlying link is replaced, so there is no need to re-authenticate, no data is lost, and the user perceives no interruption. These benefits are about a transition, not about simultaneity. "
                "THEY ARE COMPLEMENTARY, not alternatives. Multi-connectivity makes continuity easier to achieve, since a second live link is a natural place for the session to continue, but continuity can also be provided without it. "
                "A useful test when answering: if the benefit disappears when only one link exists, it belongs to multi-connectivity. If it concerns what happens at the moment of switching, it belongs to continuity.",
            ),
            (
                "What is the difference in role between a mechanism that creates simultaneous connections and one that steers traffic across them?",
                "The first provides the paths; the second decides which traffic uses which path and in what proportion",
                [
                    "The first operates in the core network and the second in the radio access network",
                    "The first applies to downlink traffic and the second to uplink traffic",
                    "The first is standardised while the second is vendor-specific",
                ],
                "Creating the connections and deciding how to use them are separate concerns. One is a connectivity capability, the other a policy applied on top of it.",
                "SEPARATING MECHANISM FROM POLICY is the concept here, and it is a recurring architectural pattern. "
                "THE CONNECTIVITY MECHANISM lets a device hold simultaneous links to a terrestrial base station and a non-terrestrial one. It answers the question of whether multiple paths exist. "
                "THE TRAFFIC POLICY decides what to do with them: routing a flow down one path, switching it between paths, or splitting it across both. It answers the question of how those paths are used. "
                "WHY THE SEPARATION IS USEFUL: policy can change without changing the connectivity, and the same connectivity supports many policies. A latency-sensitive flow and a bulk transfer can be treated differently over the same pair of links. "
                "THE OTHER SUPPORTING TECHNOLOGIES fit this frame too. Edge computing shortens the path between user and application, so latency stays low as the access link changes. Slicing isolates services so each keeps its own quality guarantees. Predictive mobility management prepares handovers in advance rather than reacting to a threshold. Each addresses a different aspect of the same objective, which is that the user should not perceive the underlying network changing.",
            ),
            (
                "Why does overlapping the old and new connections during a handover eliminate a class of failure?",
                "It removes the interval in which the device has no usable link, which is when packets are lost and sessions drop",
                [
                    "It allows the network to compare the two links before committing",
                    "It halves the signalling required to complete the transition",
                    "It lets the device authenticate on the new link before releasing the old",
                ],
                "A conventional handover releases before acquiring, leaving a gap. Overlapping the two means there is never a moment without connectivity.",
                "THE FAILURE BEING REMOVED: in a release-then-acquire sequence there is an interval where neither link is usable. Traffic arriving during that interval is lost, and a sufficiently long gap causes the session itself to fail. "
                "THE FIX: establish the new link before releasing the old, so the gap never exists. "
                "THE COST, which is worth stating in an answer because it is the interesting half: the device must support two simultaneous radio connections. That is a hardware requirement, not a configuration change, and it raises device complexity and power consumption. "
                "THE GENERAL PATTERN: many reliability improvements in this course work by overlapping in time what was previously sequential, and they are paid for in resources held simultaneously rather than in sequence. Preparing target resources before a handover has the same shape, and the same kind of cost, since capacity is reserved before it is known to be needed. "
                "Why it matters more in NTN than terrestrially: handovers happen far more often, because the cell moves rather than the user, so a per-handover cost is multiplied by a much larger number of events.",
            ),
            (
                "Why does the frequency of handovers in a non-terrestrial network change what mobility management must do?",
                "Handover stops being an exceptional event and becomes routine, so its per-event cost dominates and must be minimised rather than merely tolerated",
                [
                    "Handovers must be performed by the device rather than the network",
                    "Handovers can no longer use signal strength measurements of any kind",
                    "Handovers must be scheduled to occur only when the device is idle",
                ],
                "In a terrestrial network handovers are occasional and their cost is amortised. When the serving cell moves away every few minutes regardless of user behaviour, that cost is paid continuously.",
                "THE SHIFT IN CHARACTER: terrestrially, a handover happens because the USER moved, so a stationary user has none. In a non-terrestrial network the CELL moves, so even a stationary user is handed over repeatedly. Handover changes from an exception to the normal condition. "
                "WHY THAT CHANGES THE ENGINEERING: a procedure invoked rarely can afford to be expensive. One invoked constantly cannot. Signalling overhead, interruption time and failure probability all get multiplied by a much larger event count, so each must be driven down. "
                "WHAT FOLLOWS: preparation in advance becomes worthwhile, because the preparation cost is amortised against a benefit that recurs. Prediction becomes worthwhile, because satellite motion is deterministic and can be exploited. And reducing unnecessary handovers becomes a goal in itself, since avoiding an event entirely is cheaper than performing it efficiently. "
                "THE APPLICATIONS listed share the property that connectivity must persist through constant change: aviation, maritime, disaster recovery and connected vehicles.",
            ),
        ],
    },
    {
        "topic": "Spectrum sharing and interference management, 5G NTN and TN",
        "source": "Group 7 deck",
        "questions": [
            (
                "Why does integrating terrestrial and non-terrestrial 5G create an interference problem that neither has alone?",
                "Their frequency allocations overlap and their footprints cover the same ground, so a receiver can be inside both systems at once",
                [
                    "Satellites transmit at powers that exceed terrestrial regulatory limits",
                    "Terrestrial receivers lack filters capable of rejecting satellite signals",
                    "The two systems use waveforms that cannot coexist in the same band",
                ],
                "Interference here is a consequence of overlapping allocation and overlapping coverage, not of a hardware defect or a power violation.",
                "THE GEOMETRY OF THE PROBLEM: when both systems serve the same area, a user equipment sits inside a terrestrial cell and a satellite beam simultaneously. If the two use the same or adjacent spectrum, each becomes a source of interference to the other's receivers. "
                "WHY THE ALLOCATIONS OVERLAP AT ALL: spectrum is scarce and already allocated. Extending 5G to satellites did not create new spectrum; it created new users of bands that terrestrial services and satellite services already occupied. Overlap was therefore inevitable rather than accidental. "
                "INTERFERENCE RUNS IN BOTH DIRECTIONS, and getting the direction right is commonly examined. On the DOWNLINK the satellite beam spills into the terrestrial cell and a ground user is the victim. On the UPLINK a terrestrial transmission rises into the satellite receiver, and the satellite is the victim. The direction determines who suffers and therefore which mitigation applies. "
                "FOUR MECHANISMS to manage: same-frequency operation at the same time; leakage into an adjacent band; a beam crossing a national border into another operator's network; and spectral smearing caused by rapid satellite motion. Only the last is caused by orbital dynamics; the others would exist for a stationary satellite.",
            ),
            (
                "Why must a regulatory emission limit for satellites depend on elevation angle rather than being a single figure?",
                "How much satellite energy reaches a terrestrial receiver depends on the arrival angle, since terrestrial antennas discriminate differently against different angles",
                [
                    "Satellites transmit more power when they are low on the horizon",
                    "Atmospheric absorption varies with elevation, changing the emitted power",
                    "Elevation angle determines which country the beam falls in",
                ],
                "A single number cannot capture the geometry. A beam arriving from overhead and one arriving near the horizon interact quite differently with a terrestrial receiver's antenna pattern.",
                "THE PURPOSE OF THE LIMIT: to bound how much power a satellite may deliver to the Earth's surface, so that terrestrial receivers sharing the band remain usable. "
                "WHY ANGLE MATTERS: terrestrial antennas are directional, and their rejection of an interfering signal depends on where that signal arrives from. Energy arriving near the horizon, close to the direction of a terrestrial user's own base station, is far more damaging than energy arriving from directly overhead. A limit that ignored angle would be either too permissive at some angles or needlessly restrictive at others. "
                "THE CONSTELLATION EXTENSION, which is the conceptually important part: a limit satisfied by one satellite says nothing about the aggregate when hundreds are simultaneously visible. Mega-constellations therefore forced a shift from per-satellite compliance to AGGREGATE compliance, bounding the summed contribution of the whole system. "
                "This is a general regulatory lesson: rules written for a small number of large assets often fail when the same service is delivered by a large number of small ones, and must be restated in aggregate terms.",
            ),
            (
                "How does null-steering differ in principle from simply reducing transmit power?",
                "It reshapes the radiation pattern so that energy is suppressed only toward the victim, leaving the main beam at full strength",
                [
                    "It reduces power only during periods when the victim is transmitting",
                    "It moves the beam onto a different frequency near the victim",
                    "It reduces the number of active antenna elements to cut total emissions",
                ],
                "Reducing power degrades service everywhere. Null-steering is selective in direction, so it removes interference in one direction while preserving performance in all others.",
                "THE KEY IDEA: an adaptive array does not merely point a beam, it SHAPES one. The radiation pattern has directions of high gain and directions of near-zero gain, and those low-gain directions can be placed deliberately. "
                "WHY THAT IS BETTER THAN POWER REDUCTION: interference is a directional problem, so a directional solution costs less. Turning down the transmitter protects the victim by degrading everyone, whereas placing a null protects the victim while the intended users see no change. "
                "THE OTHER TECHNIQUES, grouped by the resource they exploit. POWER CONTROL exploits the fact that transmitting more than necessary helps nobody and harms the other system. DYNAMIC OR COGNITIVE ACCESS exploits time, sensing which channels are momentarily free and using those. GUARD RESOURCES exploit separation in frequency or time, keeping the systems apart where sharing is impossible. "
                "NOTICE THE SPECTRUM OF APPROACHES: from full separation, which is safe and wasteful, through static partitioning, to real-time sharing, which is efficient and complex. The direction of travel in the standards is from the first toward the last, because spectrum scarcity makes waste increasingly unaffordable.",
            ),
            (
                "Why is cross-border coexistence a harder problem than interference within one network?",
                "A satellite beam does not stop at a national boundary but regulatory authority does, so the operator may face inconsistent rules over one footprint",
                [
                    "Satellites cannot change frequency quickly enough while crossing a border",
                    "Doppler shift changes discontinuously at a national boundary",
                    "International links require different modulation schemes",
                ],
                "The mismatch is between physical coverage and legal jurisdiction. Two neighbouring administrations with different limits leave no single rule the operator can comply with.",
                "THE NATURE OF THE DIFFICULTY: interference within one network is an engineering problem with an engineering solution. Cross-border interference is an engineering problem constrained by a legal structure that does not align with the physics. "
                "WHY A SATELLITE MAKES IT ACUTE: a terrestrial cell is small enough to sit within one jurisdiction. A satellite beam is large enough to cover several, so a single transmission is simultaneously subject to several regulatory regimes. "
                "THE PRACTICAL CONSEQUENCE: harmonisation between administrations becomes a prerequisite for deployment, and that process is slower than the technology it governs. "
                "THE OTHER OPEN CHALLENGES follow similar patterns. Satellite motion makes the interference geometry change continuously, so a static coordination agreement is insufficient. Onboard power and thermal budgets limit how sophisticated the mitigation hardware can be. And real-time coordination between satellite and mobile operators requires data exchange between competitors, which is an organisational obstacle rather than a technical one. "
                "The general lesson is that in shared-spectrum systems, the binding constraints are frequently regulatory and organisational rather than technical.",
            ),
            (
                "Why is dynamic, learning-based spectrum sharing regarded as the direction of travel rather than wider guard bands?",
                "Separation-based approaches guarantee non-interference by leaving spectrum unused, which is unaffordable as demand grows",
                [
                    "Guard bands are prohibited by international regulation",
                    "Learning-based methods eliminate interference entirely rather than reducing it",
                    "Guard bands cannot be implemented on satellite payloads",
                ],
                "Every separation-based method works by not using something. As spectrum scarcity increases, the cost of that unused capacity comes to outweigh the simplicity it buys.",
                "THE UNDERLYING TENSION: interference can always be avoided by keeping systems apart in frequency, in time or in space. The question is what that separation costs. "
                "WHY SEPARATION IS ATTRACTIVE: it is simple, verifiable and needs no coordination once agreed. A guard band cannot fail. "
                "WHY IT BECOMES UNAFFORDABLE: separation means capacity that exists and is deliberately not used. When spectrum was plentiful relative to demand that was an acceptable price; as demand grows it becomes the dominant inefficiency. "
                "WHAT DYNAMIC SHARING OFFERS INSTEAD: rather than reserving resources permanently, sense conditions and allocate in real time, so systems occupy the same spectrum whenever they would not actually collide. This recovers the wasted capacity at the cost of complexity, coordination and the risk that a real-time decision is wrong. "
                "THE STANDARDISATION TRAJECTORY reflects this, moving over successive releases from studying whether satellite integration is feasible, to specifying it, to refining coexistence rules, and toward deeper spectrum integration. Understanding the direction matters more than memorising which release did what.",
            ),
        ],
    },
    {
        "topic": "Mobility management and handover optimization in 5G NTN",
        "source": "Group 8 deck",
        "questions": [
            (
                "Why does an intermediate connection state exist between fully connected and fully idle?",
                "Keeping the device context in the network allows a fast resume without paying the power cost of an active connection",
                [
                    "It allows the device to transmit data without acquiring a scheduling grant",
                    "It is required before a device can perform a handover",
                    "It allows the network to page the device on a different frequency",
                ],
                "The two extremes trade power against resume latency, and neither suits bursty traffic. Retaining context while releasing the connection captures most of the power saving while keeping resumption cheap.",
                "THE THREE STATES AS A TRADE-OFF, which is more useful than the list itself. "
                "FULLY CONNECTED: data can flow immediately, and power consumption is highest because the device maintains an active link. "
                "FULLY IDLE: power consumption is lowest, no context is retained anywhere, and returning to service requires the full connection setup procedure. "
                "THE INTERMEDIATE STATE: the connection is released, so power falls, but the network RETAINS the device context, so resumption skips most of the setup. It exists because real traffic is bursty, with short active periods separated by gaps too long to stay connected and too short to justify a full teardown. "
                "TRANSITIONS follow activity: from connected to intermediate when data stops, from intermediate to idle after prolonged inactivity, and back to connected on new data or a page. "
                "WHY IT MATTERS IN NTN specifically: what happens when the serving cell changes depends on the state. A device in the intermediate or idle state performs cell reselection; a connected device performs a handover. Since cells move constantly in a non-terrestrial network, both paths are exercised far more often than terrestrially.",
            ),
            (
                "Why does a handover trigger based on measured signal strength fail in a non-terrestrial network?",
                "The decision is made on information that has aged during the round trip, by which time the geometry has changed",
                [
                    "Satellites do not transmit signals that can be measured for strength",
                    "Signal strength cannot be measured accurately through the ionosphere",
                    "The device has insufficient uplink capacity to send measurement reports",
                ],
                "A measurement must travel to the network and a decision must travel back. Over a satellite link that interval is long enough for the situation that justified the report to have changed.",
                "THE ASSUMPTION BEING VIOLATED: reactive triggering assumes the world changes slowly relative to the decision loop. On the ground that holds, because only the user moves and cells are fixed. In a non-terrestrial network the serving cell is itself moving quickly, and the decision loop is long because the link is long. Both factors push in the same direction. "
                "THE SECOND, SUBTLER FAILURE: distance to the satellite dominates path loss so completely that signal strength varies little across a cell, and little between one satellite and the next. Even a fresh measurement therefore carries less information than it would terrestrially, because there is less contrast to detect. "
                "THE REPLACEMENT: triggers derived from geometry and time. Because orbital motion is deterministic, the network can compute when a device will cross a coverage boundary, or when link quality will degrade, before it happens. This is the same predict-rather-than-measure principle used for timing advance and Doppler compensation. "
                "The generalisable insight is that when a feedback loop is slow relative to the dynamics it controls, prediction must replace measurement, and prediction is only available when the dynamics are deterministic.",
            ),
            (
                "What does requiring several conditions to be satisfied together achieve, compared with a single trigger?",
                "It reduces handovers that are technically justified but not actually beneficial, such as switching to a target that is already congested",
                [
                    "It allows the handover to be executed without network involvement",
                    "It removes the need for the device to know its own position",
                    "It guarantees the handover completes without interruption",
                ],
                "A single criterion can be satisfied in situations where handing over is a poor decision. Requiring a conjunction of conditions filters those cases out.",
                "THE PROBLEM WITH ONE CRITERION: any single measure can be right about one aspect and wrong overall. A target satellite may offer a stronger signal while being heavily loaded, or a device may cross a geographic boundary moments before the current link would have served it perfectly well for longer. "
                "WHAT A CONJUNCTION ADDS: by combining radio quality, predicted time until degradation, geographic position and the target's own load, the decision accounts for both the radio path and the state of the destination. The load condition is conceptually distinct from the others, since it concerns capacity rather than propagation. "
                "THE BENEFIT: fewer unnecessary handovers. Since every handover costs signalling and risks interruption, avoiding one entirely is more valuable than executing it efficiently. In an environment where handovers are already frequent, suppressing the unnecessary ones is a first-order gain. "
                "A RELATED OPTIMISATION worth understanding: switching between beams of the same satellite is cheaper than switching between satellites, because the serving node does not change and less state has to be transferred. Preferring the cheaper transition where possible is the same kind of reasoning.",
            ),
            (
                "Why does preparing resources at the target before a handover carry a cost even when it works?",
                "Resources are committed on a prediction, so any prediction that does not come true has held capacity that served nobody",
                [
                    "Preparation requires the device to maintain two active radio links",
                    "Preparation prevents the target from serving any other device",
                    "Preparation forces the device into the idle state during the transition",
                ],
                "Advance preparation converts a latency cost into a capacity cost. The reservation is made before the outcome is known, so incorrect predictions waste the reserved resources.",
                "THE GENERAL SHAPE OF THESE OPTIMISATIONS: nearly every technique here buys speed or reliability by doing work earlier, and pays for it in resources committed before they are known to be needed. "
                "RESERVING TARGET RESOURCES trades capacity for handover latency. "
                "OVERLAPPING THE OLD AND NEW LINKS trades device hardware complexity and power for the elimination of an interruption gap. "
                "POSITION-BASED TRIGGERING trades device battery, since knowing when a boundary is crossed means fixing position continuously, for a more reliable trigger than signal strength provides. "
                "DISTRIBUTING EPHEMERIS AND SIGNALLING trades air-interface capacity for the predictive capability that ephemeris enables. "
                "RUNNING LEARNED MODELS trades onboard power and thermal budget for better decisions. "
                "RECOGNISING THE PATTERN is the examinable skill: if asked to evaluate any of these techniques, the expected answer names both the gain and the resource it is drawn from, rather than presenting the technique as free.",
            ),
            (
                "How is the overall shift in non-terrestrial mobility management best characterised?",
                "From reacting to measured degradation toward anticipating it from known orbital motion",
                [
                    "From network-controlled handover toward device-controlled handover",
                    "From hard handover toward soft handover between beams",
                    "From frequency-based triggers toward power-based triggers",
                ],
                "The defining change is when the decision is made relative to the event. Because satellite motion is predictable, the decision can precede the degradation rather than follow it.",
                "THE CENTRAL SHIFT: terrestrial mobility management observes a problem and responds. Non-terrestrial mobility management computes when a problem will occur and acts first. "
                "WHY THE SHIFT IS POSSIBLE: satellite motion follows known orbital mechanics, so future geometry is calculable. Radio fading is not predictable in this way, which is why the terrestrial approach never developed in this direction. "
                "WHY THE SHIFT IS NECESSARY: the reactive loop is too slow relative to how fast the geometry changes, and signal strength carries too little contrast to be a reliable trigger. Both failures push toward the same answer. "
                "WHAT IT COSTS: prediction requires ephemeris distribution, position knowledge at the device, resources committed in advance, and in the learned variants onboard computation. The reliability gained is real, and so is the overhead. "
                "THE EXAM-USEFUL FORMULATION: the system trades a reactive, measurement-driven model for a predictive, geometry-driven one, accepting new overheads in exchange for reliability that the speed and delay of a low orbit would otherwise make unattainable.",
            ),
        ],
    },
]
