import codecs
import re

def fix_css():
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()

        bad_css = r'/\* Put a white background on sections so grid is only visible in gaps or specific areas \*/\s*section, header, footer, \.bg-transparent \{\s*background-color: var\(--ts-white\);\s*\}'
        
        # Replace the bad css
        html = re.sub(bad_css, '', html)

        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    print("Deleted the cursed inline CSS rule!")

if __name__ == '__main__':
    fix_css()
