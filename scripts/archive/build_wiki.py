import os

base_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"

pages = {
    "Home": {
        "path": "Home.md",
        "scope": "Landing page with a short overview of how the four main sections (Light, Eye, Colors, Painting) relate to each other, plus a suggested reading order.",
        "subtopics": ["Overview of Light", "Overview of the Eye", "Overview of Colors", "Overview of Painting", "Suggested Reading Order"],
        "links": ["[[Wave Nature]]", "[[Anatomy]]", "[[CIE Systems]]", "[[Composition]]"]
    },
    
    # LIGHT
    "Wave Nature": {
        "path": "Light/Wave Nature.md",
        "scope": "Details the physical wave nature of light, covering wavelength, frequency, and spectral power distributions.",
        "subtopics": ["Wavelength and Frequency", "Spectral Power Distributions", "Energy and Photons"],
        "links": ["[[The Visible Spectrum]]", "[[Color Matching Functions and the Photopic Luminosity Function]]"]
    },
    "The Visible Spectrum": {
        "path": "Light/The Visible Spectrum.md",
        "scope": "Defines the visible spectrum purely as a physical range of electromagnetic wavelengths.",
        "subtopics": ["Visible Range limits", "Infrared and Ultraviolet Boundaries"],
        "links": ["[[Wave Nature]]"]
    },
    "Reflection vs Emission": {
        "path": "Light/Reflection vs. Emission.md",
        "scope": "Compares physical emission of light versus reflection and absorption.",
        "subtopics": ["Emission Physics", "Reflection and Absorption"],
        "links": ["[[The Visible Spectrum]]"]
    },
    "Illuminants and Correlated Color Temperature": {
        "path": "Light/Illuminants & Correlated Color Temperature.md",
        "scope": "Explores standard illuminants and the concept of Correlated Color Temperature (CCT).",
        "subtopics": ["Standard Illuminants", "Blackbody Locus", "CCT Calculation"],
        "links": ["[[Natural Daylight Variation & Hyperspectral Scene Data]]"]
    },
    "Spectral Locus and Excitation Purity": {
        "path": "Light/Spectral Locus & Excitation Purity.md",
        "scope": "Defines the physical concept of the spectral locus and excitation purity.",
        "subtopics": ["Spectral Locus Definition", "Excitation Purity vs Saturation"],
        "links": ["[[CIE Systems]]"]
    },
    "Natural Daylight Variation and Hyperspectral Scene Data": {
        "path": "Light/Natural Daylight Variation & Hyperspectral Scene Data.md",
        "scope": "Analyzes the physical variations of natural daylight and the use of hyperspectral scene data.",
        "subtopics": ["Daylight Variation", "Hyperspectral Data", "Measurement Techniques"],
        "links": ["[[Illuminants & Correlated Color Temperature]]", "[[Natural Light Gamut vs. Pigment Gamut / Metamerism]]"]
    },
    
    # EYE
    "Anatomy": {
        "path": "Eye/Anatomy.md",
        "scope": "Covers the biological anatomy of the eye, specifically the cornea, lens, and retina.",
        "subtopics": ["Cornea and Lens", "Retina", "Optic Nerve"],
        "links": ["[[Wavelength Perception]]", "[[Rods vs. Cones - Density & Distribution]]"]
    },
    "Wavelength Perception": {
        "path": "Eye/Wavelength Perception.md",
        "scope": "Details how cones biologically encode physical wavelengths into a neural signal.",
        "subtopics": ["Photoreceptor Activation", "L, M, and S Cones", "Signal Transduction"],
        "links": ["[[Anatomy]]", "[[Opponent-Process Color Coding]]", "[[Color Matching Functions and the Photopic Luminosity Function]]"]
    },
    "Rods vs Cones - Density and Distribution": {
        "path": "Eye/Rods vs. Cones - Density & Distribution.md",
        "scope": "Analyzes the density and spatial distribution of rods and cones across the retina.",
        "subtopics": ["Fovea vs Periphery", "Rod Distribution", "Cone Distribution"],
        "links": ["[[Anatomy]]", "[[Visual Acuity & Receptor Spacing]]"]
    },
    "Visual Acuity and Receptor Spacing": {
        "path": "Eye/Visual Acuity & Receptor Spacing.md",
        "scope": "Relates visual acuity to the physical spacing of photoreceptors in the eye.",
        "subtopics": ["Receptor Spacing", "Limits of Resolution", "Acuity Measurement"],
        "links": ["[[Rods vs. Cones - Density & Distribution]]"]
    },
    "Opponent-Process Color Coding": {
        "path": "Eye/Opponent-Process Color Coding.md",
        "scope": "Explains the neural opponent-process theory of color coding.",
        "subtopics": ["Red-Green Axis", "Blue-Yellow Axis", "Light-Dark Axis", "Neural Wiring"],
        "links": ["[[Wavelength Perception]]", "[[Why Lab/Munsell Were Built for Perceptual Uniformity]]", "[[Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing]]"]
    },
    
    # COLORS
    "CIE Systems": {
        "path": "Colors/CIE Systems.md",
        "scope": "Overview of CIE coordinate systems including the xy diagram, XYZ, and Lab spaces.",
        "subtopics": ["CIE xy Chromaticity Diagram", "CIE XYZ", "CIE Lab"],
        "links": ["[[Spectral Locus & Excitation Purity]]", "[[Color Matching Functions and the Photopic Luminosity Function]]", "[[Why Lab/Munsell Were Built for Perceptual Uniformity]]"]
    },
    "Munsell Notation": {
        "path": "Colors/Munsell Notation.md",
        "scope": "Explores the Munsell notation system, its structure, the 1943 Renotation, and its open-ended chroma.",
        "subtopics": ["Hue, Value, Chroma", "1943 Renotation", "Open-ended Chroma concept"],
        "links": ["[[Why Lab/Munsell Were Built for Perceptual Uniformity]]"]
    },
    "Gamuts": {
        "path": "Colors/Gamuts/Gamuts.md",
        "scope": "Parent page introducing gamuts and limits of reproducible color spaces.",
        "subtopics": ["Definition of Gamut", "Color Space Limitations"],
        "links": ["[[Optimal Color Solid/MacAdam Limits]]", "[[Pointer's Gamut]]", "[[Device Gamuts]]"]
    },
    "Optimal Color Solid - MacAdam Limits": {
        "path": "Colors/Gamuts/Optimal Color Solid-MacAdam Limits.md",
        "scope": "Discusses the Optimal Color Solid and MacAdam Limits of maximum achievable reflecting colors.",
        "subtopics": ["Optimal Color Solid", "MacAdam Limits"],
        "links": ["[[Gamuts]]"]
    },
    "Pointer's Gamut": {
        "path": "Colors/Gamuts/Pointer's Gamut.md",
        "scope": "Analyzes Pointer's Gamut of real surface colors.",
        "subtopics": ["Empirical Gamut of Real Colors", "Comparison with MacAdam limits"],
        "links": ["[[Gamuts]]"]
    },
    "Device Gamuts": {
        "path": "Colors/Gamuts/Device Gamuts.md",
        "scope": "Examines device-specific color gamuts such as those of displays and printers.",
        "subtopics": ["Display Gamuts", "Print Gamuts", "Gamut Mapping"],
        "links": ["[[Gamuts]]"]
    },
    "MacAdam Ellipses": {
        "path": "Colors/MacAdam Ellipses.md",
        "scope": "Details MacAdam ellipses and their mapping of just-noticeable differences in color.",
        "subtopics": ["Just-Noticeable Differences", "Mapping on xy Diagram"],
        "links": ["[[CIE Systems]]"]
    },
    
    # PAINTING
    "Pigments": {
        "path": "Painting/Pigments/Pigments.md",
        "scope": "Parent page for the study of pigments, their material nature, and application.",
        "subtopics": ["Overview of Pigments", "Historical to Modern Transition"],
        "links": ["[[Chemistry]]", "[[Natural vs. Synthetic]]", "[[High-Chroma Synthetics]]", "[[Sourcing Real Spectral Data]]", "[[Particle Size/Tinting/Polymorphism]]"]
    },
    "Chemistry": {
        "path": "Painting/Pigments/Chemistry.md",
        "scope": "Discusses the chemical basis of painting pigments.",
        "subtopics": ["Inorganic vs Organic", "Lightfastness Chemistry"],
        "links": ["[[Pigments]]"]
    },
    "Natural vs Synthetic": {
        "path": "Painting/Pigments/Natural vs. Synthetic.md",
        "scope": "Compares historical natural earth/mineral pigments with modern synthetic alternatives.",
        "subtopics": ["Earth Pigments", "Synthetic Advancements"],
        "links": ["[[Pigments]]"]
    },
    "High-Chroma Synthetics": {
        "path": "Painting/Pigments/High-Chroma Synthetics.md",
        "scope": "Explores the introduction and impact of high-chroma synthetic pigments like PG7, PG36, PB15:3, PR122, and PV23.",
        "subtopics": ["Phthalocyanines", "Quinacridones", "Dioxazine", "Gamut Expansion"],
        "links": ["[[Pigments]]"]
    },
    "Sourcing Real Spectral Data Pigments": {
        "path": "Painting/Pigments/Sourcing Real Spectral Data.md",
        "scope": "Methodologies for sourcing and measuring real spectral reflectance of pigments.",
        "subtopics": ["Spectrophotometry of Paint", "Database Sources"],
        "links": ["[[Pigments]]", "[[Data & Methodology]]"]
    },
    "Particle Size - Tinting - Polymorphism": {
        "path": "Painting/Pigments/Particle Size-Tinting-Polymorphism.md",
        "scope": "Examines how pigment particle size, tinting strength, and crystal polymorphism affect color.",
        "subtopics": ["Particle Size Effects", "Tinting Strength", "Polymorphism Variations"],
        "links": ["[[Pigments]]"]
    },
    "Composition": {
        "path": "Painting/Composition.md",
        "scope": "Focuses on color composition, harmony, and structural use of color in painting.",
        "subtopics": ["Color Harmony", "Balance and Proportion", "Visual Weight"],
        "links": []
    },
    "Movements and Painters": {
        "path": "Painting/Movements & Painters/Movements & Painters.md",
        "scope": "Parent page covering the historical evolution of color use across art movements and specific painters.",
        "subtopics": ["Historical Overview", "Evolution of the Palette"],
        "links": ["[[Vermeer/Dutch Golden Age]]", "[[Newton's Influence on Painters]]", "[[Romanticism/Turner]]", "[[Impressionism]]", "[[Neo-Impressionism/Pointillism]]", "[[Post-Impressionism]]", "[[Fauvism]]", "[[Bauhaus]]", "[[Op Art]]", "[[Color Field]]"]
    },
    "Vermeer - Dutch Golden Age": {
        "path": "Painting/Movements & Painters/Vermeer-Dutch Golden Age.md",
        "scope": "Analyzes the use of color by Vermeer and during the Dutch Golden Age.",
        "subtopics": ["Ultramarine usage", "Observation of Light"],
        "links": ["[[Movements & Painters]]"]
    },
    "Newton's Influence on Painters": {
        "path": "Painting/Movements & Painters/Newton's Influence on Painters.md",
        "scope": "Examines the impact of Isaac Newton's optical theories on subsequent painters and color theory.",
        "subtopics": ["Opticks", "The Color Wheel"],
        "links": ["[[Movements & Painters]]"]
    },
    "Romanticism - Turner": {
        "path": "Painting/Movements & Painters/Romanticism-Turner.md",
        "scope": "Discusses color use in Romanticism, with a focus on J.M.W. Turner's expressive light.",
        "subtopics": ["Atmospheric Perspective", "Expressive Light and Color"],
        "links": ["[[Movements & Painters]]"]
    },
    "Impressionism": {
        "path": "Painting/Movements & Painters/Impressionism.md",
        "scope": "Explores Impressionism (Monet, Renoir, Pissarro) and their focus on capturing fleeting light.",
        "subtopics": ["En Plein Air", "Broken Color", "Monet, Renoir, Pissarro"],
        "links": ["[[Movements & Painters]]"]
    },
    "Neo-Impressionism - Pointillism": {
        "path": "Painting/Movements & Painters/Neo-Impressionism-Pointillism.md",
        "scope": "Details Neo-Impressionism and Pointillism (Seurat, Signac) and their scientific application of optical mixing.",
        "subtopics": ["Optical Mixing", "Divisionism", "Seurat, Signac"],
        "links": ["[[Movements & Painters]]"]
    },
    "Post-Impressionism": {
        "path": "Painting/Movements & Painters/Post-Impressionism.md",
        "scope": "Covers Post-Impressionist use of color as structure and emotion (Van Gogh, Cézanne).",
        "subtopics": ["Color as Structure (Cézanne)", "Expressive Color (Van Gogh)"],
        "links": ["[[Movements & Painters]]"]
    },
    "Fauvism": {
        "path": "Painting/Movements & Painters/Fauvism.md",
        "scope": "Examines Fauvism (Matisse, Derain) and the liberation of color from descriptive realism.",
        "subtopics": ["Arbitrary Color", "Maximum Saturation", "Matisse, Derain"],
        "links": ["[[Movements & Painters]]"]
    },
    "Bauhaus": {
        "path": "Painting/Movements & Painters/Bauhaus.md",
        "scope": "Discusses color theory and pedagogy at the Bauhaus (Itten, Klee, Kandinsky).",
        "subtopics": ["Itten's Color Theory", "Kandinsky's Synesthesia", "Klee's Approaches"],
        "links": ["[[Movements & Painters]]"]
    },
    "Op Art": {
        "path": "Painting/Movements & Painters/Op Art.md",
        "scope": "Explores Op Art (Vasarely, Riley) and its high-contrast perceptual effects.",
        "subtopics": ["Optical Illusions", "Vibrating Boundaries", "Vasarely, Riley"],
        "links": ["[[Movements & Painters]]"]
    },
    "Color Field": {
        "path": "Painting/Movements & Painters/Color Field.md",
        "scope": "Analyzes the immersive use of color in the Color Field movement (Rothko, Newman).",
        "subtopics": ["Large Scale Color", "Emotional Resonance", "Rothko, Newman"],
        "links": ["[[Movements & Painters]]"]
    },
    
    # INTERSECTIONS
    "Color Matching Functions": {
        "path": "Intersections/Color Matching Functions and the Photopic Luminosity Function.md",
        "scope": "Cross-cutting page (Light × Eye) exploring how physical light is weighted by human biological sensitivity.",
        "subtopics": ["Deriving Color Matching Functions", "Photopic Luminosity V(lambda)", "Bridging Physics and Perception"],
        "links": ["[[Wave Nature]]", "[[Wavelength Perception]]", "[[CIE Systems]]"]
    },
    "Perceptual Uniformity": {
        "path": "Intersections/Why Lab-Munsell Were Built for Perceptual Uniformity.md",
        "scope": "Cross-cutting page (Eye × Colors) explaining the necessity of mathematically bending color spaces to match non-linear human perception.",
        "subtopics": ["Non-linear Perception", "Designing Lab", "Spacing in Munsell"],
        "links": ["[[Opponent-Process Color Coding]]", "[[CIE Systems]]", "[[Munsell Notation]]"]
    },
    "Gamut vs Metamerism": {
        "path": "Intersections/Natural Light Gamut vs. Pigment Gamut - Metamerism.md",
        "scope": "Cross-cutting page (Painting × Light) comparing the range of colors in nature to those achievable with pigments, and addressing metamerism.",
        "subtopics": ["Gamut Mapping Challenges", "Metamerism in Painting", "Spectral Limitations"],
        "links": ["[[Gamuts]]", "[[Pigments]]", "[[Natural Daylight Variation & Hyperspectral Scene Data]]"]
    },
    "Simultaneous Contrast": {
        "path": "Intersections/Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing.md",
        "scope": "Cross-cutting page (Painting × Eye) covering perceptual phenomena critical for painters.",
        "subtopics": ["Simultaneous Contrast", "Color Constancy", "Afterimages", "Subtractive vs Additive Mixing"],
        "links": ["[[Composition]]", "[[Opponent-Process Color Coding]]"]
    },
    
    # APPENDIX
    "History and Key Figures": {
        "path": "Appendix/History & Key Figures.md",
        "scope": "Short biographies and core contributions of key figures: Munsell, Schrödinger, MacAdam, Pointer, Chevreul, and the CIE committee.",
        "subtopics": ["Albert H. Munsell", "Erwin Schrödinger", "David MacAdam", "Michael Pointer", "Michel Eugène Chevreul", "CIE Committee"],
        "links": []
    },
    "Data and Methodology": {
        "path": "Appendix/Data & Methodology.md",
        "scope": "Details on sourcing spectral data, the CIE integration pipeline, and citation practices.",
        "subtopics": ["Sourcing Spectral Data", "CIE Integration Pipeline", "Citation Practices"],
        "links": []
    },
    "Project Notes": {
        "path": "Appendix/Project Notes.md",
        "scope": "Personal project notes on building a 3D color visualization, detailing the Three.js implementation and coordinate conventions.",
        "subtopics": ["Three.js Implementation", "Coordinate Conventions", "Visualization Challenges"],
        "links": []
    },
}

