#!/usr/bin/env python3
"""
Build the Satellite Communication & Navigation Systems (TE 456 / NTN) MCQ bank.

Source material (extracted from the slide decks in this folder):
  - TE456-NTN-What&Why.pdf                     (Legacy SatCom -> NTN: what & why)
  - TE456-NTN-Overview-1.pdf                   (Orbits, platforms, beams)
  - TE456-5GNR-NTN-2026-complete.pdf           (3GPP 5G NR-NTN architecture & challenges)
  - TE456-Elements-SatCom5GSystems-2026-Complete.pdf (SatCom payload, links & 5G systems)

Each question is authored as (question_text, correct_answer, [distractor, distractor, distractor]).
The script places the correct answer at a balanced, reproducible position so the key
(A/B/C/D) is evenly distributed across the 100-question bank. Output JSON matches the
format used by the other practice sites in this repository:

    {
      "question_number": 1,
      "question_text": "...",
      "options": ["...", "...", "...", "..."],
      "correct_answer": ["..."]
    }
"""
import json
import random

# ---------------------------------------------------------------------------
# GROUP A - NTN Fundamentals: What & Why
# ---------------------------------------------------------------------------
GROUP_A = [
    ("A Non-Terrestrial Network (NTN) is best defined as a wireless communication network that:",
     "Uses radio network equipment carried on airborne or spaceborne vehicles",
     ["Relies exclusively on ground-based cell towers and fibre",
      "Connects two mobile handsets without any base station",
      "Operates only at optical wavelengths between ground stations"]),

    ("Terrestrial networks (TN) and non-terrestrial networks (NTN) differ primarily in their:",
     "Infrastructure and coverage areas",
     ["Choice of programming language for the core network",
      "Use of the TCP/IP protocol suite",
      "Billing and subscription models"]),

    ("In NTN terminology, a 'spaceborne' platform refers to:",
     "Satellite communication using artificial satellites orbiting the Earth",
     ["Drones and balloons flying in the lower atmosphere",
      "Fibre-optic backbone links between data centres",
      "Ground gateways that steer antennas toward satellites"]),

    ("Which of the following are examples of airborne NTN platforms?",
     "Drones (UAVs) and High-Altitude Platform Stations (HAPS)",
     ["GEO, MEO and LEO satellites",
      "Fixed gNBs and fibre cables",
      "Undersea cables and microwave relay towers"]),

    ("The airborne NTN platform abbreviated HAPS stands for:",
     "High-Altitude Platform Station",
     ["High-Availability Packet Switch",
      "Hybrid Aerial Positioning System",
      "High-Altitude Payload Satellite"]),

    ("One motivation for NTN cited in the 6G vision is that terrestrial networks currently:",
     "Cover less than 40% of the Earth's surface",
     ["Cover more than 95% of the Earth's surface",
      "Are completely immune to natural disasters",
      "Provide uniform, seamless coverage over the oceans"]),

    ("An NTN platform creating large beams to illuminate remote farms, oceans and IoT "
     "devices anywhere on Earth illustrates which NTN use-case category?",
     "Service ubiquity",
     ["Service continuity",
      "Service scalability",
      "Service localization"]),

    ("A cellular subscriber who boards a cruise ship or an aircraft and would otherwise lose "
     "coverage is best served by which NTN use-case category?",
     "Service continuity",
     ["Service ubiquity",
      "Service scalability",
      "Service redundancy"]),

    ("Broadcasting the same content, such as a software update or a live event, to many users "
     "over a large area with one wide NTN beam illustrates:",
     "Service scalability",
     ["Service continuity",
      "Service ubiquity",
      "Service isolation"]),

    ("Deploying terrestrial base stations across sparsely populated deserts, mountains and "
     "oceans is generally avoided mainly because:",
     "It is not cost-effective and often lacks a viable business case",
     ["Radio waves cannot physically travel over open water",
      "Spectrum is legally unavailable outside cities",
      "Satellites legally prohibit ground towers in those areas"]),

    ("A major driver of the decades-long success of terrestrial mobile networks has been:",
     "International standardization ensuring vendor compatibility and lower costs",
     ["The complete absence of regulation in the sector",
      "Exclusive reliance on proprietary, closed hardware",
      "The use of a single global operator worldwide"]),

    ("Historically, the satellite communications market has been fragmented largely because "
     "of:",
     "A lack of standardization, making interoperability between vendors difficult",
     ["Excessive standardization that stifled all innovation",
      "Government bans on manufacturing satellites",
      "An unlimited supply of cheap, interchangeable devices"]),

    ("Compared with satellite systems, a key characteristic of terrestrial networks is that "
     "they offer:",
     "Low propagation delay, which is important for real-time applications",
     ["Global coverage of oceans and polar regions",
      "Complete immunity to congestion and interference",
      "Very high latency measured in hundreds of milliseconds"]),

    ("The infrastructure of a terrestrial network is characterised by:",
     "Fixed ground-based base stations (e.g., gNodeB), cables and switching centres",
     ["Satellites, HAPS and drones operating in the sky",
      "Only end-user handsets communicating peer-to-peer",
      "Optical inter-satellite links operating in orbit"]),

    ("The current relationship between the satellite and terrestrial mobile communication "
     "industries is best described as:",
     "Progressively converging toward TN-NTN integration",
     ["Diverging into two fully separate ecosystems",
      "Remaining two permanently isolated industrial chains",
      "Being replaced entirely by wired networks"]),

    ("The 3rd Generation Partnership Project (3GPP) is significant to NTN because it:",
     "Completed the first global 5G NR standard and is extending it to support satellites",
     ["Manufactures and launches communication satellites",
      "Owns and operates the Starlink constellation",
      "Issues spectrum licences to operators in each country"]),

    ("In 5G rollout, NTN is expected to serve unserved areas such as isolated regions, "
     "aircraft and vessels, and additionally to serve:",
     "Underserved areas such as sub-urban/rural regions, upgrading limited terrestrial performance",
     ["Only dense urban centres that already have 5G",
      "Only areas that already have a fibre backhaul",
      "Only military installations, never civilian users"]),

    ("Generally, compared with NTN, terrestrial networks are described as providing:",
     "Higher reliability and lower bit error rates",
     ["Lower reliability and higher bit error rates",
      "Identical reliability under all conditions",
      "Reliable service only over the open oceans"]),

    ("A frequently cited advantage of NTN over TN during earthquakes, floods or armed "
     "conflict is that NTN:",
     "Can maintain coverage when terrestrial infrastructure is damaged or destroyed",
     ["Is completely unaffected by weather of any kind",
      "Requires no ground gateways whatsoever",
      "Eliminates the need for any radio spectrum"]),

    ("The integration of satellite communications into 5G is anticipated to facilitate:",
     "Anything, anytime, anywhere connectivity",
     ["Connectivity only within licensed urban cells",
      "Fixed-line-only broadband services",
      "Connectivity that works solely during daylight hours"]),

    ("Which statement best summarises the primary limitations of terrestrial networks?",
     "Restricted global reach, vulnerability to physical damage, and high cost in rugged terrain",
     ["Unlimited reach but uniformly very high latency",
      "Perfect disaster resilience but poor data speed",
      "Global ocean coverage but no urban coverage"]),

    ("The TE 456 course explicitly shifts its focus from:",
     "Legacy satellite communication toward Non-Terrestrial Networks",
     ["Non-Terrestrial Networks back toward fixed telephony",
      "5G NR back toward 2G GSM systems",
      "Optical fibre toward copper access networks"]),

    ("Relative to extensive terrestrial deployments in remote regions, NTNs are described as:",
     "Potentially more cost-effective, while extending coverage and providing a backup",
     ["Always more expensive, with no coverage benefit",
      "Equivalent in cost but lower in coverage",
      "Cheaper only because they need no spectrum"]),

    ("In the Ghanaian context discussed, rural regions have largely lagged in 4G coverage, "
     "leaving many users dependent on:",
     "3G networks",
     ["5G standalone networks",
      "Satellite broadband that is already deployed",
      "Fibre-to-the-home connections"]),

    ("An NTN is characterised as a network that uses a communications platform at an altitude "
     "of:",
     "More than tens of kilometres above the Earth",
     ["A few hundred metres, like a typical cell tower",
      "Exactly at sea level",
      "Below the tropopause only"]),
]

