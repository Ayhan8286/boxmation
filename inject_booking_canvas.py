import codecs
from bs4 import BeautifulSoup

def inject_canvas():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove the old canvas
    old_canvas = soup.find('canvas', id='booking-bg')
    if old_canvas:
        old_canvas.decompose()
        
    # Find the main container card
    card = soup.find('div', class_=lambda c: c and 'max-w-6xl' in c)
    if card:
        # Add bg-white and relative overflow-hidden to card classes
        classes = card.get('class', [])
        if 'bg-white' not in classes:
            classes.append('bg-white')
        if 'relative' not in classes:
            classes.append('relative')
        if 'overflow-hidden' not in classes:
            classes.append('overflow-hidden')
        card['class'] = classes
        
        # Make the first child (flex flex-col gap-16) relative z-10 so it sits above canvas
        first_child = card.find('div', recursive=False)
        if first_child:
            child_classes = first_child.get('class', [])
            if 'relative' not in child_classes:
                child_classes.extend(['relative', 'z-10'])
            first_child['class'] = child_classes
            
        # Create new canvas
        new_canvas = soup.new_tag('canvas', id='booking-bg', style='opacity: 1;')
        new_canvas['class'] = ['absolute', 'inset-0', 'w-full', 'h-full', 'pointer-events-none', 'z-0']
        
        # Insert canvas as first child of card
        card.insert(0, new_canvas)
        
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
        
    print("Injected canvas into card using BS4!")

if __name__ == '__main__':
    inject_canvas()
