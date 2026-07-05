#!/usr/bin/env python3
"""
Build the Digital Signal Processing (TE 454) MCQ bank.

Source material (extracted from the lecture slide decks in this folder):
  - TE 454 Lecture 1.pdf  (Introduction to DSP; analog vs digital; applications)
  - TE 454 Lecture 2.pdf  (Continuous-time signals & systems; impulse; LTI; Fourier)
  - TE 454 Lecture 3.pdf  (Discrete-time signals & systems; convolution; FIR/IIR)

The exam for this course is theory-based, so the questions target conceptual
understanding of the ideas in the slides rather than numerical calculation.

Each question is authored as (question_text, correct_answer, [distractor, distractor, distractor]).
Options are kept comparable in length and free of absolutist "tells" so the key
cannot be guessed without knowing the material. The script places the correct
answer at a balanced, pseudo-random position among the four options so that,
across the whole bank, the key (A/B/C/D) is evenly distributed. Output JSON
matches the format used by the other practice sites in this repository:

    {
      "question_number": 1,
      "question_text": "...",
      "options": ["...", "...", "...", "..."],
      "correct_answer": ["..."]
    }
"""
import json
import random

# ---------------------------------------------------------------------------
# SET 1 - DSP Fundamentals: analog vs digital, why digital, applications
#         (TE 454 Lecture 1)
# ---------------------------------------------------------------------------
SET1 = [
    ("In the context of this course, the phrase \"digital signal processing\" is best "
     "understood as:",
     "The theories, methods and algorithms for processing signals in digital form",
     ["The branch of electronics devoted to designing analog amplifiers and filters",
      "The study of how physical sensors convert measured quantities into voltages",
      "The fabrication of microprocessor chips from raw semiconductor wafer material"]),

    ("The term \"digital signal processor\" (as opposed to \"digital signal processing\") "
     "refers to:",
     "A kind of microprocessor used to implement digital signal processing algorithms",
     ["The mathematical algorithm through which an input signal is passed for its result",
      "The analog front-end that band-limits a signal before it reaches the converter",
      "The high-level software language in which the processing routines are written"]),

    ("An analog signal is best characterised as one that is:",
     "Continuous in both time and magnitude",
     ["Continuous in time but discrete in magnitude",
      "Discrete in time but continuous in magnitude",
      "Discrete in both time and magnitude"]),

    ("A digital signal is best characterised as one that is:",
     "Discrete in both time and magnitude",
     ["Continuous in both time and magnitude",
      "Continuous in time but discrete in magnitude",
      "Discrete in time but continuous in magnitude"]),

    ("Before a real-world analog signal can be processed digitally, two transformations "
     "must be applied in order. They are:",
     "Sample the signal at discrete time points, then quantize the sample values",
     ["Quantize the signal in amplitude first, then sample it at discrete time points",
      "Amplify the signal to full scale, then shift its frequency into a lower band",
      "Filter the signal to remove noise, then store it directly in continuous form"]),

    ("Quantization of a sampled signal is normally carried out by:",
     "Rounding or truncating each sample value to an available level",
     ["Delaying each sample value by one sampling interval before it is stored",
      "Averaging each sample value together with its two nearest neighbours",
      "Multiplying each sample value by a fixed scaling constant before storage"]),

    ("Why must most real-world signals be transformed before a DSP system can operate on "
     "them?",
     "Most real-world signals are analog, while DSP works on signals in digital form",
     ["Most real-world signals are already digital and merely need to be amplified",
      "DSP systems can handle periodic signals but reject aperiodic ones outright",
      "DSP systems require a signal to be expressed in the frequency domain first"]),

    ("Which statement best captures the relationship between digitization and DSP that the "
     "course uses to motivate the subject?",
     "Digitization underpins information technology, and its kernel is digital signal processing",
     ["Digitization and DSP are competing techniques for handling the same signals",
      "DSP is a narrow niche that has little bearing on the modern information technology field",
      "Digitization replaced DSP once integrated circuits became widely available"]),

    ("A key reason a digital system offers greater programmability than an analog system is "
     "that:",
     "A digital system can be changed by modifying software rather than hardware",
     ["A digital system needs no software at all once its hardware has been fixed",
      "A digital system rewires its own internal circuits as its requirements change",
      "An analog system is reconfigured purely by editing its onboard firmware code"]),

    ("An engineer swaps a standard filter for an adaptive filter simply by loading new code, "
     "leaving the hardware untouched. This illustrates which advantage of digital systems?",
     "Programmability",
     ["Anti-noise performance",
      "Large-scale integration",
      "Real-time response"]),

    ("In a digital system, the precision of the processing is chiefly governed by:",
     "The number of ADC bits, the processor word-length and the algorithm used",
     ["The tolerance ratings printed on the resistors and the capacitors used",
      "The ambient temperature and the humidity of the operating environment",
      "The physical length of the wiring that connects the components together"]),

    ("Why is an analog system's precision considered harder to guarantee than a digital "
     "system's?",
     "Analog precision depends on component tolerances, such as resistors within 5% or capacitors within 20%",
     ["Analog precision is fixed by the bit count of its analog-to-digital converter alone",
      "Analog components retain their exact printed rated values throughout their whole service life",
      "Analog systems round each sample coarsely, discarding the finer detail of the signal"]),

    ("With respect to stability, how does a digital system typically compare with an analog "
     "one as temperature and humidity vary?",
     "The digital system shows essentially no variation across its rated operating range",
     ["The digital system drifts more because its logic gates are temperature-sensitive",
      "Both systems drift by roughly the same amount for a given change in temperature",
      "The digital system grows unstable while the analog system holds its values steady"]),

    ("The characteristics of analog components such as resistors, capacitors and op-amps are "
     "a concern for stability because they:",
     "Change with temperature, humidity and similar environmental conditions",
     ["Grow hard to measure accurately once they are soldered onto a circuit board",
      "Consume far more electrical power than the equivalent digital logic gates do",
      "Can be readjusted afterwards by rewriting the controlling software routines"]),

    ("The repeatability advantage of digital systems refers to the property that:",
     "Identical digital units process the same input into the same output",
     ["A single digital unit can process many different inputs at the same time",
      "A digital signal can be repeated indefinitely without needing any storage",
      "Digital units detect and correct a wrong result soon after producing it"]),

    ("Error-correcting codes are cited as an advantage of digital representation because "
     "they:",
     "Add redundant bits so that introduced errors can be detected and corrected",
     ["Compress the data so that fewer bits need to be sent over the channel",
      "Scramble the data so that unauthorised receivers are unable to read it",
      "Convert the data back into an analog form that is suited to transmission"]),

    ("Regarding fidelity in storage and transmission, the slides argue that:",
     "The fidelity of the digital medium is greater than that of the analog medium",
     ["The fidelity of the analog medium exceeds that of the digital medium",
      "Digital and analog media deliver essentially identical fidelity in practice",
      "Fidelity is governed mainly by the length of the transmission cable used"]),

    ("How does the course contrast analog and digital data compression?",
     "Analog compression loses some information, whereas digital technology makes lossless compression possible",
     ["Analog compression is the genuinely lossless kind, whereas digital compression loses information",
      "Neither analog nor digital compression is able to preserve the full information",
      "Digital compression suits images well but is not applicable to audio signals"]),

    ("The 3 kHz bandwidth limit applied to analog telephone lines is given as an example of:",
     "Analog compression in which some information is lost",
     ["A lossless digital compression scheme applied to the line",
      "An error-correcting code operating on the telephone line",
      "A sampling operation carried out before the quantization step"]),

    ("Which is listed as a genuine limitation of digital signal processing rather than an "
     "advantage?",
     "A/D and D/A conversion rates are not available for some applications, such as beyond GHz",
     ["Digital systems drift heavily whenever the operating temperature changes",
      "Digital systems resist any reprogramming once they have been deployed out in the field",
      "Digital systems are unable to store their data for later retrieval and use"]),

    ("One reason analog processing is still needed is real-time performance, because in an "
     "analog system:",
     "Aside from circuit delay, the processing happens in real time",
     ["The processing time is set by the processor speed and the chosen algorithm",
      "The signal must first be sampled before any output can begin to appear",
      "Each result must wait for a redundant error-correction pass to finish first"]),

    ("Why can analog systems still be preferred for very high-frequency signals such as "
     "microwave or light-wave signals?",
     "Such signals are limited by sample-and-hold, ADC and processor speeds, and fast ADCs cost a lot",
     ["Analog systems can store such high-frequency signals far more compactly than digital ones",
      "Very high-frequency signals carry no useful information that is worth the effort of digitizing",
      "Digital systems are designed to reject any signal lying above the standard audio band by rule"]),

    ("The remark that \"most signals in the real world are analog\" is used in the course to "
     "argue that:",
     "Mixed-signal processing is needed to convert such signals into digital form for a DSP system",
     ["Analog signals are best kept in analog form rather than converted into digital form",
      "DSP systems have by now made analog processing very nearly obsolete in practice",
      "Real-world signals arrive already sampled by nature and so need no conversion step"]),

    ("Base stations, switching centres and mobile phones are given as DSP applications under "
     "which broad area?",
     "Communications",
     ["Medical imaging",
      "Satellite navigation",
      "Consumer photography"]),

    ("GPS and GIS are cited as DSP applications belonging to which area?",
     "Satellite navigation",
     ["Measurement and control",
      "Military and safety",
      "Consumer electronics"]),

    ("Ultrasound, MRI and CT scanning are used in the slides as DSP examples in the field "
     "of:",
     "Medical imaging and analysis",
     ["Industrial measurement and control",
      "Wireless communication systems",
      "Satellite navigation and timing"]),

    ("MP3 audio decoding, digital cameras and HDTV are grouped in the slides under which "
     "application area?",
     "Consumer electronics",
     ["Military and safety",
      "Biomedical analysis",
      "Industrial control"]),

    ("The general problem of signal analysis and processing is framed in the course as:",
     "Letting signals pass through systems and studying the response",
     ["Storing signals in memory and later retrieving them unchanged",
      "Converting each signal into one single fixed reference frequency",
      "Stripping the timing information from a signal before it is used"]),
]

