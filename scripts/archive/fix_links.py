import os
from pathlib import Path

wiki_dir = Path(r"d:\_PROJECTS\My\ai\Light and Color Wiki")

replacements = {
    "Why Lab/Munsell Were Built for Perceptual Uniformity": "Why Lab-Munsell Were Built for Perceptual Uniformity",
    "Optimal Color Solid/MacAdam Limits": "Optimal Color Solid-MacAdam Limits",
    "Natural Light Gamut vs. Pigment Gamut / Metamerism": "Natural Light Gamut vs. Pigment Gamut - Metamerism",
    "Vermeer/Dutch Golden Age": "Vermeer-Dutch Golden Age",
    "Romanticism/Turner": "Romanticism-Turner",
    "Neo-Impressionism/Pointillism": "Neo-Impressionism-Pointillism",
    "Particle Size/Tinting/Polymorphism": "Particle Size-Tinting-Polymorphism",
    "[[Color Constancy]]": "[[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing|Color Constancy]]",
    "[[Real Spectral Data]]": "[[Sourcing Real Spectral Data|Real Spectral Data]]"
}

all_files = list(wiki_dir.rglob("*.md"))
all_files = [f for f in all_files if "raw_sources" not in f.parts and ".system_generated" not in f.parts and "scratch" not in f.parts]

for f in all_files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        
        new_content = content
        for old, new in replacements.items():
            if old in new_content:
                new_content = new_content.replace(old, new)
                
        if new_content != content:
            with open(f, "w", encoding="utf-8") as file:
                file.write(new_content)
    except Exception as e:
        pass
        
print("Step 1 fixes applied.")
