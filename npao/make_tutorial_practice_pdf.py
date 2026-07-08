#!/usr/bin/env python3
"""
Build a second Tutorial-1-style practice set (new numeric variants of the
same 4 problems: 5G NR downlink, 5G NR uplink, UMTS indoor data, WCDMA
macro-cell), mirroring the pattern already used for
TE458_Tutorial1_Problem1_Variant.pdf but covering all four problems, with
solutions written in the concise step-by-step style of "SOLUTION (2).pdf"
(formula -> substitution -> boxed answer, minimal prose) rather than the
long teaching-guide style of TE458_Tutorial1_Solutions.pdf.

Every numeric answer below was computed with a verification script
(not by hand) using the exact same formulas confirmed against the course
Module 3 slides and Tutorial 1 solutions (see make_formula_sheet_pdf.py).

Produces:
  NPAO-Tutorial1-Practice-Questions.pdf
  NPAO-Tutorial1-Practice-Solutions.pdf

    .venv2/bin/python3 make_tutorial_practice_pdf.py
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
"""

TITLE = "TE 458 &mdash; Coverage Planning: Tutorial 1 Practice Set (Variant B)"
SUBTITLE = "4 new numeric variants of Tutorial 1's problems (5G NR downlink/uplink, UMTS indoor, WCDMA macro-cell), same methods, new numbers"

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
<p class="sub">In a 5G NR system operating at 2.1 GHz, the base station transmitter power is 44 dBm,
with a feeder loss of 2.5 dB and an antenna gain of 17 dBi. For the UE receiver, the noise figure
is 7 dB with a noise floor of &minus;95 dBm, and the required SNR (E<sub>b</sub>/N<sub>0</sub>) for 16-QAM is 11 dB.</p>
<p class="given">(Boltzmann's constant: k = 1.38&times;10<sup>&minus;23</sup> J/K, T<sub>0</sub> = 290 K.
Additional margins: shadow-fading margin = 8 dB, interference margin = 4 dB.
Propagation model: MAPL = 132.4 + 37.2&nbsp;log<sub>10</sub>(R).)</p>
<p class="part">a. Calculate the EIRP.</p>
<p class="part">b. Calculate the bandwidth.</p>
<p class="part">c. Compute the receiver sensitivity.</p>
<p class="part">d. Including the shadow-fading and interference margins above, find the Maximum Allowable Path Loss for the downlink.</p>
<p class="part">e. Using the given propagation model, determine the cell radius (R).</p>

<p class="q">Problem 2 &mdash; 5G NR Uplink (variant)</p>
<p class="sub">A 5G NR uplink operates at f = 2.1 GHz. The user equipment transmits P<sub>TX</sub> = 100 mW
with antenna gain G<sub>TX</sub> = 0 dBi and no feeder loss. The gNB receiver parameters are:</p>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Receive antenna gain, G<sub>RX</sub></td><td>15 dBi</td></tr>
<tr><td>Receiver-side loss, L<sub>RX</sub></td><td>1.5 dB</td></tr>
<tr><td>Noise figure, NF</td><td>6.5 dB</td></tr>
<tr><td>Bandwidth, B</td><td>15 MHz</td></tr>
</table>
<p class="given">To support 64-QAM modulation, the required SNR is 15 dB. Additional losses and margins:
body loss = 3 dB, building penetration loss = 8 dB, fade + interference margin = 10 dB. Assume T<sub>0</sub> = 300 K.</p>
<p class="part">a. Calculate the EIRP.</p>
<p class="part">b. Determine the free-space path loss at a reference distance of 100 m.</p>
<p class="part">c. Assuming T<sub>0</sub> = 300 K, determine: i. thermal noise spectral density; ii. thermal noise power in 15 MHz; iii. receiver noise floor; iv. receiver sensitivity.</p>
<p class="part">d. Compute the maximum allowable path loss (MAPL).</p>
<p class="part">e. Using the log-distance model with n = 3.2 and reference distance d<sub>0</sub> = 100 m, determine: i. the coverage radius; ii. the coverage area assuming a hexagonal cell.</p>
<p class="part">f. State and quantify the effect on coverage area if receiver sensitivity improves by 4 dB.</p>

