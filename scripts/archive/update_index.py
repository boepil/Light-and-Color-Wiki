import os
import re
from pathlib import Path

wiki_dir = Path(r"d:\_PROJECTS\My\ai\Light and Color Wiki")

all_files = list(wiki_dir.rglob("*.md"))
all_files = [f for f in all_files if "raw_sources" not in f.parts and ".system_generated" not in f.parts and "scratch" not in f.parts]

def get_summary(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Try to find "Scope:" or "**Scope:**"
    scope_match = re.search(r'\*\*Scope:\*\*\s*(.*?)(?=\n\n|\n##)', content, flags=re.IGNORECASE|re.DOTALL)
    if scope_match:
        return scope_match.group(1).replace('\n', ' ').strip()
    
    # Try to find the first paragraph after headings
    paragraphs = re.split(r'\n\n+', content)
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith("#") and not p.startswith("-") and not p.startswith("[") and not p.startswith(">"):
            # Return first sentence
            s = p.replace('\n', ' ')
            if '. ' in s:
                return s.split('. ')[0] + '.'
            return s[:100] + "..." if len(s) > 100 else s
            
    return "Stub page."

# Group files by section
sections = {
    "Appendix": [],
    "Colors": [],
    "Eye": [],
    "Gamuts": [],
    "Intersections": [],
    "Light": [],
    "Movements & Painters": [],
    "Painting": [],
    "Pigments": [],
    "Top-Level & Root": []
}

for f in all_files:
    rel_path = f.relative_to(wiki_dir)
    link = str(rel_path).replace("\\", "/").replace(".md", "")
    name = f.stem
    summary = get_summary(f)
    
    if len(rel_path.parts) > 1:
        parent = rel_path.parts[0]
        if parent in sections:
            sections[parent].append(f"- [[{link}|{name}]]: {summary}")
        else:
            sections["Top-Level & Root"].append(f"- [[{link}|{name}]]: {summary}")
    else:
        sections["Top-Level & Root"].append(f"- [[{link}|{name}]]: {summary}")

# Build index.md
index_content = "# Wiki Index\n\n"
for section in sorted(sections.keys()):
    if sections[section]:
        index_content += f"## {section}\n"
        for line in sorted(sections[section]):
            index_content += f"{line}\n"
        index_content += "\n"

with open(wiki_dir / "index.md", "w", encoding="utf-8") as f:
    f.write(index_content)
    
print(f"Step 3: index.md updated with {sum(len(v) for v in sections.values())} files and 1-line summaries.")
