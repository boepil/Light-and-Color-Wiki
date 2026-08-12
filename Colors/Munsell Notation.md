---
title: Munsell Notation
sequence: 9
---
![[images/ChatGPT Image Aug 6, 2026, 02_36_26 PM.png]]

**Scope:** Explores the Munsell notation system, its structure, the 1943 Renotation, and its open-ended chroma.

The **Munsell color system** is a perceptually based color order system that describes colors by how they are actually seen by the human eye rather than how they are mixed with pigments or displayed on screens. Developed by **Albert H. Munsell** at the beginning of the 20th century, it provides a rigorous, numerical framework for color specification that remains a global standard in science, art, and industry (**A Comprehensive Overview**, **Color Management**, **color-for-science-art-and-technology.pdf**).

### 1. The Three Dimensions of Color

Munsell organizes color into three independent, perceptually uniform dimensions:

- **Hue (H):** the spectral quality of a color (red vs. blue). The system uses **five principal hues** (Red, Yellow, Green, Blue, Purple) and **five intermediate hues** (Yellow-Red, Green-Yellow, Blue-Green, Purple-Blue, Red-Purple). Each of these 10 hues is further divided into 10 steps, creating a 100-step hue circle.
- **Value (V):** the lightness or darkness of a color, on a vertical axis ranging from **0 (ideal black) to 10 (ideal white)**.
- **Chroma (C):** the colorfulness or "saturation" relative to a neutral gray of the same value. Chroma is measured in **equal visual steps** radiating outward from the neutral axis (/0) to the maximum achievable with available pigments.

### 2. Munsell Notation Format (H V/C)

Colors are specified with the alphanumeric format **Hue Value/Chroma**:

- **Example:** **5PB 4/8** — a purple-blue in the middle of its hue range, slightly darker than middle gray in value, with a strong chroma of 8.
- **Neutral colors:** achromatic grays are denoted **N** followed by the value (e.g., **N 5/**).

Unlike **RGB** (additive light for displays) or **CMYK** (subtractive ink for printing) — device-dependent coordinate systems — Munsell is **device-independent** and based on human vision. RGB specifies how to *make* a color on a specific screen; Munsell describes what that color *looks like* to a standard observer.

### 3. The Munsell Color Tree

Though Munsell initially envisioned a perfect sphere, the physical limits of pigments and the nature of human perception required an irregular 3D shape — the **"Color Tree"**:

- **Irregularity:** the tree is lopsided because maximum achievable chroma varies by hue and value. **Yellows reach peak chroma at high values** (light yellow), while **blues and purples sustain high chroma at lower values**.
- **Perceptual insight:** the irregularity reveals that the visual system is more efficient at certain wavelengths — the **luminosity function peaks in the green region**, allowing green surfaces to achieve high value and high chroma simultaneously, a physical impossibility for red pigments.

### 4. Albert Munsell: Artist and Educator

Albert Munsell was a painter and art teacher in Boston frustrated by the **poverty of color language**. Traditional pigment-based names — "peacock blue," "apple green," "baby blue" — were inconsistent, subjective, and "bizarre."

Munsell created his system to provide a **scientific basis for color discipline**: students could record "transitory colors" for later use and grasp the "triple balance" of color across its three attributes. The system was integrated into a **nine-year pedagogical curriculum** for school children to train color sense from an early age.

### 5. The 1943 Renotation

In the 1940s, color scientists recognized inconsistencies in the original Munsell samples and launched a large-scale visual experiment to re-measure the system:

- **Anchoring to CIE:** the **1943 Renotation** formalized Munsell by providing precise **CIE (Y, x, y) coordinates** for every ideal Munsell notation.
- **Scale and scope:** based on approximately **3 million observations**, the renotation made the system as visually uniform as possible and extended it to accommodate higher chromas and very dark values.

### 6. Value Scaling and Practical Applications

The Munsell value scale is **not linear** with respect to physical light intensity (luminance). It follows a **square-root or cube-root relationship with reflectance (Y)** to mirror how the brain perceives lightness: a value of **5/** reflects approximately **18–20%** of the light, yet is perceived as the "middle" between black and white.

**Practical uses:**

- **Art:** painters use Munsell to plan color schemes, mix precise pigments, and maintain value structures in representational painting.
- **Industry:** the standard for color specification in **textiles, plastics, and paints**, providing a "color difference ruler" for quality control.
- **Science:** used in fields requiring standardized visual comparison, such as **soil science** and archaeology, as a universal language for object colors.

## Handprint Perspectives

MacEvoy treats the Munsell system as one of the few color models built on an **11-step value scale** (0 = black to 10 = white) and notes its convenient relationship to modern metrics: the **CIELAB L\* dimension is a multiple of 10 of the Munsell scale** — a Munsell value of 6 corresponds to an L\* of 60.

He also documents Munsell's own **principles of perceptual harmony**, defined as specific paths through the color space — same hue and value with contrasting chroma, same hue and chroma with contrasting value, and so on. Munsell defined **color strength as the product of value and chroma**, proposing that color area should be balanced inversely against strength; as T.M. Cleland explained, the small-area color should be both lighter valued and more chromatic. MacEvoy notes the formula is ambiguous (chroma's larger numerical range tends to dominate), and that it can be adapted to CIELAB/CIECAM by dividing CIELAB chroma by 4 and CIELAB lightness by 10. *(Source: [[raw_sources/handprint/tech13.md|tech13.html]], [[raw_sources/handprint/color18a.md|color18a.html]])*

## HueValueChroma Perspectives

Briggs grounds the Munsell tree's famous irregularity — and several of the page's incidental numbers — in measurement:

- **Chroma is a Munsell invention with an open-ended scale.** "The term *chroma* was invented by Munsell (1905)," who "subsequently quantified the term as an open-ended scale of perceptually uniform steps." The maximum chroma attainable in surfaces "was different for different hues," and because it is open-ended it keeps advancing as new pigments arrive — "chroma ranges beyond 20 for some normal reflecting materials, as and can be as high as 30 for some fluorescent paints" *(Source: [[raw_sources/huevaluechroma/082.md|082.html]], [[raw_sources/huevaluechroma/015.md|015.html]])*.
- **The value scale's "unattainable" endpoints and the three bounds of every hue page.** Munsell's conceptual 0–10 scale was realized in his 1915 *Atlas* "as a nine level scale of actual paint between 'unattainable' black and 'unattainable' white"; in the modern system "most black paints have a value of about 2 (though a glossy black paint can be as low as 0.5), and most white paint has a value of about 9" — Frank Reilly later expanded it to an eleven-level *paint* scale with black and white paint on 0 and 10. Rightly, a single-hue page is a **triangle** in lightness–chroma space: "the range of possible chroma becomes progressively more restricted as one approaches white and black respectively," and "the lightness level at which this maximum chroma occurs is highest for yellow and lowest for hues around violet-blue" — the quantitative form of the tree's lopsidedness *(Source: [[raw_sources/huevaluechroma/081.md|081.html]], [[raw_sources/huevaluechroma/082.md|082.html]])*.
- **The chroma maxima quantify the bulge: 16 units at orange-yellow/orange-red, only 10 in cyan–green.** In the modern *Munsell Book of Color* "the highest chromas (16 Munsell chroma units) are attained in the hue range from orange-yellow to orange-red, while the lowest maximum chromas (10 Munsell chroma units) are reached in the hue range from cyan to green" — and the peak-chroma *value* runs from 8–8.5 on the 5Y hue page down to 3–4 on the 7.5PB page. Unusually, "this lopsided gamut of colours available to painters... does not really present a problem because the range of common object colours is restricted in essentially the same way, for the same combination of physical and physiological reasons" *(Source: [[raw_sources/huevaluechroma/015.md|015.html]])*.
- **The screen/paper versions of the tree disagree with the pigment tree.** Digital colors "far exceed artists' paints with Munsell chromas of 24 in the violet-blue to magenta range, down to 18 at red," while artist paints "exceed the gamut of standard (sRGB) digital colours" in the yellow and cyan regions — and the RGB "full-chroma" secondaries are all lighter than their primaries (L = 98 yellow, 91 cyan, 60 magenta vs. 88 green, 54 red, 30 blue), "disturbing the steady fall in lightness from yellow to violet-blue." Each gamut is a genuine hue–lightness–chroma region, but none is the tree *(Source: [[raw_sources/huevaluechroma/015.md|015.html]], [[raw_sources/huevaluechroma/083.md|083.html]])*.
- **Why the sphere is wrong.** Runge's sphere of 1810 and Itten's of 1961 both place all "full" colors on the equator, "ensuring that the vertical dimension does not represent absolute lightness" — "neither the Runge-Itten sphere nor the HLS digital model is a true hue-chroma-lightness space." The correct conceptual solid is a **skewed double cone** (Kirschman 1896; Arthur Pope 1922 from Denman Ross) that "tilts" the plane of full colors so yellow sits high opposite light grey and blue sits low opposite dark grey — while the Munsell system, using absolute lightness and chroma, simply allows its irregular, tree-like shape to grow to fit *(Source: [[raw_sources/huevaluechroma/083.md|083.html]])*.
- **Value is measured, not guessed — and two effects complicate it.** A middle grey that looks equidistant from black and white reflects only ~18–20% of a white's light (the cube-root L\* = 116(Y/Yn)^(1/3) − 16 compresses this nonlinearly), and "crispening" (an instance of simultaneous contrast) makes lightness steps near the background look relatively large, so "no scale can look perfectly even irrespective of background." The **Helmholtz–Kohlrausch effect** further means "certain colours can give the impression of being lighter than a grey of the same CIE lightness" — which is why "the painter's trick of *squinting*... diminishes this colour glow and is extremely useful for comparing luminance/CIE lightness/Munsell value" *(Source: [[raw_sources/huevaluechroma/081.md|081.html]], [[raw_sources/huevaluechroma/013.md|013.html]])*.

## Subtopics
- Hue, Value, and Chroma
- Notation Format
- The Color Tree
- 1943 Renotation
- Value Scaling
- The open-ended chroma scale; the 16-unit orange/red vs 10-unit cyan/green maxima (Briggs)
- The skewed double cone vs the Runge-Itten sphere, and RGB secondaries vs the pigment tree (Briggs)

## Cross-References
- [[CIE Systems]]
- [[Why Lab-Munsell Were Built for Perceptual Uniformity]]
- [[MacAdam Ellipses]]
- [[Colors|Colors]]
- [[History & Key Figures]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Dimensions of Colour : lightness" — [[raw_sources/huevaluechroma/013.md|013.html]]
* "The Dimensions of Colour : chroma" — [[raw_sources/huevaluechroma/015.md|015.html]]
* "The Dimensions of Colour : lightness and chroma" — [[raw_sources/huevaluechroma/081.md|081.html]], [[raw_sources/huevaluechroma/082.md|082.html]], [[raw_sources/huevaluechroma/083.md|083.html]]