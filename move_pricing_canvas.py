import codecs
import re

def move_canvas():
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()

        # Remove the fixed canvas from the top
        canvas_tag = r'<canvas id="pricing-bg"[^>]*></canvas>\n?'
        html = re.sub(canvas_tag, '', html)

        # Inject it into <main> as an absolute background
        main_tag = r'(<main class="[^"]*relative[^"]*">)'
        new_canvas = '\n<canvas id="pricing-bg" class="absolute inset-0 w-full h-full pointer-events-none z-[-1]" style="opacity: 1;"></canvas>\n'
        
        if 'id="pricing-bg"' not in html:
            html = re.sub(main_tag, r'\1' + new_canvas, html, count=1)

        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    print('Moved canvas into main')

if __name__ == '__main__':
    move_canvas()
