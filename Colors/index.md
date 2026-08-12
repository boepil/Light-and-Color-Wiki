---
title: Colors
aliases: [Colors]
sequence: 7
---

**Scope:** The mathematical and empirical frameworks that standardize, measure, and reproduce color — the CIE's XYZ and Lab systems, the MacAdam ellipses of just-noticeable differences, Munsell's perceptual ordering, and the gamut boundaries of real and optimal colors.

### [[CIE Systems|Colors/CIE Systems]]
The **Commission Internationale de l'Eclairage (CIE)** established the first international colorimetric standards in 1931 to replace subjective color naming with mathematical algorithms. Because real RGB primaries require "negative" light to match some saturated colors, the CIE created **imaginary primaries (X, Y, Z)** to keep all color-matching functions positive; **Y** is set equal to the luminosity curve V(λ). Two standard observers exist: the **CIE 1931 2°** and the **1964 10°**. The 2D **xy chromaticity diagram** traces the horseshoe-shaped **spectral locus** of monochromatic lights (380–780 nm). CIELAB (1976) is a more uniformly opponent space: **L\*** (lightness 0–100), **a\*** (red–green), **b\*** (yellow–blue), and serves as a device-independent "universal translator" (*Color Management*, *Color for Science, Art, and Technology*).

### [[Munsell Notation|Colors/Munsell Notation]]
Albert H. Munsell (1905) organized color into three perceptual dimensions: **Hue** (five principal and five intermediate hues), **Value** (lightness, 0/ black to 10/ white), and **Chroma** (departure from neutral of the same value, an open-ended scale). The **1943 Munsell Renotation** anchored every chip to precise CIE (Y, x, y) coordinates through ~3 million visual observations; it showed that **constant-chroma loci expand dramatically at very dark values**, so dark colors can reach very high saturation (*A Comprehensive Overview*, *A Color Notation*).

### [[MacAdam Ellipses|Colors/MacAdam Ellipses]]
**MacAdam ellipses** are regions on the chromaticity diagram within which colors are visually indistinguishable from the central color. Their widely varying sizes across the diagram quantify the diagram's **lack of visual uniformity**: a given geometric distance in xy space does not correspond to a constant perceived difference. This non-uniformity motivated perceptually uniform spaces such as CIELAB and CIELUV, whose metric distance (**ΔE**) is designed so that equal steps correspond to equal just-noticeable differences (*Color Science*).

### [[Gamuts|Colors/Gamuts]]
A **gamut** is the full range of colors a system or material can reproduce. Real-world color is bounded by a hierarchy: the eye's ~7 million distinguishable levels, the theoretical **Optimal Color Solid (MacAdam limits)** of 0/100% step-function reflecting surfaces, real-surface **Pointer's Gamut**, and the smaller device gamuts of RGB displays and CMYK printers. Because the human luminosity function V(λ) peaks near **555 nm**, the optimal color solid is **lopsided**: green hues can achieve chroma at high lightness, while red hues must trade lightness for purity (*Why Material Reality Favors Green Over Red*). Device gamuts are triangular (RGB) or irregular (CMYK) and are bridged by **ICC profiles** that translate native coordinates through device-independent CIELAB (*Contemporary Color*).

### [[Device Gamuts|Colors/Gamuts/Device Gamuts]]
A device's gamut is fixed by its primaries: additive displays use red/green/blue phosphors or filters (e.g. sRGB), while printers use the smaller, irregular gamut of CMYK pigments whose lightness is capped by the paper white point. Because subtractive inks add unwanted absorptions, **CMYK covers only a fraction of the RGB gamut** — print gamuts are roughly a third of CIELAB, and a "millions of colors" monitor can show purples, reds, and greens that are unmixable in CMYK. **ICC profiles** and rendering intents map data between device spaces and device-independent CIELAB (*Contemporary Color*).

### [[Optimal Color Solid-MacAdam Limits|Colors/Gamuts/Optimal Color Solid-MacAdam Limits]]
The **Optimal Color Solid** defines the theoretical limits of non-fluorescent surface colors: the greatest chroma for a given hue and lightness is reached by **step-function reflectance spectra** that are 0% or 100% at every wavelength. Because the luminosity function V(λ) peaks in the green-yellow (~555 nm), the solid is **asymmetric** — green hues achieve very high chroma at high lightness while reds are constrained (*Why Material Reality Favors Green Over Red*).

### [[Pointer's Gamut|Colors/Gamuts/Pointer's Gamut]]
**Pointer's Gamut**, from a 1980 study of over 4,000 real surfaces (paints, inks, textiles, minerals, flowers) under Illuminant C, is the maximum color range achievable by real surface pigments. It sits well inside the MacAdam limits and is systematically **smaller in the red than in the green** region, again reflecting the V(λ) peak; even sRGB exceeds it in some cyan/green directions (*Why Material Reality Favors Green Over Red*).

## Related Intersections
* [[Why Lab-Munsell Were Built for Perceptual Uniformity|Intersections/Why Lab-Munsell Were Built for Perceptual Uniformity]]

## Sources
* "Color Science" — Wyszecki & Stiles
* "Contemporary Color: Theory and Use" — Steven Bleicher
* "Color for Science, Art, and Technology" — Kurt Nassau (editor)
* "Color Management: A Comprehensive Guide for Graphic Designers" — John T. Drew and Sarah A. Meyer
* "A Color Notation" — Albert Henry Munsell
* "Munsell Renotation Table" — NotebookLM source
* "Why Material Reality Favors Green Over Red: The Physical Chemistry of Chromatic Limits" — NotebookLM source