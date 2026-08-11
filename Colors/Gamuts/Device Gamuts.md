---
title: Device Gamuts
sequence: 11
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

## Subtopics
- Device Primaries
- Display Standards
- Printer Limits
- Gamut Mapping & ICC

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