![[images/ChatGPT Image Aug 6, 2026, 02_46_29 PM.png]]

**Scope:** Discusses the Optimal Color Solid and MacAdam Limits of maximum achievable reflecting colors.

In color science, the **optimal color solid** represents the theoretical maximum range of colors achievable by any non-fluorescent reflecting surface. Its boundaries, the **MacAdam limits**, define the ultimate physical ceiling for material color saturation at every level of lightness.

### 1. Concept of Optimal Colors

**Optimal colors** are hypothetical reflecting surfaces with idealized reflectance curves. Unlike real pigments (which have gradual absorption slopes), an optimal color's spectral reflectance takes only two values: **0% or 100%**. This "0–1" step function maximizes **chroma** because it ensures maximum spectral purity: the material reflects a specific band of wavelengths with total efficiency while suppressing all others completely. Any wavelength added outside the primary band, or any reduction of reflectance within it, would desaturate the color or lower its luminance.

### 2. Historical Development: Schrödinger and MacAdam

- **1919–1920 — Erwin Schrödinger** mathematically derived the properties of these "ideal" pigments, proving that an optimal surface's reflectance spectrum must have **at most two transitions** (discontinuities) between 0 and 1 across the visible range.
- **1935 — David MacAdam** performed the rigorous calculations mapping these limits into the CIE 1931 color space, providing the specific **(x, y) chromaticity coordinates for optimal colors at every level of Y (luminance factor)** — effectively defining the surface of the maximum possible color solid for human vision.

### 3. Shape and Asymmetry of the Optimal Color Solid

The three-dimensional shape is often described as a **lopsided top** or **distorted spindle**, with significant **asymmetry favoring the green-yellow region at high lightness levels**:

- **The green-yellow protrusion:** because the **luminosity function V(λ) peaks near 555 nm**, a green surface reflecting a band around this peak (e.g., **500–570 nm**) achieves high luminance and high chroma simultaneously.
- **The red and blue constraints:** saturated red and blue-violet hues are restricted to much lower lightness. A red surface reflecting only above 600 nm has very low luminance, since the eye's sensitivity there is low (**V(λ) ≈ 0.1–0.3**); making a red "lighter" requires adding other wavelengths, which desaturates the hue.
- **Boundaries:** the solid's base is ideal black (Value 0), its apex ideal white (Value 10), and its "equator" the most saturated colors at middle lightness. The solid is contained within the **spectrum locus** (pure monochromatic lights) and the **line of purples** (mixture of the red and violet endpoints).

### 4. Mathematical and Physical Basis

Optimal colors fall into two classes of "banded" spectra:

- **Band-pass:** reflectance is 1 in a single central wavelength band and 0 elsewhere (producing hues like green or yellow).
- **Band-stop:** reflectance is 1 at both ends of the spectrum and 0 in a central band (producing non-spectral purples and magentas).

Mathematically these spectra are the **"extreme points" of the convex set of all possible reflectance spectra**. Their interaction with the human **opponent-process system** determines the final perceived chroma.

### 5. Relationship to Pointer's Gamut and Device Gamuts

The MacAdam limits act as the "outer shell" for all other color gamuts:

- **Pointer's Gamut (1980):** representing roughly **4,000 real-world surface colors** (flowers, textiles, paints), this is a significantly **smaller subset** of the optimal color solid. Real pigments cannot reach the MacAdam limits because of "impure" absorption and light scattering.
- **Munsell Renotation (1943):** the system includes "real" colors from the Munsell Book of Color and "unreal" extrapolated colors; the MacAdam limits determine which notations are physically realizable as surface colors.
- **Device gamuts:** most electronic displays and printing processes (like sRGB) fail to cover the more saturated regions of the optimal solid, particularly the cyan and yellow-green sectors.

### 6. Practical Significance and Applications

The optimal color solid is the **standard reference** against which the efficiency of all real pigments and reproduction systems is measured — it shows that the limits of material color are dictated by the **physics of light and the biology of the eye**, not just chemical engineering:

- **Color science:** researchers use the MacAdam limits to evaluate the performance of **spectral imaging** and color-matching functions.
- **Industry:** they define the "theoretical best" for developing new high-chroma organic pigments like **phthalocyanines**, which approach ideal step-function reflectance more closely than traditional earth pigments.
- **Evolutionary insight:** the solid's asymmetry mirrors the visual system's tuning for maximum **luminous efficiency** under daylight, enabling fine discrimination of vegetation and natural surfaces where green-yellow reflectances are abundant.

## Handprint Perspectives

MacEvoy organizes all of material color into **three chromaticity spaces** defined by maximum achievable hue purity: (1) the **physiological limits** of the retinal photoreceptors, produced by monochromatic lights (spectral hues); (2) the **ideal limits of perfectly reflecting colored materials**, defined as theoretical optimal colors; and (3) the **actual limits of the most saturated pure pigments or dyes** displayed in a transparent medium — the media gamut. The optimal color solid is thus the middle domain: real pigments can never escape it, and spectral lights are the only colors outside it. *(Source: [[raw_sources/handprint/tech13.md|tech13.html]])*

## Subtopics
- Optimal Colors
- Schrödinger & MacAdam
- Solid Shape
- Gamut Hierarchy

## Cross-References
- [[Pointer's Gamut]]
- [[Gamuts]]
- [[Device Gamuts]]
- [[CIE Systems]]
- [[MacAdam Ellipses]]
- [[History & Key Figures]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer