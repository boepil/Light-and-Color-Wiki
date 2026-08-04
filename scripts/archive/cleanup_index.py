import os
import re
from pathlib import Path

wiki_dir = Path(r"d:\_PROJECTS\My\ai\Light and Color Wiki")
index_path = wiki_dir / "index.md"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# We can parse the existing index.md to extract the links and their summaries.
# Or we can just rewrite it by reading the structure again, which is safer.

def get_summary(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()
    scope_match = re.search(r'\*\*Scope:\*\*\s*(.*?)(?=\n\n|\n##)', c, flags=re.IGNORECASE|re.DOTALL)
    if scope_match:
        return scope_match.group(1).replace('\n', ' ').strip()
    paragraphs = re.split(r'\n\n+', c)
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith("#") and not p.startswith("-") and not p.startswith("[") and not p.startswith(">"):
            s = p.replace('\n', ' ')
            if '. ' in s:
                return s.split('. ')[0] + '.'
            return s[:100] + "..." if len(s) > 100 else s
    return "Stub page."

all_files = list(wiki_dir.rglob("*.md"))
all_files = [f for f in all_files if "raw_sources" not in f.parts and ".system_generated" not in f.parts and "scratch" not in f.parts]

# Exclude operational files
exclude = {"log.md", "index.md", "llm-wiki.md", "snippets.md"}

sections = {
    "Appendix": [],
    "Colors": [],
    "Eye": [],
    "Gamuts": [],
    "Intersections": [],
    "Light": [],
    "Movements & Painters": [],
    "Painting": [],
    "Pigments": []
}

lead_ins = {}
home_line = ""

for f in all_files:
    if f.name in exclude:
        continue
        
    rel_path = f.relative_to(wiki_dir)
    link = str(rel_path).replace("\\", "/").replace(".md", "")
    name = f.stem
    summary = get_summary(f)
    
    line = f"- [[{link}|{name}]]: {summary}"
    
    if len(rel_path.parts) > 1:
        parent = rel_path.parts[0]
        if parent in sections:
            sections[parent].append(line)
    else:
        # Top-level files
        if name == "Home":
            home_line = f"[[{link}|{name}]]: {summary}\n"
        elif name in sections:
            # It's a section lead-in (e.g. Colors.md, Eye.md)
            lead_ins[name] = f"**[[{link}|{name}]]**: {summary}\n"

index_content = "# Wiki Index\n\n"
if home_line:
    index_content += home_line + "\n"

for section in sorted(sections.keys()):
    if sections[section] or section in lead_ins:
        index_content += f"## {section}\n"
        if section in lead_ins:
            index_content += lead_ins[section] + "\n"
        for line in sorted(sections[section]):
            index_content += f"{line}\n"
        index_content += "\n"

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)
    
print("index.md cleaned up successfully.")
