import codecs
import re

def swap_animations_back():
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # 1. Remove hero-bg canvas completely
    html = re.sub(r'<canvas id="hero-bg"[^>]*></canvas>\s*', '', html)

    # 2. Extract founder-bg from the founder card and remove it
    html = re.sub(r'<canvas id="founder-bg"[^>]*></canvas>\s*', '', html)

    # 3. Inject founder-bg right after <main> as a fixed background
    main_tag = r'(<main class="[^"]*relative[^"]*">)'
    new_founder_canvas = '\n<canvas id="founder-bg" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0" style="opacity: 0.5;"></canvas>\n'
    html = re.sub(main_tag, r'\1' + new_founder_canvas, html, count=1)

    # 4. Make sure <main> is white so the matrix text shows up clearly
    html = html.replace('bg-transparent', 'bg-white')
    
    # 5. Make sure the sections are transparent so the canvas shows through
    # We want `<section class="w-full border-b border-[#1e1e1e] py-16 bg-transparent relative z-10">`
    sections = re.findall(r'<section[^>]*>', html)
    for s in sections:
        new_s = s.replace('bg-white', 'bg-transparent')
        if 'bg-transparent' not in new_s:
            new_s = new_s.replace('class="', 'class="bg-transparent ')
        html = html.replace(s, new_s)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
        
    print("Set hex matrix as full page background.")

if __name__ == '__main__':
    swap_animations_back()
