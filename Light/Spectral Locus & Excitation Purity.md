---
title: Spectral Locus & Excitation Purity
sequence: 24
---
![[Pasted image 20260810103513.png]]

**Scope:** The spectral locus as the physical boundary of all real colors on the CIE chromaticity diagram, and excitation purity as the colorimetric measure of how close a color lies to that boundary.

### The Spectral Locus — Boundary of Real Colors

The **spectral locus** is the solid, horseshoe-shaped curved boundary of the CIE chromaticity diagram: the set of chromaticity coordinates of all **monochromatic (single-wavelength) lights** (*Color for Science, Art, and Technology*, *The Science of Paintings*).

- The curve runs from the shortest visible wavelengths — **~380–400 nm violet** — along the top and right side to the longest visible wavelengths — **~700–780 nm red**; "here the saturated (pure, most intense) colors of the spectrum occur on the curved line extending from red to violet" *(Source: "Color for Science, Art, and Technology")*.
- The middle of the curve is **bowed outward** because pure spectral colors — 520 nm green, for example — are the most saturated colors physically possible; any additive mixture of wavelengths necessarily falls *inside* the curve, closer to the white center (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*).
- Every physically perceivable chromaticity lies inside the region bounded by the locus and the **line of purples** — the locus is the outer envelope of human color vision (*The Science of Paintings*).

### The Line of Purples — Extraspectral Colors

The **line of purples** is the straight line closing the horseshoe across its bottom, connecting the extreme red and violet ends of the locus (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*).

- It is **straight** because the colors on it — **purples, magentas, deep reds** — are **non-spectral / extraspectral**: no single wavelength produces them, so they cannot sit on the smooth spectral curve itself; they exist only as mixtures of the two ends of the visible spectrum (red + blue/violet light) (*Color for Science, Art, and Technology*, *The Science of Paintings*).
- Technically these hues are "awkward to specify" by wavelength, so they are conventionally notated by the wavelength **directly opposite on the hue circle**: an extraspectral magenta is written as its complementary green wavelength, **c560** *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*.

### Dominant Wavelength — Mapping a Color to the Locus

The **dominant wavelength** of a color is found by drawing a straight line from the **white point (W)** through the sample's point on the diagram and extending it to the spectral locus; the wavelength at which that line intersects the locus is the dominant wavelength ([λD]), the single spectral light that matches the sample's **hue** (*Color for Science, Art, and Technology*).

- **Complementary wavelengths** are pairs whose additive mixture is white. Geometrically: any straight line through the central white point connects two complementary points on the locus — for example, appropriate amounts of **~480 nm blue + ~580 nm yellow** mix to white (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*).
- Purple (extraspectral) samples never intersect the spectral locus on the extension toward red-violet; their line meets the locus on the opposite side, giving a **"complementary dominant wavelength"** labeled with a **c** suffix — e.g. a purple beam at (0.33, 0.15) has 540c, a complementary dominant wavelength of 540 nm (*Color for Science, Art, and Technology*).
- MacEvoy's practical gloss: hue is "the attribute of color matched by a single wavelength of light or by a mixture of 'violet' and 'red' wavelengths of light" — a pure yellow carrying the wavelength notation **575**, and a brown light being a near-neutral dark orange with a dominant wavelength around **610 nm** *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*.

### Excitation Purity — the "Law of the Lever" Ratio

**Excitation purity** (colorimetric purity) is the physical measure of how much monochromatic light a color contains, computed as a **distance ratio** on the diagram — the "law of the lever" relative to the white point (*Color for Science, Art, and Technology*).

- Geometry: **W** = white point, **C** = the color being measured, **A** = the point on the spectral locus at the dominant wavelength. Then purity = **100·a/(a+w)**, where **a** is the distance W→C and **w** is the distance C→A (*Color for Science, Art, and Technology*). The locus is the set of **100% purity** points; the white point is **0%**; whites/grays anchored by **D65** (average daylight) or the **equal-energy point E** give the 0 % reference.
- Worked examples from the textbook: a beam with coordinates **(0.20, 0.45)** has dominant wavelength **510 nm** and purity **30 %**; a purple beam at **(0.33, 0.15)** has complementary dominant wavelength **540c** and purity **70 %** (*Color for Science, Art, and Technology*).
- Purity is a **physical ratio of spectral content**, not perceived saturation: the CIE 1931 xy diagram is not visually uniform, so "the same distance in the blue region represents a much smaller visual change than in the green region" — colors of equal excitation purity appear differently saturated (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*, *Vision Science: Photons to Phenomenology*).

## Handprint Perspectives

MacEvoy classifies the third color-making attribute as **hue purity** — the "concentration or intensity of hue independent of its luminance or lightness." He lists the terminological sprawl scientists have used for it — **Sättigung, colorfulness, chromaticness, chroma, saturation, excitation purity, colorimetric purity, chromatic content, brilliance** — each definition "anchored to a specific stimulus attribute or color comparison," and reassures painters they may use *chroma* or *saturation* interchangeably without worrying about the technical distinction. His painter-oriented use of the locus: every hue spoken of in the studio "can usually be matched by the color of a single wavelength of light, called the dominant wavelength," and learning correct hue designations for dull colors (brown = near-neutral dark orange, ~610 nm) directly aids mixing. On lightness, he notes that as surface colors become lighter, purple/blue/green hues contract toward the white point while yellow-green through red hues "remain at maximum saturation, along the spectrum locus" — the warm colors' "warm cliff" reflectance behavior keeps them at the boundary of the color solid even when light *(...Source: [[raw_sources/handprint/color18a.md|color18a.html]], [[raw_sources/handprint/color12.md|color12.html]])*.

> [!NOTE] **Purity is colorimetric, not perceptual:** excitation purity is a ratio of distances in a necessarily non-uniform plane — a given purity figure does not predict how saturated the color *looks*. The xy-diagram's blue-region compression (see [[Colors/MacAdam Ellipses|MacAdam Ellipses]]) is why equal-purity blues look muted next to equal-purity greens.

## Subtopics
- Geometry of the horseshoe: monochromatic boundary, bowed-out middle, endpoints ~380–400 nm to ~700–780 nm
- Line of purples as the extraspectral closing edge (purples, magentas, deep reds; notation such as **c560**)
- Dominant wavelength construction from the white point; complementary pairs (~480 nm + ~580 nm) and the **c** suffix for extraspectral hues
- Excitation purity as the lever ratio **100·a/(a+w)**; loci of purity: 100% at the spectral locus → 0% at W (D65, equal-energy E)
- Purity vs. perceived saturation under CIE xy non-uniformity

## Cross-References
- [[CIE Systems]] — the xy diagram that hosts the locus
- [[The Visible Spectrum]] — the wavelength range the locus traces
- [[MacAdam Ellipses]] — the perceptual non-uniformity that decouples purity from saturation
- [[Colors/Gamuts/index|Gamuts]] and [[Optimal Color Solid-MacAdam Limits]] — the locus and line of purples as the outer envelope of every gamut
- [[Illuminants & Correlated Color Temperature]] — the white points (D65, E) anchoring purity
- [[Natural Light Gamut vs. Pigment Gamut - Metamerism]] — locus purity vs. pigment metamerism

## Sources
* "Color for Science, Art, and Technology" — Kurt Nassau (editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Vision Science: Photons to Phenomenology" — Stephen E. Palmer