#!/usr/bin/env python3
"""
Build the Satellite Communication & NTN (TE 456) MCQ bank — Part 2.

Source material (same slide decks as Part 1):
  - TE456-NTN-What&Why.pdf
  - TE456-NTN-Overview-1.pdf
  - TE456-5GNR-NTN-2026-complete.pdf
  - TE456-Elements-SatCom5GSystems-2026-Complete.pdf

Each question is (question_text, correct_answer, [distractor, distractor, distractor]).
Output JSON: compiled_2.json
"""
import json
import random

# ---------------------------------------------------------------------------
# GROUP E - NTN Fundamentals (Part 2)
# ---------------------------------------------------------------------------
GROUP_E = [
    ("Which frequency band is most commonly used for mobile satellite phone handsets because "
     "it penetrates foliage well and suffers relatively little atmospheric attenuation?",
     "L-band (approximately 1–2 GHz), which penetrates foliage and has low atmospheric attenuation",
     ["Ka-band (26.5–40 GHz), which suffers severe rain fade and requires precise antenna pointing",
      "V-band (40–75 GHz), which is heavily absorbed by atmospheric oxygen over long paths",
      "mmWave FR2 (24–52 GHz), shared with terrestrial 5G small-cell deployments"]),

    ("NTN is particularly well-suited for narrowband IoT (NB-IoT) deployments primarily "
     "because:",
     "IoT devices are often in remote areas without terrestrial coverage, and their low data-rate requirements are compatible with satellite link constraints",
     ["IoT devices typically require very high sustained bandwidth and continuous connectivity that broadband trunk satellite links, not NB-IoT waveforms, are built to provide",
      "NTN reuses a dedicated satellite IoT protocol stack that was developed independently of 3GPP NB-IoT and cannot interoperate with terrestrial networks",
      "IoT device battery capacity is too limited to survive the long acquisition and synchronisation time needed to access a GEO satellite link"]),

    ("The Starlink constellation by SpaceX provides broadband primarily from which orbital "
     "shell?",
     "LEO at around 550 km, using thousands of small satellites for global broadband coverage",
     ["GEO at 35,786 km, using a handful of large geostationary satellites over the equator",
      "MEO at 20,200 km, mirroring the GPS navigation satellite constellation altitude",
      "HAPS at roughly 20 km altitude, using stratospheric balloons or solar aircraft"]),

    ("The Iridium system is notable for using inter-satellite links (ISLs) and for being "
     "able to route calls between satellites without a ground gateway underneath every "
     "satellite. Its constellation consists of:",
     "66 LEO satellites in polar orbit, providing near-global coverage including the poles",
     ["3 GEO satellites positioned over the equator, leaving the polar regions without coverage",
      "24 MEO satellites at GPS-like altitude, relying on a ground gateway for each individual call",
      "Thousands of HAPS platforms in the stratosphere, each covering a small local area"]),

    ("3GPP Release 17 is significant to NTN because it:",
     "Introduced the first standardised 5G NR enhancements specifically for satellite access, including timing and Doppler adaptations",
     ["Defined the baseline 5G NR air interface itself, which did not yet include any satellite-specific provisions",
      "Was the release that shelved the NTN study item proposed earlier, postponing satellite work indefinitely to a much later, unscheduled 3GPP release",
      "Focused mainly on mmWave terrestrial small-cell enhancements, with satellite access left for a future release"]),

    ("Direct-to-Device (D2X) satellite services, which allow an unmodified smartphone to "
     "communicate via satellite, are enabled primarily by:",
     "New 3GPP NTN specifications that extend 5G NR for low-power handheld UEs accessing satellites directly",
     ["Proprietary satellite handsets sold directly by satellite operators, built years before 3GPP NTN specifications existed",
      "Special hardware modules fitted at the factory that operate outside the scope of the 3GPP standard",
      "A terrestrial base station relocated near the satellite ground track to relay signals to unmodified handsets"]),

    ("A key advantage of NTN as a complement to terrestrial networks is that during large "
     "public events or disasters, NTN can:",
     "Offload or supplement congested terrestrial cells, providing capacity relief and backup connectivity",
     ["Take over as the primary network indefinitely once terrestrial capacity is exceeded, retiring the terrestrial cells",
      "Deliver lower round-trip latency than a terrestrial macro cell, thanks to its wide beam footprint",
      "Operate on the same spectrum as the terrestrial network without any coordination or interference management"]),

    ("As satellite altitude increases, the coverage footprint of a single satellite:",
     "Increases, but at the cost of longer propagation delay and higher free-space path loss",
     ["Decreases, because higher satellites must lower transmit power to stay within regulatory EIRP limits",
      "Stays roughly the same across most altitudes, since footprint size is assumed to be set by the antenna beamwidth alone",
      "Increases in proportion to altitude, while propagation delay stays fixed because delay is assumed to depend on frequency alone"]),

    ("In the 6G vision, NTN is regarded as:",
     "A native component providing the 'coverage everywhere' pillar alongside terrestrial networks",
     ["A stop-gap technology expected to be retired once dense urban 6G small-cell deployment is complete",
      "A backhaul transport layer reserved for connecting gNBs, with no role in direct user access",
      "A legacy 4G capability being phased out as networks migrate fully to 5G and 6G"]),

    ("In a LEO NTN system, a UE may experience two types of handover: satellite-to-satellite "
     "(inter-satellite) and beam-to-beam within the same satellite (inter-beam). Both require:",
     "Mobility management procedures adapted to the rapidly changing satellite geometry",
     ["Minimal signalling, since onboard satellite processing tracks each UE's position without network involvement",
      "Procedures borrowed directly from GEO systems, since LEO and GEO share an identical mobility standard",
      "A physical reconnection of the UE's antenna cable to a different ground gateway station"]),

    ("Compared with GEO, LEO satellites offer lower latency because:",
     "Their altitude is roughly 550–1,500 km vs 35,786 km for GEO, greatly reducing one-way propagation delay",
     ["LEO satellites transmit at substantially higher power than GEO satellites, shortening the effective signal travel time",
      "LEO satellites operate at a higher carrier frequency than GEO, and higher frequencies inherently propagate faster",
      "LEO satellites are physically smaller and lighter than GEO satellites, which lets their signals travel faster through space"]),

    ("Satellite link power limitation arises primarily because:",
     "The satellite's transmit power is constrained by the solar panel area and mass budget available in orbit",
     ["International spectrum regulations cap satellite EIRP at fixed limits regardless of the satellite's solar array size",
      "The ground terminal, not the satellite payload, sets the transmit power level via remote command",
      "Increasing transmit power tends to degrade signal quality because it drives the amplifier into saturation"]),

    ("The large round-trip time of a GEO satellite link causes problems for the TCP "
     "protocol because:",
     "The TCP congestion window fills slowly, capping throughput unless a Performance-Enhancing Proxy (PEP) or TCP optimisation is used",
     ["TCP's slow-start mechanism ignores propagation delay by design, so GEO's RTT has no measurable effect on throughput",
      "A large RTT causes the TCP congestion window to grow faster, which increases throughput on long-delay GEO links",
      "TCP's original design assumed satellite-scale delays, so it performs noticeably better over GEO than over short terrestrial paths"]),

    ("Spot beams in a satellite system concentrate transmit power onto a smaller geographic "
     "area in order to:",
     "Increase the power spectral density within each beam and enable frequency reuse across spatially separated beams",
     ["Lower the satellite's overall power consumption by shutting down amplifiers between transmissions",
      "Illuminate the satellite's entire visible Earth disc simultaneously from one wide antenna element",
      "Remove any need for frequency coordination between beams, since adjacent spot beams are assumed not to share the same frequency"]),

    ("3GPP defines two categories of NTN UE based on their ability to assist Doppler and "
     "timing compensation. These are:",
     "GNSS-capable UEs (which pre-compensate using their own position and ephemeris) and non-GNSS UEs (which rely on network assistance)",
     ["Voice-oriented UEs and data-oriented UEs, categorised by the type of traffic they primarily carry",
      "Fixed UEs mounted at a stationary location and mobile UEs that move during a session",
      "Transparent UEs that simply relay bent-pipe signals without processing and regenerative UEs that perform onboard demodulation and remodulation"]),

    ("Satellite spectrum coordination at the international level is managed primarily "
     "through:",
     "ITU Radio Regulations, bilateral and multilateral agreements between administrations",
     ["WTO Basic Telecommunications Agreement tariff schedules, which govern market access rather than spectrum use",
      "UN Security Council resolutions, which address international security matters rather than spectrum allocation",
      "The 3GPP technical specification process, which standardises air-interface protocols rather than allocating spectrum"]),

    ("In a bent-pipe (transparent) transponder, noise accumulated on the uplink is:",
     "Amplified and retransmitted alongside the signal, degrading the overall downlink carrier-to-noise ratio",
     ["Filtered out to a negligible level by the low-noise amplifier before the signal is retransmitted",
      "Present mainly on the downlink hop, since the uplink path is assumed to be effectively noise-free",
      "Removed by the frequency-conversion stage, which is assumed to strip noise along with shifting the carrier"]),

    ("Ephemeris data used by NTN UEs describes:",
     "The predicted position and velocity of the satellite over time, enabling the UE to compute Doppler shift and propagation delay",
     ["The satellite's onboard power budget, tracking how much energy remains in the batteries and solar arrays",
      "The list of operators licensed to access the satellite's transponders under its regulatory authorisation, renewed on a periodic basis",
      "The current software and firmware version running on the satellite's onboard payload processor"]),

    ("GNSS assists NTN UEs primarily by providing:",
     "Accurate UE position, which combined with satellite ephemeris allows the UE to pre-compensate Doppler shift and timing advance",
     ["An alternative service link that substitutes for the satellite connection when visibility to the NTN satellite is poor",
      "A supply of electrical power to the UE's radio front-end, similar to wireless charging",
      "A direct data path into the 5G core network, bypassing the NTN satellite and gNB radio path altogether"]),

    ("Maritime vessels in open ocean beyond terrestrial coastal coverage rely on NTN for:",
     "Broadband internet, voice, safety and vessel-tracking services",
     ["VHF terrestrial radio connections to land-based towers, which work solely within sight of the coastline",
      "Fibre-optic undersea cable connections spliced directly into the vessel's onboard equipment",
      "Microwave line-of-sight radio links relayed ship-to-ship until a coastal station is reached"]),

    ("In-flight connectivity (IFC) for commercial aircraft is provided by NTN because:",
     "Aircraft at cruise altitude are beyond the range of terrestrial networks, requiring satellite links for passenger and cockpit communications",
     ["Aviation regulations require commercial aircraft to rely solely on terrestrial cellular towers for connectivity",
      "Aircraft fuselage-mounted antennas are physically incompatible with the frequency bands used by NTN satellites, requiring a redesigned antenna array",
      "In-flight connectivity is delivered over long-range HF radio links rather than through satellite transponders"]),

    ("Circular polarization is preferred over linear polarization for mobile satellite "
     "terminals because:",
     "The received signal polarization is independent of the terminal's physical orientation, simplifying the antenna design",
     ["Circular polarization experiences measurably less rain attenuation than linear polarization at the same frequency",
      "Linear polarization signals cannot be picked up by the feed horns used in typical satellite antennas",
      "Circular polarization antennas achieve inherently higher peak gain than equivalent linear polarization antennas"]),

    ("The OneWeb LEO constellation differs from Starlink in that OneWeb focuses on:",
     "Providing broadband connectivity through a wholesale/B2B model, selling capacity to telecom operators rather than directly to consumers",
     ["Launching a fleet of GEO broadcast satellites aimed directly at consumer television subscribers",
      "Operating a Ka-band constellation reserved for military and government customers under contracts that exclude any commercial retail service",
      "Relying purely on bent-pipe payloads with no onboard IP routing, unlike Starlink's processed payloads"]),

    ("A Performance-Enhancing Proxy (PEP) on a satellite gateway improves TCP throughput "
     "by:",
     "Splitting the TCP connection into a terrestrial segment and a satellite segment, hiding the large satellite RTT from the end-to-end TCP feedback loop",
     ["Boosting the satellite's transmit power whenever congestion is detected, so packets arrive before timers expire",
      "Replacing standard TCP with a proprietary transport protocol running solely on the UE, leaving the server unmodified",
      "Cutting the number of acknowledgement packets the server generates, though this does nothing to shorten the underlying satellite propagation delay"]),

    ("Which NTN platform offers the most rapid deployment and easiest recovery after "
     "failure, but is most limited by weather and flight regulations?",
     "Unmanned Aircraft System (UAS/drone) used as an airborne NTN node",
     ["GEO satellite, which ground controllers can reposition to a new orbital slot within a few hours",
      "LEO satellite, which operators can temporarily lower to an altitude of about 50 km on demand",
      "HAPS balloon, which stays fully stable and unaffected by strong upper-atmosphere winds"]),
]

