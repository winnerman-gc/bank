#!/usr/bin/env python3
"""
Build a third Tutorial-1-style practice set (Variant C): new numeric
variants of the same 4 problems (5G NR downlink, 5G NR uplink, UMTS
indoor data, WCDMA macro-cell), same pattern as make_tutorial_practice_pdf.py
(Variant B).

Problem 3 in this set deliberately uses a handheld device with a nonzero
body loss (unlike the laptop/data-card case in the original tutorial and
Variant B, where body loss = 0 dB) so the "body loss folded into EIRP"
convention used by Module 3 / Problems 3-4 is visibly exercised, in
contrast with Problem 2 (5G NR uplink), where body loss is instead added
at the MAPL step. See the note under each problem's solution.

Every numeric answer below was computed with a verification script
(not by hand) using the exact same formulas confirmed against the course
Module 3 slides and Tutorial 1 solutions (see make_formula_sheet_pdf.py).

Produces:
  NPAO-Tutorial1-Practice-Questions-C.pdf
  NPAO-Tutorial1-Practice-Solutions-C.pdf

    .venv2/bin/python3 make_tutorial_practice_pdf_c.py
"""
import fitz  # PyMuPDF

CSS = """
body { font-family: sans-serif; color: #14213a; font-size: 10.5px; line-height: 1.35; }
h1 { font-size: 18px; margin: 0 0 2px 0; color: #3730a3; }
h2 { font-size: 11px; margin: 0 0 16px 0; color: #64748b; font-weight: normal; }
h3 { font-size: 14px; margin: 20px 0 8px 0; color: #3730a3; border-top: 1px solid #cbd5e1; padding-top: 12px; }
.q { font-size: 11.5px; font-weight: bold; margin: 14px 0 4px 0; color: #111827; }
.part { margin: 3px 0 3px 16px; }
.note { font-size: 9.5px; color: #9a3412; background: #fff7ed; padding: 4px 6px; margin: 4px 0 8px 0; border-left: 3px solid #fb923c; }
table { border-collapse: collapse; margin: 6px 0 10px 16px; font-size: 9.5px; }
td, th { border: 1px solid #cbd5e1; padding: 3px 8px; }
th { background: #eef2ff; text-align: left; }
.step { margin: 3px 0 3px 16px; font-size: 10px; }
.formula { font-family: monospace; background: #f1f5f9; padding: 3px 6px; margin: 3px 0 3px 16px; font-size: 9.5px; display: block; }
.answer { margin: 3px 0 12px 16px; font-size: 10.5px; color: #15803d; font-weight: bold; }
.sub { margin: 6px 0 6px 16px; }
.given { margin: 4px 0 4px 16px; font-size: 10px; }
.conv { font-size: 9.3px; color: #1d4ed8; background: #eff6ff; padding: 4px 6px; margin: 3px 0 10px 16px; border-left: 3px solid #60a5fa; }
"""

TITLE = "TE 458 &mdash; Coverage Planning: Tutorial 1 Practice Set (Variant C)"
SUBTITLE = "4 more numeric variants of Tutorial 1's problems, same methods, new numbers"

INTRO_NOTE = """
<p class="note">These are freshly parameterised variants of Tutorial 1's four problems &mdash;
same methods and formulas (see the companion Formula Sheet), different input numbers &mdash;
for additional self-test practice. Propagation-model coefficients are given directly in
each question, exactly as they would be handed to you on an exam.</p>
"""

