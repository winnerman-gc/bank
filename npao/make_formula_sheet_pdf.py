#!/usr/bin/env python3
"""
Build NPAO-Formula-Sheet.pdf: every formula from TE 458 Modules 1-4 and
Tutorial 1 (+ solutions), with a brief explanation and "when to use" note
for each. All formulas are copied verbatim (text-layer extraction, not
vision) from the source PDFs at
  /mnt/c/Users/wgcha/Documents/y4s2/Network Planning and Optimization/
so every entry is directly traceable to a slide or tutorial page.

Uses PyMuPDF's Story API for automatic multi-page text reflow (same
approach as policy/make_pdf.py / make_theory_pdf.py).
    .venv2/bin/python3 make_formula_sheet_pdf.py
"""
import fitz  # PyMuPDF

OUT = "NPAO-Formula-Sheet.pdf"
TITLE = "TE 458 &mdash; Network Planning &amp; Optimization: Formula Sheet"
SUBTITLE = "Every formula from Modules 1&ndash;4 and Tutorial 1 (+ solutions), with explanations and usage notes"

CSS = """
body { font-family: sans-serif; color: #14213a; font-size: 10.5px; line-height: 1.4; }
h1 { font-size: 18px; margin: 0 0 2px 0; color: #3730a3; }
h2 { font-size: 11px; margin: 0 0 16px 0; color: #64748b; font-weight: normal; }
h3 { font-size: 14px; margin: 20px 0 8px 0; color: #3730a3; border-top: 1px solid #cbd5e1; padding-top: 12px; }
.f { font-size: 11px; font-weight: bold; margin: 14px 0 3px 0; color: #111827; }
.formula { font-family: monospace; background: #f1f5f9; padding: 5px 8px; margin: 3px 0 5px 0; font-size: 10.5px; border-left: 3px solid #4338ca; }
.vars { font-size: 9.5px; color: #475569; margin: 2px 0 4px 0; }
.use { font-size: 9.8px; color: #14213a; margin: 2px 0 2px 0; }
.use b { color: #15803d; }
.src { font-size: 8.5px; color: #9ca3af; margin: 2px 0 10px 0; font-style: italic; }
.note { font-size: 9.5px; color: #9a3412; background: #fff7ed; padding: 5px 8px; margin: 6px 0 10px 0; border-left: 3px solid #fb923c; }
table { border-collapse: collapse; margin: 6px 0 12px 0; font-size: 9.5px; width: 100%; }
td, th { border: 1px solid #cbd5e1; padding: 3px 8px; }
th { background: #eef2ff; text-align: left; }
"""

