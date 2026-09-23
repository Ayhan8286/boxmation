import codecs
from bs4 import BeautifulSoup

def add_og_tags():
    pages = ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']
    
    for page in pages:
        try:
            with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
                html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            head = soup.find('head')
            
            if head:
                # Remove existing OG tags if any
                for tag in head.find_all('meta', attrs={'property': lambda x: x and x.startswith('og:')}):
                    tag.decompose()
                for tag in head.find_all('meta', attrs={'name': lambda x: x and x.startswith('twitter:')}):
                    tag.decompose()

                # Title mappings
                titles = {
                    'index.html': 'BoxMation | Automated Outbound Systems',
                    'founder.html': 'BoxMation | The Founder',
                    'pricing.html': 'BoxMation | Pricing & Offer',
                    'booking.html': 'BoxMation | Contact',
                    'terms.html': 'BoxMation | Terms & Privacy'
                }
                page_title = titles.get(page, 'BoxMation')

                # Create new tags
                tags = f"""
    <!-- Open Graph / Social Media Meta Tags -->
    <meta property="og:title" content="{page_title}" />
    <meta property="og:description" content="Automated LinkedIn + Email Outbound Systems for B2B Founders. We build, run, and optimise your pipeline." />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://boxmation.com" />
    <meta property="og:image" content="https://boxmation.com/og-image.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{page_title}" />
    <meta name="twitter:description" content="Automated LinkedIn + Email Outbound Systems for B2B Founders." />
    <meta name="twitter:image" content="https://boxmation.com/og-image.png" />
    """
                head.append(BeautifulSoup(tags, 'html.parser'))
                
            with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
                f.write(str(soup))
            print(f"Added OG tags to {page}")
        except Exception as e:
            print(f"Error on {page}: {e}")

if __name__ == '__main__':
    add_og_tags()
