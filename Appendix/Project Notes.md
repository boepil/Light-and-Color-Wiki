![[Pasted image 20260810111019.png]]

**Scope:** Working notes for building an interactive 3D color-space viewer — the color solids to render, the coordinate conventions that define them, and the visualization techniques that make them navigable. Content is drawn from the notebook corpus and complements the deeper pages on [[CIE Systems]], [[Munsell Notation]], and [[Optimal Color Solid-MacAdam Limits]].

### The Solids to Render

- **CIELAB (L\*a\*b\*):** every color experience maps to a unique point; the vertical **L\*** axis runs 0 (ideal black) to 100 (ideal white), and the horizontal opponent axes are **a\*** (redness–greenness) and **b\*** (yellowness–blueness). Visualized, it is "often pictured as a sphere or spindle containing the subset of human-perceivable colors" (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*).
- **Munsell Color Tree:** the pigment volume is an **irregular tree**, not a sphere — vertical trunk **Value 0–10**, hue in a circular circuit around the axis, **Chroma radiating outward**. Branches vary in length and height because hues reach maximum chroma at different values: "yellow is most vivid at high values, while purple is most vivid at low values" (*A Comprehensive Overview..., Ordering Colour: Albert Henry Munsell*).
- **RGB cube:** device signal space with axes normalized 0–1; corners are the three primaries, three secondaries (cyan, magenta, yellow) and the achromatic poles black (0,0,0) and white (1,1,1) (*A Comprehensive Overview..., The Science of Paintings*).

### Gamut Boundaries in 3D

- **Optimal color solid (MacAdam limits):** the theoretical ceiling of material colors — an **asymmetric, irregular spindle** with a characteristic protrusion in the yellow-green region at high lightness (the photopic luminosity function peaks near 555 nm), while red and blue are more restricted (*A Comprehensive Overview..., Color Management*).
- **Pointer's gamut:** the subset hull of real surfaces (paints, flowers, textiles) — smaller than the MacAdam limits, strikingly asymmetric in CIELAB, with peak chroma around hue angles **~20° (orange)** and **~150° (green)** (*A Comprehensive Overview...*).
- **Display gamuts:** project into 3D as **triangular prisms**; in practice boundaries are limited by maximum luminance and by ambient scattered light, "which reduces the gamut near the black point" (*A Comprehensive Overview, Color Management*).

### Coordinate Conventions

- **Lightness:** L\* = 116·(Y/Yn)^(1/3) − 16 for (Y/Yn) > 0.008856, with Yn the white point luminance (*A Comprehensive Overview..., Color Management*).
- **Opponent coordinates:** a\* and b\* derive from cube-root ratios of X/Xn, Y/Yn, Z/Zn (*A Comprehensive Overview...*).
- **Chroma:** C\*ab = √(a\*² + b\*²), the Euclidean distance from the neutral axis (*A Comprehensive Overview...*).
- **Hue angle:** h_ab = arctan(b\*/a\*) — 0° is +a\* (red), 90° is +b\* (yellow), 180° is −a\* (green), 270° is −b\* (blue) (*A Comprehensive Overview...*).
- **White points & projections:** D65 (6,500 K) or equal-energy E anchor the neutral axis; chromaticity (x,y or u′,v′) normalizes tristimulus values to sum 1.0 — the 2D projection of the 3D volume. The spectral locus horseshoe and the dashed line of purples form "the outermost rim of the 'equatorial' cross-section at various lightness levels" (*A Comprehensive Overview..., Color for Science, Art, and Technology*).

### Rendering and Navigation Advice

- **Constant-L\* slices:** horizontal planes at fixed lightness reveal how gamuts expand and contract (*A Comprehensive Overview..., Munsell Color Science Lab*).
- **Hue wedges:** Munsell himself navigated the solid with constant-hue slices — Value vertical, Chroma horizontal — giving "a clear 'page' of related colors" (*Ordering Colour: Albert Henry Munsell*).
- **Uniform spaces:** render in CIELAB or CIELUV so spatial distance tracks perceived difference (*A Comprehensive Overview...*).
- **Edge fidelity:** near the limits of human vision, use "unreal" extrapolated Munsell data so multidimensional interpolation fully encompasses the MacAdam limits (*Munsell Color Science Lab*).

## Handprint Perspectives

MacEvoy's deep-cut advice for such a viewer: don't trust the tidy geometry. A real gamut "does not form a symmetrical circle" — any renderer that assumes regularity will mislead — and the "color space is not as symmetrical as a circle or as homogenous as cookie dough, so using cookie cutter color concepts won't get you very far." In CIELAB the familiar triangular display-gamut shape "appears significantly altered," and hues are not proportional mixtures of primaries but coordinates measured against the 1931 CIE xy diagram or its matching dominant wavelengths *(Source: [[raw_sources/handprint/intstud.md|intstud.html]], [[raw_sources/handprint/color18a.md|color18a.html]], [[raw_sources/handprint/tech13.md|tech13.html]])*.

## Subtopics
- Rendering targets: CIELAB spindle, Munsell Color Tree, RGB cube, gamut hulls
- Boundaries: MacAdam spindle (+555 nm protrusion), Pointer's asymmetric hull, display prisms
- Conventions: L\* = 116(Y/Yn)^(1/3) − 16, C\*ab, h_ab quadrants, D65/E neutrals, chromaticity projection
- Navigation: constant-L\* slices, hue wedges, uniform-space rendering, extrapolated-Munsell interpolation
- Reality check: irregular gamuts, no symmetry, no cookie-cutter color concepts

## Cross-References
- [[CIE Systems]] — CIELAB conventions and the chromaticity plane
- [[Munsell Notation]] — the Color Tree and hue wedges
- [[Optimal Color Solid-MacAdam Limits]] — the spindle to render
- [[Pointer's Gamut]] — the real-surface hull
- [[Why Lab-Munsell Were Built for Perceptual Uniformity]] — why distance = difference matters
- [[Data & Methodology]] — the datasets feeding the model

## Sources
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management: A Comprehensive Guide for Graphic Designers" — John T. Drew and Sarah A. Meyer
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "Color for Science, Art, and Technology" — Kurt Nassau (editor)
* "Ordering Colour: Albert Henry Munsell (1858–1918)" — The Eclectic Light Company
* "Munsell Color Science Lab Educational Resources" — Rochester Institute of Technology