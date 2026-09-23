import codecs
from bs4 import BeautifulSoup

def remove_guarantee_links():
    files = ['d:/boxmation/index.html', 'd:/boxmation/pricing.html', 'd:/boxmation/booking.html', 'd:/boxmation/founder.html', 'd:/boxmation/terms.html']
    
    for filepath in files:
        try:
            with codecs.open(filepath, 'r', 'utf-8') as f:
                html = f.read()
        except FileNotFoundError:
            continue

        soup = BeautifulSoup(html, 'html.parser')

        # Find all <a> tags linking to guarantee and remove them
        for a in soup.find_all('a', href=lambda h: h and 'guarantee' in h.lower()):
            print(f"Removing in {filepath}: {a}")
            a.decompose()

        with codecs.open(filepath, 'w', 'utf-8') as f:
            f.write(str(soup))
    
    print("Done removing Guarantee links!")

if __name__ == '__main__':
    remove_guarantee_links()