# ---------------------------------------------------------------------------
# GROUP F - Orbits & Propagation (Part 2)
# ---------------------------------------------------------------------------
GROUP_F = [
    ("Free-space path loss (FSPL) increases with distance and frequency according to "
     "FSPL(dB) = 20 log(d) + 20 log(f) + constant. A doubling of the carrier frequency "
     "therefore increases FSPL by approximately:",
     "6 dB",
     ["3 dB",
      "10 dB",
      "0 dB — frequency has no effect on free-space path loss"]),

    ("Rain attenuation is most severe at which frequency range?",
     "Above approximately 10 GHz (Ku, Ka and higher bands), where raindrops are comparable in size to the signal wavelength",
     ["Below 2 GHz (L-band), where the wavelength is much larger than a raindrop and scattering is negligible",
      "At optical and infrared wavelengths, where clouds absorb light heavily but microwave links pass through unaffected",
      "Between 400 and 700 MHz (UHF), a band where atmospheric water vapour absorption happens to peak"]),

    ("A satellite orbit's inclination is defined as:",
     "The angle between the orbital plane and the Earth's equatorial plane; 0° is equatorial (GEO), 90° is polar",
     ["The satellite's altitude above mean sea level, measured at the point directly below the spacecraft",
      "The eccentricity of the orbital ellipse, describing how stretched the orbit is compared with a perfect circle",
      "The angle between the satellite's antenna boresight and the local Earth surface tangent"]),

    ("A sun-synchronous orbit is used by Earth-observation satellites because:",
     "The orbital plane precesses at the same rate as the Earth's revolution around the Sun, keeping the local solar illumination time constant over each pass",
     ["The satellite actually orbits the Sun directly rather than the Earth, giving it continuous solar exposure",
      "The satellite remains fixed above the same point on the Earth's surface continuously, like a geostationary satellite in an equatorial orbit",
      "The satellite's solar panels are mechanically fixed perpendicular to the Sun for the entire mission by orbit design alone"]),

    ("The Van Allen radiation belts are a concern for satellite designers because:",
     "They are zones of trapped high-energy charged particles that can degrade semiconductor electronics and solar cells",
     ["They are regions of charged dust that cause rain-like attenuation on Ku-band downlink signals",
      "They form a shielding layer that blocks most radio transmissions from reaching geostationary altitude",
      "They are dense cloud layers in the upper troposphere that scatter and absorb microwave signals"]),

    ("The ionosphere (roughly 60–1,000 km altitude) affects satellite radio signals primarily "
     "by causing:",
     "Propagation delay, Faraday rotation of polarization, and signal dispersion, particularly at frequencies below about 3 GHz",
     ["Rain fade and tropospheric scintillation, effects that actually occur above about 10 GHz in the lower troposphere",
      "Inter-symbol interference caused by multipath reflections off buildings near the ground terminal",
      "An increase in thermal noise generated internally within the satellite's low-noise amplifier stage"]),

    ("Tropospheric scintillation is a rapid fluctuation of received signal amplitude and phase "
     "caused by turbulence in the lower atmosphere. It is most significant at:",
     "Low elevation angles and frequencies above about 10 GHz",
     ["High elevation angles and low frequencies below 1 GHz, where the atmospheric path is shortest",
      "A broad range of elevation angles and frequencies about equally, since turbulence is assumed uniform throughout the troposphere",
      "Polar latitudes specifically, where the troposphere is thinner and turbulence is assumed weaker"]),

    ("The Doppler frequency shift experienced by a ground receiver tracking a LEO satellite "
     "depends primarily on:",
     "The radial component of the satellite's velocity relative to the receiver, and the carrier frequency",
     ["The satellite's altitude alone, since Doppler shift is assumed to depend on height rather than relative velocity",
      "The carrier frequency alone, treating the satellite's motion as having no bearing on the observed shift",
      "The signal's polarization state rather than the relative geometry between satellite and ground receiver"]),

    ("A GEO satellite produces negligible Doppler shift for a stationary ground terminal "
     "because:",
     "Both the satellite and the terminal are effectively stationary relative to each other — the satellite's angular velocity matches the Earth's rotation",
     ["GEO satellites orbit slowly enough that their absolute velocity, not their relative velocity to the ground, is assumed to be effectively zero in a typical mission scenario",
      "Doppler shift is actively cancelled inside the transponder's frequency-conversion stage before retransmission",
      "GEO satellites broadcast a dedicated pilot tone that ground receivers use to null out any residual Doppler shift"]),

    ("The elevation angle of a satellite as seen from a ground station determines:",
     "The length of the signal path through the atmosphere; higher elevation means a shorter atmospheric path and less attenuation",
     ["The satellite's orbital altitude above mean sea level, independent of the ground station's location",
      "The satellite's velocity relative to the ground station, which sets the Doppler shift rather than the path length",
      "The total number of other satellites simultaneously visible in the sky from that ground station"]),

    ("Link margin in a satellite system is defined as:",
     "The excess of received Eb/N0 (or C/N0) above the minimum threshold required for the specified bit-error rate",
     ["The physical diameter of the satellite's main reflector antenna, which sets gain but is not itself a margin figure",
      "The maximum data rate the link is permitted to carry under the operator's spectrum licence",
      "The ratio of transmit power to receive power measured at the ground station's demodulator input"]),

    ("During equinox periods, GEO satellites experience solar eclipses lasting up to about:",
     "72 minutes per day, during which the satellite relies on onboard batteries",
     ["12 hours per day, on the assumption that the satellite sits behind the Earth for the entire local night",
      "Under 1 minute per day, treating the Earth's shadow at GEO altitude as extremely narrow",
      "GEO satellites are assumed to avoid eclipse because their equatorial orbital plane is thought to keep them continuously in sunlight"]),

    ("Frequency reuse in a multi-beam satellite system increases overall system capacity "
     "because:",
     "The same frequency band is reused across spatially separated beams, multiplying the total traffic the satellite can carry",
     ["Each beam is assigned a distinct frequency, so reuse merely describes the repeating pattern of the spectrum plan",
      "Frequency reuse is assumed to reduce co-channel interference to a negligible, effectively zero level",
      "Total system capacity is fixed by the number of beams alone, irrespective of how frequencies are reused among them"]),

    ("When the same frequency is used in adjacent satellite beams (co-channel reuse), "
     "co-channel interference (CCI) is controlled by:",
     "Sufficient beam spacing and antenna sidelobe suppression to keep the interfering signal below acceptable levels",
     ["Raising the carrier frequency progressively until the coverage of adjacent beams no longer geometrically overlaps",
      "Assigning a distinct polarization to each individual beam across the whole satellite footprint",
      "Forcing each pair of adjacent beams to transmit at precisely matched power levels regardless of traffic load"]),

    ("By Kepler's third law, the orbital period of a satellite is proportional to the "
     "cube root of the cube of the semi-major axis (T² ∝ a³). This means:",
     "Higher orbits have longer periods and lower orbital speeds than lower orbits",
     ["Higher orbits have shorter orbital periods and correspondingly higher orbital speeds than lower orbits",
      "The orbital period stays roughly constant across most altitudes, since Kepler's law is assumed to depend on eccentricity rather than altitude",
      "The orbital period depends primarily on the satellite's own mass rather than on its distance from Earth"]),

    ("GEO satellites have poor coverage poleward of approximately ±75° latitude because:",
     "They orbit in the equatorial plane, so the elevation angle seen from high latitudes is very low, below the horizon or near it",
     ["The Van Allen radiation belts are assumed to block radio propagation specifically over the polar regions",
      "International spectrum regulations are assumed to prohibit GEO satellite transmissions above 75° latitude",
      "Ionospheric absorption near the poles is assumed to be so severe that essentially no signal reaches the ground"]),

    ("A Molniya orbit is a highly elliptical orbit (HEO) with an inclination of about "
     "63.4° and a 12-hour period. Its primary purpose is to:",
     "Provide long-dwell coverage of high-latitude regions (such as Russia) where GEO elevation angles are too low",
     ["Provide a geostationary-like fixed view of the equatorial belt, much as a standard GEO satellite would",
      "Achieve the shortest possible propagation delay for users near the Arctic Circle, shorter than any LEO system",
      "Allow a satellite to cross the equatorial plane several times each day while remaining at a fixed inclination"]),

    ("The Iridium constellation routes calls via inter-satellite links (ISLs), which means:",
     "Calls between any two points on Earth can be routed entirely through the satellite network without requiring a ground gateway in between",
     ["Each call must still be relayed through a dedicated ground gateway at each satellite-to-satellite hop it passes through",
      "Iridium's inter-satellite links are reserved for housekeeping telemetry, and subscriber voice traffic must instead route through gateways",
      "Iridium's inter-satellite links operate in the optical band, a medium not capable of carrying real-time voice traffic"]),

    ("The ITU-R rain zone classification system (zones A to Q) is used to:",
     "Estimate the rain attenuation statistics for a given geographic location and design satellite link margins accordingly",
     ["Set the maximum allowable satellite transmit power permitted within each geographic rain zone",
      "Classify which geostationary orbital slots are available for satellites registered under each rain zone administration",
      "Define which frequency bands are allocated to different satellite services within each rain zone"]),

    ("A multi-beam satellite antenna produces higher gain per beam than a global beam "
     "antenna. The trade-off is that:",
     "Each beam covers a smaller geographic area, requiring more beams to achieve the same total coverage",
     ["Each individual beam consumes disproportionately more onboard power, which actually reduces the satellite's total capacity",
      "Multi-beam antennas are structurally unable to reuse the same frequency band across different beams",
      "Achieving higher gain per beam inherently lowers the overall throughput the whole satellite system can deliver"]),

    ("The geosynchronous orbit is the set of all orbits with a 24-hour period, while the "
     "geostationary orbit (GEO) is a subset defined by:",
     "Zero inclination (equatorial plane) and zero eccentricity (circular orbit), resulting in a fixed position above the equator",
     ["A highly elliptical orbit inclined at 63.4°, the same geometry used by Molniya-type satellites",
      "Any polar orbit that happens to complete one revolution each 24-hour period, regardless of eccentricity",
      "An orbital inclination of exactly 28.5°, matching the latitude of major equatorial launch sites such as Cape Canaveral"]),

    ("Satellite eclipse occurs when the Earth's shadow blocks sunlight from reaching the "
     "satellite. During eclipse, the satellite continues operating because:",
     "Onboard batteries are charged during sunlit periods and supply power during eclipse",
     ["Solar panels are assumed to store energy chemically within themselves, removing any need for separate batteries",
      "A backup radioisotope power unit is assumed to switch on once eclipse begins, without needing stored battery charge",
      "The satellite shuts its payload power down to zero during eclipse and simply waits for sunlight to return"]),

    ("The figure of merit G/T of a satellite receiver system improves (increases) when:",
     "Antenna receive gain G increases or system noise temperature T decreases",
     ["Path loss along the link increases, which is unrelated to the receiver's own gain-to-noise-temperature figure",
      "The transmitting station's EIRP decreases, a transmit-side parameter that does not enter the G/T figure",
      "The carrier frequency is lowered while the antenna gain G and noise temperature T are both held fixed"]),

    ("In the link budget of a satellite system, the overall end-to-end performance is "
     "determined by:",
     "The weaker of the uplink and downlink, since the total signal-to-noise ratio is dominated by the noisier hop",
     ["The direct sum of the uplink and downlink C/N ratios once both are converted to linear scale",
      "The uplink alone, on the assumption that the satellite's transponder amplifies the downlink without adding any noise",
      "The downlink alone, on the assumption that the uplink carries a comfortable margin in most practical link designs"]),

    ("Polarization diversity allows a satellite to reuse the same frequency band twice by "
     "transmitting two independent signals using:",
     "Orthogonal polarizations (e.g., horizontal and vertical linear, or RHCP and LHCP circular)",
     ["Two separate carrier frequencies transmitted using the same single polarization",
      "Two copies of the identical signal transmitted with a 90-degree phase offset rather than orthogonal polarization",
      "Two separate antennas physically pointed at two different geographic coverage areas"]),
]

