# TE 456 Presentation Decks - Study Guide

This is the companion guide to **Part 4** of the TE 456 question bank
(`compiled_4.json`, 240 questions). It writes out the content of all 24 student
presentation decks as continuous text, one section per deck, in the same order
the bank uses.

## Why this guide exists

The decks are image heavy. Many slides carry a title and nothing else, and the
real content sits inside a diagram, a table or a figure. Reading the slide text
alone gives you the headings and none of the substance. Every deck was therefore
rendered slide by slide and read as a picture, and this guide is the result.

Where a number appears here (a delay in microseconds, a Doppler figure in
kilohertz, a latency band in milliseconds) it came off a slide, and the matching
question in the bank rests on it.

## How to use it

- Read the deck section, then answer that deck's ten questions in the practice
  site or in `TE456-Presentation-Decks-MCQs-with-answers.pdf`.
- Each question in the bank names its deck in the `topic` field and names the
  slides in the `source` field, so a wrong answer points you back here.

## Cross-cutting ideas

Six themes recur across the decks. Recognising them makes most of the material
one problem seen from different angles.

**1. The cell moves.** In a terrestrial network the tower is fixed and the user
moves. In LEO the reverse dominates. A stationary user is handed over every few
minutes, a beam plan is stale within seconds, and a measurement is out of date
by the time it is acted on. Groups 8, 12, 16 and the predictive handover deck
all start here.

**2. Predict, then correct.** Because orbits are deterministic, the geometry can
be computed in advance. Almost every solution in these decks is an open loop
that predicts from ephemeris followed by a closed loop that measures the
residual. Groups 1, 15 and 21 are three views of exactly this pattern.

**3. Delay breaks protocols built for the ground.** Anything that waits for an
acknowledgement suffers. The RACH needs two round trips before any data moves
(Groups 3 and 17), HARQ processes stall while acknowledgements are in flight
(Group 23), a CSI report is stale on arrival (Group 11), and a URLLC latency
budget simply cannot be met (Group 16).

**4. SWaP is the universal ceiling.** Size, weight and power. Every AI or
machine learning proposal in these decks ends at the same wall: onboard compute
costs power that the payload needs, generates heat that cannot be vented in
vacuum, and runs on radiation-hardened processors generations behind the ground.
Groups 3, 9, 12, 14, 22 and the two AI decks all name it.

**5. Every gain is paid for.** The decks are consistent about cost. Higher
throughput costs collisions. More HARQ processes cost memory. Slice isolation
costs capacity. Predictive handover costs battery, signalling and reserved
resources. If an answer option claims a benefit with no cost, be suspicious.

**6. Geometry is the source of the numbers.** Doppler is the radial component of
velocity, so it peaks near the horizon and crosses zero overhead. Differential
delay comes from the beam edge being further away than the beam centre. Path
loss is why a 20 km HAPS beats a 500 km LEO to an unmodified handset by about
28 dB. The figures are not arbitrary.

---

## Group 1 - Optimized timing advance and frequency offset compensation in LEO NTN

A LEO satellite flies at 600 to 1,200 km and moves at about 7.8 km/s. That gives
a low-latency link, and it creates two problems a terrestrial cell never has.
The distance is large and it changes every second. The relative speed is high and
it also changes every second.

**Problem one is propagation delay.** An uplink must arrive inside a narrow time
window at the base station. On the ground the round-trip time is short and stable
for minutes or hours. On a LEO link it is much longer and it changes within
minutes. The correction is **timing advance**: the device transmits early by the
propagation delay so the signal lands on time.

**Problem two is Doppler shift.** The satellite closes on the user and then
recedes, so the received carrier is shifted up and then down. The correction is
**frequency offset compensation**.

Both corrections use the same two-stage pattern.

**Open loop, or proactive.** The device and the base station both know where the
satellite is, because the orbit is published as ephemeris, and the device knows
its own position from GNSS. From the two positions it computes the range, halves
the round trip, and applies the timing advance before it sends its first PRACH
preamble. For frequency it computes the radial velocity from the ephemeris,
estimates Doppler as `fD = (Vr / c) x fc`, and shifts its transmit frequency
before sending.

**Closed loop, or reactive.** The prediction is never perfect. The base station
measures how early or late the uplink actually arrived, computes a correction,
and returns it as a **timing advance command** in a MAC control element. The
device applies that delta. For frequency, an AFC loop or a PLL estimates the
residual and a numerically controlled oscillator adjusts until the residual is
small enough for the demodulator.

Note the division of labour across the two link segments. The device
pre-corrects the **service link**, between the user and the satellite. The
network corrects the **feeder link**, between the satellite and the gateway. In
a transparent payload both segments contribute Doppler, so the total roughly
doubles.

Applications given: military and tactical communications, optical inter-satellite
frequency transfer, and LEO-to-LoRa gateway architectures.

Four limitations. **Hardware cost**, because the device needs dual-frequency
GNSS, a wideband front end and an enhanced baseband. **Signalling overhead**,
because frequent TA commands and AFC updates consume capacity that could carry
data. **Correction lag**, because feedback always trails the true geometry by at
least one round trip. **Model accuracy**, because open-loop prediction is only as
good as the GNSS fix and the freshness of the ephemeris.

The conclusion in one sentence: predict from known geometry, then refine from
real measurement.

---

## Group 2 - UAV-enhanced 3D beamforming for rural 5G NTN

Rural areas have sparse cellular infrastructure, because towers are expensive
where users are few and far apart. The proposal is to fly the base station
instead of building it. A UAV carries a radio payload, acts as an aerial base
station, serves users below, and reaches the core through a terrestrial link or a
satellite.

**3D beamforming** is the second half. A terrestrial antenna steers mostly in
azimuth. A UAV sits above its users, so the useful angle is as much vertical as
horizontal. Steering in both azimuth and elevation improves coverage, signal
quality and spectrum efficiency together.

Three problems make it hard. **Terrain blockage and coverage gaps**, because
hills and vegetation cut the line of sight and a fixed tower cannot move around
them. **Beam misalignment from UAV mobility**, because the platform moves and
tilts, so a beam aimed correctly one moment points at empty ground the next.
**Dynamic user distribution**, because users are unevenly spread and do not stay
still.

The mechanism has four parts.

**3D-aware placement.** Position is chosen in three dimensions. Altitude is a
real decision variable, because it trades line-of-sight probability against path
loss.

**Hybrid beamforming.** A baseband digital precoder feeds an analog phase-shift
network, which feeds the array. The point is that it uses **fewer RF chains than
antenna elements**, which gives narrow, steerable beams at low SWaP. Predictive
beam tracking then updates the weights as the UAV and the users move, holding
alignment without an exhaustive re-search.

**A closed AI control loop.** Sense channel and user state, optimize 3D position
and beam weights, act by repositioning and steering, learn by updating a
reinforcement-learning model.

**Multi-tier backhaul.** UAVs relay through neighbouring UAVs over a mesh, then
up to a HAPS or satellite feeder link. No fibre and no tower in the target area.

Applications: rural education and distance learning, temporary event coverage,
border surveillance, post-disaster response.

The limitations are systemic. **Power consumption** from the beamforming
hardware and the AI loop competes directly with flight power, cutting endurance.
**Control-loop latency** means the cycle takes time to converge, causing brief
link-quality dips during fast movement. **Hardware cost and weight** rise with
every RF chain, phase shifter and compute module, and scale badly across a
fleet. **Backhaul fragility** means one weak link in a mesh-to-satellite chain
degrades everything downstream.

The conclusion: the constraint is not any single link. Altitude, beam accuracy,
terrain and backhaul must be optimized together.

---

## Group 3 - Machine learning for RACH optimization in NTN

The Random Access Channel is the first thing a device uses. Before a byte of
user data moves, a four-message handshake must complete. Message 1 is the PRACH
preamble from the device, message 2 the random access response, message 3 the
RRC connection request, message 4 contention resolution. **Four messages is two
full round trips.** On the ground that costs about a millisecond. Over a
satellite it costs tens of milliseconds. The RACH is the first mechanism that NTN
breaks.

Four specific problems.

**Long delay.** Tens of milliseconds per round trip, so every retry is expensive.

**Doppler shift.** Over one pass of a 600 km LEO satellite at 2 GHz the offset
swings from about **+48 kHz to -48 kHz** and reverses sign. This smears the
preamble, so the receiver correlates against a shape that no longer matches.

**Contention.** Thousands of devices share one beam and the preamble is chosen at
random, so two devices can pick the same one. Both must retry a round trip later.

**Differential delay.** A device at the beam edge is further away than one at the
beam centre, so its preamble arrives later. Across a narrow LEO beam that
difference is about **650 microseconds**. The longest cyclic prefix protecting a
preamble is **684 microseconds**. Only about **34 microseconds of margin** is
left, and wider beams or higher orbits erase it.

The mechanism is a closed learning loop: **observe** collisions, load and
ephemeris; **decide** the next settings; **act** by setting barring, backoff and
preamble parameters; devices attempt access in the RACH window; **learn** by
updating the policy from a reward combining success, delay and energy.

Three families of technique.

**Supervised or deep learning:** neural preamble detection, timing-advance
estimation, frequency-offset estimation. Runs at the receiver.

**Reinforcement learning:** Q-learning, DQN and PPO tune the barring
probability and the backoff window, and partition the preamble pool.

**Predictive or ephemeris-aided:** the orbit is known in advance, so the device
pre-compensates delay and Doppler and the network pre-allocates access
occasions. This third family is not learning at all. It is deterministic
geometry, and it is the **3GPP Release 17 baseline that any learned policy must
beat**.

Reported gains from eRACH simulations: **+31.2%** throughput for eRACH, **+54.6%**
for the cooperative variant, and **1.49x** lower access delay. The cost is a
**4.94x higher collision rate**.

Limitations split in two. On the satellite: power and compute limits, because a
learned policy competes with a fixed solar budget; heat dissipation, because
inference generates heat with no way to vent it in vacuum; control-loop latency,
because by the time a decision is made the beam may serve different users. In
the design process: scarce training data, because no large public set of real
NTN random-access traces exists; a simulation-to-reality gap; and difficulty
generalising across geometries or certifying a black box against 3GPP
conformance.

---

## Group 4 - GPS signal integration and augmentation in 5G-NTN

Accurate positioning is a basic requirement for modern wireless applications, and
traditionally it comes from GPS. GPS gives global coverage and good accuracy
under open sky, but performance falls badly in urban canyons, dense forest,
tunnels and indoors, where the signal is weak and the sky view is blocked.

5G-NTN extends terrestrial 5G with platforms above the Earth, such as LEO
satellites and HAPS, serving regions where a terrestrial base station cannot be
built. Because neither system alone is good everywhere, the two are combined
into a hybrid.

GPS has three segments. The **space segment** transmits signals letting a
receiver determine location, speed and time. The **control segment** is the
ground infrastructure monitoring and managing the constellation. The **user
segment** is the receivers and the devices or people using them.

In the hybrid, GPS satellites broadcast ephemeris and the receiver estimates
position by trilateration. At the same time 5G-NTN platforms supply extra
measurements.

**Time of Arrival (ToA).** Measure travel time, convert to distance with
`d = c x dt`. Longer travel time means greater distance.

**Angle of Arrival (AoA).** An antenna array measures the arrival direction.
Different nodes measure different angles, and the intersection of the direction
lines gives the location.

**Round Trip Time (RTT).** A node sends, the device replies, the node measures
the total delay and halves it. Several nodes are combined.

Augmentation then corrects residual GPS error.

**SBAS.** Ground reference stations detect GPS errors and pass them to a master
control station, which builds correction messages and uploads them to a
geostationary satellite, which broadcasts them. Accuracy improves from **5 to
10 m down to about 1 to 2 m**.

**DGPS.** A base station at a precisely surveyed location compares its known
coordinates with its GPS-computed coordinates; the difference is the error, which
it broadcasts to nearby receivers. About **1 to 3 m**.

**RTK.** Base and rover both receive carrier-phase signals; the base sends
real-time corrections over radio, internet or cellular. Using carrier phase the
rover reaches **1 to 2 cm**.

**PPP.** Global monitoring stations compute precise orbit and clock corrections,
delivered to the receiver, which combines GNSS signals, corrections and error
models. **No nearby base station is required.** After convergence, about
**5 to 20 cm**.

Benefits: reduced GPS errors, improved accuracy, improved reliability, better
navigation for autonomous systems, better emergency response. Applications:
autonomous vehicles and drones, emergency response, aviation and maritime
navigation, IoT and asset tracking, smart cities.

The chain: GPS, then 5G-NTN, then augmentation, then enhanced positioning.

---

## Group 5 - HAPS-based disaster recovery with 5G core integration

When an earthquake, flood or storm strikes, towers fall and power is cut. Phones
lose signal and the area falls silent. Rescue teams cannot talk to each other or
reach people who need help. A fast, tower-free system is needed.

A **High Altitude Platform Station** is a stratospheric platform at about 20 km.
It sits between ground towers at 30 to 50 m and satellites at 500 to 1,200 km for
LEO. It is a **cell tower in the sky**: a standard 5G base station flown at
altitude, not a satellite payload, so **unmodified handsets attach with no
special terminal or dish**. It is a temporary layer by design, deployed when the
ground network fails and withdrawn once ground service returns.

Six steps. Disaster strikes and the ground network goes offline. A HAPS is
launched or switched on. Phones link wirelessly to the HAPS. The HAPS forwards
traffic to a gateway. The gateway connects into the 5G core. The core delivers to
services and the internet.

The architecture matters. The HAPS carries a **regenerative payload**: the
platform hosts the gNB itself, split as CU plus DU, together with a
**local-breakout UPF**. Because the User Plane Function is on board, responder
traffic is switched locally and never leaves the disaster zone. The ground core
still authenticates through the AMF and manages sessions through the SMF, and
still routes traffic to external networks. The payload terminates standard 3GPP
interfaces, so no new network-function types are needed. The service link is
direct-to-unmodified-smartphone; the feeder link to the gateway is Ka-band,
roughly 20 to 30 GHz.

The comparison table is the core quantitative content.

| KPI | HAPS | LEO | MEO | GEO |
|---|---|---|---|---|
| End-to-end latency | 1 to 10 ms | 20 to 60 ms | 60 to 200 ms | 480 to 560 ms |
| Downlink user rate | ~500 Mbps | 50 to 200 Mbps | 100 to 500 Mbps | 10 to 100 Mbps |
| Uplink user rate | ~50 Mbps | 10 to 20 Mbps | 10 to 50 Mbps | 1 to 10 Mbps |
| Coverage radius | 50 to 100 km | ~1,000s km | ~1,000s km | Continental |
| Deployment speed | Rapid (hours/days) | Slow (launch) | Slow (launch) | Slow (launch) |

Benefits: rapid deployment in hours or days rather than a launch campaign; a
50 to 100 km radius from one platform; **0.13 ms round-trip propagation** and
1 to 10 ms end to end; a direct-to-unmodified-smartphone link budget about
**28 dB better than a 500 km LEO**; temporary backhaul for surviving or portable
cells; a regenerative payload that keeps local traffic local.

Challenges: endurance, where **12 days is the current airship record**;
station-keeping against stratospheric winds; Ka-band feeder-link rain fade,
needing site diversity; emergency spectrum and airspace clearance; one
platform's capacity shared across the whole footprint; and TN-HAPS interference
and handover coordination.

Conclusion: HAPS restores coverage when the terrestrial RAN is destroyed,
**provided backhaul survives** via gateway, satellite or another HAPS.
Endurance, spectrum clearance and station-keeping remain open.

---

## Group 6 - Multi-connectivity and session continuity across TN-NTN links

Terrestrial networks leave coverage gaps where towers are not economic, and they
fail when disasters damage infrastructure. Non-terrestrial networks fix coverage
but bring their own weaknesses: LEO satellites move, forcing frequent handovers,
and high altitudes add latency.

5G-Advanced integrates both rather than choosing one. Five problems map to five
solutions.

| Challenge | Solution |
|---|---|
| Frequent handovers | Predictive AI mobility |
| Latency differences | Intelligent routing |
| Link failures | Multi-connectivity |
| Congestion | Traffic steering |
| Session interruption | Make-before-break handover |

**Multi-connectivity** means a device holds connections to more than one network
at once, for example a phone attached to a 5G base station and a LEO satellite
simultaneously. Benefits: higher reliability, higher throughput, load balancing,
and a backup path if one link drops.

**Session continuity** means an ongoing session survives a change of underlying
link without interruption. Benefits: no repeated logins, no data loss, a stable
network experience.

Six technologies deliver this.

**Multi-Radio Dual Connectivity (MR-DC)** lets a device keep simultaneous
connections to terrestrial 5G and satellite.

**Access Traffic Steering, Switching and Splitting (ATSSS)** dynamically routes
and balances traffic across the available accesses.

**AI-assisted mobility management** predicts user movement and network
conditions, so handovers are prepared in advance.

**Multi-Access Edge Computing (MEC)** processes data closer to the user, cutting
latency and keeping applications responsive during mobility.

**Network slicing** creates dedicated virtual slices per application, so each
gets consistent quality of service.

**Make-before-break handover** establishes the new connection before releasing
the old one, preventing the session dropping in the transition.

Outcome: seamless switching between terrestrial and satellite, continuous voice,
video and data, improved reliability and lower latency. Applications: aviation,
maritime, disaster recovery, connected vehicles.

---

## Group 7 - Spectrum sharing and interference management between 5G NTN and TN

Terrestrial 5G gives high capacity, low latency and dense urban coverage, and
leaves gaps over rural land and ocean. Non-terrestrial 5G gives ubiquitous
direct-to-device coverage from GEO, MEO, LEO and HAPS, standardized since 3GPP
Release 17. When integrated, a terrestrial base station and an NTN satellite
illuminate the same ground area and a shared-coverage device sits inside both
footprints. That overlap creates interference.

The root cause is shared spectrum. L-band and S-band carry mobile satellite
service and NTN IoT, including **NTN n256 at 2170 to 2200 MHz**. C-band carries
fixed satellite service and part of terrestrial 5G. **Terrestrial n77 and n78
occupy 3.3 to 4.2 GHz.** Ku-band and Ka-band carry NTN feeder and user links.
Overlapping allocations create co-channel and adjacent-band interference.

Interference runs both ways. On the **downlink**, the satellite beam spills into
the terrestrial cell and reaches a victim device. On the **uplink**, a
terrestrial user's transmission rises into the satellite receiver.

Four mechanisms to manage: **co-channel interference**, where NTN and TN use
exactly the same frequency at once; **adjacent-band leakage**, where signal
spills into the band next door; **cross-border coexistence**, where a beam
crosses into another country's network; and **Doppler-induced spreading**, where
fast-moving LEO satellites smear the signal.

The solution space is a tree. Spectrum sharing divides into exclusive or licensed
use; static co-primary sharing with fixed geographic or frequency partitions;
dynamic spectrum sharing with real-time allocation through sensing and
coordination; and geographic separation with exclusion zones and PFD or EPFD
limits. **Dynamic spectrum sharing subdivides into power control, adaptive
beamforming, cognitive sensing and AI/ML-based allocation.**

**Technique 1, PFD and EPFD masks.** A regulatory power flux density envelope
caps satellite emissions at the Earth's surface **as a function of elevation
angle**. Set out in **ITU Radio Regulations Article 21** and mirrored in 3GPP.
**EPFD** extends it to the aggregate interference from an entire constellation.

**Technique 2, adaptive beamforming and null-steering.** A conventional beam has
a fixed pattern that may point energy at a victim terrestrial receiver. An
interference-aware adaptive beam places a **null** toward that victim, preserving
the main lobe while suppressing the interference.

**Techniques 3 and 4, power control and dynamic spectrum access.** Power control
means transmitting only the power needed. Cognitive or dynamic spectrum access
means sensing free channels in real time and switching to them. Time and
frequency guard resources separate NTN and TN where sharing is not possible.

The 3GPP roadmap: **Rel-15/16 (2018-2020)** study items on NR support for NTN
begin; **Rel-17 (2022)** the first NTN specification, basic NR-NTN and NB-IoT or
eMTC over satellite; **Rel-18 (2024)** 5G-Advanced with mobility, regenerative
payloads and NTN-TN band coexistence in n255/n256; **Rel-19 (2025)** coverage and
capacity enhancements, gNB-on-satellite, RedCap NTN; **Rel-20 (6G, 2026 onward)**
deeper NTN-TN spectrum integration.

Open challenges: cross-border regulation, where countries must agree on the same
PFD rules; Doppler and mobility, because LEO geometry keeps changing; onboard
processing limits from tight power and thermal budgets; and operator
coordination, needing real-time data exchange between satellite and mobile
operators.

Takeaways: NTN and TN must coexist in shared, congested 5G spectrum; PFD masks,
beamforming, power control and DSA jointly fight interference; Releases 17 to 19
are steadily formalizing the coexistence rules; and **AI/ML-driven dynamic
spectrum sharing is the clear road to 6G**.

---

## Group 8 - Mobility management and handover optimization in 5G NTN

Mobility management keeps a device reachable and connected as it, or the network
serving it, moves. In NR-NTN a device sits in one of three RRC states.

**RRC CONNECTED**: active connection, bidirectional signalling, user data can be
transferred, highest power consumption. **RRC INACTIVE**: connection released but
the UE context is kept in the network; the device can be paged and can resume
quickly, at lower power. **RRC IDLE**: no connection and no stored context; the
device only monitors paging and needs a full RRC setup to connect, at lowest
power. Transitions run CONNECTED to INACTIVE when data transfer stops, INACTIVE
to IDLE after a timer, and INACTIVE or IDLE back to CONNECTED on a data request
or paging.

On the ground a handover is triggered by measured signal strength. In NTN that is
not enough, because the satellite is moving and the measurement is old by the
time it is acted on. NR-NTN adds triggers based on geometry and time.

**Location-based trigger.** The device obtains its location, for example from
GNSS. Crossing a predefined geographic threshold, the **handover boundary**
between the serving and target satellite coverage, triggers a handover. The
device connects to whichever satellite offers better link quality there.

**Time-based trigger.** The trigger is a predicted time derived from satellite
ephemeris and orbit data. The network knows when the serving satellite's expected
link quality will fall below a threshold at a future time, and triggers then.
This enables a proactive handover.

**Conditional handover.** The handover fires only when several conditions hold at
once: link quality, for example target SINR exceeding serving SINR plus a
hysteresis margin; time to link degradation below a threshold; the UE being
inside the target coverage area; and the target satellite's load being below a
maximum. If all hold, the handover triggers; if not, the device stays with the
serving satellite. Benefits: fewer unnecessary handovers, better service
continuity, better resource use, better user experience.

Four challenges drive all of this. **Frequent handovers**, because LEO satellites
move at about **7.5 km/s** and devices switch every few minutes. **Dynamic beam
coverage**, because moving spot beams change a stationary user's coverage
constantly. **Long propagation delay** from the distance to space. **Large
Doppler shifts** causing frequency drift and synchronization errors.

Optimization techniques: **multi-connectivity**; **make-before-break**;
**predictive mobility handover**, using orbit and user location to predict when a
handover will be needed so the network prepares target resources in advance;
**beam-based handover**, switching between spot beams of the same satellite
rather than between satellites; and **AI/ML-based handover management**,
analysing traffic patterns, satellite movement and user mobility.

Every gain has a cost. Location triggers drain the battery through continuous
position fixing. Make-before-break needs more complex hardware, because two links
run at once. Signalling and ephemeris distribution add overhead. Reserving cells
at the target wastes capacity if the handover does not happen. AI/ML optimization
runs into computational SWaP constraints on the satellite.

Conclusion: NTN mobility management shifts from **reactive to predictive**,
trading the signal-strength model for an ephemeris-driven one and accepting new
overheads in exchange for reliability that LEO speed and delay would otherwise
destroy.

---

## Group 9 - ISAC-enabled non-terrestrial networks for 6G

**Integrated Sensing and Communication** means using one waveform, one RF front
end and one slice of spectrum to do communication and sensing at the same time.
Instead of dedicating separate hardware and spectrum to radar, the communication
signal itself detects and measures the environment.

Three architectural starting points, defined by which function the waveform is
designed around. **Sensing-centric waveform design** optimizes for radar and
accepts a weaker data link. **Communication-centric waveform design** optimizes
for data and extracts whatever sensing it can. **Joint waveform design** designs
one waveform for both from the start.

Satellites already sense implicitly. Ground networks recover a satellite's full
position and velocity from Doppler alone, which is how orbit determination works,
and LEO Doppler signatures are strong enough to make this reliable. **GEO shows
almost no Doppler**, because the satellite is nearly stationary relative to the
ground, so GEO satellites are **ranged** instead. ISAC generalizes the idea: from
sensing the satellite's own motion to sensing external targets and the
environment.

Three geometries.

**Monostatic.** One platform transmits and listens for its own echo. Transmitter
and receiver share one aperture.

**Bistatic.** One platform illuminates the target and a second receives the
reflection. Transmit and receive are split across two nodes.

**Multistatic.** One transmission is caught by the rest of the constellation.
Several receivers (Rx1 to Rx4) observe the echo of a single transmitter, so the
constellation itself becomes the radar.

Functions and advantages: hardware and cost reduction, because a single RF front
end reduces SWaP-C; enhanced spectral efficiency, because no dedicated sensing
spectrum is needed and congestion falls; high-precision localization, tracking
passive objects and enabling autonomous traffic; real-time environment mapping,
creating a digital twin and preventing outages; extreme disaster resilience,
letting emergency hubs locate survivors and map terrain; and sensing-assisted
resource management, enabling predictive beamforming and removing signalling
overhead.

The challenges are serious.

**Self-interference**, in the monostatic case. The receiver must hear a faint
echo through its own loud transmitter. This needs **more than 70 dB** of combined
analog and digital cancellation, on a moving payload.

**Synchronization**, in the bistatic and multistatic cases. Independent nodes
must share time and phase to **sub-microsecond** accuracy.

**Onboard power and compute.** Limited payloads push processing to the ground,
adding latency.

**Waveform tension, worse over NTN.** Long delay, tens of kilohertz of Doppler,
and intermittent visibility all work against a dual-purpose waveform.

**No native standard** for ISAC over NTN yet.

Use cases: maritime and border surveillance, tracking ships and reading sea state
while serving broadband, one beam doing two jobs over water with no towers;
disaster and wildfire monitoring, as sensing-as-a-service from HAPS, UAVs and
satellites, restoring connectivity and mapping damage when the ground is down;
and space situational awareness and debris, detecting, tracking and classifying
orbiting objects, with **DebriSense-THz reported at 95 to 99 percent
classification at 5 THz**.

---

## Group 10 - AI-native Open RAN for NTN

Three ideas connect here. The **RAN** is the towers, antennas and baseband units
linking devices to the core. **AI** is machine learning models that observe
network data and make or recommend decisions. **NTN** is satellites, HAPS and
UAVs extending coverage beyond ground infrastructure.

**Open RAN** breaks the base station into separately deployable functions joined
by open, standardized interfaces, and adds an intelligence layer. The Service
Management and Orchestration framework hosts the **Non-Real-Time RIC**, which
runs rApps and handles policy and AI model training. Below it sits the
**Near-Real-Time RIC**, running xApps. These manage the O-CU-CP, O-CU-UP, O-DU
and O-RU over A1, E2, O1 and the open fronthaul.

The two RICs differ by control-loop timescale. The **Non-RT RIC runs the slower
loop, greater than one second**, doing AI/ML policy work and model training. The
**Near-RT RIC runs the faster loop, less than one second**, doing real-time
optimization through xApps.

Functional splits. The **O-CU** splits into **O-CU-CP (RRC, PDCP)** and
**O-CU-UP (SDAP, PDCP)**. The **O-DU** splits into **ODU-HIGH (RLC, MAC)** and
**ODU-LOW (High-PHY)**. The O-RU carries the Low-PHY. Each function is
independently deployable and interoperable through the open interfaces, and all
of it can run on the O-Cloud.

The contrast with traditional RAN is vendor lock-in. A traditional RAN has a
single vendor supplying the baseband unit and the radio unit over proprietary
fronthaul and backhaul. Open RAN splits the same chain into O-CU, O-DU and O-RU,
each possibly from a different vendor, over open midhaul and fronthaul.

**AI-RAN** is three concentric layers. **AI-for-RAN** is innermost: AI hardware,
AI software and AI integration used to improve the network itself. **AI-and-RAN**
is the middle: partner integration, partner APIs and security isolation, so AI
and RAN workloads share infrastructure. **AI-on-RAN** is outermost: marketplace
platform, developer tools and global access, delivering AI services over the
network.

In NTN the pipeline runs: satellites, HAPS and drones connect over open
interfaces to a ground RIC; a machine learning engine analyses network and NTN
data and predicts, learns and optimizes; the **Near-RT RIC then runs xApps that
allocate satellite beams and resources to user devices**.

Three AI applications. **Intelligent handovers**, where an AI-driven decision
uses signal strength, network load and user motion to pick the target satellite
along an intelligent prediction path. **Beam optimization**, steering and shaping
spot beams toward the mobile user rather than leaving a fixed pattern.
**Self-optimizing network operations**, spanning LEO, GEO and HAPS with the
ground segment.

Three challenges. **RIC placement**: ground or satellite. **Satellite mobility
breaks O-RAN's timing assumptions**, because the interfaces were designed for a
static fronthaul with predictable latency. **Resource optimization gets harder
after deployment, not easier**, because the geometry keeps changing once the
constellation is flying.

---

## Group 11 - Federated learning for CSI feedback and beam management in LEO NTN

**Channel state information** describes how the radio path changes the signal, in
strength and in timing. The satellite cannot observe the downlink channel itself,
so the device must measure it and report it before the satellite can aim a beam.
Every device reports in every beam: beam index and its power, rank (the number of
streams), precoder index (PMI) and quality index (CQI). Only tens of bits in
total.

The conventional cycle is four steps: **measure** the pilots, **quantise** to a
codebook entry, **report** the index on the uplink, **precode** the beam at the
gNB. The cost is that the report must be repeated often, and it **grows with the
antenna count, the number of users and the report rate**. Small individually,
dominant in aggregate.

**Challenge one: the report is stale on arrival.** The satellite moves at about
**7.5 km/s**. The timeline runs measure, send, arrives, applied, and the interval
over which the channel stays valid is shorter than the measure-to-use delay. The
report describes a channel that has already gone.

**Challenge two: the data needed to fix this is private.** A channel measurement
is nearly unique to one place, so **CSI is a location fingerprint**. Central
training means one dataset and one place where subscriber location can be
exposed.

**Mechanism one: a learned encoder.** An encoder on the device compresses the
measured CSI into a short codeword; a decoder at the gateway reconstructs it.
Only a few bits cross the link. Reported compression ratios are **1/16 to 1/64**.
The encoder and decoder are **trained together as one pair**, because the
codeword is not a standard format but whatever internal representation the
encoder settles on.

**Mechanism two: federated learning.** Devices train locally on their own data
and send only model updates. The aggregator averages the updates, so **raw CSI
never crosses the line**. The aggregator runs **FedAvg** as the baseline,
**FedProx** for uneven data, **SCAFFOLD** to correct drift and **FedAdam** as an
adaptive server. Added for privacy: secure aggregation and differential privacy.

**Where the aggregator sits** is a three-way trade-off. **Ground-assisted**:
every round crosses the whole link. **On the satellite**: fastest, but costs
onboard power. **Hierarchical**: partial averaging cuts the number of rounds.

**The same idea applied to beam management.** An exhaustive beam sweep has the UE
measure every beam then report the best: many measurements, many reports. A
predicted beam instead feeds ephemeris and past beams into a predictor that
outputs the best beam; one measurement confirms it. Far less reporting overhead.

Applications and why the topic matters there: **direct-to-cell**, the tightest
uplink budget of all; **rural broadband**, where no ground tower is economic;
**maritime**, far beyond coastal networks; **massive IoT**, which cannot spend
energy on reporting; **aviation and defence**, where the beam changes constantly
in flight.

Challenges and their trade-offs: **round trip cost**, each training round
crosses the full link; **update size**, which can exceed the reports it was meant
to save; **device energy**, since local training drains the battery;
**dropout**, because a satellite is visible for only minutes; and **residual
leakage**, because added noise or encryption costs accuracy.

Summary: the problem is that channel reporting is the LEO uplink bottleneck; the
cause is a small uplink budget plus a report that arrives stale; the risk is that
the data needed to fix it reveals user location; fix one is a learned encoder
that shrinks the report; fix two is federated learning that trains it without
collecting data; and the cost is paid in rounds, device energy and accuracy.

---

## Group 12 - AI-driven dynamic beam control for LEO 5G-NTN

LEO satellites sit at 300 to 1,500 km with about 7.8 km/s orbital velocity and
roughly 5 ms latency. **Beam control** means a few beams switch rapidly between
many cells, lighting busy areas more often.

The specific NTN challenge has three parts.

**Limited satellite payload and beam resources.** There are fewer beams than
cells to serve.

**Highly dynamic and uneven traffic.** Under a uniform allocation, some cells are
at high demand and others at low or none, so the same power is applied to cells
that produce nothing while busy cells are underserved.

**5G NR scheduling and timing constraints.** SSB and PRACH occupancy is fixed by
the standard. If a beam cannot serve two cells during mandatory signalling, one
of them **gets a coverage hole**.

The mechanism is AI/ML beam control, framed by 3GPP in two cases.

**Case 1, spatial domain.** **Beam steering and tracking** adjusts physical or
digital antenna weights to keep footprints aligned and compensate for high-speed
satellite movement. **User-beam mapping** groups ground UEs by location to
minimize co-channel interference across adjacent beams. **Footprint shaping**
modifies beam widths to account for changing slant ranges as the satellite moves
from horizon to zenith.

**Case 2, time domain.** **Beam hopping** time-multiplexes individual physical
beams across multiple ground target cells to serve sporadic traffic efficiently.
**Signaling alignment** reserves the strict 3GPP-defined time slots for
synchronization and broadcast signals such as SSBs without colliding with data
packets. **Temporal prediction** forecasts future traffic loads and link
blockages from historical patterns to pre-schedule hops.

Key driving factors for AI integration: reducing measurement overhead and
latency, where traditional exhaustive sweeping means many measurements, high
signalling overhead and high latency while AI-powered beam control gives smarter
selection, fewer measurements and lower latency; and positioning accuracy
enhancement, giving better angle and path estimation, more precise user
localization and robustness in challenging environments.

