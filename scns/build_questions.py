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
     ["Relies on ground-based cell towers linked by buried fibre-optic backhaul",
      "Connects two mobile handsets directly via a sidelink, bypassing any base station",
      "Uses free-space optical laser links between two fixed ground stations on Earth"]),

    ("Terrestrial networks (TN) and non-terrestrial networks (NTN) differ primarily in their:",
     "Infrastructure and coverage areas",
     ["Choice of programming language for the core network",
      "Use of the TCP/IP protocol suite",
      "Billing and subscription models"]),

    ("In NTN terminology, a 'spaceborne' platform refers to:",
     "Satellite communication using artificial satellites orbiting the Earth",
     ["Drones and stratospheric balloons flying in the lower and upper atmosphere",
      "Fibre-optic backbone cabling that links terrestrial data centres together",
      "Ground gateway stations that steer directional antennas toward orbiting satellites"]),

    ("Which of the following are examples of airborne NTN platforms?",
     "Drones (UAVs) and High-Altitude Platform Stations (HAPS)",
     ["GEO, MEO and LEO satellites orbiting hundreds to tens of thousands of km up",
      "Fixed terrestrial gNBs connected by underground fibre-optic cables",
      "Undersea fibre cables and ground-based microwave relay towers"]),

    ("A High-Altitude Platform Station (HAPS), such as a balloon or airship in the "
     "stratosphere, is best characterised as an NTN platform that is:",
     "Unmanned, with lower latency than LEO and easier maintainability than a satellite",
     ["A navigation satellite in medium Earth orbit at an altitude of about 20,000 km",
      "A ground-based mast and antenna forming a fixed part of the terrestrial network",
      "A geostationary spacecraft fixed in orbit above a point on the equator"]),

    ("One motivation for NTN cited in the 6G vision is that terrestrial networks currently:",
     "Cover less than 40% of the Earth's surface",
     ["Cover more than 95% of the Earth's surface",
      "Already provide 5G coverage across more than 90% of the Earth's landmass",
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
     ["The complete absence of any government regulation across the sector",
      "Exclusive reliance on proprietary, vendor-locked, closed hardware platforms",
      "The use of a single global mobile operator that dominates the worldwide market"]),

    ("Historically, the satellite communications market has been fragmented largely because "
     "of:",
     "A lack of standardization, making interoperability between vendors difficult",
     ["Excessive standardization efforts that limited vendor innovation and design freedom",
      "Government bans on the domestic manufacturing of communication satellites",
      "An abundant supply of low-cost, interchangeable satellite devices"]),

    ("In a TN-versus-NTN comparison, the typical cell size differs in that:",
     "TN cells are small (giving high capacity per cell), whereas NTN cells are massive, tens to thousands of km across",
     ["TN cells are typically massive in size, whereas NTN cells shrink to just a few metres across in dense deployments",
      "Both TN and NTN use cells of an identical, fixed diameter regardless of platform or altitude",
      "NTN cells are consistently smaller than TN cells specifically to limit inter-cell interference levels"]),

    ("The infrastructure of a terrestrial network is characterised by:",
     "Fixed ground-based base stations (e.g., gNodeB), cables and switching centres",
     ["Satellites, HAPS platforms and drones operating high above the ground",
      "End-user handsets communicating directly with each other via sidelink, peer-to-peer",
      "Optical inter-satellite links relaying traffic between spacecraft in orbit"]),

    ("The current relationship between the satellite and terrestrial mobile communication "
     "industries is best described as:",
     "Progressively converging toward TN-NTN integration",
     ["Diverging into two fully separate, non-interoperable ecosystems",
      "Remaining two historically isolated industrial supply chains",
      "Being steadily replaced by fixed, wired fibre-optic networks"]),

    ("The 3rd Generation Partnership Project (3GPP) is significant to NTN because it:",
     "Completed the first global 5G NR standard and is extending it to support satellites",
     ["Manufactures and launches its own fleet of communication satellites into orbit",
      "Owns and commercially operates the Starlink broadband satellite constellation",
      "Issues national spectrum licences to mobile operators in each member country"]),

    ("In 5G rollout, NTN is expected to serve unserved areas such as isolated regions, "
     "aircraft and vessels, and additionally to serve:",
     "Underserved areas such as sub-urban/rural regions, upgrading limited terrestrial performance",
     ["Dense urban centres that already enjoy full 5G coverage from terrestrial gNodeBs",
      "Areas that already have a wired fibre-optic backhaul connection installed nearby",
      "Military installations under a dedicated defence spectrum allocation, apart from civilian networks"]),

    ("Generally, compared with NTN, terrestrial networks are described as providing:",
     "Higher reliability and lower bit error rates",
     ["Lower reliability and a higher bit error rate under typical conditions",
      "Identical reliability regardless of weather or terrain conditions",
      "Reliable service specifically over open-ocean shipping routes"]),

    ("A frequently cited advantage of NTN over TN during earthquakes, floods or armed "
     "conflict is that NTN:",
     "Can maintain coverage when terrestrial infrastructure is damaged or destroyed",
     ["Requires the same fibre-based backhaul infrastructure as terrestrial networks do",
      "Relies on a single regenerative satellite payload rather than any ground gateway",
      "Operates over dedicated fibre-optic links instead of licensed radio spectrum"]),

    ("Comparing latency, terrestrial networks are typically ultra-low (under about 1 ms), "
     "whereas non-terrestrial networks range from:",
     "About 20 ms for LEO up to 500 ms or more for GEO, owing to the large distances",
     ["About 1 ms for LEO up to roughly 5 ms for GEO, similar to fibre backhaul",
      "A fixed 100 ms round-trip delay regardless of which orbit type is used",
      "Consistently lower latency than terrestrial fibre networks in most deployment cases"]),

    ("Which statement best summarises the primary limitations of terrestrial networks?",
     "Restricted global reach, vulnerability to physical damage, and high cost in rugged terrain",
     ["Effectively unlimited global reach but consistently very high transmission latency",
      "Excellent resilience to natural disasters but comparatively poor data throughput",
      "Strong global ocean coverage but comparatively weak coverage in dense urban centres"]),

    ("Regarding mobility support, a key contrast between the two networks is that:",
     "A TN requires frequent handovers, while an NTN can offer seamless mobility across wide areas",
     ["A TN offers seamless wide-area mobility, while an NTN needs frequent, active handovers instead",
      "Neither a TN nor an NTN is designed to support user mobility in current standards",
      "Both require one scheduled handover procedure at a fixed daily interval"]),

    ("Relative to extensive terrestrial deployments in remote regions, NTNs are described as:",
     "Potentially more cost-effective, while extending coverage and providing a backup",
     ["Consistently more expensive than terrestrial builds, with no added coverage benefit",
      "Roughly equivalent in total deployment cost but offering lower area coverage",
      "Cheaper mainly because satellite operators are exempt from national spectrum licensing fees"]),

    ("In the Ghanaian context discussed, rural regions have largely lagged in 4G coverage, "
     "leaving many users dependent on:",
     "3G networks",
     ["5G standalone networks",
      "Satellite broadband that is already deployed",
      "Fibre-to-the-home connections"]),

    ("Compared with a terrestrial network's standard path loss, the signal constraints of an "
     "NTN are dominated by:",
     "Severe path loss and high Doppler shifts from satellite mobility, plus atmospheric/ionospheric interference",
     ["Minimal path loss and effectively no Doppler shift, resembling a short-range terrestrial Wi-Fi link",
      "Interference arising mainly from neighbouring ground-based cellular towers and street-level clutter",
      "A near-complete absence of any meaningful propagation loss, fading, or spectral interference effects"]),
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

    ("In an altitude-versus-orbital-speed table, orbital speed falls from about 7.8 km/s near "
     "200 km to about 3.1 km/s at roughly 35,800 km. This illustrates that:",
     "Orbital speed decreases as altitude increases, while the orbital period lengthens",
     ["Orbital speed increases as altitude increases, since higher orbits require greater velocity",
      "Orbital speed remains essentially constant regardless of orbital altitude",
      "The orbital period shortens as altitude increases, mirroring the decrease in orbital speed"]),

    ("A geostationary (GEO) satellite orbits at an altitude of approximately:",
     "35,786 km",
     ["550 km",
      "20,200 km",
      "384,000 km"]),

    ("A GEO satellite appears stationary to a fixed observer on Earth because it:",
     "Completes one orbit in about 24 hours, matching the Earth's rotation",
     ["Does not actually move within its orbit, remaining fixed relative to the stars",
      "Orbits the Earth in under 90 minutes, much faster than the planet's rotation",
      "Is physically held in place by a tether anchored to a ground station below"]),

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

    ("A satellite whose orbital period matches the Earth's rotation but which may be inclined "
     "or elliptical, lacking the strict 0-degree equatorial, fixed-point constraint of a GEO, "
     "is classified as:",
     "Geosynchronous orbit (GSO), of which GEO is a special case",
     ["Low Earth orbit (LEO), typically a few hundred kilometres up",
      "Medium Earth orbit (MEO), used mainly for navigation constellations",
      "A High-Altitude Platform Station (HAPS) flying in the stratosphere"]),

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

    ("A navigation satellite orbiting at an altitude of about 20,200 km is described as "
     "semi-synchronous, meaning its orbital period is approximately:",
     "12 hours",
     ["24 hours",
      "90 minutes",
      "1 hour"]),

    ("Starlink provides broadband using thousands of LEO satellites flying at about 550 km, "
     "achieving a round-trip delay of roughly:",
     "25 ms",
     ["600 ms",
      "250 ms",
      "2 ms"]),

    ("A disadvantage of NGEO (LEO/MEO) systems compared with GEO is that they:",
     "Require dynamic hand-offs and active ground-antenna tracking of moving satellites",
     ["Have significantly higher round-trip latency than a comparable GEO satellite link",
      "Cannot provide meaningful coverage of the polar regions at high latitudes",
      "Need a single stationary dish pointed at a fixed spot, with no active tracking"]),

    ("For High-Altitude Platform Stations (HAPS), 3GPP focuses on altitudes between:",
     "8 and 50 km",
     ["300 and 1,500 km",
      "35,000 and 36,000 km",
      "1 and 5 km"]),

    ("Because a HAPS maintains its position relative to the Earth's surface, it:",
     "Uses Earth-fixed beams like a GEO satellite, with delay comparable to terrestrial networks",
     ["Uses Earth-moving beams that sweep across new ground area, like a fast-moving LEO satellite",
      "Has a round-trip propagation delay of about 600 ms, similar to a GEO satellite link",
      "Covers a ground area smaller than that of a single terrestrial gNB cell site"]),

    ("Compared with spaceborne NTN, airborne NTN platforms:",
     "Deploy quickly at lower cost with smaller delay, but face stabilization and weather challenges",
     ["Have a considerably larger end-to-end propagation delay than a comparable GEO satellite link",
      "Are largely unaffected by moderate winds and storms, unlike ground-based masts",
      "Provide continuous global coverage from a single stationary platform overhead"]),

    ("For an Unmanned Aircraft System (UAS) used as an airborne NTN platform, the drone's "
     "operating altitude is typically limited to about:",
     "90 to 150 m, depending on country and region",
     ["8 to 50 km, up in the stratosphere where a HAPS typically operates",
      "300 to 1,500 km, the typical altitude range for a LEO satellite",
      "35,786 km, the fixed altitude of a GEO satellite"]),

    ("The three types of beams used in an NTN to provide radio coverage are Earth-fixed, "
     "Earth-moving, and:",
     "Quasi-Earth-fixed beams",
     ["Polar-locked beams",
      "Counter-rotating beams",
      "Ground-anchored beams"]),

    ("An Earth-fixed beam is one that:",
     "Covers the same fixed geographic region on Earth at all times",
     ["Sweeps across a new patch of ground continuously as the satellite moves",
      "Covers area X, then abruptly jumps to a distant area Y without transition",
      "Is generated by a fast-moving LEO satellite rather than a stationary one"]),

    ("An Earth-moving beam is characterised by the fact that it:",
     "Covers a slightly different geographic area at each successive instant as the platform moves",
     ["Continuously illuminates the exact same ground area throughout the satellite pass",
      "Is produced by a stationary GEO satellite that does not move relative to Earth",
      "Requires active beam steering to remain fixed on one ground spot continuously"]),

    ("With a quasi-Earth-fixed beam covering area X from t1 to t2 and then a different area, "
     "continuity over area X is maintained because:",
     "An incoming quasi-Earth-fixed beam replaces the outgoing beam over the same area",
     ["The satellite physically slows down and briefly stops moving along its orbit",
      "A single wide beam covers the entire visible hemisphere simultaneously",
      "The user device seamlessly switches over to a wired terrestrial connection instead"]),

    ("GEO satellites, with beam footprints from roughly 200 to 3,500 km, are most commonly "
     "used for services such as:",
     "Weather monitoring, TV broadcasting, and remote sensing/positioning",
     ["Ultra-low-latency competitive online gaming requiring sub-20 ms response times",
      "Sub-millisecond industrial control loops for robotic factory automation",
      "Short-range indoor positioning within a single warehouse or building"]),
]

