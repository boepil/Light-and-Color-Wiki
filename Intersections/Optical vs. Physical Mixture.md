---
title: Optical vs. Physical Mixture
sequence: 84
---![[Pasted image 20260809183825.png]]

**Scope:** The distinction between visual/optical mixing (additive) and physical paint mixing (subtractive), specifically addressing the complementary color and primary color fallacies.

In color science and art, the method by which color stimuli are combined significantly alters the resulting visual experience. The two primary categories of mixture are **physical (subtractive)** — the blending of matter — and **optical (additive)** — the combination of light stimuli within the human visual system.

### 1. Definitions: Physical vs. Optical Mixture

- **Physical (subtractive) mixture:** pigments, dyes, or inks are mechanically blended on a palette or layered as filters. The resulting color is determined by the wavelengths that remain after others have been **absorbed (subtracted)** by the material.
- **Optical (visual) mixture:** discrete patches of color are placed so closely together that the eye and brain cannot resolve them individually, merging them into a single hue.
  - **Examples:** this principle underlies **[[Neo-Impressionism-Pointillism|pointillism]]** in painting, **halftone dot screens** in printing, and the **RGB pixels** of digital monitors and televisions.

### 2. Laws of Mixing: Additive vs. Subtractive

- **Additive mixing (light):** superimposition of light rays. Per **Grassmann's laws** (reflected in the linear nature of color space), intensities add up, making the result **lighter** than any component. Mixing the three additive primaries — **Red (≈613 nm), Green (≈542 nm), Blue (≈457 nm)** — at full intensity yields white light.
- **Subtractive mixing (matter):** selective removal of wavelengths through absorption and scattering. Each added pigment subtracts more light, making the result **darker** and more "broken." The ideal subtractive primaries are **Cyan, Magenta, and Yellow (CMY)**, which ideally yield black when combined.

### 3. Asymmetry and the Primary Color Fallacies

Physical mixing is not a simple mathematical inverse of additive mixing, due to the complex spectral behavior of matter:

- **The RYB fallacy:** traditional art education teaches Red, Yellow, and Blue (RYB) as the primary colors, but modern science identifies them as non-optimal subtractive approximations. A red pigment already reflects some green light, making it a "poor" primary for mixing clear purples.
- **Red + Blue asymmetry:** additively, red and blue light mix to **magenta**, a bright non-spectral purple. In pigments, red and blue often yield a **dull violet**, because the "stray" green wavelengths reflected by the red pigment neutralize the blue.
- **Red + Green surprise:** additively, red and green light combine to **yellow**. Physically, red and green pigments (which are complements) annihilate each other into a **neutral gray-black or brown**.

### 4. Practice in Art: Pointillism and Simultaneous Contrast

Artists have exploited optical mixing to achieve effects impossible with palette blending:

- **Seurat and pointillism:** Georges Seurat and the Neo-Impressionists applied small dots of pure, unmixed color so colors mix "in the eye."
- **Brightness and chroma:** optical mixtures are perceived as more **vibrant and luminous** than palette mixtures. A physical blend of blue and yellow yields green by absorbing red and orange light; optical dots of blue and yellow preserve more reflected light, producing a green that appears "vibrating" and less diluted.
- **[[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing|Simultaneous contrast]]:** Michel-Eugène Chevreul's theory established that juxtaposed complementary colors enhance each other — red and green in proximity "amplify each other," creating heightened intensity that exceeds the inherent chroma of the individual pigments.

### 5. Non-Equivalence: Averaging vs. Absorption

Optical mixing is not strictly equivalent to pigment mixing, because they operate by different physical mechanisms:

- **Spatial averaging:** optical mixtures are **spatially averaged additive mixtures of reflected light**. The total light reaching the eye is the sum of the light reflected from the individual dots, producing a color intermediate in lightness between the components.
- **Spectral absorption:** physical mixtures involve **complex spectral absorption**. When two opaque pigments are mixed, their particles intermingle and light must pass through or reflect off both, causing significant energy loss and a darker result than optical averaging.

### 6. Relationship to Gamut

The method of mixture fundamentally dictates the achievable **gamut**:

- **Gamut hierarchy:** additive/optical methods generally provide a **wider color gamut** than subtractive/pigment methods.
- **Unwanted absorptions:** the subtractive gamut is limited by the "unwanted absorptions" of real colorants — absorption even where they should be transparent — which compounds with every addition, quickly "muddying" the color.
- **Expansion through optical mixing:** printers and painters bypass some subtractive losses optically. The **stochastic (random dot) halftone** process in modern printing expands the gamut in darker tonal areas by minimizing the "muddying" overlap of ink films. In digital displays, highly saturated RGB primaries produce a gamut covering roughly **one-third** of all perceived colors — difficult to replicate with traditional four-color (CMYK) pigment systems.

## Handprint Perspectives