bibliography_content = """# Bibliography

## Light
* Color and Light in Nature (Lynch & Livingston)
* Light and Colour in the Outdoors (Minnaert)

## Eye
* Vision Science: Photons to Phenomenology (Palmer)
* Color Vision: From Genes to Perception (Gegenfurtner & Sharpe eds.)

## Colors
* Color Science (Wyszecki & Stiles)
* Measuring Colour (Hunt)
* Color Appearance Models (Fairchild)

## Painting
* The Principles of Harmony and Contrast of Colours (Chevreul)
* Interaction of Color (Albers)
* The Art of Color (Itten)
* Colour and Culture (Gage)
* Color and Meaning (Gage)
* Colour in Art (Gage)
* Chromophobia (Batchelor)
* Bright Earth (Ball)
* Color: A Natural History of the Palette (Finlay)
* The Artist's Handbook of Materials and Techniques (Mayer)
* Pigment Compendium (Eastaugh et al.)
"""

def generate_wiki():
    os.makedirs(base_dir, exist_ok=True)
    count = 0
    for key, data in pages.items():
        filepath = os.path.join(base_dir, data['path'])
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        content = f"# {os.path.basename(data['path']).replace('.md', '')}\n\n"
        content += f"**Scope:** {data['scope']}\n\n"
        
        content += "## Subtopics\n"
        for sub in data['subtopics']:
            content += f"- {sub}\n"
        content += "\n"
        
        if data['links']:
            content += "## Cross-References\n"
            for link in data['links']:
                content += f"- {link}\n"
            content += "\n"
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
        
    # Write Bibliography separately since it has a specific structure
    bib_path = os.path.join(base_dir, "Appendix/Bibliography.md")
    os.makedirs(os.path.dirname(bib_path), exist_ok=True)
    
    bib_content = bibliography_content + "\n**Scope:** A bibliography organized by section linking back to supporting pages.\n\n## Cross-References\n- [[History & Key Figures]]\n"
    with open(bib_path, "w", encoding="utf-8") as f:
        f.write(bib_content)
    count += 1
    
    print(f"Total pages created: {count}")

if __name__ == '__main__':
    generate_wiki()
