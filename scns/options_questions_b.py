# -*- coding: utf-8 -*-
"""Rebalanced option sets for deck_questions_b.py, questions 150 to 160 only.

Questions below 150 are left untouched. Apply with an explicit offset, since a
partial range cannot be inferred:

    python3 rebalance_options.py deck_questions_b.py --offset 80 --apply

REPLACEMENTS[question_number] = (correct, [d1, d2, d3])
"""

REPLACEMENTS = {

    # ---- Deck 15: Doppler shift estimation (last question only) ----
    150: ("Cross-correlation on the cyclic prefix, which is already being transmitted",
          ["The Release 17 GNSS method, which needs a fairly minimal pilot overhead",
           "Multi-frequency pilots, which are carried on the DM-RS resources",
           "Kalman filter tracking, which needs no GNSS seed whatsoever"]),

    # ---- Deck 16: network slicing ----
    151: ("Several virtual networks over one shared physical network, tuned end to end",
          ["Dividing the satellite footprint into a set of smaller geographic cells",
           "Splitting the available frequency band into fixed sub-bands per operator",
           "Separating the control plane from the user plane within the core network"]),

    152: ("SST 1 eMBB wide bandwidth, SST 2 URLLC priority queueing, SST 3 mMTC small packets",
          ["SST 1 URLLC low latency, SST 2 mMTC tiny packets, SST 3 eMBB wide bandwidth pipe",
           "SST 1 mMTC small packets, SST 2 eMBB wide bandwidth, SST 3 URLLC low latency",
           "SST 1 eMBB wide bandwidth, SST 2 mMTC small packets, SST 3 URLLC low latency"]),

    153: ("A one millisecond low-latency guarantee cannot be honoured at all",
          ["The broadband slice is unable to reach its stated throughput target",
           "The machine-type slice cannot support enough simultaneous devices",
           "The slice identifier cannot be carried within the packet header"]),

    154: ("One payload and one spectrum pool are shared, so isolation stays logical",
          ["Standards forbid physical isolation from being used in non-terrestrial systems",
           "The slice identifier is stripped as traffic crosses the feeder link",
           "Satellites are unable to run virtualisation software while in orbit"]),

    155: ("A beam is visible for minutes, so the slice re-anchors to a new satellite",
          ["User devices move between the cells faster than a slice can be reconfigured",
           "The slice identifier changes each time the satellite switches its beam",
           "The cell footprint shrinks as the satellite approaches the horizon line"]),

    156: ("Feeder switchover and inter-satellite re-routing change the path mid-session",
          ["The constellation gains and loses satellites while it is in operation",
           "The user device keeps switching between terrestrial and satellite access types",
           "Core network functions migrate between one data centre and another"]),

    157: ("The radio subnet manager, covering the beam and the scheduler",
          ["The customer-facing manager, which captures the customer intent",
           "The end-to-end slice manager, which spans the whole network",
           "The core and transport subnet manager, covering both of those"]),

    158: ("Policy follows ephemeris and handover timing, not a static cell plan",
          ["Slices are allocated according to the altitude of the serving satellite",
           "Each orbital plane in the constellation is given its own dedicated slice",
           "The orchestrator itself runs aboard the satellite rather than on ground"]),

    159: ("Capacity fenced off for an idle slice is wasted on a limited payload",
          ["Slice headers and per-slice buffering inflate packets on a long link",
           "Agreements must be recomputed at each handover and feeder switchover",
           "A regenerative core function per slice makes heat the platform cannot shed"]),

    160: ("Isolation costs capacity and signalling on a power and delay limited link",
          ["Slicing requires a larger constellation to deliver equivalent coverage",
           "Slicing pushes user traffic through the ground core rather than onboard",
           "Slicing rules out the use of regenerative payloads across the constellation"]),
}