# ---------------------------------------------------------------------------
# GROUP B - Orbits, Platforms & Beams
# ---------------------------------------------------------------------------
GROUP_B = [
    ("According to Kepler's laws as applied to satellites, satellite orbits are:",
     "Ellipses with the Earth at one of the foci",
     ["Perfect circles centred exactly on the Earth's core",
      "Straight lines tangent to the equator",
      "Squares traced around the two poles"]),

    ("As a satellite's orbital altitude decreases and it gets closer to Earth, its:",
     "Orbital speed increases and its orbital period reduces",
     ["Orbital speed decreases and its period lengthens",
      "Speed and period both remain constant",
      "Field of view increases while its speed drops"]),

    ("A geostationary (GEO) satellite orbits at an altitude of approximately:",
     "35,786 km",
     ["550 km",
      "20,200 km",
      "384,000 km"]),

    ("A GEO satellite appears stationary to a fixed observer on Earth because it:",
     "Completes one orbit in about 24 hours, matching the Earth's rotation",
     ["Does not actually move at all in its orbit",
      "Orbits the Earth in under 90 minutes",
      "Is physically held in place by a tether"]),

    ("Theoretically, near-global coverage (excluding the extreme poles) can be achieved with "
     "how many GEO satellites?",
     "Three",
     ["One",
      "Twelve",
      "Twenty-four"]),

    ("Because of its high altitude, a GEO satellite exhibits a round-trip propagation delay on "
     "the order of:",
     "About 600 ms",
     ["About 1 ms",
      "About 25 ms",
      "About 50 microseconds"]),

    ("A recognised disadvantage of GEO satellites is:",
     "Poor signal coverage at the extreme polar regions",
     ["The need for constant satellite-to-satellite handovers",
      "An extremely short, negligible propagation delay",
      "A requirement for thousands of satellites for coverage"]),

    ("Non-Geostationary Earth Orbit (NGEO) satellites are characterised by:",
     "Orbital periods of less than 24 hours and positions that change relative to observers",
     ["Fixed positions above the equator at all times",
      "Orbital periods of exactly 24 hours",
      "Being permanently invisible from the ground"]),

    ("Low Earth Orbit (LEO) satellites typically operate at altitudes of:",
     "300 to 1,500 km",
     ["7,000 to 25,000 km",
      "Exactly 35,786 km",
      "Above 100,000 km"]),

    ("A typical LEO satellite has an orbital period of about:",
     "90 minutes",
     ["24 hours",
      "6 to 12 hours",
      "One week"]),

    ("Because of their low altitude, LEO satellites offer a small one-way propagation delay on "
     "the order of:",
     "1 to 5 ms",
     ["About 600 ms",
      "About 83 ms",
      "Several seconds"]),

    ("Medium Earth Orbit (MEO) satellites orbit at altitudes ranging from about:",
     "7,000 to 25,000 km",
     ["300 to 1,500 km",
      "35,786 km, fixed",
      "Below 300 km"]),

    ("MEO satellites are described as the backbone of global navigation; for example, GPS "
     "uses at least:",
     "24 MEO satellites",
     ["3 GEO satellites",
      "Thousands of LEO satellites",
      "A single HAPS platform"]),

    ("Achieving continuous global coverage with LEO satellites requires:",
     "Hundreds of satellites, forming a mega-constellation",
     ["A single satellite",
      "Exactly three satellites",
      "No more than six satellites"]),

    ("Starlink provides broadband using thousands of LEO satellites flying at about 550 km, "
     "achieving a round-trip delay of roughly:",
     "25 ms",
     ["600 ms",
      "250 ms",
      "2 ms"]),

    ("A disadvantage of NGEO (LEO/MEO) systems compared with GEO is that they:",
     "Require dynamic hand-offs and active ground-antenna tracking of moving satellites",
     ["Have far higher latency than GEO satellites",
      "Cannot provide any coverage of polar regions",
      "Need only a stationary dish with no tracking"]),

    ("For High-Altitude Platform Stations (HAPS), 3GPP focuses on altitudes between:",
     "8 and 50 km",
     ["300 and 1,500 km",
      "35,000 and 36,000 km",
      "1 and 5 km"]),

    ("Because a HAPS maintains its position relative to the Earth's surface, it:",
     "Uses Earth-fixed beams like a GEO satellite, with delay comparable to terrestrial networks",
     ["Uses only Earth-moving beams like a fast LEO satellite",
      "Has a round-trip delay of about 600 ms",
      "Covers a smaller area than a single terrestrial gNB"]),

    ("Compared with spaceborne NTN, airborne NTN platforms:",
     "Deploy quickly at lower cost with smaller delay, but face stabilization and weather challenges",
     ["Have a much larger propagation delay than GEO",
      "Are completely immune to strong winds and storms",
      "Provide permanent global coverage from a single unit"]),

    ("The satellite-period relation Period = C x distance^1.5 indicates that the orbital "
     "period:",
     "Increases with the 1.5 power of the orbital distance",
     ["Is independent of the orbital distance",
      "Decreases as the orbital distance increases",
      "Varies linearly with the orbital distance"]),

    ("The three types of beams used in an NTN to provide radio coverage are Earth-fixed, "
     "Earth-moving, and:",
     "Quasi-Earth-fixed beams",
     ["Polar-locked beams",
      "Counter-rotating beams",
      "Ground-anchored beams"]),

    ("An Earth-fixed beam is one that:",
     "Covers the same fixed geographic region on Earth at all times",
     ["Sweeps across a new area at every instant",
      "Covers area X then abruptly jumps to area Y",
      "Can only be produced by a LEO satellite"]),

    ("An Earth-moving beam is characterised by the fact that it:",
     "Covers a slightly different geographic area at each successive instant as the platform moves",
     ["Always illuminates the exact same area permanently",
      "Is produced only by stationary GEO satellites",
      "Requires beam steering to remain fixed on one spot"]),

    ("With a quasi-Earth-fixed beam covering area X from t1 to t2 and then a different area, "
     "continuity over area X is maintained because:",
     "An incoming quasi-Earth-fixed beam replaces the outgoing beam over the same area",
     ["The satellite physically stops moving in its orbit",
      "One beam covers all geographic areas simultaneously",
      "The user device switches to a wired connection"]),

    ("GEO satellites, with beam footprints from roughly 200 to 3,500 km, are most commonly "
     "used for services such as:",
     "Weather monitoring, TV broadcasting, and remote sensing/positioning",
     ["Ultra-low-latency competitive online gaming",
      "Sub-millisecond industrial control loops",
      "Short-range indoor positioning"]),
]

