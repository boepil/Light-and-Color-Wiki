---
title: Causal Chain - Pigments to Perception
sequence: 78
---
![[Pasted image 20260808153904.png]]

**Scope:** Tracing the causal sequence connecting the physical reflectance spectra of pigments, the human biological response defined by CIE color-matching functions and photopic luminosity, the empirical boundaries of Pointer's Gamut, and the final perceptual experience of color asymmetry.

### Physical Foundation: Spectral Reflectance of Surfaces
The chain begins with the **spectral reflectance** of physical surfaces. The theoretical maximum saturation (chroma) a non-fluorescent material can achieve at any lightness level is governed by **optimal colors**ג€”hypothetical surfaces that reflect light with 100% efficiency in specific bands and absorb 100% elsewhere, creating a binary "0 or 1" step-function profile (**Wyszecki & Stiles**) [1, 2]. 

Real-world pigments, however, exhibit gradual absorption slopes, chemical impurities, and light scattering (**Wyszecki & Stiles**) [22]. These physical properties prevent real materials from reaching the theoretical limits of optimal color spectra, ensuring that all physical colors remain a subset of these ideal mathematical boundaries [23].

### Biological Bridge: CIE Color-Matching and the Luminosity Function $V(\lambda)$
When light reflects off these surfaces, it is filtered by the human visual system. The biological sensitivity of the human eye is standardized via the **CIE color-matching functions** and the photopic luminosity function **$V(\lambda)$**, which peaks at **555 nm** in the green-yellow region of the spectrum (**Wyszecki & Stiles**) [4, 9]. 

This biological tuning establishes a major asymmetry in how we integrate physical light into perceived lightness and chroma:
*   **Green-Yellow Protrusion:** Because $V(\lambda)$ peaks at 555 nm, surfaces reflecting light in this region stimulate the eye's luminance channel with extreme efficiency, allowing them to appear both highly saturated and very light simultaneously (**Wyszecki & Stiles**) [4, 9].
*   **Red-Blue Constraints:** Red pigments reflect light above 600 nm, where eye sensitivity drops dramatically ($V(\lambda) \approx 0.1 \text{ to } 0.3$) [4]. To make a red pigment perceptually lighter, more wavelengths must be reflected (broadening the band), which mathematically and perceptually dilutes the chromatic purity (desaturating the color) [4, 11].

### Empirical Constraints: Pointer's Gamut
The intersection of physical pigment limitations and human biological sensitivity yields the empirical boundaries of real-world color. In 1980, Michael Pointer measured over 4,000 physical surface colors (flowers, paints, inks, minerals) to map **Pointer's Gamut** (**Pointer**) [4, 5]. 

Pointer's Gamut represents the real-world boundaries of color under standard CIE Illuminant C (**Pointer**) [6]. It inherits the lopsided asymmetry of the $V(\lambda)$ sensitivity curveג€”extending deeply into high-chroma greens and oranges, but shrinking significantly in the reds and blue-violet regions [4, 8].

### The Perceptual Experience of Asymmetry
The final link in the chain is our **perceptual experience** of color. The visual system's opponent-process coding coordinates lightness and chroma along yellow-blue and red-green axes, translating these physical-biological constraints into our experience of natural color spaces (**Wyszecki & Stiles**) [11, 19]. 

This uneven distribution of saturation and lightness across the hue circle is not a defect, but an evolutionary adaptation; the visual system's tuning for maximum luminous efficiency in daylight allows humans to make fine discriminations in vegetation and natural materials where green and yellow-green reflectances dominate (**Wyszecki & Stiles**) [11, 32].

## Handprint Perspectives
Bruce MacEvoy highlights that warm surface colors (red, orange, yellow) are unique within the MacAdam limits because they retain high chroma even as lightness increases. He explains this behavior by analyzing the **"warm cliff" reflectance curve** typical of these pigmentsג€”characterized by an abrupt rise in reflectance between cyan and orange, high reflectance on the red side, and low reflectance on the blue side. Because warm pigments closely mimic the step-functions of theoretical optimal colors, they can "retain saturation sideways" by widening their reflectance band without losing chromatic purity, a property cool pigments do not possess *(Source: [[raw_sources/handprint/color12.md|color12.html]])*.

## Subtopics
- Theoretical optimal colors vs. real-world pigment limitations
- Mathematical derivation of MacAdam limits from CIE tristimulus integration
- The role of $V(\lambda)$ in creating the green-yellow lightness-chroma protrusion

## Cross-References
- [[Colors/Gamuts/Optimal Color Solid-MacAdam Limits]]
- [[Colors/Gamuts/Pointer's Gamut]]
- [[Intersections/Color Matching Functions and the Photopic Luminosity Function]]
- [[Intersections/Natural Light Gamut vs. Pigment Gamut - Metamerism]]

## Sources
* "Color Science: Concepts and Methods, Quantitative Data and Formulae" ג€” Gunter Wyszecki & W.S. Stiles
* "The Gamut of Real Surface Colours" ג€” Michael R. Pointer
