import os
import re
from pathlib import Path

wiki_dir = Path(r"d:\_PROJECTS\My\ai\Light and Color Wiki")

all_files = list(wiki_dir.rglob("*.md"))
# Exclude raw sources and .system_generated
all_files = [f for f in all_files if "raw_sources" not in f.parts and ".system_generated" not in f.parts and "scratch" not in f.parts]

file_paths = {f.name: f for f in all_files}
file_contents = {}

for f in all_files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            file_contents[f.name] = file.read()
    except Exception as e:
        print(f"Failed to read {f}: {e}")

# Check Part 1: Top-level page status
target_pages = [
    "Light.md", "Eye.md", "Colors.md", "Painting.md",
    "History & Key Figures.md", "Data & Methodology.md", "Project Notes.md"
]

print("--- PART 1: Top-Level Page Status ---")
for tp in target_pages:
    if tp in file_contents:
        content = file_contents[tp]
        # Heuristic for stub: less than 200 chars or missing "## Synthesized Content"
        if "## Synthesized Content" not in content and len(content) < 300:
            print(f"[STUB] {tp}: (length: {len(content)} chars)")
        else:
            print(f"[POPULATED] {tp}: (length: {len(content)} chars)")
    else:
        print(f"[MISSING] {tp}")

print("\n--- PART 2: Lint Pass ---")

# 1 & 2. Orphan pages & Broken links
print("\n# Broken Links:")
all_links = {} # Target -> List of sources
for fname, content in file_contents.items():
    # Find [[Link]] or [[Link|Text]] or [[Link#Section|Text]] or [[Link|Text]]
    links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]', content)
    for link in links:
        link = link.strip()
        if link.lower().startswith("raw_sources"):
            continue
        # Link might have .md extension or not
        target_fname = link if link.endswith(".md") else link + ".md"
        # Sometimes links contain the folder, e.g., Intersections/File.md
        target_basename = os.path.basename(target_fname)
        
        if target_basename not in all_links:
            all_links[target_basename] = []
        all_links[target_basename].append(fname)
        
        if target_basename not in file_paths:
            print(f"- '{link}' in {fname} is BROKEN (File not found).")

print("\n# Orphan Pages:")
orphans = []
for fname in file_contents:
    if fname not in all_links and fname not in ["index.md", "log.md", "llm-wiki.md", "task.md", "walkthrough.md", "implementation_plan.md"]:
        orphans.append(fname)
for o in orphans:
    print(f"- {o}")

print("\n# Stale or Thin Content:")
for fname, content in file_contents.items():
    if fname in ["index.md", "log.md", "llm-wiki.md", "task.md", "walkthrough.md", "implementation_plan.md", "Bibliography.md", "Project Notes.md"]:
        continue
    # Count words
    words = len(re.findall(r'\w+', content))
    if words < 150: # Very thin
        print(f"- {fname} ({words} words)")

print("\n# Index Check:")
index_content = file_contents.get("index.md", "")
index_links = re.findall(r'\[\[(.*?)\]\]', index_content)
print(f"- index.md has {len(index_links)} links.")
# Check for one-line summaries: Does it have text after the links?
lines_with_links = [l for l in index_content.splitlines() if "[[" in l]
has_summaries = any(len(l.split("]]")) > 1 and len(l.split("]]")[1].strip()) > 5 for l in lines_with_links)
print(f"- index.md has 1-line summaries: {has_summaries}")

