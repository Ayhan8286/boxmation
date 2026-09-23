import codecs
from bs4 import BeautifulSoup
import re

def update_container_colors():
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # The colors requested for the text containers
    container_colors = [
        'bg-white',
        'bg-gray-100',
        'bg-emerald-100',
        'bg-[var(--ts-pink)]',
        'bg-orange-200',
        'bg-white'
    ]

    # Find all the sections that wrap the sys.log.write cards
    sections = soup.find_all('section', class_=lambda c: c and 'py-16' in c)

    for i, section in enumerate(sections):
        # 1. Change section background to white
        s_classes = section.get('class', [])
        # Remove any bg- color
        s_classes = [c for c in s_classes if not c.startswith('bg-')]
        s_classes.append('bg-white')
        section['class'] = s_classes

        # 2. Change the inner typewriter card background
        card = section.find('div', class_=lambda c: c and 'brutalist-border' in c and 'reveal' in c and 'p-6' in c)
        if card:
            c_classes = card.get('class', [])
            c_classes = [c for c in c_classes if not c.startswith('bg-') or c == 'bg-[#1e1e1e]'] # bg-[#1e1e1e] is for the little header tab, wait! The tab is inside the card.
            
            # actually we can just strip the background class of the card itself
            # The card has classes like bg-[#fafafa], bg-white etc.
            c_classes = [c for c in c_classes if c not in ['bg-[#fafafa]', 'bg-white', 'bg-gray-100', 'bg-emerald-100', 'bg-[var(--ts-pink)]', 'bg-orange-200']]
            c_classes.append(container_colors[i % len(container_colors)])
            card['class'] = c_classes

    # Write back
    # Since bs4 can sometimes mess up formatting, let's just write str(soup)
    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(str(soup))
        
    print("Updated colors.")

if __name__ == '__main__':
    update_container_colors()
