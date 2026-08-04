import os
import re

wiki_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"

# 1. Expand Optical vs. Physical Mixture.md
optical_physical_path = os.path.join(wiki_dir, "Intersections", "Optical vs. Physical Mixture.md")
with open(optical_physical_path, "r", encoding="utf-8") as f:
    op_text = f.read()

# We need to replace the "The Myth of "Primary Colors"" section with a broader section covering Primary Colors and Geometric Harmonies.
# Let's just rewrite the whole file cleanly.
new_op_text = """# Optical vs. Physical Mixture

**Scope:** The distinction between visual/optical mixing (additive) and physical paint mixing (subtractive), specifically addressing the complementary color and primary color fallacies.

## Handprint Notes / Perspectives

> [!WARNING] **The Categorical vs. Continuous Fallacy in Color Theory**
> 
> According to extensive analysis by Bruce MacEvoy (Handprint), traditional color theory routinely conflates optical (visual) principles with physical paint mixing, relying on arbitrary geometric categories rather than continuous physical properties. This leads to major misconceptions:
> 
> **1. Visual Complements vs. Mixing Complements**
> Traditional theory assumes that colors opposite each other on the color wheel are both *visual* complements (they contrast most strongly to the eye, grounded in opponent-process theory) AND *mixing* complements (they mix to a neutral gray). Handprint demonstrates that **visual and mixing complements are almost never the same.**
> For example, the *visual* complement of Phthalo Green (PG7) is Quinacridone Rose. However, if you physically mix them, you get a dark violet, not a neutral gray. The actual *mixing* complement for PG7 is a middle red.
> 
> **2. The Myth of "Primary Colors" and Geometric Harmonies**
> Traditional color theory relies on strict geometric categories—such as three "primary colors" that must not be crossed, or rigid geometric harmonies (triadic, split-complementary, analogous). Handprint argues that these are artificial 18th-century dogmas, not physical laws. 
> 
> Real paint behavior and true visual harmony are governed by **continuous properties** (hue-circle distance, value/lightness, and chroma), not category membership:
> *   **Primary Colors are Arbitrary:** Using only three "primary" paints (like traditional synthetics or earths) unnecessarily restricts the painter's gamut. Saturation costs (the dulling of a mixture) depend purely on the distance between two paints on the hue circle and their individual chroma. Adding more distinct, high-chroma pigments to a palette actually expands the mixable color space cleanly.
> *   **Geometric Harmonies are Flawed:** Harmony is not achieved by picking hues that form a perfect triangle on a wheel. Instead, almost any hue combination can be harmonious if their *values* and *saturations* are carefully managed and contrasted.
> 
> *(Source: [[raw_sources/handprint/color14.md|color14.html]], [[raw_sources/handprint/color16.md|color16.html]], [[raw_sources/handprint/tech13.md|tech13.html]])*
"""

with open(optical_physical_path, "w", encoding="utf-8") as f:
    f.write(new_op_text)

# 2. Reduce Composition, Gamuts, Natural vs Synthetic to pointers
pointer_text = """## Handprint Perspectives

> [!TIP]
> **Note:** Traditional treatments of color—such as rigid "primary color" boundaries and geometric "triadic/analogous" harmonies—are abstract categorical rules that fail to capture the physical reality of continuous paint mixing. For Bruce MacEvoy's detailed analysis on why these 18th-century dogmas are replaced by continuous properties like hue-distance, value, and chroma, see [[Optical vs. Physical Mixture]]. *(Source: [[raw_sources/handprint/color13.md|color13.html]], [[raw_sources/handprint/tech13.md|tech13.html]])*
"""

pages_to_reduce = [
    os.path.join(wiki_dir, "Painting", "Composition.md"),
    os.path.join(wiki_dir, "Colors", "Gamuts", "Gamuts.md"),
    os.path.join(wiki_dir, "Painting", "Pigments", "Natural vs. Synthetic.md")
]

for p in pages_to_reduce:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        clean = re.split(r'##\s*Handprint', content, 1)[0].strip()
        with open(p, "w", encoding="utf-8") as f:
            f.write(clean + "\n\n" + pointer_text + "\n")

# 3. Ensure CIE Systems clearly distinguishes perceptual uniformity from mixture predictability.
cie_path = os.path.join(wiki_dir, "Colors", "CIE Systems.md")
if os.path.exists(cie_path):
    with open(cie_path, "r", encoding="utf-8") as f:
        cie_text = f.read()
    
    clean_cie = re.split(r'##\s*Handprint', cie_text, 1)[0].strip()
    new_cie_perspective = """## Handprint Perspectives

Handprint views modern CIE systems, particularly CIELAB and CIECAM, as the most accurate tools available for mapping human perceptual color space, praising their foundation in objective spectrophotometric measurement rather than subjective artistic lore. 

**Contradiction Flag: Perceptual Uniformity vs. Mixture Predictability.** 
While CIELAB excels at *perceptual uniformity* (ensuring that equal steps in the model look equally different to the human eye), MacEvoy explicitly warns against assuming this grants it *mixture predictability*. Because the subtractive mixing of pigments introduces nonlinear saturation costs, a uniform perceptual space cannot be used to mathematically predict the outcome of combining two physical paints. The model perfectly maps what we see, but it does not map how paints physically behave when mixed. *(Source: [[raw_sources/handprint/color18a.md|color18a.html]])*
"""
    with open(cie_path, "w", encoding="utf-8") as f:
        f.write(clean_cie + "\n\n" + new_cie_perspective + "\n")

# 4. Add pointer to MacAdam Ellipses.md
macadam_path = os.path.join(wiki_dir, "Colors", "MacAdam Ellipses.md")
if os.path.exists(macadam_path):
    with open(macadam_path, "a", encoding="utf-8") as f:
        f.write("\n> [!TIP]\n> **Note:** While models attempting to correct for these ellipses (like CIELAB) achieve *perceptual uniformity*, Handprint notes that this property does not grant them *mixture predictability* for physical paints. See [[CIE Systems]] for details.\n")

print("Refinement completed.")
