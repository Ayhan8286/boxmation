import codecs
import os

def update_domain():
    pages = ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']
    for page in pages:
        filepath = f'd:/boxmation/{page}'
        if os.path.exists(filepath):
            with codecs.open(filepath, 'r', 'utf-8') as f:
                html = f.read()
                
            html = html.replace('content="https://boxmation.com"', 'content="https://boxmation.vercel.app"')
            html = html.replace('content="https://boxmation.com/og-image.png"', 'content="https://boxmation.vercel.app/og-image.png"')
            
            with codecs.open(filepath, 'w', 'utf-8') as f:
                f.write(html)
            print(f'Updated {page}')

if __name__ == '__main__':
    update_domain()
