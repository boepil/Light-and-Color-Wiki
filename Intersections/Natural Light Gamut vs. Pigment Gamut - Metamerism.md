---
title: Natural Light Gamut vs. Pigment Gamut - Metamerism
sequence: 75
---
![[Pasted image 20260809130521.png]]

**Scope:** Cross-cutting page (Painting ֳ— Light) comparing the range of colors in nature to those achievable with pigments, and addressing metamerism.

The relationship between the colors found in the natural world and those reproducible by artists' pigments is governed by the physics of light, the chemistry of materials, and the biological architecture of human vision. The "pigment gamut" is a restricted subset of perceptual reality, and **metamerism** explains why matches between them are often unstable.

### 1. The Natural Light Gamut vs. Artificial Gamuts

The **natural light gamut** encompasses the full range of spectral power distributions (SPDs) in the environment — direct sun and skylight, plus light reflected by foliage, water, and minerals:

- **Scale and complexity:** describing natural light physically requires specifying a value for every wavelength between 400 and 700 nm — a "state space" of potential images in nature that "boggles the mind," given the hundred million receptors in the eye and nearly continuous luminance levels.
- **Gamut hierarchy:** the human eye has the largest "color space," distinguishing approximately **7 million different color levels**. Most natural scenes do not actually contain highly saturated colors, yet their spectral diversity is immense. Device gamuts are much smaller: **sRGB** is among the smallest, **Adobe RGB** larger but still limited versus the eye's full capacity.

### 2. The Smaller Pigment Gamut: Physical Constraints

The range of colors painters can mix is compressed by physical and chemical factors that do not apply to direct light:

- **Reflectance bounds:** pigments are non-luminous; they can only reflect between **0% and 100%** of incident light — and in practice even the brightest white substrates rarely exceed **90%**.
- **The "fundamental physical bind":** increasing the lightness (value) of a pigment like red requires reflecting more wavelengths, which inevitably **desaturates** the hue; conversely, making a color "purer" requires a narrower reflectance band, which lowers total luminance.
- **Unwanted absorptions:** real pigments are "impure" — they absorb some light where they should ideally be transparent.
- **Subtractive mixing loss:** every pigment addition in subtractive mixing further "dulls" the hue and subtracts light; mixing three primaries ideally yields black, but with traditional pigments often produces a muddy "no-color" hue.

### 3. Metamerism: The Consequence of Receptor Sampling

**Metamerism** is the phenomenon where two different spectral power distributions produce the same set of three neural signals (tristimulus values) and thus look identical under a specific light source:

- **Information reduction:** color vision reduces the infinite complexity of the spectrum to just three scalar values (one per cone type — S, M, and L).
- **The cause:** the same activation pattern across the three cone types can be triggered by many physically distinct wavelength combinations. For example, a **monochromatic yellow light (580 nm)** can look identical to a **mixture of red and green light**.

### 4. Practical Consequences for Painters

Metamerism profoundly affects how art is created and displayed:

- **Illuminant metamerism:** a painting may look perfectly balanced under a studio's incandescent light but appear "falsified" or shifted in value under a gallery's skylights or fluorescent tubes.
- **Metameric pairs:** two paint patches (one a single pigment, the other a mixture) might match in daylight but show a catastrophic mismatch under tungsten light.
- **Color constancy:** the visual system uses **chromatic adaptation** to "discount" the illuminant's color, helping objects keep their perceived color across changing light. Constancy works for real objects, but a painting's color relationships can shift unintentionally if the lighting is not controlled.

### 5. Concrete Numbers in Color Discrimination

- **Distinguishable levels:** the eye resolves roughly **150 different hues**, which multiplied by intensity and brightness variations yields ~**7 million solvable color levels**.
- **Pointer's Gamut:** in 1980, Michael Pointer benchmarked "real-world" color by measuring **over 4,000 samples** of paints, textiles, and nature.
- **Reflectance databases:** modern studies use databases of **85,879 reflectance spectra**, confirming that material reality consistently favors green-yellow chroma over red due to the luminosity function peak.
- **Digital limits:** an 8-bit display theoretically offers 16.7 million code triplets, but many are not discriminable by the eye — the true number of "different colors" a screen can show is much lower.

### 6. Metamerism and Colorimetry

The **CIE XYZ system** is founded on the mathematical acceptance of metamerism:

- **Tristimulus integration:** colorimetry computes the effect of light by integrating its SPD with the **Standard Observer's** color-matching functions, reducing the full spectrum to three tristimulus values (X, Y, Z) — making metamerism a **built-in feature** of the system.
- **Spectral vs. colorimetric matching:** a **spectral match** is "non-metameric" — materials have identical absorption and match under any light source. A **colorimetric match** only guarantees identical appearance under one specific illuminant and for one specific observer. Industrial color matching therefore often must account for **observer metamerism**, since individuals have slightly different cone sensitivities.

## Handprint Perspectives

MacEvoy demonstrates the depth of the metameric problem with a conceptual experiment: take two idealized gel filters that each make white light appear yellow, and two that each make it appear orange — their subtractive mixtures can produce **yellow, orange, red, or even black or green**, depending entirely on the overlap of their transmittance profiles. His conclusion is the modern color-theory rule that **the visual color of a paint does not predict the visual color of mixtures made with it** — there can never be universal or invariable rules for subtractive mixing. In practice, regularities survive only because real colorants follow the "warm cliff" reflectance profiles typical of saturated warm pigments. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

He adds that metameric colors are **commonly grays and dull (unsaturated) hues**; extremely impoverished or monochromatic illuminants are generally required to produce metamerism among highly saturated material colors — which then all appear as bright or dark variations on a single hue. *(Source: [[raw_sources/handprint/tech13.md|tech13.html]])*

## Subtopics
- Natural Light Gamut
- Pigment Constraints
- Metamerism
- Illuminant & Observer Shifts

## Cross-References
- [[Gamuts]]
- [[Pointer's Gamut]]
- [[Optimal Color Solid-MacAdam Limits]]
- [[Color Matching Functions and the Photopic Luminosity Function]]
- [[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing]]
- [[Natural Daylight Variation & Hyperspectral Scene Data]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "Why Material Reality Favors Green Over Red: The Physical Chemistry of Chromatic Limits"