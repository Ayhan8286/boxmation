import codecs
from bs4 import BeautifulSoup

def revert_footers():
    for page in ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']:
        try:
            with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
                html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            footer = soup.find('footer')
            if footer:
                # Put the original classes back exactly as they were
                footer['class'] = ['w-full', 'bg-white', 'py-20', 'border-t', 'border-[#1e1e1e]', 'reveal', 'brutalist-border', 'brutalist-button']
            
            with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
                f.write(str(soup))
            print(f"Reverted footer on {page}")
        except Exception as e:
            print(f"Error on {page}: {e}")

if __name__ == '__main__':
    revert_footers()
