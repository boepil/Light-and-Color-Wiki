---
title: Pigment Color Wheel (Munsell Placement)
sequence: 52
---
![[artistColorWheel.pdf]]

> The **artist's color wheel** (PDF above, from Bruce MacEvoy's handprint.com) plots actual pigments by measured hue angle and chroma rather than the idealized RYB wheel: hue runs around the circle (yellow at top, complements opposite), chroma increases outward from a neutral center (titanium white / carbon black / sepia). Each diamond is a specific pigment (PY35 cadmium yellow, PB29 ultramarine blue, PR122 quinacridone magenta...) plotted by its actual measured hue/chroma averaged across brands; convenience mixtures appear in italics ("sap green", "olive green"); bold names mark commonly available pigments; numbered sectors (1–6: yellow-orange, orange, red-orange, red/deep red, red-violet, violet) carry degree markings for hue angle. *(Source: [[raw_sources/handprint/color14.md|color14.html]] / artistColorWheel.pdf)*

**Scope:** Places real artist pigments inside the Munsell color system — where each pigment sits in hue, value, and chroma, and what that placement reveals about pigment families, chroma ceilings, and the difference between a pigment wheel and a light wheel.

### The Munsell Framework

The Munsell system organizes color into three independent, perceptually uniform dimensions, written **H V/C** (e.g., 5PB 4/8) (*A Comprehensive Overview...*, *Color for Science, Art, and Technology*):

- **Hue (H):** arranged in a circle of five principal hues (Red, Yellow, Green, Blue, Purple) plus five intermediate hues, divided into **100 steps** — 10 units per hue family, so 5R sits at the center of the red family.
- **Value (V):** a vertical lightness scale from **0 (ideal black) to 10 (ideal white)**, following an approximate square-root relationship with luminous reflectance.
- **Chroma (C):** departure from a neutral gray of the same value, /0 (neutral) outward; real pigments reach chromas of 20+, so the "sphere" Munsell first imagined grew into the irregular **Color Tree**.

### Mapping Pigments on the Color Tree

Real pigments form an irregular tree because each hue reaches maximum chroma at a different value (*A Comprehensive Overview*, *Color for Science, Art, and Technology*):

- **High-chroma synthetics at the outer edges:** cadmium yellow is intense at a high value (8.0Y 9.2/9.0); pyrrole red and quinacridone magenta reach high chroma at middle values (0.8YR 6.4/13.4); phthalocyanine blue keeps substantial chroma even at dark values (3.5PB 4.6/14.0).
- **Low-chroma earths near the trunk:** ochres, umbers and siennas sit close to the neutral axis with chromas typically **/2–/6** (yellow ochre 1.5Y 8.7/5.0; raw sienna 1.0Y 7.6/4.5; raw umber 1.5Y 6.9/2.0).
- **Representative placements:** ultramarine blue 5.0PB 6.3/10.0; viridian 7.5BG 7.3/4.5.
- **Clusters and gaps:** the wheel shows dense red/red-orange coverage, sparse yellow-green, and open gaps where no clean pigment exists at that hue/chroma — pigments do *not* sit at even intervals the way a printed wheel implies.

### Chroma Ceilings: Why Greens Win

- Perceptual chroma has hard physical ceilings per hue. Data from the **1943 Munsell Renotation** show Green (2.5G) and Green-Yellow (10GY) reaching **Chroma 34**, while Red (5R) peaks near **20**; violets and purples peak at lower values.
- The asymmetry traces to photopic luminosity V(λ) peaking near **555 nm**: green reflectances align with the most luminous band, carrying a large achromatic component per unit of spectral radiance — greens can be both light *and* saturated (*Why Material Reality Favors Green Over Red*, *A Comprehensive Overview*).
- Reds are limited because their absorption bands are broad and desaturated by "contamination" from adjacent wavelengths; greens achieve narrow-band reflectance matched to the luminosity peak.

### Pigments vs. the Spectral Locus and Optimal Colors

- **No real pigment reaches the spectral locus or the optimal (MacAdam-limit) colors:** optimal colors assume idealized 0%/100% step reflectance that no colorant achieves (*Optimal Color Solid*).
- Pigment chroma depends on how sharply a material reflects a narrow wavelength band — "unwanted absorptions" pull every real pigment inward from the gamut boundary (*Pigments hub*, *Gamuts*).

### Pigment Wheels vs. Light Wheels

- An **additive light wheel** (RGB) centers on white — the sum of all wavelengths — and has a larger gamut; mixtures move in straight lines through color space.
- A **pigment/subtractive wheel** centers on dark gray or black because pigments remove light; mixtures follow curved paths that lose chroma faster than expected because of unwanted absorptions.
- The Munsell-based pigment wheel restores the third dimension the flat wheel discards: a pigment's value and chroma both matter, which is why equal-hue pigments like raw umber and ultramarine (both "blue" or both "yellow") can look so different in mixtures (*intstud*, *color14*).

### Darkness Kills Chroma

- Munsell value tracks luminous reflectance; at very dark values approaching 0/, chromaticity becomes indistinguishable from black — dark pigments cannot appear saturated.
- To raise the value of a red pigment you must add green or blue light, which desaturates it; greens naturally carry a high achromatic component, so they remain high-chroma at high values (*Causal Chain*, *Why Material Reality Favors Green Over Red*).

## Handprint Perspectives

MacEvoy's color wheel is the definitive practical answer to the color-tree geometry: plot real pigments by measured hue/chroma (CIECAM hue angle and chroma, averaged across brands) and the wheel stops being a symmetric ideal and becomes a landscape of clusters and gaps — abundant red-oranges, sparse yellow-greens, and clean space where no pigment exists. The asymmetry is not an accident of chemistry alone: it follows the luminosity function, so greens and yellows reach higher chroma than reds and violets. This is why he distrusts the traditional RYB wheel as a mixing guide — it is a hue circle, not a map of attainable color *(Source: [[raw_sources/handprint/color14.md|color14.html]], [[raw_sources/handprint/intstud.md|intstud.html]], [[raw_sources/handprint/color18a.md|color18a.html]])*.

## Subtopics
- Munsell H V/C notation; 100-step hue circle, value 0–10, chroma /0–/20+
- Placement of high-chroma synthetics vs. low-chroma earths (with notations)
- Chroma ceilings: green 34 vs. red 20 (1943 Renotation); V(λ) 555 nm
- Pigment wheels vs. additive light wheels; curved mixing paths
- Dark value kills chroma; red vs. green luminosity asymmetry
- Clusters, gaps, and convenience mixtures on the measured wheel

## Cross-References
- [[Pigments/Reference/index|Pigment Reference]] — the individual data sheets plotted on the wheel
- [[Pigments/High-Chroma Synthetics]] — the pigments at the outer edge of the tree
- [[Munsell Notation]] — the system behind the placement
- [[Colors/Gamuts/index|Gamuts]] — why no pigment reaches the locus
- [[Causal Chain - Pigments to Perception]] — V(λ) and the green chroma ceiling
- [[Pigments/Transparency, Opacity & Pigment Codes|Transparency, Opacity & Pigment Codes]] — reading pigment labels

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "Why Material Reality Favors Green Over Red: The Physical Chemistry of Chromatic Limits"
* Artist's color wheel — Bruce MacEvoy (artistColorWheel.pdf)
* Handprint pigment and color theory pages — Bruce MacEvoy
