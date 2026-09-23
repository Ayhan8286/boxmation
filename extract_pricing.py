import os
import re

def main():
    with open('d:/boxmation/index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    # Find the transparent-offer section
    # The section starts with <section ... id="transparent-offer"> and ends with </section>
    match = re.search(r'(<!-- 4\. LOCKED OFFER & TRANSPARENT PRICING -->\s*<section[^>]*id="transparent-offer".*?</section>)', index_html, flags=re.DOTALL)
    
    if not match:
        print("Could not find the transparent-offer section.")
        return
        
    pricing_section = match.group(1)
    
    # Remove it from index.html
    new_index_html = index_html.replace(pricing_section, '')
    
    # Update navigation links in index.html
    new_index_html = new_index_html.replace('href="/#transparent-offer"', 'href="/pricing.html"')
    new_index_html = new_index_html.replace('href="#transparent-offer"', 'href="/pricing.html"')
    
    with open('d:/boxmation/index.html', 'w', encoding='utf-8') as f:
        f.write(new_index_html)
        
    # Update founder.html links
    with open('d:/boxmation/founder.html', 'r', encoding='utf-8') as f:
        founder_html = f.read()
    founder_html = founder_html.replace('href="/#transparent-offer"', 'href="/pricing.html"')
    founder_html = founder_html.replace('href="#transparent-offer"', 'href="/pricing.html"')
    with open('d:/boxmation/founder.html', 'w', encoding='utf-8') as f:
        f.write(founder_html)
        
    # Create pricing.html using founder.html as a template
    # We replace the <main> contents with the pricing section.
    # We find the <main> tag and replace its contents.
    match_main = re.search(r'(<main[^>]*>).*?(</main>)', founder_html, flags=re.DOTALL)
    if match_main:
        # In founder.html, there is a founder section. We replace the inner HTML of main.
        # But wait, founder.html has a hero section? No, it has its own content.
        # We can just inject pricing_section inside <main>
        # Add some padding to top since we are on a new page.
        pricing_page_content = f"{match_main.group(1)}\n{pricing_section}\n{match_main.group(2)}"
        pricing_html = founder_html[:match_main.start()] + pricing_page_content + founder_html[match_main.end():]
        
        # Change title
        pricing_html = pricing_html.replace('<title>BoxMation - Founder</title>', '<title>BoxMation - Pricing & Offer</title>')
        
        with open('d:/boxmation/pricing.html', 'w', encoding='utf-8') as f:
            f.write(pricing_html)
        print("Successfully created pricing.html and updated links.")
    else:
        print("Could not find <main> in founder.html")

if __name__ == '__main__':
    main()
