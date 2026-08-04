import os
import urllib.request
from bs4 import BeautifulSoup
import re

base_url = "https://handprint.com/HP/WCL/"
urls = [
    # Color Theory
    "color18a.html", "color18b.html", "intstud.html", "color11.html", 
    "color12.html", "color13.html", "color14.html", "mix.html", 
    "color16.html", "mixtable.html", "tech13.html",
    
    # Paints & Pigments
    "pigmt0.html", "pigmt1.html", "pigmt3.html", "pigmt9.html", 
    "pigmt6.html", "pigmt2.html", "waterfs.html", "pigmt8.html", 
    "palette1.html", "litetest.html", "pigmt5.html", "pigmt7.html", "pigmt4.html"
]

out_dir = r"d:\_PROJECTS\My\ai\Light and Color Wiki\raw_sources\handprint"
os.makedirs(out_dir, exist_ok=True)

def html_to_md(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove scripts, styles
    for s in soup(['script', 'style']):
        s.extract()
        
    text = soup.get_text(separator='\n')
    # Collapse multiple newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

for page in urls:
    url = base_url + page
    out_path = os.path.join(out_dir, page.replace(".html", ".md"))
    
    if os.path.exists(out_path):
        print(f"Skipping {page}, already exists.")
        continue
        
    print(f"Fetching {page}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        md = html_to_md(html)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
    except Exception as e:
        print(f"Failed to fetch {page}: {e}")

print("Scraping complete.")
