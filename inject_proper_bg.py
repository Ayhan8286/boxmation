import codecs
import re

def fix_booking():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # 1. Remove the canvas from anywhere else (e.g., inside <main> before <section>)
    html = re.sub(r'<canvas id="booking-bg"[^>]*></canvas>\n?', '', html)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # 2. Find the main section
    section = soup.find('section')
    if section:
        # Make sure section has relative and overflow-hidden so the absolute canvas stays inside it
        classes = section.get('class', [])
        if 'relative' not in classes:
            classes.append('relative')
        if 'overflow-hidden' not in classes:
            classes.append('overflow-hidden')
        section['class'] = classes
        
        # Make sure all direct children of section are relative z-10 EXCEPT the canvas
        for child in section.find_all(recursive=False):
            if child.name != 'canvas':
                child_classes = child.get('class', [])
                if 'relative' not in child_classes:
                    child_classes.append('relative')
                if 'z-10' not in child_classes:
                    child_classes.append('z-10')
                child['class'] = child_classes

        # Insert canvas as the first child of the section
        new_canvas = soup.new_tag('canvas', id='booking-bg', style='opacity: 1;')
        new_canvas['class'] = ['absolute', 'inset-0', 'w-full', 'h-full', 'pointer-events-none', 'z-0']
        section.insert(0, new_canvas)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
        
    print("Injected canvas inside the section!")

if __name__ == '__main__':
    fix_booking()
