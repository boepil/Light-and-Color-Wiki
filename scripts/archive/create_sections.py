import os
from pathlib import Path

wiki_dir = Path(r"d:\_PROJECTS\My\ai\Light and Color Wiki")

light_content = """# Light

This section explores the fundamental physics of electromagnetic radiation and how it behaves before it enters the human eye or interacts with paint. It covers the dual wave-particle nature of light, the specific band of energy we call the visible spectrum, and the critical physical distinction between emitted light and reflected/transmitted light. Additionally, it details the dynamic, ever-changing nature of natural daylight and how variations in illuminants dictate the colors we can perceive in the physical world.

## Subpages
* [[Wave Nature|Light/Wave Nature]]
* [[The Visible Spectrum|Light/The Visible Spectrum]]
* [[Reflection vs. Emission|Light/Reflection vs. Emission]]
* [[Illuminants & Correlated Color Temperature|Light/Illuminants & Correlated Color Temperature]]
* [[Natural Daylight Variation & Hyperspectral Scene Data|Light/Natural Daylight Variation & Hyperspectral Scene Data]]
* [[Spectral Locus & Excitation Purity|Light/Spectral Locus & Excitation Purity]]

## Related Intersections
* [[Natural Light Gamut vs. Pigment Gamut - Metamerism|Intersections/Natural Light Gamut vs. Pigment Gamut - Metamerism]]
* [[Color Matching Functions and the Photopic Luminosity Function|Intersections/Color Matching Functions and the Photopic Luminosity Function]]
"""

eye_content = """# Eye

This section details the biological and neurological mechanisms that translate physical wavelengths of light into the psychological experience of color. It covers the anatomy of the retina, the uneven distribution of rods and cones, and how wavelength perception is a highly synthetic process. Crucially, it explores opponent-process color coding, which explains how our brain structures raw cone signals into complementary visual channels (like red vs. green).

## Subpages
* [[Anatomy|Eye/Anatomy]]
* [[Rods vs. Cones - Density & Distribution|Eye/Rods vs. Cones - Density & Distribution]]
* [[Visual Acuity & Receptor Spacing|Eye/Visual Acuity & Receptor Spacing]]
* [[Wavelength Perception|Eye/Wavelength Perception]]
* [[Opponent-Process Color Coding|Eye/Opponent-Process Color Coding]]

## Related Intersections
* [[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing|Intersections/Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing]]
* [[Color Matching Functions and the Photopic Luminosity Function|Intersections/Color Matching Functions and the Photopic Luminosity Function]]
"""

colors_content = """# Colors

This section explores the mathematical models and empirical frameworks used to standardize, measure, and reproduce color. It contrasts historical, intuitively arranged atlases like the Munsell system with modern, instrument-based CIE uniform color spaces. It also deeply examines the concept of gamuts—the physical boundaries of reproducible color—and how human discrimination limits (like MacAdam ellipses) warp abstract geometric color models.

## Subpages
* [[CIE Systems|Colors/CIE Systems]]
* [[MacAdam Ellipses|Colors/MacAdam Ellipses]]
* [[Munsell Notation|Colors/Munsell Notation]]

### Gamuts
* [[Gamuts|Colors/Gamuts/Gamuts]]
* [[Device Gamuts|Colors/Gamuts/Device Gamuts]]
* [[Optimal Color Solid-MacAdam Limits|Colors/Gamuts/Optimal Color Solid-MacAdam Limits]]
* [[Pointer's Gamut|Colors/Gamuts/Pointer's Gamut]]

## Related Intersections
* [[Why Lab-Munsell Were Built for Perceptual Uniformity|Intersections/Why Lab-Munsell Were Built for Perceptual Uniformity]]
"""

painting_content = """# Painting

This section bridges the gap between abstract color theory and the physical reality of applied pigments. It details the chemical shift from natural earths to high-chroma modern synthetics, and how physical attributes like particle size and granulation affect watercolor mixtures. It also challenges traditional 18th-century geometric color harmonies, proving that real-world composition depends on continuous properties like value, chroma, and the objective measurement of real spectral data.

## Subpages
* [[Composition|Painting/Composition]]

### Pigments
* [[Pigments|Painting/Pigments/Pigments]]
* [[Chemistry|Painting/Pigments/Chemistry]]
* [[Natural vs. Synthetic|Painting/Pigments/Natural vs. Synthetic]]
* [[High-Chroma Synthetics|Painting/Pigments/High-Chroma Synthetics]]
* [[Particle Size-Tinting-Polymorphism|Painting/Pigments/Particle Size-Tinting-Polymorphism]]
* [[Sourcing Real Spectral Data|Painting/Pigments/Sourcing Real Spectral Data]]

## Related Intersections
* [[Optical vs. Physical Mixture|Intersections/Optical vs. Physical Mixture]]
* [[Natural Light Gamut vs. Pigment Gamut - Metamerism|Intersections/Natural Light Gamut vs. Pigment Gamut - Metamerism]]
"""

files_to_write = {
    "Light.md": light_content,
    "Eye.md": eye_content,
    "Colors.md": colors_content,
    "Painting.md": painting_content
}

for fname, content in files_to_write.items():
    with open(wiki_dir / fname, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Step 2: Top-level pages created.")
