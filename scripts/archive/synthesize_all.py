import os
import re

wiki_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"

syntheses = {
    r"Light\Wave Nature.md": """## Handprint Perspectives

Bruce MacEvoy (Handprint) emphasizes a fundamental conceptual shift when discussing the physics of light: "color is in the mind, not in the light." Wavelengths of electromagnetic radiation possess no inherent color; they are purely physical phenomena of energy. The perception of color only arises when this energy interacts with the biological mechanisms of the human eye. 

This strict separation between physical stimulus and biological response is critical. By understanding that wave nature is purely physical, we can better contextualize the [[The Visible Spectrum]] and recognize why perceptual models like [[CIE Systems]] must be introduced to translate raw energy into human color experience. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*""",

    r"Light\The Visible Spectrum.md": """## Handprint Perspectives

When discussing the visible spectrum, MacEvoy stresses that the spectral band is not uniform in its perceptual impact. Our biological sensitivity is heavily biased toward the middle of the spectrum (greens and yellows), meaning that equal physical increments in wavelength do not produce equal perceptual shifts in hue. 

This physical reality contradicts the perfectly symmetrical geometry often taught in traditional art classes. It underscores why understanding [[Wavelength Perception]] and the biological [[Anatomy]] of the eye is necessary to explain why we see the spectrum the way we do, rather than assuming light itself is symmetrically divided. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*""",

    r"Light\Reflection vs. Emission.md": """## Handprint Perspectives

MacEvoy draws a hard line between additive (emitted) and subtractive (reflected or transmitted) light, arguing that confusing the two is the root of many traditional color theory fallacies. Additive color mixing is mathematically linear and predictable, forming the basis of monitor displays and opponent-color theory. 

Conversely, paint mixtures are bound by multiplicative reflectance overlap—a complex physical interaction where the absorption curves of pigments combine. **Contradiction Flag:** MacEvoy explicitly notes that because of this difference, traditional geometric color wheels (which model additive light) fail to accurately predict the physical behavior of reflected paint mixtures. This is deeply explored in [[Optical vs. Physical Mixture]]. *(Source: [[raw_sources/handprint/color18b.md|color18b.html]])*""",

    r"Light\Illuminants & Correlated Color Temperature.md": """## Handprint Perspectives

In his analysis of light sources, Handprint highlights that natural daylight is not a single, static illuminant but a dynamic range of color temperatures known as the daylight locus. For painters, the correlated color temperature of the ambient light fundamentally alters the available gamut of the scene.

Because subtractive color (paint) only reflects the wavelengths present in the illuminant, a shift in color temperature can severely mute certain pigments while enhancing others. This ties directly into the concepts of [[Color Constancy]] and [[Natural Light Gamut vs. Pigment Gamut - Metamerism]], explaining why a painting executed under warm incandescent light will appear drastically different under cool daylight. *(Source: [[raw_sources/handprint/color12.md|color12.html]])*""",

    r"Eye\Anatomy.md": """## Handprint Perspectives

MacEvoy's approach to ocular anatomy focuses heavily on the uneven distribution and overlapping spectral sensitivities of the L, M, and S cones. He points out that our photoreceptors are not perfectly spaced to cover the visible spectrum evenly; rather, they are heavily clustered toward the longer (red/green) wavelengths.

This anatomical imbalance is the biological root of our perceptual bias toward "warm" colors and our extreme sensitivity to green hues. It reinforces the concepts discussed in [[Wavelength Perception]] and explains why mathematically perfect, symmetrical color spaces cannot accurately model human vision without severe distortion. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*""",

    r"Eye\Wavelength Perception.md": """## Handprint Perspectives

Handprint emphasizes that wavelength perception is a highly synthetic process. The eye does not act as a spectrometer measuring exact frequencies; instead, it relies on the ratios of stimulation across the three cone types. This means completely different physical combinations of wavelengths can produce the exact same perceived color—a phenomenon known as metamerism.

Understanding this biological synthesis is crucial. It explains how our visual system translates the raw physics of [[Wave Nature]] into the structured psychological experience defined by [[Opponent-Process Color Coding]]. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*""",

    r"Eye\Opponent-Process Color Coding.md": """## Handprint Perspectives

MacEvoy heavily utilizes opponent-process theory to explain how the brain structures raw cone signals into the perceptual axes of red-green and blue-yellow. He views this biological wiring as the true foundation for visual complementary colors (colors that naturally contrast and neutralize in the mind).

**Contradiction Flag:** Handprint vehemently warns against a major fallacy in traditional color theory: conflating these *visual* opponent complements with physical *mixing* complements. While opponent-process theory dictates that green and magenta are visual opposites, mixing green and magenta paints does not yield a neutral gray due to physical reflectance overlap. This crucial distinction is expanded upon in [[Optical vs. Physical Mixture]]. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*""",

    r"Colors\CIE Systems.md": """## Handprint Perspectives

Handprint views modern CIE systems, particularly CIELAB and CIECAM, as the most accurate tools available for mapping human perceptual color space, praising their foundation in objective spectrophotometric measurement rather than subjective artistic lore. 

However, MacEvoy cautions that these systems are primarily designed as uniform perceptual models for additive light and industrial color matching. **Contradiction Flag:** While CIELAB perfectly maps visual perception, MacEvoy argues it cannot reliably predict the behavior of physical paint mixtures. The subtractive mixing of pigments introduces nonlinear saturation costs that distort the tidy geometry of CIE spaces, as discussed in [[Optical vs. Physical Mixture]]. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*""",

    r"Colors\Munsell Notation.md": """## Handprint Perspectives

MacEvoy praises the Munsell system for its historical importance in establishing a perceptually uniform color space based on the three distinct dimensions of Value, Hue, and Chroma. He notes that Munsell was revolutionary for forcing artists to recognize that different hues reach their maximum chroma at different lightness levels.

While later [[CIE Systems]] and uniform color spaces like CIELAB offer more objective, instrument-based measurements, Munsell remains highly relevant for painters as an intuitive, physical atlas of color that directly informs pigment selection and [[Composition]]. *(Source: [[raw_sources/handprint/color11.md|color11.html]])*""",

    r"Colors\MacAdam Ellipses.md": """## Handprint Perspectives

Handprint uses MacAdam ellipses to illustrate a fundamental flaw in traditional, symmetrical color wheels. The ellipses mathematically prove that human color discrimination is highly uneven—we can detect minute shifts in blue-green hues, while our discrimination in the yellow-green region is much less precise. 

This biological reality, rooted in our [[Anatomy]], means that any color model attempting to represent perceptual uniformity (like [[CIE Systems]]) must necessarily warp and distort the color space, proving that a geometrically perfect circle cannot accurately represent human color vision. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*""",

    r"Painting\Composition.md": """## Handprint Perspectives

MacEvoy firmly rejects the rigid, geometric formulas of traditional color harmony (e.g., analogous, triadic, or split-complementary schemes), dismissing them as 18th-century dogma. He argues that "abstract color systems... confuse hue relationships that need to be kept distinct."

Instead, Handprint advocates for a composition strategy rooted primarily in value (lightness) structure and chroma contrast, asserting that almost any hue combination can be harmonious if the values and saturations are carefully managed. **Contradiction Flag:** This directly challenges the idea that specific hues on a color wheel are inherently harmonious by geometric definition, suggesting instead that harmony is contextual and dependent on the physical properties of the [[Pigments]] used. *(Source: [[raw_sources/handprint/tech13.md|tech13.html]])*""",

    r"Painting\Pigments\Chemistry.md": """## Handprint Perspectives

The chemical foundation of pigments is central to Handprint's analysis of modern watercolors. MacEvoy documents the historical shift from natural, inorganic earths to highly engineered synthetic organics (like Phthalocyanines and Quinacridones), which dominate modern palettes.

Understanding this chemistry is essential because modern synthetics behave entirely differently in mixtures than historical pigments. Their transparency, tinting strength, and lightfastness require a modern approach to color mixing, rendering many traditional color theory recipes obsolete and necessitating reliance on [[Real Spectral Data]]. *(Source: [[raw_sources/handprint/pigmt1.md|pigmt1.html]])*""",

    r"Painting\Pigments\Natural vs. Synthetic.md": """## Handprint Perspectives

When comparing natural and synthetic pigments, MacEvoy notes that natural earths (like raw sienna and umbers) offer unique, subtle granulation and low chroma that are impossible to perfectly replicate with high-intensity synthetic mixtures. However, modern synthetics offer unparalleled permanence and saturation.

**Contradiction Flag:** MacEvoy argues that the traditional reliance on three "primary colors" is fundamentally flawed when dealing with modern synthetics. Limiting a palette to three synthetics artificially restricts the gamut. As explored in [[Optical vs. Physical Mixture]], saturation costs dictate that a wider array of specific synthetic pigments will always produce cleaner, brighter mixtures than a restricted primary triad. *(Source: [[raw_sources/handprint/pigmt1.md|pigmt1.html]])*""",

    r"Painting\Pigments\High-Chroma Synthetics.md": """## Handprint Perspectives

MacEvoy champions high-chroma synthetic organic pigments (such as PB15:3 and PR122) as the backbone of the modern watercolor palette. These pigments push the boundaries of the reproducible [[Device Gamuts]], allowing painters to achieve saturations previously impossible with natural pigments.

However, he warns that these intense pigments must be managed carefully. Their high tinting strength can easily overwhelm a mixture. Understanding their specific chemical behavior (as detailed in [[Chemistry]]) is critical to harnessing their power without creating visually harsh or unbalanced compositions. *(Source: [[raw_sources/handprint/pigmt1.md|pigmt1.html]])*""",

    r"Painting\Pigments\Particle Size-Tinting-Polymorphism.md": """## Handprint Perspectives

Handprint heavily emphasizes that the physical behavior of a pigment—specifically its particle size and specific gravity—is just as important as its hue. Pigments with large, heavy particles (like Cobalt Blue or Ultramarine) settle rapidly into the valleys of watercolor paper, creating textural granulation.

Conversely, finely milled synthetic organics stain the paper fibers evenly. MacEvoy points out that traditional color theory entirely ignores these physical attributes. A painter must understand these properties (detailed in [[Chemistry]]) because combining a heavily granulating pigment with a staining pigment creates distinct visual separations that simple color wheels cannot predict. *(Source: [[raw_sources/handprint/pigmt3.md|pigmt3.html]])*""",

    r"Painting\Pigments\Sourcing Real Spectral Data.md": """## Handprint Perspectives

MacEvoy is famous for conducting exhaustive, spectrophotometer-based testing of hundreds of commercial watercolor paints. He converted these measurements into CIELAB coordinates to create an objective, empirical atlas of pigment behavior, replacing the subjective marketing claims of paint manufacturers.

By providing real spectral data (such as the exact hue angle and lightness shifts of pigments as they dry), Handprint allows artists to construct palettes based on actual physical performance rather than abstract theory. This objective data is crucial for understanding the true boundaries of pigment [[Gamuts]] and the realities of [[Optical vs. Physical Mixture]]. *(Source: [[raw_sources/handprint/pigmt8.md|pigmt8.html]])*""",

    r"Colors\Gamuts\Gamuts.md": """## Handprint Perspectives

In his essay "more is less? a gamut comparison," MacEvoy dismantles the traditional reliance on three "primary" colors by examining the physical limits of pigment gamuts. He defines a gamut as "the domain of all colors that can be mixed from a specific set of fundamental colors." 

**Contradiction Flag:** Handprint argues that using a limited primary triad guarantees severe saturation costs in mixed colors. By comparing pigment gamuts within a CIELAB space, he demonstrates that adding more distinct pigments to a palette actually expands the mixable color space. Therefore, the "primary color" restriction is a theoretical handicap, not a physical law. This directly links to the discussions of [[Pointer's Gamut]] and [[Device Gamuts]], illustrating that physical media always have hard boundaries that abstract color wheels ignore. *(Source: [[raw_sources/handprint/color13.md|color13.html]])*"""
}

def update_file(stub_path, new_content):
    full_path = os.path.join(wiki_dir, stub_path)
    if not os.path.exists(full_path):
        print(f"Skipping {stub_path}, not found.")
        return False
        
    with open(full_path, 'r', encoding='utf-8') as f:
        original = f.read()
        
    # Remove everything from "## Handprint" or "## Handprint Notes / Perspectives" to the end
    clean_text = re.split(r'##\s*Handprint', original, 1)[0].strip()
    
    # Append the new synthesis
    updated_text = clean_text + "\n\n" + new_content + "\n"
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    return True

success_count = 0
for stub, content in syntheses.items():
    if update_file(stub, content):
        success_count += 1

print(f"Successfully synthesized and updated {success_count} files.")