BODY = f"""
<h1>{TITLE}</h1>
<h2>{SUBTITLE}</h2>

<p class="note">All formulas below are transcribed directly from the text layer of the four
TE 458 module decks and the Tutorial 1 problem sheet / worked solutions
(<i>TE458_Module1&ndash;4.pdf</i>, <i>TE 458 TUTORIAL 1.pdf</i>, <i>TE458_Tutorial1_Solutions.pdf</i>,
<i>SOLUTION (2).pdf</i>) &mdash; not re-derived or guessed. Each entry cites the source module/page
so you can cross-check against your own copy.</p>

<h3>Module 1 &mdash; Introduction to Network Planning &amp; Optimization</h3>
<p class="note">Module 1 is conceptual only (QoS vs QoE, KPIs, SLAs, CAPEX vs OPEX, planning-vs-optimization
trade-offs). It contains no numeric formulas to extract.</p>

<h3>Module 2 &mdash; Traffic Engineering &amp; Network Dimensioning</h3>

<p class="f">Traffic intensity (the Erlang)</p>
<p class="formula">A = &lambda;h</p>
<p class="vars">A = offered traffic intensity in Erlangs &middot; &lambda; = average arrival rate of calls/sessions &middot; h = average holding time</p>
<p class="use"><b>Use when:</b> converting a call-arrival-rate + average-duration description into an Erlang traffic figure &mdash; the starting point for any Erlang B/C dimensioning problem. 1 Erlang = one resource occupied continuously for the whole observation period.</p>
<p class="src">Source: Module 2, p.7&ndash;8</p>

<p class="f">Erlang B formula (blocking / loss system)</p>
<p class="formula">B(N, A) = (A<sup>N</sup>/N!) &divide; &Sigma;<sub>k=0</sub><sup>N</sup> (A<sup>k</sup>/k!)</p>
<p class="vars">B(N,A) = blocking probability &middot; N = number of circuits/channels/resources &middot; A = offered traffic in Erlangs</p>
<p class="use"><b>Use when:</b> the system has a fixed number of resources and blocked users simply abandon the attempt (no queue) &mdash; e.g. trunk circuits, circuit-switched voice channels, legacy cellular voice capacity. Solve for the smallest N such that B(N,A) &le; the target Grade of Service (e.g. 2%). Worked example in the deck: A=20&nbsp;Erlangs, target 2% blocking &rarr; N=28 channels.</p>
<p class="src">Source: Module 2, p.15, 29&ndash;30</p>

<p class="f">Erlang C formula (delay / queueing system)</p>
<p class="formula">C(N, A) = [(A<sup>N</sup>/N!)&middot;(N/(N&minus;A))] &divide; [&Sigma;<sub>k=0</sub><sup>N&minus;1</sup>(A<sup>k</sup>/k!) + (A<sup>N</sup>/N!)&middot;(N/(N&minus;A))]</p>
<p class="vars">C(N,A) = probability an arriving request has to wait &middot; N = number of servers/resources &middot; A = offered traffic in Erlangs (valid only for A &lt; N)</p>
<p class="use"><b>Use when:</b> arriving requests wait in a queue instead of being blocked &mdash; e.g. call centres, packet-processing systems, shared server pools. Test increasing N until C(N,A) &le; target delay probability.</p>
<p class="src">Source: Module 2, p.18, 32</p>

<h3>Module 3 &mdash; Propagation Modelling &amp; Coverage Design</h3>

<p class="f">EIRP (Effective Isotropic Radiated Power)</p>
<p class="formula">EIRP (dBm) = TX power + antenna gain &minus; body/feeder loss</p>
<p class="use"><b>Use when:</b> establishing the transmit side of any link budget (uplink: mobile is TX; downlink: base station is TX). Use body loss for a handset held against the body; use feeder loss for the base-station side.</p>
<p class="src">Source: Module 3, p.16; Tutorial 1 formula sheet</p>

<p class="f">Receiver sensitivity (direct / non-spread-spectrum form)</p>
<p class="formula">S<sub>i</sub> (dBm) = 30 + E<sub>b</sub>/N<sub>0</sub>(dB) + F(dB) + 10log<sub>10</sub>(kT<sub>0</sub>)(dB) + 10log<sub>10</sub>(W)(dB)</p>
<p class="vars">k = Boltzmann's constant (1.38&times;10<sup>&minus;23</sup> J/K) &middot; T<sub>0</sub> = 290 K reference temperature &middot; F = receiver noise figure &middot; W = detection bandwidth (Hz) &middot; equivalently S<sub>i</sub> = noise floor + E<sub>b</sub>/N<sub>0</sub>, where noise floor = N<sub>0</sub> + 10log<sub>10</sub>(W) + F</p>
<p class="use"><b>Use when:</b> there is <b>no spreading/despreading gain</b> to account for &mdash; i.e. a plain digital link where the required E<sub>b</sub>/N<sub>0</sub> (or SNR) applies directly across the channel bandwidth. This is the form used for the 5G NR downlink/uplink tutorial problems (Problems 1 &amp; 2), <u>not</u> the WCDMA/CDMA problems.</p>
<p class="src">Source: Module 3, p.10&ndash;11, 14&ndash;15; Tutorial 1 Problems 1&ndash;2 &amp; solutions</p>

<p class="f">Thermal noise density, thermal noise power, receiver noise floor</p>
<p class="formula">N<sub>0</sub> (dBm/Hz) = 30 + 10log<sub>10</sub>(kT<sub>0</sub>)<br>
Thermal noise power (dBm) = N<sub>0</sub> + 10log<sub>10</sub>(W)<br>
Receiver noise floor (dBm) = N<sub>0</sub> + 10log<sub>10</sub>(W) + NF</p>
<p class="use"><b>Use when:</b> building up a receiver noise budget from first principles (Boltzmann's constant and temperature) rather than being given a lump "thermal noise density" figure. All three lines chain together: density &rarr; power over bandwidth W &rarr; + noise figure = floor.</p>
<p class="src">Source: Module 3, p.10; Tutorial 1 formula sheet; Tutorial 1 Problem 2 solution</p>

<p class="f">Processing gain (spread-spectrum / CDMA)</p>
<p class="formula">Processing gain (dB) = 10log<sub>10</sub>(M<sub>cps</sub> / R<sub>s</sub>)</p>
<p class="vars">M<sub>cps</sub> = chip rate &middot; R<sub>s</sub> = information/bit rate of the service</p>
<p class="use"><b>Use when:</b> the system is a spread-spectrum/CDMA system (WCDMA/UMTS) &mdash; despreading at the receiver "relaxes" the raw SNR requirement by this amount. Higher service bit rate &rarr; lower processing gain (they move inversely, since M<sub>cps</sub> is fixed for the air interface).</p>
<p class="src">Source: Module 3, p.18; Tutorial 1 formula sheet</p>

<p class="f">Total noise + interference</p>
<p class="formula">Total noise interference (dBm) = Receiver noise power + Interference margin</p>
<p class="use"><b>Use when:</b> the problem gives an explicit interference margin (representing other-user/other-cell interference loading, e.g. "7 dB due to 70% cell loading") to add on top of thermal receiver noise, before computing effective sensitivity.</p>
<p class="src">Source: Module 3, p.18; Tutorial 1 formula sheet</p>

<p class="f">Effective receiver sensitivity (CDMA/WCDMA uplink)</p>
<p class="formula">Without a stated user count:<br>
Rx (dBm) = Total noise+interference &minus; Processing gain + E<sub>b</sub>/N<sub>0</sub><br><br>
With N simultaneously active users stated:<br>
Rx (dBm) = 10log<sub>10</sub>(N) + Total noise+interference &minus; Processing gain + E<sub>b</sub>/N<sub>0</sub></p>
<p class="vars">N = number of simultaneously active users</p>
<p class="use"><b>Use when:</b> computing WCDMA/CDMA uplink effective sensitivity. <b>Critical rule:</b> include the 10log<sub>10</sub>(N) term only when the problem explicitly gives a user count (e.g. "considering 20 users"); omit it if no user count is stated. This is the single most commonly missed term in these problems &mdash; it is a genuine part of the formula, not optional embellishment, whenever N is given.</p>
<p class="src">Source: Module 3, p.18 (defines N term); Tutorial 1 Solutions p.4, 11&ndash;12 (explicit rule + worked contrast between Problem 3 [N given, term included] and Problem 4 [N not given, term omitted])</p>

<p class="f">General link budget (received power)</p>
<p class="formula">P<sub>r</sub> = P<sub>t</sub> + G<sub>t</sub> + G<sub>r</sub> &minus; L<sub>p</sub> &minus; L<sub>misc</sub></p>
<p class="vars">P<sub>r</sub> = received power &middot; P<sub>t</sub> = transmit power &middot; G<sub>t</sub>,G<sub>r</sub> = TX/RX antenna gains &middot; L<sub>p</sub> = propagation path loss &middot; L<sub>misc</sub> = other losses (cable, connector, body, penetration)</p>
<p class="use"><b>Use when:</b> deriving or explaining the conceptual link-budget equation. Coverage exists where P<sub>r</sub> &ge; P<sub>sens</sub> (receiver sensitivity).</p>
<p class="src">Source: Module 3, p.21, 23</p>

<p class="f">Maximum Allowable Path Loss (MAPL) &mdash; general form</p>
<p class="formula">L<sub>p,max</sub> = P<sub>t</sub> + G<sub>t</sub> + G<sub>r</sub> &minus; L<sub>misc</sub> &minus; P<sub>sens</sub></p>
<p class="use"><b>Use when:</b> deriving MAPL conceptually from the general link-budget equation (rearranged so P<sub>r</sub> = P<sub>sens</sub>, the coverage-edge condition).</p>
<p class="src">Source: Module 3, p.24</p>

<p class="f">MAPL &mdash; practical WCDMA/tutorial "master" form</p>
<p class="formula">MAPL = EIRP &minus; Rx/S<sub>i</sub> &minus; (all losses &amp; margins) + (all gains)</p>
<p class="use"><b>Use when:</b> solving an actual worked problem &mdash; this is the template every Tutorial 1 problem plugs into, but which specific losses/margins/gains appear depends on what the question gives you. Only include a term if the problem states it (e.g. Problem 4 gives no base-station antenna gain or feeder loss, so those terms simply don't appear in its MAPL line). Common terms seen across the tutorial: shadow-fading margin, interference margin, fast-fading margin, log-normal fade margin, building penetration loss, base-station antenna gain, feeder/connector loss, soft-handover gain, body loss.</p>
<p class="src">Source: Tutorial 1 formula sheet, p.1; applied in Problems 1&ndash;4 solutions</p>

<p class="f">Free-space path loss (Hz &amp; metres form)</p>
<p class="formula">L<sub>FS</sub> (dB) = 20log<sub>10</sub>(f) + 20log<sub>10</sub>(d) &minus; 147.56</p>
<p class="vars">f = frequency in Hz &middot; d = distance in metres</p>
<p class="use"><b>Use when:</b> f and d are given/converted to Hz and metres respectively. Frequently used at a short reference distance (e.g. d<sub>0</sub>=100 m) as the anchor for a log-distance model.</p>
<p class="src">Source: Module 3, p.30; Tutorial 1 formula sheet</p>

<p class="f">Free-space path loss (MHz &amp; km form)</p>
<p class="formula">L<sub>FS</sub> (dB) = 32.44 + 20log<sub>10</sub>(f<sub>MHz</sub>) + 20log<sub>10</sub>(d<sub>km</sub>)</p>
<p class="vars">f<sub>MHz</sub> = frequency in MHz &middot; d<sub>km</sub> = distance in km</p>
<p class="note">Common pitfall (flagged explicitly in Tutorial 1 Solutions): the two free-space forms use different constants (147.56 vs 32.44) and are <b>only</b> equivalent if you keep the matching unit system (Hz/m vs MHz/km). Do not mix a MHz frequency into the 147.56 formula or vice versa.</p>
<p class="src">Source: Module 3, p.25, 32; Tutorial 1 Solutions p.3</p>

<p class="f">Okumura-Hata model (urban macrocell)</p>
<p class="formula">L<sub>50</sub>(dB) = 69.55 + 26.16log<sub>10</sub>(f) &minus; 13.82log<sub>10</sub>(h<sub>b</sub>) &minus; a(h<sub>m</sub>) + [44.9 &minus; 6.55log<sub>10</sub>(h<sub>b</sub>)]log<sub>10</sub>(d)</p>
<p class="vars">f = frequency in MHz &middot; h<sub>b</sub> = base-station antenna height (m) &middot; h<sub>m</sub> = mobile antenna height (m) &middot; d = distance in km &middot; a(h<sub>m</sub>) = mobile-antenna correction factor</p>
<p class="use"><b>Use when:</b> macrocell coverage planning roughly in the 150&ndash;1500 MHz range, across urban/suburban/rural environments. Gives median path loss, not instantaneous fading. In several tutorial problems, plugging in typical macrocell heights (h<sub>b</sub>&asymp;30 m, h<sub>m</sub>&asymp;1.5 m) at a UMTS-band frequency collapses this to the compact form <span style="font-family:monospace">A + B&middot;log<sub>10</sub>(R)</span> the exam questions often hand you directly (e.g. 137.4 + 35.2log<sub>10</sub>(R)).</p>
<p class="src">Source: Module 3, p.35&ndash;36; Tutorial 1 Solutions p.3, 13</p>

<p class="f">COST-231 Hata model (extends Hata to 1.5&ndash;2 GHz)</p>
<p class="formula">L(dB) = 46.3 + 33.9log<sub>10</sub>(f) &minus; 13.82log<sub>10</sub>(h<sub>b</sub>) &minus; a(h<sub>m</sub>) + [44.9 &minus; 6.55log<sub>10</sub>(h<sub>b</sub>)]log<sub>10</sub>(d) + C</p>
<p class="vars">C = 0 dB for medium-sized cities/suburban areas &middot; C = 3 dB for metropolitan/dense-urban areas</p>
<p class="use"><b>Use when:</b> urban/suburban cellular planning above roughly 1.5 GHz, or whenever the question specifically names "COST-231" / "dense urban" (e.g. Tutorial 1 Problem 4 uses a COST-231 dense-urban variant, PL<sub>max</sub>=137.8+35.4log<sub>10</sub>(R)).</p>
<p class="src">Source: Module 3, p.37; Tutorial 1 Solutions p.3, 13</p>

<p class="f">Mobile-height correction factor a(h<sub>m</sub>)</p>
<p class="formula">a(h<sub>m</sub>) = (1.1log<sub>10</sub>f &minus; 0.7)h<sub>m</sub> &minus; (1.56log<sub>10</sub>f &minus; 0.8)</p>
<p class="use"><b>Use when:</b> you need to actually evaluate a(h<sub>m</sub>) rather than being told it's negligible. In the tutorial's worked example this term came out to &asymp;0.05 dB (negligible) for typical UMTS-band parameters &mdash; don't assume it's always negligible for other frequency/height combinations.</p>
<p class="src">Source: Tutorial 1 Solutions p.13 (medium-city COST-231 correction form)</p>

<p class="f">Log-distance path loss model</p>
<p class="formula">PL(d) = PL(d<sub>0</sub>) + 10n&middot;log<sub>10</sub>(d/d<sub>0</sub>)</p>
<p class="vars">n = path-loss exponent (environment-dependent) &middot; d<sub>0</sub> = reference distance &middot; PL(d<sub>0</sub>) = path loss at the reference distance (often computed via free-space loss)</p>
<p class="use"><b>Use when:</b> the question gives a path-loss exponent n and a reference distance/loss rather than a named empirical model (Okumura-Hata/COST-231) &mdash; e.g. Tutorial 1 Problem 2 uses n=3.5, d<sub>0</sub>=100 m.</p>
<p class="src">Source: Module 3, p.38; Tutorial 1 formula sheet; Problem 2 solution</p>

<p class="f">Log-normal shadowing model</p>
<p class="formula">PL(d) = PL(d<sub>0</sub>) + 10n&middot;log<sub>10</sub>(d/d<sub>0</sub>) + X<sub>&sigma;</sub></p>
<p class="vars">X<sub>&sigma;</sub> = zero-mean Gaussian random variable (shadowing effect, standard deviation &sigma;)</p>
<p class="use"><b>Use when:</b> the log-distance model needs an added random shadowing term for statistical/probabilistic coverage analysis (as opposed to a single deterministic radius).</p>
<p class="src">Source: Module 3, p.38</p>

<p class="f">Coverage area of a hexagonal cell</p>
<p class="formula">A = (3&radic;3/2)&middot;R<sup>2</sup> &asymp; 2.598&middot;R<sup>2</sup></p>
<p class="vars">R = cell radius</p>
<p class="use"><b>Use when:</b> converting a computed cell radius into a coverage area, for hexagonal-cell tessellation assumptions (used throughout Tutorial 1 for area/percentage-change questions).</p>
<p class="src">Source: Tutorial 1 formula sheet, p.1; used in Problems 2 &amp; 4 solutions</p>

<h3>Module 4 &mdash; Access Network Capacity &amp; Interference Planning</h3>

<p class="f">Cell capacity (simplified)</p>
<p class="formula">C<sub>cell</sub> = B&middot;&eta;</p>
<p class="vars">B = available bandwidth &middot; &eta; = spectral efficiency (bits/s/Hz)</p>
<p class="use"><b>Use when:</b> making a first-order capacity estimate from bandwidth and an assumed/average spectral efficiency figure.</p>
<p class="src">Source: Module 4, p.6, 28</p>

<p class="f">Average user throughput</p>
<p class="formula">R<sub>user</sub> &asymp; C<sub>cell</sub> / N<sub>active</sub></p>
<p class="vars">N<sub>active</sub> = number of active users sharing the cell</p>
<p class="use"><b>Use when:</b> estimating a simple per-user share of total cell capacity. Explicitly flagged in the deck as a simplification &mdash; real throughput also depends on SINR, scheduling, mobility and traffic type.</p>
<p class="src">Source: Module 4, p.7</p>

<p class="f">Cluster size (hexagonal reuse)</p>
<p class="formula">N = i<sup>2</sup> + ij + j<sup>2</sup></p>
<p class="vars">i, j = non-negative integers &middot; typical values N = 1, 3, 4, 7, 9, 12, &hellip;</p>
<p class="use"><b>Use when:</b> determining valid cluster sizes for a hexagonal frequency-reuse layout. Smaller N &rarr; more frequent reuse, higher capacity, more interference risk.</p>
<p class="src">Source: Module 4, p.11</p>

<p class="f">Frequency reuse factor</p>
<p class="formula">Reuse factor = 1/N</p>
<p class="use"><b>Use when:</b> expressing what fraction of total channels each cell gets in a cluster of size N. (Some textbooks call N itself the "reuse factor" &mdash; the deck notes this naming inconsistency explicitly.)</p>
<p class="src">Source: Module 4, p.11, 14</p>

<p class="f">Reuse distance</p>
<p class="formula">D = R&radic;(3N)</p>
<p class="vars">D = distance between cells reusing the same frequency group &middot; R = cell radius &middot; N = cluster size</p>
<p class="use"><b>Use when:</b> estimating how far apart co-channel cells must be in a hexagonal layout. Worked example: R=1 km, N=7 &rarr; D=&radic;21&asymp;4.58 km.</p>
<p class="src">Source: Module 4, p.12, 15</p>

<p class="f">Channels per cell / total system channels</p>
<p class="formula">S = kN &nbsp;&nbsp;&hArr;&nbsp;&nbsp; k = S/N</p>
<p class="vars">S = total available channels in the system &middot; N = cluster size &middot; k = channels assigned per cell</p>
<p class="use"><b>Use when:</b> splitting a total channel budget S (e.g. from S = total bandwidth &divide; channel bandwidth) across N cells in a cluster. Worked GSM example: 50 MHz &divide; 200 kHz = 250 channels total; with N=4, k=62.5 channels/cell.</p>
<p class="src">Source: Module 4, p.13, 17&ndash;18</p>

<p class="f">System capacity (multiple clusters)</p>
<p class="formula">C = M&middot;k&middot;N = M&middot;S</p>
<p class="vars">M = number of clusters in the system</p>
<p class="use"><b>Use when:</b> scaling from one cluster's capacity to the full system's capacity across M repeated clusters. Worked example: 7 clusters &times; 4 cells/cluster &times; 500 calls/cell (8 calls/channel &times; 62.5 channels/cell) = 14,000 simultaneous calls.</p>
<p class="src">Source: Module 4, p.14, 19&ndash;20</p>

<p class="f">SINR (Signal-to-Interference-plus-Noise Ratio)</p>
<p class="formula">SINR = S / (I + N) &nbsp;&nbsp;&nbsp; SINR<sub>dB</sub> = 10log<sub>10</sub>(S/(I+N))</p>
<p class="vars">S = desired signal power &middot; I = interference power &middot; N = noise power</p>
<p class="use"><b>Use when:</b> assessing signal <i>quality</i> (not just strength) &mdash; determines achievable modulation/coding scheme and throughput. Coverage (RSRP) alone is not sufficient; a covered user can still have poor SINR.</p>
<p class="src">Source: Module 4, p.24</p>

<p class="f">Spectral efficiency</p>
<p class="formula">&eta; = R / B</p>
<p class="vars">R = data rate &middot; B = bandwidth &middot; &eta; in bits/s/Hz</p>
<p class="use"><b>Use when:</b> quantifying how efficiently a system converts bandwidth into throughput; feeds directly into the C<sub>cell</sub>=B&middot;&eta; capacity estimate.</p>
<p class="src">Source: Module 4, p.26</p>

<p class="f">Shannon capacity (ideal channel capacity)</p>
<p class="formula">C = B&middot;log<sub>2</sub>(1 + SINR)</p>
<p class="vars">SINR here in linear scale (not dB)</p>
<p class="use"><b>Use when:</b> estimating a theoretical upper-bound capacity from bandwidth and SINR. Note the logarithmic (diminishing) return from improving SINR versus the linear return from adding bandwidth.</p>
<p class="src">Source: Module 4, p.27</p>

<p class="f">5G NR subcarrier spacing</p>
<p class="formula">&Delta;f = 2<sup>&mu;</sup> &times; 15 kHz, &nbsp; &mu; = 0, 1, 2, 3, 4</p>
<p class="use"><b>Use when:</b> reasoning about 5G NR numerology, in contrast with LTE's fixed 15 kHz subcarrier spacing.</p>
<p class="src">Source: Module 4, p.33</p>

<h3>Quick-reference: which sensitivity/MAPL form for which system?</h3>
<table>
<tr><th>System type</th><th>Receiver sensitivity form</th><th>MAPL form</th></tr>
<tr><td>5G NR (plain SNR, no spreading)</td><td>S<sub>i</sub> = noise floor + E<sub>b</sub>/N<sub>0</sub></td><td>MAPL = EIRP &minus; S<sub>i</sub> &minus; margins (+ any stated gains)</td></tr>
<tr><td>WCDMA/UMTS (CDMA, no user count given)</td><td>Rx = Total noise+interference &minus; Processing gain + E<sub>b</sub>/N<sub>0</sub></td><td>MAPL = EIRP &minus; Rx &minus; margins + gains</td></tr>
<tr><td>WCDMA/UMTS (CDMA, N users stated)</td><td>Rx = 10log<sub>10</sub>(N) + Total noise+interference &minus; Processing gain + E<sub>b</sub>/N<sub>0</sub></td><td>MAPL = EIRP &minus; Rx &minus; margins + gains</td></tr>
</table>
<p class="note">Always build MAPL from only the terms the specific question actually gives you &mdash; do not assume every margin/gain in the "master" MAPL line applies to every problem.</p>
"""


def render():
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
    render()
