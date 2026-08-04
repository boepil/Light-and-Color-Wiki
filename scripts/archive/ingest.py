import os
import re

wiki_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"
raw_dir = os.path.join(wiki_dir, "raw_sources")

def append_to_stub(rel_path, content):
    path = os.path.join(wiki_dir, rel_path)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            original = f.read()
        if "## Synthesized Content" in original:
            original = original.split("## Synthesized Content")[0]
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(original.strip() + "\n\n## Synthesized Content\n\n" + content.strip() + "\n")
    else:
        print(f"Not found: {path}")

def get_section(text, start_pattern, end_pattern=None):
    if end_pattern:
        match = re.search(f"{start_pattern}(.*?)(?={end_pattern})", text, re.DOTALL)
    else:
        match = re.search(f"{start_pattern}(.*)", text, re.DOTALL)
    return match.group(1).strip() if match else ""

# --- Eye ---
with open(os.path.join(raw_dir, "notebooklm_eye_notes.md"), 'r', encoding='utf-8') as f:
    eye_text = f.read()

anatomy = get_section(eye_text, r"### 1\. Eye Anatomy", r"### 2\.")
wavelength = get_section(eye_text, r"### 2\. Wavelength Perception by Cones", r"### 3\.")
opponent = get_section(eye_text, r"### 3\. Opponent-Process Theory")

append_to_stub(r"Eye\Anatomy.md", anatomy)
append_to_stub(r"Eye\Wavelength Perception.md", wavelength)
append_to_stub(r"Eye\Rods vs. Cones - Density & Distribution.md", wavelength)
append_to_stub(r"Eye\Visual Acuity & Receptor Spacing.md", anatomy)
append_to_stub(r"Eye\Opponent-Process Color Coding.md", opponent)

# --- Colors ---
with open(os.path.join(raw_dir, "notebooklm_colors_notes.md"), 'r', encoding='utf-8') as f:
    colors_text = f.read()

cie = get_section(colors_text, r"### 1\. CIE Systems: XYZ, xy, and Lab", r"### 2\.")
munsell = get_section(colors_text, r"### 2\. Munsell Notation and the 1943 Renotation", r"### 3\.")
macadam = get_section(colors_text, r"### 3\. MacAdam Ellipses and Limits", r"### 4\.")
gamuts = get_section(colors_text, r"### 4\. Gamuts: Pointer's and Device-Specific")

append_to_stub(r"Colors\CIE Systems.md", cie)
append_to_stub(r"Colors\Munsell Notation.md", munsell)
append_to_stub(r"Colors\MacAdam Ellipses.md", macadam)
append_to_stub(r"Colors\Gamuts\Optimal Color Solid-MacAdam Limits.md", macadam)
append_to_stub(r"Colors\Gamuts\Pointer's Gamut.md", gamuts)
append_to_stub(r"Colors\Gamuts\Device Gamuts.md", gamuts)

# --- Painting ---
with open(os.path.join(raw_dir, "notebooklm_painting_notes.md"), 'r', encoding='utf-8') as f:
    painting_text = f.read()

comp = get_section(painting_text, r"### 1\. Color Composition and Design", r"### 2\.")
chem = get_section(painting_text, r"### 2\. Pigment Chemistry and Physical Properties", r"### 3\.")
spectral = get_section(painting_text, r"### 3\. Sourcing and Analyzing Spectral Data", r"### 4\.")
hist = get_section(painting_text, r"### 4\. Historical Use of Color in Art Movements")

append_to_stub(r"Painting\Composition.md", comp)
append_to_stub(r"Painting\Pigments\Chemistry.md", chem)
append_to_stub(r"Painting\Pigments\Natural vs. Synthetic.md", chem)
append_to_stub(r"Painting\Pigments\High-Chroma Synthetics.md", chem)
append_to_stub(r"Painting\Pigments\Particle Size-Tinting-Polymorphism.md", chem)
append_to_stub(r"Painting\Pigments\Sourcing Real Spectral Data.md", spectral)

append_to_stub(r"Painting\Movements & Painters\Vermeer-Dutch Golden Age.md", hist)
append_to_stub(r"Painting\Movements & Painters\Impressionism.md", hist)
append_to_stub(r"Painting\Movements & Painters\Neo-Impressionism-Pointillism.md", hist)
append_to_stub(r"Painting\Movements & Painters\Post-Impressionism.md", hist)
append_to_stub(r"Painting\Movements & Painters\Bauhaus.md", hist)
append_to_stub(r"Painting\Movements & Painters\Color Field.md", hist)

# --- Light ---
with open(os.path.join(raw_dir, "notebooklm_light_notes.md"), 'r', encoding='utf-8') as f:
    light_text = f.read()

sec1 = get_section(light_text, r"### 1\. Fundamental Nature of Light: Electromagnetic Radiation and Duality", r"### 2\.")
sec2 = get_section(light_text, r"### 2\. Physical Properties: Wavelength, Frequency, and Energy", r"### 3\.")
sec3 = get_section(light_text, r"### 3\. The Visible Spectrum and Prismatic Dispersion", r"### 4\.")
sec4 = get_section(light_text, r"### 4\. Emission vs\. Reflection", r"### 5\.")
sec5 = get_section(light_text, r"### 5\. Interactions with Matter: Absorption, Refraction, and Scattering", r"### 6\.")
sec6 = get_section(light_text, r"### 6\. Illuminants and Spectral Power Distributions \(SPD\)", r"### 7\.")
sec7 = get_section(light_text, r"### 7\. Correlated Color Temperature \(CCT\)", r"### 8\.")
sec8 = get_section(light_text, r"### 8\. Spectral Locus and Excitation Purity", r"### 9\.")
sec9_10 = get_section(light_text, r"### 9\. Natural Daylight Variation and Atmospheric Physics")

append_to_stub(r"Light\Wave Nature.md", sec1 + "\n\n" + sec2)
append_to_stub(r"Light\The Visible Spectrum.md", sec3)
append_to_stub(r"Light\Reflection vs. Emission.md", sec4 + "\n\n" + sec5)
append_to_stub(r"Light\Illuminants & Correlated Color Temperature.md", sec6 + "\n\n" + sec7)
append_to_stub(r"Light\Spectral Locus & Excitation Purity.md", sec8)
append_to_stub(r"Light\Natural Daylight Variation & Hyperspectral Scene Data.md", sec9_10)

print("Ingest complete.")
