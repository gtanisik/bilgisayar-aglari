import re
import json
import urllib.request
import urllib.parse
import os
import time

def translate(text):
    if not text.strip():
        return text
    
    # Split text if it's too long, but for a single slide it should be fine
    try:
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=tr&dt=t&q=" + urllib.parse.quote(text)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        res = "".join(i[0] for i in data[0] if i[0])
        return res
    except Exception as e:
        print(f"Translation failed for '{text[:30]}': {e}")
        time.sleep(1)
        return text # fallback

def format_slide(title_en, content_en, title_tr, content_tr):
    # Apply terms mapping
    terms = {
        r'\bbant genişliği\b': 'bant genişliği (bandwidth)',
        r'\bgecikme\b': 'gecikme (latency/delay)',
        r'\baktarım hızı\b': 'aktarım hızı (throughput)',
        r'\bseğirme\b': 'seğirme (jitter)',
        r'\byönlendirici\b': 'yönlendirici (router)',
        r'\banahtar\b': 'anahtar (switch)',
        r'\bkuyruk\b': 'kuyruk (queue)',
        r'\btıkanıklık\b': 'tıkanıklık (congestion)'
    }
    
    for k, v in terms.items():
        # Simple string replace for now since regex can be tricky with cases
        pass # Better to do simple replace
    
    # Simple replacement dictionary (case-insensitive simulation)
    replacements = {
        "bant genişliği": "bant genişliği (bandwidth)",
        "gecikme": "gecikme (delay/latency)",
        "aktarım hızı": "aktarım hızı (throughput)",
        "seğirme": "seğirme (jitter)",
        "yönlendirici": "yönlendirici (router)",
        "anahtarlam": "anahtarlama (switching)",
        "tıkanıklık": "tıkanıklık (congestion)",
        "kuyruğa alma": "kuyruğa alma (queuing)"
    }
    
    for k, v in replacements.items():
        content_tr = re.sub(rf'(?i)\b{k}\b', v, content_tr)
        
    # Fix bullets
    content_tr = re.sub(r'(?m)^d\s+', '- ', content_tr)
    content_tr = re.sub(r'(?m)^–\s+', '  - ', content_tr)
    
    # Heuristic for visuals: if mostly no bullets and just short words
    if '- ' not in content_tr and '  - ' not in content_tr and len(content_tr.split('\n')) > 3:
        if not re.search(r'\b(is|are|the|a|an)\b', content_en, re.IGNORECASE):
            content_tr += "\n\n> 📷 *[Görsel: Diyagram/Grafik — yakında eklenecek]*"
            
    slide_md = f"## {title_tr}\n\n{content_tr}\n"
    return slide_md

# Read original text
with open('/Users/gokhan/ws/ufuk/networks/ai/pdf_text/mod06_text.txt') as f:
    text = f.read()

pages = re.split(r'--- PDF PAGE \d+ ---', text)[1:]

slides = []
for p in pages:
    lines = [line.strip() for line in p.strip().split('\n')]
    if not lines: continue
    title = lines[0]
    
    content_lines = []
    for line in lines[1:]:
        if 'Computer Networks and Internets' in line or 'Copyright' in line or 'Spring, 2014' in line or re.match(r'^\d+$', line):
            continue
        if line.strip():
            content_lines.append(line)
            
    content = '\n'.join(content_lines)
    slides.append({'title': title, 'content': content})

# Deduplicate build-up slides
dedup_slides = []
for i in range(len(slides)):
    if i < len(slides) - 1 and slides[i]['title'] == slides[i+1]['title']:
        continue
    dedup_slides.append(slides[i])

# Generate Marp output
out_lines = []
out_lines.append("""---
marp: true
theme: custom-theme
paginate: true
header: 'Bilgisayar Ağları ve İnternet | Modül 6: Diğer Konular'
footer: 'Adapted from D. E. Comer (Prentice-Hall)'
---

<!-- _class: lead -->
# Modül 6: Ağ Güvenliği, Yönetim ve Diğer Konular

**Prof. Douglas E. Comer** ders materyalinden uyarlanmıştır.
""")

os.makedirs('/Users/gokhan/ws/ufuk/networks/slides/mod06-other-topics', exist_ok=True)

print(f"Total deduplicated slides: {len(dedup_slides)}")
for i, s in enumerate(dedup_slides):
    out_lines.append("\n---\n")
    if i % 10 == 0:
        print(f"Processing slide {i}...")
        
    title_en = s['title']
    content_en = s['content']
    
    # Translate
    # Re-structure bullets before translation so they translate cleanly
    clean_en = content_en
    # Keep bullets as d and - for translation, or replace with standard -, then translate
    clean_en = re.sub(r'(?m)^d\s+', '- ', clean_en)
    clean_en = re.sub(r'(?m)^–\s+', '  * ', clean_en)
    
    title_tr = translate(title_en)
    content_tr = translate(clean_en)
    
    # Make sure titles that shouldn't have english terms don't, but technical ones do
    # "Motivasyon", "Özet", "Soru", "Terminoloji", "Değerlendirme", "Örnekler"
    if title_tr.lower() not in ['motivasyon', 'özet', 'soru', 'terminoloji', 'değerlendirme', 'örnekler', 'konular']:
        # If the title has technical abbreviations like QoS, etc.
        pass # Already handled by translator generally leaving acronyms intact
        
    slide_md = format_slide(title_en, content_en, title_tr, content_tr)
    # clean up the bullets if google translate messed them up
    slide_md = slide_md.replace('- ', '- ')
    slide_md = slide_md.replace('* ', '- ')
    
    out_lines.append(slide_md)

with open('/Users/gokhan/ws/ufuk/networks/slides/mod06-other-topics/mod06_diger_konular.md', 'w') as f:
    f.write('\n'.join(out_lines))

print(f"Done! Wrote {len(dedup_slides)+1} slides.")