# ---------------------------------------------------------------------------
# SET 2 - Continuous-time signals, the unit impulse, and LTI systems
#         (TE 454 Lecture 2, first half)
# ---------------------------------------------------------------------------
SET2 = [
    ("The general strategy the course recommends for analysing a complicated signal through "
     "a system is to:",
     "Represent the signal as a sum of simple signals, get each response, then add the responses",
     ["Measure the output for the whole complicated signal without first decomposing it",
      "Replace the whole system with a single resistor-and-capacitor network before analysing",
      "Convert the input into one constant value before it is applied to the system"]),

    ("A signal f(t) for which f(t) = 0 for all t < 0 is called:",
     "A causal signal",
     ["A periodic signal",
      "An even signal",
      "A singularity signal"]),

    ("Multiplying an arbitrary (possibly non-causal) signal by the unit step u(t) has the "
     "effect of:",
     "Turning it into a causal signal that is zero for t < 0",
     ["Shifting it later in time by exactly one unit of time",
      "Reflecting it about the vertical amplitude axis",
      "Scaling its amplitude everywhere by a factor of two"]),

    ("For the sinusoid f(t) = A sin(2 pi f t + phi), the quantity omega = 2 pi f is called "
     "the:",
     "Angular frequency in radians per second",
     ["Amplitude of the waveform",
      "Start phase of the waveform in radians",
      "Period of the waveform in seconds"]),

    ("Why does the course classify a pure sinusoid as a non-causal signal?",
     "Being periodic, it has no start and no end in time",
     ["Its amplitude decays steadily toward zero as time increases",
      "It is defined for negative values of time but not positive ones",
      "It changes its frequency continuously as time goes on"]),

    ("For the real exponential f(t) = e^(alpha t), the sign of alpha determines that the "
     "signal is:",
     "Decaying when alpha < 0, constant when alpha = 0, and growing when alpha > 0",
     ["Growing when alpha < 0, and decaying when alpha > 0, for any real alpha",
      "Periodic for each real value that alpha can happen to take on",
      "Constant at zero unless alpha happens to equal exactly one"]),

    ("For a complex exponential with alpha = sigma + j omega, the real part sigma governs "
     "the envelope so that the signal is:",
     "A pure sinusoid when sigma = 0, growing when sigma > 0, and decaying (damped) when sigma < 0",
     ["A pure sinusoid when sigma > 0, and a constant amplitude when sigma < 0",
      "A constant-amplitude wave for each value that sigma may happen to take",
      "A non-oscillatory signal for whatever value the frequency omega happens to take on"]),

    ("A gate (rectangular) signal of width tau can be written using unit step signals as:",
     "The difference of two shifted unit steps, u(t + tau/2) - u(t - tau/2)",
     ["The product of two shifted unit steps taken over the interval",
      "The integral of a single unit step evaluated over all of time",
      "The derivative of a single unit step taken right at the origin"]),

    ("Why is the unit impulse delta(t) described as a singularity (generalized) function "
     "rather than a regular function?",
     "It cannot be given an ordinary value even at t = 0 and is defined only through an integral",
     ["It takes a different finite constant value at each separate instant along the axis",
      "It stays non-zero over a wide but finite interval around the time origin",
      "It is identical to the unit step function at each point along the time axis"]),

    ("Starting from a gate signal of width tau and unit area, the unit impulse delta(t) is "
     "obtained by:",
     "Shrinking the duration tau toward zero while keeping the area equal to one",
     ["Widening the duration tau while holding the pulse height fixed at one",
      "Holding the duration fixed while raising the pulse height toward infinity",
      "Averaging the gate signal over one full period of the waveform"]),

    ("As the width tau of the unit-area gate shrinks toward zero, its amplitude:",
     "Tends toward infinity, so the impulse cannot be defined by a regular function",
     ["Tends toward zero, so the impulse effectively vanishes from the signal",
      "Stays fixed at one throughout the whole limiting process",
      "Swings between plus one and minus one without ever settling down"]),

    ("The sampling (sifting) property of the impulse follows from the facts that delta(t) "
     "is zero for t not equal to 0 and that:",
     "At t = 0 the other factor equals its value f(0), a constant, over the impulse",
     ["The impulse takes on a distinct value at each separate instant of time",
      "The impulse integrates to a value of zero across the whole time axis",
      "The impulse equals the unit step signal near the neighbourhood of the origin"]),

    ("When the impulse is scaled as A*delta(t), the constant A is referred to as the:",
     "Impulse intensity, equal to the area of the scaled impulse",
     ["Angular frequency, equal to the rate of change of the impulse",
      "Start phase, equal to the time offset applied to the impulse",
      "Duration, equal to the width over which the impulse acts"]),

    ("The integral of the unit impulse delta(t) is:",
     "The unit step signal",
     ["Another impulse of twice the area",
      "A decaying exponential signal",
      "A constant equal to zero everywhere"]),

    ("With respect to symmetry, the unit impulse delta(t) is:",
     "An even function, so delta(t) = delta(-t)",
     ["An odd function, so delta(t) = -delta(-t)",
      "A causal function, zero for values of t below zero",
      "A periodic function with some finite repetition period"]),

    ("The course shows that any signal f(t) can be represented as:",
     "A sum (limit of an integral) of shifted and weighted unit impulses",
     ["A single scaled copy of the unit step function of time",
      "A product of two sinusoids lying at two different frequencies",
      "A constant term plus one single decaying exponential term"]),

    ("In approximating f(t) by narrow rectangles, the rectangle at t = k*(delta-tau) is "
     "represented as f(k*delta-tau)*(delta-tau)*delta(t - k*delta-tau). Making delta-tau "
     "smaller:",
     "Increases the accuracy, becoming exact as delta-tau tends to d-tau",
     ["Decreases the accuracy of the rectangle-based approximation",
      "Leaves the accuracy of the approximation unchanged at each step",
      "Removes the impulses entirely from the signal representation"]),

    ("A system is linear if, for scaling and additivity, it satisfies:",
     "a*f1(t) + b*f2(t) produces a*y1(t) + b*y2(t)",
     ["f(t - t0) produces the shifted output y(t - t0) for any t0",
      "The output equals the input multiplied by one fixed constant gain",
      "f1(t)*f2(t) produces the product y1(t)*y2(t) for any two inputs"]),

    ("A system is time-invariant if:",
     "Shifting the input as f(t - t0) simply shifts the output to y(t - t0)",
     ["Scaling the input by a factor of a scales the output up to a*y(t)",
      "Adding two separate inputs adds their two separate outputs",
      "The output depends on the present value of the input alone"]),

    ("Why are linear time-invariant (LTI) systems so central to this analysis method?",
     "Summing the responses to all the shifted, weighted impulses in f(t) works only for LTI systems",
     ["They form the sole class of systems capable of processing periodic input signals",
      "They yield a valid output even without any known impulse response function being available",
      "They convert each input signal into a single pure sinusoid at their output"]),

    ("The response of an LTI system to the unit impulse delta(t) is given a special name and "
     "symbol:",
     "The unit impulse response, denoted h(t)",
     ["The transfer function, denoted F(j*omega)",
      "The unit step response, denoted u(t)",
      "The system gain, denoted by the constant A"]),

    ("Why is the impulse response h(t) regarded as such an important descriptor of an LTI "
     "system?",
     "Since any signal is a sum of shifted, weighted impulses, h(t) gives the response to any input",
     ["Because it only gives the system response to a steady constant direct-current input",
      "Because it fixes the system's operating frequency without needing any input",
      "Because it lets you skip knowing the input signal when finding the output"]),

    ("When an input f(t) passes through an LTI system with impulse response h(t), the output "
     "is written y(t) = f(t) * h(t), where the operation \"*\" denotes:",
     "Convolution of f(t) and h(t)",
     ["Ordinary point-by-point multiplication",
      "Correlation of f(t) with itself",
      "Simple addition of f(t) and h(t)"]),

    ("Convolution y(t) = f(t) * h(t) is built from the elementary LTI facts that "
     "delta(t) -> h(t) and that:",
     "A shifted, scaled impulse a*delta(t - t0) produces a*h(t - t0)",
     ["A shifted impulse produces an unshifted, unscaled copy of h(t)",
      "Any impulse produces the unit step response rather than h(t)",
      "The impulse located at t = 0 alone produces a valid output"]),

    ("How does the course contrast the decomposition used in time-domain analysis with that "
     "used in frequency-domain analysis?",
     "Time-domain uses shifted, weighted impulses; frequency-domain uses a sinusoid plus harmonics",
     ["Both of the approaches decompose the signal into shifted, weighted impulses in time",
      "Time-domain analysis uses sinusoids and harmonics while frequency-domain uses impulses",
      "Neither of the approaches decomposes the signal; each processes it as a single whole"]),
]