# ---------------------------------------------------------------------------
# GROUP G - 5G NR-NTN: Key Procedures & Enhancements
# ---------------------------------------------------------------------------
GROUP_G = [
    ("3GPP Release 17 introduced the first NTN-specific 5G NR enhancements, which "
     "included adaptations to timing advance, Doppler compensation and:",
     "HARQ process design to handle the long satellite round-trip time",
     ["Removal of the standard OFDM waveform, replaced by a bespoke satellite-specific modulation scheme",
      "Allocation of a brand-new dedicated NTN frequency band located below 100 MHz",
      "Replacement of the standard 5G core network with a separate satellite-specific core architecture"]),

    ("In NTN, an extended Timing Advance (TA) mechanism is required because:",
     "Propagation delays of tens to hundreds of milliseconds must be pre-compensated so that uplink transmissions arrive at the gNB within the correct slot boundary",
     ["The satellite's onboard clock is assumed to run measurably faster than the ground station's reference clock",
      "Timing advance is applied to delay the downlink signal so that it matches the user's ground location",
      "Timing advance is needed solely for stationary UEs and is switched off the moment a UE begins moving, unlike the fixed procedure used in terrestrial NR"]),

    ("The PRACH (Physical Random Access Channel) preamble design is modified for NTN by:",
     "Extending the preamble length and guard period to accommodate the large round-trip propagation delay, preventing preamble collisions",
     ["Shortening the preamble and guard period to cut overhead, on the assumption that a shorter window suits long delays",
      "Replacing the Zadoff-Chu preamble sequence with a CDMA spreading code borrowed from 3G systems",
      "Moving the PRACH transmission to the downlink direction, where the gNB rather than the UE originates it"]),

    ("The fundamental problem HARQ faces in a GEO NTN system is that:",
     "The 500+ ms RTT means the transmitter must buffer many HARQ processes simultaneously, far exceeding the 8-ms terrestrial HARQ round-trip budget",
     ["HARQ acknowledgements are individually encrypted, and the added decryption step is what causes the delay",
      "HARQ retransmissions are assumed to travel back to the UE faster than the original transmission did",
      "The round-trip time over a GEO link is assumed to match the roughly 8-ms terrestrial NR RTT, leaving HARQ buffering requirements unaffected"]),

    ("For GEO NTN, 3GPP permits HARQ to be disabled. When HARQ feedback is turned off, "
     "residual errors are handled by:",
     "Outer-layer error recovery mechanisms such as RLC ARQ or application-layer FEC",
     ["The satellite's onboard processor, which is assumed to correct bit errors itself before relaying the signal",
      "Progressively increasing the UE's transmit power until the error rate is driven down to nothing",
      "A fixed rule that repeats each transmission exactly twice, independent of whether an error actually occurred"]),

    ("As a LEO satellite moves, beam management in NTN must handle:",
     "Beam sweeping, beam measurement reporting, and beam failure recovery adapted to the satellite's high angular velocity relative to the ground",
     ["Static beam assignments that stay fixed for the duration of a session, regardless of satellite motion",
      "Uplink beam management alone, on the assumption that the downlink beam remains optimal without adjustment",
      "Beam management procedures carried over unchanged from terrestrial massive-MIMO base stations, which assume a fixed antenna array location"]),

    ("In a LEO NTN with Earth-moving beams, the cell associated with a given geographic "
     "area changes as the satellite passes overhead. 3GPP addresses this by:",
     "Distinguishing between Earth-fixed and Earth-moving cell identities, and adapting cell re-selection and handover procedures accordingly",
     ["Assigning a fixed, permanent cell identity to each geographic point on Earth, independent of which satellite passes overhead",
      "Requiring the UE to fall back temporarily to a terrestrial network during each cell transition",
      "Removing the cell concept from NTN altogether and replacing it with continuous satellite-based tracking"]),

    ("Conditional Handover (CHO) is particularly beneficial in NTN because:",
     "The network can prepare the target cell in advance and trigger execution automatically when conditions are met, avoiding added signalling latency on a long-RTT link",
     ["Conditional handover is assumed to require a very short RTT, which would actually suit GEO rather than LEO",
      "Conditional handover is prohibited under NTN specifications, which instead rely on fast re-registration procedures",
      "Conditional handover applies solely to UEs that are physically moving on the ground, and offers no benefit against satellite-induced signalling latency"]),

    ("The primary frequency bands targeted by 3GPP NR-NTN specifications for the service "
     "link (UE-to-satellite) are:",
     "S-band (around 2 GHz) and Ka-band (around 26 GHz)",
     ["mmWave FR2 bands (24–52 GHz) shared directly with terrestrial 5G small cells",
      "HF bands (3–30 MHz), chosen for their long-range ionospheric propagation characteristics",
      "The same Ku-band frequencies used for the satellite's feeder link to the ground gateway"]),

    ("Inter-satellite links (ISLs) are most naturally associated with the regenerative "
     "payload architecture because:",
     "A regenerative satellite can route and forward data packets, making it practical to relay traffic between satellites toward a distant gateway",
     ["Bent-pipe payloads are assumed to support inter-satellite links natively, since they need essentially no onboard signal processing",
      "Inter-satellite links are assumed to require the transparent frequency conversion stage that bent-pipe payloads are specifically built to provide",
      "ITU regulations are assumed to prohibit inter-satellite links between satellites carrying regenerative payloads"]),

    ("In the RLC layer, the NTN large RTT creates an issue analogous to the TCP window "
     "problem, because:",
     "The RLC ARQ window may need to be enlarged to allow enough outstanding unacknowledged PDUs so that throughput is not stalled waiting for acknowledgements",
     ["RLC ARQ is switched off for NTN links, which removes any window-size constraint from the resulting throughput calculation",
      "The RLC window size is assumed to have no bearing on achievable throughput, regardless of the link's RTT",
      "The RLC sublayer itself was removed from the NTN protocol stack as part of the Release 17 specifications"]),

    ("In LEO NTN, paging areas tend to be larger than in terrestrial networks because:",
     "Satellite footprints cover vast geographic areas, and using large paging areas reduces the frequency of tracking area updates as the satellite moves",
     ["LEO satellites are assumed to have limited onboard resources, capping the number of UEs that can be paged at once",
      "Larger paging areas are assumed to reduce the total data volume that needs to be transmitted to each UE",
      "Paging in NTN uses procedures and area sizes carried over unchanged from terrestrial 5G networks, ignoring the satellite footprint size"]),

    ("Open-loop power control is preferred over closed-loop power control for NTN uplinks "
     "because:",
     "The long RTT makes it impractical to rely on fast gNB feedback to adjust UE transmit power in near real-time",
     ["Closed-loop control is assumed to be more accurate but to demand extra dedicated hardware inside the UE",
      "Open-loop control is assumed to rely on gNB feedback that arrives within about 1 millisecond, like terrestrial NR",
      "3GPP specifications are assumed to mandate closed-loop power control as the default for NTN uplink transmissions"]),

    ("eMBB (enhanced Mobile BroadBand) services over LEO NTN are achievable, but their "
     "throughput is typically lower than terrestrial 5G because of:",
     "Large free-space path loss and the constrained transmit power of the satellite, limiting link capacity",
     ["LEO NTN relying on a fundamentally different air-interface waveform that is incompatible with standard eMBB service",
      "3GPP specifications explicitly prohibiting the delivery of eMBB services over NTN in Release 17",
      "eMBB service being defined as requiring sub-millisecond latency, a target no NTN satellite link can realistically reach"]),

    ("URLLC (Ultra-Reliable Low-Latency Communication) requirements cannot be met by GEO "
     "NTN primarily because:",
     "GEO round-trip delay (~600 ms) far exceeds the sub-millisecond latency target of URLLC",
     ["GEO satellites lack sufficient transmit power to carry the data rates URLLC services typically demand",
      "URLLC is defined solely as a terrestrial 5G feature and is formally excluded from the NTN specifications",
      "GEO NTN mandates the use of HARQ retransmission, a mechanism assumed to be fundamentally incompatible with URLLC"]),

    ("Larger subcarrier spacing (higher numerology) in 5G NR is more robust against "
     "Doppler-induced inter-carrier interference in NTN because:",
     "A wider subcarrier spacing means the Doppler shift is a smaller fraction of the subcarrier bandwidth, reducing ICI",
     ["Larger subcarrier spacing shortens the OFDM symbol duration, which is assumed to give the channel more time to change within a symbol",
      "Lower numerology, meaning smaller subcarrier spacing, is assumed to be the generally preferred configuration for NTN links",
      "Doppler shift is assumed to be unrelated to subcarrier spacing in any OFDM-based system"]),

    ("Gateway diversity in NTN means:",
     "Multiple geographically separated gateways can serve the same satellite, so if one suffers rain fade the satellite can switch to a clear-sky gateway automatically",
     ["Deploying multiple satellites to serve a single ground gateway simultaneously, rather than diversifying the gateway sites themselves geographically",
      "Installing redundant user terminals at each individual subscriber site to guard against local outages",
      "Routing gateway traffic through two fully separate 5G core network instances for redundancy"]),

    ("Ka-band is attractive for high-throughput satellite (HTS) systems because:",
     "Wide available bandwidths (~500 MHz or more per polarization) enable high throughput, despite more severe rain attenuation and stricter antenna pointing requirements than L- or S-band",
     ["Ka-band signals are assumed to be largely unaffected by rain, which would make the band especially well suited to tropical deployments",
      "Ka-band is assumed to offer narrower channel bandwidths than L-band, which would make it more spectrally efficient",
      "Ka-band spectrum is assumed to be reserved solely for military satellite communications, excluding commercial use"]),

    ("NTN is well-suited for massive Machine-Type Communications (mMTC) IoT primarily "
     "because:",
     "IoT sensors are often deployed in remote or unpowered locations without terrestrial coverage, and their low data-rate and infrequent transmission requirements suit satellite capacity constraints",
     ["IoT sensors are assumed to demand ultra-high bandwidth that solely satellite trunk links are capable of supplying",
      "mMTC is assumed to require sub-millisecond latency, a target that specifically low-altitude LEO satellites are said to reliably reach",
      "IoT devices are assumed to be unable to connect to any satellite because they lack an onboard GNSS receiver"]),

    ("When a UE moves between satellite beams or between satellites, 5G session continuity "
     "mechanisms ensure:",
     "PDU sessions are maintained without application-level disruption, through UPF selection and session anchor management in the 5G core",
     ["PDU sessions are fully terminated and re-established from scratch each time the UE changes satellite or beam",
      "Session continuity is managed solely by the UE's own software, without any coordination from the 5G core network",
      "Session continuity mechanisms are assumed to cover voice calls specifically, while data sessions are simply dropped"]),

    ("A GNSS-capable NTN UE uses its own position and satellite ephemeris to:",
     "Pre-compute the uplink frequency offset and timing advance needed to compensate for Doppler shift and propagation delay before transmitting",
     ["Authenticate itself directly with the satellite's onboard processor before being allowed to transmit",
      "Determine which 5G core network slice the UE should connect to for its intended service",
      "Request a handover to a terrestrial network whenever a GNSS fix becomes available, regardless of the current NTN link quality or signal strength"]),

    ("Timing pre-compensation in NTN requires the UE to:",
     "Advance its uplink transmission by an amount equal to the computed propagation delay to the satellite, so the signal arrives within the expected slot window",
     ["Delay, rather than advance, its uplink transmission to compensate for the satellite's forward orbital motion",
      "Request that the gNB shift the downlink timing by the propagation delay instead of adjusting its own uplink",
      "Transmit using a fixed timing offset of 0.5 ms that stays constant no matter how far away the satellite currently is in its orbit"]),

    ("Network slicing in 5G NTN allows different service types (broadband, IoT, emergency) "
     "to share the same NTN physical resources while maintaining:",
     "Independent quality of service, isolation and scheduling policies per slice",
     ["One shared QoS profile applied across each service type, chosen to simplify the network's overall management",
      "A dedicated physical satellite payload allocated separately to each individual network slice",
      "No meaningful service differentiation, with each slice receiving essentially identical scheduling treatment"]),

    ("5G NR reference signals (DMRS, CSI-RS, SRS) in NTN must be designed to account for:",
     "The large and time-varying delays of the NTN channel, requiring additional reference signal configurations for accurate channel estimation",
     ["The satellite channel's assumed complete absence of multipath, unlike dense urban terrestrial deployments",
      "The assumption that the NTN channel is perfectly static over time, meaning the standard terrestrial channel estimation approach applies unchanged",
      "A shorter OFDM symbol duration than terrestrial NR uses, intended to fit in more pilot reference symbols"]),

    ("The main factor limiting uplink throughput for direct-to-handset LEO NTN is:",
     "The constrained transmit power of handheld UEs (typically 23–26 dBm), which combined with the large path loss sets an upper bound on achievable uplink data rate",
     ["The downlink direction, which is assumed to be the bottleneck across most NTN system designs regardless of UE type",
      "Excessive UE transmit power that is assumed to spill over and cause interference with neighbouring satellite constellations sharing the band",
      "The lack of multi-antenna MIMO support at the handset, which is assumed to force it into single-antenna transmission mode"]),
]

# ---------------------------------------------------------------------------
# GROUP H - SatCom Systems & 5G Architecture (Part 2)
# ---------------------------------------------------------------------------
GROUP_H = [
    ("DVB-S2 (Digital Video Broadcasting — Satellite, Second Generation) is significant "
     "for satellite broadband because it:",
     "Employs Adaptive Coding and Modulation (ACM), dynamically selecting the modulation and coding scheme to maximise throughput under varying link conditions",
     ["Uses a fixed QPSK modulation scheme at a constant code rate, chosen deliberately to keep receiver design simple",
      "Is a 3GPP-defined standard, developed specifically as part of the 5G NR satellite access specifications",
      "Is fundamentally a terrestrial digital broadcast standard, unrelated in design to any of the DVB satellite broadcast specifications"]),

    ("DVB-RCS2 (Return Channel via Satellite, Second Generation) defines:",
     "The interactive return channel from the user terminal to the satellite, enabling two-way broadband satellite services",
     ["The forward broadcast link running from the satellite outward to each subscriber terminal in the coverage footprint",
      "The ITU standard governing how administrations coordinate geostationary orbital slot assignments",
      "The inter-satellite link protocol adopted by LEO constellations such as Iridium and Starlink"]),

    ("A VSAT (Very Small Aperture Terminal) system typically uses:",
     "Small dish antennas of 0.6–3.6 m diameter to provide satellite broadband at fixed or mobile sites, usually via GEO satellites in Ku or Ka band",
     ["Large parabolic dishes exceeding 10 metres in diameter, typically reserved for military ground stations and deep-space tracking facilities",
      "LEO satellite constellations alone, since VSAT terminals are assumed unable to link to any GEO satellite",
      "Phased-array antenna panels mounted on aircraft or balloons flying above 50 km altitude"]),

    ("In FDMA (Frequency Division Multiple Access) for satellite systems, a key "
     "disadvantage is:",
     "Spectrum is wasted when an assigned frequency sub-band is idle because its allocated user has no traffic to send",
     ["Each user is forced to transmit within the same shared time slot, which causes frequent collisions",
      "FDMA is assumed to require tighter synchronization than any other multiple-access scheme, including TDMA",
      "FDMA is assumed to be structurally incompatible with combining alongside TDMA on the same satellite transponder"]),

    ("Satellite TDMA (Time Division Multiple Access) requires tight time synchronization "
     "across all terminals because:",
     "Without synchronisation, bursts from different terminals will overlap in time at the satellite, causing interference",
     ["TDMA assigns a unique spreading code to each user, and synchronisation is what prevents those codes from colliding",
      "TDMA gives each terminal a separate carrier frequency, and timing synchronisation is what prevents frequency drift",
      "Synchronisation is required solely at the ground gateway, since individual user terminals need no separate timing reference of their own"]),

    ("In CDMA (Code Division Multiple Access), all users share the same bandwidth "
     "simultaneously and are separated by unique spreading codes. A critical operational "
     "requirement is:",
     "Accurate uplink power control, so that no single user's signal overpowers the others (the near-far problem)",
     ["That no two users are ever scheduled to transmit within the same time slot, as in TDMA",
      "That each user is instead assigned a dedicated separate frequency channel, as in FDMA",
      "That the spreading codes assigned to each user are regenerated on a fixed one-millisecond cycle"]),

    ("OFDMA (Orthogonal Frequency Division Multiple Access) is used in the 5G NR "
     "downlink because it:",
     "Allows flexible per-slot scheduling of subcarriers to different users, enabling efficient multi-user resource allocation",
     ["Assigns each user a unique CDMA-style spreading code rather than a set of frequency subcarriers",
      "Is essentially FDMA implemented with analogue carriers rather than digitally generated subcarriers",
      "Was originally designed for single-user point-to-point links and lacks any native support for multi-user scheduling decisions"]),

    ("DFT-spread OFDM (DFT-s-OFDM), also called SC-FDMA, is used in the 5G NR uplink "
     "rather than pure OFDMA because it:",
     "Achieves a lower Peak-to-Average Power Ratio (PAPR), which reduces power amplifier stress and is beneficial for power-constrained UE transmitters",
     ["Actually produces a higher peak-to-average power ratio than plain OFDM, which is assumed to suit power amplifiers better",
      "Is mandated specifically for satellite gNB transmitters while being formally prohibited across terrestrial gNB uplink deployments worldwide",
      "Spreads each user's data across fewer subcarriers than OFDMA, which is assumed to shrink the transmitted bandwidth"]),

    ("The Access and Mobility Management Function (AMF) in the 5G SA core is responsible "
     "for:",
     "UE registration, connection establishment and mobility management including handover decisions",
     ["Routing user-plane IP packets directly between the radio access network and the public internet",
      "Establishing, modifying and releasing PDU sessions along with allocating IP addresses to UEs",
      "Scheduling individual radio resource blocks on the air interface inside the gNB scheduler"]),

    ("The Session Management Function (SMF) in the 5G SA core is responsible for:",
     "Establishing, modifying and releasing PDU sessions and managing IP address allocation for UEs",
     ["Handling UE authentication and initial registration procedures with the 5G core network",
      "Performing physical-layer radio resource scheduling decisions inside the gNB itself",
      "Providing the physical NG interface connection that links the gNB to the 5G core network"]),

    ("The User Plane Function (UPF) in the 5G SA core is the:",
     "Data-plane anchor that handles packet routing and forwarding between the RAN and external data networks such as the internet",
     ["Control-plane function responsible for managing UE authentication and mobility registration procedures with the core network",
      "Radio access network node responsible for scheduling downlink transmissions over the air interface",
      "National spectrum management entity responsible for assigning frequency bands to individual operators"]),

    ("The NG interface in 5G connects the gNB to the 5G core network, with:",
     "NG-C (N2) carrying control-plane signalling to the AMF and NG-U (N3) carrying user-plane traffic to the UPF",
     ["NG-C (N2) carrying user-plane traffic while NG-U (N3) carries the control-plane signalling, the reverse of the actual split",
      "Both NG-C and NG-U providing a direct connection from the gNB straight out to the public internet",
      "The NG interface linking two neighbouring gNBs together for direct handover coordination"]),

    ("The Xn interface in 5G connects:",
     "Neighbouring gNBs to each other, enabling handover coordination, dual connectivity and interference management",
     ["The gNB directly to the 5G core network's AMF, duplicating the role of the NG-C interface",
      "The UE to the gNB over the Uu air interface, rather than a link between two network nodes",
      "The UPF to external data networks such as the internet, via the N6 reference point defined in the 5G core architecture"]),

    ("Phased-array antennas are used in LEO satellite user terminals because they:",
     "Electronically steer narrow beams toward the moving satellite without mechanical movement, enabling rapid tracking at low latency",
     ["Are generally cheaper to manufacture than an equivalent mechanically steered parabolic dish antenna",
      "Radiate omnidirectionally and therefore need essentially no beam steering or pointing mechanism toward the satellite",
      "Are restricted to stationary, fixed-site installations and cannot be mounted on moving vehicles or aircraft"]),

    ("Massive MIMO in 5G NR uses a large number of antenna elements at the gNB to:",
     "Form narrow, high-gain beams directed at individual UEs, greatly increasing spectral efficiency through spatial multiplexing",
     ["Deliberately reduce the antenna count compared with 4G LTE base stations, simplifying RF hardware",
      "Serve each UE within the cell from one single broad beam, which is assumed to simplify scheduling",
      "Operate solely at sub-1 GHz frequencies, where the comparatively large wavelength is assumed to better suit big antenna arrays"]),

    ("Null-steering in multi-beam satellite antennas suppresses interfering signals by:",
     "Placing deep nulls in the antenna radiation pattern in the direction of interferers while maintaining high gain toward intended users",
     ["Reducing the satellite's overall transmit power across each beam simultaneously to lower interference",
      "Assigning a distinct orthogonal frequency to each individual beam at the same time",
      "Physically rotating the satellite's attitude to point its beams away from interfering sources on the ground"]),

    ("Higher-order modulation (e.g., 64QAM vs QPSK) transmits more bits per symbol but "
     "requires a higher SNR. In satellite systems, higher-order modulation is used when:",
     "The link has a large margin above the minimum threshold, typically in good weather or for large dish terminals",
     ["The link sits close to its minimum SNR threshold, leaving very little margin to spare for extra bits per symbol",
      "Rain fade has already reduced the received signal level, which is assumed to call for packing in more bits per symbol",
      "Higher-order modulation schemes are assumed to operate at a fundamentally lower SNR requirement than QPSK"]),

    ("Adaptive Coding and Modulation (ACM) in a satellite system monitors the link quality "
     "and dynamically selects the MCS to:",
     "Maximise throughput when the link is good and switch to more robust coding during rain fade or shadowing",
     ["Fix the modulation and coding scheme for the entire lifetime of a session, avoiding any signalling overhead",
      "Select the highest-order modulation available at each scheduling opportunity, irrespective of current link conditions",
      "Reduce the symbol rate during rain fade while deliberately holding the modulation order constant"]),

    ("The carrier-to-noise density ratio C/N₀ at a satellite receiver is determined by "
     "combining the transmitter EIRP, free-space path loss, atmospheric losses and the "
     "receiver:",
     "Figure of merit G/T (antenna gain divided by system noise temperature)",
     ["Transmit power and antenna gain considered separately rather than combined into a single receiver figure",
      "The measured bit error rate together with the required Eb/N₀ threshold for that error rate",
      "The transponder's total bandwidth and the number of carriers currently active within it"]),

    ("The satellite power budget must carefully balance onboard power generation against "
     "consumption because:",
     "Solar panel area is constrained by mass and structural limits, and the high-power amplifiers (HPAs) are the dominant power consumers on the payload",
     ["Most communications satellites rely on onboard nuclear reactors, which supply effectively unlimited power to the payload",
      "High-power amplifiers are assumed to consume a negligible fraction of power compared with the onboard processor",
      "Solar panel technology is assumed to be mature enough that available power is rarely a limiting factor in modern payload design"]),

    ("In a hub-and-spoke satellite network, remote VSAT terminals communicate via the "
     "satellite to a central hub, which:",
     "Connects the satellite network to the terrestrial internet or PSTN and provides high-power, high-bandwidth uplinking to the satellite",
     ["Is physically located in orbit as part of the satellite's own payload rather than on the ground",
      "Has been replaced by full-mesh inter-satellite-link topologies across most modern commercial satellite systems",
      "Needs no uplink of its own since it is assumed to solely receive traffic coming down from the satellite"]),

    ("A full-mesh satellite network enabled by ISLs or multi-spot beams allows:",
     "Terminals to communicate directly with each other through the satellite without routing through a terrestrial hub, reducing latency for terminal-to-terminal traffic",
     ["Each communication path to still be routed back through a single central hub, regardless of any ISLs present",
      "Terminals to bypass the satellite altogether and exchange traffic through direct terrestrial radio links",
      "Full-mesh connectivity to be achievable solely with GEO satellites, a capability assumed structurally unavailable to any LEO constellation"]),

    ("A satellite link availability specification of 99.9% per year means the link is "
     "unavailable for approximately:",
     "About 8.8 hours per year, so the link margin must be sized to withstand rain fades for all but that time",
     ["About 1 second of downtime per year, a figure so small it would require just a negligible link margin",
      "About 36.5 days of downtime per year, which would demand an unrealistically large link margin to correct",
      "Availability specifications and required link margin are treated as unrelated, independent design parameters"]),

    ("Most satellite systems use Frequency Division Duplex (FDD) rather than Time Division "
     "Duplex (TDD) because:",
     "The uplink and downlink already use different frequency bands (e.g., 14 GHz up / 11 GHz down in Ku band), naturally accommodating simultaneous two-way transmission",
     ["TDD is assumed to require two separate satellite transponders while FDD needs just a single shared transponder",
      "TDD is assumed to be prohibited outright by ITU Radio Regulations for use in any commercial satellite communication system",
      "FDD is assumed to require simpler transponder hardware overall than an equivalent TDD-based satellite payload"]),

    ("In 5G NR, PDSCH scheduling is performed by the gNB using:",
     "DCI (Downlink Control Information) transmitted on the PDCCH, which tells the UE which resource blocks carry its data in each slot",
     ["A fixed, static resource assignment configured once at network deployment and left unchanged thereafter",
      "Uplink control signalling that the UE itself sends to reserve its own downlink resource blocks",
      "Random access preambles transmitted on the PRACH, which are assumed to directly initiate PDSCH scheduling without any DCI grant"]),
]

# All 100 Part-2 questions compiled into a single bank.
ALL_QUESTIONS = GROUP_E + GROUP_F + GROUP_G + GROUP_H
OUTPUT_FILE = "compiled_2.json"


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def main():
    rng = random.Random(457)  # different seed from Part 1
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
