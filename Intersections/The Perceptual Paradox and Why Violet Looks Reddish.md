![[Codex Image Aug 29, 2026, 10_39_46 PM.png]]

**Scope:** The physiological and philosophical resolution to why short-wavelength violet looks reddish despite sitting at the opposite physical extreme from long-wavelength red — the S-cone contribution to the red–green opponent channel, Hurvich–Jameson dual-lobe chromatic response functions, the closure of the hue circle, and the distinction between spectral violet and nonspectral purple.

### The paradox: a linear spectrum vs. a circular hue space

The visible spectrum is physically a **linear, open continuum**: wavelengths vary monotonically from roughly 380 nm (short) to 780 nm (long). If human color vision were a direct sensor of wavelength, perceptual experience would form a linear scale between two maximally divergent endpoints. Instead, color perception is organized as a **closed hue circle**: moving from red through orange, yellow, green, and blue leads to violet, which perceptually loops back to resemble red rather than an opposing quality. The physical extremes meet perceptually, and the circle is closed by hues (purples and magentas) that have no single physical wavelength in the electromagnetic spectrum.

The fundamental paradox is that **the shortest-wavelength light (violet ≈ 400–450 nm) induces a reddish sensation similar to the longest-wavelength light (red ≈ 650–700 nm)**, despite sitting on opposite physical boundaries.

### Mechanism: cone sensitivities and opponent recoding

The resolution lies in the principle of univariance: photoreceptors do not measure wavelength directly. The human retina samples the spectrum through three broadly overlapping cone classes:
- **S-cones (Short-wavelength sensitive):** Peak absorption ≈ 420 nm.
- **M-cones (Middle-wavelength sensitive):** Peak absorption ≈ 530 nm.
- **L-cones (Long-wavelength sensitive):** Peak absorption ≈ 560 nm.

Because cone absorption curves overlap, the visual system extracts chromatic information through **opponent neural comparisons**:
1. **Red–Green Channel (\(r-g\)):** Computes differences between cone excitations. S-cones and L-cones feed the *red* (+excitatory) pole, while M-cones feed the *green* (-inhibitory) pole.
2. **Blue–Yellow Channel (\(y-b\)):** Computes \(S - (L+M)\), driving *blue* when S dominates and *yellow* when L+M dominate.
3. **Achromatic Luminance Channel (\(L+M\)):** Sums cone signals for brightness.

When violet light (400–440 nm) enters the eye:
- **Strong S-cone excitation** drives the blue–yellow channel decisively toward **blue**.
- At the shortest visible wavelengths, **L-cone sensitivity exceeds M-cone sensitivity** (the L-cone photopigment retains a secondary short-wavelength "beta-band" absorption tail, while M-cone absorption drops steeply).
- S-cone inputs also feed the red pole of the red–green opponent mechanism. The combined S- and L-cone signals overwhelm the near-zero M-cone input, driving the red–green channel toward **red**.

In the quantitative **Hurvich–Jameson opponent model**, the red–green chromatic response function possesses **two red lobes**: a primary peak at long wavelengths and a secondary, smaller peak below 475 nm. At **unique blue (≈ 475 nm)**, the red–green signal crosses zero, producing a pure, unmixed blue. Below 475 nm, redness re-emerges, making spectral violet a **phenomenally binary hue** containing simultaneous blueness and redness.

### Spectral violet vs. nonspectral purple (The "Magenta Gap")

This opponent architecture clarifies the distinction between violet and purple:
- **Spectral Violet (Monochromatic ≈ 400–450 nm):** A single physical wavelength that simultaneously stimulates the blue pole of the blue–yellow channel and the short-wavelength red lobe of the red–green channel.
- **Nonspectral Purple / Magenta:** An extra-spectral mixture requiring two or more distinct wavelengths from opposite ends of the physical spectrum (e.g., 440 nm blue + 650 nm red) to drive the blue and red opponent poles equally without green interference.

Because no single physical wavelength can stimulate the red and blue opponent channels with equal balance without exciting green, the hue circle must be closed by bridging the spectral extremes with nonspectral mixtures.

## Handprint Perspectives

Bruce MacEvoy emphasizes that the circularity of color space is an artifact of the visual brain rather than a property of physical light. In his color vision analyses *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*, he details how the S-cone's spectral sensitivity and the second peak in the Hurvich–Jameson red–green response curve prevent color from mapping as an open linear spectrum. David Briggs similarly notes that unique hues represent the null-points of the opponent channels, and that violet's perceptual redness is a direct consequence of cone ratio comparisons rather than optical wavelength properties *(Source: [[raw_sources/huevaluechroma/011.md|011.html]], [[raw_sources/huevaluechroma/062.md|062.html]])*.

> [!WARNING] **Contradiction Flag: Phenomenal binary hues vs. physical spectrum.** Physical optics treats the spectrum as an open, linear continuum of frequencies, but human color vision bends this line into a closed circuit. Conflating physical wavelength with perceptual color creates the illusion of a physical contradiction; the paradox exists only when color is mistakenly treated as a property of light rather than an opponent neural computation.

## Subtopics
- The open linear spectrum vs. the closed perceptual hue circle
- Cone photopigment beta-band absorption and S-cone input to the red–green channel
- Hurvich–Jameson dual-lobe chromatic response functions
- Unique blue (475 nm) as the red–green opponent crossover point
- Spectral violet (monochromatic) vs. nonspectral purple/magenta (polychromatic)
- Evolutionary and perceptual rationale for a four-category closed color space

## Cross-References
- [[Eye/Opponent-Process Color Coding]] — the neural wiring underlying the dual red lobes
- [[Colors/Nonspectral Colors|Nonspectral Colors]] — why purples and magentas do not exist in the physical spectrum
- [[Eye/Wavelength Perception|Wavelength Perception]] — cone absorption curves and spectral sensitivity
- [[Eye/Rods vs. Cones - Density & Distribution|Rods vs. Cones]] — photoreceptor mosaic and receptor spacing
- [[Colors/Color Wheel System]] — how the closed circle is mapped in standard color systems
- [[Colors/Why CMY Beats RYB for Color Mixing]] — why magenta acts as a primary in subtractive mixing
- [[Intersections/The Neuroscience Behind Why Colours Rewire Your Brain|The Neuroscience Behind Why Colours Rewire Your Brain]] — higher-order cortical color representation

## Sources
* "Color Appearance: On Seeing Red—or Yellow, or Green, or Blue" — I. Abramov & J. Gordon
* "Redness from short-wavelength-sensitive cones does not induce greenness" — S. K. Shevell
* "Hue signals from short- and middle-wavelength-sensitive cones" — B. Drum
* "Some Quantitative Aspects of an Opponent-Colors Theory II: Brightness, Saturation, and Hue in Normal and Dichromatic Vision" — L. M. Hurvich & D. Jameson
* "A rationale for the structure of color space" — R. Lotto & D. Purves
* "A magenta gap in the colour wheel" — A. A. Silva & P. Topa
* "Unique hues and their stimuli—state of the art" — R. G. Kuehni
* "handprint: color vision" — Bruce MacEvoy ([[raw_sources/handprint/color18a.md|color18a.html]])
* "The Dimensions of Colour" — David Briggs ([[raw_sources/huevaluechroma/011.md|011.html]], [[raw_sources/huevaluechroma/062.md|062.html]])