import os

wiki_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"

# 1. Create Intersections/Optical vs. Physical Mixture.md
optical_physical_path = os.path.join(wiki_dir, "Intersections", "Optical vs. Physical Mixture.md")
optical_physical_content = """# Optical vs. Physical Mixture

**Scope:** The distinction between visual/optical mixing (additive) and physical paint mixing (subtractive), specifically addressing the complementary color and primary color fallacies.

## Handprint Notes / Perspectives

> [!WARNING] **The "Primary Colors" and Complementary Color Fallacies**
> 
> According to extensive analysis by Bruce MacEvoy (Handprint), traditional color theory routinely conflates optical (visual) principles with physical paint mixing. This leads to two major misconceptions that are widely taught but physically incorrect:
> 
> **1. Visual Complements vs. Mixing Complements**
> Traditional theory assumes that colors opposite each other on the color wheel are both *visual* complements (they contrast most strongly to the eye, grounded in opponent-process theory) AND *mixing* complements (they mix to a neutral gray). Handprint demonstrates that **visual and mixing complements are almost never the same.**
> 
> For example:
> * The *visual* complement of Phthalo Green (PG7) is Quinacridone Rose.
> * However, if you physically mix PG7 and Quinacridone Rose, you do not get a neutral gray—you get a dark violet. The actual *mixing* complement for PG7 is a middle red.
> 
> **2. The Myth of "Primary Colors"**
> Traditional theory relies on three "primary colors" (e.g., Red, Yellow, Blue) and assumes mixtures must not cross these "primary boundaries" to avoid muddy colors. Handprint argues that "primary colors" are merely an arbitrary boundary, not a physical law. 
> 
> In reality, saturation costs (the dulling of a mixture) depend purely on the distance between two paints on the hue circle and their individual chroma. Using only three primary paints unnecessarily restricts the gamut. Saturation costs are an unavoidable, universal rule of physical paint mixing, not a result of violating primary boundaries.
> 
> *(Source: [[raw_sources/handprint/color14.md|color14.html]] and [[raw_sources/handprint/color16.md|color16.html]])*
"""
with open(optical_physical_path, "w", encoding="utf-8") as f:
    f.write(optical_physical_content)

# 2. Update Intersections/Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing.md
# I will just append the color wheel fallacy to it.
additive_subtractive_path = os.path.join(wiki_dir, "Intersections", "Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing.md")
additive_subtractive_addition = """

## Handprint Notes / Perspectives

> [!WARNING] **The Color Wheel Fallacy (Subtractive vs. Additive Mixing)**
> 
> According to Bruce MacEvoy (Handprint), the application of a geometrically perfect color wheel to paint mixing is a fundamental error known as the **"Color Wheel Fallacy."**
> 
> The traditional color wheel (and modern uniform color spaces like CIELAB) successfully models *additive light mixing* (where light is emitted). In additive mixing, lights can be made brighter or dimmer without altering the color of their mixtures, and the simple geometry of the wheel predicts outcomes accurately.
> 
> However, **paint mixing is subtractive and bound by multiplicative reflectance overlap** (reflecting vs. emitting light). When you mix two paints, you are multiplying their reflectance curves, which does not behave with geometric symmetry. Furthermore, paint chroma changes unpredictably when diluted.
> 
> Therefore, opponent-color theory and geometrical color wheels are grounded in the physics of additive light mixing and the biology of the eye. They do not—and mathematically cannot—accurately predict the physical reality of subtractive paint mixing. 
> 
> *(Source: [[raw_sources/handprint/color14.md|color14.html]])*
"""
with open(additive_subtractive_path, "a", encoding="utf-8") as f:
    f.write(additive_subtractive_addition)

# 3. Add pointers to the 4 originally-flagged pages
pointer = "\n> [!TIP]\n> **Note:** This traditional treatment holds for additive light but not for paint mixing — see [[Optical vs. Physical Mixture]] and [[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing]] for why."

pages_to_flag = [
    os.path.join(wiki_dir, "Eye", "Opponent-Process Color Coding.md"),
    os.path.join(wiki_dir, "Painting", "Composition.md"),
    os.path.join(wiki_dir, "Painting", "Pigments", "Natural vs. Synthetic.md"),
    os.path.join(wiki_dir, "Colors", "CIE Systems.md")
]

for page in pages_to_flag:
    if os.path.exists(page):
        with open(page, "a", encoding="utf-8") as f:
            f.write(pointer)

print("Updates completed successfully.")