# ---------------------------------------------------------------------------
# GROUP C - 5G NR-NTN Architecture & Challenges
# ---------------------------------------------------------------------------
GROUP_C = [
    ("In 5G NR-NTN, the 'service link' is:",
     "The 5G radio access (Uu interface) between the UE and the satellite",
     ["The connection between the satellite and the gateway",
      "The direct link between two satellites in orbit",
      "The wired link between the gateway and the 5GC"]),

    ("The 'feeder link' (satellite radio interface, SRI) describes the connection between:",
     "The satellite and the ground gateway",
     ["The UE and the satellite",
      "The gNB and the 5G core network",
      "Two user devices directly"]),

    ("In NTN, the term SAN refers to the:",
     "Satellite Access Node",
     ["Secure Access Network",
      "Satellite Antenna Numerology",
      "Signal Attenuation Node"]),

    ("A transparent (bent-pipe) NTN payload:",
     "Amplifies, filters and frequency-translates the signal without onboard baseband processing",
     ["Fully decodes and re-encodes the signal in orbit",
      "Hosts the complete gNB onboard the satellite",
      "Terminates the Uu interface on the satellite"]),

    ("With a transparent payload, the NTN gNB is located:",
     "On the ground, typically co-located with the gateway",
     ["Onboard the satellite itself",
      "Inside the UE handset",
      "Distributed across several satellites"]),

    ("In the transparent-payload architecture, the 5G Uu radio interface terminates at:",
     "The terrestrial gNB, not at the satellite",
     ["The satellite payload",
      "The UE only",
      "The 5G core network"]),

    ("A regenerative (decode-and-forward) payload differs from a transparent one in that it:",
     "Incorporates gNB functions onboard, terminating the Uu interface at the satellite",
     ["Only amplifies and forwards, with no onboard processing",
      "Removes the need for any gateway or 5G core",
      "Cannot support inter-satellite links"]),

    ("A key latency advantage of the regenerative architecture is that:",
     "The single-way latency includes only the service link, reducing round-trip time",
     ["The satellite hardware becomes far simpler and cheaper",
      "It eliminates the need for a service link entirely",
      "The Uu interface terminates on the ground"]),

    ("An Inter-Satellite Link (ISL) in a regenerative NTN:",
     "Connects NTN payloads to one another, allowing relay toward a distant gateway",
     ["Connects a satellite to a terrestrial fibre ring",
      "Links a UE directly to the 5G core network",
      "Replaces the feeder link with a wired cable"]),

    ("A disaggregated gNB is split into a:",
     "Centralized Unit (CU) and a Distributed Unit (DU)",
     ["Uplink Unit and a Downlink Unit",
      "Service Unit and a Feeder Unit",
      "Primary Unit and a Secondary Unit"]),

    ("When a regenerative payload hosts only the gNB-DU while the CU stays on the ground, the "
     "feeder link carries the:",
     "F1 interface (F1-C signalling and F1-U user-plane traffic)",
     ["Uu air interface only",
      "N6 interface toward the Internet",
      "ISL optical control channel"]),

    ("In a multi-connectivity NTN scenario, the NTN UE:",
     "Simultaneously communicates with multiple radio or core networks",
     ["Connects to exactly one satellite at any time",
      "Uses only a wired backhaul connection",
      "Cannot connect to any terrestrial network"]),

    ("For direct NTN access to handheld UEs within FR1, the commonly used frequency bands "
     "are:",
     "S-band and L-band",
     ["Only the mmWave FR2 bands",
      "Only optical/visible-light bands",
      "Only sub-100 MHz HF bands"]),

    ("The first 5G NR-NTN specifications target enhanced Mobile Broadband via 5G NR and "
     "machine-type communication via:",
     "NB-IoT",
     ["Bluetooth Low Energy",
      "Wi-Fi 6",
      "LoRaWAN"]),

    ("The most challenging NTN characteristic inhibiting low-latency communication is:",
     "The long round-trip time due to the large UE-to-satellite distance",
     ["The small physical size of satellite antennas",
      "The absence of any modulation scheme",
      "The low cost of ground gateways"]),

    ("Typical one-way latency values quoted for NTN range from about 30-40 ms in LEO up to:",
     "About 544 ms in GEO constellations",
     ["About 5 ms in GEO constellations",
      "About 1 ms in GEO constellations",
      "About 60 ms in GEO constellations"]),

    ("The Doppler (carrier-frequency) shift in NTN arises mainly because:",
     "The satellite, and possibly the UE, moves, causing a time-variant carrier-frequency deviation",
     ["The satellite is perfectly stationary in space",
      "The gateway periodically changes its IP address",
      "The UE increases its transmit power over time"]),

    ("The 'Doppler rate' in an NTN specifically refers to:",
     "The variation of the Doppler shift over the connection time",
     ["The fixed frequency offset at a single instant",
      "The data rate carried on the feeder link",
      "The rate at which satellites are launched"]),

    ("To compensate the uplink Doppler shift, the UE typically:",
     "Estimates its position via GNSS and uses satellite ephemeris to pre-adjust its uplink carrier frequency",
     ["Randomly hops across all available subcarriers",
      "Increases transmit power to overpower the shift",
      "Waits until the satellite stops moving"]),

    ("Ionospheric propagation that causes a rotation of the waveform's polarization is known "
     "as:",
     "Faraday rotation",
     ["Doppler rotation",
      "Keplerian precession",
      "Rayleigh fading"]),

    ("Beyond round-trip time and Doppler effects, a further NTN technical challenge affecting "
     "the PHY/MAC layers is:",
     "Moving cells caused by satellite motion",
     ["Perfectly static, unchanging coverage areas",
      "The complete absence of any base station",
      "An unlimited supply of available spectrum"]),

    ("In the transparent-payload protocol stack, the termination points for RRC, PDCP, RLC, "
     "MAC and PHY are on the:",
     "NTN UE and the NTN gNB, since the satellite and gateway are transparent",
     ["Satellite payload and the gateway",
      "5G core network and the Internet",
      "UE and the satellite only"]),

    ("When a regenerative payload houses the full gNB, the RRC terminates in the satellite, "
     "which results in:",
     "A shorter reaction time for RRC procedures",
     ["A much longer RRC reaction time than the transparent case",
      "No RRC layer being needed at all",
      "RRC termination out on the Internet"]),

    ("In NTN, the gateway is the terrestrial station that:",
     "Connects the gNB (or 5GC) functions to the satellite",
     ["Acts as the end-user handset",
      "Generates the satellite's onboard electrical power",
      "Provides GNSS positioning directly to the UE"]),

    ("The regenerative payload's on-board processor (OBP), inserted between the LNA and the "
     "HPA, enables:",
     "Error correction and routing of packets between beams before retransmission",
     ["Only analogue amplification with no processing",
      "Elimination of the downlink antenna",
      "A direct wired connection to the 5G core"]),
]