# ---------------------------------------------------------------------------
# SET 3 - Fourier series, Fourier transform, and system functions
#         (TE 454 Lecture 2, second half)
# ---------------------------------------------------------------------------
SET3 = [
    ("The Fourier series is a tool that applies specifically to:",
     "Periodic signals",
     ["Causal signals",
      "Non-periodic signals",
      "Impulse signals"]),

    ("In frequency-domain analysis, a signal is decomposed into:",
     "A fundamental sinusoid together with its harmonics",
     ["A set of shifted and weighted impulse functions",
      "A single decaying exponential component in time",
      "A product of two unit step functions of time"]),

    ("The sampling function that arises in the spectrum of a periodic rectangular waveform "
     "is:",
     "Sa(x) = sin(x)/x",
     ["Sa(x) = cos(x)/x",
      "Sa(x) = x*sin(x)",
      "Sa(x) = 1/(1 + x^2)"]),

    ("The Fourier transform is introduced as the tool needed when a signal is:",
     "Non-periodic, formed as a periodic signal's period tends to infinity",
     ["Periodic, though repeating only over a very short period of time",
      "Constant in both its time variable and its amplitude value",
      "Defined at only a single isolated instant along the time axis"]),

    ("As the period T of a periodic signal is expanded toward infinity, both the line "
     "amplitude Fn and the spacing omega_0 tend to zero, which motivates:",
     "Introducing spectrum density instead of discrete frequency lines",
     ["Keeping the discrete frequency lines exactly as they were",
      "Discarding all of the frequency information about the signal",
      "Treating the whole signal as a single impulse located in time"]),

    ("The Fourier transform of a unit impulse delta(t) is a constant across all frequencies, "
     "which means the impulse:",
     "Has uniform frequency density and therefore an infinitely wide band",
     ["Contains only one single frequency component in its spectrum",
      "Has essentially no frequency content anywhere in its spectrum",
      "Is band-limited to a narrow range of low frequencies"]),

    ("The Fourier transform of a constant (DC) signal of value 1 is:",
     "An impulse at zero frequency, 2*pi*delta(omega)",
     ["A constant density spread across all frequencies",
      "A pair of impulses at plus and minus omega_0",
      "A sinc-shaped spectrum centred at the origin"]),

    ("Why does the spectrum of the constant signal 1 consist of an impulse only at "
     "omega = 0?",
     "A constant represents a direct-current signal, whose energy lies entirely at zero frequency",
     ["A constant carries equal amounts of energy at every single frequency that is present",
      "A constant is a high-frequency signal that occupies only a very narrow band",
      "A constant places its energy at a pair of separate carrier frequencies only"]),

    ("The Fourier transform of cos(omega_0 t) consists of:",
     "A pair of impulses located at plus and minus omega_0",
     ["A single impulse located exactly at zero frequency",
      "A uniform density spread across all of the frequencies",
      "A sinc-shaped lobe centred at omega_0 by itself"]),

    ("The linearity property of the Fourier transform states that:",
     "The transform of a*f1(t) + b*f2(t) is a*F1(j*omega) + b*F2(j*omega)",
     ["The transform of a product equals the product of the two transforms",
      "The transform of a sum equals the larger of the two transforms",
      "Scaling a signal in time has no effect at all on its transform"]),

    ("According to the time-shift property, delaying a signal by t0 in the time domain "
     "corresponds in the frequency domain to:",
     "Multiplying the spectrum by the phase e^(-j*omega*t0), the magnitude unchanged",
     ["Scaling the magnitude of the whole spectrum by the delay value of t0",
      "Sliding the entire spectrum bodily along the frequency axis by t0 units",
      "Adding a fixed constant phase equal to t0 radians at each frequency"]),

    ("The frequency-shift (modulation) property says that multiplying f(t) by e^(j*omega_0 t) "
     "in the time domain:",
     "Shifts the spectrum to F[j(omega - omega_0)] in the frequency domain",
     ["Multiplies the spectrum by the constant factor e^(-j*omega_0)",
      "Delays the signal by omega_0 seconds along the time axis",
      "Leaves the spectrum of the signal unaffected altogether"]),

    ("Multiplying a baseband signal f(t) by a carrier cos(omega_0 t) produces a spectrum "
     "that is:",
     "Two half-amplitude copies of F(j*omega) centred at plus and minus omega_0",
     ["A single copy of F(j*omega) left sitting right at the frequency origin",
      "An impulse at zero frequency scaled by the carrier amplitude",
      "The original spectrum F(j*omega) with its bandwidth halved"]),

    ("Parseval's relation (the energy theorem) expresses that:",
     "The total energy of a signal can be computed in the time or the frequency domain",
     ["The total energy of a real-valued signal always works out to be zero",
      "The phase of a signal carries the whole of its energy information",
      "Energy is conserved only for perfectly periodic signals but not for others"]),

    ("The quantity |F(j*omega)|^2 is called the signal's energy spectrum because it "
     "represents:",
     "The signal energy contained in a unit band of frequency, carrying no phase information",
     ["The instantaneous power carried by the signal at each separate moment in time",
      "The phase of the signal expressed as a function of the frequency",
      "The total count of the frequency lines making up the whole spectrum"]),

    ("The time-domain convolution theorem of the Fourier transform states that:",
     "Convolution in time corresponds to multiplication of the spectra, F1(j*omega)*F2(j*omega)",
     ["Convolution in time corresponds instead to convolution of the two spectra as well",
      "Convolution in time corresponds to simple addition of the two spectra",
      "Convolution in time leaves each of the two signal spectra unchanged"]),

    ("The frequency-domain convolution theorem states that multiplication of two signals in "
     "time corresponds in frequency to:",
     "Convolution of their spectra, scaled by a factor of 1/(2*pi)",
     ["Multiplication of their spectra with no extra scaling factor",
      "Addition of their two spectra with a factor of 2*pi applied",
      "The difference of their two spectra taken across frequency"]),

    ("What broad usefulness does the convolution theorem provide, according to the slides?",
     "It turns convolution in one domain into an algebraic operation in the other domain",
     ["It converts an input signal into a single sharp impulse located firmly in time",
      "It removes the need to know a system's impulse response when solving",
      "It applies solely to signals that happen to be perfectly periodic ones"]),

    ("For a linear system, the quantity H(j*omega) that relates input and output spectra is "
     "called the:",
     "System function, also called the transfer function",
     ["Energy spectrum of the applied input signal in frequency",
      "Impulse intensity of the system",
      "Sampling function of the output"]),

    ("If a system has impulse response h(t) and transfer function H(j*omega), then the "
     "output spectrum is given by:",
     "Y(j*omega) = F(j*omega)*H(j*omega), the product of input spectrum and transfer function",
     ["Y(j*omega) = F(j*omega) + H(j*omega), the sum of the input and the function",
      "Y(j*omega) = F(j*omega) / H(j*omega), the ratio of the input to the transfer function",
      "Y(j*omega) = F(j*omega), taken independently of the system's own function"]),

    ("The fact that Y(j*omega) = F(j*omega)*H(j*omega) in the frequency domain corresponds "
     "in the time domain to:",
     "The convolution y(t) = f(t) * h(t) taken in the time domain",
     ["The product y(t) = f(t)*h(t) taken sample by sample in time",
      "The sum y(t) = f(t) + h(t) taken point by point in time",
      "The derivative of f(t) with respect to time at each instant"]),

    ("If a system is too complicated to express analytically, the slides suggest measuring "
     "its transfer function by:",
     "Applying sine inputs at different frequencies, measuring each output, and combining them",
     ["Applying a single impulse and reading off the final steady-state value",
      "Applying a constant direct-current input and then scaling up the measured result",
      "Computing the ratio between two arbitrarily chosen samples in time"]),

    ("The technique of driving a system with sine inputs across a range of frequencies to "
     "characterise it is called:",
     "A frequency sweep",
     ["A convolution sum",
      "A time reversal",
      "An impulse decomposition"]),

    ("Euler's relation is invoked in this material chiefly to:",
     "Express sine and cosine signals in terms of complex exponentials",
     ["Convert a periodic signal into an equivalent causal signal",
      "Prove that the unit impulse is an even function of time",
      "Define the sampling interval used for a discrete signal"]),

    ("The Fourier transform of the one-sided exponential e^(-a t)*u(t) with a > 0 has a "
     "magnitude spectrum that:",
     "Is largest at zero frequency and then rolls off as the frequency increases",
     ["Is a pair of sharp impulses located at plus and minus a",
      "Is flat and equal in value at every one of the frequencies",
      "Is zero at the low frequencies and then rises without any upper bound"]),
]