<p class="q">Problem 3 &mdash; UMTS System Design (variant)</p>
<p class="sub">As part of a UMTS system design, the following parameters are given to perform a link budget
analysis for a 64-kbps indoor data service:</p>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Mobile TX power (dBm)</td><td>21</td></tr>
<tr><td>Antenna gain (dBi)</td><td>0</td></tr>
<tr><td>Body loss (dB)</td><td>0</td></tr>
<tr><td>Thermal noise density (dBm/Hz)</td><td>&minus;174</td></tr>
<tr><td>Receiver noise figure (dB)</td><td>6</td></tr>
<tr><td>Interference margin (dB)</td><td>3</td></tr>
<tr><td>Required E<sub>b</sub>/N<sub>0</sub> (dB)</td><td>3</td></tr>
<tr><td>Base station antenna gain (dBi)</td><td>17</td></tr>
<tr><td>Base station feeder and connector losses (dB)</td><td>2.5</td></tr>
<tr><td>Fast fading margin (dB)</td><td>5</td></tr>
<tr><td>Log-normal fade margin (dB)</td><td>8</td></tr>
<tr><td>Building penetration loss (dB)</td><td>12</td></tr>
<tr><td>Soft handover gain (dB)</td><td>2.5</td></tr>
<tr><td>Chip rate, M<sub>cps</sub></td><td>3.84&times;10<sup>6</sup></td></tr>
</table>
<p class="part">a. Perform link budget calculations for the 64 kbps indoor data service in the uplink direction for a laptop, considering 12 users.</p>
<p class="part">b. What is the maximum allowable path loss? (Propagation model: MAPL = 137.4 + 35.2&nbsp;log<sub>10</sub>(R).)</p>
<p class="part">c. What is the coverage radius of the base station?</p>

<p class="q">Problem 4 &mdash; WCDMA Macro-Cell Analysis (variant)</p>
<p class="sub">You are planning the uplink link budget for a WCDMA macro-cell in a dense urban area
supporting a 144 kbps video streaming service. Given:</p>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Mobile transmit power</td><td>24 dBm</td></tr>
<tr><td>Mobile antenna gain</td><td>1 dBi</td></tr>
<tr><td>Body loss</td><td>3 dB</td></tr>
<tr><td>Base station receiver noise figure</td><td>5 dB</td></tr>
<tr><td>Chip rate</td><td>3.84 Mcps</td></tr>
<tr><td>Video service bit rate</td><td>144 kbps</td></tr>
<tr><td>Required E<sub>b</sub>/N<sub>0</sub></td><td>5 dB</td></tr>
<tr><td>Thermal noise density</td><td>&minus;174 dBm/Hz</td></tr>
<tr><td>Interference margin (60% cell loading)</td><td>6 dB</td></tr>
<tr><td>Slow fading margin (90% edge coverage probability)</td><td>8 dB</td></tr>
<tr><td>Soft handover gain</td><td>+2 dB</td></tr>
</table>
<p class="part">a. Compute the following step-by-step, showing all intermediate formulas: i. EIRP; ii. receiver noise power; iii. total noise-plus-interference power; iv. processing gain; v. effective receiver sensitivity; vi. Maximum Allowable Path Loss; vii. cell radius R using the propagation model PL<sub>max</sub> = 135.0 + 36.0&nbsp;log<sub>10</sub>(R).</p>
<p class="part">b. Perform a quantitative impact analysis on the hexagonal cell coverage area A = (3&radic;3/2)R&sup2;:</p>
<p class="part">&nbsp;&nbsp;i. If the service bit rate is increased to 288 kbps (same E<sub>b</sub>/N<sub>0</sub>), calculate the new radius and percentage reduction in coverage area.</p>
<p class="part">&nbsp;&nbsp;ii. If the interference margin rises to 9 dB due to higher network load, determine the new MAPL, radius, and area. Discuss the trade-off with system capacity.</p>
"""

SOLUTIONS_BODY = f"""
<h1>{TITLE} &mdash; Solutions</h1>
<h2>{SUBTITLE}</h2>
{INTRO_NOTE}

<p class="q">Problem 1 &mdash; 5G NR Downlink at 2.1 GHz</p>
<p class="step">(a) EIRP</p>
<p class="formula">EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>TX</sub> = 44 + 17 &minus; 2.5</p>
<p class="answer">EIRP = 58.5 dBm</p>

<p class="step">(b) Bandwidth</p>
<p class="formula">Noise floor = N<sub>0</sub> + 10log<sub>10</sub>(W) + NF<br>
10log<sub>10</sub>(W) = &minus;95 &minus; (&minus;173.98) &minus; 7 = 71.98<br>
W = 10<sup>7.198</sup></p>
<p class="answer">W &asymp; 15.8 MHz</p>

<p class="step">(c) Receiver Sensitivity</p>
<p class="formula">S<sub>i</sub> = Noise floor + E<sub>b</sub>/N<sub>0</sub> = &minus;95 + 11</p>
<p class="answer">S<sub>i</sub> = &minus;84 dBm</p>

<p class="step">(d) Maximum Allowable Path Loss (MAPL)</p>
<p class="formula">MAPL = EIRP &minus; S<sub>i</sub> &minus; M<sub>shadow</sub> &minus; M<sub>interference</sub><br>
MAPL = 58.5 &minus; (&minus;84) &minus; 8 &minus; 4</p>
<p class="answer">MAPL = 130.5 dB</p>

<p class="step">(e) Cell Radius</p>
<p class="formula">MAPL = 132.4 + 37.2&nbsp;log<sub>10</sub>(R)<br>
log<sub>10</sub>(R) = (130.5 &minus; 132.4) / 37.2 = &minus;0.0511</p>
<p class="answer">R = 10<sup>&minus;0.0511</sup> &asymp; 0.889 km (&asymp; 889 m)</p>

<p class="q">Problem 2 &mdash; 5G NR Uplink at 2.1 GHz (Log-Distance Model)</p>
<p class="step">(a) EIRP</p>
<p class="formula">P<sub>TX</sub> = 10log<sub>10</sub>(100) = 20.0 dBm<br>
EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>TX</sub> = 20.0 + 0 &minus; 0</p>
<p class="answer">EIRP = 20.0 dBm</p>

<p class="step">(b) Free-Space Path Loss at d<sub>0</sub> = 100 m</p>
<p class="formula">PL<sub>0</sub> = 20log<sub>10</sub>(f) + 20log<sub>10</sub>(d) &minus; 147.56<br>
= 20log<sub>10</sub>(2.1&times;10<sup>9</sup>) + 20log<sub>10</sub>(100) &minus; 147.56<br>
= 186.44 + 40.00 &minus; 147.56</p>
<p class="answer">PL<sub>0</sub> &asymp; 78.88 dB</p>

<p class="step">(c) Noise Calculations at T<sub>0</sub> = 300 K</p>
<p class="formula">i. N<sub>0</sub> = 30 + 10log<sub>10</sub>(kT<sub>0</sub>) = 30 + 10log<sub>10</sub>(1.38&times;10<sup>&minus;23</sup>&times;300)</p>
<p class="answer">N<sub>0</sub> &asymp; &minus;173.83 dBm/Hz</p>
<p class="formula">ii. Thermal noise power = N<sub>0</sub> + 10log<sub>10</sub>(B) = &minus;173.83 + 10log<sub>10</sub>(15&times;10<sup>6</sup>) = &minus;173.83 + 71.76</p>
<p class="answer">Thermal noise power &asymp; &minus;102.07 dBm</p>
<p class="formula">iii. Noise floor = Thermal noise power + NF = &minus;102.07 + 6.5</p>
<p class="answer">Noise floor &asymp; &minus;95.57 dBm</p>
<p class="formula">iv. Receiver sensitivity = Noise floor + required SNR = &minus;95.57 + 15</p>
<p class="answer">Rx sensitivity &asymp; &minus;80.57 dBm</p>

