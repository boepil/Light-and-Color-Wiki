---
title: Gamuts
aliases: [Gamuts]
sequence: 11
---
![[images/ChatGPT Image Aug 6, 2026, 02_43_04 PM.png]]

**Scope:** Parent page introducing gamuts and limits of reproducible color spaces.

A **color gamut** is the total range of color a specific device — monitor, scanner, or printer — can display or reproduce. Because every medium, whether projected light or reflected pigment, has unique physical and chemical constraints, no single device can capture or recreate the full breadth of colors visible to the human eye.

### 1. Representation of Gamuts (CIE and CIELAB)

Color gamuts are mathematically visualized within standard color spaces to compare devices:

- **CIE chromaticity diagrams:** in the 1931 xy diagram, **additive display gamuts** are typically **triangles**. The apexes correspond to the coordinates of the device's red, green, and blue (RGB) primaries, and every reproducible color must lie within that triangle.
- **Irregular pigment gamuts:** unlike displays, **subtractive gamuts** (paints and inks) are **irregular and bounded by curves**, because subtractive mixing results are not simple linear combinations of coordinates but depend on complex absorption and scattering spectra.
- **CIELAB and 3D volume:** because color is three-dimensional (hue, value, chroma), a 2D diagram is often insufficient. In 3D space the pigment gamut forms an irregular **"color tree"** or lopsided solid, reflecting that different hues reach maximum saturation at different lightness levels.

### 2. The Hierarchy of Gamuts

There is a clear hierarchy from theoretical ideals to practical limitations:

- **Human vision:** the eye has the largest "color space," capable of discerning approximately **7 million different color levels**.
- **Optimal Color Solid (MacAdam Limits):** the theoretical maximum saturation for material colors — surfaces that reflect light with 0% or 100% efficiency.
- **Pointer's Gamut:** the range of **all real surface colors** (paints, textiles, flowers). Smaller than the MacAdam limits and markedly lopsided, favoring high chroma in the green-yellow region.
- **Device spaces:** standards like **Adobe RGB 1998** cover a wide range but are still smaller than the eye's capacity. The standard **sRGB** (used for the Internet) is smaller still, restricted to approximately **256 distinct hues** in 8-bit web-safe palettes.

### 3. Additive vs. Subtractive Limitations

The fundamental gamut-size difference stems from how color is produced:

- **Additive (displays):** monitors project light directly into the eye, bypassing the energy loss inherent in reflection, so displays can produce **saturated colors at high luminance**.
- **Subtractive (reflective surfaces):** pigments must absorb (subtract) light from a source. Their gamut is limited by the **luminosity function V(λ)**, which peaks in the green (555 nm). A green pigment can therefore be both light and highly saturated; a red pigment, however, must reflect wavelengths where the eye is less sensitive — to make it "lighter," other wavelengths must be added, which inevitably **desaturates the red**.
- **Unwanted absorptions:** real pigments are "impure," absorbing light in spectral regions where they should be transparent, further compressing the achievable gamut of mixed colors.

### 4. Physical Gamut Boundaries

- **The spectral locus:** the curved, horseshoe-shaped boundary of the CIE diagram represents **monochromatic light** (pure spectral hues) — the absolute physical limit of all real colors.
- **The line of purples:** the dashed straight line connecting the 380 nm (violet) and 700 nm (red) endpoints represents non-spectral purples and magentas, created only by mixing red and blue light; they do not exist as single wavelengths.
- **The monochromatic limit:** no real-world device can reproduce pure monochromatic light across the entire spectrum, because its primary light sources or pigments are **broadband** — they emit or reflect a range of wavelengths rather than a single "pure" ray.

### 5. Practical Consequences and Gamut Mapping

When a color from one device must be reproduced on another with a smaller gamut (e.g., monitor to printer):

- **Out-of-gamut colors:** colors that exist in the original image but cannot be physically reproduced by the target device.
- **Clipping:** if out-of-gamut values are simply set to the device's maximum (e.g., any value > 255 becomes 255), **detail is lost** in the saturated regions.
- **Gamut mapping and compression:** software substitutes the "nearest" reproducible hue for out-of-gamut colors, or **compresses the entire gamut** to preserve perceptual relationships between colors.
- **The matching challenge:** matching colors across devices is difficult because each hardware component uses different color models and phosphors/inks, requiring **ICC profiles** to translate between them.

### 6. Human Discrimination vs. Device Quantization

The limits of the human eye dictate the requirements of digital color technology:

- **Distinguishable colors:** while a 24-bit system theoretically produces 16.7 million colors, the eye can distinguish only about **1.4 million unique colors** within the gamut of a standard HDTV.
- **Geometry of gamuts:** additive gamuts are **triangular** because they rely on three discrete primaries. The **Pointer gamut** of real surface colors is **irregular** because of the visual system's evolutionary tuning: the eye is far more sensitive to changes in the green-yellow region, where natural reflectances (like vegetation) are most abundant, producing a surface-color gamut much larger in the green region than in the red.

## Handprint Perspectives

