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
     "L-band (approximately 1–2 GHz)",
     ["Ka-band (26.5–40 GHz)",
      "V-band (40–75 GHz)",
      "mmWave FR2 (24–52 GHz)"]),

    ("NTN is particularly well-suited for narrowband IoT (NB-IoT) deployments primarily "
     "because:",
     "IoT devices are often in remote areas without terrestrial coverage, and their low data-rate requirements are compatible with satellite link constraints",
     ["IoT devices require very high bandwidth that only satellites can provide",
      "NTN never supports IoT, which is a terrestrial-only service",
      "IoT battery life is too short for any terrestrial network"]),

    ("The Starlink constellation by SpaceX provides broadband primarily from which orbital "
     "shell?",
     "LEO at around 550 km, using thousands of satellites for global coverage",
     ["GEO at 35,786 km, using three satellites",
      "MEO at 20,200 km, like GPS",
      "HAPS at 20 km altitude"]),

    ("The Iridium system is notable for using inter-satellite links (ISLs) and for being "
     "able to route calls between satellites without a ground gateway underneath every "
     "satellite. Its constellation consists of:",
     "66 LEO satellites providing polar and global coverage",
     ["3 GEO satellites covering only the tropics",
      "24 MEO satellites identical to the GPS constellation",
      "Thousands of HAPS platforms in the stratosphere"]),

    ("3GPP Release 17 is significant to NTN because it:",
     "Introduced the first standardised 5G NR enhancements specifically for satellite access, including timing and Doppler adaptations",
     ["Defined the basic 5G NR air interface with no NTN provisions",
      "Removed NTN support that had been added in Release 15",
      "Only addressed mmWave terrestrial enhancements"]),

    ("Direct-to-Device (D2X) satellite services, which allow an unmodified smartphone to "
     "communicate via satellite, are enabled primarily by:",
     "New 3GPP NTN specifications that extend 5G NR for low-power handheld UEs accessing satellites directly",
     ["A dedicated satellite handset sold only by satellite operators",
      "Special IoT modules embedded at the factory that are not part of 3GPP",
      "A terrestrial base station located near the satellite ground track"]),

    ("A key advantage of NTN as a complement to terrestrial networks is that during large "
     "public events or disasters, NTN can:",
     "Offload or supplement congested terrestrial cells, providing capacity relief and backup connectivity",
     ["Replace the terrestrial network permanently after the event",
      "Provide lower latency than any terrestrial alternative",
      "Prevent any interference to the terrestrial network"]),

    ("As satellite altitude increases, the coverage footprint of a single satellite:",
     "Increases, but at the cost of longer propagation delay and higher free-space path loss",
     ["Decreases, because higher satellites transmit at lower power",
      "Remains constant regardless of altitude",
      "Increases, with no effect on propagation delay"]),

    ("In the 6G vision, NTN is regarded as:",
     "A native component providing the 'coverage everywhere' pillar alongside terrestrial networks",
     ["A temporary solution to be replaced by dense urban 6G cells",
      "Exclusively a backhaul technology, not a direct user-access layer",
      "A 4G-only technology being phased out for 5G"]),

    ("In a LEO NTN system, a UE may experience two types of handover: satellite-to-satellite "
     "(inter-satellite) and beam-to-beam within the same satellite (inter-beam). Both require:",
     "Mobility management procedures adapted to the rapidly changing satellite geometry",
     ["No signalling, because the satellite tracks the UE autonomously",
      "Only GEO-specific procedures, as LEO uses a different standard",
      "Physical reconnection of the UE to a different ground gateway"]),

    ("Compared with GEO, LEO satellites offer lower latency because:",
     "Their altitude is roughly 550–1,500 km vs 35,786 km for GEO, greatly reducing one-way propagation delay",
     ["LEO satellites transmit at higher power than GEO",
      "LEO satellites use a higher carrier frequency than GEO",
      "LEO satellites are physically smaller and therefore faster"]),

    ("Satellite link power limitation arises primarily because:",
     "The satellite's transmit power is constrained by the solar panel area and mass budget available in orbit",
     ["Spectrum regulations prohibit satellites from transmitting above a certain power",
      "The ground terminal regulates the satellite's power remotely",
      "Higher power always degrades signal quality in satellite systems"]),

    ("The large round-trip time of a GEO satellite link causes problems for the TCP "
     "protocol because:",
     "The TCP congestion window fills slowly, capping throughput unless a Performance-Enhancing Proxy (PEP) or TCP optimisation is used",
     ["TCP ignores propagation delay entirely and is unaffected",
      "Large RTT increases the TCP window size automatically, improving throughput",
      "TCP was designed for satellite links and performs better over GEO than over terrestrial"]),

    ("Spot beams in a satellite system concentrate transmit power onto a smaller geographic "
     "area in order to:",
     "Increase the power spectral density within each beam and enable frequency reuse across spatially separated beams",
     ["Reduce the satellite's power consumption",
      "Illuminate the entire Earth from a single antenna element",
      "Eliminate the need for frequency planning between beams"]),

    ("3GPP defines two categories of NTN UE based on their ability to assist Doppler and "
     "timing compensation. These are:",
     "GNSS-capable UEs (which pre-compensate using their own position and ephemeris) and non-GNSS UEs (which rely on network assistance)",
     ["Voice-only UEs and data-only UEs",
      "Fixed UEs and mobile UEs",
      "Transparent UEs and regenerative UEs"]),

    ("Satellite spectrum coordination at the international level is managed primarily "
     "through:",
     "ITU Radio Regulations, bilateral and multilateral agreements between administrations",
     ["WTO BTA tariff schedules",
      "UN Security Council resolutions",
      "The 3GPP technical specification process"]),

    ("In a bent-pipe (transparent) transponder, noise accumulated on the uplink is:",
     "Amplified and retransmitted alongside the signal, degrading the overall downlink carrier-to-noise ratio",
     ["Completely removed by the low-noise amplifier before retransmission",
      "Only present on the downlink, not the uplink",
      "Eliminated by the frequency-conversion process"]),

    ("Ephemeris data used by NTN UEs describes:",
     "The predicted position and velocity of the satellite over time, enabling the UE to compute Doppler shift and propagation delay",
     ["The satellite's onboard power budget",
      "The list of licensed operators permitted to use the satellite",
      "The software version running on the satellite payload"]),

    ("GNSS assists NTN UEs primarily by providing:",
     "Accurate UE position, which combined with satellite ephemeris allows the UE to pre-compensate Doppler shift and timing advance",
     ["A replacement for the NTN service link in areas of poor satellite visibility",
      "Electrical power to the UE's radio module",
      "Direct connection to the 5G core network via GNSS satellites"]),

    ("Maritime vessels in open ocean beyond terrestrial coastal coverage rely on NTN for:",
     "Broadband internet, voice, safety and vessel-tracking services",
     ["VHF terrestrial radio connections to land-based towers",
      "Fibre undersea cable connections carried by the vessel",
      "Microwave line-of-sight links between ships"]),

    ("In-flight connectivity (IFC) for commercial aircraft is provided by NTN because:",
     "Aircraft at cruise altitude are beyond the range of terrestrial networks, requiring satellite links for passenger and cockpit communications",
     ["Aviation regulations require aircraft to use terrestrial cellular only",
      "Aircraft antennas are incompatible with satellite frequencies",
      "In-flight connectivity is delivered by HF radio, not satellites"]),

    ("Circular polarization is preferred over linear polarization for mobile satellite "
     "terminals because:",
     "The received signal polarization is independent of the terminal's physical orientation, simplifying the antenna design",
     ["Circular polarization suffers less rain attenuation than linear polarization",
      "Linear polarization cannot be received by any satellite antenna",
      "Circular polarization always achieves higher gain than linear polarization"]),

    ("The OneWeb LEO constellation differs from Starlink in that OneWeb focuses on:",
     "Providing broadband connectivity through a wholesale/B2B model, selling capacity to telecom operators rather than directly to consumers",
     ["Launching GEO satellites for direct-to-consumer TV broadcasting",
      "Operating exclusively in Ka-band for military applications",
      "Using only bent-pipe payloads with no IP routing onboard"]),

    ("A Performance-Enhancing Proxy (PEP) on a satellite gateway improves TCP throughput "
     "by:",
     "Splitting the TCP connection into a terrestrial segment and a satellite segment, hiding the large satellite RTT from the end-to-end TCP feedback loop",
     ["Increasing the satellite's transmit power automatically",
      "Replacing TCP with a proprietary transport protocol at the UE",
      "Reducing the number of TCP acknowledgements the server must send"]),

    ("Which NTN platform offers the most rapid deployment and easiest recovery after "
     "failure, but is most limited by weather and flight regulations?",
     "Unmanned Aircraft System (UAS/drone) used as an airborne NTN node",
     ["GEO satellite, which can be repositioned within hours",
      "LEO satellite, which can be lowered to 50 km on demand",
      "HAPS balloon, which is immune to strong winds"]),
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
     ["Below 2 GHz (L-band), where wavelengths are long relative to raindrop size",
      "At optical wavelengths only, not at microwave frequencies",
      "Between 400 and 700 MHz (UHF), where absorption is strongest"]),

    ("A satellite orbit's inclination is defined as:",
     "The angle between the orbital plane and the Earth's equatorial plane; 0° is equatorial (GEO), 90° is polar",
     ["The altitude of the satellite above sea level",
      "The eccentricity of the orbital ellipse",
      "The angle between the satellite's antenna and the Earth's surface"]),

    ("A sun-synchronous orbit is used by Earth-observation satellites because:",
     "The orbital plane precesses at the same rate as the Earth's revolution around the Sun, keeping the local solar illumination time constant over each pass",
     ["The satellite orbits the Sun rather than the Earth, providing global energy coverage",
      "The satellite is stationary above the same point on Earth at all times",
      "Solar panels on a sun-synchronous satellite are always perpendicular to the Sun"]),

    ("The Van Allen radiation belts are a concern for satellite designers because:",
     "They are zones of trapped high-energy charged particles that can degrade semiconductor electronics and solar cells",
     ["They cause rain attenuation on Ku-band downlinks",
      "They prevent radio signals from reaching GEO altitude",
      "They are cloud layers in the troposphere that scatter microwave signals"]),

    ("The ionosphere (roughly 60–1,000 km altitude) affects satellite radio signals primarily "
     "by causing:",
     "Propagation delay, Faraday rotation of polarization, and signal dispersion, particularly at frequencies below about 3 GHz",
     ["Rain fade and tropospheric scintillation above 10 GHz",
      "Inter-symbol interference caused by multipath from buildings",
      "Thermal noise amplification in the satellite LNA"]),

    ("Tropospheric scintillation is a rapid fluctuation of received signal amplitude and phase "
     "caused by turbulence in the lower atmosphere. It is most significant at:",
     "Low elevation angles and frequencies above about 10 GHz",
     ["High elevation angles and low frequencies below 1 GHz",
      "All elevation angles equally, independent of frequency",
      "Polar latitudes only, where the troposphere is thinner"]),

    ("The Doppler frequency shift experienced by a ground receiver tracking a LEO satellite "
     "depends primarily on:",
     "The radial component of the satellite's velocity relative to the receiver, and the carrier frequency",
     ["Only the satellite's altitude, not its velocity",
      "Only the carrier frequency, not the satellite's motion",
      "The polarization of the signal, not the satellite geometry"]),

    ("A GEO satellite produces negligible Doppler shift for a stationary ground terminal "
     "because:",
     "Both the satellite and the terminal are effectively stationary relative to each other — the satellite's angular velocity matches the Earth's rotation",
     ["GEO satellites orbit too slowly to produce any relative motion",
      "Doppler shift is cancelled by the transponder's frequency converter",
      "GEO satellites transmit a compensation tone that removes Doppler"]),

    ("The elevation angle of a satellite as seen from a ground station determines:",
     "The length of the signal path through the atmosphere; higher elevation means a shorter atmospheric path and less attenuation",
     ["The satellite's orbital altitude above sea level",
      "The satellite's velocity relative to the ground",
      "The number of other satellites visible from the ground station"]),

    ("Link margin in a satellite system is defined as:",
     "The excess of received Eb/N0 (or C/N0) above the minimum threshold required for the specified bit-error rate",
     ["The physical diameter of the satellite's main reflector antenna",
      "The maximum allowable data rate on the satellite link",
      "The ratio of transmit power to receive power at the ground station"]),

    ("During equinox periods, GEO satellites experience solar eclipses lasting up to about:",
     "72 minutes per day, during which the satellite relies on onboard batteries",
     ["12 hours per day, as the satellite is behind the Earth all night",
      "Under 1 minute, since the Earth's shadow is very narrow at GEO",
      "GEO satellites never experience eclipse because they orbit the equatorial plane"]),

    ("Frequency reuse in a multi-beam satellite system increases overall system capacity "
     "because:",
     "The same frequency band is reused across spatially separated beams, multiplying the total traffic the satellite can carry",
     ["Each beam uses a different frequency, and reuse simply means the spectrum plan repeats",
      "Frequency reuse reduces co-channel interference to zero",
      "Total system capacity is limited by the number of beams regardless of reuse"]),

    ("When the same frequency is used in adjacent satellite beams (co-channel reuse), "
     "co-channel interference (CCI) is controlled by:",
     "Sufficient beam spacing and antenna sidelobe suppression to keep the interfering signal below acceptable levels",
     ["Increasing the carrier frequency until adjacent beams no longer overlap",
      "Assigning different polarizations to every beam",
      "Requiring adjacent beams to transmit at exactly the same power level"]),

    ("By Kepler's third law, the orbital period of a satellite is proportional to the "
     "cube root of the cube of the semi-major axis (T² ∝ a³). This means:",
     "Higher orbits have longer periods and lower orbital speeds than lower orbits",
     ["Higher orbits have shorter periods and higher orbital speeds",
      "The orbital period is the same regardless of altitude",
      "The orbital period depends on satellite mass, not altitude"]),

    ("GEO satellites have poor coverage poleward of approximately ±75° latitude because:",
     "They orbit in the equatorial plane, so the elevation angle seen from high latitudes is very low, below the horizon or near it",
     ["The Van Allen belts block radio signals at polar latitudes",
      "International regulations prohibit GEO satellite transmissions above 75° latitude",
      "Ionospheric absorption is so high at the poles that any signal is lost"]),

    ("A Molniya orbit is a highly elliptical orbit (HEO) with an inclination of about "
     "63.4° and a 12-hour period. Its primary purpose is to:",
     "Provide long-dwell coverage of high-latitude regions (such as Russia) where GEO elevation angles are too low",
     ["Provide geostationary-like fixed coverage over the equator",
      "Achieve the lowest possible propagation delay for Arctic users",
      "Allow satellites to pass over the equator at least four times per day"]),

    ("The Iridium constellation routes calls via inter-satellite links (ISLs), which means:",
     "Calls between any two points on Earth can be routed entirely through the satellite network without requiring a ground gateway in between",
     ["Each call must pass through a dedicated gateway for every hop",
      "ISLs are used only for housekeeping telemetry, not user traffic",
      "Iridium ISLs operate in the optical band and cannot carry voice"]),

    ("The ITU-R rain zone classification system (zones A to Q) is used to:",
     "Estimate the rain attenuation statistics for a given geographic location and design satellite link margins accordingly",
     ["Regulate the maximum allowable satellite transmit power in each zone",
      "Classify the orbital slots available to geostationary satellites",
      "Define the spectrum allocations for different satellite services"]),

    ("A multi-beam satellite antenna produces higher gain per beam than a global beam "
     "antenna. The trade-off is that:",
     "Each beam covers a smaller geographic area, requiring more beams to achieve the same total coverage",
     ["Each beam consumes more power, reducing total satellite capacity",
      "Multi-beam antennas cannot reuse frequencies between beams",
      "Higher gain per beam means lower overall system throughput"]),

    ("The geosynchronous orbit is the set of all orbits with a 24-hour period, while the "
     "geostationary orbit (GEO) is a subset defined by:",
     "Zero inclination (equatorial plane) and zero eccentricity (circular orbit), resulting in a fixed position above the equator",
     ["A highly elliptical orbit with an inclination of 63.4°",
      "Any polar orbit with a 24-hour period",
      "An inclination of exactly 28.5°, the latitude of the main launch sites"]),

    ("Satellite eclipse occurs when the Earth's shadow blocks sunlight from reaching the "
     "satellite. During eclipse, the satellite continues operating because:",
     "Onboard batteries are charged during sunlit periods and supply power during eclipse",
     ["Solar panels store energy chemically without needing batteries",
      "A backup nuclear power unit activates during eclipse",
      "The satellite automatically reduces power to zero and waits for sunlight"]),

    ("The figure of merit G/T of a satellite receiver system improves (increases) when:",
     "Antenna receive gain G increases or system noise temperature T decreases",
     ["Path loss increases",
      "The transmitter EIRP decreases",
      "The carrier frequency decreases while G and T remain constant"]),

    ("In the link budget of a satellite system, the overall end-to-end performance is "
     "determined by:",
     "The weaker of the uplink and downlink, since the total signal-to-noise ratio is dominated by the noisier hop",
     ["The sum of the uplink and downlink C/N values in linear scale",
      "The uplink only, since the satellite amplifies the downlink without adding noise",
      "The downlink only, since the uplink is always in surplus"]),

    ("Polarization diversity allows a satellite to reuse the same frequency band twice by "
     "transmitting two independent signals using:",
     "Orthogonal polarizations (e.g., horizontal and vertical linear, or RHCP and LHCP circular)",
     ["Two different carrier frequencies in the same polarization",
      "Two identical signals with a phase offset of 90 degrees",
      "Two antennas pointing at different geographic areas"]),
]

