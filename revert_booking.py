import codecs
from bs4 import BeautifulSoup

def revert_canvas():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the canvas
    canvas = soup.find('canvas', id='booking-bg')
    if canvas:
        canvas.decompose()
        
    # Find the card and remove the classes we added
    card = soup.find('div', class_=lambda c: c and 'max-w-6xl' in c)
    if card:
        classes = card.get('class', [])
        if 'bg-white' in classes:
            classes.remove('bg-white')
        if 'relative' in classes:
            classes.remove('relative')
        if 'overflow-hidden' in classes:
            classes.remove('overflow-hidden')
        card['class'] = classes
        
        # Remove relative z-10 from the first child
        first_child = card.find('div', recursive=False)
        if first_child:
            child_classes = first_child.get('class', [])
            if 'relative' in child_classes:
                child_classes.remove('relative')
            if 'z-10' in child_classes:
                child_classes.remove('z-10')
            first_child['class'] = child_classes

    # Inject the canvas back outside the section, into main
    main = soup.find('main')
    if main:
        new_canvas = soup.new_tag('canvas', id='booking-bg', style='opacity: 1;')
        new_canvas['class'] = ['fixed', 'top-0', 'left-0', 'w-full', 'h-full', 'pointer-events-none', 'z-0']
        main.insert(0, new_canvas)
        
    # Format HTML to string without adding closing tags where they shouldn't be
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
        
    print("Reverted canvas to fixed background.")

if __name__ == '__main__':
    revert_canvas()
