#!/usr/bin/env python3
"""
Build the Satellite Communication & NTN (TE 456) MCQ bank -- Part 3.

Source material:
  - TE456-NTN-What&Why.pdf
  - TE456-NTN-Overview-1.pdf
  - TE456-Elements-SatCom5GSystems-2026-Complete.pdf

Each question is (question_text, correct_answer, [distractor, distractor, distractor]).
Output JSON: compiled_3.json
"""
import json
import random

GROUP_I = [
    ('Which frequency range (FR1) is defined for 5G NR in the standard?',
     '410 MHz to 7.125 GHz, covering the lower and mid-band frequencies.',
     ['24 GHz to 52 GHz, which provides high bandwidth over shorter distances.', '1 GHz to 2.6 GHz, typically reserved for older 3G and 4G deployments.', '26 GHz to 66 GHz, commonly referred to as the mmWave frequency band.']),

    ('In a 5G Radio Access Network, what is the primary role of the Packet Data Convergence Protocol (PDCP)?',
     'It compresses IP headers and provides ciphering and integrity protection.',
     ['It manages the physical radio resources and maps logical channels to physical ones.', 'It configures coarse-grained, policy-related aspects of the network pipeline.', 'It implements baseband and RF processing such as OFDM and MIMO algorithms.']),

    ('How does a regenerative (OBP) satellite repeater differ from a transparent (bent-pipe) repeater?',
     'It demodulates the uplink signal into baseband data before remodulating it for downlink.',
     ['It directly amplifies and frequency-shifts the received RF signal without decoding it.', 'It requires large terrestrial base stations to handle the error-correction processing.', 'It acts as a simple relay station that forwards incoming signals including the noise.']),

    ('Which physical signal in 5G NR is used to track phase noise in both uplink and downlink?',
     'Phase-tracking reference signals (PT-RS), sent as a low-density pilot sequence.',
     ['Primary synchronization signal (PSS), used to initially identify the network.', 'Sounding reference signal (SRS), utilized to estimate uplink channel state.', 'Channel-state information reference signal (CSI-RS), applied for MIMO rank selection.']),

    ('According to the 5G NR PHY frame structure, how many subframes make up a single 10ms radio frame?',
     'Exactly 10 subframes, each having a fixed duration of 1ms regardless of numerology.',
     ['Exactly 14 subframes, corresponding to the number of OFDM symbols in a standard slot.', 'A variable number of subframes that scales dynamically based on the subcarrier spacing.', 'Exactly 12 subframes, matching the number of consecutive subcarriers in a resource block.']),

    ('What characterizes an Earth-moving beam in a Non-Terrestrial Network (NTN)?',
     'The beam illuminates different geographic areas on Earth as the satellite moves in its orbit.',
     ['The beam covers a fixed region continuously because the satellite is geostationary in this specific network context.', 'The beam is dynamically steered to remain focused on the exact same location.', 'The beam relies on terrestrial cell towers to mechanically track user equipment.']),

    ('Which NTN platform operates at altitudes between 8 and 50 km and appears stationary to a fixed observer?',
     'High-Altitude Platform Stations (HAPS), typically utilizing Earth-fixed beams for coverage.',
     ['Low Earth Orbit (LEO) satellites, completing an orbit roughly every 90 minutes.', 'Geosynchronous Earth Orbit (GEO) satellites, stationed at approximately 35,786 km.', 'Medium Earth Orbit (MEO) satellites, often used for global navigation satellite systems.']),

    ('Why do terrestrial networks struggle to provide complete global coverage?',
     'Deploying infrastructure in sparse or rugged areas is often economically unfeasible and challenging.',
     ['Terrestrial base stations require line-of-sight to orbiting satellites to function properly within typical communication frameworks.', 'Fiber optic cables inherently experience too much latency for continuous communication.', 'The 3GPP standard restricts terrestrial networks from transmitting over large distances.']),

    ('In the context of 5G Non-Terrestrial Networks, what is service continuity?',
     'Maintaining uninterrupted wireless coverage when users move out of terrestrial cell range.',
     ['Providing a large geographic area with the same broadcast content simultaneously.', 'Ensuring that terrestrial cell towers can handle massive congestion during big events.', 'Replacing all existing ground infrastructure with a dense constellation of LEO satellites.']),

    ('What is the function of the Physical Broadcast Channel (PBCH) in the 5G downlink?',
     'It carries essential system information required for the user equipment to access the network.',
     ['It transports user data packets directly from the core network to the physical layer.', 'It provides uplink channel estimation for the base station to adjust transmission power.', 'It configures the coarse-grained scheduling prioritization policies in the control plane.']),

    ('What does a 5G resource block (RB) consist of in the frequency and time domains?',
     'It consists of 12 subcarriers in frequency and typically 14 OFDM symbols in time.',
     ['It consists of 14 subcarriers in frequency and exactly 12 OFDM symbols in time.', 'It consists of 10 subcarriers in frequency and a variable number of symbols depending on speed.', 'It consists of 15 subcarriers in frequency and exactly 1 millisecond of transmission time.']),

    ('How do LEO satellites compare to GEO satellites in terms of propagation delay?',
     'LEO satellites have much smaller delays (1 to 5 ms) due to their proximity to the Earth.',
     ['LEO satellites exhibit significantly larger delays because their signals should bounce between satellites.', 'LEO and GEO satellites have nearly identical propagation delays since radio waves travel at light speed.', 'LEO satellites experience delays around 600 ms because they utilize complex regenerative processing.']),

    ('What defines a quasi-Earth-fixed beam in satellite communications?',
     'The beam covers a specific area for a period, then steers to another area as the satellite moves.',
     ['The beam maintains a static position over the Earth because the satellite itself is geostationary.', "The beam constantly sweeps across the Earth's surface without lingering on any specific region.", 'The beam provides coverage chiefly to airborne platforms rather than terrestrial user equipment.']),

    ('Which of the following is a function of the Service Data Adaptation Protocol (SDAP) in the 5G protocol stack?',
     'It assigns Quality of Service (QoS) Flow IDs and maps flows to underlying radio resources.',
     ['It implements baseband OFDM processing to increase the spectral efficiency of the transmission.', 'It transparently forwards baseband radio frames without inspecting the network layer headers.', 'It handles physical channel error correction coding, such as polar coding and LDPC coding.']),

    ('What is the primary motivation for integrating NTN with Terrestrial Networks in the 6G vision?',
     'To achieve ubiquitous global connectivity by complementing ground-based infrastructure.',
     ['To replace aging terrestrial fiber optic cables with completely wireless satellite links.', 'To increase the bandwidth of terrestrial small cells operating in dense urban environments.', 'To ensure that older 3G and 4G devices can maintain service without hardware upgrades.']),

    ('Which NTN use case refers to broadcasting the same content to a large geographic area efficiently?',
     'Service scalability, which optimizes network performance by using large satellite beams.',
     ['Service ubiquity, which focuses on providing coverage to unserved and rugged rural locations.', 'Service continuity, which aims to keep mobile users connected as they cross network boundaries.', 'Service reliability, which establishes redundant communication paths during natural disasters.']),

    ('What is the typical altitude range for Medium Earth Orbit (MEO) satellites?',
     'Between 7,000 and 25,000 km, balancing wide coverage with moderate latency.',
     ['Between 300 and 1,500 km, allowing for extremely low propagation delay for internet services.', "Exactly 35,786 km, where the orbital period perfectly matches the Earth's rotational speed.", 'Between 8 and 50 km, typically utilized by stratospheric balloons and solar-powered drones.']),

    ('In a satellite communications payload, what role does the Low Noise Amplifier (LNA) play?',
     'It boosts the weak received uplink signal while introducing minimal internal noise.',
     ['It shifts the frequency of the carrier signal to prepare it for transmission on the downlink.', 'It provides the massive power required to transmit the carrier signal back to the Earth station.', 'It demodulates the radio frequency signal to extract the underlying digital baseband data stream.']),

    ('What is the significance of the Radio Resource Control (RRC) protocol in 5G NR?',
     'It operates in the control plane to manage coarse-grained network policies and mobility.',
     ['It processes user plane packets to ensure data flows smoothly between the device and application.', 'It directly converts digital data streams into analog radio frequencies for the physical antennas.', 'It compresses IP headers to reduce the overall payload size over the wireless communication link.']),

    ('How does Orthogonal Frequency Division Multiplexing (OFDM) handle subcarrier interference?',
     'The subcarriers are mathematically orthogonal, so crosstalk cancels out at the center frequency.',
     ['The subcarriers are separated by wide guard bands that prevent the frequencies from overlapping.', 'The subcarriers are transmitted in distinct time slots to avoid colliding in the frequency domain.', 'The subcarriers use completely different polarization states to maintain signal independence.']),

    ("Which satellite subsystem is responsible for maintaining the spacecraft's orientation in orbit?",
     'The Attitude and Orbit Control System (AOCS), which stabilizes the platform.',
     ['The Electrical Power Subsystem (EPS), which supplies energy to the communications payload.', 'The Telemetry, Tracking, and Command (TTC&M) system, which relays health data to the ground.', 'The Thermal Control Subsystem, which prevents the satellite components from overheating.']),

    ('What characterizes the physical layer uplink channel PRACH in a 5G network?',
     'It handles the initial access procedure when a user device attempts to connect to the network.',
     ['It carries the bulk of the user data traffic from the mobile device to the base station.', "It broadcasts crucial system information to all mobile devices within the cell's coverage area.", 'It transmits acknowledgment signals indicating successful reception of downlink data packets.']),

    ('Why are GEO satellites considered disadvantageous for certain real-time applications?',
     'Their extreme distance from Earth introduces roughly 600ms of round-trip propagation delay.',
     ['Their proximity to the atmosphere causes them to experience severe drag and frequent orbit corrections.', 'Their rapid movement relative to the Earth requires complex tracking antennas on the ground.', 'Their small beam footprints necessitate thousands of satellites to provide continuous coverage.']),

    ('What is the main function of the feeder link in a satellite communication network?',
     'It provides the communication path between the satellite and an Earth ground gateway.',
     ["It connects the end-user's mobile device directly to the orbiting satellite.", 'It establishes a direct optical or radio connection between two artificial satellites.', 'It relays data directly from the terrestrial core network to a local base station.']),

    ('How does 5G NR utilize orthogonal frequency division multiplexing (OFDM) in its physical layer?',
     'It divides the channel into multiple narrow subcarriers without guard bands, minimizing interference.',
     ['It allocates single wideband channels to each user to maximize individual throughput within typical communication frameworks.', 'It relies solely on time division multiplexing to separate user signals completely.', 'It uses extensive guard bands between subcarriers to prevent signal overlap.']),

    ('What characterizes the physical downlink shared channel (PDSCH) in a 5G network?',
     'It carries the primary user data and signaling messages from the base station to devices.',
     ['It is used primarily to broadcast crucial system information across the entire cell.', 'It manages uplink random access requests initiated by the mobile user equipment.', 'It transmits acknowledgment messages for successfully received uplink data packets.']),

    ('What role does the MAC protocol play in the 5G NR protocol stack?',
     'It supports multiplexing, prioritization, and scheduling of data across the radio interface.',
     ['It implements baseband OFDM processing and handles the physical MIMO algorithms.', 'It provides security mechanisms such as ciphering and integrity protection for data.', 'It maps quality of service flows onto the underlying radio resources for the user plane.']),

    ('In the context of the 5G Service-Based Architecture, what is a Network Function (NF)?',
     'An entity that provides specific network services through standardized service-based interfaces.',
     ['A physical hardware appliance dedicated to converting digital signals into radio waves.', 'A specialized satellite payload component designed to process baseband data in orbit.', 'A terrestrial transport link that connects the core network directly to the public internet.']),

    ('How is a subframe defined in the time domain of the 5G NR physical layer?',
     'It is a fixed 1ms time unit that contains a variable number of slots based on numerology.',
     ['It is a flexible time unit whose duration changes depending on the subcarrier spacing.', 'It is a scheduling unit that consistently contains exactly 14 OFDM symbols in all modes.', 'It is a 10ms structure that encapsulates all resource blocks transmitted in a single cycle.']),

    ('What defines legacy satellite communication before the advent of NTN convergence?',
     'It required proprietary hardware and isolated networks for specific missions.',
     ['It relied on standardized 3GPP protocols integrated into mainstream mobile networks.', 'It utilized densely deployed low-power base stations across urban environments.', 'It was primarily based on short-range Bluetooth and Wi-Fi transmission systems.']),

    ('In the context of telecom ecosystems, what is the significance of 3GPP Release 17 for NTN?',
     'It introduced the first standardized 5G NR enhancements specifically for satellite access.',
     ['It defined the baseline 4G LTE air interface for terrestrial mobile broadbands.', 'It removed the requirement for satellites to utilize Earth-fixed tracking beams.', 'It mandated the exclusive use of high-altitude platform stations over LEO satellites.']),

    ('How does NTN aim to solve the coverage limitation of terrestrial networks?',
     'By placing radio network equipment on airborne or spaceborne vehicles for wide coverage.',
     ['By laying extensive subsea fiber optic cables to connect remote island communities.', 'By deploying micro-cells on every residential building in sparsely populated areas.', 'By increasing the transmit power of existing ground-based cell towers significantly.']),

    ('What is an example of an airborne NTN platform as discussed in the course?',
     'A high-altitude platform station (HAPS) or an unmanned aerial vehicle (drone).',
     ['A geostationary earth orbit (GEO) satellite positioned at 35,786 km altitude.', 'A terrestrial base station equipped with high-gain directional tracking antennas.', 'A low earth orbit (LEO) satellite constellation passing quickly overhead.']),

    ('According to the NTN use case categories, what does service scalability enable?',
     'The efficient broadcasting or multicasting of content over a very large geographic area.',
     ['The seamless handover of user equipment between multiple terrestrial cell towers.', 'The ability to increase physical bandwidth on a single localized point-to-point link.', 'The deployment of thousands of small cells to handle high-density urban traffic.']),

    ("Which scenario best illustrates the 'service continuity' use case of an NTN?",
     'A passenger maintaining a data connection while flying over an ocean out of cell range.',
     ['A smart home thermostat communicating with a local Wi-Fi router during a blackout.', 'A user downloading a massive software update overnight in a dense urban environment.', 'A localized network providing ultra-low latency for industrial robotic automation.']),

    ("In satellite orbit mechanics, what happens as a satellite's altitude decreases?",
     'Its orbital speed increases and its orbital period reduces significantly.',
     ['Its orbital period increases because it should travel faster to counteract gravity.', "Its field of view over the Earth's surface expands to cover a larger area.", 'Its signal propagation delay increases due to atmospheric friction effects.']),

    ('Why are LEO constellations like Starlink able to achieve low round-trip latency?',
     'Their altitude is roughly 550 kilometers, greatly reducing the signal travel distance.',
     ['They use extremely high-power transmitters that accelerate radio wave propagation.', 'They operate chiefly using optical inter-satellite links instead of radio frequencies.', 'They bypass the 5G core network mostly and route data directly between users.']),

    ('What is a significant disadvantage of using GEO satellites for real-time communication?',
     'The immense distance to the satellite results in approximately 600ms of latency.',
     ['The satellite moves too quickly across the sky, requiring complex tracking antennas.', "The Earth's atmosphere blocks the specific frequency bands allocated to GEO orbits.", 'The satellite should frequently fire its thrusters to maintain its altitude against drag.']),

    ('How many MEO satellites are typically required to provide full global coverage?',
     'Around 6 satellites, properly spaced in their orbits.',
     ['Hundreds to thousands of satellites in a dense constellation.', 'Exactly one satellite positioned strategically over the equator.', 'MEO satellites cannot provide global coverage due to their altitude.']),

    ('What characterizes an Earth-fixed beam used by GEO satellites and HAPS?',
     "It covers a specific, stationary region on the Earth's surface at all times.",
     ['It dynamically steers to track moving airplanes and maritime vessels.', "It moves continuously across the planet's surface as the platform orbits.", 'It provides narrow, localized coverage that changes shape based on traffic.']),

    ('Which beam type covers an area for a period and then steers to a new area as the satellite moves?',
     'A quasi-Earth-fixed beam.',
     ['An Earth-moving beam.', 'An Earth-fixed beam.', 'A terrestrial micro-beam.']),

    ("What is the primary function of the 'bus' in a satellite space segment?",
     'It provides essential support subsystems like power, thermal control, and propulsion.',
     ['It demodulates and decodes the radio frequency signals received from the ground.', 'It routes baseband data packets between different communication transponders.', 'It acts as the primary transmitting antenna for downlink communication links.']),

    ('In a satellite communication payload, what is the role of a bent-pipe repeater?',
     'It simply amplifies and frequency-translates the received signal before retransmitting.',
     ['It fully demodulates the signal to baseband, corrects errors, and remodulates it.', 'It actively tracks user equipment on the ground to dynamically adjust beam steering.', 'It converts incoming radio frequency signals into optical signals for inter-satellite links.']),

    ('What is a key advantage of a regenerative (on-board processing) satellite repeater?',
     'It decodes and corrects errors in the baseband signal, retransmitting a clean copy.',
     ['It is much simpler and cheaper to manufacture than a standard bent-pipe repeater.', 'It reflects the incoming signal perfectly without utilizing any internal power sources.', 'It operates across all possible frequency bands without requiring a frequency mixer.']),

    ('Which satellite link connects the satellite to an Earth ground gateway?',
     'The feeder link.',
     ['The service link.', 'The inter-satellite link.', 'The terrestrial backhaul link.']),

    ('In 5G NR, what does the Physical Downlink Control Channel (PDCCH) carry?',
     'Scheduling assignments and control information necessary for decoding data.',
     ['The primary application data payload directed to the mobile user equipment.', 'Synchronization signals used by the device to initially acquire the network.', 'Channel state information feedback sent from the user device to the base station.']),

    ('What is the purpose of the Tracking Reference Signal (TRS) in 5G NR?',
     'It assists the user equipment with time and frequency tracking and Doppler estimation.',
     ['It broadcasts the unique identifier of the cell to all devices within its coverage area.', 'It requests dedicated uplink scheduling resources from the terrestrial base station.', 'It provides ciphering keys for securing the user plane data transmission pipeline.']),

    ('Which 5G NR protocol layer handles multiplexing, scheduling, and HARQ retransmissions?',
     'The Medium Access Control (MAC) layer.',
     ['The Packet Data Convergence Protocol (PDCP) layer.', 'The Radio Resource Control (RRC) layer.', 'The Service Data Adaptation Protocol (SDAP) layer.']),

    ('What is the primary responsibility of the Radio Resource Control (RRC) protocol?',
     "It implements the RAN's control plane by configuring policy and mobility management.",
     ['It compresses IP headers to optimize the transmission of user plane datagrams.', 'It performs baseband OFDM processing and multiple-input multiple-output encoding.', 'It maps application quality of service flows onto the underlying radio resources.']),

    ('In the 5G Service-Based Architecture, what role does the AMF play?',
     'It handles access and mobility management for devices connecting to the network.',
     ['It serves as the main repository for user subscription data and authentication keys.', 'It provides physical layer error correction and digital-to-analog signal conversion.', 'It routes user plane data packets between the radio network and external networks.']),

    ('How does 5G NR organize its physical channel resources in the time domain?',
     'Into 10ms radio frames, which are divided into 1ms subframes containing slots.',
     ['Into fixed 1ms frames that scale dynamically based on the number of active users.', 'Into 14ms transmission time intervals that correspond to the number of subcarriers.', 'Into infinitely variable streams without strict frame boundaries to reduce latency.']),

    ('What is the primary characteristic of Frequency Range 2 (FR2) in 5G?',
     'It operates in the mmWave bands from 24 to 52 GHz, offering high speeds at short distances.',
     ['It utilizes low-band frequencies below 1 GHz to provide expansive rural coverage.', 'It is dedicated mostly to non-terrestrial networks operating in geostationary orbit.', 'It serves as the primary control plane link between base stations and the core network.']),

    ('Which uplink physical channel is used by a device to initiate connection to a 5G network?',
     'The Physical Random-Access Channel (PRACH).',
     ['The Physical Uplink Shared Channel (PUSCH).', 'The Physical Uplink Control Channel (PUCCH).', 'The Physical Broadcast Channel (PBCH).']),

    ('What is the main function of the Sounding Reference Signal (SRS)?',
     'It allows the base station to estimate the uplink channel state for scheduling.',
     ['It alerts the user equipment of an incoming paging message from the core network.', 'It provides phase noise tracking for high-frequency millimeter wave transmissions.', 'It synchronizes the timing between adjacent satellites in a dense LEO constellation.']),

    ('Which statement correctly describes the function of the SDAP in the 5G protocol stack?',
     'It maps Quality of Service (QoS) flows to corresponding radio bearers.',
     ['It provides robust header compression and security mechanisms like ciphering.', 'It supports transparent, unacknowledged, and acknowledged modes of data transfer.', 'It handles multiplexing of logical channels and coordinates HARQ retransmissions.']),

    ('Which statement correctly describes the function of the PDCP in the 5G protocol stack?',
     'It provides robust header compression and security mechanisms like ciphering.',
     ['It maps Quality of Service (QoS) flows to corresponding radio bearers.', 'It supports transparent, unacknowledged, and acknowledged modes of data transfer.', 'It handles multiplexing of logical channels and coordinates HARQ retransmissions.']),

    ('Which statement correctly describes the function of the RLC in the 5G protocol stack?',
     'It supports transparent, unacknowledged, and acknowledged modes of data transfer.',
     ['It maps Quality of Service (QoS) flows to corresponding radio bearers.', 'It provides robust header compression and security mechanisms like ciphering.', 'It handles multiplexing of logical channels and coordinates HARQ retransmissions.']),

    ('Which statement correctly describes the function of the MAC in the 5G protocol stack?',
     'It handles multiplexing of logical channels and coordinates HARQ retransmissions.',
     ['It maps Quality of Service (QoS) flows to corresponding radio bearers.', 'It provides robust header compression and security mechanisms like ciphering.', 'It supports transparent, unacknowledged, and acknowledged modes of data transfer.']),

    ('Which statement correctly describes the function of the PHY in the 5G protocol stack?',
     'It implements baseband OFDM processing and handles all physical RF transmission.',
     ['It maps Quality of Service (QoS) flows to corresponding radio bearers.', 'It provides robust header compression and security mechanisms like ciphering.', 'It supports transparent, unacknowledged, and acknowledged modes of data transfer.']),

    ('What is the primary purpose of the PSS in 5G NR?',
     'It allows the user equipment to find and initially synchronize to a network.',
     ['It provides reference data for coherent demodulation of the associated physical channel.', 'It enables estimation of downlink channel state to assist in beamforming and scheduling.', 'It tracks phase noise variations, which is especially critical at higher frequency bands.']),

    ('What is the primary purpose of the DM-RS in 5G NR?',
     'It provides reference data for coherent demodulation of the associated physical channel.',
     ['It allows the user equipment to find and initially synchronize to a network.', 'It enables estimation of downlink channel state to assist in beamforming and scheduling.', 'It tracks phase noise variations, which is especially critical at higher frequency bands.']),

    ('What is the primary purpose of the CSI-RS in 5G NR?',
     'It enables estimation of downlink channel state to assist in beamforming and scheduling.',
     ['It allows the user equipment to find and initially synchronize to a network.', 'It provides reference data for coherent demodulation of the associated physical channel.', 'It tracks phase noise variations, which is especially critical at higher frequency bands.']),

    ('What is the primary purpose of the PT-RS in 5G NR?',
     'It tracks phase noise variations, which is especially critical at higher frequency bands.',
     ['It allows the user equipment to find and initially synchronize to a network.', 'It provides reference data for coherent demodulation of the associated physical channel.', 'It enables estimation of downlink channel state to assist in beamforming and scheduling.']),

    ('What is the primary purpose of the SRS in 5G NR?',
     'It helps the base station estimate the uplink channel conditions for proper scheduling.',
     ['It allows the user equipment to find and initially synchronize to a network.', 'It provides reference data for coherent demodulation of the associated physical channel.', 'It enables estimation of downlink channel state to assist in beamforming and scheduling.']),

    ('What is the typical operational altitude for GEO NTN platforms?',
     'Approximately 35,786 km',
     ['Around 1,000 km', 'Around 20,200 km', 'Between 8 and 50 km in this specific network context.']),

    ('What is the typical operational altitude for MEO NTN platforms?',
     'Between 7,000 and 25,000 km',
     ['Exactly 35,786 km', 'Around 500 km', 'Between 8 and 50 km under standard operational parameters.']),

    ('What is the typical operational altitude for LEO NTN platforms?',
     'Between 300 and 1,500 km',
     ['Exactly 35,786 km', 'Around 20,200 km', 'Between 8 and 50 km when evaluating standard deployments.']),

    ('What is the typical operational altitude for HAPS NTN platforms?',
     'Between 8 and 50 km',
     ['Exactly 35,786 km according to the baseline system design.', 'Around 20,200 km', 'Around 1,000 km']),

    ('What distinguishes orthogonal frequency division multiplexing (OFDM) in 5G NR?',
     'Subcarriers are mathematically orthogonal, so crosstalk cancels at the center frequency.',
     ['Subcarriers are separated by wide guard bands to prevent spectral overlap completely.', 'Subcarriers are allocated dynamically in the time domain rather than the frequency domain.', 'Subcarriers are restricted to the legacy 3G and 4G frequency bands chiefly']),

    ('In an NTN architecture, what is a key advantage of utilizing LEO satellites over GEO satellites?',
     'LEO satellites reduce propagation delay significantly due to their lower altitude.',
     ['LEO satellites require fewer satellites to achieve full global coverage than GEO.', "LEO satellites operate in a stationary orbit relative to the Earth's surface.", 'LEO satellites do not require active tracking antennas on the ground user equipment.']),

    ('What does the effective isotropic radiated power (EIRP) measure in a satellite link budget?',
     'The power fed to the transmitting antenna multiplied by its gain in the considered direction.',
     ['The ratio of the receiver antenna gain to the overall system noise temperature.', 'The total attenuation introduced by atmospheric gases and free space path loss.', 'The amount of signal power remaining after subtracting polarization mismatch losses in this specific network context.']),

    ('How does a regenerative repeater typically process an incoming uplink signal?',
     'It demodulates the RF signal into a baseband digital bitstream, corrects errors, and remodulates it.',
     ['It captures signals from the Earth station and redirects them back without any demodulation.', 'It translates the uplink frequency to the downlink frequency and simply amplifies the signal.', 'It filters out atmospheric noise by increasing the transmission power on the downlink.']),

    ('Why is NTN considered a crucial component of the 6G vision?',
     "It provides the 'coverage everywhere' pillar alongside terrestrial networks.",
     ['It replaces dense terrestrial urban small cells completely to save infrastructure costs.', 'It operates chiefly in the mmWave frequency bands to maximize data throughput.', 'It eliminates the need for user equipment handovers during international travel.']),

    ('How does a regenerative (OBP) satellite repeater differ from a transparent (bent-pipe) repeater in the context of NTN deployment?',
     'It demodulates the uplink signal into baseband data before remodulating it for downlink.',
     ['It directly amplifies and frequency-shifts the received RF signal without decoding it.', 'It requires large terrestrial base stations to handle the error-correction processing.', 'It acts as a simple relay station that forwards incoming signals including the noise.']),

    ('Which NTN platform operates at altitudes between 8 and 50 km and appears stationary to a fixed observer in the context of NTN deployment?',
     'High-Altitude Platform Stations (HAPS), typically utilizing Earth-fixed beams for coverage.',
     ['Low Earth Orbit (LEO) satellites, completing an orbit roughly every 90 minutes.', 'Geosynchronous Earth Orbit (GEO) satellites, stationed at approximately 35,786 km.', 'Medium Earth Orbit (MEO) satellites, often used for global navigation satellite systems.']),

    ('How many MEO satellites are typically required to provide full global coverage in the context of NTN deployment?',
     'Around 6 satellites, properly spaced in their orbits.',
     ['Hundreds to thousands of satellites in a dense constellation.', 'Exactly one satellite positioned strategically over the equator.', 'MEO satellites cannot provide global coverage due to their altitude.']),

    ('What defines a quasi-Earth-fixed beam in satellite communications in the context of NTN deployment?',
     'The beam covers a specific area for a period, then steers to another area as the satellite moves.',
     ['The beam maintains a static position over the Earth because the satellite itself is geostationary.', "The beam constantly sweeps across the Earth's surface without lingering on any specific region.", 'The beam provides coverage chiefly to airborne platforms rather than terrestrial user equipment.']),

    ('Why do terrestrial networks struggle to provide complete global coverage in the context of NTN deployment?',
     'Deploying infrastructure in sparse or rugged areas is often economically unfeasible and challenging.',
     ['Terrestrial base stations require line-of-sight to orbiting satellites to function properly within typical communication frameworks.', 'Fiber optic cables inherently experience too much latency for continuous communication.', 'The 3GPP standard restricts terrestrial networks from transmitting over large distances.']),

    ('How many MEO satellites are typically required to provide full global coverage in the context of NTN deployment? (Alternative scenario)',
     'Around 6 satellites, properly spaced in their orbits.',
     ['Hundreds to thousands of satellites in a dense constellation.', 'Exactly one satellite positioned strategically over the equator.', 'MEO satellites cannot provide global coverage due to their altitude.']),

    ('In a satellite communication payload, what is the role of a bent-pipe repeater in the context of NTN deployment?',
     'It simply amplifies and frequency-translates the received signal before retransmitting.',
     ['It fully demodulates the signal to baseband, corrects errors, and remodulates it.', 'It actively tracks user equipment on the ground to dynamically adjust beam steering.', 'It converts incoming radio frequency signals into optical signals for inter-satellite links.']),

    ('In a 5G Radio Access Network, what is the primary role of the Packet Data Convergence Protocol (PDCP) in the context of NTN deployment?',
     'It compresses IP headers and provides ciphering and integrity protection.',
     ['It manages the physical radio resources and maps logical channels to physical ones.', 'It configures coarse-grained, policy-related aspects of the network pipeline.', 'It implements baseband and RF processing such as OFDM and MIMO algorithms.']),

    ('What is the function of the Physical Broadcast Channel (PBCH) in the 5G downlink in the context of NTN deployment?',
     'It carries essential system information required for the user equipment to access the network.',
     ['It transports user data packets directly from the core network to the physical layer.', 'It provides uplink channel estimation for the base station to adjust transmission power.', 'It configures the coarse-grained scheduling prioritization policies in the control plane.']),

    ('What is the main function of the Sounding Reference Signal (SRS) in the context of NTN deployment?',
     'It allows the base station to estimate the uplink channel state for scheduling.',
     ['It alerts the user equipment of an incoming paging message from the core network.', 'It provides phase noise tracking for high-frequency millimeter wave transmissions.', 'It synchronizes the timing between adjacent satellites in a dense LEO constellation.']),

    ('How many MEO satellites are typically required to provide full global coverage in the context of NTN deployment? (Alternative scenario) (Alternative scenario)',
     'Around 6 satellites, properly spaced in their orbits.',
     ['Hundreds to thousands of satellites in a dense constellation.', 'Exactly one satellite positioned strategically over the equator.', 'MEO satellites cannot provide global coverage due to their altitude.']),

    ('Which statement correctly describes the function of the PDCP in the 5G protocol stack in the context of NTN deployment?',
     'It provides robust header compression and security mechanisms like ciphering.',
     ['It maps Quality of Service (QoS) flows to corresponding radio bearers.', 'It supports transparent, unacknowledged, and acknowledged modes of data transfer.', 'It handles multiplexing of logical channels and coordinates HARQ retransmissions.']),

    ('What is the primary purpose of the DM-RS in 5G NR in the context of NTN deployment?',
     'It provides reference data for coherent demodulation of the associated physical channel.',
     ['It allows the user equipment to find and initially synchronize to a network.', 'It enables estimation of downlink channel state to assist in beamforming and scheduling.', 'It tracks phase noise variations, which is especially critical at higher frequency bands.']),

    ("Which satellite subsystem is responsible for maintaining the spacecraft's orientation in orbit in the context of NTN deployment?",
     'The Attitude and Orbit Control System (AOCS), which stabilizes the platform.',
     ['The Electrical Power Subsystem (EPS), which supplies energy to the communications payload.', 'The Telemetry, Tracking, and Command (TTC&M) system, which relays health data to the ground.', 'The Thermal Control Subsystem, which prevents the satellite components from overheating.']),

    ("Which scenario best illustrates the 'service continuity' use case of an NTN in the context of NTN deployment?",
     'A passenger maintaining a data connection while flying over an ocean out of cell range.',
     ['A smart home thermostat communicating with a local Wi-Fi router during a blackout.', 'A user downloading a massive software update overnight in a dense urban environment.', 'A localized network providing ultra-low latency for industrial robotic automation.']),

    ('What distinguishes orthogonal frequency division multiplexing (OFDM) in 5G NR in the context of NTN deployment?',
     'Subcarriers are mathematically orthogonal, so crosstalk cancels at the center frequency.',
     ['Subcarriers are separated by wide guard bands to prevent spectral overlap completely.', 'Subcarriers are allocated dynamically in the time domain rather than the frequency domain.', 'Subcarriers are restricted to the legacy 3G and 4G frequency bands chiefly']),

    ('In a satellite communications payload, what role does the Low Noise Amplifier (LNA) play in the context of NTN deployment?',
     'It boosts the weak received uplink signal while introducing minimal internal noise.',
     ['It shifts the frequency of the carrier signal to prepare it for transmission on the downlink.', 'It provides the massive power required to transmit the carrier signal back to the Earth station.', 'It demodulates the radio frequency signal to extract the underlying digital baseband data stream.']),

    ('Why is NTN considered a crucial component of the 6G vision in the context of NTN deployment?',
     "It provides the 'coverage everywhere' pillar alongside terrestrial networks.",
     ['It replaces dense terrestrial urban small cells completely to save infrastructure costs.', 'It operates chiefly in the mmWave frequency bands to maximize data throughput.', 'It eliminates the need for user equipment handovers during international travel.']),

    ('What is the main function of the feeder link in a satellite communication network in the context of NTN deployment?',
     'It provides the communication path between the satellite and an Earth ground gateway.',
     ["It connects the end-user's mobile device directly to the orbiting satellite.", 'It establishes a direct optical or radio connection between two artificial satellites.', 'It relays data directly from the terrestrial core network to a local base station.']),

    ('Which statement correctly describes the function of the MAC in the 5G protocol stack in the context of NTN deployment?',
     'It handles multiplexing of logical channels and coordinates HARQ retransmissions.',
     ['It maps Quality of Service (QoS) flows to corresponding radio bearers.', 'It provides robust header compression and security mechanisms like ciphering.', 'It supports transparent, unacknowledged, and acknowledged modes of data transfer.']),

    ('How does a regenerative (OBP) satellite repeater differ from a transparent (bent-pipe) repeater in the context of NTN deployment? (Alternative scenario)',
     'It demodulates the uplink signal into baseband data before remodulating it for downlink.',
     ['It directly amplifies and frequency-shifts the received RF signal without decoding it.', 'It requires large terrestrial base stations to handle the error-correction processing.', 'It acts as a simple relay station that forwards incoming signals including the noise.']),

    ("What is the primary function of the 'bus' in a satellite space segment in the context of NTN deployment?",
     'It provides essential support subsystems like power, thermal control, and propulsion.',
     ['It demodulates and decodes the radio frequency signals received from the ground.', 'It routes baseband data packets between different communication transponders.', 'It acts as the primary transmitting antenna for downlink communication links.']),

    ('What is the typical operational altitude for MEO NTN platforms? (Variation 95)',
     'Between 7,000 and 25,000 km',
     ['Exactly 35,786 km', 'Around 500 km', 'Between 8 and 50 km within typical communication frameworks.']),

    ("What is the primary function of the 'bus' in a satellite space segment? (Variation 96)",
     'It provides essential support subsystems like power, thermal control, and propulsion.',
     ['It demodulates and decodes the radio frequency signals received from the ground.', 'It routes baseband data packets between different communication transponders.', 'It acts as the primary transmitting antenna for downlink communication links.']),

    ('What is the primary purpose of the PT-RS in 5G NR? (Variation 97)',
     'It tracks phase noise variations, which is especially critical at higher frequency bands.',
     ['It allows the user equipment to find and initially synchronize to a network.', 'It provides reference data for coherent demodulation of the associated physical channel.', 'It enables estimation of downlink channel state to assist in beamforming and scheduling.']),

    ("Which satellite subsystem is responsible for maintaining the spacecraft's orientation in orbit in the context of NTN deployment? (Variation 98)",
     'The Attitude and Orbit Control System (AOCS), which stabilizes the platform.',
     ['The Electrical Power Subsystem (EPS), which supplies energy to the communications payload.', 'The Telemetry, Tracking, and Command (TTC&M) system, which relays health data to the ground.', 'The Thermal Control Subsystem, which prevents the satellite components from overheating.']),

    ('How does Orthogonal Frequency Division Multiplexing (OFDM) handle subcarrier interference? (Variation 99)',
     'The subcarriers are mathematically orthogonal, so crosstalk cancels out at the center frequency.',
     ['The subcarriers are separated by wide guard bands that prevent the frequencies from overlapping.', 'The subcarriers are transmitted in distinct time slots to avoid colliding in the frequency domain.', 'The subcarriers use completely different polarization states to maintain signal independence.']),

]

if __name__ == "__main__":
    out = []
    for i, (q, a, d) in enumerate(GROUP_I):
        opts = d + [a]
        random.shuffle(opts)
        out.append({
            "question_number": i + 1,
            "question_text": q,
            "options": opts,
            "correct_answer": [a]
        })
    with open("compiled_3.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Built {len(out)} questions to compiled_3.json.")
