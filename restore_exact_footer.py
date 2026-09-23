import codecs
from bs4 import BeautifulSoup

def restore_exact_footer():
    # Get exact footer from index.html
    with codecs.open('d:/boxmation/index.html', 'r', 'utf-8') as f:
        index_html = f.read()
    index_soup = BeautifulSoup(index_html, 'html.parser')
    index_footer = index_soup.find('footer')

    # Put it in terms.html
    with codecs.open('d:/boxmation/terms.html', 'r', 'utf-8') as f:
        terms_html = f.read()
    terms_soup = BeautifulSoup(terms_html, 'html.parser')
    
    current_footer = terms_soup.find('footer')
    if current_footer and index_footer:
        current_footer.replace_with(BeautifulSoup(str(index_footer), 'html.parser').find('footer'))

    with codecs.open('d:/boxmation/terms.html', 'w', 'utf-8') as f:
        f.write(str(terms_soup))
    
    print("Restored exact index footer to terms.html")

if __name__ == '__main__':
    restore_exact_footer()
