import codecs
from bs4 import BeautifulSoup

def fix_card():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Ensure section is transparent
    section = soup.find('section')
    if section:
        classes = section.get('class', [])
        if 'bg-white' in classes:
            classes.remove('bg-white')
        if 'bg-transparent' not in classes:
            classes.append('bg-transparent')
        section['class'] = classes

    # 2. Make the card (max-w-6xl) bg-white
    card = soup.find('div', class_=lambda c: c and 'max-w-6xl' in c)
    if card:
        classes = card.get('class', [])
        if 'bg-white' not in classes:
            classes.append('bg-white')
        card['class'] = classes
        
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
        
    print("Fixed card background!")

if __name__ == '__main__':
    fix_card()