<p class="step">(d) Maximum Allowable Path Loss (MAPL)</p>
<p class="formula">MAPL = EIRP + G<sub>RX</sub> &minus; L<sub>RX</sub> &minus; Rx sensitivity &minus; L<sub>body</sub> &minus; L<sub>bldg</sub> &minus; Margin<br>
= 20.0 + 15 &minus; 1.5 &minus; (&minus;80.57) &minus; 3 &minus; 8 &minus; 10</p>
<p class="answer">MAPL &asymp; 93.07 dB</p>

<p class="step">(e) Coverage Radius and Area (Log-Distance Model, n = 3.2, d<sub>0</sub> = 100 m)</p>
<p class="formula">PL(d) = PL(d<sub>0</sub>) + 10n&middot;log<sub>10</sub>(d/d<sub>0</sub>)<br>
93.07 = 78.88 + 10(3.2)&middot;log<sub>10</sub>(d/100) = 78.88 + 32&middot;log<sub>10</sub>(d/100)<br>
log<sub>10</sub>(d/100) = (93.07 &minus; 78.88)/32 = 0.4433<br>
d = 100&times;10<sup>0.4433</sup></p>
<p class="answer">i. R &asymp; 277.5 m (&asymp; 0.278 km)</p>
<p class="formula">Area = (3&radic;3/2)R&sup2; = 2.598&times;(0.2775)&sup2;</p>
<p class="answer">ii. Area &asymp; 0.200 km&sup2;</p>

<p class="step">(f) Effect of a 4 dB Improvement in Receiver Sensitivity</p>
<p class="formula">A 4 dB more sensitive receiver tolerates 4 dB more path loss for the same transmit conditions:<br>
MAPL<sub>new</sub> = 93.07 + 4 = 97.07 dB<br>
log<sub>10</sub>(d/100) = (97.07 &minus; 78.88)/32 = 0.5683 &rArr; d &asymp; 370.1 m<br>
Area<sub>new</sub> = 2.598&times;(0.3701)&sup2; &asymp; 0.356 km&sup2;</p>
<p class="answer">R<sub>new</sub> &asymp; 0.370 km; coverage area increases by &asymp; 77.8% (from &asymp; 0.200 km&sup2; to &asymp; 0.356 km&sup2;).</p>

<p class="q">Problem 3 &mdash; UMTS Indoor Link Budget (64 kbps, 12 users)</p>
<p class="step">Step 1: Processing Gain</p>
<p class="formula">G<sub>p</sub> = 10log<sub>10</sub>(M<sub>cps</sub>/R<sub>s</sub>) = 10log<sub>10</sub>(3.84&times;10<sup>6</sup> / 64&times;10<sup>3</sup>) = 10log<sub>10</sub>(60)</p>
<p class="answer">G<sub>p</sub> &asymp; 17.78 dB</p>

<p class="step">Step 2: Receiver Noise Power</p>
<p class="formula">RNP = N<sub>0</sub> + 10log<sub>10</sub>(M<sub>cps</sub>) + NF = &minus;174 + 10log<sub>10</sub>(3.84&times;10<sup>6</sup>) + 6 = &minus;174 + 65.84 + 6</p>
<p class="answer">RNP &asymp; &minus;102.16 dBm</p>

<p class="step">Step 3: Total Noise Interference</p>
<p class="formula">TNI = RNP + Interference margin = &minus;102.16 + 3</p>
<p class="answer">TNI &asymp; &minus;99.16 dBm</p>

