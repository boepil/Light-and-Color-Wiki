import urllib.request
import re
from bs4 import BeautifulSoup
import os

wiki_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki"

def html_to_md(html):
    soup = BeautifulSoup(html, 'html.parser')
    for s in soup(['script', 'style']):
        s.extract()
    text = soup.get_text(separator='\n')
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

# 1. Add gamut comparison from color13.md to Colors/Gamuts/Gamuts.md
with open(os.path.join(wiki_dir, "raw_sources", "handprint", "color13.md"), "r", encoding="utf-8") as f:
    color13 = f.read()

# Extract from "more is less? a gamut comparison" to the end of the section
match = re.search(r"(more is less\? a gamut comparison.*?)(\n\n[a-z ]+\n\n|the 18th century)", color13, re.DOTALL | re.IGNORECASE)
if match:
    gamut_text = match.group(1).strip()
    # It might be cut off, let's do a simpler extraction by index
    idx = color13.find("more is less? a gamut comparison")
    if idx != -1:
        end_idx = color13.find("the artist's value wheel", idx) # just an arbitrary next section if any
        if end_idx == -1: end_idx = idx + 4000 # just grab 4000 chars
        gamut_text = color13[idx:end_idx].strip()
        
        target = os.path.join(wiki_dir, "Colors", "Gamuts", "Gamuts.md")
        with open(target, "a", encoding="utf-8") as f:
            f.write("\n\n## Handprint: Gamut Comparison\n\n" + gamut_text)

# 2. Fetch specific pigment pages to get numeric data for PG7, PB15:3, PR122, PV23, PV19
pigments_to_find = ["PG7", "PB15:3", "PR122", "PV23", "PV19"]
urls_to_check = [
    "watery.html", "watero.html", "waterr.html", "waterm.html", 
    "waterv.html", "waterb.html", "waterg.html", "watere.html", "waterw.html"
]
base_url = "https://handprint.com/HP/WCL/"

found_data = []

for page in urls_to_check:
    url = base_url + page
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        md = html_to_md(html)
        
        for pig in pigments_to_find:
            if pig in md:
                # Find paragraphs mentioning the pigment
                paragraphs = md.split("\n\n")
                for i, p in enumerate(paragraphs):
                    if pig in p:
                        found_data.append(f"### {pig} from {page}\n" + p)
                        if i+1 < len(paragraphs):
                            found_data.append(paragraphs[i+1])
    except Exception as e:
        print(f"Failed {page}: {e}")

if found_data:
    target2 = os.path.join(wiki_dir, "Painting", "Pigments", "Sourcing Real Spectral Data.md")
    with open(target2, "a", encoding="utf-8") as f:
        f.write("\n\n## Handprint: Real Spectral & Pigment Data\n\n" + "\n\n".join(found_data))

print("Extraction script finished.")
