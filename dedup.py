import codecs
import re

def deduplicate():
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    # The string we want to keep
    keep_canvas = '<canvas id="founder-bg" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0" style="opacity: 1;"></canvas>'
    
    # Let's count how many founder-bg canvases exist
    matches = re.findall(r'<canvas[^>]*id="founder-bg"[^>]*></canvas>', html)
    print("Found canvases:", len(matches))
    
    if len(matches) > 1:
        # Replace the first one with the proper one, and remove the others
        html = re.sub(r'<canvas[^>]*id="founder-bg"[^>]*></canvas>\s*', '', html)
        # Re-inject just one properly
        main_tag = r'(<main class="[^"]*relative[^"]*">)'
        html = re.sub(main_tag, r'\1\n' + keep_canvas + '\n', html, count=1)
        
    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    deduplicate()
