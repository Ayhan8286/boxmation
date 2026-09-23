import codecs
import re

def combine_animations():
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # 1. Inject the hero-bg canvas right after <main>
    # Make sure we don't inject it twice if it's already there
    if 'id="hero-bg"' not in html:
        main_tag = r'(<main class="[^"]*relative[^"]*">)'
        canvas_html = '\n<canvas id="hero-bg" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0" style="opacity: 0.2;"></canvas>\n'
        html = re.sub(main_tag, r'\1' + canvas_html, html, count=1)
        
    # 2. Make sections transparent and relative z-10 so they overlay the canvas but don't block it
    # Find all sections and remove bg-white, add bg-transparent relative z-10
    sections = re.findall(r'<section[^>]*>', html)
    for s in sections:
        # replace bg-white with bg-transparent relative z-10
        # If it's already bg-transparent, just ensure relative z-10 is there
        new_s = s.replace('bg-white', 'bg-transparent relative z-10')
        if 'relative' not in new_s:
            new_s = new_s.replace('bg-transparent', 'bg-transparent relative z-10')
        html = html.replace(s, new_s)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
        
    print("Combined animations successfully.")

if __name__ == '__main__':
    combine_animations()
