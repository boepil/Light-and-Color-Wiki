---
title: Optimal Color Solid-MacAdam Limits
sequence: 58
---
![[images/ChatGPT Image Aug 6, 2026, 02_46_29 PM.png]]

**Scope:** The theoretical ceiling of color — the largest range any non-glowing, light-reflecting material could ever fill, and why even the best pigments fall short of it.

In color science, the **optimal color solid** is the theoretical maximum range of colors achievable by **any non-fluorescent reflecting surface**. Its outer walls — the **MacAdam limits** — are the ultimate physical ceiling for material color at every level of lightness. Real paints live inside this shape; nothing that reflects light can leave it.

### 1. What an "optimal color" is

**Optimal colors** are hypothetical surfaces with idealized reflectance: unlike real pigments (whose absorption ramps up gradually), an optimal surface reflects either **0% or 100% of the light** at every wavelength. This "0–1" step function produces the maximum possible **vividness** for a given color, because it reflects one band of wavelengths with total efficiency and suppresses everything else completely. Any extra wavelength beyond the main band, or any dip within it, would dull the color or lower its brightness.

### 2. Who worked it out: Schrödinger and MacAdam

- **1919–1920 — Erwin Schrödinger** proved mathematically that an optimal surface's reflectance spectrum must switch between 0 and 1 at **at most two points** across the visible range.
- **1935 — David MacAdam** performed the painstaking calculations that placed these limits into the CIE 1931 color space, giving the exact color coordinates of optimal colors **at every level of lightness** — in effect drawing the surface of the largest color solid human vision allows.

### 3. The shape: a lopsided spindle

The solid is often drawn as a **lopsided top or distorted spindle**, with a pronounced bulge toward **green-yellow at high lightness**:

- **The green-yellow bulge:** because the **luminosity function V(λ) peaks near 555 nm**, a green surface reflecting a band around that peak (roughly **500–570 nm**) can be both bright and intensely vivid at the same time.
- **The red and blue squeeze:** saturated red and blue-violet hues are confined to much lower lightness. A red that reflects only above 600 nm looks dark, because the eye's sensitivity there is poor (**V(λ) ≈ 0.1–0.3**); to make a red brighter you must add other wavelengths, which dulls it.
- **The overall frame:** the solid's base is ideal black, its apex ideal white, and its "equator" the most vivid colors at middle lightness. It sits entirely inside the **spectrum locus** (pure rainbow light) and the **line of purples** (mixes of the red and violet ends).

### 4. Why it has that shape: the math and physics

Optimal colors fall into two "banded" families:

- **Band-pass** — reflecting a single middle band of wavelengths (0 elsewhere): produces hues like green or yellow.
- **Band-stop** — reflecting both ends of the spectrum but not the middle: produces non-spectral purples and magentas.

Mathematically these are the **"extreme points" of the set of all possible reflectance spectra**; their final perceived vividness is set by how they interact with your eye's **opponent-process** color system.

### 5. How everything else fits inside it

The MacAdam limits act as the "outer shell" for every other gamut:

- **Pointer's Gamut (1980):** roughly **4,000 real-world surface colors** (flowers, textiles, paints) — a significantly **smaller subset** of the optimal solid. Real pigments can't reach the ceiling because of "impure" absorption and light scattering.
- **Munsell Renotation (1943):** the system contains both "real" colors from the Munsell Book of Color and "unreal" extrapolated ones; the MacAdam limits decide which notations could actually exist as surface colors.
- **Devices:** most displays and printing processes (like sRGB) fail to cover the solid's most saturated regions, especially the cyan and yellow-green sectors.

### 6. Why it matters

The optimal color solid is the **standard yardstick** against which all real pigments and reproduction systems are measured. It shows that the limits of material color are set by **the physics of light and the biology of the eye** — not just by chemical engineering:

- **Color science:** researchers use the MacAdam limits to evaluate spectral imaging and color-matching.
- **Industry:** the limits define the "theoretical best" for developing new high-vividness pigments like the **phthalocyanines**, which approach the ideal step-function reflectance far more closely than traditional earth pigments.
- **An evolutionary hint:** the solid's asymmetry mirrors how the visual system is tuned for maximum efficiency under daylight — enabling fine discrimination of vegetation and natural surfaces, where green-yellow reflectances are abundant.

## Handprint Perspectives