# ---------------------------------------------------------------------------
# SET 4 - Discrete-time signals & systems, convolution sum, FIR/IIR
#         (TE 454 Lecture 3)
# ---------------------------------------------------------------------------
SET4 = [
    ("In the time domain, a discrete-time signal is represented as:",
     "A sequence of numbers, called samples",
     ["A continuous waveform defined at every instant",
      "A single scalar value that never changes in time",
      "A frequency spectrum holding no time information"]),

    ("When a discrete-time sequence is formed by sampling a continuous signal x_a(t), the "
     "n-th sample is given by:",
     "x[n] = x_a(nT), the value of x_a(t) taken at t = nT",
     ["x[n] = x_a(t) integrated from time 0 up to t = nT",
      "x[n] = x_a(t) averaged across the interval of width T",
      "x[n] = the derivative of x_a(t) evaluated at t = nT"]),

    ("The spacing T between two consecutive samples is called the sampling interval, and its "
     "reciprocal 1/T is called the:",
     "Sampling frequency",
     ["Angular frequency of the samples",
      "Fundamental period of the sequence",
      "Quantization step of the sequence"]),

    ("The course distinguishes sampled-data signals from digital signals by noting that:",
     "Sampled-data signals have continuous-valued samples, while digital signals have discrete-valued samples",
     ["Sampled-data signals have discrete-valued samples, while the digital ones are continuous-valued",
      "Both sampled-data and digital signals turn out to have continuous-valued samples",
      "Sampled-data signals alone are the ones actually defined at discrete time instants"]),

    ("Signals in a practical DSP system are digital signals, obtained from sample values by:",
     "Quantizing them, either by rounding or by truncation",
     ["Convolving them with the unit step sequence in time",
      "Reversing them in time about the sampling origin",
      "Interpolating them up to a higher sampling rate"]),

    ("A right-sided sequence has zero-valued samples for n < N1. It is additionally called a "
     "causal sequence when:",
     "N1 >= 0",
     ["N1 < 0",
      "N1 is a non-integer value",
      "N1 tends to negative infinity"]),

    ("In the modulation (product) operation on sequences, the output is formed by:",
     "Multiplying the two input sequences sample by sample, y[n] = x[n]*w[n]",
     ["Adding the two input sequences sample by sample, y[n] = x[n] + w[n]",
      "Delaying one of the input sequences by a single sampling interval",
      "Reversing one input sequence in time before they are combined"]),

    ("The scalar-multiplication operation on a sequence produces:",
     "y[n] = A*x[n], each sample scaled by a constant A",
     ["y[n] = x[n] + A, a constant A added to each sample",
      "y[n] = x[n - A], the sequence delayed by A samples",
      "y[n] = x[A*n], the sequence resampled in the time index"]),

    ("A unit-delay operation applied to x[n] produces the output:",
     "y[n] = x[n - 1]",
     ["y[n] = x[n + 1]",
      "y[n] = x[-n]",
      "y[n] = A*x[n]"]),

    ("The time-reversal (folding) operation on a sequence produces:",
     "y[n] = x[-n]",
     ["y[n] = x[n - 1]",
      "y[n] = x[n] + x[-n]",
      "y[n] = x[n]*x[-n]"]),

    ("The branching operation in a discrete-time structure is used to:",
     "Provide multiple copies of a sequence for use at different points",
     ["Combine several separate sequences into just one single output",
      "Delay a sequence by exactly one sampling period in time",
      "Reverse a sequence about the origin of the time axis"]),

    ("In sampling-rate alteration, the ratio R = F'_T / F_T describes the change of rate. "
     "The process is called interpolation when:",
     "R > 1, giving a higher sampling rate",
     ["R < 1, giving a lower sampling rate",
      "R = 1, leaving the rate unchanged",
      "R is negative, reversing the sequence"]),

    ("In sampling-rate alteration, the process is called decimation when:",
     "R < 1, giving a lower sampling rate",
     ["R > 1, giving a higher sampling rate",
      "R = 0, removing all of the samples",
      "R = 1, leaving the rate unchanged"]),

    ("A discrete-time sequence is classified as periodic when:",
     "It repeats, so that x[n] equals x[n + N] for some period N",
     ["Its samples all settle to one and the same constant value",
      "It has only a finite number of non-zero samples in total",
      "Its samples decay steadily toward zero as n increases"]),

    ("With respect to length and energy, which statement matches the course's classification?",
     "A finite-length sequence with finite sample values always has finite energy",
     ["A finite-length sequence with finite sample values instead has infinite energy",
      "An infinite-length sequence is guaranteed to end up with finite energy",
      "A sequence that has finite energy is bound to have an infinite length"]),

    ("A sequence is classified as a power signal when it has:",
     "Infinite energy but finite average power, as a periodic sequence has",
     ["Finite energy but zero average power, as a short sequence has",
      "Both finite energy and finite average power at the same time",
      "Zero energy together with zero average power everywhere"]),

    ("A sequence is classified as an energy signal when it has:",
     "Finite energy but zero average power, as a finite-length sequence has",
     ["Infinite energy but finite average power, as a periodic sequence has",
      "Infinite energy together with an infinite average power at once",
      "Finite energy together with a finite, non-zero average power"]),

    ("A sequence x[n] is said to be bounded when:",
     "Its magnitude stays below a finite limit for all n, as cos(0.3*pi*n) does",
     ["The sum of all of its sample values turns out to be finite",
      "The sum of the squares of all of its sample values turns out finite",
      "It has only a finite number of non-zero samples in total"]),

    ("The two fundamental basic sequences introduced first in the discrete-time material "
     "are:",
     "The unit sample sequence and the unit step sequence",
     ["The gate sequence and the linear ramp sequence",
      "The chirp sequence and the constant sequence",
      "The random sequence and the periodic sequence"]),

    ("A real sinusoidal sequence is written x[n] = A*cos(omega_0*n + phi), where the symbol "
     "omega_0 is the:",
     "Angular frequency of the sequence",
     ["Amplitude of the sequence",
      "Phase offset of the sequence",
      "Sampling interval of the sequence"]),

    ("For a complex exponential sequence, the real part sigma_0 of the exponent controls the "
     "amplitude so that the real sinusoidal parts are:",
     "Constant when sigma_0 = 0, growing when sigma_0 > 0, and decaying when sigma_0 < 0",
     ["Constant when sigma_0 > 0, and growing when sigma_0 turns out to equal zero",
      "Growing whenever sigma_0 is less than zero, for any amplitude",
      "Held at zero unless sigma_0 turns out to equal exactly one"]),

    ("A sinusoidal sequence A*cos(omega_0*n + phi) is periodic only when:",
     "omega_0*N = 2*pi*r for positive integers N and r",
     ["omega_0 is any real number that is greater than zero",
      "omega_0 equals the sampling frequency of the sequence exactly",
      "N is chosen freely as any convenient non-integer value"]),

    ("For a periodic sequence, the fundamental period N is:",
     "The smallest value of N satisfying omega_0*N = 2*pi*r",
     ["The largest value of N that satisfies the periodicity condition",
      "Any value of N for which omega_0*N is a whole integer",
      "A value equal to the amplitude A of the sinusoidal sequence"]),

    ("The sampling theorem (Nyquist theorem) states that a continuous signal can be "
     "represented uniquely by its samples if the sampling frequency is:",
     "Greater than twice the highest frequency contained in the signal",
     ["Equal to the highest frequency that is contained in the signal",
      "Less than half of the highest frequency present in the signal",
      "Set independently of which frequencies are present in the signal"]),

    ("The specific problem that the sampling theorem is meant to prevent is:",
     "Aliasing, which occurs when the sampling frequency is too low",
     ["Quantization error, which grows when too few bits are used",
      "Truncation, which cuts the sequence down to a finite length",
      "Phase loss, which discards the timing detail of the signal"]),

    ("A discrete-time system is defined to be linear when, for x[n] = a*x1[n] + b*x2[n], the "
     "output is:",
     "y[n] = a*y1[n] + b*y2[n] for any constants a and b and any inputs",
     ["y[n] = y1[n - n0], a shifted version of one of the responses",
      "y[n] = y1[n]*y2[n], the product of the two responses formed",
      "y[n] = a*y1[n] on its own, disregarding the second input"]),

    ("A discrete-time system is shift-invariant when a shift of the input by n0, so that "
     "x[n] = x1[n - n0], produces:",
     "y[n] = y1[n - n0], the same response shifted along by n0",
     ["y[n] = y1[n], the same response with no shift applied to it",
      "y[n] = n0*y1[n], the response scaled by the factor n0",
      "y[n] = y1[-n], the response reversed about the time origin"]),

    ("A linear time-invariant (LTI) discrete-time system is one that:",
     "Satisfies both the linearity and the shift-invariance properties",
     ["Satisfies linearity but fails the shift-invariance property",
      "Satisfies shift-invariance but fails the linearity property",
      "Satisfies neither property yet remains causal in all cases"]),

    ("Why are LTI discrete-time systems emphasised so strongly in the course?",
     "They are easy to analyze, characterize and design, and support many useful algorithms",
     ["They form the sole class that is able to process periodic input sequences properly",
      "They produce an output without any impulse response being known",
      "They require the sampling rate to be altered before they are used"]),

    ("The response of a discrete-time system to a unit sample sequence delta[n] is called "
     "the:",
     "Unit impulse response, denoted h[n]",
     ["Unit step response, denoted s[n]",
      "Transfer function, denoted by H",
      "Convolution sum, denoted y[n]"]),

    ("A key consequence of the linear, time-invariant property is that an LTI discrete-time "
     "system is:",
     "Completely characterized by its impulse response",
     ["Characterized instead by its unit step response",
      "Independent of whatever input is applied to it",
      "Fully described by a single output sample value"]),

    ("Because any input can be written as a linear combination of shifted unit samples, the "
     "response of an LTI system to an input x[k]*delta[n - k] is:",
     "x[k]*h[n - k]",
     ["x[k]*delta[n - k], left unchanged by the system",
      "h[n], taken independently of the index k",
      "x[n]*h[k], with the two indices swapped over"]),

    ("The summation that combines x[n] and h[n] to give the output of an LTI system, written "
     "y[n] = x[n] * h[n], is called the:",
     "Convolution sum",
     ["Fourier series",
      "Frequency sweep",
      "Sampling sum"]),

    ("The commutative property of the convolution sum states that:",
     "x[n] * h[n] = h[n] * x[n]",
     ["x[n] * h[n] = x[n] + h[n]",
      "x[n] * h[n] = x[-n] * h[-n]",
      "x[n] * h[n] varies with the operand order"]),

    ("The distributive property of the convolution sum states that:",
     "x[n] * (h[n] + y[n]) = x[n] * h[n] + x[n] * y[n]",
     ["x[n] * (h[n] + y[n]) = x[n] * h[n] on its own",
      "x[n] * (h[n] * y[n]) = (x[n] * h[n]) * y[n]",
      "x[n] * (h[n] + y[n]) = h[n] + y[n] regardless of x"]),

    ("In the graphical interpretation of the convolution sum, the impulse response h[k] is "
     "first:",
     "Time-reversed to form h[-k], then shifted before multiplying and summing",
     ["Scaled by a fixed constant, then integrated over all of the values of k",
      "Left just as it is, then added straight onto the sequence x[k]",
      "Resampled to a higher rate, then quantized before being summed"]),

    ("If two sequences of lengths M and N are convolved, the resulting sequence has length:",
     "M + N - 1",
     ["M + N",
      "M * N",
      "the larger of M and N"]),

    ("A discrete-time LTI system is classified as a finite impulse response (FIR) system "
     "when its impulse response h[n] is:",
     "Of finite length",
     ["Of infinite length",
      "Equal to the unit step sequence",
      "Undefined for negative values of n"]),

    ("A discrete-time LTI system is classified as an infinite impulse response (IIR) system "
     "when its impulse response is:",
     "Of infinite length",
     ["Of finite length",
      "Zero outside one single sample",
      "Identical to its own input sequence"]),

    ("The IIR systems studied in this course are characterized mathematically by:",
     "Linear constant-coefficient difference equations",
     ["Finite sums of products with no feedback path",
      "A single scalar-multiplication operation",
      "The Fourier series of a periodic signal"]),

    ("The discrete-time accumulator defined by y[n] = y[n - 1] + x[n] is given as an example "
     "of:",
     "An IIR system, since its impulse response is of infinite length",
     ["An FIR system, since it uses present and past inputs only",
      "A non-linear system, since it adds two signals together",
      "A time-varying system, since its coefficients change over time"]),

    ("A discrete-time system is called non-recursive when its output can be computed:",
     "From just the present and past input samples",
     ["Using past output samples along with the inputs",
      "Without knowing any of the input samples at all",
      "Once the whole input sequence has been received"]),

    ("A discrete-time system is called recursive when its output computation:",
     "Involves past output samples besides present and past inputs",
     ["Uses just the single present input sample each time",
      "Uses present and past input samples but no outputs",
      "Leaves out all the earlier values of the input and the output"]),

    ("The response of a discrete-time system to a unit step sequence is called the:",
     "Unit step response, denoted s[n]",
     ["Unit impulse response, denoted h[n]",
      "Convolution sum, denoted y[n]",
      "Transfer function, denoted H[n]"]),

    ("An arbitrary discrete-time sequence can be represented in the time domain as:",
     "A weighted sum of a basic sequence and its shifted versions",
     ["A single scaled copy of the unit step sequence in time",
      "The product of two sinusoidal sequences of different rates",
      "A constant term plus one single decaying exponential term"]),

    ("For a complex exponential sequence written A*alpha^n, the symbols A and alpha are, in "
     "general:",
     "Real or complex numbers",
     ["Strictly positive integers",
      "Numbers equal to one another",
      "Values between zero and one"]),
]

# All questions are compiled, in thematic order, into a single bank.
ALL_QUESTIONS = SET1 + SET2 + SET3 + SET4
OUTPUT_FILE = "compiled.json"


def build_options(distractors, correct, position):
    """Insert `correct` at `position` among the (ordered) distractors."""
    opts = list(distractors)
    opts.insert(position, correct)
    return opts


def main():
    rng = random.Random(454)  # reproducible key placement
    n = len(ALL_QUESTIONS)

    # Balanced key positions: as close to 25 / 25 / 25 / 25 as the count allows.
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
