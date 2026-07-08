#!/usr/bin/env python3
"""
Build a compact "what is / why is" theory reference for TE 458 Modules
1-3 (Introduction to Network Planning & Optimization; Traffic Engineering
& Network Dimensioning; Propagation Modelling & Coverage Design) --
definitions and concepts only, no calculations (those are covered
separately by the Formula Sheet and the Tutorial 1 practice sets).

Content is transcribed/paraphrased directly from the module decks'
text layer (same source-of-truth extraction used for the Formula
Sheet), each entry citing its module/page for traceability.

Module 4 (Capacity & Interference Planning) is intentionally excluded
per the request -- only Modules 1-3.

Output is written directly into the course source folder (not the
bank/npao working directory), since this is a reference document for
that material rather than a generated practice artifact.

    .venv2/bin/python3 make_theory_reference_pdf.py
"""
import fitz  # PyMuPDF

OUT = "/mnt/c/Users/wgcha/Documents/y4s2/Network Planning and Optimization/NPAO-Theory-Reference-Modules1-3.pdf"

TITLE = "TE 458 &mdash; Theory Reference: Modules 1&ndash;3"
SUBTITLE = "Compact \"what is / why is\" definitions and concepts &mdash; no calculations. Covers Module 1 (Intro), Module 2 (Traffic Engineering), Module 3 (Coverage Planning)."

CSS = """
body { font-family: sans-serif; color: #14213a; font-size: 10px; line-height: 1.32; }
h1 { font-size: 18px; margin: 0 0 2px 0; color: #3730a3; }
h2 { font-size: 10.5px; margin: 0 0 16px 0; color: #64748b; font-weight: normal; }
h3 { font-size: 14px; margin: 18px 0 8px 0; color: #3730a3; border-top: 1px solid #cbd5e1; padding-top: 10px; }
h4 { font-size: 11px; margin: 12px 0 4px 0; color: #4338ca; }
.qt { font-size: 10.2px; font-weight: bold; margin: 8px 0 1px 0; color: #111827; }
.a { font-size: 9.7px; margin: 1px 0 2px 0; color: #1f2937; }
.src { font-size: 8px; color: #9ca3af; margin: 0 0 6px 0; font-style: italic; }
.note { font-size: 9px; color: #9a3412; background: #fff7ed; padding: 4px 6px; margin: 4px 0 10px 0; border-left: 3px solid #fb923c; }
table { border-collapse: collapse; margin: 4px 0 8px 0; font-size: 8.8px; width: 100%; }
td, th { border: 1px solid #cbd5e1; padding: 2px 6px; }
th { background: #eef2ff; text-align: left; }
ul { margin: 2px 0 6px 0; padding-left: 16px; font-size: 9.5px; }
li { margin: 1px 0; }
"""

BODY = f"""
<h1>{TITLE}</h1>
<h2>{SUBTITLE}</h2>

<p class="note">Definitions and concepts only, transcribed/paraphrased directly from the module
decks' text layer &mdash; no formulas or worked numbers here (see the separate Formula Sheet and
Tutorial 1 practice sets for those). Each entry cites its module/page so you can cross-check.
Module 4 is intentionally excluded from this reference.</p>

<h3>Module 1 &mdash; Introduction to Network Planning &amp; Optimization</h3>

<p class="qt">What is network planning?</p>
<p class="a">The engineering process of designing and dimensioning a communication network before
deployment so it can meet coverage, capacity, quality, reliability and cost objectives. It answers:
where should nodes be placed, how much capacity is needed, what coverage area must be served, what
technologies/resources to use, and how the network should grow.</p>
<p class="src">Source: Module 1, p.3</p>

<p class="qt">What is network optimization?</p>
<p class="a">The continuous process of improving the performance of an existing or planned network
by adjusting parameters, resources, topology or operating policies. It focuses on coverage, capacity,
throughput, latency, reliability, energy efficiency and user experience.</p>
<p class="src">Source: Module 1, p.4</p>

<p class="qt">What is network dimensioning?</p>
<p class="a">The process of estimating and allocating required resources (channels, bandwidth, sites,
links, wavelengths, processing capacity) so expected traffic demand can be served with acceptable
QoS, reliability and cost.</p>
<p class="src">Source: Module 1, p.5</p>

<p class="qt">How do planning and optimization differ?</p>
<p class="a">Planning asks "how should the network be designed?", happens before/during deployment,
and takes forecast demand/coverage area/budget as input to produce a design (e.g. site planning,
link budget, capacity estimate). Optimization asks "how can the network be improved?", happens after
deployment/during operation, and takes KPIs/measurements/complaints/logs as input to produce
improved configuration or performance (e.g. handover tuning, load balancing, power adjustment).</p>
<p class="src">Source: Module 1, p.6</p>

<p class="qt">Why do planning and optimization matter?</p>
<p class="a">Poor planning causes coverage holes, congestion, high call/session drop rate, poor
throughput, excessive interference and high operational cost. Good optimization improves service
quality, resource utilization, customer satisfaction, reliability and operator revenue.</p>
<p class="src">Source: Module 1, p.7</p>

<p class="qt">What is the network lifecycle?</p>
<p class="a">Demand Estimation &rarr; Network Design &rarr; Deployment &rarr; Operation &rarr;
Optimization, with a feedback loop back into redesign. Planning is not a one-time activity;
operational feedback continuously informs redesign and optimization.</p>
<p class="src">Source: Module 1, p.8</p>

<p class="qt">What is the scope of network planning?</p>
<p class="a">It spans several layers: radio access planning (coverage, capacity, interference,
handover areas); IP/core planning (routing, redundancy, traffic engineering, QoS); transport/optical
planning (fibre routes, optical power budget, DWDM, OTN, ROADM placement); and service planning
(SLAs, user demand, QoE targets, service differentiation).</p>
<p class="src">Source: Module 1, p.9</p>

<p class="qt">What is the difference between QoS and QoE?</p>
<p class="a">QoS (Quality of Service) refers to measurable, network-centric performance parameters:
throughput, delay, jitter, packet loss, availability. QoE (Quality of Experience) refers to the
user's perceived quality of the service &mdash; call clarity, video smoothness, web responsiveness,
application satisfaction. Good planning must consider both.</p>
<p class="src">Source: Module 1, p.10&ndash;11</p>

<p class="qt">What are KPIs (Key Performance Indicators)?</p>
<p class="a">Measurable indicators used to evaluate whether a network meets its performance
objectives &mdash; e.g. coverage probability, call setup success rate, drop call rate, handover
success rate, throughput, latency, packet loss, availability, congestion rate. Categories include
Coverage, Quality, Accessibility, Retainability, Mobility, Capacity, and Availability.</p>
<p class="src">Source: Module 1, p.12&ndash;13</p>

<p class="qt">What is a Service Level Agreement (SLA)?</p>
<p class="a">A formal agreement specifying the expected level of service between a provider and a
customer &mdash; e.g. minimum availability, maximum latency, minimum throughput, fault repair time,
packet loss limits. Planning ensures infrastructure can support SLA targets; optimization ensures
targets continue to be met during operation.</p>
<p class="src">Source: Module 1, p.14</p>

<p class="qt">What is the difference between CAPEX and OPEX?</p>
<p class="a">CAPEX (capital expenditure) is the cost of acquiring and deploying network assets:
towers/sites, base stations, routers/switches, fibre deployment, spectrum acquisition. OPEX
(operational expenditure) is the cost of running and maintaining the network: energy, site rental,
maintenance, backhaul leasing, field operations.</p>
<p class="src">Source: Module 1, p.15</p>

<p class="qt">What trade-offs does network planning involve?</p>
<p class="a">More sites improve coverage but increase CAPEX/OPEX; higher transmit power may improve
coverage but increase interference; smaller cells improve capacity but increase handover frequency;
more redundancy improves reliability but increases cost. Planning is about achieving a balanced
design, not maximizing one parameter.</p>
<p class="src">Source: Module 1, p.16</p>

<p class="qt">How has network planning evolved from 2G to 6G?</p>
<p class="a">2G focused on voice/SMS (coverage, frequency reuse, Erlang capacity); 3G on mobile data
(coverage, interference, soft handover, data capacity); 4G on mobile broadband (SINR, throughput,
packet scheduling, IP backhaul); 5G on eMBB/URLLC/mMTC (densification, slicing, massive MIMO, edge
computing); 6G on AI-native/sensing/THz/non-terrestrial networks (automation, intelligence, digital
twins, integrated terrestrial/non-terrestrial planning).</p>
<p class="src">Source: Module 1, p.18&ndash;19</p>

<p class="qt">What data sources feed planning vs. optimization?</p>
<p class="a">Planning uses population/user density data, traffic forecasts, terrain/clutter maps,
building/road maps, spectrum allocation data, existing KPI reports, drive-test measurements,
complaint data, and cost/business constraints. Optimization is based on live/measured network
information: KPI dashboards, network counters, drive-test logs, call/session trace data, alarms,
traffic load measurements, user experience reports. Optimization should be evidence-based, not
guesswork.</p>
<p class="src">Source: Module 1, p.20&ndash;21</p>

<p class="qt">What are typical optimization actions?</p>
<p class="a">Adjusting antenna tilt/azimuth, tuning transmit power, adding/removing neighbour
relations, modifying handover thresholds, rebalancing traffic across cells/links, adding capacity
where congestion occurs, rerouting traffic, upgrading backhaul/transport, improving fault response.</p>
<p class="src">Source: Module 1, p.22</p>

<h3>Module 2 &mdash; Traffic Engineering &amp; Network Dimensioning</h3>

<p class="qt">What is traffic engineering?</p>
<p class="a">The process of estimating, modelling, controlling and dimensioning network resources so
communication traffic can be carried with acceptable quality and efficient resource utilization. It
answers: how much traffic will users generate, how many channels/links/servers are required, what
blocking/delay level is acceptable, and when to expand capacity.</p>
<p class="src">Source: Module 2, p.3</p>

<p class="qt">Why does traffic engineering matter?</p>
<p class="a">Under-dimensioning leads to blocking, congestion, packet loss, poor throughput and poor
user experience. Over-dimensioning leads to wasted capacity, higher CAPEX/OPEX, and poor return on
investment. Traffic engineering balances service quality and resource cost.</p>
<p class="src">Source: Module 2, p.4</p>

<p class="qt">What are offered, carried and lost traffic?</p>
<p class="a">Offered traffic is the demand presented to the network by users. Carried traffic is the
portion successfully served. Lost traffic is the portion rejected due to insufficient resources. If
resources are enough, most offered traffic is carried; if not, some is blocked or delayed.</p>
<p class="src">Source: Module 2, p.5&ndash;6</p>

<p class="qt">What is busy hour traffic, and why dimension for it?</p>
<p class="a">Busy hour traffic is the traffic carried/offered during the busiest continuous one-hour
period of the day. Networks are normally dimensioned for busy hour traffic because dimensioning only
for average daily traffic can lead to congestion during peak periods. Busy hour varies by service
type (e.g. voice peaks evening, office data peaks working hours, video peaks at night).</p>
<p class="src">Source: Module 2, p.9</p>

<p class="qt">What is Grade of Service (GoS)?</p>
<p class="a">A measure of the probability that a call/session is blocked or delayed during the busy
hour. In circuit-switched systems it is commonly expressed as blocking probability (e.g. GoS = 0.02
means about 2 in 100 attempts may be blocked). Lower GoS means better service but requires more
resources.</p>
<p class="src">Source: Module 2, p.11</p>

<p class="qt">What is blocking, and what is delay probability?</p>
<p class="a">Blocking occurs when a new request arrives and all required resources are already
occupied (e.g. all voice channels/trunk circuits busy) &mdash; blocking probability is the chance a
request is rejected. Delay probability is the probability that an arriving request must wait before
being served (e.g. packet buffers, call-centre queues) &mdash; important where requests can queue
instead of being blocked.</p>
<p class="src">Source: Module 2, p.12&ndash;13</p>

<p class="qt">What is the difference between a loss system and a delay system?</p>
<p class="a">In a loss system, a request is blocked/lost if resources are busy (typical model: Erlang
B; metric: blocking probability; example: trunk circuits, voice channels). In a delay system, a
request waits in a queue instead (typical model: Erlang C; metric: delay probability; example:
packet buffers, call centres).</p>
<p class="src">Source: Module 2, p.14</p>

<p class="qt">What is the Erlang B model used for, and when should it be used?</p>
<p class="a">Erlang B estimates blocking probability in a loss system where blocked calls are cleared
immediately (users do not wait or retry). Use it when the system has a fixed number of resources,
users are blocked if all are busy, there is no queue, and blocked users abandon the attempt &mdash;
e.g. traditional telephone trunk dimensioning, circuit-switched voice channels, legacy cellular
voice capacity.</p>
<p class="src">Source: Module 2, p.15&ndash;16</p>

<p class="qt">What is the Erlang C model used for, and when should it be used?</p>
<p class="a">Erlang C estimates the probability that an arriving request must wait in a queue before
being served. Use it when requests wait instead of being blocked and there is a queue &mdash; e.g.
call centres, packet-processing systems, shared server systems. Erlang B is about loss/blocking;
Erlang C is about waiting/delay.</p>
<p class="src">Source: Module 2, p.18&ndash;19</p>

<p class="qt">What is queueing theory, and what describes a queueing system?</p>
<p class="a">Queueing theory studies systems where users, packets or sessions wait for service. A
queueing system is described by its arrival process, service process, number of servers, buffer
size, and queue discipline. Examples: router buffers, packet schedulers, call centres, base-station
resource queues, server farms.</p>
<p class="src">Source: Module 2, p.20</p>

<p class="qt">What is Kendall notation, and what do M, D, G mean?</p>
<p class="a">A queue is represented as A/S/c/K, where A = arrival process, S = service time
distribution, c = number of servers, K = system capacity/buffer size (often omitted, implying
infinite/non-central capacity). M = Markovian/memoryless (Poisson arrivals or exponential service);
D = deterministic (fixed inter-arrival or service time); G = general distribution. Examples: M/M/1,
M/M/c, M/D/1, D/M/1, G/G/1.</p>
<p class="src">Source: Module 2, p.22&ndash;23</p>

<p class="qt">What are the principles of network dimensioning?</p>
<p class="a">Determine the service area and user population; estimate traffic per user; estimate busy
hour traffic; choose a target GoS or delay requirement; compute required channels/links/servers/
spectrum/capacity; and add a margin for growth, failures and uncertainty.</p>
<p class="src">Source: Module 2, p.24</p>

<p class="qt">How does dimensioning differ across network segments?</p>
<p class="a">Radio access dimensions spectrum/PRBs/sectors/carriers (metric: users, throughput, SINR,
GoS). Circuit/trunk networks dimension circuits/channels (metric: Erlangs, blocking probability).
Packet core dimensions links/routers/buffers (metric: throughput, delay, packet loss). Transport
dimensions fibre links/wavelengths/OTN containers (metric: capacity, protection, utilization).
Cloud/edge dimensions servers/storage/compute (metric: CPU load, latency, service requests).</p>
<p class="src">Source: Module 2, p.26</p>

<p class="qt">Why is a growth margin needed in dimensioning?</p>
<p class="a">Demand grows due to more users, more devices per user, higher video/cloud usage, new
applications, and IoT/machine-type communication. A design that works today may become congested in
one or two years, so planning should include spare capacity without over-investing.</p>
<p class="src">Source: Module 2, p.27</p>

<p class="qt">What are common mistakes in dimensioning?</p>
<p class="a">Using average traffic instead of busy hour traffic; ignoring growth in demand; ignoring
traffic variation across locations; assuming all users behave the same way; planning access capacity
but forgetting backhaul; ignoring redundancy/failure scenarios; choosing a GoS target without
considering business requirements.</p>
<p class="src">Source: Module 2, p.36</p>

<h3>Module 3 &mdash; Propagation Modelling &amp; Coverage Design</h3>

<p class="qt">What is coverage planning?</p>
<p class="a">The process of estimating and designing the geographical area over which users can
receive adequate signal strength and quality from a network. It answers: how far can a base station
reach, what transmit power/antenna height are required, which areas will have weak signal, how many
sites are needed, and what margins are needed for fading/buildings/terrain.</p>
<p class="src">Source: Module 3, p.3</p>

<p class="qt">Why is propagation modelling needed?</p>
<p class="a">Radio waves weaken with distance, and buildings/trees/hills/rain/terrain cause additional
loss; received signal varies with distance, frequency, height and environment. Propagation models
help estimate path loss before physical deployment, allowing engineers to predict coverage, estimate
cell radius, and reduce deployment trial-and-error.</p>
<p class="src">Source: Module 3, p.4</p>

<p class="qt">What do link budget calculations do, and why is uplink more critical?</p>
<p class="a">Link budgets give the signal-strength loss between mobile and base-station antennas, help
define cell ranges and coverage thresholds, and are computed for both uplink and downlink. The uplink
is more critical because the power transmitted by the mobile station is much less than that
transmitted by the base station.</p>
<p class="src">Source: Module 3, p.6</p>

<p class="qt">What do MS sensitivity and BTS sensitivity depend on, and what are typical values?</p>
<p class="a">Both depend on the receiver noise figure and the minimum required E<sub>b</sub>/N<sub>0</sub>.
Recommended MS sensitivity values: GSM900 &asymp; &minus;102 dBm, GSM1800 &asymp; &minus;100 dBm.
Recommended BTS sensitivity: &asymp; &minus;106 dBm. In practice, link budgets use the manufacturer's
stated value.</p>
<p class="src">Source: Module 3, p.9</p>

<p class="qt">What is fade margin, conceptually?</p>
<p class="a">A margin included in the link budget to protect against signal fading; it is the
difference between the received signal (P<sub>r</sub>) and the receiver threshold. It is included so
the link keeps working even when the signal fluctuates below its average level.</p>
<p class="src">Source: Module 3, p.12</p>

<p class="qt">What other parameters appear in a link budget?</p>
<p class="a">Antenna gains, diversity gain, cable and connector losses, other equipment loss factors
(isolator, combiner, filter losses), and two gain factors: mast head amplifier (MHA) and booster.</p>
<p class="src">Source: Module 3, p.13</p>

<p class="qt">What is receiver sensitivity, and what is the coverage condition?</p>
<p class="a">Receiver sensitivity is the minimum received power required for the receiver to correctly
detect and decode a signal at an acceptable error rate. If the received power P<sub>r</sub> is at
least the sensitivity, the link is feasible; if below it, the user may see weak signal, dropped
sessions or low throughput. Coverage exists where the received signal is above the required
threshold.</p>
<p class="src">Source: Module 3, p.23</p>

<p class="qt">What does Maximum Allowable Path Loss (MAPL) mean for planning?</p>
<p class="a">MAPL is the largest path loss the link can tolerate while the received power still meets
the receiver sensitivity requirement. The cell radius is the distance at which the predicted path
loss equals MAPL &mdash; it is the central quantity linking the link budget to a physical coverage
distance.</p>
<p class="src">Source: Module 3, p.24</p>

<p class="qt">What is free-space path loss, and what is its key idea?</p>
<p class="a">Free-space path loss assumes clear line-of-sight propagation with no obstacles,
reflections or diffraction. The key idea is that path loss increases with both distance and
frequency &mdash; doubling either roughly adds about 6 dB of loss.</p>
<p class="src">Source: Module 3, p.25, 31</p>

<p class="qt">Why is the free-space model not enough for real planning?</p>
<p class="a">Real environments include buildings and walls, trees/vegetation, terrain height
variation, moving vehicles/people, reflection and scattering, diffraction around obstacles, and
indoor penetration loss. Free-space loss is a useful baseline, but practical planning requires
empirical or site-specific propagation models.</p>
<p class="src">Source: Module 3, p.33</p>

<p class="qt">What are the main propagation environment types?</p>
<p class="a">Rural (few obstacles, longer cell radius), suburban (moderate clutter, moderate path
loss), urban (high building density, strong shadowing, shorter cell radius), dense urban (tall
buildings, street canyons, severe multipath/blockage), and indoor (walls, floors, partitions,
furniture, human blockage).</p>
<p class="src">Source: Module 3, p.34</p>

<p class="qt">What is the Okumura-Hata model for, and when should it be used?</p>
<p class="a">An empirical propagation model widely used for macrocell coverage planning in cellular
networks, typically applied around 150&ndash;1500 MHz across urban, suburban and rural environments.
It gives median path loss rather than instantaneous fading behaviour, and should ideally be
calibrated with field measurements for local accuracy.</p>
<p class="src">Source: Module 3, p.35&ndash;36</p>

<p class="qt">What is the COST-231 Hata model, and how does it extend Hata?</p>
<p class="a">It extends the Hata model to higher frequencies (roughly 1.5&ndash;2 GHz), especially for
urban and suburban cellular planning, adding a correction constant C (0 dB for medium-sized
cities/suburban, 3 dB for metropolitan/dense-urban areas).</p>
<p class="src">Source: Module 3, p.37</p>

<p class="qt">What do the log-distance and log-normal shadowing models represent?</p>
<p class="a">The log-distance model expresses path loss as increasing with the logarithm of distance
from a reference point, scaled by a path-loss exponent n that depends on the environment. The
log-normal shadowing model adds a zero-mean Gaussian random term on top of that, representing the
random variation caused by shadowing (buildings, terrain, clutter).</p>
<p class="src">Source: Module 3, p.38</p>

<p class="qt">What is the difference between shadowing and fast fading?</p>
<p class="a">Shadowing is a slow variation in signal level caused by buildings, terrain and clutter,
often modelled as log-normal. Fast fading is a rapid signal fluctuation caused by multipath
propagation, changing over small distances or short time intervals. Coverage design includes margins
to protect against both.</p>
<p class="src">Source: Module 3, p.40</p>

<p class="qt">How is cell radius estimated (as a process, not a formula)?</p>
<p class="a">First compute the Maximum Allowable Path Loss from the link budget; then select an
appropriate propagation model; then solve for the distance at which the model's predicted path loss
equals the MAPL. The result is a planning approximation &mdash; actual coverage depends on terrain,
clutter, interference and antenna configuration.</p>
<p class="src">Source: Module 3, p.42</p>

<p class="qt">What is a coverage map, and what can it show?</p>
<p class="a">A geographical representation of predicted or measured signal strength or quality over an
area. It may show received signal level, RSRP/RSSI, SINR, serving-cell regions, coverage holes, and
interference zones.</p>
<p class="src">Source: Module 3, p.44</p>

<p class="qt">What is a coverage hole, and what causes it?</p>
<p class="a">An area within the intended service region where the signal falls below the required
threshold. Causes include distance from the serving site, building/terrain blockage, poor antenna
orientation, insufficient transmit power, indoor penetration loss, and interference reducing
effective signal quality.</p>
<p class="src">Source: Module 3, p.46</p>

<p class="qt">How can coverage be improved?</p>
<p class="a">Increasing antenna height, adjusting antenna tilt/azimuth, increasing transmit power
(within regulatory/interference limits), adding new sites or small cells, using repeaters or
distributed antenna systems, improving receiver sensitivity, using lower-frequency bands, or applying
beamforming/massive MIMO.</p>
<p class="src">Source: Module 3, p.47</p>

<p class="qt">How do you distinguish a coverage problem from a capacity problem?</p>
<p class="a">A coverage problem shows weak signal (metric: RSRP/RSSI), typically caused by high path
loss or blockage, solved with a new site/antenna change/lower band. A capacity problem shows
congestion or low throughput (metric: throughput, PRB utilization, blocking), typically caused by too
many users or insufficient resources, solved by adding spectrum, sectorization, or densification.</p>
<p class="src">Source: Module 3, p.48</p>

<p class="qt">What is the overall planning workflow for coverage design?</p>
<p class="a">Define service area &rarr; set coverage threshold &rarr; prepare link budget &rarr;
select propagation model &rarr; estimate cell radius &rarr; generate coverage map &rarr; verify with
measurements &rarr; optimize design.</p>
<p class="src">Source: Module 3, p.49</p>

<p class="qt">What are common coverage planning mistakes?</p>
<p class="a">Using free-space path loss for urban/indoor planning; ignoring building penetration loss;
ignoring terrain and clutter; designing only for outdoor coverage when indoor users dominate;
ignoring uplink coverage constraints; confusing coverage improvement with capacity improvement; and
not validating predictions with field measurements.</p>
<p class="src">Source: Module 3, p.50</p>
"""


def main():
    story = fitz.Story(html="<body>" + BODY + "</body>", user_css=CSS)
    writer = fitz.DocumentWriter(OUT)
    mediabox = fitz.paper_rect("a4")
    where = mediabox + (50, 50, -50, -50)

    pages = 0
    more = 1
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
        pages += 1
    writer.close()
    print(f"Wrote {OUT}: {pages} pages")


if __name__ == "__main__":
    main()
