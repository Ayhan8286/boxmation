import codecs
from bs4 import BeautifulSoup

def clean_footer():
    for page in ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']:
        try:
            with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
                html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            footer = soup.find('footer')
            if footer:
                classes = footer.get('class', [])
                # Remove reveal and brutalist-button
                classes = [c for c in classes if c not in ['reveal', 'brutalist-button', 'brutalist-border']]
                
                # Make sure it has bg-white, border-t, border-[#1e1e1e]
                if 'bg-white' not in classes:
                    classes.append('bg-white')
                if 'border-t' not in classes:
                    classes.append('border-t')
                
                # Replace gray border with brutalist dark border
                classes = [c for c in classes if c != 'border-gray-100']
                if 'border-[#1e1e1e]' not in classes:
                    classes.append('border-[#1e1e1e]')

                footer['class'] = classes

            with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
                f.write(str(soup))
            print(f"Cleaned footer on {page}")
        except Exception as e:
            print(f"Error on {page}: {e}")

if __name__ == '__main__':
    clean_footer()
