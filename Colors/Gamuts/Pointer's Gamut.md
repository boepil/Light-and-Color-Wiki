---
title: Pointer's Gamut
sequence: 13
---
![[images/ChatGPT Image Aug 6, 2026, 02_48_23 PM.png]]

**Scope:** The real-world record of color — the most vivid colors ever measured on actual objects, why they fall short of the theoretical ceiling, and how that matters for screens and printers.

In **1980**, the color scientist **Michael R. Pointer** published a landmark study, *"The Gamut of Real Surface Colours"*, that mapped the practical limits of color as it actually exists in the physical world — as opposed to theoretical or mathematical ideals. He measured the spectral reflectance of **over 4,000 real objects and surfaces**: paints, inks, textiles, plastics, minerals and flowers. Their real-world reflectances drew the empirical boundary of what the eye can see on a non-luminous, non-fluorescent surface.

### What it is, and how it was measured

**Pointer's Gamut** is the total range of colors that real, light-reflecting surfaces can actually produce:

- **The lighting used:** the 1980 calculations assumed **CIE Illuminant C**, the standard of the time for approximating average daylight.
- **What it gives us:** a standardized set of color coordinates showing the **maximum vividness achievable for any hue at any lightness level** with real pigments and materials.

### Why its shape is lopsided

Pointer's Gamut is strikingly **irregular and lopsided** — not a circle or sphere, but a lumpy solid that favors certain hue regions:

- **Strongest in green-yellow:** it reaches peak vividness in the **green and green-yellow region** (hue angle ≈ 150°), with a secondary peak in the **orange region** (≈ 20°).
- **Weak in red and blue:** the maximum vividness for red and blue-violet hues is considerably lower than for greens.
- **The reason is your eye, not the paint:** the lopsidedness is a direct consequence of the human **luminosity function V(λ)**, which peaks at **555 nm** in the green-yellow region. Green surfaces reflect light where your eye is most sensitive, so a green can be **very light and very vivid at the same time**. Red pigments must reflect light above 600 nm, where sensitivity is low — so making a red "lighter" requires adding other wavelengths (green or blue), which inevitably **drains the red's vividness**.

### How it compares with other gamuts

Pointer's data serves as the reality check against both theory and hardware:

- **vs. the MacAdam limits (optimal colors):** the **theoretical maximum** for material colors, assuming perfectly "0 or 1" reflecting surfaces. Pointer's Gamut is a **smaller, realistic subset** of that theoretical space — real surfaces can never quite reach the ideal.
- **vs. the spectral locus (the rainbow):** the absolute outer boundary of all visible color. Pointer's Gamut is much smaller, because real surfaces always reflect a broad band of wavelengths, never a single pure frequency.
- **vs. devices:** standard displays like sRGB often **fail to cover significant parts of Pointer's Gamut** — especially the saturated cyan, green and yellow-green regions. In professional imaging, reproducing all of Pointer's colors is the benchmark of "high fidelity."

### Why industry cares

Pointer's Gamut is a standard measuring stick for manufacturers and imaging professionals:

- **Manufacturer claims:** a display maker can honestly say "this monitor covers **98% of Pointer's Gamut**" — a far more meaningful real-world measure than a percentage of an abstract RGB triangle.
- **Gamut mapping:** when converting between devices (a wide-gamut camera to a printer, say), **gamut mapping** algorithms use Pointer's data to shift out-of-gamut colors while preserving the perceptual relationships that exist in nature.

### Limitations and caveats

The Pointer data has real constraints:

- **No glowing colors allowed:** it covers only simple reflection and absorption. **Fluorescent materials** "cheat" the MacAdam limits by converting ultraviolet light into visible light, appearing brighter and more vivid than Pointer's Gamut suggests is possible.
- **Surface finish matters:** the data assumes diffuse (matte) reflection. **Glossiness** or texture changes perceived vividness and lightness — a glossy version of a color usually looks more vivid than a matte one.
- **The database keeps growing:** recent efforts like the **ISO Reference Colour Gamut** use far larger databases (up to **85,879 spectra**) to refine Pointer's original work — while confirming the "green-favored" asymmetry he first identified.

## Handprint Perspectives

MacEvoy explains why real surfaces fall short of theoretical ideals: physical surfaces **never completely absorb or reflect all the light at each wavelength** — they channel some luminance into invisible infrared wavelengths and scatter some as diffuse "white" light, producing rounded, darker reflectance profiles. They are therefore **inherently duller than optimal colors of the same hue and lightness**, with a more restricted lightness range — exactly the gap between the MacAdam limits and Pointer's Gamut of real pigments. *(Source: [[raw_sources/handprint/tech13.md|tech13.html]])*

He defines **optimal colors** as those with the highest hue purity possible for a non-fluorescent surface color of a given hue and lightness — and notes we commonly see colors comparable to optimal colors in saturated surfaces under moderate illuminance contrast. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

## Subtopics
- The 1980 Study
- Gamut Shape & V(λ)
- Gamut Comparisons
- Industry Benchmarking

## Cross-References
- [[Optimal Color Solid-MacAdam Limits]]
- [[Gamuts]]
- [[Device Gamuts]]
- [[Natural Light Gamut vs. Pigment Gamut - Metamerism]]
- [[MacAdam Ellipses]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer