import codecs
import re
from bs4 import BeautifulSoup

def inject_booking_bg():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # Remove the canvas from anywhere else
    html = re.sub(r'<canvas id="booking-bg"[^>]*></canvas>\n?', '', html)

    soup = BeautifulSoup(html, 'html.parser')
    section = soup.find('section')
    if section:
        classes = section.get('class', [])
        if 'relative' not in classes:
            classes.append('relative')
        if 'overflow-hidden' not in classes:
            classes.append('overflow-hidden')
        section['class'] = classes
        
        for child in section.find_all(recursive=False):
            if child.name != 'canvas':
                child_classes = child.get('class', [])
                if 'relative' not in child_classes:
                    child_classes.append('relative')
                if 'z-10' not in child_classes:
                    child_classes.append('z-10')
                child['class'] = child_classes

        new_canvas = soup.new_tag('canvas', id='booking-bg', style='opacity: 1;')
        new_canvas['class'] = ['absolute', 'inset-0', 'w-full', 'h-full', 'pointer-events-none', 'z-0']
        section.insert(0, new_canvas)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Injected canvas into section successfully.")

if __name__ == '__main__':
    inject_booking_bg()
