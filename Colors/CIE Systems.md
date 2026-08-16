---
title: CIE Systems
sequence: 56
---
![[images/ChatGPT Image Aug 6, 2026, 02_26_10 PM.png]]

**Scope:** The international number system for color — how the CIE turned "how the average human eye responds to light" into coordinates any lab, factory, or screen can share, from the classic xy map to the modern Lab space.

The **Commission Internationale de l'Éclairage (CIE)** — the International Commission on Illumination — established the first international standards for putting color into numbers in **1931**, replacing subjective color names with a rigorous coordinate framework that allows precise color matching across industries and devices. If there is an "official ruler" for color, this is it.

### From measured light to CIE numbers

These coordinates rest on **physical measurement**, not abstract math. A spectrophotometer or spectroradiometer records how much light a surface reflects (or a source emits) at each wavelength; those measurements are then weighted by the standard observer's color-matching functions and summed into the **X, Y, Z** tristimulus values. That is why a single RGB swatch or paint chip is never enough — the full **spectral fingerprint** is what survives a change of lighting or device.

The complete pipeline — color-matching experiments, the photopic luminosity function **V(λ)**, and the integration formula — is covered in **[[Color Matching Functions and the Photopic Luminosity Function|Color Matching Functions and the Photopic Luminosity Function]]**. The **instruments, reference datasets, and measurement caveats** catalogued for this wiki are in **[[Data & Methodology|Data & Methodology]]**.

### 1. How the CIE built its standard (1931)

Before 1931, specifying a color meant describing it by eye, which made manufacturing inconsistent. To fix this, the CIE ran **color-matching experiments** in which observers looked at a split circular field:

- **The task:** one half showed a "test" spectral color (one specific wavelength); the observer adjusted the intensities of three primary lights — **red (700 nm)**, **green (546.1 nm)**, and **blue (435.8 nm)** — on the other half until both sides matched.
- **The result:** averaging many observers with normal color vision produced the **color-matching functions**, which state how much of each primary is needed to match any wavelength of the visible spectrum.

### 2. The XYZ system and its "imaginary" primaries

A critical discovery was that **real RGB primaries cannot match every spectral color**. For certain highly saturated wavelengths (especially in the blue-green region), a primary had to be added to the *test color* side to achieve a match — which mathematically meant **negative values**.

- **Imaginary primaries (X, Y, Z):** to eliminate negative numbers and simplify calculation, the CIE invented a new set of **mathematical primaries**, X, Y and Z. They are "imaginary" in the sense that no device can produce them directly, but they are positioned so that every visible color is described by positive values.
- **What each one means:**
  - **Y (luminance)** is deliberately set to match the eye's **luminous efficiency function V(λ)** — it carries the perceived *lightness* or brightness.
  - **X and Z** carry the remaining chromatic information — the hue and vividness.

### 3. The two standard observers: 2° (1931) and 10° (1964)

The CIE defines "standard observers" according to how wide the visual field was in the matching experiments:

- **1931 2° Standard Observer** — based on a field covering a **2° angle**, roughly the size of a **dime held at arm's length**. That small field lands on the **fovea**, the region of the retina with the densest cones and no rods.
- **1964 10° Supplemental Standard Observer** — added because we usually look at larger color fields, where the receptor mix differs from the central fovea. It approximates **industrial viewing conditions** and is the standard for most modern colorimetry.

### 4. The xy chromaticity diagram (the "color map")

The three XYZ numbers are often projected into a 2D **xy chromaticity diagram** so color can be visualized apart from lightness:

- **How it's drawn:** the coordinates are ratios — **x = X/(X+Y+Z)** and **y = Y/(X+Y+Z)**.
- **The spectral locus:** the curved, horseshoe-shaped boundary is the **pure rainbow** — monochromatic light from **380 nm** (violet) to **780 nm** (red).
- **The line of purples:** the dashed line joining the horseshoe's ends represents **purples and magentas**, which exist only as mixtures of red and violet light, never as a single wavelength.
- **The white point:** the center contains the **Equal Energy (Point E)** white, though real illuminants like **D65** (average daylight, 6,500 K) are more commonly used in practice.

### 5. CIELAB (1976): a more "honest" space

A major flaw of XYZ is its **non-uniformity** — equal distances on the xy diagram do not mean equal perceived differences. In **1976** the CIE introduced **CIELAB** to fix this:

- **Opponent framework:** built on Ewald Hering's **[[Opponent-Process Color Coding|opponent-process theory]]**, with three axes:
  - **L\*** — lightness (0 = black, 100 = white);
  - **a\*** — redness–greenness;
  - **b\*** — yellowness–blueness.
- **White-point adaptation:** CIELAB accounts for the way your eye adapts to lighting by referencing a **standard white** under the specific illuminant.
- **ΔE (color difference):** the distance between two points in this space is a "color difference ruler"; a **ΔE of 1.0** is roughly the threshold for a commercially acceptable match in the textile industry.
- **Device independence:** CIELAB is a **universal translator** — its values are based on human perception rather than any screen's phosphors or a printer's inks (unlike RGB or CMYK).

### 6. Gamuts, MacAdam ellipses, and later refinements