# ---------------------------------------------------------------------------
# GROUP G - 5G NR-NTN: Key Procedures & Enhancements
# ---------------------------------------------------------------------------
GROUP_G = [
    ("3GPP Release 17 introduced the first NTN-specific 5G NR enhancements, which "
     "included adaptations to timing advance, Doppler compensation and:",
     "HARQ process design to handle the long satellite round-trip time",
     ["Removal of the OFDM waveform in favour of a satellite-specific scheme",
      "A dedicated NTN frequency band below 100 MHz",
      "Replacement of the 5G core network with a satellite-specific core"]),

    ("In NTN, an extended Timing Advance (TA) mechanism is required because:",
     "Propagation delays of tens to hundreds of milliseconds must be pre-compensated so that uplink transmissions arrive at the gNB within the correct slot boundary",
     ["The satellite's clock runs faster than the ground station's clock",
      "Timing advance is used to delay the downlink signal to match user location",
      "TA is needed only when the UE is stationary; it is disabled for moving UEs"]),

    ("The PRACH (Physical Random Access Channel) preamble design is modified for NTN by:",
     "Extending the preamble length and guard period to accommodate the large round-trip propagation delay, preventing preamble collisions",
     ["Shortening preambles to reduce overhead in the long-delay channel",
      "Using a CDMA spreading code instead of a Zadoff-Chu sequence",
      "Transmitting the PRACH on the downlink rather than the uplink"]),

    ("The fundamental problem HARQ faces in a GEO NTN system is that:",
     "The 500+ ms RTT means the transmitter must buffer many HARQ processes simultaneously, far exceeding the 8-ms terrestrial HARQ round-trip budget",
     ["HARQ acknowledgements are encrypted, causing decoding delays",
      "HARQ retransmissions travel faster than the original transmission",
      "The RTT in GEO is the same as in terrestrial NR, so HARQ is unaffected"]),

    ("For GEO NTN, 3GPP permits HARQ to be disabled. When HARQ feedback is turned off, "
     "residual errors are handled by:",
     "Outer-layer error recovery mechanisms such as RLC ARQ or application-layer FEC",
     ["The satellite's onboard processor, which corrects errors in orbit",
      "Increasing UE transmit power until no errors occur",
      "Repeating every transmission exactly twice regardless of error status"]),

    ("As a LEO satellite moves, beam management in NTN must handle:",
     "Beam sweeping, beam measurement reporting, and beam failure recovery adapted to the satellite's high angular velocity relative to the ground",
     ["Static beam assignments that never change during a session",
      "Only uplink beam management, since the downlink is always optimal",
      "Beam management identical to that used in terrestrial massive MIMO"]),

    ("In a LEO NTN with Earth-moving beams, the cell associated with a given geographic "
     "area changes as the satellite passes overhead. 3GPP addresses this by:",
     "Distinguishing between Earth-fixed and Earth-moving cell identities, and adapting cell re-selection and handover procedures accordingly",
     ["Assigning a permanent cell ID to each geographic point on Earth, independent of the satellite",
      "Requiring UEs to switch to a terrestrial network during the cell transition",
      "Eliminating the cell concept entirely in NTN"]),

    ("Conditional Handover (CHO) is particularly beneficial in NTN because:",
     "The network can prepare the target cell in advance and trigger execution automatically when conditions are met, avoiding added signalling latency on a long-RTT link",
     ["CHO requires a very short RTT to operate correctly, suiting GEO best",
      "CHO is prohibited in NTN specifications and replaced by fast re-registration",
      "CHO is only applicable when the UE is moving on the ground, not the satellite"]),

    ("The primary frequency bands targeted by 3GPP NR-NTN specifications for the service "
     "link (UE-to-satellite) are:",
     "S-band (around 2 GHz) and Ka-band (around 26 GHz)",
     ["Only mmWave FR2 bands (24–52 GHz) shared with terrestrial 5G",
      "HF (3–30 MHz) for long-range propagation",
      "The same Ku-band feeder link frequencies used by the gateway"]),

    ("Inter-satellite links (ISLs) are most naturally associated with the regenerative "
     "payload architecture because:",
     "A regenerative satellite can route and forward data packets, making it practical to relay traffic between satellites toward a distant gateway",
     ["Bent-pipe payloads support ISLs natively without any onboard processing",
      "ISLs require transparent frequency conversion that only bent-pipe payloads provide",
      "ISLs are prohibited between regenerative satellites under ITU regulations"]),

    ("In the RLC layer, the NTN large RTT creates an issue analogous to the TCP window "
     "problem, because:",
     "The RLC ARQ window may need to be enlarged to allow enough outstanding unacknowledged PDUs so that throughput is not stalled waiting for acknowledgements",
     ["RLC ARQ is completely disabled in NTN, removing the window size constraint",
      "RLC window size has no impact on throughput regardless of RTT",
      "The RLC layer is removed from the NTN protocol stack in Release 17"]),

    ("In LEO NTN, paging areas tend to be larger than in terrestrial networks because:",
     "Satellite footprints cover vast geographic areas, and using large paging areas reduces the frequency of tracking area updates as the satellite moves",
     ["LEO satellites have fewer resources and can only page a small number of UEs",
      "Large paging areas reduce the total amount of data transmitted to UEs",
      "Paging in NTN follows identical procedures and area sizes as terrestrial 5G"]),

    ("Open-loop power control is preferred over closed-loop power control for NTN uplinks "
     "because:",
     "The long RTT makes it impractical to rely on fast gNB feedback to adjust UE transmit power in near real-time",
     ["Closed-loop control is more accurate but requires more UE hardware",
      "Open-loop control uses gNB feedback received within 1 ms",
      "Closed-loop control is mandated by 3GPP for all NTN uplinks"]),

    ("eMBB (enhanced Mobile BroadBand) services over LEO NTN are achievable, but their "
     "throughput is typically lower than terrestrial 5G because of:",
     "Large free-space path loss and the constrained transmit power of the satellite, limiting link capacity",
     ["LEO NTN using a fundamentally different waveform incompatible with eMBB",
      "3GPP prohibiting eMBB services in NTN Release 17",
      "eMBB requiring a latency below 1 ms which is impossible in any NTN"]),

    ("URLLC (Ultra-Reliable Low-Latency Communication) requirements cannot be met by GEO "
     "NTN primarily because:",
     "GEO round-trip delay (~600 ms) far exceeds the sub-millisecond latency target of URLLC",
     ["GEO satellites are not powerful enough to support URLLC traffic",
      "URLLC is defined only for terrestrial networks and excluded from NTN specifications",
      "GEO NTN requires HARQ, which is incompatible with URLLC"]),

    ("Larger subcarrier spacing (higher numerology) in 5G NR is more robust against "
     "Doppler-induced inter-carrier interference in NTN because:",
     "A wider subcarrier spacing means the Doppler shift is a smaller fraction of the subcarrier bandwidth, reducing ICI",
     ["Larger spacing reduces symbol duration, giving the channel more time to change",
      "Lower numerology (smaller subcarrier spacing) is always preferred in NTN",
      "Doppler shift has no relation to subcarrier spacing in OFDM systems"]),

    ("Gateway diversity in NTN means:",
     "Multiple geographically separated gateways can serve the same satellite, so if one suffers rain fade the satellite can switch to a clear-sky gateway automatically",
     ["Using multiple satellites to serve one ground gateway simultaneously",
      "Providing redundant user terminals at each subscriber site",
      "Using two separate core networks to process gateway traffic"]),

    ("Ka-band is attractive for high-throughput satellite (HTS) systems because:",
     "Wide available bandwidths (~500 MHz or more per polarization) enable high throughput, despite more severe rain attenuation and stricter antenna pointing requirements than L- or S-band",
     ["Ka-band signals are unaffected by rain, making it ideal in tropical regions",
      "Ka-band has narrower bandwidth than L-band, making it more spectrally efficient",
      "Ka-band is exclusively allocated to military satellite communications"]),

    ("NTN is well-suited for massive Machine-Type Communications (mMTC) IoT primarily "
     "because:",
     "IoT sensors are often deployed in remote or unpowered locations without terrestrial coverage, and their low data-rate and infrequent transmission requirements suit satellite capacity constraints",
     ["IoT devices require ultra-high bandwidth only satellites can provide",
      "mMTC requires sub-millisecond latency that only LEO satellites can guarantee",
      "IoT devices cannot connect to satellites because they lack GNSS receivers"]),

    ("When a UE moves between satellite beams or between satellites, 5G session continuity "
     "mechanisms ensure:",
     "PDU sessions are maintained without application-level disruption, through UPF selection and session anchor management in the 5G core",
     ["PDU sessions are always fully terminated and re-established from scratch",
      "Session continuity is handled exclusively by the UE without any network involvement",
      "Session continuity is only supported for voice calls, not data sessions"]),

    ("A GNSS-capable NTN UE uses its own position and satellite ephemeris to:",
     "Pre-compute the uplink frequency offset and timing advance needed to compensate for Doppler shift and propagation delay before transmitting",
     ["Authenticate with the satellite's on-board processor",
      "Determine which core network slice to connect to",
      "Request a handover to a terrestrial network when GNSS is available"]),

    ("Timing pre-compensation in NTN requires the UE to:",
     "Advance its uplink transmission by an amount equal to the computed propagation delay to the satellite, so the signal arrives within the expected slot window",
     ["Delay its uplink transmission to account for the satellite's forward motion",
      "Ask the gNB to shift the downlink timing by the propagation delay",
      "Transmit at a fixed offset of 0.5 ms regardless of satellite distance"]),

    ("Network slicing in 5G NTN allows different service types (broadband, IoT, emergency) "
     "to share the same NTN physical resources while maintaining:",
     "Independent quality of service, isolation and scheduling policies per slice",
     ["A single shared QoS profile for all services to simplify management",
      "Separate physical satellite hardware for each slice",
      "No service differentiation — all slices receive identical treatment"]),

    ("5G NR reference signals (DMRS, CSI-RS, SRS) in NTN must be designed to account for:",
     "The large and time-varying delays of the NTN channel, requiring additional reference signal configurations for accurate channel estimation",
     ["The complete absence of multipath in the satellite channel",
      "The fact that the NTN channel is perfectly static and needs no estimation",
      "A shorter symbol duration than in terrestrial NR to fit more pilots"]),

    ("The main factor limiting uplink throughput for direct-to-handset LEO NTN is:",
     "The constrained transmit power of handheld UEs (typically 23–26 dBm), which combined with the large path loss sets an upper bound on achievable uplink data rate",
     ["The downlink, which is always the bottleneck in NTN systems",
      "Excessive UE transmit power causing interference to neighbouring satellites",
      "The absence of MIMO at the UE, which forces single-antenna transmission"]),
]