# ---------------------------------------------------------------------------
# GROUP C - 5G NR-NTN Architecture & Challenges
# ---------------------------------------------------------------------------
GROUP_C = [
    ("In 5G NR-NTN, the 'service link' is:",
     "The 5G radio access (Uu interface) between the UE and the satellite",
     ["The feeder-link connection between the satellite and the ground gateway station",
      "The direct radio link between two satellites relaying traffic in orbit",
      "The wired terrestrial link between the ground gateway and the 5G core network"]),

    ("The 'feeder link' (satellite radio interface, SRI) describes the connection between:",
     "The satellite and the ground gateway",
     ["The UE and the satellite over the radio service link",
      "The gNB and the 5G core network via a wired N2/N3 interface",
      "Two user devices communicating directly via sidelink"]),

    ("An NTN round-trip time is expressed as RTT = 2(Tprop1 + Tprop2) + 2 Tslot + Tproc1 + "
     "Tproc2. In this expression, the propagation terms Tprop1 and Tprop2 correspond to the:",
     "UE-to-satellite link and the satellite-to-gateway link",
     ["Uplink and downlink of a single terrestrial cell",
      "Two processing steps carried out inside the gNB",
      "Inter-satellite link and the terrestrial fibre backhaul"]),

    ("A transparent (bent-pipe) NTN payload:",
     "Amplifies, filters and frequency-translates the signal without onboard baseband processing",
     ["Fully decodes, error-corrects and re-encodes the signal onboard before retransmission",
      "Hosts the complete gNB, including RRC and PDCP layers, onboard the satellite",
      "Terminates the 5G Uu radio interface directly on the satellite payload itself"]),

    ("With a transparent payload, the NTN gNB is located:",
     "On the ground, typically co-located with the gateway",
     ["Onboard the satellite itself, alongside the on-board processor",
      "Inside the UE handset, integrated with the baseband modem",
      "Distributed redundantly across several satellites in the same orbital plane"]),

    ("In the transparent-payload architecture, the 5G Uu radio interface terminates at:",
     "The terrestrial gNB, not at the satellite",
     ["The satellite payload, acting as a transparent relay point",
      "The UE alone, with no counterpart terminating on the network side",
      "The 5G core network, several hops beyond the ground gateway"]),

    ("A regenerative (decode-and-forward) payload differs from a transparent one in that it:",
     "Incorporates gNB functions onboard, terminating the Uu interface at the satellite",
     ["Simply amplifies and frequency-converts the signal, with no onboard processing",
      "Removes the need for a ground-based gateway station between hops",
      "Cannot support any inter-satellite links due to onboard hardware limits"]),

    ("A key latency advantage of the regenerative architecture is that:",
     "The single-way latency includes only the service link, reducing round-trip time",
     ["The satellite hardware becomes far simpler, cheaper, and lighter to launch",
      "It removes the need for a service link between the UE and the satellite altogether",
      "The Uu interface terminates on the ground at the gateway, not in orbit"]),

    ("An Inter-Satellite Link (ISL) in a regenerative NTN:",
     "Connects NTN payloads to one another, allowing relay toward a distant gateway",
     ["Connects a satellite to a terrestrial fibre ring encircling a data centre",
      "Links a UE directly to the 5G core network without any radio interface",
      "Replaces the feeder link with a buried fibre-optic cable to the gateway"]),

    ("A disaggregated gNB is split into a:",
     "Centralized Unit (CU) and a Distributed Unit (DU)",
     ["Uplink Processing Unit and a separate Downlink Processing Unit",
      "Service Link Unit and a distinct Feeder Link Unit",
      "Primary Radio Unit and a redundant Secondary Radio Unit"]),

    ("When a regenerative payload hosts only the gNB-DU while the CU stays on the ground, the "
     "feeder link carries the:",
     "F1 interface (F1-C signalling and F1-U user-plane traffic)",
     ["Uu air interface signalling directly between the UE and the DU",
      "N6 interface carrying user traffic toward the public Internet",
      "ISL optical control channel linking neighbouring satellites"]),

    ("In a multi-connectivity NTN scenario, the NTN UE:",
     "Simultaneously communicates with multiple radio or core networks",
     ["Connects to exactly one satellite at any given time, with no fallback",
      "Relies on a wired backhaul connection instead of any radio link",
      "Cannot connect to any terrestrial network alongside the satellite link"]),

    ("For direct NTN access to handheld UEs within FR1, the commonly used frequency bands "
     "are:",
     "S-band and L-band, the sub-6 GHz FR1 ranges used for handheld access",
     ["The mmWave FR2 bands above 24 GHz, unsuitable for handheld devices",
      "Optical and visible-light bands used for free-space laser links",
      "Sub-100 MHz HF bands used for long-distance ionospheric skywave links"]),

    ("In the NTN HARQ retransmission process, after the receiver returns a negative "
     "acknowledgement (NACK) for a corrupted packet, the transmitter responds by:",
     "Retransmitting the data using a new redundancy version (RV)",
     ["Dropping the connection to the UE after a small fixed number of retries",
      "Switching the UE over to a different satellite constellation mid-session",
      "Ignoring the NACK and simply moving on to the next scheduled data block"]),

    ("The most challenging NTN characteristic inhibiting low-latency communication is:",
     "The long round-trip time due to the large UE-to-satellite distance",
     ["The small physical size of the satellite antenna array limiting gain",
      "The absence of a standardized modulation scheme for the downlink carrier",
      "The relatively low deployment cost of terrestrial ground gateway stations"]),

    ("Typical one-way latency values quoted for NTN range from about 30-40 ms in LEO up to:",
     "About 544 ms in GEO constellations",
     ["About 5 ms in GEO constellations",
      "About 1 ms in GEO constellations",
      "About 60 ms in GEO constellations"]),

    ("The Doppler (carrier-frequency) shift in NTN arises mainly because:",
     "The satellite, and possibly the UE, moves, causing a time-variant carrier-frequency deviation",
     ["The satellite remains perfectly stationary relative to a fixed point on the Earth's surface",
      "The ground gateway periodically changes its assigned IP address mid-session",
      "The UE gradually increases its transmit power as the session progresses"]),

    ("The 'Doppler rate' in an NTN specifically refers to:",
     "The variation of the Doppler shift over the connection time",
     ["The fixed frequency offset measured at a single instant in time",
      "The data throughput rate carried on the satellite feeder link",
      "The rate at which new satellites are launched into a constellation"]),

    ("To compensate the uplink Doppler shift, the UE typically:",
     "Estimates its position via GNSS and uses satellite ephemeris to pre-adjust its uplink carrier frequency",
     ["Randomly hops across the available subcarriers, hoping the receiver stays synchronized despite the shift",
      "Increases its uplink transmit power in an attempt to overpower the frequency shift",
      "Waits passively until the satellite pauses its motion along the orbital path"]),

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
     ["Satellite payload and the ground gateway station, since both process baseband",
      "5G core network and the public Internet, several hops beyond the gateway",
      "UE and the satellite alone, without the gateway or gNB participating"]),

    ("When a regenerative payload houses the full gNB, the RRC terminates in the satellite, "
     "which results in:",
     "A shorter reaction time for RRC procedures",
     ["A much longer RRC reaction time than the transparent case",
      "No RRC layer being present anywhere in the regenerative architecture",
      "RRC termination out on the Internet"]),

    ("In NTN, the gateway is the terrestrial station that:",
     "Connects the gNB (or 5GC) functions to the satellite",
     ["Acts as the end-user handset",
      "Generates the satellite's onboard electrical power",
      "Provides GNSS positioning directly to the UE"]),

    ("The regenerative payload's on-board processor (OBP), inserted between the LNA and the "
     "HPA, enables:",
     "Error correction and routing of packets between beams before retransmission",
     ["Purely analogue amplification and frequency conversion, with no digital processing",
      "Elimination of the separate downlink antenna, reusing the uplink array instead",
      "A direct wired fibre connection from the satellite down to the 5G core network"]),
]

