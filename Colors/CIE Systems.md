# CIE Systems

**Scope:** Overview of CIE coordinate systems including the xy diagram, XYZ, and Lab spaces.

## Subtopics
- CIE xy Chromaticity Diagram
- CIE XYZ
- CIE Lab

## Cross-References
- [[Spectral Locus & Excitation Purity]]
- [[Color Matching Functions and the Photopic Luminosity Function]]
- [[Why Lab-Munsell Were Built for Perceptual Uniformity]]

## Synthesized Content

The **Commission Internationale de l’Eclairage (CIE)** established the first international standards for colorimetry in 1931 to replace subjective identification with mathematical algorithms (**Contemporary Color**).

*   **CIE XYZ and Standard Observers:** The system was founded on color-matching experiments where observers matched spectral wavelengths using three primaries. Because real RGB primaries required "negative" light to match certain saturated colors, the CIE created imaginary "ideal" primaries—**X, Y, and Z**—to ensure all color-matching functions remained positive (**color-for-science-art-and-technology.pdf**). The **CIE 1931 2° Standard Observer** represents the foveal region of the eye, while the **1964 10° Standard Observer** was developed for larger viewing fields typical in industrial settings (**color-for-science-art-and-technology.pdf**, **Color Management**).
*   **CIE xy Chromaticity Diagram:** This 2D diagram is a projection of the 3D XYZ space where $x$ and $y$ coordinates are calculated from tristimulus values (**color-for-science-art-and-technology.pdf**). It features a horseshoe-shaped **spectral locus** representing pure monochromatic lights from 380 nm to 780 nm (**The Science of Paintings**, **color-for-science-art-and-technology.pdf**). The central **"E" or "W" point** represents the achromatic white point (**Contemporary Color**, **color-for-science-art-and-technology.pdf**).
*   **CIELAB (L*a*b*):** Introduced in 1976, this space was designed to be more **perceptually uniform** than xy space (**color-for-science-art-and-technology.pdf**). It utilizes an **opponent-color** framework: **L*** represents lightness (0 to 100), **a*** represents the red-green axis, and **b*** represents the yellow-blue axis (**color-for-science-art-and-technology.pdf**, **Contemporary Color**). It is a **device-independent** model, acting as a "universal translator" between different hardware platforms (**Contemporary Color**).

## Handprint Perspectives

Handprint views modern CIE systems, particularly CIELAB and CIECAM, as the most accurate tools available for mapping human perceptual color space, praising their foundation in objective spectrophotometric measurement rather than subjective artistic lore. 

**Contradiction Flag: Perceptual Uniformity vs. Mixture Predictability.** 
While CIELAB excels at *perceptual uniformity* (ensuring that equal steps in the model look equally different to the human eye), MacEvoy explicitly warns against assuming this grants it *mixture predictability*. Because the subtractive mixing of pigments introduces nonlinear saturation costs, a uniform perceptual space cannot be used to mathematically predict the outcome of combining two physical paints. The model perfectly maps what we see, but it does not map how paints physically behave when mixed. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

