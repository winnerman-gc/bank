#!/usr/bin/env python3
"""
Build a compact quick-reference PDF covering every slide deck in this folder
(TE 454 Lectures 1-3): definitions, formulas and properties, condensed for
revision rather than reproducing slide-by-slide.

Uses PyMuPDF's Story API for automatic multi-page text reflow.
    pip install pymupdf
    python3 make_reference_pdf.py
"""
import fitz  # PyMuPDF

OUT = "TE454-Digital-Signal-Processing-Quick-Reference.pdf"
TITLE = "TE 454 &middot; Digital Signal Processing"
SUBTITLE = "Compact Quick Reference &mdash; Lectures 1-3 (Introduction, Continuous-Time, Discrete-Time)"

CSS = """
body { font-family: sans-serif; color: #14213a; }
.title { font-size: 18px; margin: 0 0 2px 0; color: #115e59; font-weight: bold; }
.subtitle { font-size: 9.5px; margin: 0 0 10px 0; color: #64748b; }
.lec { font-size: 12.5px; font-weight: bold; color: #ffffff; background-color: #115e59;
       padding: 4px 7px; margin: 14px 0 7px 0; page-break-inside: avoid; page-break-after: avoid;
       page-break-before: always; }
.lec.first { page-break-before: avoid; }
.h { font-size: 10.5px; font-weight: bold; color: #115e59; margin: 8px 0 2px 0;
     border-bottom: 1px solid #cbd5e1; padding-bottom: 1px; page-break-inside: avoid; }
.p { font-size: 8.4px; line-height: 1.35; margin: 2px 0; color: #1f2937; }
.li { font-size: 8.4px; line-height: 1.32; margin: 1px 0 1px 0; color: #1f2937; }
.note { font-size: 7.7px; line-height: 1.3; margin: 1px 0 2px 14px; color: #64748b; font-style: italic; }
.eq { font-size: 9px; line-height: 1.4; margin: 3px 0 3px 8px; color: #0f766e; font-weight: bold; }
.rows { margin: 3px 0 8px 0; }
.rowhd { font-size: 7.7px; font-weight: bold; color: #ffffff; background-color: #475569;
         padding: 2px 5px; margin: 0; }
.row { font-size: 8.2px; line-height: 1.32; color: #1f2937; margin: 0; padding: 2px 5px;
       border-bottom: 0.5px solid #dbe2ea; }
.row .lbl { color: #0f766e; font-weight: bold; }
"""

# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------


def sec(title, first=False):
    cls = "lec first" if first else "lec"
    return f'<p class="{cls}">{title}</p>'


def h(title):
    return f'<p class="h">{title}</p>'


def p(text):
    return f'<p class="p">{text}</p>'


def note(text):
    return f'<p class="note">{text}</p>'


def eq(text):
    return f'<p class="eq">{text}</p>'


def ul(items):
    lis = "".join(f'<li class="li">{i}</li>' for i in items)
    return f"<ul>{lis}</ul>"


def table(headers, rows, widths=None):
    # Rendered as bordered label/description rows rather than an HTML <table>,
    # since PyMuPDF's Story engine mis-paints a stray header-colored band when
    # a real <table> is immediately preceded by a heading + paragraph.
    head_label = " &middot; ".join(headers[:-1])
    out = ['<div class="rows">', f'<p class="rowhd">{head_label} &mdash; {headers[-1]}</p>']
    for r in rows:
        label = ". ".join(str(c) for c in r[:-1])
        out.append(f'<p class="row"><span class="lbl">{label}.</span> {r[-1]}</p>')
    out.append("</div>")
    return "".join(out)


