import codecs
from bs4 import BeautifulSoup

def fix_terms_head_body():
    with codecs.open('d:/boxmation/terms.html', 'r', 'utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    # Remove the old tailwind config script
    for s in soup.find_all('script'):
        if s.string and 'tailwind.config' in s.string:
            s.decompose()

    # Update body class
    body = soup.find('body')
    if body:
        body['class'] = ['antialiased']

    with codecs.open('d:/boxmation/terms.html', 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Fixed terms.html head and body!")

if __name__ == '__main__':
    fix_terms_head_body()