# ---------------------------------------------------------------------------
# GROUP D - SatCom Payload, Links & 5G Systems
# ---------------------------------------------------------------------------
GROUP_D = [
    ("At its most basic, a communication satellite acts as a:",
     "Repeater - a receiver linked to a transmitter using different frequencies",
     ["Passive mirror that reflects signals unchanged",
      "Data-storage warehouse held in orbit",
      "GNSS timing clock and nothing more"]),

    ("A satellite communication system is divided into two main segments:",
     "The space segment and the earth/ground segment",
     ["The uplink segment and the billing segment",
      "The analogue segment and the digital segment",
      "The civilian segment and the military segment"]),

    ("The communications payload of a satellite consists of two distinct parts:",
     "Repeaters/transponders and antennas",
     ["Solar panels and batteries",
      "Thrusters and fuel tanks",
      "Ground gateways and user terminals"]),

    ("A transponder changes the uplink carrier frequency to a different downlink frequency. In "
     "the Ku band this is, for example, from:",
     "14 GHz on the uplink to 11 GHz on the downlink",
     ["11 GHz on the uplink to 14 GHz on the downlink",
      "20 GHz on the uplink to 30 GHz on the downlink",
      "14 GHz on the uplink to 14 GHz on the downlink"]),

    ("If a payload bandwidth of 500 MHz is divided into channels of 36 MHz each, the "
     "approximate number of transponders is:",
     "About 12",
     ["About 500",
      "About 36",
      "About 2"]),

    ("A satellite repeater always uses different frequencies for receive and transmit mainly "
     "in order to:",
     "Avoid interference between the incoming and outgoing signals",
     ["Save electrical power onboard the satellite",
      "Comply with Kepler's laws of motion",
      "Reduce the satellite to a single antenna"]),

    ("A transparent (bent-pipe) repeater typically consists of a low-noise amplifier, a "
     "high-power amplifier, and:",
     "A mixer with a local oscillator for frequency conversion",
     ["An on-board baseband processor for decoding",
      "A GNSS receiver for satellite positioning",
      "A propulsion thruster for station-keeping"]),

    ("Unlike a transparent repeater, a regenerative (processing) repeater:",
     "Demodulates the uplink to baseband, corrects errors, then remodulates for the downlink",
     ["Simply amplifies and forwards everything, including noise",
      "Cannot change the carrier frequency at all",
      "Contains no amplifiers of any kind"]),

    ("A benefit of a regenerative repeater over a bent-pipe one is that it:",
     "Cleans the signal by decoding and correcting errors instead of forwarding noise",
     ["Consumes far less power and mass",
      "Operates without any antennas",
      "Works only with analogue signals"]),

    ("Which of the following is a space-platform (bus) subsystem that supports the payload?",
     "Attitude and Orbit Control System (AOCS)",
     ["Physical Downlink Shared Channel (PDSCH)",
      "User Plane Function (UPF)",
      "Resource Block scheduler"]),

    ("The Telemetry, Tracking, and Command (TTC&M) subsystem is responsible for:",
     "Monitoring subsystem health, tracking position, and executing commands from ground control",
     ["Amplifying and retransmitting the user carriers",
      "Allocating IP addresses to the user devices",
      "Performing OFDMA resource scheduling"]),

    ("The three main satellite links are the service link, the feeder link, and the:",
     "Inter-satellite link (ISL)",
     ["Fibre backhaul link",
      "Ethernet control link",
      "Terrestrial microwave link"]),

    ("Inter-satellite links (ISLs) can be implemented using:",
     "Either radio-frequency or optical links",
     ["Only copper cabling",
      "Only acoustic signalling",
      "Only undersea fibre"]),

    ("The performance of transmitting equipment is measured by its EIRP, which is:",
     "The power fed to the antenna multiplied by the antenna gain in the considered direction",
     ["The ratio of antenna gain to system noise temperature",
      "The Boltzmann constant multiplied by temperature",
      "The received carrier-to-noise density ratio"]),

    ("The receiver figure of merit, G/T, is the ratio of:",
     "The antenna receive gain to the system noise temperature",
     ["The transmit power to the antenna gain",
      "The carrier power to the user bit rate",
      "The uplink frequency to the downlink frequency"]),

    ("A satellite link budget is fundamentally used to:",
     "Predict whether the received signal will be strong enough relative to the noise",
     ["Schedule the satellite's launch window",
      "Allocate telephone numbers to users",
      "Determine the satellite's orbital inclination"]),

    ("Noise power spectral density N0 is defined as:",
     "The product of the Boltzmann constant k and the system noise temperature T",
     ["The antenna gain divided by the temperature",
      "The EIRP minus the free-space path loss",
      "The carrier power multiplied by the bit rate"]),

    ("Which of the following is a link (propagation) loss accounted for in a satellite link "
     "budget?",
     "Free-space path loss together with rain/atmospheric attenuation",
     ["The Boltzmann constant of the receiver",
      "The EIRP of the transmitter",
      "The number of transponders onboard"]),

    ("In 5G NR, Frequency Range 1 (FR1) spans approximately:",
     "410 MHz to 7.125 GHz",
     ["24 to 52 GHz",
      "50 to 66 GHz",
      "Below 100 MHz only"]),

    ("In 5G NR, a resource block (RB) in the frequency domain is defined as:",
     "12 consecutive subcarriers",
     ["14 consecutive subcarriers",
      "10 consecutive subframes",
      "A single OFDM symbol"]),

    ("A 5G NR radio frame lasts 10 ms and contains:",
     "Ten subframes of 1 ms each",
     ["One subframe of 10 ms",
      "Fourteen subframes of 1 ms each",
      "Twelve subframes of 0.5 ms each"]),

    ("In 5G NR, the subcarrier spacing given by delta-f = 2^u x 15 kHz means that it:",
     "Scales flexibly with the numerology u (e.g., 15, 30, 60, 120 kHz)",
     ["Is fixed at 15 kHz for every deployment",
      "Decreases as the numerology u increases",
      "Depends only on the carrier frequency band"]),

    ("Which set lists three 5G NR downlink physical channels?",
     "PDSCH, PDCCH and PBCH",
     ["PUSCH, PRACH and PUCCH",
      "AMF, SMF and UPF",
      "RRC, PDCP and RLC"]),

    ("In the 5G initial access procedure, the UE first performs cell search using:",
     "The synchronization signals PSS and SSS",
     ["The random-access preamble on PRACH",
      "The RRC Connection Setup message",
      "The Sounding Reference Signal (SRS)"]),

    ("To increase spectral efficiency, the 5G NR physical layer adopts which channel-coding "
     "techniques?",
     "Polar coding and LDPC coding",
     ["Convolutional and Reed-Solomon coding only",
      "Turbo coding, exactly as used in LTE, only",
      "No channel coding at all"]),
]

