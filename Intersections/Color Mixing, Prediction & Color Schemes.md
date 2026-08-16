---
title: Color Mixing, Prediction & Color Schemes
sequence: 85
---![[Pasted image 20260813123650.png]]

**Scope:** The physics, physical chemistry, and visual mechanics of paint mixing — why physical mixtures follow curved paths and resist simple geometric prediction — combined with the geometry, scientific critiques, and studio practice of color schemes.

### 1. Mixing Mechanics & The Prediction Problem

Paint color mixing is fundamentally different from mixing light: it is governed by **subtractive (multiplicative) filtering** rather than additive superposition. In additive mixing, light energies sum linearly to a lighter result; in subtractive mixing, each pigment absorbs specific wavelength bands from incident white light, leaving only the unabsorbed wavelengths to be reflected. Consequently:

- **Curved mixing paths:** Mixtures of two pigments do not follow straight lines on a color wheel or chromaticity diagram. Instead, they trace **curved paths** bending inward toward lower chroma, because spectral reflectance curves multiply value-by-value across the spectrum (*"Choosing Colors (Live)"* — Color Nerd; *Color for Science, Art and Technology*, Fig. 1.11; *Interaction of Color*, Ch. X).
- **The RYB fallacy vs. CMY primaries:** Traditional art education teaches Red, Yellow, and Blue (**[[Why CMY Beats RYB for Color Mixing|RYB]]**) as the primary colors. However, modern color science establishes **Cyan, Magenta, and Yellow (CMY)** as the optimal subtractive primaries, because each absorbs exactly one-third of the visible spectrum (cyan absorbs red 600–700 nm, magenta absorbs green 500–600 nm, yellow absorbs blue 400–500 nm).
- **Why Yellow + Blue yields green, gray, or black:** Yellow and blue lights additively combine to white. Yellow and blue paints typically mix to green because blue pigments absorb red and yellow wavelengths while yellow pigments absorb blue wavelengths, leaving only the **shared green window (500–570 nm)** reflected by both. If two specific pigments lack an overlapping spectral window, their mixture yields an achromatic **gray or black** rather than green.

### 2. Physical Mechanisms Behind Prediction Failures

Predicting the exact hue, value, and chroma of a paint mixture from the individual components frequently fails due to five material factors:

- **Neutralization & "Mud":** Every added pigment increases cumulative absorption, lowering total reflectance and darkening the mixture. Combining three or more pigments (or two complementary pigments) cancels chromatic power across all three cone channels, collapsing the mixture into an unchromatic gray, brown, or "mud".
- **Value & Tinting Strength Dominance:** Pigments possess vastly different **tinctorial strengths** (molar extinction coefficients). A high-strength, dark-valued pigment such as **[[PB15 - Phthalo Blue|Phthalo Blue]]** (PB15) or **[[PV23 - Dioxazine Violet|Dioxazine Violet]]** (PV23) easily overwhelms a low-strength, light-valued pigment such as **[[PY35 - Cadmium Yellow|Cadmium Yellow]]** (PY35) — a tiny trace of phthalo completely shifts the hue, whereas adding yellow to phthalo produces almost no visual change.
- **Refractive Index & Opacity/Transparency ($\Delta n$):** Hiding power (opacity) depends on the refractive-index difference $\Delta n = n_{\text{pigment}} - n_{\text{binder}}$. **[[PW6 - Titanium White|Titanium White]]** (PW6, $n \approx 2.55–2.71$) has a large gap against linseed oil ($n \approx 1.48$), scattering light strongly and creating opaque tints; **[[PB29 - Ultramarine Blue|Ultramarine Blue]]** (PB29, $n \approx 1.50$) matches the oil's index almost perfectly, producing a transparent glaze that reveals underlying layers rather than covering them. See [[Transparency, Opacity & Pigment Codes]], [[Media, Vehicles & Solvents]].
- **Handling, Over-Mixing & Granulation:** Mechanical over-mixing on the palette grinds particles together into a uniform suspension, destroying the vibrant, microscopic light-scattering of individual pigment grains — "loosely scrambled" strokes preserve far greater chromatic vitality. Flocculation and particle agglomeration (e.g. **[[PB27 - Prussian Blue|Prussian Blue]]** or raw earth granulations) alter wash texture and apparent value on paper.
- **Metamerism in Blends:** Two pigment mixtures can appear identical under studio daylight (e.g. 5000 K D50) yet diverge dramatically under tungsten or fluorescent lighting if their underlying spectral reflectance curves differ — as seen when comparing Smalt against **[[PB28 - Cobalt Blue|Cobalt Blue]]**. Therefore, a mixture's outcome **cannot be predicted from hue coordinates alone** without knowing the full spectral power distribution.

