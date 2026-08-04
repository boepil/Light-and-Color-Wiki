# Pointer's Gamut

**Scope:** Analyzes Pointer's Gamut of real surface colors.

## Subtopics
- Empirical Gamut of Real Colors
- Comparison with MacAdam limits

## Cross-References
- [[Gamuts]]

## Synthesized Content

A **gamut** is the actual range of color that a specific system or material can reproduce (**Contemporary Color**).

*   **Pointer's Gamut:** Established in a landmark 1980 study, this gamut represents the maximum achievable range of **real surface colors** (paints, inks, textiles, etc.) under Illuminant C (**Why Material Reality Favors Green Over Red...**, **Munsell Color Science Lab...**). It confirms that the real-world color space is smaller than the MacAdam limits and remains systematically smaller in the red region compared to the green region (**Why Material Reality Favors Green Over Red...**).
*   **Device Gamuts:** 
    *   **Additive (RGB):** Used by monitors and displays; the gamut is typically a triangle within the CIE diagram defined by the chromaticities of the red, green, and blue phosphors or filters (**Contemporary Color**, **color-for-science-art-and-technology.pdf**). 
    *   **Subtractive (CMYK):** Used in printing; these gamuts are smaller and irregularly shaped due to the absorption limitations of physical pigments and substrates (**Contemporary Color**, **color-for-science-art-and-technology.pdf**). 
    *   **Management:** To bridge these disparate gamuts, **ICC profiles** are used to translate color data from a device's native space into a device-independent space like CIELAB, then back to a different device's gamut (**Contemporary Color**).
