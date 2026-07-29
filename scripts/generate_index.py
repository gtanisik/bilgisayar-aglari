#!/usr/bin/env python3
import os
import re
import glob
import shutil

DIST_DIR = "dist"
INDEX_FILE = os.path.join(DIST_DIR, "index.html")

MODULE_TITLES = {
    "mod01-introduction": "Modül 1: Giriş, Ders Özeti ve Katmanlı Mimari",
    "mod02-applications": "Modül 2: Ağ Programlama ve Uygulama Katmanı",
    "mod03-physical-layer": "Modül 3: Veri İletişimi ve Fiziksel Katman",
    "mod04-datalink-layer": "Modül 4: Veri Bağı Katmanı ve LAN",
    "mod05-internetworking": "Modül 5: İnternet Çalışması (IP, TCP, UDP)",
    "mod06-other-topics": "Modül 6: Ağ Güvenliği ve Yönetimi",
    "mod07-emerging-tech": "Modül 7: Gelişen Teknolojiler",
}

def copy_assets():
    slides_dir = "slides"
    if not os.path.exists(slides_dir):
        return
    for root, dirs, files in os.walk(slides_dir):
        rel_path = os.path.relpath(root, slides_dir)
        target_dir = os.path.join(DIST_DIR, rel_path) if rel_path != "." else DIST_DIR
        for f in files:
            if not f.endswith(".md") and not f.startswith("."):
                os.makedirs(target_dir, exist_ok=True)
                src_file = os.path.join(root, f)
                dst_file = os.path.join(target_dir, f)
                shutil.copy2(src_file, dst_file)
                print(f"Copied asset: {src_file} -> {dst_file}")

def get_slide_info(html_path):
    rel_path = os.path.relpath(html_path, DIST_DIR)
    dir_name = os.path.dirname(rel_path)
    file_name = os.path.basename(rel_path)
    
    title = None
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read(5000)
            m = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE | re.DOTALL)
            if m:
                title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
            else:
                m_title = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
                if m_title:
                    title = m_title.group(1).strip()
    except Exception:
        pass

    if not title:
        title = file_name.replace(".html", "").replace("_", " ").title()

    module_name = MODULE_TITLES.get(dir_name, dir_name.replace("-", " ").title())
    return {
        "rel_path": rel_path,
        "dir_name": dir_name,
        "file_name": file_name,
        "title": title,
        "module_name": module_name
    }

def main():
    os.makedirs(DIST_DIR, exist_ok=True)
    copy_assets()

    html_files = glob.glob(os.path.join(DIST_DIR, "**", "*.html"), recursive=True)
    slides = []
    for f in sorted(html_files):
        if os.path.basename(f) == "index.html":
            continue
        slides.append(get_slide_info(f))

    modules = {}
    for slide in slides:
        mod = slide["module_name"]
        if mod not in modules:
            modules[mod] = []
        modules[mod].append(slide)

    cards_html = ""
    if not modules:
        cards_html = "<div class='empty'>Henüz derlenmiş slayt bulunmuyor.</div>"
    else:
        for mod_name, mod_slides in modules.items():
            cards_html += f"<div class='module-card'><h2>{mod_name}</h2><ul>"
            for slide in mod_slides:
                cards_html += f"<li><a href='{slide['rel_path']}'><span>📄 {slide['title']}</span> <span class='badge'>HTML Sunum</span></a></li>"
            cards_html += "</ul></div>"

    html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bilgisayar Ağları ve İnternet - Ders Slaytları</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-color: #0b0f19;
      --card-bg: #151c2c;
      --card-border: #232d42;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --badge-bg: #1e293b;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      min-height: 100vh;
      padding: 40px 20px;
    }}
    .container {{
      max-width: 900px;
      margin: 0 auto;
    }}
    header {{
      text-align: center;
      margin-bottom: 40px;
    }}
    header h1 {{
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 12px;
      letter-spacing: -0.02em;
    }}
    header p {{
      color: var(--text-muted);
      font-size: 1.1rem;
    }}
    .module-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }}
    .module-card h2 {{
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 16px;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 10px;
    }}
    .module-card ul {{
      list-style: none;
    }}
    .module-card li {{
      margin-bottom: 10px;
    }}
    .module-card li:last-child {{
      margin-bottom: 0;
    }}
    .module-card a {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 16px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid transparent;
      border-radius: 8px;
      color: var(--text-main);
      text-decoration: none;
      font-weight: 500;
      transition: all 0.2s ease;
    }}
    .module-card a:hover {{
      background: rgba(56, 189, 248, 0.08);
      border-color: var(--accent);
      transform: translateY(-1px);
    }}
    .badge {{
      font-size: 0.75rem;
      padding: 4px 8px;
      background: var(--badge-bg);
      color: var(--accent);
      border-radius: 6px;
      border: 1px solid var(--card-border);
    }}
    footer {{
      text-align: center;
      margin-top: 50px;
      color: var(--text-muted);
      font-size: 0.9rem;
      border-top: 1px solid var(--card-border);
      padding-top: 20px;
    }}
    footer a {{
      color: var(--accent);
      text-decoration: none;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🌐 Bilgisayar Ağları ve İnternet</h1>
      <p>Prof. Douglas E. Comer - Türkçe Ders Slaytları Portalı</p>
    </header>

    <main>
      {cards_html}
    </main>

    <footer>
      <p>Açık kaynak Türkçe slayt deponuza <a href="https://github.com/gtanisik/bilgisayar-aglari" target="_blank">GitHub Deposu</a> üzerinden ulaşabilirsiniz.</p>
    </footer>
  </div>
</body>
</html>
"""

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Index created successfully at {INDEX_FILE}")

if __name__ == "__main__":
    main()