<p class="step">Step 4: Effective Sensitivity (with N = 12 users)</p>
<p class="formula">Since the problem states "considering 12 users", include the 10log<sub>10</sub>(N) term:<br>
S<sub>e</sub> = 10log<sub>10</sub>(N) + TNI &minus; G<sub>p</sub> + E<sub>b</sub>/N<sub>0</sub><br>
= 10log<sub>10</sub>(12) + (&minus;99.16) &minus; 17.78 + 3 = 10.79 &minus; 99.16 &minus; 17.78 + 3</p>
<p class="answer">S<sub>e</sub> &asymp; &minus;103.15 dBm</p>

<p class="step">Step 5: Mobile EIRP</p>
<p class="formula">EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>body</sub> = 21 + 0 &minus; 0</p>
<p class="answer">EIRP = 21 dBm</p>

<p class="step">(b) Maximum Allowable Path Loss</p>
<p class="formula">MAPL = EIRP &minus; S<sub>e</sub> + G<sub>BS</sub> &minus; L<sub>feeder</sub> &minus; M<sub>ff</sub> &minus; M<sub>sf</sub> &minus; L<sub>bldg</sub> + G<sub>SHO</sub><br>
= 21 &minus; (&minus;103.15) + 17 &minus; 2.5 &minus; 5 &minus; 8 &minus; 12 + 2.5</p>
<p class="answer">MAPL &asymp; 116.15 dB</p>

<p class="step">(c) Coverage Radius</p>
<p class="formula">MAPL = 137.4 + 35.2&nbsp;log<sub>10</sub>(R)<br>
log<sub>10</sub>(R) = (116.15 &minus; 137.4)/35.2 = &minus;0.6037</p>
<p class="answer">R = 10<sup>&minus;0.6037</sup> &asymp; 0.249 km (&asymp; 249 m)</p>

<p class="q">Problem 4 &mdash; WCDMA Uplink: 144 kbps Video in Dense Urban</p>
<p class="step">Part (a) Step-by-Step Link Budget</p>
<p class="formula">i. EIRP = P<sub>TX</sub> + G<sub>TX</sub> &minus; L<sub>body</sub> = 24 + 1 &minus; 3</p>
<p class="answer">EIRP = 22 dBm</p>
<p class="formula">ii. Receiver Noise Power<br>
P<sub>N</sub> = N<sub>0</sub> + 10log<sub>10</sub>(M<sub>cps</sub>) + NF = &minus;174 + 10log<sub>10</sub>(3.84&times;10<sup>6</sup>) + 5 = &minus;174 + 65.84 + 5</p>
<p class="answer">P<sub>N</sub> &asymp; &minus;103.16 dBm</p>
<p class="formula">iii. Total Noise-Plus-Interference Power<br>
I<sub>total</sub> = P<sub>N</sub> + MI = &minus;103.16 + 6</p>
<p class="answer">I<sub>total</sub> &asymp; &minus;97.16 dBm</p>
<p class="formula">iv. Processing Gain<br>
G<sub>p</sub> = 10log<sub>10</sub>(3.84&times;10<sup>6</sup>/144&times;10<sup>3</sup>) = 10log<sub>10</sub>(26.67)</p>
<p class="answer">G<sub>p</sub> &asymp; 14.26 dB</p>
<p class="formula">v. Effective Receiver Sensitivity (no user count given &rArr; base formula, no 10log<sub>10</sub>(N) term)<br>
S<sub>e</sub> = I<sub>total</sub> + E<sub>b</sub>/N<sub>0</sub> &minus; G<sub>p</sub> = &minus;97.16 + 5 &minus; 14.26</p>
<p class="answer">S<sub>e</sub> &asymp; &minus;106.42 dBm</p>
<p class="formula">vi. Maximum Allowable Path Loss<br>
MAPL = EIRP &minus; S<sub>e</sub> &minus; M<sub>sf</sub> + G<sub>SHO</sub> = 22 &minus; (&minus;106.42) &minus; 8 + 2</p>
<p class="answer">MAPL &asymp; 122.42 dB</p>
<p class="formula">vii. Cell Radius (given model PL<sub>max</sub> = 135.0 + 36.0&nbsp;log<sub>10</sub>(R))<br>
log<sub>10</sub>(R) = (122.42 &minus; 135.0)/36.0 = &minus;0.3494</p>
<p class="answer">R &asymp; 0.447 km (&asymp; 447 m)</p>

