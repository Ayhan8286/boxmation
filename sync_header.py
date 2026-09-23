import codecs
from bs4 import BeautifulSoup

def sync_header_footer():
    # Get the latest header and footer from index.html
    with codecs.open('d:/boxmation/index.html', 'r', 'utf-8') as f:
        index_html = f.read()
    index_soup = BeautifulSoup(index_html, 'html.parser')
    latest_header = index_soup.find('header')
    latest_footer = index_soup.find('footer')

    # Apply to terms.html
    with codecs.open('d:/boxmation/terms.html', 'r', 'utf-8') as f:
        terms_html = f.read()
    terms_soup = BeautifulSoup(terms_html, 'html.parser')

    old_header = terms_soup.find('header')
    if old_header and latest_header:
        old_header.replace_with(latest_header.__copy__())

    old_footer = terms_soup.find('footer')
    if old_footer and latest_footer:
        old_footer.replace_with(latest_footer.__copy__())

    with codecs.open('d:/boxmation/terms.html', 'w', 'utf-8') as f:
        f.write(str(terms_soup))

    print("Synced header and footer on terms.html!")

if __name__ == '__main__':
    sync_header_footer()
