---
title: Gamuts
aliases: [Gamuts]
sequence: 59
---
![[images/ChatGPT Image Aug 6, 2026, 02_43_04 PM.png]]

**Scope:** Parent page introducing gamuts — what "the range of colors a thing can produce" actually means, and how the different limits (physics, real objects, everyday devices, and the human eye) compare.

A **gamut** (say "GAM-ut") is the range of colors a particular thing — a monitor, a scanner, a printer, or a paint — can actually display or reproduce. Every medium, whether it emits light like a screen or reflects it like a pigment, has its own physical and chemical limits, so **no single device can show the full range of colors the human eye can see**. This page explains what a gamut is, why some things have bigger gamuts than others, and what happens when a color doesn't fit.

### 1. How we draw a gamut

Gamuts are drawn inside standard color maps so different devices can be compared:

- **Screens are triangles.** On the classic 1931 CIE diagram, a display's gamut is typically a **triangle** whose three corners are the screen's red, green, and blue primaries — every color that screen can show lies inside that triangle.
- **Paints and inks are lumpy.** Subtractive media (paints, inks, printed color) don't make triangles: their gamuts are **irregular shapes bounded by curves**, because pigment mixing isn't a simple combination of three coordinates — it depends on how pigments absorb and scatter light wavelength by wavelength.
- **Color is really 3D.** Hue, lightness, and vividness are three independent dimensions, so a flat 2D map can't tell the whole story. In 3D, a paint gamut becomes an irregular lopsided solid (the "color tree"), reflecting that different hues reach peak vividness at different lightness levels.

### 2. The ladder of limits

From the largest possible set of colors to the smallest, the limits stack up in a clear order:

- **The human eye** — the biggest "gamut" of all, able to distinguish roughly **7 million different color levels**.
- **The theoretical ceiling for materials** — the *Optimal Color Solid* (MacAdam limits): the most vivid a real, light-reflecting surface could ever be, reached only by surfaces that reflect either 0% or 100% of light at every wavelength.
- **The real-world record** — *Pointer's Gamut*: the range of colors actually measured across real surfaces (paints, textiles, flowers). Smaller than the theoretical ceiling, and lopsided — far roomier in green-yellow than in red.
- **Everyday devices** — *Adobe RGB* covers a wide range but still less than the eye; the standard **sRGB** used for the internet is smaller still, restricted to about **256 distinct hues** in the classic 8-bit web palette.

### 3. Why screens can be more vivid than paint

The big difference comes down to emitting light versus reflecting it:

- **Additive — screens emit light.** A monitor shines light straight into your eye, losing no energy to reflection, so it can produce **vivid colors and strong brightness at the same time**.
- **Subtractive — paint must borrow light.** A pigment can only absorb (subtract) light from whatever lights the room, and its gamut is capped by how sensitive your eye is to each color — the *luminosity function* **V(λ)**, which peaks in the green near **555 nm**. Because your eye is most sensitive there, a **green** pigment can be both light and intensely saturated. A **red** pigment, though, must reflect wavelengths your eye finds dimmer — so to make a red lighter you have to add other wavelengths, which inevitably **drains the red's vividness**.
- **Imperfect pigments.** Real pigments are "impure" — they absorb a little light in the regions where they should be transparent — which squeezes the gamut of any color mixed from them even further.

### 4. The absolute boundaries of color

- **The rainbow is the outer wall.** The curved, horseshoe-shaped edge of the CIE diagram is the *spectral locus* — the colors of **pure spectral light** (the rainbow). It is the physical limit of every real color.
- **Purples and magentas are not on the rainbow.** The dashed line across the bottom of the horseshoe — the *line of purples* — connects the violet (380 nm) and red (700 nm) ends. Purples and magentas exist only as **mixtures of red and blue light**; there is no single wavelength of light that is purple.
- **No device reaches the wall.** No screen or printer can reproduce pure rainbow colors across the whole spectrum, because every practical light source and pigment is **broadband** — it emits or reflects a whole spread of wavelengths, not one perfect "pure" ray.

### 5. What happens when a color doesn't fit

When you move an image from one device to another with a smaller gamut (say, monitor to printer), some colors won't survive:

- **Out-of-gamut colors** are the ones that exist in the original but the target device physically cannot produce.
- **Clipping** is the crude fix — shoving every too-vivid value to the device's maximum (like turning anything above 255 into 255). It works, but **drops the detail** in the saturated areas.
- **Gamut mapping** is the clever fix — software substitutes the nearest color the device *can* show, or gently compresses the whole gamut so the relationships between colors stay believable.
- **ICC profiles** are the translators that let different devices — each with its own primaries, inks, and quirks — interpret the same numbers and land close to the same color.

### 6. How sharp is your eye, really?

Human sensitivity sets the bar for digital color:

- **What you can actually tell apart:** a 24-bit system offers 16.7 million colors, but within a standard HDTV's gamut your eye can genuinely distinguish only about **1.4 million distinct colors** — the rest are duplicates your eye can't tell apart.
- **Why shapes differ:** screens make **triangles** because three primaries define them. The **Pointer gamut** of real surfaces is **irregular** because your visual system was evolutionarily tuned for the natural world — it's far more sensitive to small changes in green-yellow (where vegetation lives), so real surfaces cover much more gamut in green than in red.

## Handprint Perspectives

