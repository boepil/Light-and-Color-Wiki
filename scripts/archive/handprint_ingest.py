import os
import re

wiki_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"
handprint_dir = os.path.join(wiki_dir, "raw_sources", "handprint")

# Mapping of Wiki stubs to Handprint source files
mapping = {
    # Light
    r"Light\Wave Nature.md": ["color18a.md"],
    r"Light\The Visible Spectrum.md": ["color18a.md"],
    r"Light\Reflection vs. Emission.md": ["color18b.md"],
    r"Light\Illuminants & Correlated Color Temperature.md": ["color12.md"],
    
    # Eye
    r"Eye\Anatomy.md": ["color18a.md"],
    r"Eye\Wavelength Perception.md": ["color18a.md"],
    r"Eye\Opponent-Process Color Coding.md": ["color18a.md", "color16.md"],
    
    # Colors
    r"Colors\CIE Systems.md": ["color18a.md"],
    r"Colors\Munsell Notation.md": ["color11.md"],
    r"Colors\MacAdam Ellipses.md": ["color18a.md"],
    
    # Painting / Composition
    r"Painting\Composition.md": ["tech13.md"],
    
    # Pigments
    r"Painting\Pigments\Chemistry.md": ["pigmt1.md"],
    r"Painting\Pigments\Natural vs. Synthetic.md": ["pigmt1.md"],
    r"Painting\Pigments\High-Chroma Synthetics.md": ["pigmt1.md"],
    r"Painting\Pigments\Particle Size-Tinting-Polymorphism.md": ["pigmt3.md"],
    r"Painting\Pigments\Sourcing Real Spectral Data.md": ["pigmt8.md"],
    
    # Color mixing
    r"Intersections\Optical vs. Physical Mixture.md": ["mix.md", "color14.md"],
    r"Intersections\Natural Light Gamut vs. Pigment Gamut / Metamerism.md": ["color18b.md"]
}

def extract_handprint_intro(filename):
    path = os.path.join(handprint_dir, filename)
    if not os.path.exists(path):
        return ""
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract the first few meaningful paragraphs (skip title and links at the top)
    # Paragraphs in the markdown are separated by double newlines.
    paragraphs = content.split("\n\n")
    intro_paragraphs = []
    
    for p in paragraphs:
        p = p.strip()
        # Skip titles, short navigation links, or lines that start with 'Title:' or 'Source:'
        if not p or len(p) < 100 or p.startswith("Title:") or p.startswith("Source:") or p.startswith("---"):
            continue
        intro_paragraphs.append(p)
        if len(intro_paragraphs) >= 2: # Get max 2 good paragraphs
            break
            
    intro = "\n\n".join(intro_paragraphs)
    return intro

def append_handprint(rel_path, handprint_files):
    path = os.path.join(wiki_dir, rel_path)
    if not os.path.exists(path):
        print(f"Skipping {rel_path} - file not found.")
        return
        
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
        
    if "## Handprint Notes / Perspectives" in original:
        print(f"Already appended to {rel_path}")
        return
        
    perspectives = []
    for hf in handprint_files:
        intro = extract_handprint_intro(hf)
        if intro:
            # Add a citation/link to the raw source
            source_link = f"[[raw_sources/handprint/{hf}|{hf.replace('.md', '.html')}]]"
            perspective = f"> [!NOTE] **Perspective from Handprint ({source_link})**\n> \n"
            # Prefix each line with blockquote to format nicely
            perspective += "\n".join([f"> {line}" for line in intro.split("\n")])
            perspectives.append(perspective)
            
    if perspectives:
        new_content = original.strip() + "\n\n## Handprint Notes / Perspectives\n\n" + "\n\n".join(perspectives) + "\n"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {rel_path}")

for stub, files in mapping.items():
    append_handprint(stub, files)

print("Ingestion complete.")
