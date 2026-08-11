---
title: Pointer's Gamut
sequence: 12
---
![[images/ChatGPT Image Aug 6, 2026, 02_48_23 PM.png]]

**Scope:** Analyzes Pointer's Gamut of real surface colors.

**Michael R. Pointer**, a prominent figure in color science, published a landmark study in **1980** titled *"The Gamut of Real Surface Colours"*, defining the practical limits of color as it exists in the physical world, distinct from theoretical or mathematical ideals.

- **Experimental method and sample size:** Pointer compiled a database by measuring the spectral reflectance of **over 4,000 real-world objects and surfaces**, including **paints, inks, textiles, plastics, minerals, and flowers**. These real-world reflectances established the empirical boundary of what the human eye can actually see when viewing non-luminous, non-fluorescent surfaces.

### Definition and Standard Viewing Conditions

**Pointer's Gamut** is the total range of chromaticities producible by real-world reflecting surfaces:

- **Illuminant assumptions:** the original 1980 calculations were performed under **CIE Illuminant C**, the standard of the time for approximating average daylight.
- **Standardization:** the gamut provides a standardized coordinate set (often visualized in CIE xy or CIELAB space) establishing the maximum saturation achievable for any given hue at any given lightness level with real pigments and materials.

### Shape of the Gamut: The Luminosity Asymmetry

The most striking characteristic of Pointer's Gamut is that it is **highly irregular and lopsided** — not a perfect circle or sphere, but a complex solid favoring specific hue regions:

- **Peak chroma in green-yellow:** the gamut reaches its maximum chroma in the **green and green-yellow region** (h_ab ≈ 150°), and secondarily in the **orange region** (h_ab ≈ 20°).
- **Limited chroma in red and blue:** maximum achievable chroma for red and blue-violet hues is significantly lower than for greens.
- **The V(λ) connection:** this lopsidedness is a direct consequence of the human **luminosity function V(λ)**, which peaks at **555 nm** in the green-yellow region. Green surfaces reflect where the eye is most sensitive, so they can be both very light (high value/luminance) and very saturated at once. Red pigments must reflect light above 600 nm, where sensitivity is low; making a red "lighter" requires adding other wavelengths (green or blue), which inevitably **desaturates the hue**.

### Comparison with Other Gamuts

Pointer's data serves as a reality check against theoretical boundaries and device capabilities:

- **MacAdam Limits (optimal colors):** the **theoretical maximum** for material colors, assuming perfect "0 or 1" reflectance spectra. Though the MacAdam limits also show a green-yellow asymmetry, Pointer's Gamut is a **smaller, realistic subset** of this theoretical space.
- **Spectral locus:** the absolute boundary of all visible color (pure monochromatic light). Pointer's Gamut is much smaller, because real surfaces always reflect a broad band of wavelengths rather than a single pure frequency.
- **Device gamuts (displays/printers):** standard displays (like sRGB) often fail to cover significant portions of Pointer's Gamut, particularly in the **saturated cyan, green, and yellow-green** regions. For professional imaging, reproducing all Pointer colors is the benchmark of "high fidelity."

### Practical Importance in Industry

Pointer's Gamut is a critical benchmark for manufacturers and imaging professionals:

- **Manufacturer benchmarking:** display and printer manufacturers cite their performance as e.g. "this monitor covers 98% of Pointer's Gamut" — a more meaningful measure of real-world performance than a percentage of a triangular RGB space.
- **Gamut mapping:** when converting between devices (e.g., wide-gamut camera to printer), **gamut mapping** algorithms use Pointer's data to shift out-of-gamut colors while preserving the perceptual relationships that exist in nature.

### Limitations and Caveats

The Pointer data has specific constraints:

- **Non-fluorescent materials:** the gamut covers only colors from simple reflection and absorption. **Fluorescent materials** can "cheat" the MacAdam limits by converting UV light into visible light, appearing brighter and more saturated than Pointer's Gamut suggests possible.
- **Surface finish:** the data is generally based on diffuse reflectance. **Glossiness** or texture significantly alters perceived chroma and lightness — a glossy surface often appears more chromatic than a matte version of the same color.
- **Database evolution:** recent efforts, such as the **ISO Reference Colour Gamut**, use larger databases (up to **85,879 spectra**) to refine Pointer's original work, while confirming the fundamental "green-favored" asymmetry he first identified.

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