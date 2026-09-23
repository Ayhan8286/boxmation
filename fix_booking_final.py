import codecs
from bs4 import BeautifulSoup

def fix_booking():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Make the section transparent so the canvas behind it shows through
    section = soup.find('section')
    if section:
        classes = section.get('class', [])
        # Remove bg-white
        while 'bg-white' in classes:
            classes.remove('bg-white')
        section['class'] = classes

    # Keep the inner content card (max-w-6xl) as bg-white so text stays readable
    card = soup.find('div', class_=lambda c: c and 'max-w-6xl' in c)
    if card:
        classes = card.get('class', [])
        if 'bg-white' not in classes:
            classes.append('bg-white')
        card['class'] = classes

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Done!")

if __name__ == '__main__':
    fix_booking()
