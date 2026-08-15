---
title: Device Gamuts
sequence: 56
---
![[images/ChatGPT Image Aug 6, 2026, 02_39_45 PM.png]]

**Scope:** Why screens, printers and scanners each show different ranges of color — and how images are converted when a color from one device can't be reproduced by another.

A **color gamut** (say "GAM-ut") is the actual range of color a specific piece of hardware — a monitor, a scanner, or a printer — can display or reproduce. Every device makes color by its own physical process, so **no single device can show the full breadth of color the human eye can see**.

### 1. Every device's gamut is set by its primaries

A device's gamut is fundamentally determined by its **primaries** — the "corner" colors it can't mix from anything else:

- **Screens (additive):** monitors and projectors combine **red, green and blue (RGB) light**. The gamut is defined by how the screen's video signals turn into the light (and the CIE X, Y, Z numbers) that reach your eye.
- **Printers (subtractive):** printers use **cyan, magenta, yellow and black (CMYK) inks** that absorb specific wavelengths from white light. Where screen gamuts are triangles on a color map, printer gamuts are **irregular and bounded by curves**, because subtractive mixing isn't a simple linear rule — it depends on each ink's exact absorption behavior.

### 2. The everyday display standards

A few standard gamuts dominate digital imaging:

- **sRGB** — the standard for the internet and general computing; the **smallest** common color space, chosen so cheap consumer monitors can agree with each other.
- **Adobe RGB (1998)** — a **larger** gamut used in professional photography and printing prepress, because it includes the vivid cyans and greens of photographic film that sRGB leaves out.
- **HDTV (ITU-R BT.709)** — professional standard whose primary colors are fixed at specific coordinates: red (x=0.64, y=0.33), green (x=0.30, y=0.60), blue (x=0.15, y=0.06).
- **Scale:** the eye can distinguish roughly **7 million color levels**, while standard display gamuts like sRGB cover only a fraction — often drawn as **about one-third of the colors in CIELAB space**.

### 3. Emitted light vs. reflected ink

The gap between monitors and printers comes down to where the light comes from:

- **Screens emit light.** Because they project light straight into your eye, they can show **vivid colors at strong brightness**, with high contrast and deep blacks.
- **Printers reflect light.** Reflection is inherently dimmer. A printer's gamut is capped by the **whiteness of the paper**, which rarely reflects more than about **90%** of the light hitting it. Printers also suffer *additivity failure* — overlapping inks absorb more than their individual densities add up to, so dark areas turn "muddy" and lose saturation.

### 4. Gamuts by device class

- **Capture devices (cameras/scanners):** scanners and digital cameras record scenes through their sensors. High-end drum scanners capture enormous dynamic range (**optical density greater than 4.00**) — often *more* than the monitors used to view the results.
- **Monitor vs. printer:** a monitor's gamut is generally wider and more vibrant than a printer's. A standard CMYK printing process can typically simulate only about **60% of the colors** found in a specialized spot-color system like **Pantone**.

### 5. Making mismatched devices agree: ICC profiles

To keep color consistent from one device to another, the industry uses **ICC profiles** — standardized descriptions of what each device can do:

- **The workflow:** when a file moves from a wide-gamut device (like a camera) to a narrow one (like a printer), **gamut mapping** decides what to do with **out-of-gamut colors** — colors that exist in the original but the target device physically can't show.
- **Rendering intents** are the two main strategies:
  - **Perceptual:** gently compresses the *whole* gamut so the relationships between colors stay believable (everything shifts a little).
  - **Relative colorimetric:** matches in-gamut colors exactly and clips only the out-of-gamut ones to the nearest reproducible color, preserving the paper's white.
- **Clipping** is the blunt fallback: if out-of-gamut values aren't managed, the system simply cuts them off (everything above 255 becomes 255), causing **total loss of detail** in the saturated areas.

### 6. The benchmarks: human vision and physical limits

Device gamuts are measured against two outer benchmarks:

- **Human vision** — the ultimate limit: roughly **150 hues** and millions of intensity levels.
- **The theoretical ceiling (MacAdam limits)** — the maximum saturation any non-fluorescent material could reach, asymmetric because the eye's sensitivity peaks in green-yellow.
- **Pointer's Gamut** — the range of **all real-world surface colors** (paints, textiles, nature). Many professional displays try to cover it; few printers can reproduce its most vivid regions.
- **Quantization:** an 8-bit system offers 16.7 million colors, but to make the *steps* between colors genuinely invisible your eye needs **10-bit precision (1,024 levels per channel)**.

## Handprint Perspectives

MacEvoy notes that a color reproduction system is itself a way of specifying a standard visual color: a digital code like **"#336699" in the RGB color space** or a formula like **"30-50-15-5" in the Pantone CMYK system** is not a "different kind" of color but a different way to address the same material or radiant stimulus. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*

He also contrasts gamut shapes: the printing industry relies on standardized primary inks, mixture recipes (Pantone), and halftone screens of different densities, while a "millions of colors" RGB monitor gamut contains purples, reds, and greens that are **unmixable in the CMYK system** — monitor colors are created by tiny colored lights, so they achieve greater luminance contrasts and higher saturation than reflective prints. *(Source: [[raw_sources/handprint/color13.md|color13.html]])*

