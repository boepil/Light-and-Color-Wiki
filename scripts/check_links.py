import os
import re
from pathlib import Path

wiki_dir = Path(r"d:\_PROJECTS\My\ai\Light and Color Wiki")

all_files = list(wiki_dir.rglob("*.md"))
all_files = [f for f in all_files if "raw_sources" not in f.parts and ".system_generated" not in f.parts and "scratch" not in f.parts]

file_paths = {f.name: f for f in all_files}

for f in all_files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]', content)
            for link in links:
                link = link.strip()
                if link.lower().startswith("raw_sources"):
                    continue
                target_fname = link if link.endswith(".md") else link + ".md"
                target_basename = os.path.basename(target_fname)
                if target_basename not in file_paths:
                    print(f"BROKEN LINK: '{link}' in {f.name}")
    except Exception as e:
        pass
