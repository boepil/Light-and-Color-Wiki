
![[images/ChatGPT Image Aug 6, 2026, 02_26_10 PM.png]]

**Scope:** Overview of CIE coordinate systems including the xy diagram, XYZ, and Lab spaces.

The **Commission Internationale de l'Éclairage (CIE)**, or International Commission on Illumination, established the first international standards for the mathematical description of color in **1931**, replacing subjective color naming with a rigorous, coordinate-based framework that allows precise color matching across industries and devices (**Contemporary Color**, **Color Management**).

### 1. The Founding of CIE 1931 and Color-Matching Experiments

Before 1931, color specification relied on subjective visual identification, leading to inconsistent manufacturing standards. To resolve this, the CIE conducted **color-matching experiments** in which human observers viewed a split circular field:

- **The task:** one half displayed a "test" spectral color (a specific wavelength); the observer adjusted the intensities of three primary lights — **Red (700 nm)**, **Green (546.1 nm)**, and **Blue (435.8 nm)** — on the other half to create a visual match.
- **The standardization:** averaging the results of multiple observers with normal color vision produced the **Color Matching Functions**, which define the amount of each primary required to match any wavelength of the visible spectrum.

### 2. The CIE XYZ System and Imaginary Primaries

A critical discovery of these experiments was that **real RGB primaries cannot match every spectral color**. For certain highly saturated wavelengths (particularly in the blue-green region), a primary had to be added to the *test color* side of the field to achieve a match — mathematically, **negative values** in the RGB color-matching functions.

- **Imaginary primaries (X, Y, Z):** to eliminate negative numbers and simplify industrial calculation, the CIE created a new set of **mathematical primaries**, X, Y, and Z. They are "imaginary" in that they cannot be physically produced, but they are positioned in color space so that all visible colors are described with positive values.
- **Representations:**
  - **Y (luminance):** the Y value is specifically defined to match the human eye's **luminous efficiency function (V(λ))**, representing the perceived lightness or "brightness" of a color.
  - **X and Z:** the remaining chromatic information defining the color's hue and saturation.

### 3. Standard Observers: 2° (1931) vs. 10° (1964)

The CIE defines "Standard Observers" according to the size of the visual field used in the matching experiments:

- **1931 2° Standard Observer:** based on a field of view covering a **2° angle**, roughly the size of a **dime at arm's length**. This small field focuses the stimulus on the **fovea**, the retinal region with the highest cone concentration and no rods.
- **1964 10° Supplemental Standard Observer:** added because humans often view color in larger fields where receptor distribution differs from the central fovea. It more closely approximates **industrial viewing conditions** and is the standard for most modern colorimetric calculations.

### 4. The xy Chromaticity Diagram

The three-dimensional XYZ values are often projected into a two-dimensional **xy chromaticity diagram** to visualize color independent of lightness:

- **Derivation:** the coordinates are calculated as ratios: **x = X/(X+Y+Z)** and **y = Y/(X+Y+Z)**.
- **Spectral locus:** the curved, horseshoe-shaped boundary represents the **pure spectral colors** (monochromatic light), ranging from **380 nm** (violet) to **780 nm** (red).
- **Line of purples:** the straight dashed line connecting the ends of the horseshoe represents **non-spectral purples**, which exist not as single wavelengths but as mixtures of red and violet light.
- **White point:** the center contains the **Equal Energy (Point E)** white point, though standard illuminants like **D65** (average daylight at 6,500 K) are more commonly used in practice.

### 5. CIELAB (1976): Perceptual Uniformity and Device Independence

One major flaw of XYZ is its lack of **perceptual uniformity** — equal distances on the xy diagram do not correspond to equal perceived color differences. To fix this, the CIE introduced **CIELAB** in **1976**:

- **Opponent framework:** based on Ewald Hering's **opponent-process theory**, CIELAB uses three axes:
  - **L\*** — lightness (0 = black, 100 = white);
  - **a\*** — redness–greenness;
  - **b\*** — yellowness–blueness.
- **White point adaptation:** CIELAB calculations include a subscript *n* referring to the tristimulus values of a **standard white diffuser** under a specific illuminant, allowing the system to account for human chromatic adaptation.
- **ΔE (color difference):** the distance between two points in this space provides a "color difference ruler"; a **ΔE of 1.0** is generally considered the threshold for a commercially acceptable match in the textile industry.
- **Device independence:** CIELAB acts as a **universal translator** — its values are based on human perception rather than the specific phosphors or inks of a device (unlike RGB or CMYK).

### 6. Gamuts, MacAdam Ellipses, and Later Developments

- **Gamuts:** a device's **gamut** is the range of colors it can reproduce, often shown as a triangle within the chromaticity diagram.
- **MacAdam ellipses:** regions on the chromaticity diagram where all colors are perceived as identical to the center color; the varying sizes of these ellipses in XYZ space were the primary motivation for creating more uniform spaces like CIELAB.
- **Munsell connection:** in **1943**, the **Munsell Renotation** provided precise CIE (Y, x, y) coordinates for the Munsell Color Tree, anchoring that visual system to a mathematical standard.
- **Later developments:**
  - **CIELUV (1976):** a companion to CIELAB, primarily used in the **television and video display** industries because it retains a meaningful chromaticity diagram;
  - **CIECAM:** advanced color appearance models (e.g., **CIECAM97**) further adjust for complex viewing environments and lighting conditions.

## Handprint Perspectives

MacEvoy uses the CIE system to illuminate the "double life" of primary colors — **conceptual color** (an abstract, ideal color) versus **material color** (a physical colorant that creates color perception). The X, Y, Z primaries are the perfect illustration: the visible **spectral primaries RGB cannot mix all colors**, while the invisible **mathematical primaries XYZ explain all color mixtures**. Because it is impossible to create a primary color that is both real (visible) and able to mix all other colors, all color-theory primaries are either conceptual or material — imaginary or imperfect. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

> [!WARNING] **Contradiction Flag: Perceptual Uniformity vs. Mixture Predictability.** While CIELAB excels at *perceptual uniformity* (equal steps look equally different), MacEvoy warns against assuming this grants *mixture predictability*: because subtractive pigment mixing introduces nonlinear saturation costs, a uniform perceptual space cannot mathematically predict the outcome of combining two physical paints. The model maps what we see, but not how paints physically behave when mixed. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

## Subtopics
- CIE xy Chromaticity Diagram
- CIE XYZ
- CIE Lab
- Standard Observers

## Cross-References
- [[Spectral Locus & Excitation Purity]]
- [[Color Matching Functions and the Photopic Luminosity Function]]
- [[Why Lab-Munsell Were Built for Perceptual Uniformity]]
- [[MacAdam Ellipses]]
- [[Munsell Notation]]
- [[Gamuts]]

## Sources

* "Contemporary Color" — Steven Bleicher
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer