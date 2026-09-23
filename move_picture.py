import os
import re
from bs4 import BeautifulSoup

def main():
    # 1. Read index.html
    with open('d:/boxmation/index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()
    
    # 2. Extract the visual presentation frame (the founder picture)
    # The frame is <div class="lg:col-span-5 relative">
    match = re.search(r'(<!-- Visual Presentation Frame -->\s*<div class="lg:col-span-5 relative">.*?(?:<!-- Floating Live Card -->.*?</div\s*>\s*</div\s*>\s*</div\s*>\s*</div\s*>))', index_html, flags=re.DOTALL)
    
    if match:
        picture_html = match.group(1)
        
        # Remove from index.html
        index_html = index_html.replace(picture_html, '')
        
        # Change the text grid from lg:col-span-7 to full width
        index_html = index_html.replace('<div class="lg:col-span-7">', '<div class="lg:col-span-12 max-w-4xl mx-auto">')
        
        # Also, the grid was grid-cols-12, let's keep it but now it's just col-span-12 so it centers.
        
        with open('d:/boxmation/index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
            
        print("Removed picture from index.html")
    else:
        print("Could not find picture frame in index.html")
        return

    # 3. Read founder.html and fix its h1
    with open('d:/boxmation/founder.html', 'r', encoding='utf-8') as f:
        founder_html = f.read()

    # Fix h1
    founder_html = re.sub(
        r'<h1 class="font-display[^>]*>.*?</h1>',
        r'''<h1 class="font-display text-5xl md:text-7xl max-w-5xl font-extrabold tracking-tighter leading-[1.1] mb-6 uppercase">
                    The <span class="bg-[var(--ts-pink)] text-[var(--ts-dark)] px-2">Founder</span><span class="cursor-blink"></span>
                </h1>''',
        founder_html,
        flags=re.DOTALL
    )

    # 4. Inject the picture_html into founder.html
    # We will put it right before the "Beyond the Systems" <h2>
    # Wait, the picture_html has <div class="lg:col-span-5 relative">. We should change it to be max-w-md mx-auto.
    picture_html = picture_html.replace('<div class="lg:col-span-5 relative">', '<div class="max-w-md mx-auto relative mb-16">')
    
    injection_target = '<h2 class="text-xl md:text-2xl font-medium mt-6">Beyond the Systems</h2>'
    new_injection = f"{picture_html}\n{injection_target}"
    
    founder_html = founder_html.replace(injection_target, new_injection)
    
    with open('d:/boxmation/founder.html', 'w', encoding='utf-8') as f:
        f.write(founder_html)
    print("Injected picture into founder.html")

if __name__ == '__main__':
    main()
