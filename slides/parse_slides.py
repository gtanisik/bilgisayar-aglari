import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    pages = re.split(r'--- PDF PAGE \d+ ---', content)
    
    cleaned_pages = []
    
    for page in pages:
        if not page.strip(): continue
        
        # Clean up footers
        lines = page.strip().split('\n')
        # Remove footers like:
        # Computer Networks and Internets -- Module 4
        # 32
        # Copyright  2014. All rights reserved.
        # Spring, 2014
        
        content_lines = []
        for line in lines:
            if 'Computer Networks and Internets -- Module' in line or \
               'Copyright' in line or \
               'Spring, 2014' in line or \
               re.match(r'^\d+$', line.strip()):
                continue
            content_lines.append(line)
        
        cleaned_pages.append('\n'.join(content_lines).strip())
        
    # Remove build up slides
    # A build up slide usually has the same title and is a prefix of the next slide
    final_pages = []
    for page in cleaned_pages:
        if not page: continue
        
        if len(final_pages) > 0:
            prev = final_pages[-1]
            title_curr = page.split('\n')[0]
            title_prev = prev.split('\n')[0]
            
            # if same title, check if prev is mostly in curr
            if title_curr == title_prev:
                # Just replace it, assuming it's a buildup
                final_pages[-1] = page
            else:
                final_pages.append(page)
        else:
            final_pages.append(page)
            
    # Write to a clean file
    with open('cleaned_slides.txt', 'w') as f:
        for i, p in enumerate(final_pages):
            f.write(f"=== SLIDE {i} ===\n{p}\n\n")
            
    print(f"Total unique slides: {len(final_pages)}")

process_file('/Users/gokhan/ws/ufuk/networks/ai/pdf_text/mod04_text.txt')