# ---------------------------------------------------------------------------
# GROUP D - SatCom Payload, Links & 5G Systems
# ---------------------------------------------------------------------------
GROUP_D = [
    ("At its most basic, a communication satellite acts as a:",
     "Repeater - a receiver linked to a transmitter using different frequencies",
     ["A passive mirror that simply reflects incoming signals unchanged, with no amplification",
      "A data-storage warehouse in orbit, downloading its contents once per day",
      "A GNSS timing clock broadcasting position data, with no communication relay function"]),

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
     ["Save electrical power onboard the satellite by cutting amplifier duty cycles",
      "Comply with Kepler's laws of motion governing the shape of the orbit",
      "Reduce the satellite payload down to a single shared antenna element"]),

    ("A transparent (bent-pipe) repeater typically consists of a low-noise amplifier, a "
     "high-power amplifier, and:",
     "A mixer with a local oscillator for frequency conversion",
     ["An on-board baseband processor that fully decodes and re-encodes the signal",
      "A GNSS receiver used solely for determining the satellite's own position",
      "A propulsion thruster used for periodic orbital station-keeping manoeuvres"]),

    ("Unlike a transparent repeater, a regenerative (processing) repeater:",
     "Demodulates the uplink to baseband, corrects errors, then remodulates for the downlink",
     ["Simply amplifies and forwards everything it receives, including any accumulated noise",
      "Cannot translate the uplink carrier frequency to a different downlink frequency",
      "Contains no power amplifiers, relying purely on passive reflection of the signal"]),

    ("A benefit of a regenerative repeater over a bent-pipe one is that it:",
     "Cleans the signal by decoding and correcting errors instead of forwarding noise",
     ["Consumes noticeably less electrical power and structural mass than a bent-pipe design",
      "Operates without any onboard antenna, coupling signals directly through waveguides",
      "Works with analogue signals alone, unable to process digital baseband data"]),

    ("Which of the following is a space-platform (bus) subsystem that supports the payload?",
     "Attitude and Orbit Control System (AOCS)",
     ["Physical Downlink Shared Channel (PDSCH)",
      "User Plane Function (UPF)",
      "Resource Block scheduler"]),

    ("The Telemetry, Tracking, and Command (TTC&M) subsystem is responsible for:",
     "Monitoring subsystem health, tracking position, and executing commands from ground control",
     ["Amplifying and retransmitting the user carriers between the uplink and downlink paths",
      "Allocating dynamic IP addresses to each connected user device",
      "Performing OFDMA resource-block scheduling for the user-plane traffic"]),

    ("The three main satellite links are the service link, the feeder link, and the:",
     "Inter-satellite link (ISL)",
     ["Fibre backhaul link",
      "Ethernet control link",
      "Terrestrial microwave link"]),

    ("Inter-satellite links (ISLs) can be implemented using:",
     "Either radio-frequency (RF) links or optical (laser) links",
     ["Copper coaxial cabling strung physically between adjacent satellites",
      "Acoustic signalling pulses transmitted through the vacuum of space",
      "Undersea fibre-optic cable strung between satellites in orbit"]),

    ("The performance of transmitting equipment is measured by its EIRP, which is:",
     "The power fed to the antenna multiplied by the antenna gain in the considered direction",
     ["The ratio of antenna receive gain to the system's equivalent noise temperature",
      "The Boltzmann constant multiplied by the absolute system noise temperature",
      "The received carrier power divided by the noise power spectral density"]),

    ("The receiver figure of merit, G/T, is the ratio of:",
     "The antenna receive gain to the system noise temperature",
     ["The ratio of transmit power fed into the antenna to its gain",
      "The ratio of received carrier power to the user's data bit rate",
      "The ratio of the uplink carrier frequency to the downlink carrier frequency"]),

    ("A satellite link budget is fundamentally used to:",
     "Predict whether the received signal will be strong enough relative to the noise",
     ["Schedule the optimal launch window for the satellite's rocket vehicle",
      "Allocate telephone numbers and IP addresses to individual subscriber devices",
      "Determine the orbital inclination the satellite should maintain over its lifetime"]),

    ("Noise power spectral density N0 is defined as:",
     "The product of the Boltzmann constant k and the system noise temperature T",
     ["The antenna receive gain divided by the physical system temperature in kelvin",
      "The transmitted EIRP minus the total free-space path loss along the link",
      "The received carrier power multiplied by the transmitted bit rate"]),

    ("Which of the following is a link (propagation) loss accounted for in a satellite link "
     "budget?",
     "Free-space path loss together with rain/atmospheric attenuation",
     ["The Boltzmann constant used in the receiver's noise-temperature calculation",
      "The EIRP radiated by the transmitting ground station or satellite",
      "The total number of active transponders carried onboard the satellite"]),

    ("In 5G NR, Frequency Range 1 (FR1) spans approximately:",
     "410 MHz to 7.125 GHz, the FR1 sub-6 GHz range",
     ["24 to 52 GHz, part of the FR2 mmWave range",
      "50 to 66 GHz, part of the FR2 upper mmWave extension",
      "Below 100 MHz, in the HF/VHF broadcast range"]),

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
     ["Remains fixed at 15 kHz for a typical sub-6 GHz 5G NR deployment",
      "Decreases steadily as the numerology index u increases in value",
      "Depends primarily on the carrier frequency band rather than the numerology"]),

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
     "Polar coding for control channels and LDPC coding for data channels",
     ["Convolutional coding and Reed-Solomon coding, inherited unchanged from earlier standards",
      "Turbo coding, carried over unchanged from the LTE physical layer",
      "No dedicated channel coding scheme, relying purely on modulation for robustness"]),
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
