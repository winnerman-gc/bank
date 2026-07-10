#!/usr/bin/env python3
"""
Build the Satellite Communication & NTN (TE 456) MCQ bank -- Part 3.

Source material (subset of the slide decks in this folder -- the NR-NTN
architecture deck used for Parts 1-2 is no longer present on disk, so this
batch draws only from the following three):
  - TE456-NTN-What&Why.pdf
  - TE456-NTN-Overview-1.pdf
  - TE456-Elements-SatCom5GSystems-2026-Complete.pdf

Each question is (question_text, correct_answer, [distractor, distractor, distractor]).
Output JSON: compiled_3.json
"""
import json
import random

# ---------------------------------------------------------------------------
# GROUP I - Part 3 (sourced from What&Why, Overview-1, Elements-SatCom5GSystems)
# ---------------------------------------------------------------------------
GROUP_I = [
    ("Which frequency range (FR1) is defined for 5G NR in the standard?",
     "410 MHz to 7.125 GHz, covering the lower and mid-band frequencies.",
     ["24 GHz to 52 GHz, which provides high bandwidth over shorter distances.",
      "1 GHz to 2.6 GHz, typically reserved for older 3G and 4G deployments.",
      "26 GHz to 66 GHz, commonly referred to as the mmWave frequency band."]),

    ("In a 5G Radio Access Network, what is the primary role of the Packet Data Convergence Protocol (PDCP)?",
     "It compresses IP headers and provides ciphering and integrity protection.",
     ["It manages the physical radio resources and maps logical channels to physical ones.",
      "It configures coarse-grained, policy-related aspects of the network pipeline.",
      "It implements baseband and RF processing such as OFDM and MIMO algorithms."]),

    ("How does a regenerative (OBP) satellite repeater differ from a transparent (bent-pipe) repeater?",
     "It demodulates the uplink signal into baseband data before remodulating it for downlink.",
     ["It directly amplifies and frequency-shifts the received RF signal without decoding it.",
      "It requires large terrestrial base stations to handle the error-correction processing.",
      "It acts as a simple relay station that forwards incoming signals including the noise."]),

    ("Which physical signal in 5G NR is used to track phase noise in both uplink and downlink?",
     "Phase-tracking reference signals (PT-RS), sent as a low-density pilot sequence.",
     ["Primary synchronization signal (PSS), used to initially identify the network.",
      "Sounding reference signal (SRS), utilized to estimate uplink channel state.",
      "Channel-state information reference signal (CSI-RS), applied for MIMO rank selection."]),

    ("According to the 5G NR PHY frame structure, how many subframes make up a single 10ms radio frame?",
     "Exactly 10 subframes, each having a fixed duration of 1ms regardless of numerology.",
     ["Exactly 14 subframes, corresponding to the number of OFDM symbols in a standard slot.",
      "A variable number of subframes that scales dynamically based on the subcarrier spacing.",
      "Exactly 12 subframes, matching the number of consecutive subcarriers in a resource block."]),

    ("What characterizes an Earth-moving beam in a Non-Terrestrial Network (NTN)?",
     "The beam illuminates different geographic areas on Earth as the satellite moves in its orbit.",
     ["The beam covers a fixed region continuously because the satellite is geostationary in this specific network context.",
      "The beam is dynamically steered to remain focused on the exact same location.",
      "The beam relies on terrestrial cell towers to mechanically track user equipment."]),

    ("Which NTN platform operates at altitudes between 8 and 50 km and appears stationary to a fixed observer?",
     "High-Altitude Platform Stations (HAPS), typically utilizing Earth-fixed beams for coverage.",
     ["Low Earth Orbit (LEO) satellites, completing an orbit roughly every 90 minutes.",
      "Geosynchronous Earth Orbit (GEO) satellites, stationed at approximately 35,786 km.",
      "Medium Earth Orbit (MEO) satellites, often used for global navigation satellite systems."]),

    ("Why do terrestrial networks struggle to provide complete global coverage?",
     "Deploying infrastructure in sparse or rugged areas is often economically unfeasible and challenging.",
     ["Terrestrial base stations require line-of-sight to orbiting satellites to function properly within typical communication frameworks.",
      "Fiber optic cables inherently experience too much latency for continuous communication.",
      "The 3GPP standard restricts terrestrial networks from transmitting over large distances."]),

    ("In the context of 5G Non-Terrestrial Networks, what is service continuity?",
     "Maintaining uninterrupted wireless coverage when users move out of terrestrial cell range.",
     ["Providing a large geographic area with the same broadcast content simultaneously.",
      "Ensuring that terrestrial cell towers can handle massive congestion during big events.",
      "Replacing all existing ground infrastructure with a dense constellation of LEO satellites."]),

    ("What is the function of the Physical Broadcast Channel (PBCH) in the 5G downlink?",
     "It carries essential system information required for the user equipment to access the network.",
     ["It transports user data packets directly from the core network to the physical layer.",
      "It provides uplink channel estimation for the base station to adjust transmission power.",
      "It configures the coarse-grained scheduling prioritization policies in the control plane."]),

    ("What does a 5G resource block (RB) consist of in the frequency and time domains?",
     "It consists of 12 subcarriers in frequency and typically 14 OFDM symbols in time.",
     ["It consists of 14 subcarriers in frequency and exactly 12 OFDM symbols in time.",
      "It consists of 10 subcarriers in frequency and a variable number of symbols depending on speed.",
      "It consists of 15 subcarriers in frequency and exactly 1 millisecond of transmission time."]),

    ("How do LEO satellites compare to GEO satellites in terms of propagation delay?",
     "LEO satellites have much smaller delays (1 to 5 ms) due to their proximity to the Earth.",
     ["LEO satellites exhibit significantly larger delays because their signals should bounce between satellites.",
      "LEO and GEO satellites have nearly identical propagation delays since radio waves travel at light speed.",
      "LEO satellites experience delays around 600 ms because they utilize complex regenerative processing."]),

    ("What defines a quasi-Earth-fixed beam in satellite communications?",
     "The beam covers a specific area for a period, then steers to another area as the satellite moves.",
     ["The beam maintains a static position over the Earth because the satellite itself is geostationary.",
      "The beam constantly sweeps across the Earth's surface without lingering on any specific region.",
      "The beam provides coverage chiefly to airborne platforms rather than terrestrial user equipment."]),

    ("In a satellite link budget, what does the effective isotropic radiated power (EIRP) represent?",
     "The power fed to the transmitting antenna multiplied by its gain in a specific direction.",
     ["The ratio of the receiving antenna's gain to the overall system noise temperature.",
      "The amount of signal attenuation caused by free space path loss and atmospheric gases.",
      "The final carrier-to-noise ratio calculated at the receiver after all losses are applied."]),

    ("Which of the following is a function of the Service Data Adaptation Protocol (SDAP) in the 5G protocol stack?",
     "It assigns Quality of Service (QoS) Flow IDs and maps flows to underlying radio resources.",
     ["It implements baseband OFDM processing to increase the spectral efficiency of the transmission.",
      "It transparently forwards baseband radio frames without inspecting the network layer headers.",
      "It handles physical channel error correction coding, such as polar coding and LDPC coding."]),

    ("What is the primary motivation for integrating NTN with Terrestrial Networks in the 6G vision?",
     "To achieve ubiquitous global connectivity by complementing ground-based infrastructure.",
     ["To replace aging terrestrial fiber optic cables with completely wireless satellite links.",
      "To increase the bandwidth of terrestrial small cells operating in dense urban environments.",
      "To ensure that older 3G and 4G devices can maintain service without hardware upgrades."]),

    ("Which NTN use case refers to broadcasting the same content to a large geographic area efficiently?",
     "Service scalability, which optimizes network performance by using large satellite beams.",
     ["Service ubiquity, which focuses on providing coverage to unserved and rugged rural locations.",
      "Service continuity, which aims to keep mobile users connected as they cross network boundaries.",
      "Service reliability, which establishes redundant communication paths during natural disasters."]),

    ("What is the typical altitude range for Medium Earth Orbit (MEO) satellites?",
     "Between 7,000 and 25,000 km, balancing wide coverage with moderate latency.",
     ["Between 300 and 1,500 km, allowing for extremely low propagation delay for internet services.",
      "Exactly 35,786 km, where the orbital period perfectly matches the Earth's rotational speed.",
      "Between 8 and 50 km, typically utilized by stratospheric balloons and solar-powered drones."]),

    ("In a satellite communications payload, what role does the Low Noise Amplifier (LNA) play?",
     "It boosts the weak received uplink signal while introducing minimal internal noise.",
     ["It shifts the frequency of the carrier signal to prepare it for transmission on the downlink.",
      "It provides the massive power required to transmit the carrier signal back to the Earth station.",
      "It demodulates the radio frequency signal to extract the underlying digital baseband data stream."]),

    ("What is the significance of the Radio Resource Control (RRC) protocol in 5G NR?",
     "It operates in the control plane to manage coarse-grained network policies and mobility.",
     ["It processes user plane packets to ensure data flows smoothly between the device and application.",
      "It directly converts digital data streams into analog radio frequencies for the physical antennas.",
      "It compresses IP headers to reduce the overall payload size over the wireless communication link."]),

    ("How does Orthogonal Frequency Division Multiplexing (OFDM) handle subcarrier interference?",
     "The subcarriers are mathematically orthogonal, so crosstalk cancels out at the center frequency.",
     ["The subcarriers are separated by wide guard bands that prevent the frequencies from overlapping.",
      "The subcarriers are transmitted in distinct time slots to avoid colliding in the frequency domain.",
      "The subcarriers use completely different polarization states to maintain signal independence."]),

    ("Which satellite subsystem is responsible for maintaining the spacecraft's orientation in orbit?",
     "The Attitude and Orbit Control System (AOCS), which stabilizes the platform.",
     ["The Electrical Power Subsystem (EPS), which supplies energy to the communications payload.",
      "The Telemetry, Tracking, and Command (TTC&M) system, which relays health data to the ground.",
      "The Thermal Control Subsystem, which prevents the satellite components from overheating."]),

    ("What characterizes the physical layer uplink channel PRACH in a 5G network?",
     "It handles the initial access procedure when a user device attempts to connect to the network.",
     ["It carries the bulk of the user data traffic from the mobile device to the base station.",
      "It broadcasts crucial system information to all mobile devices within the cell's coverage area.",
      "It transmits acknowledgment signals indicating successful reception of downlink data packets."]),

    ("Why are GEO satellites considered disadvantageous for certain real-time applications?",
     "Their extreme distance from Earth introduces roughly 600ms of round-trip propagation delay.",
     ["Their proximity to the atmosphere causes them to experience severe drag and frequent orbit corrections.",
      "Their rapid movement relative to the Earth requires complex tracking antennas on the ground.",
      "Their small beam footprints necessitate thousands of satellites to provide continuous coverage."]),

    ("What is the main function of the feeder link in a satellite communication network?",
     "It provides the communication path between the satellite and an Earth ground gateway.",
     ["It connects the end-user's mobile device directly to the orbiting satellite.",
      "It establishes a direct optical or radio connection between two artificial satellites.",
      "It relays data directly from the terrestrial core network to a local base station."]),

    ("In the 5G NR PHY frame structure, what is the subcarrier spacing when the numerology parameter μ = 0?",
     "15 kHz, calculated using the standard base formula.",
     ["180 kHz, which is the bandwidth of a full resource block.",
      "30 kHz, corresponding to a higher numerology setting.",
      "15 kHz, which represents a narrower subcarrier bandwidth."]),

    ("In the 5G NR PHY frame structure, what is the subcarrier spacing when the numerology parameter μ = 1?",
     "30 kHz, calculated using the standard base formula.",
     ["60 kHz, corresponding to a higher numerology setting.",
      "15 kHz, which represents a narrower subcarrier bandwidth.",
      "360 kHz, which is the bandwidth of a full resource block."]),

    ("In the 5G NR PHY frame structure, what is the subcarrier spacing when the numerology parameter μ = 2?",
     "60 kHz, calculated using the standard base formula.",
     ["30 kHz, which represents a narrower subcarrier bandwidth.",
      "720 kHz, which is the bandwidth of a full resource block.",
      "120 kHz, corresponding to a higher numerology setting."]),

    ("In the 5G NR PHY frame structure, what is the subcarrier spacing when the numerology parameter μ = 3?",
     "120 kHz, calculated using the standard base formula.",
     ["240 kHz, corresponding to a higher numerology setting.",
      "60 kHz, which represents a narrower subcarrier bandwidth.",
      "1440 kHz, which is the bandwidth of a full resource block."]),

    ("In the 5G NR PHY frame structure, what is the subcarrier spacing when the numerology parameter μ = 4?",
     "240 kHz, calculated using the standard base formula.",
     ["480 kHz, corresponding to a higher numerology setting.",
      "2880 kHz, which is the bandwidth of a full resource block.",
      "120 kHz, which represents a narrower subcarrier bandwidth."]),

    ("According to the 5G NR standards, how many slots are contained in a single 1ms subframe when the numerology μ = 0?",
     "1 slots, as the number of slots scales exponentially with μ.",
     ["1 slots, representing a lower numerology configuration.",
      "10 slots, which is the number contained in an entire radio frame.",
      "2 slots, which would occur if the subcarrier spacing were doubled."]),

    ("According to the 5G NR standards, how many slots are contained in a single 1ms subframe when the numerology μ = 1?",
     "2 slots, as the number of slots scales exponentially with μ.",
     ["20 slots, which is the number contained in an entire radio frame.",
      "1 slots, representing a lower numerology configuration.",
      "4 slots, which would occur if the subcarrier spacing were doubled."]),

    ("According to the 5G NR standards, how many slots are contained in a single 1ms subframe when the numerology μ = 2?",
     "4 slots, as the number of slots scales exponentially with μ.",
     ["2 slots, representing a lower numerology configuration.",
      "40 slots, which is the number contained in an entire radio frame.",
      "8 slots, which would occur if the subcarrier spacing were doubled."]),

    ("According to the 5G NR standards, how many slots are contained in a single 1ms subframe when the numerology μ = 3?",
     "8 slots, as the number of slots scales exponentially with μ.",
     ["80 slots, which is the number contained in an entire radio frame.",
      "4 slots, representing a lower numerology configuration.",
      "16 slots, which would occur if the subcarrier spacing were doubled."]),

    ("According to the 5G NR standards, how many slots are contained in a single 1ms subframe when the numerology μ = 4?",
     "16 slots, as the number of slots scales exponentially with μ.",
     ["32 slots, which would occur if the subcarrier spacing were doubled.",
      "8 slots, representing a lower numerology configuration.",
      "160 slots, which is the number contained in an entire radio frame."]),

    ("What is the exact time period of a single slot in 5G NR when utilizing numerology μ = 0?",
     "1.0 ms, determined by dividing the 1ms subframe by the slot count.",
     ["0.5 ms, which corresponds to the subsequent numerology level.",
      "2.0 ms, which would be the duration under a narrower subcarrier spacing.",
      "14.0 ms, which mistakenly multiplies the period by the number of symbols."]),

    ("What is the exact time period of a single slot in 5G NR when utilizing numerology μ = 1?",
     "0.5 ms, determined by dividing the 1ms subframe by the slot count.",
     ["7.0 ms, which mistakenly multiplies the period by the number of symbols.",
      "0.25 ms, which corresponds to the subsequent numerology level.",
      "1.0 ms, which would be the duration under a narrower subcarrier spacing."]),

    ("What is the exact time period of a single slot in 5G NR when utilizing numerology μ = 2?",
     "0.25 ms, determined by dividing the 1ms subframe by the slot count.",
     ["0.125 ms, which corresponds to the subsequent numerology level.",
      "3.5 ms, which mistakenly multiplies the period by the number of symbols.",
      "0.5 ms, which would be the duration under a narrower subcarrier spacing."]),

    ("What is the exact time period of a single slot in 5G NR when utilizing numerology μ = 3?",
     "0.125 ms, determined by dividing the 1ms subframe by the slot count.",
     ["0.0625 ms, which corresponds to the subsequent numerology level.",
      "0.25 ms, which would be the duration under a narrower subcarrier spacing.",
      "1.75 ms, which mistakenly multiplies the period by the number of symbols."]),

    ("What is the exact time period of a single slot in 5G NR when utilizing numerology μ = 4?",
     "0.0625 ms, determined by dividing the 1ms subframe by the slot count.",
     ["0.875 ms, which mistakenly multiplies the period by the number of symbols.",
      "0.125 ms, which would be the duration under a narrower subcarrier spacing.",
      "0.03125 ms, which corresponds to the subsequent numerology level."]),

    ("Assuming a normal cyclic prefix, what is the approximate duration of one OFDM symbol for 5G NR numerology μ = 0?",
     "Approximately 0.0714 ms, calculated by dividing the slot duration by 14.",
     ["Approximately 0.0357 ms, corresponding to a higher subcarrier spacing.",
      "Approximately 0.1429 ms, reflecting a lower numerology setting.",
      "Approximately 0.0833 ms, which assumes an extended cyclic prefix with 12 symbols."]),

    ("Assuming a normal cyclic prefix, what is the approximate duration of one OFDM symbol for 5G NR numerology μ = 1?",
     "Approximately 0.0357 ms, calculated by dividing the slot duration by 14.",
     ["Approximately 0.0714 ms, reflecting a lower numerology setting.",
      "Approximately 0.0417 ms, which assumes an extended cyclic prefix with 12 symbols.",
      "Approximately 0.0179 ms, corresponding to a higher subcarrier spacing."]),

    ("Assuming a normal cyclic prefix, what is the approximate duration of one OFDM symbol for 5G NR numerology μ = 2?",
     "Approximately 0.0179 ms, calculated by dividing the slot duration by 14.",
     ["Approximately 0.0357 ms, reflecting a lower numerology setting.",
      "Approximately 0.0089 ms, corresponding to a higher subcarrier spacing.",
      "Approximately 0.0208 ms, which assumes an extended cyclic prefix with 12 symbols."]),

    ("Assuming a normal cyclic prefix, what is the approximate duration of one OFDM symbol for 5G NR numerology μ = 3?",
     "Approximately 0.0089 ms, calculated by dividing the slot duration by 14.",
     ["Approximately 0.0045 ms, corresponding to a higher subcarrier spacing.",
      "Approximately 0.0179 ms, reflecting a lower numerology setting.",
      "Approximately 0.0104 ms, which assumes an extended cyclic prefix with 12 symbols."]),

    ("Assuming a normal cyclic prefix, what is the approximate duration of one OFDM symbol for 5G NR numerology μ = 4?",
     "Approximately 0.0045 ms, calculated by dividing the slot duration by 14.",
     ["Approximately 0.0089 ms, reflecting a lower numerology setting.",
      "Approximately 0.0022 ms, corresponding to a higher subcarrier spacing.",
      "Approximately 0.0052 ms, which assumes an extended cyclic prefix with 12 symbols."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 10000 km from the center of the Earth?",
     "Approximately 10000.0 hours, using the established relationship between altitude and period.",
     ["Approximately 1000000.0 hours, incorrectly squaring the distance instead of using the 1.5 power.",
      "Approximately 100000.0 hours, resulting from a calculation error in the proportionality constant.",
      "Approximately 5000.0 hours, which implies a significantly lower orbit."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 15000 km from the center of the Earth?",
     "Approximately 18371.17 hours, using the established relationship between altitude and period.",
     ["Approximately 9185.58 hours, which implies a significantly lower orbit.",
      "Approximately 2250000.0 hours, incorrectly squaring the distance instead of using the 1.5 power.",
      "Approximately 183711.73 hours, resulting from a calculation error in the proportionality constant."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 20000 km from the center of the Earth?",
     "Approximately 28284.27 hours, using the established relationship between altitude and period.",
     ["Approximately 4000000.0 hours, incorrectly squaring the distance instead of using the 1.5 power.",
      "Approximately 282842.71 hours, resulting from a calculation error in the proportionality constant.",
      "Approximately 14142.14 hours, which implies a significantly lower orbit."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 25000 km from the center of the Earth?",
     "Approximately 39528.47 hours, using the established relationship between altitude and period.",
     ["Approximately 19764.24 hours, which implies a significantly lower orbit.",
      "Approximately 395284.71 hours, resulting from a calculation error in the proportionality constant.",
      "Approximately 6250000.0 hours, incorrectly squaring the distance instead of using the 1.5 power."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 30000 km from the center of the Earth?",
     "Approximately 51961.52 hours, using the established relationship between altitude and period.",
     ["Approximately 9000000.0 hours, incorrectly squaring the distance instead of using the 1.5 power.",
      "Approximately 25980.76 hours, which implies a significantly lower orbit.",
      "Approximately 519615.24 hours, resulting from a calculation error in the proportionality constant."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 35000 km from the center of the Earth?",
     "Approximately 65479.0 hours, using the established relationship between altitude and period.",
     ["Approximately 654790.04 hours, resulting from a calculation error in the proportionality constant.",
      "Approximately 12250000.0 hours, incorrectly squaring the distance instead of using the 1.5 power.",
      "Approximately 32739.5 hours, which implies a significantly lower orbit."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 40000 km from the center of the Earth?",
     "Approximately 80000.0 hours, using the established relationship between altitude and period.",
     ["Approximately 16000000.0 hours, incorrectly squaring the distance instead of using the 1.5 power.",
      "Approximately 40000.0 hours, which implies a significantly lower orbit.",
      "Approximately 800000.0 hours, resulting from a calculation error in the proportionality constant."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 45000 km from the center of the Earth?",
     "Approximately 95459.42 hours, using the established relationship between altitude and period.",
     ["Approximately 47729.71 hours, which implies a significantly lower orbit.",
      "Approximately 954594.15 hours, resulting from a calculation error in the proportionality constant.",
      "Approximately 20250000.0 hours, incorrectly squaring the distance instead of using the 1.5 power."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 50000 km from the center of the Earth?",
     "Approximately 111803.4 hours, using the established relationship between altitude and period.",
     ["Approximately 1118033.99 hours, resulting from a calculation error in the proportionality constant.",
      "Approximately 25000000.0 hours, incorrectly squaring the distance instead of using the 1.5 power.",
      "Approximately 55901.7 hours, which implies a significantly lower orbit."]),

    ("According to Kepler's laws as modeled in the course, what is the orbital period of a satellite located at a distance of 55000 km from the center of the Earth?",
     "Approximately 128986.43 hours, using the established relationship between altitude and period.",
     ["Approximately 1289864.33 hours, resulting from a calculation error in the proportionality constant.",
      "Approximately 64493.21 hours, which implies a significantly lower orbit.",
      "Approximately 30250000.0 hours, incorrectly squaring the distance instead of using the 1.5 power."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 40 dBm, antenna gain of 20 dBi, feeder loss of 2 dB, and pointing loss of 1 dB.",
     "57 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["63 dBm, incorrectly adding the system losses instead of subtracting them.",
      "60 dBm, ignoring the feeder and pointing losses mostly in the calculation.",
      "797 dBm, improperly multiplying the power and gain in the logarithmic domain."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 45 dBm, antenna gain of 15 dBi, feeder loss of 3 dB, and pointing loss of 2 dB.",
     "55 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["65 dBm, incorrectly adding the system losses instead of subtracting them.",
      "670 dBm, improperly multiplying the power and gain in the logarithmic domain.",
      "60 dBm, ignoring the feeder and pointing losses mostly in the calculation."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 50 dBm, antenna gain of 10 dBi, feeder loss of 1 dB, and pointing loss of 1 dB.",
     "58 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["60 dBm, ignoring the feeder and pointing losses mostly in the calculation.",
      "62 dBm, incorrectly adding the system losses instead of subtracting them.",
      "498 dBm, improperly multiplying the power and gain in the logarithmic domain."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 30 dBm, antenna gain of 25 dBi, feeder loss of 4 dB, and pointing loss of 1 dB.",
     "50 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["745 dBm, improperly multiplying the power and gain in the logarithmic domain.",
      "60 dBm, incorrectly adding the system losses instead of subtracting them.",
      "55 dBm, ignoring the feeder and pointing losses mostly in the calculation."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 35 dBm, antenna gain of 22 dBi, feeder loss of 2 dB, and pointing loss of 2 dB.",
     "53 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["766 dBm, improperly multiplying the power and gain in the logarithmic domain.",
      "61 dBm, incorrectly adding the system losses instead of subtracting them.",
      "57 dBm, ignoring the feeder and pointing losses mostly in the calculation."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 38 dBm, antenna gain of 18 dBi, feeder loss of 1 dB, and pointing loss of 0 dB.",
     "55 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["683 dBm, improperly multiplying the power and gain in the logarithmic domain.",
      "56 dBm, ignoring the feeder and pointing losses mostly in the calculation.",
      "57 dBm, incorrectly adding the system losses instead of subtracting them."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 42 dBm, antenna gain of 24 dBi, feeder loss of 3 dB, and pointing loss of 1 dB.",
     "62 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["1004 dBm, improperly multiplying the power and gain in the logarithmic domain.",
      "66 dBm, ignoring the feeder and pointing losses mostly in the calculation.",
      "70 dBm, incorrectly adding the system losses instead of subtracting them."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 48 dBm, antenna gain of 12 dBi, feeder loss of 2 dB, and pointing loss of 1 dB.",
     "57 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["63 dBm, incorrectly adding the system losses instead of subtracting them.",
      "60 dBm, ignoring the feeder and pointing losses mostly in the calculation.",
      "573 dBm, improperly multiplying the power and gain in the logarithmic domain."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 33 dBm, antenna gain of 28 dBi, feeder loss of 5 dB, and pointing loss of 2 dB.",
     "54 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["61 dBm, ignoring the feeder and pointing losses mostly in the calculation.",
      "68 dBm, incorrectly adding the system losses instead of subtracting them.",
      "917 dBm, improperly multiplying the power and gain in the logarithmic domain."]),

    ("In a satellite link budget, calculate the Effective Isotropic Radiated Power (EIRP) given a transmit power of 36 dBm, antenna gain of 30 dBi, feeder loss of 4 dB, and pointing loss of 3 dB.",
     "59 dBm, obtained by adding transmit power and gain, then subtracting losses.",
     ["1073 dBm, improperly multiplying the power and gain in the logarithmic domain.",
      "73 dBm, incorrectly adding the system losses instead of subtracting them.",
      "66 dBm, ignoring the feeder and pointing losses mostly in the calculation."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 60 dBm, a receiving antenna gain of 10 dBi, a free space loss of 150 dB, and other combined atmospheric/pointing losses totaling 5 dB.",
     "-85 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["-105 dBm, incorrectly subtracting the receiving antenna gain.",
      "225 dBm, improperly treating the path loss as a signal gain.",
      "-75 dBm, incorrectly adding the atmospheric and pointing losses in this specific network context."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 65 dBm, a receiving antenna gain of 15 dBi, a free space loss of 160 dB, and other combined atmospheric/pointing losses totaling 10 dB.",
     "-90 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["250 dBm, improperly treating the path loss as a signal gain.",
      "-70 dBm, incorrectly adding the atmospheric and pointing losses in this specific network context.",
      "-120 dBm, incorrectly subtracting the receiving antenna gain."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 70 dBm, a receiving antenna gain of 20 dBi, a free space loss of 180 dB, and other combined atmospheric/pointing losses totaling 8 dB.",
     "-98 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["-138 dBm, incorrectly subtracting the receiving antenna gain.",
      "278 dBm, improperly treating the path loss as a signal gain.",
      "-82 dBm, incorrectly adding the atmospheric and pointing losses in this specific network context."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 55 dBm, a receiving antenna gain of 12 dBi, a free space loss of 140 dB, and other combined atmospheric/pointing losses totaling 3 dB.",
     "-76 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["210 dBm, improperly treating the path loss as a signal gain.",
      "-100 dBm, incorrectly subtracting the receiving antenna gain.",
      "-70 dBm, incorrectly adding the atmospheric and pointing losses according to the baseline system design."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 58 dBm, a receiving antenna gain of 18 dBi, a free space loss of 155 dB, and other combined atmospheric/pointing losses totaling 6 dB.",
     "-85 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["-73 dBm, incorrectly adding the atmospheric and pointing losses within typical communication frameworks.",
      "-121 dBm, incorrectly subtracting the receiving antenna gain.",
      "237 dBm, improperly treating the path loss as a signal gain."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 62 dBm, a receiving antenna gain of 22 dBi, a free space loss of 165 dB, and other combined atmospheric/pointing losses totaling 7 dB.",
     "-88 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["256 dBm, improperly treating the path loss as a signal gain.",
      "-74 dBm, incorrectly adding the atmospheric and pointing losses in this specific network context.",
      "-132 dBm, incorrectly subtracting the receiving antenna gain."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 68 dBm, a receiving antenna gain of 14 dBi, a free space loss of 175 dB, and other combined atmospheric/pointing losses totaling 4 dB.",
     "-97 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["261 dBm, improperly treating the path loss as a signal gain.",
      "-89 dBm, incorrectly adding the atmospheric and pointing losses under standard operational parameters.",
      "-125 dBm, incorrectly subtracting the receiving antenna gain."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 50 dBm, a receiving antenna gain of 25 dBi, a free space loss of 130 dB, and other combined atmospheric/pointing losses totaling 2 dB.",
     "-57 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["207 dBm, improperly treating the path loss as a signal gain.",
      "-107 dBm, incorrectly subtracting the receiving antenna gain.",
      "-53 dBm, incorrectly adding the atmospheric and pointing losses within typical communication frameworks."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 52 dBm, a receiving antenna gain of 28 dBi, a free space loss of 135 dB, and other combined atmospheric/pointing losses totaling 9 dB.",
     "-64 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["224 dBm, improperly treating the path loss as a signal gain.",
      "-46 dBm, incorrectly adding the atmospheric and pointing losses within typical communication frameworks.",
      "-120 dBm, incorrectly subtracting the receiving antenna gain."]),

    ("Calculate the received power (PR) for a satellite link with an EIRP of 72 dBm, a receiving antenna gain of 16 dBi, a free space loss of 190 dB, and other combined atmospheric/pointing losses totaling 11 dB.",
     "-113 dBm, found by adding the gain to EIRP and subtracting all propagation losses.",
     ["289 dBm, improperly treating the path loss as a signal gain.",
      "-145 dBm, incorrectly subtracting the receiving antenna gain.",
      "-91 dBm, incorrectly adding the atmospheric and pointing losses under standard operational parameters."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 2 assigned Resource Blocks (RBs)?",
     "24 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["20 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "48 subcarriers, which would represent exactly twice the standard resource block capacity.",
      "28 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 5 assigned Resource Blocks (RBs)?",
     "60 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["70 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot.",
      "50 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "120 subcarriers, which would represent exactly twice the standard resource block capacity."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 10 assigned Resource Blocks (RBs)?",
     "120 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["100 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "140 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot.",
      "240 subcarriers, which would represent exactly twice the standard resource block capacity."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 20 assigned Resource Blocks (RBs)?",
     "240 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["480 subcarriers, which would represent exactly twice the standard resource block capacity.",
      "200 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "280 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 50 assigned Resource Blocks (RBs)?",
     "600 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["700 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot.",
      "1200 subcarriers, which would represent exactly twice the standard resource block capacity.",
      "500 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 100 assigned Resource Blocks (RBs)?",
     "1200 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["1400 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot.",
      "1000 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "2400 subcarriers, which would represent exactly twice the standard resource block capacity."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 256 assigned Resource Blocks (RBs)?",
     "3072 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["2560 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "3584 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot.",
      "6144 subcarriers, which would represent exactly twice the standard resource block capacity."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 512 assigned Resource Blocks (RBs)?",
     "6144 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["5120 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "7168 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot.",
      "12288 subcarriers, which would represent exactly twice the standard resource block capacity."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 1024 assigned Resource Blocks (RBs)?",
     "12288 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["10240 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "24576 subcarriers, which would represent exactly twice the standard resource block capacity.",
      "14336 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot."]),

    ("In a 5G NR configuration, how many total subcarriers are contained across 2048 assigned Resource Blocks (RBs)?",
     "24576 subcarriers, since each individual resource block is strictly defined as 12 subcarriers.",
     ["20480 subcarriers, assuming a base-10 structure rather than the standardized 3GPP parameters.",
      "28672 subcarriers, mistakenly confusing the frequency dimension with the number of OFDM symbols in a slot.",
      "49152 subcarriers, which would represent exactly twice the standard resource block capacity."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 2 slots?",
     "28 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["30 symbols, erroneously linking the symbol count to the base subcarrier spacing value.",
      "20 symbols, confusing the symbol count with the number of subframes in a radio frame.",
      "24 symbols, which corresponds to the configuration used for an extended cyclic prefix."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 4 slots?",
     "56 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["48 symbols, which corresponds to the configuration used for an extended cyclic prefix.",
      "60 symbols, erroneously linking the symbol count to the base subcarrier spacing value.",
      "40 symbols, confusing the symbol count with the number of subframes in a radio frame."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 5 slots?",
     "70 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["75 symbols, erroneously linking the symbol count to the base subcarrier spacing value.",
      "60 symbols, which corresponds to the configuration used for an extended cyclic prefix.",
      "50 symbols, confusing the symbol count with the number of subframes in a radio frame."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 8 slots?",
     "112 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["96 symbols, which corresponds to the configuration used for an extended cyclic prefix.",
      "80 symbols, confusing the symbol count with the number of subframes in a radio frame.",
      "120 symbols, erroneously linking the symbol count to the base subcarrier spacing value."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 10 slots?",
     "140 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["150 symbols, erroneously linking the symbol count to the base subcarrier spacing value.",
      "120 symbols, which corresponds to the configuration used for an extended cyclic prefix.",
      "100 symbols, confusing the symbol count with the number of subframes in a radio frame."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 12 slots?",
     "168 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["120 symbols, confusing the symbol count with the number of subframes in a radio frame.",
      "180 symbols, erroneously linking the symbol count to the base subcarrier spacing value.",
      "144 symbols, which corresponds to the configuration used for an extended cyclic prefix."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 15 slots?",
     "210 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["180 symbols, which corresponds to the configuration used for an extended cyclic prefix.",
      "150 symbols, confusing the symbol count with the number of subframes in a radio frame.",
      "225 symbols, erroneously linking the symbol count to the base subcarrier spacing value."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 20 slots?",
     "280 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["200 symbols, confusing the symbol count with the number of subframes in a radio frame.",
      "300 symbols, erroneously linking the symbol count to the base subcarrier spacing value.",
      "240 symbols, which corresponds to the configuration used for an extended cyclic prefix."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 50 slots?",
     "700 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["500 symbols, confusing the symbol count with the number of subframes in a radio frame.",
      "600 symbols, which corresponds to the configuration used for an extended cyclic prefix.",
      "750 symbols, erroneously linking the symbol count to the base subcarrier spacing value."]),

    ("Assuming a normal cyclic prefix in 5G NR, how many OFDM symbols are transmitted over a duration of 100 slots?",
     "1400 symbols, because the standard dictates 14 symbols per slot in this mode.",
     ["1200 symbols, which corresponds to the configuration used for an extended cyclic prefix.",
      "1000 symbols, confusing the symbol count with the number of subframes in a radio frame.",
      "1500 symbols, erroneously linking the symbol count to the base subcarrier spacing value."]),

    ("How does 5G NR utilize orthogonal frequency division multiplexing (OFDM) in its physical layer?",
     "It divides the channel into multiple narrow subcarriers without guard bands, minimizing interference.",
     ["It allocates single wideband channels to each user to maximize individual throughput within typical communication frameworks.",
      "It relies solely on time division multiplexing to separate user signals completely.",
      "It uses extensive guard bands between subcarriers to prevent signal overlap."]),

    ("What characterizes the physical downlink shared channel (PDSCH) in a 5G network?",
     "It carries the primary user data and signaling messages from the base station to devices.",
     ["It is used primarily to broadcast crucial system information across the entire cell.",
      "It manages uplink random access requests initiated by the mobile user equipment.",
      "It transmits acknowledgment messages for successfully received uplink data packets."]),

    ("What role does the MAC protocol play in the 5G NR protocol stack?",
     "It supports multiplexing, prioritization, and scheduling of data across the radio interface.",
     ["It implements baseband OFDM processing and handles the physical MIMO algorithms.",
      "It provides security mechanisms such as ciphering and integrity protection for data.",
      "It maps quality of service flows onto the underlying radio resources for the user plane."]),

    ("In the context of the 5G Service-Based Architecture, what is a Network Function (NF)?",
     "An entity that provides specific network services through standardized service-based interfaces.",
     ["A physical hardware appliance dedicated to converting digital signals into radio waves.",
      "A specialized satellite payload component designed to process baseband data in orbit.",
      "A terrestrial transport link that connects the core network directly to the public internet."]),

    ("How is a subframe defined in the time domain of the 5G NR physical layer?",
     "It is a fixed 1ms time unit that contains a variable number of slots based on numerology.",
     ["It is a flexible time unit whose duration changes depending on the subcarrier spacing.",
      "It is a scheduling unit that consistently contains exactly 14 OFDM symbols in all modes.",
      "It is a 10ms structure that encapsulates all resource blocks transmitted in a single cycle."]),

]

# All 100 questions are compiled, in thematic order, into a single bank.
ALL_QUESTIONS = GROUP_I
OUTPUT_FILE = "compiled_3.json"


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def main():
    rng = random.Random(4563)  # reproducible key placement
    n = len(ALL_QUESTIONS)

    # Balanced key positions: as close to even as possible across the bank.
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
