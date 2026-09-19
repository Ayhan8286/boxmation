import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update top nav
    old_link = '<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" href="/#transparent-offer">'
    if old_link not in html:
        old_link = '<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" href="#transparent-offer">'
    
    new_link = '<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" href="founder.html">The Founder</a>'
    
    if new_link not in html:
        html = html.replace(old_link, new_link + old_link)
        
    # 2. Update footer nav
    old_footer_link = '<a class="hover:text-on-surface transition-colors" href="/#transparent-offer">'
    if old_footer_link not in html:
        old_footer_link = '<a class="hover:text-on-surface transition-colors" href="#transparent-offer">'
    
    new_footer_link = '<a class="hover:text-on-surface transition-colors" href="founder.html">The Founder</a>'
    
    if new_footer_link not in html:
        html = html.replace(old_footer_link, new_footer_link + old_footer_link)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Updated navs.")