### 3. The Shrinking Gamut

Physical paint mixing always results in a **loss of chroma** relative to the unmixed parent pigments. On a 3D color solid, any mixture line between two pigments passes through the interior of the solid, dropping below the outer boundary. Real pigment gamuts fall well short of Schrödinger's theoretical **[[Optimal Color Solid-MacAdam Limits|MacAdam limits]]** (the maximum achievable chroma for non-fluorescent surfaces) and exhibit severe asymmetries (e.g. greens reaching **[[Munsell Notation|Munsell Chroma]]** ~34 while reds peak near 20). Compared to RGB digital displays, physical paint mixtures lose the most saturation in the cyan-blue and violet sectors (*"Choosing Colors (Live)"* — Color Nerd).

### 4. Color Scheme Geometry & Scientific Critique

Traditional color harmony relies on geometric arrangements across a hue wheel:

- **Scheme families:** **Monochromatic** (variations in value/chroma of one hue), **Analogous** (adjacent wheel hues), **Complementary** (diametric opposites), **Split-Complementary** (a base hue plus the two neighbors of its complement), **Triadic** (equidistant 120° triangle), and **Tetradic / Rectangular** (four hues forming a rectangle).
- **Munsell's Value-Neutrality Critique:** Munsell argued that 2D wheel schemes are scientifically defective because they ignore value and chroma. True color balance requires **value-neutrality** — weighting hues by their value and chroma so their 3D center of gravity falls exactly on the neutral gray axis ($N 5/$) of the Munsell color tree.
- **Itten's Seven Contrasts & Relative Perception:** **[[Bauhaus|Johannes Itten]]** codified seven distinct contrast mechanisms: Hue, Light-Dark, Cold-Warm, Complementary, Simultaneous, Quality (saturation), and Quantity (area). **[[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing|Simultaneous contrast]]** demonstrates that the retina actively generates the complement of any fixated color, shifting adjacent colors and making color "the most relative medium in art".

### 5. Practical Painting Strategies

To manage mixing unpredictability and enforce harmony, painters rely on four empirical studio systems:

- **Complementary Underpainting (Verdaccio):** Applying a cool complementary underpainting (e.g. Terra Verte / Green Earth or umber) beneath warm flesh tones allows light to pass through translucent glazes, creating optical depth and natural chromatic grays that palette mixing cannot replicate.
- **Limited Palettes & The "Mother Color":** Restricting the palette to 3–5 pigments (e.g. the historical **Zorn palette**: Titanium White, **[[PY43 - Yellow Ochre|Yellow Ochre]]**, Vermilion/**[[PR108 - Cadmium Red|Cadmium Red]]**, Ivory Black) eliminates mud by constraining all mixtures to a shared, harmonious gamut hull. Adding a small amount of a single **"mother color"** to every mixture on the palette unifies the entire painting's spectral envelope.
- **Color Strings & Value Grids:** Pre-mixing "color strings" — systematic value and chroma ladders of a single hue string before painting — allows the artist to adjust hue, value, and chroma independently, avoiding palette guesswork (*"Choosing Colors (Live)"* — Color Nerd; *Carlson's Guide to Landscape Painting*).

## Handprint Perspectives

MacEvoy reframes paint mixing around the **"three-paint method" vs. the "four-paint wobble"** *(Source: [[raw_sources/handprint/mix.md|mix.html]])*. Any target color can be reached with at most three paints: two to define the primary mixing line (setting hue and maximum chroma) and one adjusting paint to shift value or lower chroma toward the center. Adding a fourth paint creates a unstable "wobble" around the target point that almost always results in mud.

On complementary colors, MacEvoy demonstrates that **visual complements and mixing complements are almost never the same** *(Source: [[raw_sources/handprint/color16.md|color16.html]])*. Visual complements (grounded in opponent-process vision) govern visual contrast and afterimages; mixing complements are the specific pairs of paints that cancel to an achromatic gray. For example, Ultramarine Blue's visual complement is a yellowish green, but its mixing complement is a dull deep yellow (or Raw Sienna); **[[PG7 - Phthalo Green|Phthalo Green]]**'s visual complement is Quinacridone Rose, but its mixing complement is a middle red. He codifies **three rules for mixing complements**:
1. Yellow paints (lemon to Hansa deep) are ineffective mixing complements for cool pigments.
2. All blues form mixing complements with deep yellow to middle red (and earth browns like raw umber).
3. All greens form mixing complements with deep red to violet; yellow-greens are neutralized by dioxazine violet.

*(Source: [[raw_sources/handprint/color16.md|color16.html]], [[raw_sources/handprint/mixtable.md|mixtable.html]])*.

## HueValueChroma Perspectives

Briggs provides the exact mathematical formulation of subtractive mixing *(Source: [[raw_sources/huevaluechroma/051.md|051.html]])*: subtractive interaction multiplies spectral reflectance wavelength by wavelength ($R_{\text{mix}}(\lambda) = R_1(\lambda) \times R_2(\lambda)$). Because multiplication operates across the whole spectrum, **exact mixture results cannot be predicted from hue alone** — two paints with identical visual hues can yield entirely different mixture hues if their secondary spectral transmission windows differ.

Briggs also dismantles Michael Wilcox's popular **"split-primary" theory** *(Source: [[raw_sources/huevaluechroma/062.md|062.html]])*. Wilcox claimed that paints fail to mix clean secondaries because they contain "impurities" of adjacent hues, requiring a "warm" and "cool" version of each primary. Briggs shows that this rationale is based on a false intermixture model: all yellow paints reflect red, orange, yellow, and green light (up to two-thirds of the spectrum), not a single hue with "impurities." Split-primary palettes work simply because they sneak in the true subtractive primaries (Cyan, Magenta, Yellow) alongside warm accent pigments *(Source: [[raw_sources/huevaluechroma/062.md|062.html]])*.

Finally, Briggs stresses that paint mixing is a **compound of subtractive filtering + additive-averaging** from particle back-scatter, which is why opaque paints can never mix a true pitch-black *(Source: [[raw_sources/huevaluechroma/041.md|041.html]], [[raw_sources/huevaluechroma/061.md|061.html]])*.

## Subtopics
- Subtractive Multiplicative Mechanics & Curved Mixing Paths
- Prediction Failures: Mud, Value Dominance & Refractive Index $\Delta n$
- Metamerism in Blends & Gamut Shortfalls
- Color Scheme Geometry & Munsell's Value-Neutral Balance
- Practical Studio Workflows: Verdaccio, Limited Palettes & Color Strings

## Cross-References
- [[Optical vs. Physical Mixture]]
- [[Perceptual Complements vs. Mixing Complements]] — the 3 rules of why visual and mixing complements differ
- [[Why CMY Beats RYB for Color Mixing]] — the primaries that actually span the mixing gamut
- [[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing]]
- [[Transparency, Opacity & Pigment Codes]]
- [[Media, Vehicles & Solvents]]
- [[Colors/Gamuts/Optimal Color Solid-MacAdam Limits|Optimal Color Solid-MacAdam Limits]]
- [[Pointer's Gamut]]
- [[Munsell Notation]]
- [[Composition]]
- [[The artist's color wheel]]

## Sources
* "Color for Science, Art, and Technology" — Kurt Nassau (editor)
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Artist's Handbook of Materials and Techniques" — Ralph Mayer
* "Interaction of Color: 50th Anniversary Edition" — Josef Albers
* "The Art of Color: The Subjective Experience and Objective Rationale of Color" — Johannes Itten
* "Color by Betty Edwards" — Betty Edwards
* "A Color Notation" — Albert H. Munsell
* "Contemporary Color: Theory and Use" — Steven Bleicher
* "Carlson's Guide to Landscape Painting" — John F. Carlson
* "Artists' Pigments: A Handbook of Their History and Characteristics" — Robert L. Feller (editor)
* "Illusions of Seeing" — Thomas Ditzinger
* "Choosing Colors (Live)" — Color Nerd
* "The Dimensions of Colour" — David Briggs ([[raw_sources/huevaluechroma/041.md|041.html]], [[raw_sources/huevaluechroma/051.md|051.html]], [[raw_sources/huevaluechroma/061.md|061.html]], [[raw_sources/huevaluechroma/062.md|062.html]])
