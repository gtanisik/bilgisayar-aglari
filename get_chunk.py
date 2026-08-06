import json
with open('slides.json') as f:
    slides = json.load(f)
for i, s in enumerate(slides[:30]):
    print(f"Slide {i+1}: {s['title']}")
    print(s['content'])
    print("-" * 20)