MacEvoy organizes all of material color into **three chromaticity spaces** defined by maximum achievable hue purity: (1) the **physiological limits** of the retinal photoreceptors, produced by monochromatic lights (spectral hues); (2) the **ideal limits of perfectly reflecting colored materials**, defined as theoretical optimal colors; and (3) the **actual limits of the most saturated pure pigments or dyes** displayed in a transparent medium — the media gamut. The optimal color solid is thus the middle domain: real pigments can never escape it, and spectral lights are the only colors outside it. *(Source: [[raw_sources/handprint/tech13.md|tech13.html]])*

## HueValueChroma Perspectives

Briggs translates the theoretical solid into paint terms, and supplies the data that ties it to the Munsell clipboard:

- **The optimal solid is the "home value" template.** For any hue the range of possible chroma "becomes progressively more restricted as one approaches white and black respectively," with a maximum "at some intermediate value that depends on the hue, being high for yellow and low for violet and blue" — the value at which this occurs being "sometimes known to artists as the *home value* or the *peak-chroma value*." This "general pattern is repeated... in the matte and glossy editions of the *Munsell Book of Color*, in digital colours, and in the colour range of *optimal colour stimuli*," the theoretical 100%/0% reflectors that "mark the theoretical limits of colour for non-luminous objects" *(Source: [[raw_sources/huevaluechroma/015.md|015.html]])*.
- **Yellows almost *are* optimal colors — greens and blues never get close.** The ideal optimal yellow would reflect the red and green arms of the spectrum and absorb the blue-violet. Real high-chroma yellows "closely approach an *optimal* yellow colour," so bright yellow surfaces are "the lightest of all high chroma materials." The reverse holds for the blue-green sector: "none of our green or blue paints attain the near-optimal plateau-shaped reflectance curves seen in many red, orange and yellow paints" — the best blue-green pigments, the phthalocyanines, reach "a maximum chroma of about 12 Munsell units... moderate compared to the chroma of 14 to 16 of many red, orange and yellow paints." Even the best reds fall short of the ideal: cadmium red "reflects less light from the red part of the spectrum than does a bright white pigment like titanium white," and cadmium red deep drops in chroma as well as value *(Source: [[raw_sources/huevaluechroma/045.md|045.html]])*.
- **"Fullest chroma" pigments are a historical miscellany, and the ceiling varies by hue.** The highest-chroma pigments "are a miscellaneous collection of substances united only by the fact that the combination of saturation and brightness of their reflectances gives the highest chroma known for their hue among acceptably lightfast materials," and they "all fall short of the maximum chroma that is theoretically possible, and much more so for blues, greens and purples than for reds, oranges and yellows." The solid is the reason substances near it "tend to appear *fluorent* (fluorescent-looking)" — including genuinely fluorescent materials and some intense dyes *(Source: [[raw_sources/huevaluechroma/045.md|045.html]])*.
- **The measured numbers that fill the solid.** In the Munsell terms of the modern *Book of Color*, "the highest chromas (16 Munsell chroma units)... are attained in the hue range from orange-yellow to orange-red, while the lowest maximum chromas (10 units) are reached in the hue range from cyan to green," with peak-chroma value from 8–8.5 (5Y) down to 3–4 (7.5PB). Digital full-chroma colors poke far past paint into the violet-blue/magenta (chroma 24) regions the solid reserves as theoretical. And because the range of *common object colors* is limited in essentially the same way, the lop-sidedness "does not really present a problem" for painters *(Source: [[raw_sources/huevaluechroma/015.md|015.html]])*.
- **The solid is why "impurities in yellow" is a fallacy.** Briggs's direct correction to popular color books: a bright yellow paint "must reflect most of the spectrum, because it is so close to white in value," and its green and orange reflectances "are not impurities in the yellow; they are *additive components* of the yellow." A hypothetical paint reflecting only "yellow wavelengths plus impurities" would be dark brown or olive — impossible near the optimal solid's yellow apex *(Source: [[raw_sources/huevaluechroma/045.md|045.html]])*.

## Subtopics
- Optimal Colors
- Schrödinger & MacAdam
- Solid Shape
- Gamut Hierarchy
- The peak-chroma "home value" template and the near-optimal yellows (Briggs)
- Phthalocyanines at 12 vs red/orange/yellow at 14–16; yellow "impurities" fallacy (Briggs)

## Cross-References
- [[Pointer's Gamut]]
- [[Colors/Gamuts/index|Gamuts]]
- [[Device Gamuts]]
- [[CIE Systems]]
- [[MacAdam Ellipses]]
- [[History & Key Figures]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Dimensions of Colour : chroma" — [[raw_sources/huevaluechroma/015.md|015.html]]
* "The Dimensions of Colour : additive mixing" — [[raw_sources/huevaluechroma/045.md|045.html]]