## HueValueChroma Perspectives

Briggs supplies the geometry and the caveats behind the page's device-gamut summary:

- **A cube, whichever model you use.** RGB space is "a cubic volume enclosing all possible screen colours, with black at the origin and white at the opposite corner"; CMY space is "identical to RGB space, apart from the fact that the origin of the C, M and Y axes is at the point representing white." (Strictly, RGB is a *model* "which can be embodied in various defined colour spaces, such as sRGB or AdobeRGB.") A standing trap: "these RGB values sometimes refer to **linear** units of light energy... and sometimes to **nonlinear** units of perceived brightness... Often no care is taken to show which" *(Source: [[raw_sources/huevaluechroma/092.md|092.html]])*.
- **Why CMYK needs K — discovered by Le Blon.** "Most actual colour printing uses black ink in addition" to CMY, partly because the three inks "may not yield a black that is neutral enough, or dark enough," partly to spare expensive colored ink and speed drying. Briggs dates the practice to the birth of color printing itself: "the need for a black component was recognized right from the invention of colour printing by the German artist J.C. Le Blon in the early 1700's" — and notes the charming dispute in which Le Blon's pupil **Jacques Gautier D'Agoty** denied the master ever used four plates, while Le Blon's supporters "replied that their master kept quiet about his use of the fourth plate because he used it in spite of himself" *(Source: [[raw_sources/huevaluechroma/092.md|092.html]])*.
- **The "S" in HSB and the "L" in HSL are not saturation and lightness.** HSB's B "measures the brightness of a colour compared to the maximum possible for a colour of the same hue and saturation" — so all pure colors, tints and white register B = 100 even though their *lightness* runs from L = 100 (white) down to L = 30 (Monitor Blue). Its S measures "the proportion of the coloured component to the whole" of a color's light. HLS's L is "even more tenuous": "all fully saturated colours, irrespective of how light or dark they look," get L = 0.5, and HLS S is "the degree of saturation compared to the maximum possible **at a given value of L**" — so "a very pale pink can have an S of 100." Neither space "has a true lightness or chroma dimension," which matters whenever "desaturate" or saturation sliders are treated as value-preserving *(Source: [[raw_sources/huevaluechroma/093.md|093.html]], [[raw_sources/huevaluechroma/094.md|094.html]])*.
- **The real gamut difference between lights and paints is *chroma*, not just range.** The page's lists of coordinates describe footprint; the material difference sits in where each gamut peaks. Digital "full-chroma" colors reach Munsell chromas of **24 in the violet-blue to magenta range, down to 18 at red**; artist paints instead "exceed the gamut of standard (sRGB) digital colours where these are relatively poor in the vicinity of yellow and cyan." And the highest-chroma *pigments* are themselves "a miscellaneous collection of substances united only by the fact that the combination of saturation and brightness of their reflectances gives the highest chroma known... for their hue" — all "fall short of the maximum chroma that is theoretically possible, and much more so for blues, greens and purples than for reds, oranges and yellows" *(Source: [[raw_sources/huevaluechroma/015.md|015.html]], [[raw_sources/huevaluechroma/045.md|045.html]])*.
- **Saturated yellow is additive structure, not a "yellow pigment."** A bright yellow paint "reflects most of the red, orange, yellow and green parts of the spectrum," and "much more of its yellow colour is due to additive mixture of the red and green wavelengths than to the wavelengths that are yellow in themselves." The claim that greenish/orange-tinged yellows reflect "yellow with impurities" is "an old misunderstanding that has been revived" by popular books on color mixing: "no paints that actually do this exist, and if they did they would reflect much less light than a bright yellow paint, and so would be dark brown or olive in appearance" *(Source: [[raw_sources/huevaluechroma/045.md|045.html]])*.

## Subtopics
- Device Primaries
- Display Standards
- Printer Limits
- Gamut Mapping & ICC
- RGB/CMY cube geometry; the linear vs nonlinear units trap (Briggs)
- HSB/HSL "brightness" and "saturation" as relative, not perceptual, dimensions (Briggs)
- Paint vs display chroma peaks: violet-blue/magenta 24 vs red 18 for RGB; yellow/cyan where paints win (Briggs)

## Cross-References
- [[Colors/Gamuts/index|Gamuts]]
- [[Pointer's Gamut]]
- [[Optimal Color Solid-MacAdam Limits]]
- [[CIE Systems]]
- [[MacAdam Ellipses]]
- [[Sourcing Real Spectral Data]]
- [[Why CMY Beats RYB for Color Mixing]] — why the CMY primaries define the wider subtractive gamut

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Dimensions of Colour : chroma" — [[raw_sources/huevaluechroma/015.md|015.html]]
* "The Dimensions of Colour : additive mixing" — [[raw_sources/huevaluechroma/045.md|045.html]]
* "The Dimensions of Colour : brightness and saturation" — [[raw_sources/huevaluechroma/092.md|092.html]], [[raw_sources/huevaluechroma/093.md|093.html]], [[raw_sources/huevaluechroma/094.md|094.html]]