MacEvoy uses CIELAB (or CIECAM) as the objective frame of reference for judging the shape and size of gamuts: the CIE color models enclose the space of all possible colors, and spectrophotometric measurement locates each colorant inside it. Comparing the "millions of colors" Apple RGB monitor gamut with the 256-color "web safe" gamut and the CMYK printing gamut, he notes the range of purples, reds, and greens available on a monitor but **unmixable in CMYK** — because monitor colors are made of tiny colored lights, they achieve greater luminance contrasts and higher saturation than reflective prints.

He also stresses that a gamut is **always three-dimensional and context-sensitive**: the gamut of a television shrinks when sunlight falls on the screen, just as a printer's gamut shrinks on gray paper, with coarse halftones, or in dim viewing light. *(Source: [[raw_sources/handprint/color13.md|color13.html]])*

## HueValueChroma Perspectives

Briggs connects the gamut concept to its own history and to the arithmetic that makes paint gamuts behave the way they do:

- **"Gamut" thinking is older than colorimetry.** Robert Boyle (1664), the writer who introduced the term "primary colour" in English, "shows an awareness of the concept of a *gamut*": the primaries suffice to mix a full range of hues, "but some colours will, by their greater 'splendor' (we would say *chroma*), lie outside this gamut." The mismatch of range vs. top-chroma — the core of the page's hierarchy — was thus noted at the very origin of primary-color language *(Source: [[raw_sources/huevaluechroma/062.md|062.html]])*.
- **The paint gamut is computed by multiplication, not addition.** Subtractive results "are calculated by multiplying together the percentage of light energy passed on by both colourants, for each wavelength," which is why the page's pigment gamuts are "irregular and bounded by curves": shape is set wavelength-by-wavelength by the overlap of reflectance curves, not by three primary coordinates. And metamerism means "the **exact** results of subtractive mixing of real colourants can not be predicted merely from their colour" — though "all common cyan and yellow colourants combined subtractively will make a green" *(Source: [[raw_sources/huevaluechroma/051.md|051.html]])*.
- **The lop-sidedness is shared with nature, so it is not a defect.** The paint gamut's bulge between orange-yellow and orange-red (16 Munsell units maximum chroma) against its cyan-green trough (10 units) "does not really present a problem because the range of common object colours is restricted in essentially the same way, for the same combination of physical and physiological reasons." What is a defect — and entirely avoidable — is shrinking the gamut by using a psychologically-pure RYB trio: "if the red paint is a *psychologically* pure red... it is found to be impossible to mix purples above a very low chroma," a problem printers solved with the **YMC subtractive primaries** while many traditional teachers still escape it via the "split-primary" palette, whose recurring rationale Briggs judges "entirely discredited" *(Source: [[raw_sources/huevaluechroma/015.md|015.html]], [[raw_sources/huevaluechroma/062.md|062.html]])*.
- **Digital "subtractive" mixing is an idealization that can leave the real gamut.** Multiply-mode blending in graphics programs "gives a realistic representation of what subtractive mixing involving comparably coloured lights and materials **might** result in," but "unrealistic effects may result from subtractively mixing very bright and/or very saturated digital colours that are outside the range of real object colours." Even Painter — which simulates the appearance and behavior of paints — "nevertheless" mixes by ideal subtractive rules: "Monitor yellow" and "Monitor blue" mix to black or grey, "while paints of similar hues would mix to a dull green" *(Source: [[raw_sources/huevaluechroma/051.md|051.html]])*.
- **Where screen gamuts beat paints and where they lose.** Digital full-chroma colors reach "Munsell chromas of **24 in the violet-blue to magenta range, down to 18 at red**" — far past paints — "while artist's paints... exceed the gamut of standard (sRGB) digital colours where these are relatively poor in the vicinity of yellow and cyan" *(Source: [[raw_sources/huevaluechroma/015.md|015.html]], [[raw_sources/huevaluechroma/045.md|045.html]])*.

## Subtopics
- Gamut Representation
- Gamut Hierarchy
- Additive vs Subtractive
- Gamut Mapping
- Boyle 1664 and the origin of "gamut" thinking; the multiplicative, metamerism-bound paint gamut (Briggs)
- Shared lop-sidedness with common object colors; ideal-subtractive digital mixing vs real paint mixtures (Briggs)

## Cross-References
- [[Device Gamuts]]
- [[Pointer's Gamut]]
- [[Optimal Color Solid-MacAdam Limits]]
- [[CIE Systems]]
- [[MacAdam Ellipses]]
- [[Natural Light Gamut vs. Pigment Gamut - Metamerism]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Dimensions of Colour : chroma" — [[raw_sources/huevaluechroma/015.md|015.html]]
* "The Dimensions of Colour : additive mixing" — [[raw_sources/huevaluechroma/045.md|045.html]]
* "The Dimensions of Colour : subtractive mixing" — [[raw_sources/huevaluechroma/051.md|051.html]]
* "The Dimensions of Colour : primary colours" — [[raw_sources/huevaluechroma/062.md|062.html]]