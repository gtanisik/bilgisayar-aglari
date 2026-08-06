import re, json

with open('/Users/gokhan/ws/ufuk/networks/ai/pdf_text/mod06_text.txt') as f:
    text = f.read()

pages = re.split(r'--- PDF PAGE \d+ ---', text)[1:]

slides = []
for p in pages:
    lines = [line.strip() for line in p.strip().split('\n')]
    if not lines: continue
    title = lines[0]
    
    # Extract content, skipping title, footer, page number, copyright
    content_lines = []
    for line in lines[1:]:
        if 'Computer Networks and Internets' in line or 'Copyright' in line or 'Spring, 2014' in line or re.match(r'^\d+$', line):
            continue
        if line.strip():
            content_lines.append(line)
            
    content = '\n'.join(content_lines)
    slides.append({'title': title, 'content': content})

# Remove build-up slides (keep the last one for each title sequence)
dedup_slides = []
for i in range(len(slides)):
    if i < len(slides) - 1 and slides[i]['title'] == slides[i+1]['title']:
        continue # skip because the next one is likely the build-up
    dedup_slides.append(slides[i])

with open('slides.json', 'w') as f:
    json.dump(dedup_slides, f, indent=2)

print(len(dedup_slides))
