---
title: Color Matching Functions and the Photopic Luminosity Function
sequence: 85
---
![[Pasted image 20260809130318.png]]

**Scope:** Cross-cutting page (Light × Eye) exploring how physical light is weighted by human biological sensitivity.

In mathematical colorimetry, **color matching functions (CMFs)** and the **luminosity function** are the essential bridge between the physical spectrum of light and the human perception of color and brightness. Established by the **[[CIE Systems|Commission Internationale de l'Éclairage (CIE)]]** in **1931**, they allow the visual effect of any light source to be calculated from its spectral power distribution.

### 1. Color Matching Functions (CMFs) and the RGB Experiments

The CIE 1931 CMFs were derived from **color-matching experiments** with a bipartite (split) field:

- **The procedure:** one half displayed a "test" monochromatic light of a specific wavelength; the other was illuminated by a mixture of three primaries — **Red (700 nm)**, **Green (546.1 nm)**, and **Blue (435.8 nm)**. Observers adjusted the primary intensities until the two halves matched in hue, saturation, and brightness.
- **The negative values:** real RGB primaries cannot match all spectral colors. For certain highly saturated wavelengths (particularly in the blue-green region), the test color appeared "too pure" to match by mixing; a primary (usually red) had to be added to the **test color side** of the field. Mathematically this was recorded as a **negative value** for that primary in the CMF.

### 2. The CIE 1931 Standard Observer (x̄, ȳ, z̄)

To eliminate negative numbers for industrial calculations, the CIE performed a linear transformation of the experimental RGB data, creating **x̄(λ), ȳ(λ), and z̄(λ)** — the CMFs of the "imaginary" XYZ primaries, which enclose all visible colors in a positive coordinate space.

The peaks for the **2° Standard Observer** (based on foveal vision):

- **z̄(λ) (blue-sensitive):** peaks at approximately **445–450 nm**.
- **ȳ(λ) (green-sensitive/luminance):** peaks at exactly **555 nm**.
- **x̄(λ) (red-sensitive):** a primary peak in the long-wavelength region at approximately **595–600 nm** and a secondary peak in the blue near **445 nm**.

### 3. The Photopic Luminosity Function V(λ)

**V(λ)**, the photopic luminosity function, represents the eye's relative sensitivity to perceived brightness under daylight (photopic) conditions:

- **Identity with ȳ(λ):** in the CIE XYZ system, **ȳ(λ) is defined to be identical to V(λ)** — the Y tristimulus value is the relative "luminance" of a color as perceived.
- **Measurement:** historical measurements used **flicker photometry** or **heterochromatic matching**, where observers compared the brightness of different colored lights to find an "equal energy" balance.
- **Peak sensitivity:** V(λ) peaks at **555 nm** in the yellow-green region — a peak that evolved to optimize vision under solar radiation, which itself peaks near 550 nm.

### 4. Deficiencies and Modifications

The original **1924 CIE V(λ)** (which became the ȳ of 1931) has known **deficiencies in the blue/violet region** (below 460 nm), where it significantly **underestimates** the eye's actual sensitivity. To address this, **Deane B. Judd** and **J.J. Vos** proposed modified functions; the **1988 V_M(λ)** is a supplemental spectral luminous efficiency function providing a more accurate representation of photopic vision in the short-wavelength (blue) region.

### 5. Applications in Colorimetry and Color Management

CMFs and the luminosity function are the foundation of all modern color calculations:

- **Computing tristimulus values:** the X, Y, Z values of an object are computed by integrating the source's spectral power (P), the object's reflectance (R), and the observer's CMFs: **X = k Σ P(λ) · x̄(λ) · R(λ)** (and likewise for Y and Z).
- **Chromaticity coordinates:** tristimulus values yield **(x, y) chromaticity coordinates**, x = X/(X+Y+Z), y = Y/(X+Y+Z), defining the **CIE xy diagram** whose curved edge is the pure spectral colors.
- **Device independence:** these functions underlie perceptually uniform spaces like **[[Why Lab-Munsell Were Built for Perceptual Uniformity|CIELAB]]**, enabling device-independent color management between cameras, monitors, and printers.

### 6. Scotopic Vision and the Purkinje Shift

Under low-light conditions the visual system switches from cones to **[[Rods vs. Cones - Density & Distribution|rods]]** — **scotopic vision**:

- **Scotopic luminosity function V′(λ):** the rod sensitivity curve is shifted toward shorter wavelengths, peaking at approximately **507 nm** in the blue-green region.
- **The Purkinje shift:** because the peak shifts, as light levels drop **blues and greens appear relatively brighter** while reds appear significantly darker or black.
- **Crossover:** rods provide **achromatic (monochromatic)** vision and predominate outside the fovea at angles greater than **4°**; they are far more sensitive than cones but deliver significantly lower spatial acuity.

## Handprint Perspectives

MacEvoy links the luminosity function directly to painterly practice. Hues near yellow-green reach their **peak chroma only at very high lightness**, while blue-violet hues reach peak chroma only when very dark — a relationship that "roughly matches the relative luminance of the individual hues as they appear in the spectrum," i.e., their contribution to the **photopic sensitivity function**. The major exceptions are violet to violet-red hues, which are spectral mixtures and appear brighter than spectral blue-violet. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

He also stresses the practical consequence of the photopic→scotopic peak shift (from **555 nm to ~510 nm**): the peak of sensitivity moves toward shorter wavelengths at night, so low-light viewing changes which colors appear brightest. *(Source: [[raw_sources/handprint/color12.md|color12.html]])*

## Subtopics
- Color Matching Experiments
- CIE 1931 CMFs
- V(λ) & Y
- Scotopic Vision

## Cross-References
- [[CIE Systems]]
- [[Spectral Locus & Excitation Purity]]
- [[Rods vs. Cones - Density & Distribution]]
- [[Wavelength Perception]]
- [[Natural Daylight Variation & Hyperspectral Scene Data]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