> [!WARNING] **The Categorical vs. Continuous Fallacy in Color Theory.** According to MacEvoy's extensive analysis, traditional color theory routinely conflates optical (visual) principles with physical paint mixing, relying on arbitrary geometric categories rather than continuous physical properties:
>
> **1. Visual Complements vs. Mixing Complements.** Traditional theory assumes colors opposite on the wheel are both *visual* complements (strongest contrast, grounded in opponent-process theory) AND *mixing* complements (they mix to neutral gray). Handprint demonstrates that **visual and mixing complements are almost never the same** — the visual complement of phthalo green (PG7) is quinacridone rose, but mixing them gives a dark violet, not a neutral gray; the actual mixing complement of PG7 is a middle red. *(Source: [[raw_sources/handprint/color16.md|color16.html]])*
>
> **2. The Myth of "Primary Colors" and Geometric Harmonies.** Strict geometric categories — three "primary colors" that must not be crossed, rigid triadic/split-complementary harmonies — are artificial 18th-century dogmas, not physical laws. Real paint behavior and visual harmony are governed by **continuous properties** (hue-circle distance, value, chroma): using only three "primary" paints unnecessarily restricts the painter's gamut, since saturation costs depend on the distance between paints on the hue circle and their individual chroma; and harmony is not achieved by picking hues forming a perfect triangle, but by managing values and saturations. *(Source: [[raw_sources/handprint/color14.md|color14.html]], [[raw_sources/handprint/color16.md|color16.html]], [[raw_sources/handprint/tech13.md|tech13.html]])*

## HueValueChroma Perspectives

Briggs gives the mixing taxonomy its missing precision. **Four — not two — kinds of stimulus mixing exist**: *simple additive* (lights add power; screen subpixels; overlapping beams), *additive-averaging* (finely interspersed stimuli averaged over area or time — spinning discs, fine halftone dots, unresolved pointillist dots), *subtractive* (filters/colourants successively remove wavelengths; results are computed by *multiplying* the percent transmittance/reflectance wavelength by wavelength), and the *complex mixing of paints*, which is a **compound of subtractive + additive-averaging**. Physical mixing of opaque paints is never purely subtractive: light back-scattered off particles of a single component alone contributes an additive-averaging term, which is exactly why "it is impossible to mix a deep black" from near-complementary opaque paints. *(Source: [[raw_sources/huevaluechroma/041.md|041.html]], [[raw_sources/huevaluechroma/051.md|051.html]], [[raw_sources/huevaluechroma/061.md|061.html]])*. This four-fold structure sharpens each of the page's fallacies:

- **The "green made of yellow + blue" idea is inverted.** Subtractive mixing produces green from yellow/cyan filters not because the components contain green but because they *both transmit* it — "if any colour can be said to be 'made of' yellow and blue, it's white!" (051). The RYB red+blue→dull-violet and R+G→black surprises follow from multiplying real (imperfect) reflectance curves, not from mixing "colours."
- **Additive primaries are optimal, not arbitrary.** "To be effective as additive primaries the three stimuli must remain within the basic hue categories of red to orange-red, yellow-green to green, and blue to violet" (041) — they are neither perfect (they cannot mix all hues at full saturation) nor arbitrary. Zone theory explains why additive mixing is *vector* addition in which opponent dispositions add or cancel: R+G light yields a *pure yellow* whose perceived colour "does not contain" red or green (041).
- **Metamerism bounds the prediction.** Because two colourants can match in colour yet differ in reflectance curves, "the exact results of subtractive mixing of real colourants can not be predicted merely from their colour" — though all common cyan+yellow colourants will make some green (051).
- **Ideal colourant primaries are YMC, not RYB.** The combined analysis of additive-averaging + subtractive mixing in paint mixes revealed "that the ideal primaries for colourant mixing are not in fact yellow, red and blue, but yellow, magenta and cyan" (041).

> [!NOTE] On "optical mixtures are more vibrant": the page's §4 claim (after the older Seka/pointillist literature) that optical mixtures are "perceived as more vibrant and luminous than palette mixtures" is what Briggs says was *misinterpreted* from Rood (see [[Neo-Impressionism-Pointillism]]): optical mixing of the *same* paints can be lighter than their physical mixture, but pointillist dots are *additive-averaged* and necessarily sit intermediate in brightness between their components — no free "luminosity" bonus follows.

## Subtopics
- Additive vs Subtractive Mixing
- Primary Color Fallacies
- Pointillism & Optical Mixing
- Gamut Consequences

## Cross-References
- [[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing]]
- [[Perceptual Complements vs. Mixing Complements]]
- [[Neo-Impressionism-Pointillism]]
- [[Colors/Gamuts/index|Gamuts]]
- [[Natural Light Gamut vs. Pigment Gamut - Metamerism]]
- [[Munsell Notation]]
- [[History & Key Figures]]

## Sources

* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Contemporary Color" — Steven Bleicher
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Dimensions of Colour: additive mixing" — [[raw_sources/huevaluechroma/041.md|041.html]] et seq.