**3GPP AI execution models.** **Type 1**: joint training at one side. **Type 2**:
joint training at two sides, exchanging forward activation and backward gradient.
**Type 3**: separate training at two sides, sharing a training dataset.

Applications: tactical satellite communications, disaster emergency recovery,
maritime satellite connectivity.

Limitations. **Computing power against SWaP**, balancing heavy processing against
strict power and thermal constraints. **A wrong prediction drops the link**,
because incorrect predictions cut coverage completely and cause highly visible
outages. **Models must be trained before they can be tested**, so day-one models
rely on simulations that may not match real orbital conditions. **Decision speed
against how fast the beam moves**, because rapidly changing geometry leaves
real-time corrections constantly behind reality.

Conclusion: in a LEO network the cell itself moves at orbital speed, so a fixed
beam plan is out of date within seconds. AI-driven dynamic beam control predicts
where capacity will be needed and steers beams there continuously. **The gain in
efficiency is paid for in onboard computing power, which is the central
engineering trade-off.**

---

## Group 13 - GPS and Galileo

A **GNSS** is a constellation of satellites broadcasting timed radio signals that
a receiver anywhere on or near Earth uses to compute its own position, velocity
and time autonomously, **without transmitting anything back**. Satellites
transmit their position and precise time. A receiver measures signals from **at
least four satellites** to calculate its location and correct its clock error.
Both open civilian and secure encrypted services exist.

**History.** GPS was developed by the US Department of Defense in the 1970s;
first satellite launched 1978; fully operational **1995**. Galileo is the EU's
GNSS, designed from the outset for civilian control; project began 1999; first
satellites 2011; **Full Operational Capability 2024**.

### GPS: a three-segment system

Owned by the US Government, operated by the US Space Force, free worldwide.

**Space segment.** 32 operational satellites today; designed to guarantee at
least 24 at all times, with in-orbit spares filling the remaining slots. Orbit:
**Medium Earth Orbit at about 20,200 km**. **6 orbital planes** at **55°
inclination**, spaced so at least 4 satellites are visible from almost anywhere.
Orbital period about **12 hours**, so two orbits per day. Satellite generations
run from Block IIR/IIF to GPS III/IIIF, which carry more accurate atomic clocks,
stronger anti-jamming and the new civilian **L1C** signal, interoperable with
Galileo's E1. Each satellite carries multiple atomic clocks (rubidium and
caesium, accurate to nanoseconds), solar panels, and antennas broadcasting the
satellite identity, precise orbital position (ephemeris) and timestamp.

**Control segment.** The **Master Control Station** at Schriever Space Force
Base, Colorado, with a backup elsewhere. **Monitor stations**, unmanned and
worldwide, which send nothing and only listen, measuring how each satellite's
orbit and clock are drifting. **Ground antennas**, the uplink stations that
transmit corrections up to the satellites. The segment performs orbit
determination, clock correction (a nanosecond-level drift causes a real position
error because the maths relies on the speed of light), health monitoring, and
uploading fresh navigation messages.

**User segment.** Every device that listens and computes a position. The receiver
transmits nothing. It picks up several satellites, measures travel time, converts
to distance, and solves by trilateration. Two access tiers: **Standard
Positioning Service (SPS)**, the free civilian signal on the C/A code, L1 band,
typically a few metres; and **Precise Positioning Service (PPS)**, encrypted
P(Y)-code and M-code for the US military and authorized allies, with better
accuracy and jamming or spoofing resistance.

**Frequencies.** L1 at 1575.42 MHz carries C/A, P(Y), M-code and L1C, for
civilian SPS plus military PPS. L2 at 1227.60 MHz carries P(Y), L2C and M-code,
for dual-frequency ionospheric correction. L5 at 1176.45 MHz carries L5 (I/Q) for
safety-of-life and aviation. **Code Division Multiple Access**: every satellite
transmits on the same frequencies with a unique **pseudo-random noise (PRN)**
code, letting a receiver separate each satellite from the combined spectrum.

### Galileo: Europe's civilian GNSS

Jointly governed by the European Commission, EUSPA and ESA. Same three-segment
structure with European naming.

**Space segment.** A nominal **24/3/1 Walker constellation**: 24 operational
satellites across **3 orbital planes**, at **23,222 km** MEO, plus **6 active
spares** for a total of 30. Every satellite carries ultra-precise atomic clocks
such as Passive Hydrogen Masers and a **Search and Rescue transponder**. Orbital
period about **14 hours 5 minutes**.

**Ground segment.** Two **Galileo Control Centres** at Oberpfaffenhofen, Germany
and Fucino, Italy. The **Ground Control Segment (GCS)** handles spacecraft
housekeeping, mechanical health and orbital manoeuvres. The **Ground Mission
Segment (GMS)** manages navigation data, clock synchronization and signal
integrity. Three distributed sub-networks: **Galileo Sensor Stations (GSS)**
tracking signal quality and range data; **Uplink Stations (ULS)** beaming
navigation and mission data up; and **Telemetry, Tracking and Control (TT&C)**
sending operational commands.

**Frequencies.** **E1 at 1575.42 MHz**, overlapping GPS L1 and enabling combined
receivers. **E5a/E5b at 1176.45 / 1207.14 MHz** for high-accuracy dual-frequency
ranging. **E6 at 1278.75 MHz** for commercial, high-accuracy and PRS data.

### Interoperability

GPS L1C and Galileo E1 share a compatible signal structure, so **a single
receiver chip tracks both**. Combining constellations roughly doubles satellites
in view, lowering **Dilution of Precision**. Fixes are faster and more reliable,
especially in urban canyons and dense forest. If one system is degraded or
jammed, the other maintains continuity. Most modern smartphone chipsets already
track GPS, Galileo, GLONASS and BeiDou simultaneously.

### What a signal carries

**Pseudorandom code and time**: the PRN code as a unique satellite ID, and the
Time-of-Week from the satellite's atomic clock. **Ephemeris data**: the
satellite's exact position and orbit details, clock corrections, health status
and atmospheric correction data, updated frequently and **valid about 4 hours**.
**Almanac data**: approximate orbital information for **all** satellites, helping
the receiver find visible satellites quickly and achieve faster lock.

### How positioning works

Each satellite broadcasts its position and a precise time stamp. The receiver
measures travel time and converts it to a range, `p = c x dt`. One range narrows
the location to a sphere; a second to a circle; a third to two points. **A fourth
satellite resolves the ambiguity and solves for receiver clock bias**, which is
why GNSS needs a minimum of four satellites in view.

The pseudorange equation:

    p = sqrt((x-xs)^2 + (y-ys)^2 + (z-zs)^2) + c*dt

where `(x, y, z)` is the unknown receiver position and `dt` the receiver clock
bias.

**Trilateration** finds position from known distances to fixed reference points.
A **pseudorange** is the computed receiver-to-satellite distance containing a
time-sync error. It is "pseudo" because it is **not the true physical distance**.

**Why clocks matter.** Distance equals the speed of light multiplied by the time
delay. Satellites carry atomic clocks accurate to nanoseconds. **A 1 microsecond
clock error produces a 300 metre positioning error on the ground.**

### Sources of error

**Ionospheric delay**: charged particles slow signals, about **5 to 15 m**, worse
near the equator and at midday. **Tropospheric delay**: water vapour bends and
slows signals near the horizon, about **2 to 25 m**. **Multipath**: signal
reflects off buildings or terrain, up to about **1 m**. **Satellite clock and
ephemeris**: onboard drift and orbit-prediction error, about **1 to 2 m**.
**Receiver noise and hardware**: thermal noise and antenna imperfections, under
**1 m**. **Geometric Dilution of Precision**: poor satellite geometry
**amplifies all of the above**.

### Augmentation

Augmentation systems use accurately surveyed ground stations to compute the exact
difference between known coordinates and faulty GNSS data, and transmit real-time
corrections. **DGPS**: a fixed reference station broadcasts range corrections to
nearby receivers, for metre-level accuracy. **SBAS**: wide-area corrections via
geostationary satellites, including WAAS (US), EGNOS (Europe), GAGAN (India) and
MSAS (Japan). **GBAS**: a highly accurate local airport system sending radio
signals to arriving aircraft, giving the precision and safety data needed to land
in zero-visibility conditions. **RTK**: carrier-phase measurements between a base
and rover for centimetre-level accuracy.

### GPS against Galileo

| Attribute | GPS | Galileo |
|---|---|---|
| Governance | US Space Force (military-led) | European Commission / EUSPA (civilian-led) |
| Nominal constellation | 24 to 32 satellites | 30 (24 active + 6 spare) |
| Orbital altitude | ~20,200 km | 23,222 km |
| Planes / inclination | 6 planes, 55° | 3 planes, 56° |
| Orbital period | ~12 h (2 orbits/day) | ~14 h 5 min |
| Shared civilian frequency | L1, 1575.42 MHz | E1, 1575.42 MHz |
| Open-service accuracy | ~5 m (single-frequency) | <1 m (dual-freq); ~20 cm with HAS |
| Authorised service | PPS, M-code (encrypted) | PRS (encrypted) + OSNMA authentication |
| Full capability declared | 1995 | 2024 |

### GNSS in 5G NTN

**Assistance data delivery**: A-GNSS assistance data (ephemeris, almanac, clock
corrections) is broadcast to UEs over the NTN downlink, cutting time-to-first-fix.
**Timing and synchronization**: GNSS provides a precise common time reference so
gNB and UE stay synchronized despite long propagation delay. **Doppler and delay
compensation**: satellite ephemeris and GNSS timing let the network
pre-compensate Doppler and timing advance before the UE connects.

Benefits: positioning coverage extended to remote and maritime areas; faster
fixes via broadcast assistance data; reliable timing sync despite orbit dynamics.
Challenges: long propagation delay, up to about **275 ms round trip for GEO**;
high Doppler, especially for fast-moving LEO; multipath and signal blockage.

Applications: aviation, maritime, precision agriculture, autonomous and connected
vehicles, surveying and mapping, search and rescue (Galileo SAR relays distress
beacon locations), timing and synchronisation for telecom, power grids and
financial transactions, defence and security, and everyday navigation.

---

## Group 14 - Post-quantum cryptography for non-terrestrial networks

### Security mechanisms in 5G NTN today

Three link segments, each with its own protections.

**Service link**, handset to satellite: **subscriber identity privacy**, hiding
the phone identity in an encrypted digital envelope; **primary authentication**, a
two-way trust handshake using a SIM card secret key; and **air interface
ciphering**, scrambling all data packets travelling through the air.

**Feeder link**, satellite to ground dish: **encrypted tunnels (IPsec)**, a
secure digital pipe; **fast signaling security (DTLS)**, lightweight protection
for quick control messages; and **ground border protection (NDS/IP)**, a security
checkpoint at the ground station.

**Gateway to core**: **service-based architecture (SBI) security**, a never
trust, always verify digital pass system; **data tunnel security (GTP-U
encryption)** for traffic through ground fibre cables; and **cross-network
integrity**, digital stamps preventing tampering with system messages.

### The quantum threat

A classical bit is either 0 or 1, in a definite state at all times. A **qubit**
can be both 0 and 1 simultaneously, a superposition on the Bloch sphere,
expressed as `|psi> = a|0> + b|1>`.

**Shor's algorithm** factors large primes efficiently on a quantum computer,
which breaks **RSA and ECC**. Current NTN cryptography uses RSA and ECC for key
exchange and authentication, AES for symmetric encryption, and SHA-256 for
integrity and hashing.

The threat is present, not future. Under **harvest now, decrypt later**, data
intercepted today is stored and decrypted once a quantum computer exists. Traffic
with a long secrecy lifetime is already at risk.

