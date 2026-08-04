import os
from pathlib import Path
import re

wiki_dir = Path(r"d:\_PROJECTS\My\ai\Light and Color Wiki")

anatomy_path = wiki_dir / "Eye" / "Anatomy.md"
with open(anatomy_path, "r", encoding="utf-8") as f:
    anat_content = f.read()

new_anat_text = """## Handprint Perspectives

MacEvoy's approach to ocular anatomy focuses heavily on the uneven distribution and overlapping spectral sensitivities of the L, M, and S cones. He points out that our photoreceptors are not perfectly spaced to cover the visible spectrum evenly; rather, they are heavily clustered toward the longer (red/green) wavelengths.

> [!WARNING] **Contradiction Flag: Biological Asymmetry vs. Symmetrical Color Spaces**
> Traditional models and uniform color spaces often imply mathematically symmetrical spectral divisions to create neat color wheels. Handprint explicitly flags that because the L, M, and S cones are heavily clumped and unevenly distributed, mathematical symmetry in color spaces is a biological falsehood. This anatomical imbalance is the biological root of our perceptual bias toward "warm" colors and our extreme sensitivity to green hues, explaining why perfectly symmetrical color spaces cannot accurately model human vision without severe distortion. 
> 
> *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*"""

anat_content = re.sub(r'## Handprint Perspectives.*', new_anat_text, anat_content, flags=re.DOTALL)
with open(anatomy_path, "w", encoding="utf-8") as f:
    f.write(anat_content)

particle_path = wiki_dir / "Painting" / "Pigments" / "Particle Size-Tinting-Polymorphism.md"
with open(particle_path, "r", encoding="utf-8") as f:
    part_content = f.read()
    
new_part_text = """## Handprint Perspectives

Handprint heavily emphasizes that the physical behavior of a pigment—specifically its particle size and specific gravity—is just as important as its hue. Pigments with large, heavy particles (like Cobalt Blue or Ultramarine) settle rapidly into the valleys of watercolor paper, creating textural granulation. Conversely, finely milled synthetic organics stain the paper fibers evenly.

> [!WARNING] **Contradiction Flag: Abstract Hue vs. Physical Pigment Attributes**
> Traditional abstract color theory treats paint mixtures as pure combinations of "hue." Handprint points out that traditional color theory entirely ignores the physical realities of the paint. A painter must understand these physical properties (detailed in [[Chemistry]]) because combining a heavily granulating pigment with a staining pigment creates distinct visual separations and textural behaviors that simple, abstract color wheels cannot predict and are incapable of modeling.
> 
> *(Source: [[raw_sources/handprint/pigmt3.md|pigmt3.html]])*"""

part_content = re.sub(r'## Handprint Perspectives.*', new_part_text, part_content, flags=re.DOTALL)
with open(particle_path, "w", encoding="utf-8") as f:
    f.write(part_content)

print("Step 5: Contradictions folded in.")
