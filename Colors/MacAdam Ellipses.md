---
title: MacAdam Ellipses
sequence: 10
---
![[images/ChatGPT Image Aug 6, 2026, 02_29_42 PM.png]]

**Scope:** How big a color difference has to be before a person actually notices it — and why that threshold is wildly different depending on which color you're looking at.

Human color discrimination is **highly uneven** across the visible spectrum. The clearest picture of that unevenness is the **MacAdam ellipse**: a region around a color inside which everything looks identical to that color. Draw enough of these regions and you see exactly where the eye is sharp — and where it's indifferent.

### 1. The 1942 experiments

In **1942**, David MacAdam published a landmark study in the *Journal of the Optical Society of America* on **just-noticeable differences (JNDs)** of color:

- **The setup:** a specialized **colorimeter** showed a split circular field. One half displayed a fixed "test" color; the observer adjusted the other half until it matched.
- **Measuring the spread:** rather than averaging the "correct" match, MacAdam measured the **standard deviation of the matching errors** across **25 different target colors**. Because matching is never perfect (the eye has built-in noise), the range of coordinates an observer accepted as a match defined the threshold of noticeable difference around each color.
- **The ellipse appears:** when these match-regions were plotted on the **CIE 1931 xy diagram**, they came out as ellipses — every point on an ellipse's edge is about one JND away from its center color.

### 2. Ellipses that vary wildly in size and angle

The key discovery: sensitivity to color change is **drastically uneven** across the diagram:

- **Size range:** roughly a **10:1 ratio** separates the largest ellipses from the smallest. *(Note: the notebook sources also demonstrate this unevenness with Munsell plots, where distances vary by a factor of ~3.86×.)*
- **Big in green, tiny in blue-violet:** the ellipses are **largest in the green region** — the eye is relatively insensitive there, so colors must drift far apart before a difference is noticed. They are **smallest in the blue-violet region**, where the visual system is extremely sensitive to minute changes.
- **Orientation:** the ellipses **"rotate"** as they move around the diagram, their long axes pointing generally toward the red and blue corners — a signature of the underlying biology of the L, M, and S cones.

### 3. JND steps and digital "banding"

The ellipses reveal the sampling limit of human vision — with direct consequences for digital images:

- **Crossing the spectrum:** it takes roughly **150 to 300 JND steps** (order of magnitude) to walk across the whole spectrum in terms of hue.
- **8-bit banding:** 8-bit quantization (256 levels per channel) often makes steps **bigger than one MacAdam ellipse**, producing visible **"banding"** artifacts — smooth gradients breaking into stripes.
- **The 10-bit fix:** though a 24-bit system theoretically offers 16.7 million colors, the eye can only tell apart about **1.4 million** within a standard display gamut. To keep the steps completely invisible everywhere (especially in the ultra-sensitive blues), you need at least **10-bit quantization (1,024 levels)**.

### 4. Why this pushed color science to "warp" the map

MacAdam's work was the main reason color science built **perceptually uniform spaces** — maps warped so that every JND region becomes a perfect, equal-sized circle:

- **CIELAB and CIELUV (1976):** introduced by the CIE as a more honest "color difference ruler."
- **MacAdam's own attempt:** before 1976, MacAdam proposed the **CIE 1960 UCS (Uniform Chromaticity Scale)** with u, v coordinates designed to linearize visual distances.
- **ΔE:** in uniform spaces, the distance between two colors — **ΔE** — quantifies the perceived difference, with **1.0** usually taken as about one JND.

### 5. The Munsell connection

The Munsell system (1905) was the first major attempt to order color by visual judgment:

- **The comparison:** a circle of constant Munsell chroma plotted on the xy diagram becomes a highly distorted, elongated oval. Between the green-yellow and purple-blue regions, the same *perceived* step is **3.86 times larger** in distance on the diagram.
- **Renotation (1943):** MacAdam's insights anchored the Munsell system to precise CIE coordinates, making its visual spacing scientifically rigorous.

### 6. What this tells us about human vision (and industry)

MacAdam's ellipses expose the functional architecture of the eye:

- **Where we're sharp:** discrimination is **finest near 495 nm (blue-green) and 590 nm (yellow-orange)** and **worst in the deep greens** — an evolutionarily sensible arrangement, since those fine regions are where we identify natural resources and read changes in daylight.
- **What industry does with it:** these thresholds underlie quality control in the **textile, paint, and plastics** industries. Because inspectors are "least tolerant of hue differences" compared with lightness or vividness, industrial tolerances are often drawn as elongated **acceptability ellipsoids** in CIELAB space — a direct echo of MacAdam's original findings.

## Handprint Perspectives

MacEvoy's hue-circle analyses independently confirm MacAdam's pattern of discrimination. The spacing of spectral hues around the color circle shows **increased wavelength discrimination around the "yellow" and "cyan" wavelengths**, and **decreased discrimination at the spectrum ends and in the "green" wavelengths** — the same fine regions (roughly 495 nm and 590 nm) and the same insensitive green region that MacAdam's ellipses expose. He also notes the strong tinting effect of "violet" light in mixtures of red and violet hues, and points out that this scaling vindicates Newton's original hue scaling, developed with the crudest light-manipulation tools. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

## Subtopics
- JND & Color Matching
- Ellipse Size and Orientation
- Quantization Limits
- Uniform Color Spaces
- Munsell & Industry

## Cross-References
- [[CIE Systems]]
- [[Munsell Notation]]
- [[Why Lab-Munsell Were Built for Perceptual Uniformity]]
- [[Gamuts]]
- [[Color Matching Functions and the Photopic Luminosity Function]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer