---
title: Data & Methodology
sequence: 3
---
![[Pasted image 20260810110552.png]]

**Scope:** The instruments, protocols, datasets, and calculation pipelines that turn physical reflectance and emission spectra into CIE colorimetry — and the caveats that limit them.

### Instruments and Measurement Protocols

Three instrument classes capture color data (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*, *Color Management: A Comprehensive Guide*, *The Measurement of Colour*):

- **Spectrophotometers** measure the **reflectance or transmittance factor** of objects at specific wavelength intervals; "abridged" instruments measure only selected wavelengths.
- **Spectroradiometers** measure the radiant energy of **self-luminous sources** — lamps and displays.
- **Colorimeters** measure chromaticity directly, using filters to simulate the response of a standard observer.

Protocol conventions in the sources:

- **Sampling:** intervals of 1 nm, 5 nm, 10 nm, or 20 nm across the visible band, generally **380–780 nm** (*Munsell Color Science Lab*).
- **Geometries:** for diffuse specimens the CIE recommends bidirectional geometries **0/45 and 45/0** (account for texture) and diffuse geometries **0/d and d/0** using integrating spheres (minimize gloss effects) (*The Measurement of Colour*).
- **Observers:** the **1931 2° Standard Observer** (foveal fields) or the **1964 10° Standard Observer** (larger industrial fields) (*A Comprehensive Overview...*).
- **Illuminants:** D65 (average daylight), D50 (graphic arts), Illuminant A (tungsten) as the reference conditions (*The Measurement of Colour*).

### The Standard CIE Calculation Pipeline

Physical spectra become device-independent tristimulus values through one summation — **X = k·Σ[P(λ)·x̄(λ)·R(λ)·Δλ]** — where P(λ) is the illuminant's spectral power, x̄(λ) the color matching function, and R(λ) the sample reflectance (*A Comprehensive Overview..., The Measurement of Colour*). Two components complete it:

- **Normalization constant k = 100/Σ[P(λ)·ȳ(λ)]**, fixed so that the Y value (luminance) equals **100 for a perfect white diffuser** (*The Measurement of Colour*).
- **Color matching functions x̄, ȳ, z̄** represent "the averaged spectral responsivity of the human eye's long, middle, and short-wave cones" (*A Comprehensive Overview..., The Science of Paintings*).

### The Classic Datasets Behind This Wiki

- **1943 Munsell Renotation:** a correction of Munsell's system based on "three million visual observations by 41 observers," supplying precise CIE coordinates for visually uniform spacing (*A Comprehensive Overview..., Munsell Color Science Lab*).
- **Pointer's 1980 study** ("The Gamut of Real Surface Colours"): catalogued **4,088 real surfaces** under Illuminant C to establish empirical limits of surface colors (*A Comprehensive Overview...*).
- **MacAdam Limits (1942):** theoretical boundaries of optimal colors — "the most saturated surface colors physically possible" (*A Comprehensive Overview..., The Science of Paintings*).
- **RIT Munsell Lab:** provides complete **1 nm datasets** for standard illuminants and observers, including the 1988 spectral luminous efficiency functions (*Munsell Color Science Lab*).

### Methodological Caveats

- **Observer variation:** every individual has unique cone sensitivities; the "Standard Observers" are only averages "and may not match any single person perfectly" (*Vision Science: Photons to Phenomenology*, *A Comprehensive Overview...*).
- **Instrument differences:** spectral **bandpass width** matters — "a 20 nm bandpass might fail to capture sharp spectral peaks seen in a 1 nm measurement" (*The Measurement of Colour*).
- **Fluorescence effects:** fluorescent materials re-emit absorbed energy at longer wavelengths, "potentially producing reflectance factors >100%"; they require strict UV control and bidirectional geometry, "because integrating spheres can suppress their efficiency" (*The Measurement of Colour*).
- **Sampling artifacts:** sample preparation, surface texture, and **thermochromism** (color change with temperature) cause reproducibility errors (*The Measurement of Colour*, *A Comprehensive Overview...*).

## Handprint Perspectives

MacEvoy's measurement warning is aimed at the same bandpass problem from the painter's side: spectral data only means what the instrument could resolve, and single-number summaries of a pigment's behavior (a brand's masstone swatch, an RGB triple) conceal the full reflectance structure that governs mixtures, lightfastness, and metamerism. This is why objective pigment analysis requires full reflectance curves — the "spectral fingerprint" that survives changes of illuminant, while any trichromatic summary is hostage to the viewing conditions under which it was measured *(Source: [[raw_sources/handprint/color13.md|color13.html]], [[raw_sources/handprint/tech13.md|tech13.html]])*.

## Subtopics
- Instruments: spectrophotometer (reflectance/transmittance), spectroradiometer (sources), colorimeter (filtered chromaticity)
- Protocols: 1–20 nm sampling over 380–780 nm; 0/45, 45/0, 0/d, d/0 geometries; 1931 2° vs. 1964 10° observers
- CIE pipeline: X = k·Σ P·x̄·R·Δλ with k = 100/Σ P·ȳ (Y = 100 at perfect white)
- Foundational datasets: Munsell 1943 (3M obs, 41 observers), Pointer 1980 (4,088 surfaces), MacAdam 1942, RIT 1 nm data
- Caveats: observer averaging, bandpass resolution, fluorescence >100% reflectance, sample/thermal artifacts

## Cross-References
- [[CIE Systems]] — the spaces the pipeline feeds
- [[Munsell Notation]] — the 1943 Renotation dataset
- [[Pointer's Gamut]] — the 4,088-surface empirical dataset
- [[MacAdam Ellipses]] and [[Optimal Color Solid-MacAdam Limits]] — the 1942 datasets
- [[Sourcing Real Spectral Data]] — instruments in the pigment workflow
- [[Natural Daylight Variation & Hyperspectral Scene Data]] — hyperspectral acquisition

## Sources
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "The Measurement of Colour" — R.W.G. Hunt
* "Color Management: A Comprehensive Guide for Graphic Designers" — John T. Drew and Sarah A. Meyer
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "Vision Science: Photons to Phenomenology" — Stephen E. Palmer
* "Munsell Color Science Lab Educational Resources" — Rochester Institute of Technology