### Post-quantum cryptography

Today's vulnerable primitives are RSA, ECC and AES-based public-key use, broken
by Shor's algorithm. The replacements are **CRYSTALS-Kyber** for key
encapsulation, standardised as **NIST FIPS 203**, and **CRYSTALS-Dilithium** for
signatures. Both are secure against classical and quantum attack.

### Why migration is harder in space

**Bandwidth and overhead.** PQC keys and signatures are far larger than RSA or
ECC. Satellite links have limited, often expensive bandwidth, so every extra byte
costs real capacity.

**Onboard compute and power constraints.** Satellite payloads run on tight energy
budgets with radiation-hardened, lower-power processors, well behind today's
ground hardware for ECC and RSA primitives.

**Propagation delay and handshake latency.** LEO round-trip times are high, and
multi-round-trip PQC key exchanges multiply that delay, slowing setup and
re-keying.

### Resolutions

**Hybrid cryptographic handshakes**, running a classical and a post-quantum
exchange together so the session holds if either survives, as provided for by
**IETF RFC 9370** for IKEv2. **Quantum-safe 5G AKA and TLS tunnels**. **Upgrading
inter-satellite links (ISL)**.

Applications: defence and military communications, commercial aviation, maritime
navigation, 5G/6G cellular networks.

Conclusion: 5G NTNs rely on standard classical cryptography today; quantum
computing threatens that classical security; PQC adoption is essential for space
networks, which are hard to upgrade after launch.

---

## Group 15 - Doppler shift estimation in 5G NR non-terrestrial networks

### Architecture

Two payload types. **Transparent (bent-pipe)**: the satellite is a repeater, the
gNB is at the ground station, and both the service link and the feeder link carry
Doppler, so the impact is **doubled**. **Regenerative**: onboard digital
processing and an onboard gNB, so the digital backhaul carries no Doppler and the
shift is **concentrated on the service link only**, giving a single point of
compensated Doppler.

### The physics

Doppler is proportional to the projection of relative velocity onto the line of
sight. For **S-band at 600 km**, the shift reaches **up to about ±48 kHz**: about
+48 kHz on horizon approach, **0 Hz at the zenith pass**, and about -48 kHz
receding. The **Doppler rate of change peaks at zenith**, at approximately
**500 Hz/s**. A **GEO** satellite at 35,786 km, being a far, stationary look,
shows **near-zero shift**.

### The problem

OFDM depends on perfect orthogonality: each subcarrier peak aligns with its
neighbours' zero crossings. Doppler-shifted subcarriers move the peaks off those
nulls, producing **inter-carrier interference (ICI)**.

**Spatial variation and multi-user interference.** On the **downlink** one common
signal is broadcast to all UEs, and each receives a different shifted frequency
depending on its **local elevation angle**: the deck shows +40 kHz at the front
of the beam, 0 kHz at the centre and -40 kHz at the back. On the **uplink**
multiple UEs transmit simultaneously via OFDMA, and their transmissions converge
at the satellite receiver with different frequency offsets.

### 3GPP Release 17 baseline

**System assumption: Rel-17 mandates that NTN UEs carry an active GNSS receiver
(GPS / Galileo / BDS).** The workflow is four steps. **1. Ephemeris broadcast**:
the satellite broadcasts orbital position and velocity via **SIB19**. **2. UE
self-positioning**: the UE determines its own coordinates using GNSS. **3.
Doppler calculation**: the UE derives the distance vector and estimates the
downlink and uplink Doppler. **4. Uplink pre-compensation**: the UE shifts its
transmit frequency in the reverse direction.

### Why GNSS-assisted methods fail in practice

**Environmental vulnerability**: GNSS signals at about **-130 dBm** fall over in
urban canyons, indoors and under foliage. **Security risks**: susceptible to RF
jamming, spoofing or deliberate denial. **Hardware and power constraints**:
low-cost IoT and mMTC devices often lack GNSS chipsets. **Oscillator error
coupling**: the measured offset mixes true Doppler with local clock drift.

### Autonomous pilot-based estimation

Objective: enable NTN access without relying on GPS/GNSS. Using the 5G NR OFDM
resource grid, the receiver measures phase change at the SSB subcarrier over one
interval and at the DM-RS subcarrier over another, then solves a two-equation
system that **separates motion Doppler `f_d` from local oscillator drift
`df_LO`**.

### Integer and fractional separation

Total Doppler shift = **integer subcarrier shift (M x SCS) + fractional shift
(e x SCS), where |e| < 0.5**.

**Fractional recovery** uses the cyclic prefix, which is an exact repeat of the
symbol's last `N_cp` samples. A complex-conjugate multiplier computes
`y[n] . y*[n+N]`, and an angle evaluator turns the result into the fractional
Doppler `e`.

**Integer recovery** uses frequency-domain cross-correlation of the PSS and SSS
synchronization signals over a sliding frequency search grid, yielding the
integer `M`.

### Predictive trajectory tracking (Rel-18/19 and 6G)

An **Extended Kalman Filter** state vector incorporates satellite position,
velocity, acceleration and UE clock drift rates. The EKF or an LSTM predicts a
smooth Doppler trajectory that survives short signal occlusions, tracking through
gaps where a measurement-only method would lose lock.

### Trade-offs

| Criteria | Rel-17 GNSS | Multi-freq pilots (GNSS-free) | CP / cross-correlation | AI / EKF tracking |
|---|---|---|---|---|
| GNSS dependency | High (mandatory) | None | None | Optional initial seed |
| Estimation accuracy | Very high (<=10 Hz) | High (~50-100 Hz) | Moderate | High (smooth) |
| Pilot overhead | Minimal | Moderate (DM-RS) | **Low (standard CP)** | Very low (predictive) |
| Computational complexity | Low (algebraic) | Moderate (phase corr.) | Moderate (FFT search) | High (matrix/inference) |
| Indoor / jamming use | Fails completely | Fully operational | Fully operational | Robust to short fades |

### Future direction

5G NR NTN today uses an OFDM waveform with GNSS-assisted tracking and explicit
Doppler pre-compensation. 6G NTN moves toward an **OTFS (delay-Doppler)
waveform**, **Integrated Sensing and Communication**, and **AI-driven trajectory
prediction**, via Releases 19 and 6G.

---

## Group 16 - Network slicing in non-terrestrial networks

**Network slicing** runs several independent virtual networks on top of one
shared physical network. Each slice is tuned end to end for a different service
and behaves as if it were a separate network. The shared physical layer is radio
spectrum and beams, satellite payload, feeder and transport links, and 5G core
compute. Slicing is achieved by SDN and NFV virtualisation.

Three standard slice types. **SST 1, eMBB**: a wide, high-throughput pipe that
tolerates delay, for streaming, broadband and video. **SST 2, URLLC**: priority
scheduling, short queues, guaranteed, for control, safety and emergency traffic.
**SST 3, mMTC**: store-and-forward, tiny packets, huge scale, for IoT sensors,
tracking and metering. Same hardware, separate SLAs, logically isolated.

**Why bring slicing to NTN?** One satellite must serve many services at once,
including video, safety-critical traffic and millions of IoT sensors, each with
different needs. Slicing lets a single, scarce space platform behave like several
tailored networks.

### The NTN challenge

In terrestrial 5G a slice is pinned to a fixed cell and a fixed fibre path. In an
NTN **both the radio cell and the transport path are in motion**. Four
consequences.

**Delay that breaks the SLA.** Round-trip delay is **25.8 ms for a 600 km LEO**
and **541 ms for GEO**, against **under 1 ms** on a terrestrial cell. A **1 ms
URLLC slice simply cannot be honoured**.

**No room for hard isolation.** Mass, power and thermal limits mean one payload
and one spectrum pool are shared by every slice. **Isolation has to be logical,
not physical.**

**A cell that will not stay still.** A LEO beam sweeps the ground and is visible
for only **6 to 10 minutes**, so the slice must be re-anchored to a new satellite
every few minutes. The satellite ground speed shown is **7.56 km/s**.

**A topology that re-wires itself.** Feeder-link switchover and inter-satellite
re-routing change the slice's end-to-end transport segment mid-session.

### The proposed mechanism

Management and orchestration runs as a chain with orbit-aware policy driven by
ephemeris and SLA: **CSMF** captures customer intent; **NSMF** manages the
end-to-end slice; **NSSMF (RAN)** handles the beam and scheduler; **NSSMF
(CN/TN)** handles core and transport.

Below that, each slice runs across four segments. The **terminal** makes a
slice-aware UE S-NSSAI request. The **NTN radio segment** applies a per-slice
scheduler and a beam and power split on a regenerative gNB. The **transport
segment** carries feeder-link and inter-satellite links with slice-tagged
bearers. The **5G core** provides NSSF, AMF, SMF and UPF, on the ground or on
board.

### Applications

**Maritime**: crew broadband, vessel telemetry and fleet safety on one link
(eMBB + mMTC). **Aviation**: passenger internet kept strictly apart from cockpit
and operations data (eMBB | URLLC). **Rural broadband**: schools, clinics and
mobile money for unserved communities (eMBB + mMTC). **Disaster response**: a
priority slice for responders when terrestrial sites are down (URLLC). **IoT at
scale**: agriculture, energy and rail sensors over huge areas, delay-tolerant
(mMTC). **Government and defence**: a hardened, isolated slice on shared
commercial capacity (URLLC + eMBB).

### What slicing buys, and what it costs

| What slicing buys | What it costs |
|---|---|
| Guaranteed QoS per service | Protocol overhead and latency amplification: slice headers, per-slice buffering and PDC keys inflate packets on an already long link |
| Strict isolation between tenants | Isolation against efficiency: capacity fenced off for an idle slice is wasted on a scarce, power-limited payload |
| One infrastructure, many operators | Orchestration in a moving topology: SLAs must be re-computed at every handover and feeder-link switchover, meaning heavy control signalling |
| Core functions moved on board | SWaP on the satellite: a regenerative gNB and UPF per slice draw power and generate heat the platform may not be able to shed |
| Seamless terrestrial-satellite service | Multi-domain accountability: a slice spans operator, satellite owner and regulator, and end-to-end SLA assurance is still an open standards item |

### Summary

**Same idea, harder physics.** Slicing turns one satellite system into several
logical networks, but the cell, the transport path and the power budget all move.
**Orbit-aware orchestration.** The slice must be planned from ephemeris and
handover timing, not from a static cell plan, and SLAs are re-negotiated as the
constellation turns. **Every gain has a price.** Isolation costs capacity and
signalling overhead on a link that is already power-limited and delay-limited.
Slicing is a budgeting exercise.

---

## Group 17 - eRACH, a learned random access protocol for LEO networks

### Context

LEO satellite networks orbit at about **550 km**, moving at about **7.6 km/s**,
with wide, shifting coverage and **no fixed base station location**.
Mega-constellations such as Starlink aim to provide global broadband.

**Random access** is how a device requests a connection before sending data. The
existing method is the 4G/5G **Random Access Channel**, a four-step handshake:
preamble, response, request, setup. **RACH was designed for terrestrial towers,
not moving satellites.**

**Multi-agent deep reinforcement learning** is the tool. Multiple independent
agents, the ground terminals, each learn a behaviour. Learning happens through
trial and error, with **no communication between agents**. The agents share the
same environment but act independently.

### Why RACH fails for LEO

**1. Non-stationary topology.** Satellites move at about 7.6 km/s, so the best
satellite to connect to changes every few milliseconds. Standard RACH **does not
account for which satellite to associate with**.

**2. Long round-trip time.** Even LEO incurs **1 to 5 ms one-way** propagation
delay. CSMA/CA and acknowledgment-based protocols become slow and prone to wasted
retransmissions.

**3. Uncontrolled collision rate.** RACH selects a preamble randomly. When many
devices access at once they collide and must retry, wasting bandwidth and
increasing access delay.

### How eRACH works

**1. Observe, locally and without communication.** Each ground terminal monitors
two things: the **expected satellite position**, known from the predictable
orbit, and **whether its last access attempt caused a collision**.

**2. Decide, using an actor-critic neural network.** From its local observations
each terminal independently decides either to **access now, and choose which
satellite**, or to **back off and wait** for a better slot.

**3. Improve, through reinforcement learning.** Over many orbital cycles the
terminals learn to spread their access attempts. Collisions fall, throughput
rises, and **no coordination is needed**. The coordination is emergent: it arises
from independent learning rather than from any signalling between devices.

### Applications

**Rural and remote broadband**, where billions without ground infrastructure gain
connectivity through LEO mega-constellations, and low-collision access is
critical for sharing limited satellite bandwidth. **Maritime and aviation
tracking**, where constantly moving ships and aircraft need seamless handovers
with low-latency, reliable uplinks. **Disaster recovery communications**, where
fast, collision-free access matters when ground infrastructure is destroyed.
**IoT sensor networks**, where thousands of low-power devices in smart
agriculture, environmental monitoring and industrial IoT must share the satellite
uplink without central coordination.

### Challenges

**High computational complexity against SWaP constraints.** **Sensitivity to
satellite positioning accuracy**, because the expected satellite position is one
of only two policy inputs, so an error corrupts the decision. **Higher collision
tolerance trade-off.**

### Summary

**The problem**: existing RACH does not account for satellite mobility, leading
to high collision rates and excessive access delays. **The solution**: eRACH uses
multi-agent reinforcement learning so each terminal independently learns when and
which satellite to access, achieving **54.6% higher throughput and about 2x lower
access delay** than RACH, with **no inter-device coordination** (Paper Table II).
**Key trade-offs**: eRACH is robust to orbital positioning errors and can
flexibly trade between throughput maximisation (**rho = 0**) and collision
avoidance (**rho = 2**) to suit different application classes.

---

## Group 18 - RIS-enhanced NTN for coverage and capacity in 6G

### The coverage problem

A satellite needs a clear view of the user. A building, a hill or a roof removes
the link completely, and **the link budget is already tight**. The user sits in
the shadow with no service at all.

### What a RIS is

A **Reconfigurable Intelligent Surface** is a panel of controlled elements. Each
unit cell contains a tunable phase shifter covering 0 to 360 degrees. An incident
signal from the base station strikes the surface and is reflected toward the user
equipment, even when the direct path is blocked. An external **RIS controller**
sets the phase of every element over a control link.

The mechanism is passive beamforming: **each small element applies its own phase
shift, so the reflected waves add up in one chosen direction**. No RF chain, no
amplifier and no moving part is required.

### Types of RIS

**1. Passive RIS.** No RF chains or amplifiers on the surface. Only adjusts the
phase, and sometimes the amplitude, of the reflected signal. Controlled by an
external RIS controller.

**2. Active RIS.** Each element is connected to an active component, an amplifier
and an RF chain. Can control both amplitude and phase. Enables signal
amplification and higher efficiency.

**3. Hybrid RIS.** A combination of passive and active elements, with only a
subset of elements connected to RF chains. Lower cost and complexity than a fully
active RIS.

**4. Tunable (analog) RIS.** Uses analog phase shifters such as varactors and PIN
diodes for continuous phase tuning. Infinite, or very large, numbers of phase
states. Higher performance but more hardware complexity.

**5. Digital (discrete) RIS.** Uses discrete phase shifts, for example 1-bit
giving 0 or 180 degrees, extendable to multi-bit (2-bit, 3-bit). Lower complexity
and cost, slightly lower performance than analog.

**6. Frequency-selective (wideband) RIS.** Elements have different responses
across frequency, so the surface can manipulate multiple frequency bands
simultaneously. Suitable for wideband and multi-band communications.

### Placement

Two arrangements are shown. A **RIS-assisted satellite-to-user link**, where the
surface is mounted on a building and reflects the satellite downlink around the
obstruction to a user in the shadow. A **RIS-enabled satellite link**, where the
RIS is mounted **on the satellite itself**, reflecting and steering an uplink from
a ground station or another satellite toward the user, giving flexible beam
steering without mechanical movement, energy-efficient and lightweight compared
with a phased array.

### Coverage and capacity

A single-antenna base station blocked by an obstacle reaches a RIS, which
distributes the signal to multiple regions and multi-antenna devices. **Coverage**
comes from building a path where no clear view exists. **Capacity** comes from
that path being distinct from the direct one, so a second spatial stream becomes
possible.

### Applications

**Urban streets**: serves users the satellite cannot see. **Rural and remote**:
extends a beam edge with no new tower. **Satellite payload**: a light replacement
for a phased array. **Indoor coverage**: carries a signal in through a window.
**Ships and aircraft**: steerable gain with no moving parts. **Disaster
response**: flown in and placed where it is needed.

### Challenges and limitations

**Multiplied loss**: the two hops multiply rather than add, so the panel must be
large. **Element count**: thousands of elements are needed to close the link
budget. **Channel knowledge**: a passive surface cannot measure anything itself,
so the channel must be estimated by other means. **Control overhead**: phases
must be recomputed continuously as the satellite keeps moving. **Near-field
effects**: a large panel breaks the simple distance model that far-field design
assumes. **Not standardised**: a candidate for 6G, in no released standard yet.

### Summary

**Problem**: blockage removes the link, and the budget is tight. **Idea**: a panel
of controlled elements steers its own reflection. **Coverage**: it builds a path
where no clear view exists. **Capacity**: it adds a second path, so a second
stream is possible. **Cost**: the two losses multiply, so it must be large and
close. **Status**: a candidate for 6G, still before standardisation.

---

## Group 21 - Uplink time synchronization for NTN without GNSS

### Setup

Network: **5G NR**. Architecture: **regenerative**, with an onboard gNodeB.
Orbit: **LEO**, hundreds of kilometres. Uplink: **CP-OFDM**.

The architecture matters. A regenerative payload puts the base station in orbit,
so the timing reference the device must align to is on the satellite itself.

### The channel challenge: timing advance

Two approaches exist. **Open-loop TA**: the UE calculates the timing advance
itself, using **GNSS** and **ephemeris data**. **Closed-loop TA**: the network
measures the timing, adjusts the TA and signals the correction back.

### The Release 17 baseline: a GNSS-assisted dual loop

**GNSS** means satellite constellations broadcasting highly precise time and
location data worldwide: GPS (USA, 31 satellites, 6 orbit planes), GLONASS
(Russia, 24 satellites, 3 orbit planes), Galileo (Europe, 24 satellites, 3 orbit
planes) and BeiDou (China, 35 satellites, 3 orbit planes).

The timing advance is built from three parts. An **open-loop calculation** made
of **TA common**, broadcast by the satellite, plus **TA UE**, computed by the
device from GNSS and ephemeris. And a **closed-loop adjustment**, **TA adj**,
signalled by the gNB as a residual correction.

### What "without GNSS" means

**The open-loop equation breaks.** The user equipment **does not know its position
relative to the satellite**, so it **cannot directly determine the propagation
delay** and **cannot accurately discern the timing advance**. It must rely on
closed-loop signalling alone to gauge timing, and its signals arrive with
**massive timing errors, far greater than the cyclic prefix**. The deck calls this
a **blind UE**: it does not know how early to transmit.

This is why closed-loop-only is not a fallback. A closed loop can only refine an
estimate that is already close enough to be received. With no starting estimate,
the signal lands outside the reception window and there is nothing to measure.

### Method 1: GNSS-time-free drift compensation

**Key insight: satellite motion changes the propagation delay, so by tracking
downlink arrival-time drift, the UE can estimate timing advance without GNSS.**

Satellite motion changes the signal path length, so the distance to the satellite
changes over time and expected arrival times shift. The process is six steps.
**1.** The satellite is in motion, changing the signal path length. **2.** The UE
receives the downlink signal, with no GNSS position used. **3.** The UE measures
arrival-time drift, tracking how downlink slot arrivals shift over time.
**4.** It estimates the TA adjustment, by direct update or a Kalman filter.
**5.** It applies the corrected TA to pre-compensate uplink timing.
**6.** The uplink arrives time-aligned at the gNB.

### Method 2: Extended Kalman Filter

The cycle runs **initialization**, then **prediction**, **measurement**,
**filtering and update**, producing a **true distance** estimate and from it the
**timing advance**, feeding uplink synchronization.

The **state vector** contains **UE latitude**, **satellite longitude** and the
**UE-to-satellite distance**. Strengths: **robust performance** and **rapid
convergence to accurate values**.

### Method 3: network-provided common timing advance

The network broadcasts a single common TA value for the beam. The trade-off is
geometric: **a UE near the beam centre receives a very accurate broadcast value**,
while **a UE near the beam edge finds the broadcast value can be significantly
off**. One value cannot describe every point in a footprint.

### Method 4: timing advance feedback loop

The UE transmits uplink data or PUCCH with an initial TA, which may be zero or an
estimate. The gNB measures the arrival time of the uplink signal relative to the
expected time in the slot, and classifies it as **arrived too early** (a negative
timing error, so **increase TA**), **arrived too late** (a positive timing error,
so **decrease TA**), or **arrived on time**, inside the timing window, so **keep
TA**. The gNB sends a timing advance command indicating how much to adjust. The UE
updates its TA and retransmits. The loop continues until the uplink consistently
arrives within the allowed timing window: **closed-loop convergence**.

### Conclusion

**The challenge**: 5G satellite networks rely on timing advance to align uplink
signals, which normally requires GNSS on the user's device to calculate position
and propagation delay. **The problem**: without GNSS, devices cannot determine
their distance to the satellite, causing massive timing errors that break
standard open-loop synchronization. **The solution**: the alternative methods
described allow uplink synchronization without GNSS.

---

## Group 22 - Deep reinforcement learning for space-air-ground 6G resource allocation

### What a SAGIN is

A **Space-Air-Ground Integrated Network** layers satellites, aerial platforms and
terrestrial infrastructure under one 6G system, coordinated through a **Space
Operation Center**, an **Aerial Operation Center** and a **Ground Operation
Center**, all connected to an internet data center. The point is that all three
tiers are managed together rather than as separate networks.

### Challenges

**Spectrum scarcity and interference.** **Limited on-board power and energy.**
**Uneven and constantly shifting user demands.** All three are resource problems:
there is not enough spectrum, not enough power, and the demand to be served will
not stay still.

### Resource allocation

**What?** Resource allocation is the process of distributing a SAGIN's limited
communication and computing resources among its users and platforms. **Why?**
With limited resources and constant movement, smart sharing is what keeps the
network fast, fair and reliable.

### Why deep reinforcement learning

Agentic AI for a wireless network cycles through **perception** (channel
estimation), **reasoning** (user intent and network analysis), **learning**
(traffic and load prediction) and **action** (resource allocation), all acting on
a ubiquitous wireless environment spanning space, air and land.

### The DRL framework

An **agent** contains a policy controller, a neural network. It emits an
**action**: channel allocation, power control and access point selection. That
action is applied to the ubiquitous wireless environment across space (satellites
and unmanned space vehicles), air (HAPS and UAVs) and land (base stations and
mobile equipment). The environment returns a **state**: available power,
bandwidth, SINR and CSI. And a **reward**: quality of service, quality of
experience and spectrum efficiency.

### Key algorithms

