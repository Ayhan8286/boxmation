import codecs
from bs4 import BeautifulSoup, Tag

def sync_terms():
    # Load index as source of truth
    with codecs.open('d:/boxmation/index.html', 'r', 'utf-8') as f:
        index_html = f.read()
    index_soup = BeautifulSoup(index_html, 'html.parser')

    # Load terms
    with codecs.open('d:/boxmation/terms.html', 'r', 'utf-8') as f:
        terms_html = f.read()
    terms_soup = BeautifulSoup(terms_html, 'html.parser')

    # 1. Fix favicon
    old_icon = terms_soup.find('link', rel=lambda r: r and 'icon' in r)
    if old_icon:
        old_icon['href'] = 'new-logo.png'
        old_icon['type'] = 'image/png'
        print("Fixed favicon")

    # 2. Replace header
    old_header = terms_soup.find('header')
    new_header = index_soup.find('header')
    if old_header and new_header:
        old_header.replace_with(BeautifulSoup(str(new_header), 'html.parser').find('header'))
        print("Replaced header")

    # 3. Replace footer
    old_footer = terms_soup.find('footer')
    new_footer = index_soup.find('footer')
    if old_footer and new_footer:
        old_footer.replace_with(BeautifulSoup(str(new_footer), 'html.parser').find('footer'))
        print("Replaced footer")

    with codecs.open('d:/boxmation/terms.html', 'w', 'utf-8') as f:
        f.write(str(terms_soup))
    print("Done!")

if __name__ == '__main__':
    sync_terms()