QUESTIONS_BODY = f"""
<h1>{TITLE}</h1>
<h2>{SUBTITLE}</h2>
{INTRO_NOTE}

<p class="q">Problem 1 &mdash; 5G NR Downlink (variant)</p>
<p class="sub">In a 5G NR system operating at 1.8 GHz, the base station transmitter power is 46 dBm,
with a feeder loss of 3 dB and an antenna gain of 15 dBi. For the UE receiver, the noise figure
is 8 dB with a noise floor of &minus;93 dBm, and the required SNR (E<sub>b</sub>/N<sub>0</sub>) for QPSK is 6 dB.</p>
<p class="given">(Boltzmann's constant: k = 1.38&times;10<sup>&minus;23</sup> J/K, T<sub>0</sub> = 290 K.
Additional margins: shadow-fading margin = 6 dB, interference margin = 3 dB.
Propagation model: MAPL = 126.0 + 35.0&nbsp;log<sub>10</sub>(R).)</p>
<p class="part">a. Calculate the EIRP.</p>
<p class="part">b. Calculate the bandwidth.</p>
<p class="part">c. Compute the receiver sensitivity.</p>
<p class="part">d. Including the shadow-fading and interference margins above, find the Maximum Allowable Path Loss for the downlink.</p>
<p class="part">e. Using the given propagation model, determine the cell radius (R).</p>

<p class="q">Problem 2 &mdash; 5G NR Uplink (variant)</p>
<p class="sub">A 5G NR uplink operates at f = 1.8 GHz. The user equipment transmits P<sub>TX</sub> = 125 mW
with antenna gain G<sub>TX</sub> = 0 dBi and no feeder loss. The gNB receiver parameters are:</p>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Receive antenna gain, G<sub>RX</sub></td><td>16 dBi</td></tr>
<tr><td>Receiver-side loss, L<sub>RX</sub></td><td>1 dB</td></tr>
<tr><td>Noise figure, NF</td><td>7 dB</td></tr>
<tr><td>Bandwidth, B</td><td>10 MHz</td></tr>
</table>
<p class="given">To support 16-QAM modulation, the required SNR is 9 dB. Additional losses and margins:
body loss = 2 dB, building penetration loss = 6 dB, fade + interference margin = 9 dB. Assume T<sub>0</sub> = 295 K.</p>
<p class="part">a. Calculate the EIRP.</p>
<p class="part">b. Determine the free-space path loss at a reference distance of 100 m.</p>
<p class="part">c. Assuming T<sub>0</sub> = 295 K, determine: i. thermal noise spectral density; ii. thermal noise power in 10 MHz; iii. receiver noise floor; iv. receiver sensitivity.</p>
<p class="part">d. Compute the maximum allowable path loss (MAPL).</p>
<p class="part">e. Using the log-distance model with n = 3.0 and reference distance d<sub>0</sub> = 100 m, determine: i. the coverage radius; ii. the coverage area assuming a hexagonal cell.</p>
<p class="part">f. State and quantify the effect on coverage area if receiver sensitivity improves by 3 dB.</p>

<p class="q">Problem 3 &mdash; UMTS System Design (variant, handheld device)</p>
<p class="sub">As part of a UMTS system design, the following parameters are given to perform a link budget
analysis for a 32-kbps handheld voice/data service (unlike the laptop data-card case in earlier
problem sets, this device is held against the body, so body loss is nonzero here):</p>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Mobile TX power (dBm)</td><td>23</td></tr>
<tr><td>Antenna gain (dBi)</td><td>1</td></tr>
<tr><td>Body loss (dB)</td><td>2</td></tr>
<tr><td>Thermal noise density (dBm/Hz)</td><td>&minus;174</td></tr>
<tr><td>Receiver noise figure (dB)</td><td>5.5</td></tr>
<tr><td>Interference margin (dB)</td><td>3.5</td></tr>
<tr><td>Required E<sub>b</sub>/N<sub>0</sub> (dB)</td><td>2.5</td></tr>
<tr><td>Base station antenna gain (dBi)</td><td>16</td></tr>
<tr><td>Base station feeder and connector losses (dB)</td><td>2</td></tr>
<tr><td>Fast fading margin (dB)</td><td>4</td></tr>
<tr><td>Log-normal fade margin (dB)</td><td>7</td></tr>
<tr><td>Building penetration loss (dB)</td><td>13</td></tr>
<tr><td>Soft handover gain (dB)</td><td>2</td></tr>
<tr><td>Chip rate, M<sub>cps</sub></td><td>3.84&times;10<sup>6</sup></td></tr>
</table>
<p class="part">a. Perform link budget calculations for the 32 kbps handheld service in the uplink direction, considering 15 users.</p>
<p class="part">b. What is the maximum allowable path loss? (Propagation model: MAPL = 134.0 + 34.5&nbsp;log<sub>10</sub>(R).)</p>
<p class="part">c. What is the coverage radius of the base station?</p>

<p class="q">Problem 4 &mdash; WCDMA Macro-Cell Analysis (variant)</p>
<p class="sub">You are planning the uplink link budget for a WCDMA macro-cell in a dense urban area
supporting a 256 kbps video streaming service. Given:</p>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Mobile transmit power</td><td>22 dBm</td></tr>
<tr><td>Mobile antenna gain</td><td>1.5 dBi</td></tr>
<tr><td>Body loss</td><td>3.5 dB</td></tr>
<tr><td>Base station receiver noise figure</td><td>5.2 dB</td></tr>
<tr><td>Chip rate</td><td>3.84 Mcps</td></tr>
<tr><td>Video service bit rate</td><td>256 kbps</td></tr>
<tr><td>Required E<sub>b</sub>/N<sub>0</sub></td><td>5.2 dB</td></tr>
<tr><td>Thermal noise density</td><td>&minus;174 dBm/Hz</td></tr>
<tr><td>Interference margin (75% cell loading)</td><td>8 dB</td></tr>
<tr><td>Slow fading margin (97% edge coverage probability)</td><td>9.5 dB</td></tr>
<tr><td>Soft handover gain</td><td>+1.8 dB</td></tr>
</table>
<p class="part">a. Compute the following step-by-step, showing all intermediate formulas: i. EIRP; ii. receiver noise power; iii. total noise-plus-interference power; iv. processing gain; v. effective receiver sensitivity; vi. Maximum Allowable Path Loss; vii. cell radius R using the propagation model PL<sub>max</sub> = 136.5 + 35.8&nbsp;log<sub>10</sub>(R).</p>
<p class="part">b. Perform a quantitative impact analysis on the hexagonal cell coverage area A = (3&radic;3/2)R&sup2;:</p>
<p class="part">&nbsp;&nbsp;i. If the service bit rate is increased to 512 kbps (same E<sub>b</sub>/N<sub>0</sub>), calculate the new radius and percentage reduction in coverage area.</p>
<p class="part">&nbsp;&nbsp;ii. If the interference margin rises to 11 dB due to higher network load, determine the new MAPL, radius, and area. Discuss the trade-off with system capacity.</p>
"""