**Deep Q-Network (DQN)** chooses from a list of fixed options, for example which
channel to use. **Deep Deterministic Policy Gradient (DDPG)** fine-tunes exact
values, for example a precise power level. **Proximal Policy Optimization (PPO)**
learns a stable strategy step by step. **Soft-Actor Critic / Twin Delayed DDPG
(SAC/TD3)** explores boldly and converges reliably, handling many goals at once.

### Allocation tasks by tier

**Space**: beam hopping, spectrum and power provisioning, frequency and channel
assignment, optimal transmit power allocation.

**HAPS**: HAPS position allocation, dynamic spectrum and power distribution, edge
server compute resource provisioning.

**Drone (UAV)**: optimal drone 3D location assignment, channel estimation and
capacity provisioning, anti-interference spectrum management, navigation path
energy scheduling, resource scheduling and fairness allocation.

**Ground**: offloading between terrestrial cloud, LEO satellites and terrestrial
base stations serving terrestrial UEs.

### Challenges of DRL for SAGIN resource allocation

**Scalability.** **Non-stationarity from high mobility.** **Real-time deadlines
against slow learning.** The environment is large, it will not hold still long
enough for a policy to settle, and decisions are needed faster than learning
naturally converges.

### Conclusion

SAGINs power 6G everywhere, but their fast-changing, multi-layered resource
demands outpace traditional management methods. Deep reinforcement learning
enables real-time resource allocation and continuous improvement, driving
autonomous 6G non-terrestrial networks.

---

## Group 23 - HARQ mechanisms and limitations in NTN

### Background

A transmitter sends a packet, and noise, fading and interference corrupt bits in
the wireless channel, so the receiver gets a damaged packet.

Three approaches. **ARQ (Automatic Repeat Request)**: the sender waits for
ACK/NACK, and retransmits on error, after a timeout. **FEC (Forward Error
Correction)**: redundancy is added so errors are corrected without
retransmission. **HARQ (Hybrid ARQ)**: data plus FEC is sent, and on error the
receiver **combines and decodes** using both the stored copy and the
retransmission, giving increased reliability and efficiency.

### What HARQ is in 5G

HARQ lives in the **MAC layer** of the 5G stack (SDAP, PDCP, RLC, MAC, PHY). In
the terrestrial flow the gNB sends original data; if decoding succeeds the UE
sends ACK; if it fails the UE sends NACK, the gNB retransmits, the UE combines
both attempts and then sends ACK. At the receiver, a correct packet (above about
90 percent) gets an ACK, a damaged but repairable packet (about 70 percent) gets
an FEC repair, and a packet needing retransmission (about 30 percent) gets a
NACK.

### The specific NTN challenge

A terrestrial link has a **short RTT**. A satellite link has a **long and variable
RTT**. The failure chain runs: transmission, long satellite RTT, wait for
feedback, **process occupied**, **processes full**, **pipeline stall**,
**transmission stops**. New data cannot be sent because every HARQ process is
occupied waiting for ACK/NACK.

The comparison is stark. In **terrestrial 5G with short RTT**, ACKs return
quickly, processes are released, transmissions are continuous, and throughput is
high. In **NTN with long RTT**, all processes become busy, no free process
remains, the pipeline stalls, and **throughput drops drastically**. The RTT
quoted is **30 ms to 500+ ms**, over which all 16 processes end up waiting for
ACK/NACK.

### The mechanism

A ground station gNB sends packets P1 to P4 into a **data pipe** of parallel HARQ
processes, offset by **K_offset**, across a LEO RTT. The UE stores a failed packet
in a **soft buffer**. On NACK the gNB retransmits P1, and the UE performs **chase
combining** of the stored and the new copy, giving successful decoding.

### The two combining methods

**Chase combining.** The first transmission sends coded data bits with
redundancy. An error is detected, the UE stores the soft bits and sends NACK. The
second transmission sends **the same coded packet**. The receiver combines the
first reception (stored soft bits) with the second (new soft bits), decodes and
sends ACK.

**Incremental redundancy.** The first transmission sends systematic bits with some
parity bits punctured. The second transmission sends **different parity bits**,
the ones previously punctured. Soft combining of the two produces a combined
packet protected by a lower-rate, stronger code.

### Transparent against regenerative payloads

**Transparent payload**: the satellite is a repeater, the service link (Uu) runs
from the UE up and the feeder link down to a gateway-gNB, then NG to the 5GC and
N6 to the internet. The gNB is on the ground, so **the HARQ loop crosses both the
service and the feeder link**: the longest possible loop.

**Regenerative payload**: the gNB is on the satellite (SAT-gNB), with
inter-satellite links between spacecraft, the service link (Uu) from the UE, and
a feeder link to a gateway then to the 5GC and the internet. **The HARQ loop
closes over the service link alone**: the fastest loop, and the highest satellite
cost.

### How NTN addresses the limitation (3GPP Rel-17/18)

**1. Increase the number of HARQ processes.** The 5G default is **16 processes**;
the NTN adaptation allows **up to 32**. More parallel processes keep the pipe full
during a long RTT.

**2. Disable HARQ feedback (feedback-less).** The gNB or satellite sends data with
high redundancy and the UE returns **no ACK/NACK**. This avoids waiting for
feedback, relying instead on strong FEC or blind retransmissions.

**3. HARQ-less operation (higher layer recovery).** The gNB sends data and errors
are handled by **RLC or higher layers**. MAC and PHY do not wait for HARQ
feedback. Recovery is done at the RLC layer, which is slower but avoids stalling.

### Trade-offs

| Adaptation | Gain | Cost |
|---|---|---|
| More HARQ processes | Higher throughput | More memory required |
| Longer timers | No false alarms | Slower failure detection |
| Disable feedback | Constant flow | Delayed error recovery |
| Onboard processing | Fastest loop | Highest satellite cost |

### Conclusion

HARQ combines error correction, feedback, retransmission and soft combining to
improve radio-link reliability. Long and variable NTN RTT delays ACK/NACK
feedback, occupies HARQ processes and may reduce throughput. NTN adaptations keep
the pipeline moving, but increase memory, latency, complexity, power or hardware
cost.

---

## Group 24 - Network digital twinning for 3D satellite constellation simulation and optimization

### Context and background

**6G NTN** extends communication beyond terrestrial towers using satellites, UAVs
and HAPS. A **3D satellite constellation** distributes satellites in multiple
orbital planes providing global coverage. A **digital twin** is a **virtual
replica of a physical system that is continuously updated with real-world data**.
The continuous update is what distinguishes a twin from a simulation model.

### The specific NTN challenge

Dynamic 3D satellite constellation management faces six problems.

**1. Constant satellite mobility.** Satellites move at high speeds in orbit,
constantly changing their position relative to users and ground stations.
**2. Rapid topology changes.** Links between satellites and between satellites and
ground stations are frequently created or broken. **3. Long propagation delay.**
Large distances result in higher latency, affecting real-time communication and
control. **4. Limited onboard resources.** Satellites have constraints on power,
computation and storage, limiting complex operations. **5. Frequent handovers.**
Users must frequently switch between satellites or beams, causing potential
service interruptions. **6. High deployment and maintenance cost.** Launching
satellites and updating them in orbit is expensive and difficult.

In 6G NTN, satellites move constantly in 3D space, causing the network to change
every second. The consequences are **increased latency**, **routing
instability**, **resource allocation difficulties**, **reduced quality of
service**, **slow fault detection and recovery** and **higher operational costs**.

### The proposed mechanism

A **hierarchical digital twin network**. The physical system spans standard
satellites, data relay satellites and gateway satellites, with ground stations
and base stations below. Mirroring it are **edge digital twins** at the ground
stations and **central digital twins** in the terrestrial network, exchanging
DT-DT, PS-DT and PS-PS communications over the network topology.

Two controller levels. A **global controller** at the network control centre
handles network verification, global optimization, traffic engineering and
slicing management, working from global network models and a **central DT**
covering QoS, traffic status, topology dynamics and link status. A **local
controller** at each ground station handles beam allocation, radio resource
allocation, data processing and fault diagnosis, working from an **edge DT**
covering QoS, device status, mobility information and radio resource status.

Enabling techniques: AI, data modelling, cloud computation, optimization theory
and scalability.

### How digital twinning optimizes a 3D constellation

Five steps, with feedback for continuous learning and improvement.
**1. Collect** real-time satellite data. **2. Synchronize** the physical network
with the digital twin. **3. Simulate** multiple future network conditions.
**4. Evaluate** different routing and resource options. **5. Deploy** the best
decision to the physical network.

The distinguishing step is simulating multiple futures before committing to one.
That is what a twin adds over a plain control loop: decisions are tested in the
model rather than on the live network.

Benefits: **lower latency**, **better routing**, **faster fault detection** and
**reduced operational cost**.

### Applications

**Rural broadband**: high-speed internet to remote and underserved communities.
**Maritime communications**: reliable voice, data and IoT connectivity for ships.
**Aviation connectivity**: in-flight broadband and aircraft operations tracking.
**Disaster recovery**: restoring critical communication quickly when terrestrial
infrastructure is damaged. **Military and defence**: secure, resilient and
ubiquitous communication. **Earth observation missions**: real-time data
collection for environmental monitoring, weather forecasting and resource
mapping.

### Challenges and limitations

**High computational requirements**: large-scale constellation simulations need
powerful servers and high processing capability. **DT migration complexity**:
digital twins must migrate as satellites move, adding complexity.
**Synchronization overhead**: keeping the physical and digital networks
synchronized consumes bandwidth. **AI model accuracy**: poor predictions can lead
to suboptimal or wrong decisions. **Security concerns**: compromised digital twins
could be exploited to disrupt network operations, because decisions computed in
the twin are deployed to the real constellation.

### Summary

6G NTN satellite networks are highly dynamic and difficult to manage with
traditional methods. Network digital twinning creates a real-time virtual replica
for simulation, prediction and optimization. Hierarchical digital twin networks
improve monitoring, prediction, routing and optimization, reducing latency and
operational cost.

---

## AI-driven predictive handover management for high-mobility LEO networks

*(This deck carries no group number on its title slide.)*

### High mobility

From the ground, one LEO satellite appears, crosses the sky and disappears within
minutes. A **GEO** satellite is parked far above Earth and stays in the same spot.
A **LEO** satellite moves fast across the sky and its visibility window is short:
it appears low in the sky, passes overhead at best coverage, and disappears below
the horizon, all within **a few minutes**. LEO satellites travel about **7.5 km
every second** and circle the Earth in about **90 minutes**.

Because no single satellite stays overhead for long, the device keeps switching to
the next satellite that comes into view. **On normal mobile networks you move past
towers. On LEO networks the tower moves across the sky.**

### Problems

Doing this every few minutes, millions of times a day, creates real problems.

**1. Broken or choppy connection.** If the switch is not timed well, there is a
brief gap where data cannot get through, like a call that stutters.

**2. Handover storms.** Many devices share the same satellite. When it sets, they
all need to switch at nearly the same time, like every shopper rushing the same
checkout counter.

**3. The ping-pong effect.** If the system is not confident, a device flips
between two satellites, wasting effort and hurting the connection.

**4. Extra strain on limited resources.** Every handover needs signalling between
the device, the satellite and the ground network, and satellites have limited
power and processing to spare.

Handover is not the exception in LEO networks, it is the constant, everyday norm:
every few minutes, millions of devices, all day, every day. The goal is a smooth,
seamless connection, avoiding overload and storms, no ping-pong waste, efficient
use of limited resources, and reliable service every time.

### The reactive approach and why it is riskier in satellite networks