MacEvoy uses CIELAB (or CIECAM) as the objective frame of reference for judging the shape and size of gamuts: the CIE color models enclose the space of all possible colors, and spectrophotometric measurement locates each colorant inside it. Comparing the "millions of colors" Apple RGB monitor gamut with the 256-color "web safe" gamut and the CMYK printing gamut, he notes the range of purples, reds, and greens available on a monitor but **unmixable in CMYK** — because monitor colors are made of tiny colored lights, they achieve greater luminance contrasts and higher saturation than reflective prints.

He also stresses that a gamut is **always three-dimensional and context-sensitive**: the gamut of a television shrinks when sunlight falls on the screen, just as a printer's gamut shrinks on gray paper, with coarse halftones, or in dim viewing light. *(Source: [[raw_sources/handprint/color13.md|color13.html]])*

## HueValueChroma Perspectives

Briggs connects the gamut concept to its own history and to the arithmetic that makes paint gamuts behave the way they do:

- **"Gamut" thinking is older than colorimetry.** Robert Boyle (1664), the writer who introduced the term "primary colour" in English, "shows an awareness of the concept of a *gamut*": the primaries suffice to mix a full range of hues, "but some colours will, by their greater 'splendor' (we would say *chroma*), lie outside this gamut." The mismatch of range vs. top-chroma — the core of the page's hierarchy — was thus noted at the very origin of primary-color language *(Source: [[raw_sources/huevaluechroma/062.md|062.html]])*.
- **The paint gamut is computed by multiplication, not addition.** Subtractive results "are calculated by multiplying together the percentage of light energy passed on by both colourants, for each wavelength," which is why the page's pigment gamuts are "irregular and bounded by curves": shape is set wavelength-by-wavelength by the overlap of reflectance curves, not by three primary coordinates. And metamerism means "the **exact** results of subtractive mixing of real colourants can not be predicted merely from their colour" — though "all common cyan and yellow colourants combined subtractively will make a green" *(Source: [[raw_sources/huevaluechroma/051.md|051.html]])*.
- **The lop-sidedness is shared with nature, so it is not a defect.** The paint gamut's bulge between orange-yellow and orange-red (16 Munsell units maximum chroma) against its cyan-green trough (10 units) "does not really present a problem because the range of common object colours is restricted in essentially the same way, for the same combination of physical and physiological reasons." What is a defect — and entirely avoidable — is shrinking the gamut by using a psychologically-pure RYB trio: "if the red paint is a *psychologically* pure red... it is found to be impossible to mix purples above a very low chroma," a problem printers solved with the **YMC subtractive primaries** while many traditional teachers still escape it via the "split-primary" palette, whose recurring rationale Briggs judges "entirely discredited" *(Source: [[raw_sources/huevaluechroma/015.md|015.html]], [[raw_sources/huevaluechroma/062.md|062.html]])*.
- **Digital "subtractive" mixing is an idealization that can leave the real gamut.** Multiply-mode blending in graphics programs "gives a realistic representation of what subtractive mixing involving comparably coloured lights and materials **might** result in," but "unrealistic effects may result from subtractively mixing very bright and/or very saturated digital colours that are outside the range of real object colours." Even Painter — which simulates the appearance and behavior of paints — "nevertheless" mixes by ideal subtractive rules: "Monitor yellow" and "Monitor blue" mix to black or grey, "while paints of similar hues would mix to a dull green" *(Source: [[raw_sources/huevaluechroma/051.md|051.html]])*.
- **Where screen gamuts beat paints and where they lose.** Digital full-chroma colors reach "Munsell chromas of **24 in the violet-blue to magenta range, down to 18 at red**" — far past paints — "while artist's paints... exceed the gamut of standard (sRGB) digital colours where these are relatively poor in the vicinity of yellow and cyan" *(Source: [[raw_sources/huevaluechroma/015.md|015.html]], [[raw_sources/huevaluechroma/045.md|045.html]])*.

## Subtopics
- Gamut Representation
- Gamut Hierarchy
- Additive vs Subtractive
- Gamut Mapping
- Boyle 1664 and the origin of "gamut" thinking; the multiplicative, metamerism-bound paint gamut (Briggs)
- Shared lop-sidedness with common object colors; ideal-subtractive digital mixing vs real paint mixtures (Briggs)

## Cross-References
- [[Device Gamuts]]
- [[Pointer's Gamut]]
- [[Optimal Color Solid-MacAdam Limits]]
- [[CIE Systems]]
- [[MacAdam Ellipses]]
- [[Natural Light Gamut vs. Pigment Gamut - Metamerism]]

## Sources

* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Color Management"
* "Color for Science, Art, and Technology" — Kurt Nassau (Editor)
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "Choosing Colors (Live)"
* "The Case Against Color Bias"
* "The Material Supremacy of Green Chroma"
* "Illusions of Seeing"
* "The Dimensions of Colour: chroma" — [[raw_sources/huevaluechroma/015.md|015.html]]
* "The Dimensions of Colour: additive mixing" — [[raw_sources/huevaluechroma/045.md|045.html]]
* "The Dimensions of Colour: subtractive mixing" — [[raw_sources/huevaluechroma/051.md|051.html]]
* "The Dimensions of Colour: primary colours" — [[raw_sources/huevaluechroma/062.md|062.html]]