SOLUTIONS_BODY = f"""
<h1>{TITLE} &mdash; Solutions</h1>
<h2>{SUBTITLE}</h2>
{INTRO_NOTE}

<p class="q">Problem 1 &mdash; 5G NR Downlink at 1.8 GHz</p>
<p class="step">(a) EIRP</p>
<p class="formula">EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>TX</sub> = 46 + 15 &minus; 3</p>
<p class="answer">EIRP = 58 dBm</p>

<p class="step">(b) Bandwidth</p>
<p class="formula">Noise floor = N<sub>0</sub> + 10log<sub>10</sub>(W) + NF<br>
10log<sub>10</sub>(W) = &minus;93 &minus; (&minus;173.98) &minus; 8 = 72.98<br>
W = 10<sup>7.298</sup></p>
<p class="answer">W &asymp; 19.85 MHz (&asymp; 20 MHz)</p>

<p class="step">(c) Receiver Sensitivity</p>
<p class="formula">S<sub>i</sub> = Noise floor + E<sub>b</sub>/N<sub>0</sub> = &minus;93 + 6</p>
<p class="answer">S<sub>i</sub> = &minus;87 dBm</p>

<p class="step">(d) Maximum Allowable Path Loss (MAPL)</p>
<p class="formula">MAPL = EIRP &minus; S<sub>i</sub> &minus; M<sub>shadow</sub> &minus; M<sub>interference</sub><br>
MAPL = 58 &minus; (&minus;87) &minus; 6 &minus; 3</p>
<p class="answer">MAPL = 136 dB</p>

<p class="step">(e) Cell Radius</p>
<p class="formula">MAPL = 126.0 + 35.0&nbsp;log<sub>10</sub>(R)<br>
log<sub>10</sub>(R) = (136 &minus; 126.0) / 35.0 = 0.2857</p>
<p class="answer">R = 10<sup>0.2857</sup> &asymp; 1.931 km</p>

<p class="q">Problem 2 &mdash; 5G NR Uplink at 1.8 GHz (Log-Distance Model)</p>
<p class="conv"><b>Body-loss convention:</b> as in the original Tutorial 1 Problem 2, body loss is <u>not</u>
folded into EIRP here &mdash; EIRP only covers TX power, antenna gain and feeder loss (the hardware
between the PA and the antenna). Body loss is a propagation-path loss, so it is added later, at the
MAPL step, alongside building penetration loss. Contrast this with Problem 3 below.</p>
<p class="step">(a) EIRP</p>
<p class="formula">P<sub>TX</sub> = 10log<sub>10</sub>(125) = 20.97 dBm<br>
EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>TX</sub> = 20.97 + 0 &minus; 0</p>
<p class="answer">EIRP &asymp; 20.97 dBm</p>

<p class="step">(b) Free-Space Path Loss at d<sub>0</sub> = 100 m</p>
<p class="formula">PL<sub>0</sub> = 20log<sub>10</sub>(f) + 20log<sub>10</sub>(d) &minus; 147.56<br>
= 20log<sub>10</sub>(1.8&times;10<sup>9</sup>) + 20log<sub>10</sub>(100) &minus; 147.56<br>
= 185.11 + 40.00 &minus; 147.56</p>
<p class="answer">PL<sub>0</sub> &asymp; 77.55 dB</p>

<p class="step">(c) Noise Calculations at T<sub>0</sub> = 295 K</p>
<p class="formula">i. N<sub>0</sub> = 30 + 10log<sub>10</sub>(kT<sub>0</sub>) = 30 + 10log<sub>10</sub>(1.38&times;10<sup>&minus;23</sup>&times;295)</p>
<p class="answer">N<sub>0</sub> &asymp; &minus;173.90 dBm/Hz</p>
<p class="formula">ii. Thermal noise power = N<sub>0</sub> + 10log<sub>10</sub>(B) = &minus;173.90 + 10log<sub>10</sub>(10&times;10<sup>6</sup>) = &minus;173.90 + 70.00</p>
<p class="answer">Thermal noise power &asymp; &minus;103.90 dBm</p>
<p class="formula">iii. Noise floor = Thermal noise power + NF = &minus;103.90 + 7</p>
<p class="answer">Noise floor &asymp; &minus;96.90 dBm</p>
<p class="formula">iv. Receiver sensitivity = Noise floor + required SNR = &minus;96.90 + 9</p>
<p class="answer">Rx sensitivity &asymp; &minus;87.90 dBm</p>

<p class="step">(d) Maximum Allowable Path Loss (MAPL)</p>
<p class="formula">MAPL = EIRP + G<sub>RX</sub> &minus; L<sub>RX</sub> &minus; Rx sensitivity &minus; L<sub>body</sub> &minus; L<sub>bldg</sub> &minus; Margin<br>
= 20.97 + 16 &minus; 1 &minus; (&minus;87.90) &minus; 2 &minus; 6 &minus; 9</p>
<p class="answer">MAPL &asymp; 106.87 dB</p>

<p class="step">(e) Coverage Radius and Area (Log-Distance Model, n = 3.0, d<sub>0</sub> = 100 m)</p>
<p class="formula">PL(d) = PL(d<sub>0</sub>) + 10n&middot;log<sub>10</sub>(d/d<sub>0</sub>)<br>
106.87 = 77.55 + 10(3.0)&middot;log<sub>10</sub>(d/100) = 77.55 + 30&middot;log<sub>10</sub>(d/100)<br>
log<sub>10</sub>(d/100) = (106.87 &minus; 77.55)/30 = 0.9776<br>
d = 100&times;10<sup>0.9776</sup></p>
<p class="answer">i. R &asymp; 949.6 m (&asymp; 0.950 km)</p>
<p class="formula">Area = (3&radic;3/2)R&sup2; = 2.598&times;(0.9496)&sup2;</p>
<p class="answer">ii. Area &asymp; 2.343 km&sup2;</p>

<p class="step">(f) Effect of a 3 dB Improvement in Receiver Sensitivity</p>
<p class="formula">MAPL<sub>new</sub> = 106.87 + 3 = 109.87 dB<br>
log<sub>10</sub>(d/100) = (109.87 &minus; 77.55)/30 = 1.0776 &rArr; d &asymp; 1195.5 m<br>
Area<sub>new</sub> = 2.598&times;(1.1955)&sup2; &asymp; 3.713 km&sup2;</p>
<p class="answer">R<sub>new</sub> &asymp; 1.196 km; coverage area increases by &asymp; 58.5% (from &asymp; 2.343 km&sup2; to &asymp; 3.713 km&sup2;).</p>

<p class="q">Problem 3 &mdash; UMTS Handheld Link Budget (32 kbps, 15 users)</p>
<p class="conv"><b>Body-loss convention:</b> unlike Problem 2 above, this is a WCDMA/UMTS uplink problem, so it
follows Module 3's canonical mobile-uplink EIRP formula (p.16): "EIRP = Mobile TX power + antenna
gain &minus; body loss" &mdash; the same convention Tutorial 1 Problems 3 &amp; 4 use. Body loss is subtracted
directly in the EIRP line, not added later. (In earlier problem sets this device was a laptop data
card with 0 dB body loss, so the subtraction was invisible; here the device is handheld, so it isn't.)</p>
<p class="step">Step 1: Mobile EIRP</p>
<p class="formula">EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>body</sub> = 23 + 1 &minus; 2</p>
<p class="answer">EIRP = 22 dBm</p>

<p class="step">Step 2: Processing Gain</p>
<p class="formula">G<sub>p</sub> = 10log<sub>10</sub>(M<sub>cps</sub>/R<sub>s</sub>) = 10log<sub>10</sub>(3.84&times;10<sup>6</sup> / 32&times;10<sup>3</sup>) = 10log<sub>10</sub>(120)</p>
<p class="answer">G<sub>p</sub> &asymp; 20.79 dB</p>

<p class="step">Step 3: Receiver Noise Power</p>
<p class="formula">RNP = N<sub>0</sub> + 10log<sub>10</sub>(M<sub>cps</sub>) + NF = &minus;174 + 10log<sub>10</sub>(3.84&times;10<sup>6</sup>) + 5.5 = &minus;174 + 65.84 + 5.5</p>
<p class="answer">RNP &asymp; &minus;102.66 dBm</p>

<p class="step">Step 4: Total Noise Interference</p>
<p class="formula">TNI = RNP + Interference margin = &minus;102.66 + 3.5</p>
<p class="answer">TNI &asymp; &minus;99.16 dBm</p>

<p class="step">Step 5: Effective Sensitivity (with N = 15 users)</p>
<p class="formula">Since the problem states "considering 15 users", include the 10log<sub>10</sub>(N) term:<br>
S<sub>e</sub> = 10log<sub>10</sub>(N) + TNI &minus; G<sub>p</sub> + E<sub>b</sub>/N<sub>0</sub><br>
= 10log<sub>10</sub>(15) + (&minus;99.16) &minus; 20.79 + 2.5 = 11.76 &minus; 99.16 &minus; 20.79 + 2.5</p>
<p class="answer">S<sub>e</sub> &asymp; &minus;105.69 dBm</p>

<p class="step">(b) Maximum Allowable Path Loss</p>
<p class="formula">MAPL = EIRP &minus; S<sub>e</sub> + G<sub>BS</sub> &minus; L<sub>feeder</sub> &minus; M<sub>ff</sub> &minus; M<sub>sf</sub> &minus; L<sub>bldg</sub> + G<sub>SHO</sub><br>
= 22 &minus; (&minus;105.69) + 16 &minus; 2 &minus; 4 &minus; 7 &minus; 13 + 2</p>
<p class="answer">MAPL &asymp; 119.69 dB</p>

<p class="step">(c) Coverage Radius</p>
<p class="formula">MAPL = 134.0 + 34.5&nbsp;log<sub>10</sub>(R)<br>
log<sub>10</sub>(R) = (119.69 &minus; 134.0)/34.5 = &minus;0.4148</p>
<p class="answer">R = 10<sup>&minus;0.4148</sup> &asymp; 0.385 km (&asymp; 385 m)</p>

<p class="q">Problem 4 &mdash; WCDMA Uplink: 256 kbps Video in Dense Urban</p>
<p class="step">Part (a) Step-by-Step Link Budget</p>
<p class="formula">i. EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>body</sub> = 22 + 1.5 &minus; 3.5</p>
<p class="answer">EIRP = 20.0 dBm</p>
<p class="formula">ii. Receiver Noise Power<br>
P<sub>N</sub> = N<sub>0</sub> + 10log<sub>10</sub>(M<sub>cps</sub>) + NF = &minus;174 + 10log<sub>10</sub>(3.84&times;10<sup>6</sup>) + 5.2 = &minus;174 + 65.84 + 5.2</p>
<p class="answer">P<sub>N</sub> &asymp; &minus;102.96 dBm</p>
<p class="formula">iii. Total Noise-Plus-Interference Power<br>
I<sub>total</sub> = P<sub>N</sub> + MI = &minus;102.96 + 8</p>
<p class="answer">I<sub>total</sub> &asymp; &minus;94.96 dBm</p>
<p class="formula">iv. Processing Gain<br>
G<sub>p</sub> = 10log<sub>10</sub>(3.84&times;10<sup>6</sup>/256&times;10<sup>3</sup>) = 10log<sub>10</sub>(15)</p>
<p class="answer">G<sub>p</sub> &asymp; 11.76 dB</p>
<p class="formula">v. Effective Receiver Sensitivity (no user count given &rArr; base formula, no 10log<sub>10</sub>(N) term)<br>
S<sub>e</sub> = I<sub>total</sub> + E<sub>b</sub>/N<sub>0</sub> &minus; G<sub>p</sub> = &minus;94.96 + 5.2 &minus; 11.76</p>
<p class="answer">S<sub>e</sub> &asymp; &minus;101.52 dBm</p>
<p class="formula">vi. Maximum Allowable Path Loss<br>
MAPL = EIRP &minus; S<sub>e</sub> &minus; M<sub>sf</sub> + G<sub>SHO</sub> = 20.0 &minus; (&minus;101.52) &minus; 9.5 + 1.8</p>
<p class="answer">MAPL &asymp; 113.82 dB</p>
<p class="formula">vii. Cell Radius (given model PL<sub>max</sub> = 136.5 + 35.8&nbsp;log<sub>10</sub>(R))<br>
log<sub>10</sub>(R) = (113.82 &minus; 136.5)/35.8 = &minus;0.6335</p>
<p class="answer">R &asymp; 0.232 km (&asymp; 232 m)</p>

<p class="step">Part (b) Quantitative Impact Analysis</p>
<p class="formula">Baseline coverage area: A = 2.598&times;(0.232)&sup2; &asymp; 0.140 km&sup2;</p>

<p class="step">(i) Bit Rate Increased to 512 kbps (same E<sub>b</sub>/N<sub>0</sub>)</p>
<p class="formula">New processing gain: G<sub>p</sub>&prime; = 10log<sub>10</sub>(3.84&times;10<sup>6</sup>/512&times;10<sup>3</sup>) = 10log<sub>10</sub>(7.5) &asymp; 8.75 dB<br>
New S<sub>e</sub>&prime; = &minus;94.96 + 5.2 &minus; 8.75 &asymp; &minus;98.51 dBm<br>
New MAPL&prime; = 20.0 &minus; (&minus;98.51) &minus; 9.5 + 1.8 &asymp; 110.81 dB<br>
log<sub>10</sub>(R&prime;) = (110.81 &minus; 136.5)/35.8 = &minus;0.7178 &rArr; R&prime; &asymp; 0.192 km<br>
A&prime; = 2.598&times;(0.192)&sup2; &asymp; 0.0953 km&sup2;</p>
<p class="answer">R&prime; &asymp; 192 m; coverage area shrinks by &asymp; 32.1% (from &asymp; 0.140 km&sup2; to &asymp; 0.0953 km&sup2;).</p>

<p class="step">(ii) Interference Margin Rises to 11 dB (higher network load, bit rate back to 256 kbps)</p>
<p class="formula">New total noise + interference: I&Prime;<sub>total</sub> = &minus;102.96 + 11 = &minus;91.96 dBm<br>
Processing gain unchanged: 11.76 dB<br>
New S<sub>e</sub>&Prime; = &minus;91.96 + 5.2 &minus; 11.76 &asymp; &minus;98.52 dBm<br>
New MAPL&Prime; = 20.0 &minus; (&minus;98.52) &minus; 9.5 + 1.8 &asymp; 110.82 dB<br>
log<sub>10</sub>(R&Prime;) = (110.82 &minus; 136.5)/35.8 = &minus;0.7175 &rArr; R&Prime; &asymp; 0.192 km<br>
A&Prime; = 2.598&times;(0.192)&sup2; &asymp; 0.0955 km&sup2;</p>
<p class="answer">R&Prime; &asymp; 192 m; coverage area shrinks by &asymp; 32.0% (from &asymp; 0.140 km&sup2; to &asymp; 0.0955 km&sup2;).</p>

<p class="step">Trade-off Discussion</p>
<p class="sub">As in the earlier problem sets, both changes remove almost exactly the same amount (&asymp;3 dB)
from the link budget and produce almost identical area shrinkage (&asymp;32%). This is "cell breathing":
loading a CDMA cell with more traffic or higher bit rates shrinks its effective radius, because the
added interference (or added bit-rate demand) eats directly into the same link margin that otherwise
buys coverage distance.</p>
"""


def render(body_html, out_path):
    story = fitz.Story(html="<body>" + body_html + "</body>", user_css=CSS)
    writer = fitz.DocumentWriter(out_path)
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
    print(f"Wrote {out_path}: {pages} pages")


def main():
    render(QUESTIONS_BODY, "NPAO-Tutorial1-Practice-Questions-C.pdf")
    render(SOLUTIONS_BODY, "NPAO-Tutorial1-Practice-Solutions-C.pdf")


if __name__ == "__main__":
    main()