- **Gamuts:** a device's **gamut** is the range of colors it can reproduce, often drawn as a triangle inside the chromaticity diagram.
- **[[MacAdam Ellipses|MacAdam ellipses]]:** regions on the diagram within which all colors look identical to the center color. Their wildly varying sizes were the primary motivation for building uniform spaces like CIELAB.
- **The Munsell connection:** in **1943**, the **[[Munsell Notation|Munsell Renotation]]** anchored the Munsell Color Tree to precise CIE (Y, x, y) coordinates, tying that visual system to the mathematical standard.
- **Later refinements:**
  - **CIELUV (1976)** — CIELAB's sibling, used mainly in **television and video** because it keeps a meaningful chromaticity diagram;
  - **CIECAM** — advanced appearance models (e.g., **CIECAM97**) that adjust for complex viewing environments and lighting conditions.

## Handprint Perspectives

MacEvoy uses the CIE system to illuminate the "double life" of primary colors — **conceptual color** (an abstract, ideal color) versus **material color** (a physical colorant that creates color perception). The X, Y, Z primaries are the perfect illustration: the visible **spectral primaries RGB cannot mix all colors**, while the invisible **mathematical primaries XYZ explain all color mixtures**. Because it is impossible to create a primary color that is both real (visible) and able to mix all other colors, all color-theory primaries are either conceptual or material — imaginary or imperfect. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

> [!WARNING] **Contradiction Flag: Perceptual Uniformity vs. Mixture Predictability.** While CIELAB excels at *perceptual uniformity* (equal steps look equally different), MacEvoy warns against assuming this grants *mixture predictability*: because subtractive pigment mixing introduces nonlinear saturation costs, a uniform perceptual space cannot mathematically predict the outcome of combining two physical paints. The model maps what we see, but not how paints physically behave when mixed. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

## HueValueChroma Perspectives

Briggs grounds the CIE machinery in the biology and the naming conventions that the coordinate jargon hides:

- **XYZ's "imaginary" primaries are virtual, not absent.** CIE XYZ "measures colours in relation to three virtual 'primaries' that are not colours, but are purely mathematical transformations of actual lights" — precisely the "double life" MacEvoy describes. It is "the foundation of colour management," and what most painters actually meet is the **xyY chromaticity diagram** and **CIE L\*a\*b\***, which "arranges colours similarly to the Munsell system, but describes their positions in terms of reddish/greenish (a\*/-a\*) and yellowish/bluish (b\*/-b\*) chroma instead of hue and total chroma" *(Source: [[raw_sources/huevaluechroma/112.md|112.html]])*.
- **Three is the key to stimulus because of three cone types — not three "colour rays."** "While the number **four** is the key to *colour perception*, **three** is the key to *colour stimulus and colour technology*. This number three stems from the fact that colour vision is ultimately based on three types of receptors in the eye called **L, M and S cone cells**." These cones "do not detect individual wavelength bands or 'colours' of the spectrum, but respond to very broad and extensively overlapping ranges of wavelengths peaking in the parts of the spectrum we see as *greenish-yellow*, green and blue-violet." Nor do they directly create sensations of colour: "**differences** in the responses of the three cone types are recorded in the retina in the form of *cone-opponent signals* (L-M and L+M-S)," and colour is created in the brain as colour-opponent signals. "When a light creates a balanced response of all three cone types, each cone-opponent signal is balanced at zero, and the light is seen as colourless ('white light')" *(Source: [[raw_sources/huevaluechroma/112.md|112.html]])*.
- **"RGB", "red", "green", "blue" are convenient misnomers.** The additive primaries and the psychological primaries "bear no direct relationship," yet "we have a strong unconscious predisposition to apply to the former the *names* of these hues that form the framework of our experience of colour" — exactly as the old RYB paint primaries were "almost universally labelled as simply 'yellow', 'red' and 'blue'," "in the same way today we routinely label the **orangeish red**, **yellowish green** and blue or violet-blue primaries of additive-mixing technology as simply 'red', 'green' and 'blue' (RGB)" *(Source: [[raw_sources/huevaluechroma/112.md|112.html]])*.
- **Additive primaries work by one-cone dominance.** RGB "red", "green" and "blue" lights work as additive primaries "because each of them stimulates one cone type *more than the other two*," so their mixtures produce a large variety of relative cone responses, and hence colours. The perennial classroom surprise — "red" + "green" light mixing to a *yellow* that is neither reddish nor greenish — is "the inevitable consequence of the mismatch between having three additive and four psychological primaries": the yellow is not made of the colours red and green, but results because "the yellow signals add together while the red and green signals cancel out" *(Source: [[raw_sources/huevaluechroma/112.md|112.html]])*.
- **Lab's axes are the opponent framework the page's §5 inherits.** CIELAB is the practical realization of Hering's model in a CIE-approved space: a value axis (L\*) plus the reddish/greenish a\* and yellowish/bluish b\* chroma axes — and, as Briggs notes, Photoshop's long-standing Lab colour-picker mode is an everyday instance of it for digital painters *(Source: [[raw_sources/huevaluechroma/112.md|112.html]])*.

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
- [[Colors/Gamuts/index|Gamuts]]

## Sources

* "Contemporary Color" — Steven Bleicher
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Dimensions of Colour: traditional and modern colour theory" — [[raw_sources/huevaluechroma/112.md|112.html]]