<p class="step">Part (b) Quantitative Impact Analysis</p>
<p class="formula">Baseline coverage area: A = 2.598&times;(0.447)&sup2; &asymp; 0.519 km&sup2;</p>

<p class="step">(i) Bit Rate Increased to 288 kbps (same E<sub>b</sub>/N<sub>0</sub>)</p>
<p class="formula">New processing gain: G<sub>p</sub>&prime; = 10log<sub>10</sub>(3.84&times;10<sup>6</sup>/288&times;10<sup>3</sup>) = 10log<sub>10</sub>(13.33) &asymp; 11.25 dB<br>
New S<sub>e</sub>&prime; = &minus;97.16 + 5 &minus; 11.25 &asymp; &minus;103.41 dBm<br>
New MAPL&prime; = 22 &minus; (&minus;103.41) &minus; 8 + 2 &asymp; 119.41 dB<br>
log<sub>10</sub>(R&prime;) = (119.41 &minus; 135.0)/36.0 = &minus;0.4331 &rArr; R&prime; &asymp; 0.369 km<br>
A&prime; = 2.598&times;(0.369)&sup2; &asymp; 0.353 km&sup2;</p>
<p class="answer">R&prime; &asymp; 369 m; coverage area shrinks by &asymp; 32.0% (from &asymp; 0.519 km&sup2; to &asymp; 0.353 km&sup2;).</p>

<p class="step">(ii) Interference Margin Rises to 9 dB (higher network load, bit rate back to 144 kbps)</p>
<p class="formula">New total noise + interference: I&Prime;<sub>total</sub> = &minus;103.16 + 9 = &minus;94.16 dBm<br>
Processing gain unchanged: 14.26 dB<br>
New S<sub>e</sub>&Prime; = &minus;94.16 + 5 &minus; 14.26 &asymp; &minus;103.42 dBm<br>
New MAPL&Prime; = 22 &minus; (&minus;103.42) &minus; 8 + 2 &asymp; 119.42 dB<br>
log<sub>10</sub>(R&Prime;) = (119.42 &minus; 135.0)/36.0 = &minus;0.4328 &rArr; R&Prime; &asymp; 0.369 km<br>
A&Prime; = 2.598&times;(0.369)&sup2; &asymp; 0.354 km&sup2;</p>
<p class="answer">R&Prime; &asymp; 369 m; coverage area shrinks by &asymp; 31.9% (from &asymp; 0.519 km&sup2; to &asymp; 0.354 km&sup2;).</p>

<p class="step">Trade-off Discussion</p>
<p class="sub">Both changes remove almost exactly the same amount (&asymp;3 dB) from the link budget &mdash; one because a
higher bit rate needs a smaller processing gain, the other because more interference directly raises the
noise floor &mdash; and both shrink the coverage radius by &asymp;17% and the coverage area by &asymp;32%. This is
"cell breathing": loading a CDMA cell with more traffic or higher bit rates shrinks its effective radius,
because the added interference (or added bit-rate demand) eats directly into the same link margin that
otherwise buys coverage distance. A site sized for coverage at light load can develop coverage holes at its
edge once load or throughput demand rises.</p>
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
    render(QUESTIONS_BODY, "NPAO-Tutorial1-Practice-Questions.pdf")
    render(SOLUTIONS_BODY, "NPAO-Tutorial1-Practice-Solutions.pdf")


if __name__ == "__main__":
    main()