def build_html():
    parts = [f'<p class="title">{TITLE}</p>', f'<p class="subtitle">{SUBTITLE}</p>']

    # =====================================================================
    # LECTURE 1 - INTRODUCTION TO DSP
    # =====================================================================
    parts.append(sec("Lecture 1 &middot; Introduction to Digital Signal Processing", first=True))

    parts.append(h("1.1 What is DSP?"))
    parts.append(p(
        "<b>Digital Signal Processing</b>: theories, methods and algorithms for processing "
        "signals in digital form. <b>Digital Signal Processor</b>: a microprocessor built to "
        "run DSP algorithms (architecture: chips, peripherals, pipelines, instructions; plus "
        "hardware &amp; software system design)."
    ))
    parts.append(p(
        "<b>Analog</b> signal &rarr; continuous in both time and magnitude. "
        "<b>Digital</b> signal &rarr; discrete in both time and magnitude. Most real-world "
        "signals are analog, so DSP needs a conversion: "
        "<b>Step 1 &ndash; Sample</b> the analog signal at discrete time points; "
        "<b>Step 2 &ndash; Quantize</b> the sample values (by rounding or truncation)."
    ))
    parts.append(p(
        "Why DSP matters: digitization is the foundation of information technology, and DSP "
        "is the kernel of digitization. Most real-time DSP is implemented on DSP processors "
        "or DSP-core ASICs &mdash; a key driver of the whole semiconductor industry."
    ))

    parts.append(h("1.2 Digital vs Analog Signal Processing"))
    parts.append(p(
        "<b>Advantages of digital over analog:</b> more reliable / less sensitive to "
        "component tolerances (temperature, noise, ageing); higher accuracy; can be "
        "integrated on a single chip. <b>Limitation:</b> A/D and D/A conversion rates are "
        "not available at every extreme &mdash; beyond ~GHz, or below a few Hz, converters "
        "become impractical."
    ))
    parts.append(table(
        ["#", "Why Digital?", "Explanation"],
        [
            ["1", "Programmability", "Analog systems need a hardware redesign to change behaviour; digital systems only need new software (e.g. adaptive filters)."],
            ["2", "Precision", "Analog precision is set by component spec (resistors &plusmn;5%, capacitors &plusmn;20% or worse); digital precision is set by ADC bit-depth, word length and the algorithm."],
            ["3", "Stability", "Analog components (R, C, op-amps) drift with temperature/humidity; digital systems show no variation over their guaranteed operating range."],
            ["4", "Anti-noise", "Digital signals tolerate noise far better since only two logic levels must be distinguished."],
            ["5", "Repeatability", "Two digital implementations of the same design behave identically; two analog builds (component variation) do not."],
            ["6", "VLSI", "Digital algorithms map efficiently onto very-large-scale integrated circuits."],
            ["7", "Error-correcting codes", "Digital/binary data can carry redundant bits so transmission/storage errors are detected and corrected."],
            ["8", "Data transmission &amp; storage", "Digital media (Internet, CD, DVD) give far higher fidelity than analog storage/transmission."],
            ["9", "Data compression", "Digital techniques allow lossless compression; analog compression (e.g. 3 kHz-limited telephone lines) always loses information."],
        ],
    ))

    parts.append(h("1.3 We Still Need Analog Processing"))
    parts.append(ul([
        "<b>Real-time processing</b>: analog processing time is only the circuit delay; digital processing time depends on processor speed and algorithm &mdash; harder to guarantee true real time.",
        "<b>Very high frequency signals</b>: analog circuits can process microwave/mm-wave/light-wave signals directly; by the Nyquist rule, digital processing is capped by sample-and-hold and A/D speed, and very-high-rate ADCs are expensive.",
        "<b>Most real-world signals are analog</b>: to process them digitally they must first be converted via mixed-signal (analog + digital) processing.",
    ]))

    parts.append(h("1.4 Applications of DSP"))
    parts.append(table(
        ["Area", "Examples"],
        [
            ["Communication", "Wireless comms (base stations, switching centres, mobile phones); GSM cell-phone chain"],
            ["Satellite navigation", "GPS (Global Positioning System), GIS (Geographic Information System)"],
            ["Measurement &amp; control", "Virtual instruments (e.g. vector analyzers), automotive electronics"],
            ["Military &amp; safety", "Early-warning radar/sonar, cruise missiles, smart bombs, UAVs"],
            ["Consumer electronics", "Digital video/camera, MP3, HDTV, home theatre, IP phone, IPTV"],
            ["Medical", "Ultrasound, MRI, CT, gamma knife, hearing aids"],
            ["Other", "Drowsy-driving alert, digital watermarking, video surveillance, fingerprint ID, pattern recognition, image/video repair"],
        ],
    ))
    parts.append(note(
        "Course context: assessment = Exams 50% + Project 20% + Homework 20% + Quizzes 10%; "
        "related courses are Signals &amp; Systems, Advanced Maths/Linear Algebra, Programming, "
        "Microcomputer Principles, Logic Circuits."
    ))

    # =====================================================================
    # LECTURE 2 - CONTINUOUS-TIME SIGNALS AND SYSTEMS
    # =====================================================================
    parts.append(sec("Lecture 2 &middot; Continuous-Time Signals and Systems"))

    parts.append(h("2.1 Analysis Philosophy"))
    parts.append(p(
        "There are too many distinct signals/systems to study one at a time. Instead: "
        "decompose an arbitrary signal into simple building-block signals, find the system's "
        "response to each, then combine (superpose) those responses to get the response to the "
        "original input. This is the core idea behind both time-domain (impulse/convolution) "
        "and frequency-domain (Fourier) analysis."
    ))

    parts.append(h("2.2 Typical Continuous-Time Signals"))
    parts.append(p(
        "A signal is a time function f(t). If f(t) = 0 for t &lt; 0 it is a <b>causal</b> "
        "signal (has a start at t = 0)."
    ))
    parts.append(table(
        ["Signal", "Definition / notes"],
        [
            ["Unit step u(t)", "u(t)=1 for t&ge;0, 0 otherwise. Basic causal signal &mdash; multiplying any signal by u(t) makes it causal."],
            ["Sinusoid", "f(t)=A sin(&omega;t+&phi;)=A sin(2&pi;ft+&phi;). A=amplitude, f=frequency (Hz), &omega;=2&pi;f=angular frequency (rad/s), &phi;=start phase. Non-causal &amp; periodic: f(t)=f(t+mT); representable via Euler's relation (complex exponentials)."],
            ["Exponential, real &alpha;: f(t)=e<sup>&alpha;t</sup>", "&alpha;&lt;0 decaying, &alpha;=0 constant, &alpha;&gt;0 growing."],
            ["Exponential, complex &alpha;=&sigma;+j&omega;", "f(t)=Ae<sup>&alpha;t</sup>=Ae<sup>&sigma;t</sup>cos&omega;t + jAe<sup>&sigma;t</sup>sin&omega;t. &sigma;=0: sinusoidal; &sigma;&gt;0: growing sinusoid; &sigma;&lt;0: decaying (damped) sinusoid."],
            ["Gate p&tau;(t)", "p&tau;(t)=u(t+&tau;/2) &minus; u(t&minus;&tau;/2): a rectangular pulse of width &tau;, built from two shifted unit steps."],
        ],
    ))

    parts.append(h("2.3 Unit Impulse &delta;(t) and its Properties"))
    parts.append(p(
        "&delta;(t) is zero everywhere except t=0, and cannot be given a finite value even at "
        "t=0 &mdash; it is a <b>singularity (generalized) function</b>, defined only through an "
        "integral, not a regular function with exact point values. It is obtained as the limit "
        "of a gate pulse p&tau;(t) whose width &tau;&rarr;0 while its area stays 1 (so its "
        "height &rarr;&infin;)."
    ))
    parts.append(table(
        ["Property", "Statement"],
        [
            ["Sampling property", "f(t)&middot;&delta;(t)=f(0)&delta;(t) (since &delta;(t)=0 for t&ne;0 and f(0) is constant at t=0); &int;f(t)&delta;(t)dt=f(0)"],
            ["Shift", "&delta;(t&minus;&tau;) is the impulse relocated to t=&tau;"],
            ["Scaling", "A&delta;(t): A is the impulse <i>intensity</i> = area under the impulse"],
            ["Derivative / integral", "&delta;&prime;(t)=d&delta;(t)/dt is also an impulse-type function; the integral of &delta;(t) is the unit step u(t)"],
            ["Even symmetry", "&delta;(t)=&delta;(&minus;t), inherited from the even gate signal it derives from"],
        ],
    ))
    parts.append(p(
        "Any signal can be approximated as a sum of narrow rectangles of width &Delta;&tau;, "
        "height f(k&Delta;&tau;) &mdash; i.e. weighted, shifted impulses f(k&Delta;&tau;)&Delta;&tau;&delta;(t&minus;k&Delta;&tau;). "
        "As &Delta;&tau;&rarr;d&tau; this sum becomes the exact integral representation of f(t) "
        "as a continuum of shifted, weighted impulses &mdash; the basis for convolution."
    ))

    parts.append(h("2.4 Linear Time-Invariant (LTI) Systems &amp; Convolution"))
    parts.append(table(
        ["Property", "Condition"],
        [
            ["Linear", "Scaling: af(t)&rarr;ay(t). Additivity: f<sub>1</sub>(t)+f<sub>2</sub>(t)&rarr;y<sub>1</sub>(t)+y<sub>2</sub>(t). Combined: af<sub>1</sub>(t)+bf<sub>2</sub>(t)&rarr;ay<sub>1</sub>(t)+by<sub>2</sub>(t)"],
            ["Time-invariant", "f(t&minus;t<sub>0</sub>)&rarr;y(t&minus;t<sub>0</sub>) for any shift t<sub>0</sub>"],
        ],
    ))
    parts.append(p(
        "The response to &delta;(t) is the system's <b>unit impulse response h(t)</b>. Because "
        "any input f(t) is a sum of shifted, weighted impulses, and the system is linear &amp; "
        "time-invariant, the total response is the same sum of shifted, weighted copies of "
        "h(t) &mdash; this sum is the <b>convolution</b> of f(t) and h(t):"
    ))
    parts.append(eq("y(t) = f(t) * h(t)   (convolution)"))
    parts.append(note(
        "Time-domain view: decompose signals into shifted/weighted &delta;(t) and track only "
        "the impulse response. Frequency-domain view: decompose signals into sin&omega;t and "
        "its harmonics instead (Fourier analysis, below)."
    ))

    parts.append(h("2.5 Fourier Series (Periodic Signals)"))
    parts.append(p(
        "A periodic signal (period T) can be expanded as a Fourier series (trigonometric or, "
        "more compactly, exponential form), with coefficients equal to the signal's average "
        "over one period. Example: a periodic rectangular pulse train (period T, pulse width "
        "&tau;, amplitude A) has Fourier coefficients"
    ))
    parts.append(eq("F<sub>n</sub> = (A&tau;/T)&middot;Sa(n&omega;<sub>0</sub>&tau;/2),  Sa(x) = sin(x)/x,  &omega;<sub>0</sub>=2&pi;/T"))
    parts.append(p(
        "where Sa(x)=sin(x)/x is the <b>sampling function</b> &mdash; the discrete line "
        "spectrum of a rectangular pulse train follows its envelope."
    ))

    parts.append(h("2.6 Fourier Transform (Non-Periodic Signals)"))
    parts.append(p(
        "Viewing a non-periodic signal as the limit of a periodic one as T&rarr;&infin;: the "
        "harmonic spacing &omega;<sub>0</sub>&rarr;0 and each line's amplitude F<sub>n</sub>&rarr;0, "
        "so discrete spectral lines no longer make sense &mdash; instead we describe the signal "
        "by a continuous <b>spectrum density</b>, the Fourier Transform F(j&omega;)."
    ))
    parts.append(table(
        ["Signal", "Fourier Transform F(j&omega;)"],
        [
            ["Gate p&tau;(t)", "&tau;&middot;Sa(&omega;&tau;/2) &mdash; a Sa-shaped spectrum, first zeros at &omega;=&plusmn;2&pi;/&tau;"],
            ["Exponential e<sup>&minus;at</sup>u(t), a&gt;0", "1/(a+j&omega;); magnitude peaks at 1/a, decays with &omega;"],
            ["Unit impulse &delta;(t)", "1 &mdash; uniform (flat) density over all frequencies &rArr; infinite bandwidth"],
            ["Constant 1 (DC)", "2&pi;&delta;(&omega;) &mdash; all energy concentrated at &omega;=0 (symmetry of the DC/impulse pair)"],
            ["cos&omega;<sub>0</sub>t", "&pi;[&delta;(&omega;+&omega;<sub>0</sub>)+&delta;(&omega;&minus;&omega;<sub>0</sub>)] &mdash; two real impulses at &plusmn;&omega;<sub>0</sub>"],
            ["sin&omega;<sub>0</sub>t", "j&pi;[&delta;(&omega;+&omega;<sub>0</sub>)&minus;&delta;(&omega;&minus;&omega;<sub>0</sub>)] &mdash; imaginary impulses at &plusmn;&omega;<sub>0</sub>"],
            ["Unit impulse train (period T)", "another impulse train in frequency, spacing &omega;<sub>0</sub>=2&pi;/T, weight &omega;<sub>0</sub> &mdash; basis of sampling theory"],
        ],
    ))

    parts.append(h("2.7 Properties of the Fourier Transform"))
    parts.append(table(
        ["Property", "Statement"],
        [
            ["Linearity", "af<sub>1</sub>(t)+bf<sub>2</sub>(t) &harr; aF<sub>1</sub>(j&omega;)+bF<sub>2</sub>(j&omega;) (FT is an integral &rArr; linear operator)"],
            ["Time shift", "f(t&minus;t<sub>0</sub>) &harr; F(j&omega;)e<sup>&minus;j&omega;t0</sup> &mdash; a time shift is a pure phase shift in frequency"],
            ["Frequency shift (modulation)", "f(t)e<sup>j&omega;0t</sup> &harr; F[j(&omega;&minus;&omega;<sub>0</sub>)]; so f(t)cos&omega;<sub>0</sub>t &harr; &frac12;{F[j(&omega;+&omega;<sub>0</sub>)]+F[j(&omega;&minus;&omega;<sub>0</sub>)]} &mdash; amplitude modulation shifts the spectrum to &plusmn;&omega;<sub>0</sub>"],
            ["Energy / Parseval", "Signal energy W computed in time equals the integral of |F(j&omega;)|&sup2; (energy spectrum) in frequency &mdash; same shape as |F(j&omega;)| but with no phase information"],
            ["Convolution (time)", "f<sub>1</sub>(t)*f<sub>2</sub>(t) &harr; F<sub>1</sub>(j&omega;)F<sub>2</sub>(j&omega;) &mdash; convolution in time = multiplication in frequency"],
            ["Convolution (frequency)", "f<sub>1</sub>(t)f<sub>2</sub>(t) &harr; (1/2&pi;)[F<sub>1</sub>(j&omega;)*F<sub>2</sub>(j&omega;)] &mdash; multiplication in time = convolution in frequency"],
        ],
    ))
    parts.append(note(
        "The convolution theorem is the key link: it turns convolution in one domain into "
        "plain algebra (multiplication) in the other &mdash; nearly every other FT property can "
        "be derived from it."
    ))

    parts.append(h("2.8 Frequency-Domain Analysis of Linear Systems"))
    parts.append(p(
        "H(j&omega;) is the system (transfer) function: Y(j&omega;)=F(j&omega;)H(j&omega;), the "
        "frequency-domain counterpart of y(t)=f(t)*h(t). When a system is too complex for an "
        "analytical H(j&omega;), it can be measured empirically by driving the system with "
        "sinusoids of different frequencies and recording the output &mdash; this technique is "
        "called a <b>frequency sweep</b>."
    ))

    # =====================================================================
    # LECTURE 3 - DISCRETE-TIME SIGNALS AND SYSTEMS
    # =====================================================================
    parts.append(sec("Lecture 3 &middot; Discrete-Time Signals and Systems"))

    parts.append(h("3.1 Discrete-Time Signals &amp; Sampling"))
    parts.append(p(
        "A discrete-time sequence x[n] is often generated by uniformly sampling a "
        "continuous-time signal x<sub>a</sub>(t):"
    ))
    parts.append(eq("x[n] = x<sub>a</sub>(t)|<sub>t=nT</sub> = x<sub>a</sub>(nT),  n = &hellip;,&minus;1,0,1,&hellip;"))
    parts.append(p(
        "T = sampling interval/period; F<sub>T</sub>=1/T = sampling frequency. "
        "<b>Sampled-data signal</b>: samples are continuous-valued. <b>Digital signal</b>: "
        "samples are discrete-valued (obtained by quantizing via rounding/truncation) &mdash; "
        "real DSP systems work on digital signals. A sequence with zero samples for n&lt;N<sub>1</sub> "
        "is <b>right-sided</b>; if N<sub>1</sub>&ge;0 it is <b>causal</b>."
    ))

    parts.append(h("3.2 Basic Operations on Sequences"))
    parts.append(table(
        ["Operation", "Definition"],
        [
            ["Product (modulation)", "y[n]=x[n]&middot;w[n]"],
            ["Addition", "y[n]=x[n]+w[n]"],
            ["Scalar multiplication", "y[n]=A&middot;x[n]"],
            ["Time shift &mdash; unit delay", "y[n]=x[n&minus;1]"],
            ["Time shift &mdash; unit advance", "y[n]=x[n+1]"],
            ["Time reversal (folding)", "y[n]=x[&minus;n]"],
            ["Branching", "one sequence copied to feed multiple operations"],
        ],
    ))
    parts.append(note("Example combining several: y[n]=&alpha;<sub>1</sub>x[n]+&alpha;<sub>2</sub>x[n&minus;1]+&alpha;<sub>3</sub>x[n&minus;2]+&alpha;<sub>4</sub>x[n&minus;3]."))

    parts.append(h("3.3 Sampling-Rate Alteration"))
    parts.append(p(
        "Generates a new sequence y[n] with sampling rate F&prime;<sub>T</sub> different from "
        "x[n]'s rate F<sub>T</sub>. Alteration ratio R=F&prime;<sub>T</sub>/F<sub>T</sub>: "
        "<b>R&gt;1 &rArr; interpolation</b> (rate increases), <b>R&lt;1 &rArr; decimation</b> (rate decreases)."
    ))

    parts.append(h("3.4 Classifying Sequences"))
    parts.append(table(
        ["Class", "Definition"],
        [
            ["Periodic", "x[n]=x[n+N] for all n &mdash; satisfies the periodicity condition for some integer N"],
            ["Energy signal", "Finite total energy &Sigma;|x[n]|&sup2;, but zero average power (e.g. any finite-length sequence)"],
            ["Power signal", "Infinite total energy but finite average power (e.g. a periodic sequence)"],
            ["Bounded", "|x[n]|&le;B<sub>x</sub>&lt;&infin; for all n (e.g. cos(0.3&pi;n) is bounded)"],
            ["Absolutely summable", "&Sigma;|x[n]| &lt; &infin; over all n"],
            ["Square summable", "&Sigma;|x[n]|&sup2; &lt; &infin; (finite energy) over all n"],
        ],
    ))

    parts.append(h("3.5 Basic Sequences"))
    parts.append(table(
        ["Sequence", "Definition / notes"],
        [
            ["Unit sample &delta;[n]", "1 at n=0, 0 elsewhere &mdash; discrete analogue of &delta;(t)"],
            ["Unit step u[n]", "1 for n&ge;0, 0 for n&lt;0"],
            ["Real sinusoid", "x[n]=Acos(&omega;<sub>0</sub>n+&phi;): A=amplitude, &omega;<sub>0</sub>=angular frequency, &phi;=phase"],
            ["Exponential", "x[n]=A&alpha;<sup>n</sup>, A and &alpha; real or complex. Real &alpha;: |&alpha;|&gt;1 grows (e.g. &alpha;=1.2), |&alpha;|&lt;1 decays (e.g. &alpha;=0.9). Complex: real/imag parts are sinusoids with constant (&sigma;<sub>0</sub>=0), growing (&sigma;<sub>0</sub>&gt;0) or decaying (&sigma;<sub>0</sub>&lt;0) envelopes"],
        ],
    ))
    parts.append(p(
        "Acos(&omega;<sub>0</sub>n+&phi;) and Be<sup>j&omega;0n</sup> are periodic with period N "
        "iff &omega;<sub>0</sub>N=2&pi;r for positive integers N, r; the smallest such N is the "
        "<b>fundamental period</b> (e.g. &omega;<sub>0</sub>=0.1&pi; &rArr; N=2&pi;r/&omega;<sub>0</sub>=20 "
        "for r=1). As with continuous signals, an arbitrary sequence can be written as a "
        "weighted sum of basic sequences and their delayed/advanced versions."
    ))

    parts.append(h("3.6 The Sampling Process &amp; Nyquist Theorem"))
    parts.append(p(
        "Sample instants: t<sub>n</sub>=nT=n/F<sub>T</sub>=2&pi;n/&Omega;<sub>T</sub>, where "
        "&Omega;<sub>T</sub>=2&pi;F<sub>T</sub> is the sampling angular frequency. For a signal "
        "x<sub>a</sub>(t) built from a weighted sum of sinusoids, {x[n]} represents x<sub>a</sub>(t) "
        "uniquely only if &Omega;<sub>T</sub> is chosen greater than 2&times; the highest "
        "frequency present in x<sub>a</sub>(t). This anti-aliasing condition is the "
        "<b>sampling theorem (Nyquist theorem)</b>."
    ))

    parts.append(h("3.7 Discrete-Time System Properties"))
    parts.append(table(
        ["Property", "Definition"],
        [
            ["Linear", "Input ax<sub>1</sub>[n]+bx<sub>2</sub>[n] &rArr; output ay<sub>1</sub>[n]+by<sub>2</sub>[n], for any constants a, b and any inputs"],
            ["Shift-invariant", "x[n]=x<sub>1</sub>[n&minus;n<sub>0</sub>] &rArr; y[n]=y<sub>1</sub>[n&minus;n<sub>0</sub>] for any integer n<sub>0</sub> (a.k.a. time-invariant)"],
            ["Causal", "Output at n depends only on present and past inputs"],
            ["Stable", "Bounded input produces bounded output"],
            ["Passive / lossless", "Output energy does not exceed (passive) / exactly equals (lossless) input energy"],
        ],
    ))
    parts.append(p(
        "A system satisfying both linearity and shift-invariance is an <b>LTI system</b> &mdash; "
        "mathematically easy to analyze/design, and the basis of most practical DSP algorithms."
    ))

    parts.append(h("3.8 Impulse Response &amp; the Convolution Sum"))
    parts.append(p(
        "The response to &delta;[n] is the <b>impulse response h[n]</b>; the response to u[n] "
        "is the <b>step response s[n]</b>. Because linearity+shift-invariance let any x[n] be "
        "written as a sum of weighted, shifted unit samples, the output is fully determined by "
        "h[n]:"
    ))
    parts.append(eq("y[n] = x[n] * h[n] = &Sigma;<sub>k</sub> x[k]h[n&minus;k]   (convolution sum)"))
    parts.append(table(
        ["Property", "Statement"],
        [
            ["Commutative", "x[n]*h[n] = h[n]*x[n]"],
            ["Associative", "(x[n]*h[n])*y[n] = x[n]*(h[n]*y[n])"],
            ["Distributive", "x[n]*(h[n]+y[n]) = x[n]*h[n] + x[n]*y[n]"],
        ],
    ))
    parts.append(p(
        "<b>Graphical procedure</b> to evaluate y[n]: (1) time-reverse h[k] to get h[&minus;k]; "
        "(2) shift right by n (n&gt;0) or left (n&lt;0) to get h[n&minus;k]; (3) form the "
        "product v[k]=x[k]h[n&minus;k]; (4) sum all samples of v[k] to get y[n]. If x[n] and "
        "h[n] have lengths M and N, the convolution result has length <b>M+N&minus;1</b>."
    ))

    parts.append(h("3.9 FIR vs IIR, Recursive vs Non-Recursive"))
    parts.append(table(
        ["Classification", "Definition"],
        [
            ["FIR (Finite Impulse Response)", "h[n]=0 for n&lt;N<sub>1</sub> and n&gt;N<sub>2</sub> (finite length). Output is a finite sum of products, computed directly from the convolution sum."],
            ["IIR (Infinite Impulse Response)", "h[n] has infinite length; characterized by linear constant-coefficient difference equations. Example &mdash; the accumulator y[n]=y[n&minus;1]+x[n] is IIR."],
            ["Non-recursive", "Output computed from present &amp; past <i>inputs</i> only"],
            ["Recursive", "Output computation also uses past <i>output</i> samples (feedback), in addition to present/past inputs"],
        ],
    ))

    return "<body>" + "".join(parts) + "</body>", 3


def main():
    body_html, n_lectures = build_html()
    story = fitz.Story(html=body_html, user_css=CSS)
    writer = fitz.DocumentWriter(OUT)
    mediabox = fitz.paper_rect("a4")
    where = mediabox + (34, 30, -34, -30)

    pages = 0
    more = 1
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
        pages += 1
    writer.close()
    print(f"Wrote {OUT}: {n_lectures} lectures across {pages} pages")


if __name__ == "__main__":
    main()
