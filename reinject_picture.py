import os
import re

def main():
    # 1. Read index.backup.html to get the picture frame
    with open('d:/boxmation/index.backup.html', 'r', encoding='utf-8') as f:
        index_html = f.read()
    
    match = re.search(r'(<!-- Visual Presentation Frame -->\s*<div class="lg:col-span-5 relative">.*?(?:<!-- Floating Live Card -->.*?</div\s*>\s*</div\s*>\s*</div\s*>\s*</div\s*>))', index_html, flags=re.DOTALL)
    
    if match:
        picture_html = match.group(1)
        
        # We need to brutalize the picture html manually because it came from backup!
        picture_html = picture_html.replace('rounded-2xl', '')
        picture_html = picture_html.replace('shadow-2xl', '')
        picture_html = picture_html.replace('ring-1', '')
        picture_html = picture_html.replace('ring-black/10', '')
        picture_html = picture_html.replace('rounded-lg', '')
        picture_html = picture_html.replace('shadow-lg', '')
        picture_html = picture_html.replace('border-gray-200', 'border-[#1e1e1e] brutalist-border')
        picture_html = picture_html.replace('bg-green-500', 'bg-[var(--ts-green)]')
        
        # Add B&W to img
        picture_html = re.sub(r'(<img[^>]*class=")([^"]*)(")', r'\1\2 grayscale contrast-125\3', picture_html)
        
        # 3. Read founder.html
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

        picture_html = picture_html.replace('<div class="lg:col-span-5 relative">', '<div class="max-w-md mx-auto relative mb-16">')
        
        injection_target = '<h2 class="text-xl md:text-2xl font-medium mt-6">Beyond the Systems</h2>'
        
        if injection_target in founder_html and 'Visual Presentation Frame' not in founder_html:
            new_injection = f"{picture_html}\n{injection_target}"
            founder_html = founder_html.replace(injection_target, new_injection)
        
        with open('d:/boxmation/founder.html', 'w', encoding='utf-8') as f:
            f.write(founder_html)
        print("Injected picture into founder.html")
    else:
        print("Could not find picture frame in backup")

if __name__ == '__main__':
    main()
