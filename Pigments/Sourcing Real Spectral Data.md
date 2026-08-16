---
title: Sourcing Real Spectral Data
sequence: 17
---
![[Pasted image 20260811174721.png]]

**Scope:** Sourcing real spectral data — how reflectance curves of paint films are measured, archived, and used to fingerprint pigments and map gamuts.

### Reflectance Spectrophotometry and the Drying Shift

- **Non-destructive reflectance measurement:** a spectrophotometer directs light of known intensity at specific wavelengths onto a pigment layer and records the percentage reflected — a **spectral reflectance curve** unique to each colorant (red: high reflectance at long wavelengths; blue: peak at the short end), typically 380–780 nm or 400–700 nm.
- **The drying shift:** color is not inherent to the pigment but depends on its environment. Dry particles mixed into liquid binder dry "darker and deeper in tone": the binder's index (linseed oil ≈1.48) is much closer to the pigment's than air (1.00), reducing surface reflection so more light is absorbed. Watercolors look more translucent when wet — the water-to-air index change makes the hiding-power change dramatic upon drying.

### Databases and Standards

- **Munsell Renotation (1943):** formalized the color order system with precise **CIE (Y, x, y) coordinates** for ideal chips from millions of visual judgments — "establishing the empirical limits of achievable object colors under standard illumination (Illuminant C)".
- **Spectral libraries (RIT MCSL):** the `real.dat` file of real colors within physical limits, `1929.dat` for the original 1929 Munsell Book colors, and spectral data for common targets — Macbeth ColorChecker, CERAM tiles.
- **Imaging standards:** standard observers and standardized illuminants (**D65** for average daylight) as the baseline for all spectral calculations.

### Fingerprinting and Gamut Maps

- **Pigment identification ("fingerprinting"):** comparing an unknown sample's curve with reference curves identifies the colorant — e.g., **smalt vs. [[PB28 - Cobalt Blue|cobalt blue]]**, distinguishable because cobalt blue "has a higher reflectance in the red region".
- **Terminal dating:** pigments have introduction/discontinuation dates — **[[PR108 - Cadmium Red|cadmium red]]** (c. 1910) on a painting "purported to be from 1600" is direct forgery evidence.
- **Gamut maps:** spectral data builds the "three-dimensional volume of color a specific set of pigments can achieve" — the irregular "**color tree**" — with the **Pointer Gamut** as the scientific reference for "the maximum achievable gamut of over 4,000 real-world surface colors".

## Handprint Perspectives

MacEvoy's practice is the artist-facing half of this methodology: he has "conducted exhaustive, spectrophotometer-based testing of hundreds of commercial watercolor paints," converting measurements into CIELAB coordinates to build "an objective, empirical atlas of pigment behavior, replacing the subjective marketing claims of paint manufacturers." The drying-shift phenomenon above is exactly why he measures dried films and reports the "exact hue angle and lightness shifts of pigments as they dry"; his charts let painters build palettes "based on actual physical performance rather than abstract theory," including true boundaries of pigment gamuts and the realities of optical vs. physical mixture *(Source: [[raw_sources/handprint/pigmt8.md|pigmt8.html]])*.

## Subtopics
- Reflectance curves 380–780 nm; fingerprint uniqueness (red long-wave, blue short-wave)
- The drying shift: binder index ≈ pigment index → darker/denser dry color
- RIT MCSL libraries: real.dat, 1929.dat, ColorChecker, CERAM; Illuminant C baseline
- Fingerprinting (smalt vs cobalt) and terminal dating (cadmium red c. 1910)
- Gamut maps, the color tree, and the Pointer Gamut reference (4,000+ surfaces)

## Cross-References
- [[Pigments/index|Pigments]] — the cluster hub
- [[Data & Methodology]] — instruments and protocols behind these measurements
- [[High-Chroma Synthetics]] — the pigments the data must tame
- [[Pointer's Gamut]] — the reference hull for real surface colors
- [[Colors/Gamuts/index|Gamuts]] — from pigment data to gamut volume

## Sources
* "Artists' Pigments: A Handbook of Their History and Characteristics" — Robert L. Feller
* "The Science of Paintings" — W. Stanley Taft Jr.
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* Munsell Color Science Lab Educational Resources — Rochester Institute of Technology
* "Color Management: A Comprehensive Guide for Graphic Designers" — John Drew & Sarah Meyer
* "Why Material Reality Favors Green Over Red: The Physical Chemistry of Chromatic Limits"
* "Ordering Colour: Albert Henry Munsell (1858–1918)" — The Eclectic Light Company