Traditional handover waits for the signal to get weak, then reacts. The device
keeps measuring signal, the signal gets noticeably weak, the device tells the
network it needs to switch now, the network scrambles to arrange the handover,
and the handover happens **after the problem has already appeared**.

On the ground, towers do not move, so only the radio signal is unpredictable. In
satellite networks, by the time the weak-signal warning travels to the satellite
and back to the ground network, **the satellite has already moved a meaningful
distance**. The decision comes back based on old, outdated information.

### The proactive approach

**The key insight: satellite motion is predictable.** Unlike random radio
interference, a satellite's flight path is not a mystery. It follows the fixed,
well-known laws of orbital motion, the same physics used to predict eclipses and
plan rocket launches. Therefore we can calculate in advance when any satellite
will rise, when it will be overhead and when it will set. And therefore we know
when a handover will become necessary **long before the signal weakens**.

Reactive means waiting for a problem, then reacting: problem occurs, delay while
the network reacts, higher risk of gaps and errors, less smooth, less reliable.
Predictive means seeing the handover coming and preparing ahead: predict using
orbital knowledge, prepare resources in advance, execute a fast seamless
handover, smoother, faster, more reliable, meaning better experience for users and
more efficient networks.

### First proactive approach: conditional handover

The network prepares the move ahead of time and gives the device backup options
and the conditions for switching. Reactively, the device detects a weak signal,
then device and network go back and forth in real time to negotiate, and the
handover is arranged at the moment it is needed. With conditional handover, the
network tells the device in advance: here are your backup satellites and the
conditions to switch (Backup 1, Backup 2), and the device monitors conditions and
switches automatically when they are met. This removes a lot of the delay and
back-and-forth that a purely reactive system would need, right at the busiest,
most time-critical moment.

**Where AI fits.** Conditional handover is the solid foundation, giving
predefined backup satellites and simple trigger conditions. AI builds on top: it
learns patterns from data, predicts changes in signal, congestion and satellite
movement, adapts decisions to many factors in real time, and chooses the best
satellite and best time to switch. The outcome is fewer unnecessary switches,
lower failure risk, smoother and faster handovers, better use of limited
resources and a better user experience. **Conditional handover was an important
improvement, but it still relies on relatively simple, fixed trigger conditions.
AI fills this gap by making those decisions smarter, adaptive and predictive.**

### Three complementary layers

**Layer 1 - trajectory and channel-quality prediction.** Forecast future
connectivity for each satellite using orbital trajectory plus past signal history.
Because satellite orbits are deterministic, one class of methods forecasts the
**physical quantities** that drive handover decisions: elevation angle, slant
range, Doppler shift and received signal quality, ahead of time, using propagation
models such as **SGP4** combined with learned correction models. Another popular
approach forecasts the **RSRP time series** itself using deep learning models such
as **CNN + LSTM**, so each terminal can predict its own future RSRP trajectory and
decide handover targets and timing autonomously. What is predicted, by example:
elevation angle, slant range, range-rate and Doppler shift, path loss and
SNR/RSRP, RSRP time series, optimal handover timing (when) and handover target
(which satellite).

**Layer 2 - reinforcement-learning-based handover decision.** The second layer
treats the handover decision itself, which satellite to switch to and when, as a
sequential decision problem solved via reinforcement learning. RL formulates
handover as a **Markov Decision Process**. **State**: current and predicted
network, link and geometry features, including current link quality (RSRP, SINR),
predicted link quality, relative speed, elevation and geometry, and network load,
battery, mobility and history. **Action**: choose the target satellite (Sat A,
Sat B, Sat C) or stay with the current satellite. **Environment**: the network
responds to the action. **Reward**: balances link quality with handover cost.
Positive for high link quality, stable connection and successful handover;
negative for frequent handovers, handover failures and high signalling cost.
**Policy** `pi(a|s)` learns to maximise long-term reward. **Output**: the optimal
handover action, which satellite and when.

The deck compares a **legacy protocol with measurement report** (measure, report,
decide, handover; higher access delay, higher collision rate, lower handover
success rate) against **DHO (Deep-learning-based HandOver) with no measurement
report** (observe, decide, handover; **directly predicts the appropriate handover
action**, removing the measurement report step entirely; lower access delay, lower
collision rate, higher handover success rate). Key benefits: lower access delay
and faster decision-making, lower collision rate and fewer simultaneous handovers,
higher handover success rate and more reliable connectivity, adaptation to
changing network conditions and mobility patterns, and continuous learning and
improvement over time.

**Layer 3 - graph- and optimisation-based predictive scheduling, "the air-traffic
controller".** This technique looks at the bigger picture across many users and
many satellites at once. Much like an air-traffic controller who does not just
look at one plane in isolation, but assigns and sequences many planes to runways
so that everything flows smoothly without overload, this method works out **the
best overall pattern of handovers across all connected devices and satellites**,
balancing load, avoiding congestion, and keeping the whole system running
efficiently rather than optimising just one connection at a time. How it works at
a high level: many users and satellites, model the system as a graph (devices,
satellites, links, constraints), use optimisation to find the best global handover
plan, schedule handovers in advance, execute handovers seamlessly, and achieve
better load balance, less congestion and higher efficiency for all. **Key idea:
optimise the whole system, not just a single connection.**

The three layers work together: **forecast** predicts link quality for all
satellites; **decide** lets the RL agent pick the best device for each device;
**optimise** applies graph and optimisation-layer decisions for the whole network.
System benefits: seamless, reliable connectivity; fewer drops and lower latency;
efficient use of limited resources; a stable network with no ping-pong or storms;
and a better experience for all users.

### Applications

**Rural broadband**: reliable internet where terrestrial towers cannot reach.
**Maritime tracking**: continuous connectivity for vessels far from shore.
**Aviation connectivity**: in-flight broadband as planes cross satellite beams.
**Defense and security**: resilient links for military and mission-critical
operations. **Disaster recovery**: instant network coverage when ground
infrastructure fails. **IoT and transport**: tracking for trains, trucks and
remote sensors on the move.

### Challenges and limitations

**Computational complexity against SWaP constraints**, where SWaP is size, weight
and power, the tight budget every satellite must operate within. **Onboard power
drain**: running AI/ML inference natively on a satellite consumes scarce onboard
power that would otherwise serve the payload. **Heat generation**: continuous
prediction workloads generate excess heat that is hard to dissipate in the vacuum
of space. **Limited hardware**: satellite compute hardware is far less powerful
than ground-based servers, constraining model size and accuracy.

---

## AI-assisted trajectory optimization of UAV and HAPS platforms for 3D coverage in 6G NTN

*(This deck carries no group number on its title slide.)*

### The core concept

6G aims to provide **global connectivity** beyond terrestrial networks using NTN
such as satellites, UAVs (drones) and HAPS. **AI enables autonomous movement and
optimization** in areas where traditional deployment causes poor coverage, high
latency and network congestion.

### 6G NTN architecture and platforms

Three tiers. **Satellites (LEO/MEO/GEO)**: wide-area coverage, backhaul
connectivity, IoT and broadcast services. **HAPS (about 20 km altitude)**:
quasi-stationary platforms, large coverage of hundreds of kilometres, acting as
aerial base stations and providing backhaul for UAVs. **UAVs (low altitude)**:
highly flexible and agile, rapid deployment, on-demand coverage, supporting
hotspots and disaster areas. Below them, **terrestrial networks**: ground base
stations, fibre and backhaul, core network and edge cloud.

### 3D coverage challenges

Current UAV/HAPS deployment suffers from **static trajectories**, **uneven user
distribution**, **coverage holes**, **high interference**, **energy limitations**
and **dynamic user mobility**. The platforms can move, but if they follow fixed
paths they behave like fixed towers.

### The solution: AI-assisted trajectory optimization

**Artificial Intelligence** is the broader concept of creating machines that can
perform human-like tasks, while **Machine Learning** is a branch of AI that
enables these machines to **learn from data and improve their performance without
explicit programming**.

### Deep reinforcement learning

Why DRL? It **learns by interacting with the environment**, **adapts to changing
user locations** and **optimizes long-term rewards**. Trajectory planning is
sequential: where the platform goes now changes what is available later, so
optimising long-term reward rather than the immediate step is exactly the right
tool.

The UAV/HAPS continuously collects: **user locations (x, y)**, **signal strength
(SINR/SNR)**, **battery level**, **traffic demand**, **obstacles (buildings,
terrain)**, **weather conditions** and **backhaul link quality**.

The **reward function** maximises coverage while minimising **energy**, **delay**
and **interference**.

**Positive reward (+)**: more users covered, higher throughput, lower latency,
lower interference, lower energy consumption. **Negative reward (-)**: coverage
holes, signal blockage, high interference, excessive battery use, weak backhaul
links.

### Applications

Emergency communication, military operations, precision agriculture, mining,
disaster recovery, maritime communication, remote healthcare, smart
transportation.

### Challenges

Battery limitations, AI computational complexity, airspace regulations, security,
weather effects. Several of these are non-technical constraints on an otherwise
workable technique.

### Conclusion

AI significantly improves UAV/HAPS trajectory planning. Intelligent mobility
enhances 3D coverage in 6G NTNs. Reinforcement learning enables autonomous,
adaptive decision-making. The proposed framework improves coverage, energy
efficiency and quality of service for future wireless networks.

---

## Appendix: figures worth memorising

| Figure | Value | Deck |
|---|---|---|
| LEO altitude / velocity | 300-1,500 km / ~7.5-7.8 km/s | Groups 1, 8, 12, 17 |
| LEO orbital period | ~90 minutes | Predictive handover |
| LEO satellite visibility window | ~6-10 minutes | Group 16 |
| S-band LEO Doppler at 600 km | up to ±48 kHz, zero at zenith | Groups 3, 15 |
| Doppler rate of change at zenith | ~500 Hz/s | Group 15 |
| Differential delay across a LEO beam | ~650 us | Group 3 |
| Longest preamble cyclic prefix | 684 us (≈34 us margin) | Group 3 |
| LEO round-trip delay | 25.8 ms (600 km) | Group 16 |
| GEO round-trip delay | 541 ms; ~275 ms quoted for GNSS in NTN | Groups 13, 16 |
| HAPS altitude / latency / radius | ~20 km / 1-10 ms / 50-100 km | Group 5 |
| HAPS link-budget gain over 500 km LEO | ~28 dB | Group 5 |
| HAPS endurance record | 12 days | Group 5 |
| GPS orbit | ~20,200 km, 6 planes, 55°, ~12 h | Group 13 |
| Galileo orbit | 23,222 km, 3 planes, 56°, ~14 h 5 min | Group 13 |
| Shared civil frequency | GPS L1 / Galileo E1 at 1575.42 MHz | Group 13 |
| 1 microsecond clock error | ~300 m position error | Group 13 |
| SBAS / DGPS / PPP / RTK accuracy | 1-2 m / 1-3 m / 5-20 cm / 1-2 cm | Groups 4, 13 |
| HARQ processes | 16 default, up to 32 for NTN | Group 23 |
| NTN RTT that stalls HARQ | 30 ms to 500+ ms | Group 23 |
| eRACH gains | +31.2% / +54.6% throughput, 1.49x lower delay, 4.94x collisions | Groups 3, 17 |
| CSI encoder compression | 1/16 to 1/64 | Group 11 |
| ISAC monostatic cancellation | >70 dB | Group 9 |
| DebriSense-THz classification | 95-99% at 5 THz | Group 9 |
| GNSS received power | ~-130 dBm | Group 15 |
| Terrestrial 5G n77/n78 | 3.3-4.2 GHz | Group 7 |
| NTN n256 | 2170-2200 MHz | Group 7 |
| Non-RT / Near-RT RIC loop | >1 s / <1 s | Group 10 |
