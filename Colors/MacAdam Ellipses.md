---
title: MacAdam Ellipses
sequence: 10
---
![[images/ChatGPT Image Aug 6, 2026, 02_29_42 PM.png]]

**Scope:** Details MacAdam ellipses and their mapping of just-noticeable differences in color.

Human color discrimination is highly non-uniform across the visible spectrum. The primary mathematical visualization of this non-uniformity is the **MacAdam ellipse**, which identifies regions of a color space within which all colors are perceived as identical to a central reference color.

### 1. The 1942 Color-Matching Experiments

In **1942**, David MacAdam published a landmark study in the *Journal of the Optical Society of America* investigating **just-noticeable differences (JNDs)** of chromaticity:

- **Experimental procedure:** MacAdam used a specialized **colorimeter** with a bipartite (split) circular field. One half displayed a fixed "test" color while the observer adjusted the other half to create a visual match.
- **Measuring variance:** rather than seeking the "average" match, MacAdam measured the **standard deviation of matching errors** across 25 different target colors. Because a match is never mathematically "perfect" due to visual noise, the range of (x, y) chromaticity coordinates the observer accepted as a match defined the discrimination threshold around each color.
- **Defining the ellipse:** when the matching errors were plotted on the **CIE 1931 xy chromaticity diagram**, they formed elliptical shapes; points on each ellipse's boundary represented chromaticities approximately one JND from the center color.

### 2. Variability of Size and Orientation

A key finding was that sensitivity to color change varies drastically across the chromaticity diagram:

- **Size disparity:** approximately a **10:1 ratio** exists between the largest and smallest ellipses. *(Note: the notebook sources demonstrate this non-uniformity through Munsell plots, where distances vary by a factor of ~3.86×.)*
- **Green vs. blue regions:** the ellipses are **largest in the green region** — the eye is relatively insensitive to changes in green chromaticity, and large physical shifts are needed before a difference is perceived. They are **smallest in the blue-violet region**, where the visual system is extremely sensitive to minute changes.
- **Orientation:** the ellipses "rotate" as they move around the diagram, their major axes generally pointing toward the red and blue corners, reflecting the underlying biological sensitivities of the L, M, and S cones.

### 3. JND Steps and Color Quantization

The ellipses highlight the "sampling limit" of human color vision and have major implications for digital imaging:

- **Traversing the diagram:** roughly **150 to 300 JND steps** (order-of-magnitude) are required to traverse the spectrum in terms of hue.
- **Quantization artifacts:** 8-bit quantization (256 levels per channel) often produces steps larger than one MacAdam ellipse, causing visible "banding" — **quantization artifacts**.
- **The 10-bit requirement:** although a 24-bit system theoretically yields 16.7 million colors, the eye can distinguish only about **1.4 million colors** in a standard display gamut. To keep quantization steps completely invisible in all regions (especially the sensitive blues), at least **10-bit quantization (1,024 levels)** is required.

### 4. Motivation for Perceptually Uniform Spaces

MacAdam's work was the primary driver for **perceptually uniform color spaces** that "warp" the chromaticity diagram so that JND regions appear as perfect, equal-sized circles:

- **CIELAB and CIELUV (1976):** introduced by the CIE as a more uniform "color difference ruler".
- **MacAdam's uv diagram:** before 1976, MacAdam proposed the **CIE 1960 UCS (Uniform Chromaticity Scale)** with u and v coordinates to linearize visual distances.
- **ΔE calculation:** in uniform spaces, the distance between two points — **ΔE** — quantifies perceived difference, with a value of **1.0** typically representing one JND.

### 5. Relationship to the Munsell System

The Munsell system (1905) was the first major attempt at a perceptually uniform color order based on visual judgments:

- **Comparison:** a circle of constant Munsell chroma plotted on the CIE xy diagram appears as a highly distorted, elongated oval. The distance between Munsell steps in the green-yellow region is **3.86 times greater** than the same perceived step in the purple-blue region on the xy diagram.
- **Munsell Renotation (1943):** used MacAdam's insights to anchor the Munsell system to precise CIE coordinates, making its visual spacing scientifically rigorous.

### 6. Insights into Human Discrimination and Industry Impact

MacAdam ellipses reveal the functional architecture of the eye:

- **Hue discrimination:** discrimination is **finest near 495 nm (blue-green) and 590 nm (yellow-orange)** and **worst in the deep greens** — an evolutionarily adaptive arrangement, allowing finer discrimination in regions critical for identifying natural resources and daylight changes.
- **Industry standards:** these thresholds are fundamental to quality control in the **textile, paint, and plastics industries**. Because inspectors are "least tolerant of hue differences" compared with lightness or chroma, industrial tolerances often plot as elongated **acceptability ellipsoids** in CIELAB space, directly mirroring MacAdam's original findings.

## Handprint Perspectives

MacEvoy's hue-circle analyses independently confirm MacAdam's pattern of discrimination. The spacing of spectral hues around the color circle shows **increased wavelength discrimination around the "yellow" and "cyan" wavelengths**, and **decreased discrimination at the spectrum ends and in the "green" wavelengths** — the same fine regions (roughly 495 nm and 590 nm) and the same insensitive green region that MacAdam's ellipses expose. He also notes the strong tinting effect of "violet" light in mixtures of red and violet hues, and points out that this scaling vindicates Newton's original hue scaling, developed with the crudest light-manipulation tools. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

## Subtopics
- JND & Color Matching
- Ellipse Size and Orientation
- Quantization Limits
- Uniform Color Spaces
- Munsell & Industry

## Cross-References
- [[CIE Systems]]
- [[Munsell Notation]]
- [[Why Lab-Munsell Were Built for Perceptual Uniformity]]
- [[Gamuts]]
- [[Color Matching Functions and the Photopic Luminosity Function]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer