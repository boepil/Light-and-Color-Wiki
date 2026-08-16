---
title: Colors
aliases: [Colors]
sequence: 54
---
### What this section is about

We measure temperature in degrees and distance in meters so that everyone agrees on what "warm" or "a meter" means. Color needed the same kind of system. For most of history, describing a color meant something like "kind of a blue-green" — fine for conversation, but useless when a paint factory, a printer, and a computer screen all need to match the *same* blue. **This section collects the systems people built to pin color down with numbers** — to describe it, compare it, and reproduce it reliably. Each page below goes deep on one system; this page only explains what each one is *for* and where to start.

### The systems, one by one

#### [[Color Wheel System]] — why every color wheel is a convention, not a discovery

Colors have no natural order — wavelengths run together without inherent boundaries — so any wheel's geometry (which hues sit where, which lie "opposite") is a human decision judged by studio usefulness, not by symmetry. Surveys eight historical systems — Newton 1704, the RYB wheel, Goethe 1810, Itten, Munsell 1905, CIELAB, RGB/CMY, Ostwald — each built on a different organizing principle (light physics, pigment mixing, perceptual spacing, or subjective harmony); their disagreement is the proof that classification is a human choice, with Munsell's wheel the perceptual-uniformity benchmark.

#### [[Why CMY Beats RYB for Color Mixing]] — why the subtractive primaries actually matter

Why three cyan/magenta/yellow paints can mix a far wider gamut than the red/yellow/blue triad — each CMY pigment absorbs roughly one-third of the visible spectrum and aligns with the eye's cone classes, while RYB's "primaries" are spectrally impure historical hues that cannot reach cyan, magenta, or clean violets. Covers the 1/3-spectrum physics, spectral purity (Schrödinger step pigments), curved mixing paths, the modern pigment set (phthalo/quinacridone/hansa), and the history from Le Blon and Helmholtz to Itten.

#### [[Colors/Nonspectral Colors|Nonspectral Colors]] — the colors the spectrum doesn't contain

**Purples, magentas, and deep reds have no single wavelength of light** — they exist only as mixtures of the two spectral ends, on the "line of purples" that closes the CIE horseshoe, and they still claim a large share of every perceptual hue circle: a full fifth of Munsell's principal hues. Why the brain "invents" magenta (S+L cone response without M), how the additive complements thread through this region, the complementary-wavelength "c" notation, and their natural occurrences (scattering, interference, minerals) and pigments (quinacridone magenta, dioxazine violet).

#### [[CIE Systems]] — the scientific foundation

The original international standard for measuring color (1931), built on **how the average human eye actually responds to light**. Instead of asking people to agree on names, it turns a color's light into numbers that any lab in the world can read. Think of it as the official ruler for color. If you want the scientific side — how color is defined objectively — start here.

#### [[Munsell Notation]] — the artist-friendly system

A system organized around **how colors actually look to people**, not around abstract math. Every color is sorted by three things anyone can see: its **hue** (red, yellow, green, and so on), its **lightness** (dark to light), and its **vividness** (muted to intense) — like a three-dimensional library of color chips you can walk through. Artists often find this more intuitive than raw numbers. If you want the visual, painter-oriented side, start here.

#### [[Colors/Gamuts/index|Gamuts]] — how much color can something actually produce?

A **gamut** (say "GAM-ut") is simply **the range of colors a particular thing — a screen, a printer, a paint, or even light itself — is capable of producing**. Nothing can show every possible color: a monitor cannot print a pure magenta, a printer cannot glow like a screen, and even the most vivid paint cannot match pure light. This folder compares several different boundaries — where the limits come from and how they differ:

- [[Device Gamuts]] — why a screen shows colors a printer cannot (and vice versa), and how the two are made to work together anyway when you move an image from screen to print.
- [[Optimal Color Solid-MacAdam Limits]] — the **physical ceiling**: the theoretical limit of what any color made from real, light-reflecting material could ever be. Some colors simply cannot exist as objects, no matter how good the pigment.
- [[Pointer's Gamut]] — the **real-world record**: a landmark 1980 survey of more than 4,000 actual things (paints, inks, textiles, plastics, flowers) that maps the most colorful real surfaces ever measured.

#### [[MacAdam Ellipses]] — when do two colors look different?

**How big a color difference has to be before a person actually notices it.** The answer is not the same everywhere in the color spectrum: in some regions two colors must be fairly far apart to look different, while in others a tiny shift is immediately visible. Human eyes are not equally sensitive to small changes in every part of the rainbow — and any system that measures color has to account for that uneven sensitivity.

#### [[Data & Methodology]] — how color is actually measured

The technical back room behind all the systems above: the **instruments** (spectrophotometers, spectroradiometers, colorimeters), the **protocols** (sampling rates, viewing geometries, standard observers and illuminants), the **calculation pipeline** that turns a reflectance curve into CIE numbers, and the classic **datasets** (Munsell Renotation, Pointer's gamut, MacAdam limits) that anchor them. Includes the caveats — observer averaging, bandpass width, fluorescence. **For readers who want to know how the numbers on these pages are produced** — or how to trust a measurement claim.

#### [[Why Material Reality Favors Green Over Red]] — why is green the most "colorful" color?

**Why green, uniquely among hues, can be both bright and intensely vivid in real materials — while red is stuck with a "pure but dark, or light but dull" choice.** The eye's luminosity function peaks in the green (555 nm), the theoretical color solid bulges there, and green pigment chemistry is unusually sharp-edged. This page traces that green advantage through all three constraints — and why the same facts mean red-orange, not green, holds the real-pigment chroma record.

### How the pieces fit together

These systems are not competing answers — they **build on one another**. CIE came first as the scientific foundation: numbers that define color in a way labs can share worldwide. Munsell offered a more visual, artistic alternative: the same idea, organized the way people actually see color (and later refined when the science caught up). The gamut pages and MacAdam ellipses then describe the **limits** — what physics allows, what the real world has actually achieved, what screens and printers can show, and how fine human color perception really is.

So if you are visiting for the first time, you have a clear choice of entry point: **[[CIE Systems]]** if you want the scientific view, or **[[Munsell Notation]]** if you want the artist-friendly view — and wander into the gamut pages whenever you wonder, "Why can't my screen show that color?"

## Related Intersections
- [[Why Lab-Munsell Were Built for Perceptual Uniformity]] — the story of why both of these systems were engineered so that equal steps in the numbers feel like equal steps to your eyes.