# All 100 questions are compiled, in thematic order, into a single bank.
ALL_QUESTIONS = GROUP_A + GROUP_B + GROUP_C + GROUP_D
OUTPUT_FILE = "compiled.json"


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def main():
    rng = random.Random(456)  # reproducible key placement
    n = len(ALL_QUESTIONS)

    # Balanced key positions: exactly 25 of each slot across the 100 questions.
    per_slot, remainder = divmod(n, 4)
    positions = []
    for slot in range(4):
        positions += [slot] * (per_slot + (1 if slot < remainder else 0))
    rng.shuffle(positions)

    summary = {0: 0, 1: 0, 2: 0, 3: 0}
    records = []
    for idx, (q_text, correct, distractors) in enumerate(ALL_QUESTIONS):
        pos = positions[idx]
        options = build_options(distractors, correct, pos)
        assert options[pos] == correct
        assert len(options) == 4 and len(set(options)) == 4, q_text[:40]
        summary[pos] += 1
        records.append({
            "question_number": idx + 1,
            "question_text": q_text,
            "options": options,
            "correct_answer": [correct],
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)
    print(f"Wrote {OUTPUT_FILE}: {len(records)} questions")

    total = sum(summary.values())
    print("\nKey distribution (option slot -> count):")
    for slot in range(4):
        print(f"  slot {chr(65 + slot)}: {summary[slot]} ({summary[slot] / total:.0%})")
    print(f"  total: {total}")


if __name__ == "__main__":
    main()
