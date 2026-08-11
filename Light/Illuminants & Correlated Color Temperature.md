---
title: Illuminants & Correlated Color Temperature
sequence: 25
---
![[Pasted image 20260811113607.png]]

**Scope:** Standardized mathematical descriptions of light sources — the CIE illuminants — and the blackbody/correlated-color-temperature scale that characterizes them.

### Sources vs. Illuminants

Colorimetry distinguishes the **physical light source** from the **illuminant**: a source is a tangible object that emits radiant energy (a tungsten bulb, a candle, the sun); "an **illuminant** is a **mathematical description** of a light source," defined by its spectral power distribution (SPD), and "may describe light sources that do not actually exist in the laboratory" (*The Measurement of Colour*). Illuminants exist to predict, in colorimetric calculations, "how a surface color will appear under specific conditions" (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*).

### The CIE Standard Illuminants

The CIE standardized a set of illuminants for reproducible color measurement (*A Comprehensive Overview...*, *Color Management: A Comprehensive Guide*, *Contemporary Color*):

- **A — incandescent/tungsten, ≈ 2854–2856 K:** physically a Planckian radiator; "high in long-wavelength (red) energy and low in blue."
- **B and C — filtered daylight:** liquid filters placed in front of source A. **C (≈ 6,774 K)** was "an early attempt to approximate average daylight" but "lacks the ultraviolet (UV) content of real daylight."
- **D series — measured daylight:** built from measurements of real daylight, including significant UV energy. **D50 (5,000 K)** is the U.S. graphic-arts standard, "favored for its relatively flat SPD"; **D65 (6,500 K)** "represents average daylight and is the most widely used daylight illuminant"; **D75 (7,500 K)** approximates indoor north-sky daylight, "preferred by many professional color matchers."
- **F series — fluorescent:** SPDs of real fluorescent lamps; **F2 (≈ 4,100 K)** represents the common cool-white office lamp.

### Blackbodies and the Temperature Scale of Light

The temperature scale for light is defined by the **blackbody (full radiator)** — a theoretical object (often simulated in the laboratory by a block of carbon) "that absorbs all incident radiation and changes color predictably as it is heated" (*A Comprehensive Overview...*).

- **Planck's distribution** gives the energy emitted at each wavelength for a given temperature (*Color for Science, Art, and Technology*).
- **Wien's law** links temperature to peak wavelength: **λm = 2,897/T** (λm in µm, T in Kelvin) (*Color for Science, Art, and Technology*).
- The visible progression with heat: **black → red (~1,000 K) → yellow (~2,500 K) → white (~4,500 K) → bluish-white (above 6,500 K)** (*A Comprehensive Overview...*).

### CCT and Its Values in the World

**Correlated color temperature (CCT)** describes lights that are *not* true blackbodies (e.g., fluorescents): it is "the temperature of the full radiator whose color is closest to that of the light source" (*A Comprehensive Overview...*). Practical values from the sources:

| Light | CCT |
|---|---|
| Candle flame | ~1,900 K |
| Sunrise / sunset | ~2,000 K (reddest daylight) |
| Household tungsten | ~2,850 K |
| Direct noon sun | ~4,800–5,500 K |
| Average daylight (D65) | 6,500 K |
| Overcast sky | >10,000 K |
| Clear bright blue sky | 12,000 K or higher |

(*A Comprehensive Overview..., The Science of Paintings, Color for Science, Art, and Technology, Vision Science: Photons to Phenomenology*)

### The Daylight Locus

Daylight is not a single illuminant: "its spectral character changes constantly due to atmospheric filtering, time of day, and weather" (*Contemporary Color*). The **daylight locus** is the path on a chromaticity diagram that all variations of natural daylight follow (*A Comprehensive Overview...*). Remarkably, "the human blue–yellow opponent channel appears to have evolved to coincide with this locus," solving much of color constancy — "allowing surfaces to look consistent even as the daylight shifts from yellow sun to blue sky" (*Vision Science: Photons to Phenomenology*, see [[Illuminants & Correlated Color Temperature|CCT]] and the [[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing|color constancy]] page).

### Chromatic Adaptation and Color Rendering

The eye–brain system uses **chromatic adaptation** to keep whites white: "the brain compensates for the shift in illumination by adjusting the sensitivity of the cone receptors," which is why white paper looks white both under a yellow tungsten bulb and in blue daylight (*Illusions of Seeing*, *A Comprehensive Overview...*). But adaptation only fixes the white point:

- A lamp's **Color Rendering Index (CRI)** "measures how well the lamp reveals the colors of objects compared to a standard illuminant"; CRI of **at least 90** is recommended for accurate color viewing (*Contemporary Color*).
- "If an illuminant lacks certain wavelengths (as many cheap fluorescents do), even perfect adaptation cannot recover the 'missing' colors of the objects" (*Contemporary Color*, *A Comprehensive Overview...*).

## Handprint Perspectives

MacEvoy's essentials of the blackbody locus: (1) the curve is closest to the equal-energy white point at ~**5,800 K**; (2) above ~5,000 K it is nearly straight, "aligned from blue to yellow (approximately from 470 nm to 575 nm)"; (3) below 4,000 K it "arcs sharply into orange and red, and becomes much more saturated"; (4) blackbody radiation never reaches violet or purple — "at an infinitely high temperature, the blackbody chromaticity has a dominant wavelength of about 470 nm." He also explains why a warm 120-watt incandescent bulb at ~2,860 K can still rate **CRI 100**: because it approximates a high-temperature blackbody, it emits "across the entire spectral range without spikes or gaps," and chromatic adaptation preserves the perception of white — "that adaptation is the origin and principal basis of our warm/cool color sensitivity." For painters this matters: the illuminant's color temperature shifts the whole gamut of reflected paint colors (see [[Natural Light Gamut vs. Pigment Gamut - Metamerism]]) *(Source: [[raw_sources/handprint/color12.md|color12.html]])*.

## Subtopics
- Source vs. illuminant: physical object vs. mathematical SPD used in colorimetric prediction
- CIE standards: A (2854–2856 K), B/C (6,774 K, UV-deficient), D50/D65/D75, F2 fluorescent (4,100 K)
- Blackbody physics: Planck's distribution, Wien λm = 2,897/T, the red→white→bluish heat progression
- CCT as closest-matching full-radiator temperature; real-world table (candle 1,900 K → blue sky 12,000 K+)
- Daylight locus and its evolutionary alignment with the blue–yellow opponent channel
- Chromatic adaptation (white stays white) vs. CRI (≥90) and unrecoverable missing wavelengths

## Cross-References
- [[Wave Nature]] — SPDs as the multi-wavelength description illuminants capture
- [[The Visible Spectrum]] — the 380–780 nm band illuminants span
- [[Natural Daylight Variation & Hyperspectral Scene Data]] — why daylight is a locus, not a point
- [[CIE Systems]] — illuminants as inputs to tristimulus calculation
- [[Spectral Locus & Excitation Purity]] — the white point anchoring purity
- [[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing]] — chromatic adaptation in practice

## Sources
* "The Measurement of Colour" — R.W.G. Hunt
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management: A Comprehensive Guide for Graphic Designers" — John T. Drew and Sarah A. Meyer
* "Contemporary Color: Theory and Use" — Steven Bleicher
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "Color for Science, Art, and Technology" — Kurt Nassau (editor)
* "Vision Science: Photons to Phenomenology" — Stephen E. Palmer
* "Illusions of Seeing" — Thomas Ditzinger