import os
import re
from collections import Counter

wiki_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"

mapping = {
    r"Light\Wave Nature.md": "color18a.md",
    r"Light\The Visible Spectrum.md": "color18a.md",
    r"Light\Reflection vs. Emission.md": "color18b.md",
    r"Light\Illuminants & Correlated Color Temperature.md": "color12.md",
    r"Eye\Anatomy.md": "color18a.md",
    r"Eye\Wavelength Perception.md": "color18a.md",
    r"Eye\Opponent-Process Color Coding.md": "color18a.md",
    r"Colors\CIE Systems.md": "color18a.md",
    r"Colors\Munsell Notation.md": "color11.md",
    r"Colors\MacAdam Ellipses.md": "color18a.md",
    r"Painting\Composition.md": "tech13.md",
    r"Painting\Pigments\Chemistry.md": "pigmt1.md",
    r"Painting\Pigments\Natural vs. Synthetic.md": "pigmt1.md",
    r"Painting\Pigments\High-Chroma Synthetics.md": "pigmt1.md",
    r"Painting\Pigments\Particle Size-Tinting-Polymorphism.md": "pigmt3.md",
    r"Colors\Gamuts\Gamuts.md": "color13.md"
}

out_lines = []

for stub, handprint_file in mapping.items():
    stub_path = os.path.join(wiki_dir, stub)
    hp_path = os.path.join(wiki_dir, "raw_sources", "handprint", handprint_file)
    
    if not os.path.exists(stub_path) or not os.path.exists(hp_path):
        continue
        
    with open(stub_path, 'r', encoding='utf-8') as f:
        stub_text = f.read()
        
    # Get keywords from stub (ignoring common words)
    words = re.findall(r'\b[a-zA-Z]{5,}\b', stub_text.lower())
    common = {"handprint", "notes", "perspectives", "source", "cross", "references", "subtopics", "scope", "synthesized", "content"}
    words = [w for w in words if w not in common]
    top_words = [w[0] for w in Counter(words).most_common(10)]
    
    with open(hp_path, 'r', encoding='utf-8') as f:
        hp_text = f.read()
        
    paragraphs = hp_text.split("\n\n")
    best_score = 0
    best_p = ""
    best_idx = 0
    
    for i, p in enumerate(paragraphs):
        p_lower = p.lower()
        score = sum(1 for w in top_words if w in p_lower)
        # weight paragraphs that are substantive
        if score > best_score and len(p) > 200:
            best_score = score
            best_idx = i
            
    if best_score > 0:
        # extract best paragraph and surrounding context
        start = max(0, best_idx - 1)
        end = min(len(paragraphs), best_idx + 2)
        chunk = "\n\n".join(paragraphs[start:end])
    else:
        chunk = "No highly relevant text found based on keywords."
        
    out_lines.append(f"### {stub}\n\n**Keywords used:** {', '.join(top_words)}\n\n**Extracted text from {handprint_file}:**\n{chunk}\n\n{'='*50}\n")

with open(os.path.join(wiki_dir, "snippets.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Created snippets.md")
