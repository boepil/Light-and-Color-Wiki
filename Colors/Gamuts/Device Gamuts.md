---
title: Device Gamuts
sequence: 12
---
![[images/ChatGPT Image Aug 6, 2026, 02_39_45 PM.png]]

**Scope:** Examines device-specific color gamuts such as those of displays and printers.

A **color gamut** is the actual range of color that a specific hardware component — monitor, scanner, or printer — can display or reproduce. Because every device relies on unique physical processes to generate color, no single device can capture the full breadth of color visible to the human eye.

### 1. Definition and Device Primaries

A device's gamut is fundamentally determined by its **primaries**, which act as the "corners" of its reproducible color space:

- **Displays (additive):** monitors and projectors use **additive color mixing**, combining red, green, and blue (RGB) light. The gamut is characterized by the relationship between the video signals (E_R, E_G, E_B) and the resulting **CIE tristimulus values (X, Y, Z)** produced on screen.
- **Printers (subtractive):** printers use **subtractive color mixing**, where inks (Cyan, Magenta, Yellow, Black — CMYK) absorb specific wavelengths from white light. While display gamuts are represented as triangles on a chromaticity diagram, printer gamuts are **irregular and bounded by curves**, because subtractive mixing is non-linear and subject to the specific absorption spectra of pigments.

### 2. Display Gamut Standards

Common standards define the "ideal" primaries and range for digital imaging:

- **sRGB:** the standard for the Internet and general computing; the smallest standard color space, designed for consistency across diverse consumer monitors.
- **Adobe RGB (1998):** a larger gamut than sRGB, common in professional photography and prepress because it includes more saturated cyans and greens typical of photographic film but excluded by sRGB.
- **Primary coordinates:** professional standards like **ITU-R BT.709** (HDTV, related to sRGB) define primary chromaticity coordinates as **Red (x=0.64, y=0.33)**, **Green (x=0.30, y=0.60)**, and **Blue (x=0.15, y=0.06)**.
- **Coverage:** digital gamuts represent only a fraction of human vision. While the eye can distinguish approximately **7 million color levels**, standard display gamuts like sRGB are significantly more restricted — often visualized as covering **roughly one-third of the perceived colors in CIELAB space**.

### 3. Additive Light vs. Subtractive Ink

The disparity between monitor and printer gamuts arises from their physical mechanisms:

- **Displays** use **emitted light**, achieving **highly saturated colors at high luminance**. Technologies like LED and plasma offer high contrast ratios and deep blacks by controlling the excitation of phosphors or pixels directly.
- **Printers** rely on **reflected light**, which is inherently less brilliant. The gamut is limited by the **whitepoint of the paper**, which rarely reflects more than 90% of incident light. Printers also suffer from **additivity failure**: the combined density of overlapping inks is less than the sum of their parts, producing "muddy" or desaturated colors in dark regions.

### 4. Gamut Differences by Device Class

- **Capture devices (cameras/scanners):** scanners and digital cameras use **CCD or PMT sensors** to record RGB records from an original. High-end drum scanners capture a very high dynamic range (**optical density > 4.00**), often exceeding the gamut of the monitors used to view the files.
- **Monitor vs. printer:** a monitor's gamut is generally wider and more vibrant than a printer's. For example, a standard CMYK printing process can typically simulate only about **60% of the colors** found in a specialized spot-color system like **Pantone**.

### 5. Gamut Mapping and ICC Color Management

To maintain color consistency, the industry uses **ICC profiles** — standardized formulas describing the attributes of specific devices:

- **The workflow:** when a file moves from a wide-gamut device (like a camera) to a narrow-gamut device (like a printer), **gamut mapping** must handle **out-of-gamut colors**.
- **Rendering intents:**
  - **Perceptual:** compresses the entire gamut to maintain the visual relationships between colors, though it may shift all colors slightly;
  - **Relative colorimetric:** matches in-gamut colors exactly and clips out-of-gamut colors to the nearest reproducible boundary, preserving the target medium's whitepoint.
- **Clipping:** if out-of-gamut values are not managed, the system may "clip" the data (e.g., setting all values above 255 to 255), causing a **total loss of detail** in saturated areas.

### 6. Human Vision and Physical Limits

Device gamuts are compared against theoretical and biological benchmarks:

- **Human vision:** the ultimate limit, discerning roughly **150 hues** and millions of intensity levels.
- **Optimal Color Solid (MacAdam Limits):** the theoretical maximum saturation for material (non-fluorescent) colors — asymmetric, favoring **high chroma in the green-yellow region** where the human luminosity function peaks.
- **Pointer's Gamut:** the range of **all real-world surface colors** (paints, textiles, nature). Many professional displays attempt to cover it, though few printers can fully reproduce its most saturated regions.
- **Quantization:** while 8-bit systems theoretically produce 16.7 million colors, the eye requires **10-bit quantization (1,024 levels per channel)** to make steps between colors truly invisible.

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
- [[Gamuts]]
- [[Pointer's Gamut]]
- [[Optimal Color Solid-MacAdam Limits]]
- [[CIE Systems]]
- [[MacAdam Ellipses]]
- [[Sourcing Real Spectral Data]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Dimensions of Colour : chroma" — [[raw_sources/huevaluechroma/015.md|015.html]]
* "The Dimensions of Colour : additive mixing" — [[raw_sources/huevaluechroma/045.md|045.html]]
* "The Dimensions of Colour : brightness and saturation" — [[raw_sources/huevaluechroma/092.md|092.html]], [[raw_sources/huevaluechroma/093.md|093.html]], [[raw_sources/huevaluechroma/094.md|094.html]]