# ---------------------------------------------------------------------------
# GROUP H - SatCom Systems & 5G Architecture (Part 2)
# ---------------------------------------------------------------------------
GROUP_H = [
    ("DVB-S2 (Digital Video Broadcasting — Satellite, Second Generation) is significant "
     "for satellite broadband because it:",
     "Employs Adaptive Coding and Modulation (ACM), dynamically selecting the modulation and coding scheme to maximise throughput under varying link conditions",
     ["Uses fixed QPSK modulation at a constant code rate regardless of link quality",
      "Is a 3GPP standard designed specifically for 5G NR satellite access",
      "Is a terrestrial broadcast standard not used in satellite systems"]),

    ("DVB-RCS2 (Return Channel via Satellite, Second Generation) defines:",
     "The interactive return channel from the user terminal to the satellite, enabling two-way broadband satellite services",
     ["The forward link broadcast from the satellite to all terminals",
      "The ITU standard for GEO orbital slot coordination",
      "The inter-satellite link protocol used in LEO constellations"]),

    ("A VSAT (Very Small Aperture Terminal) system typically uses:",
     "Small dish antennas of 0.6–3.6 m diameter to provide satellite broadband at fixed or mobile sites, usually via GEO satellites in Ku or Ka band",
     ["Large parabolic dishes over 10 m in diameter for military communications",
      "LEO satellite constellations exclusively",
      "Phased-array antennas at altitudes above 50 km"]),

    ("In FDMA (Frequency Division Multiple Access) for satellite systems, a key "
     "disadvantage is:",
     "Spectrum is wasted when an assigned frequency sub-band is idle because its allocated user has no traffic to send",
     ["All users must transmit in the same time slot, causing collisions",
      "FDMA requires the most complex synchronization of all multiple-access schemes",
      "FDMA cannot be used in combination with TDMA on the same satellite"]),

    ("Satellite TDMA (Time Division Multiple Access) requires tight time synchronization "
     "across all terminals because:",
     "Without synchronisation, bursts from different terminals will overlap in time at the satellite, causing interference",
     ["TDMA assigns unique codes to each user and synchronisation prevents code collisions",
      "TDMA uses separate frequencies per terminal and timing prevents frequency drift",
      "Synchronisation is needed only for the ground gateway, not for user terminals"]),

    ("In CDMA (Code Division Multiple Access), all users share the same bandwidth "
     "simultaneously and are separated by unique spreading codes. A critical operational "
     "requirement is:",
     "Accurate uplink power control, so that no single user's signal overpowers the others (the near-far problem)",
     ["That no two users transmit during the same time slot",
      "That each user is assigned a separate frequency channel",
      "That the spreading codes are regenerated every millisecond"]),

    ("OFDMA (Orthogonal Frequency Division Multiple Access) is used in the 5G NR "
     "downlink because it:",
     "Allows flexible per-slot scheduling of subcarriers to different users, enabling efficient multi-user resource allocation",
     ["Assigns each user a unique spreading code instead of a frequency sub-band",
      "Is identical to FDMA but with analogue instead of digital carriers",
      "Was designed for single-user access and does not support multi-user scheduling"]),

    ("DFT-spread OFDM (DFT-s-OFDM), also called SC-FDMA, is used in the 5G NR uplink "
     "rather than pure OFDMA because it:",
     "Achieves a lower Peak-to-Average Power Ratio (PAPR), which reduces power amplifier stress and is beneficial for power-constrained UE transmitters",
     ["Has a higher PAPR than OFDM, which suits satellite power amplifiers",
      "Is mandatory for satellite gNBs but prohibited in terrestrial gNBs",
      "Spreads the signal across fewer subcarriers, reducing the transmitted bandwidth"]),

    ("The Access and Mobility Management Function (AMF) in the 5G SA core is responsible "
     "for:",
     "UE registration, connection establishment and mobility management including handover decisions",
     ["Routing user-plane IP packets between the RAN and the internet",
      "Establishing and releasing PDU sessions and managing IP address allocation",
      "Scheduling radio resource blocks within the gNB"]),

    ("The Session Management Function (SMF) in the 5G SA core is responsible for:",
     "Establishing, modifying and releasing PDU sessions and managing IP address allocation for UEs",
     ["Handling UE authentication and registration",
      "Performing radio resource scheduling in the gNB",
      "Connecting the gNB to the 5G core via the NG interface"]),

    ("The User Plane Function (UPF) in the 5G SA core is the:",
     "Data-plane anchor that handles packet routing and forwarding between the RAN and external data networks such as the internet",
     ["Control-plane function that manages UE authentication",
      "Radio access node that schedules downlink transmissions",
      "Spectrum management entity that assigns frequencies to operators"]),

    ("The NG interface in 5G connects the gNB to the 5G core network, with:",
     "NG-C (N2) carrying control-plane signalling to the AMF and NG-U (N3) carrying user-plane traffic to the UPF",
     ["NG-C carrying user-plane traffic and NG-U carrying control signalling",
      "Both NG-C and NG-U connecting the gNB directly to the internet",
      "The NG interface connecting two neighbouring gNBs to each other"]),

    ("The Xn interface in 5G connects:",
     "Neighbouring gNBs to each other, enabling handover coordination, dual connectivity and interference management",
     ["The gNB to the 5G core AMF",
      "The UE to the gNB over the air interface",
      "The UPF to external data networks"]),

    ("Phased-array antennas are used in LEO satellite user terminals because they:",
     "Electronically steer narrow beams toward the moving satellite without mechanical movement, enabling rapid tracking at low latency",
     ["Are cheaper to manufacture than parabolic dish antennas",
      "Do not require any antenna pointing, making them omnidirectional",
      "Can only be used at stationary fixed terminals, not on mobile vehicles"]),

    ("Massive MIMO in 5G NR uses a large number of antenna elements at the gNB to:",
     "Form narrow, high-gain beams directed at individual UEs, greatly increasing spectral efficiency through spatial multiplexing",
     ["Reduce the number of antennas compared with 4G LTE",
      "Serve all UEs from a single broad beam to simplify scheduling",
      "Operate only at sub-1 GHz frequencies where wavelengths are large"]),

    ("Null-steering in multi-beam satellite antennas suppresses interfering signals by:",
     "Placing deep nulls in the antenna radiation pattern in the direction of interferers while maintaining high gain toward intended users",
     ["Reducing the satellite's total transmit power across all beams",
      "Assigning orthogonal frequencies to all beams simultaneously",
      "Rotating the satellite's attitude to avoid interfering sources"]),

    ("Higher-order modulation (e.g., 64QAM vs QPSK) transmits more bits per symbol but "
     "requires a higher SNR. In satellite systems, higher-order modulation is used when:",
     "The link has a large margin above the minimum threshold, typically in good weather or for large dish terminals",
     ["The link is close to the minimum SNR threshold and the margin is small",
      "Rain fade has reduced the signal level, necessitating more bits per symbol",
      "Higher-order modulation always operates at a lower SNR than QPSK"]),

    ("Adaptive Coding and Modulation (ACM) in a satellite system monitors the link quality "
     "and dynamically selects the MCS to:",
     "Maximise throughput when the link is good and switch to more robust coding during rain fade or shadowing",
     ["Fix modulation and coding for the lifetime of a session to avoid overhead",
      "Always select the highest-order modulation regardless of link conditions",
      "Reduce the symbol rate during rain fade, keeping the modulation order constant"]),

    ("The carrier-to-noise density ratio C/N₀ at a satellite receiver is determined by "
     "combining the transmitter EIRP, free-space path loss, atmospheric losses and the "
     "receiver:",
     "Figure of merit G/T (antenna gain divided by system noise temperature)",
     ["Transmit power and antenna gain separately",
      "Bit error rate and the required Eb/N₀",
      "Transponder bandwidth and the number of active carriers"]),

    ("The satellite power budget must carefully balance onboard power generation against "
     "consumption because:",
     "Solar panel area is constrained by mass and structural limits, and the high-power amplifiers (HPAs) are the dominant power consumers on the payload",
     ["Satellites use nuclear reactors with unlimited power but limited cooling",
      "HPAs consume negligible power compared with the onboard processor",
      "Solar panel technology is mature enough that power is never a constraint"]),

    ("In a hub-and-spoke satellite network, remote VSAT terminals communicate via the "
     "satellite to a central hub, which:",
     "Connects the satellite network to the terrestrial internet or PSTN and provides high-power, high-bandwidth uplinking to the satellite",
     ["Is located in orbit on the satellite itself",
      "Is replaced by a full-mesh ISL topology in all modern systems",
      "Requires no uplink because it only receives traffic from the satellite"]),

    ("A full-mesh satellite network enabled by ISLs or multi-spot beams allows:",
     "Terminals to communicate directly with each other through the satellite without routing through a terrestrial hub, reducing latency for terminal-to-terminal traffic",
     ["All communication to be routed through a single hub regardless of ISLs",
      "Terminals to bypass the satellite and communicate directly by radio",
      "A full-mesh to be established only with GEO satellites, not LEO"]),

    ("A satellite link availability specification of 99.9% per year means the link is "
     "unavailable for approximately:",
     "About 8.8 hours per year, so the link margin must be sized to withstand rain fades for all but that time",
     ["About 1 second per year, requiring a negligible link margin",
      "About 36.5 days per year, requiring a very large link margin",
      "Availability specifications do not affect the required link margin"]),

    ("Most satellite systems use Frequency Division Duplex (FDD) rather than Time Division "
     "Duplex (TDD) because:",
     "The uplink and downlink already use different frequency bands (e.g., 14 GHz up / 11 GHz down in Ku band), naturally accommodating simultaneous two-way transmission",
     ["TDD requires two satellite transponders while FDD needs only one",
      "TDD is prohibited by ITU regulations for satellite systems",
      "FDD has lower hardware complexity in the satellite transponder than TDD"]),

    ("In 5G NR, PDSCH scheduling is performed by the gNB using:",
     "DCI (Downlink Control Information) transmitted on the PDCCH, which tells the UE which resource blocks carry its data in each slot",
     ["A fixed static resource assignment programmed at network deployment and never changed",
      "Uplink control signalling sent by the UE to reserve its own resources",
      "Random access preambles on the PRACH that initiate scheduling"]),
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
