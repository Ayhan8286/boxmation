import re
import glob

# 1. Add id="contact" to the section in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_section = '<section class="w-full py-20 bg-surface-container-lowest relative">'
if target_section in html:
    html = html.replace(target_section, '<section class="w-full py-20 bg-surface-container-lowest relative" id="contact">')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added ID to section")
else:
    print("Could not find section to add ID")

# 2. Add Contact to navs
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update top nav
    old_link = '<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" href="founder.html">The Founder</a>'
    
    # Since we are on other pages, it should link to `/#contact` for external pages, and `#contact` for index.html.
    # To keep it simple, we can use `/#contact` on terms/founder and `#contact` on index, OR just `index.html#contact` for external.
    # Actually, the other anchor links (like `#transparent-offer`) are just `#...` which breaks if clicked from `founder.html`.
    # Let's fix that too while we're at it? No, let's just use `/#contact`.
    link_url = '#contact' if filepath == 'index.html' else '/#contact'
    
    new_link = f'<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" href="{link_url}">Contact</a>'
    
    if new_link not in html:
        # insert it at the end of the nav list
        # Find </nav>
        html = html.replace('</nav>', f'{new_link}</nav>')
        
    # Update footer nav
    footer_target = '<a class="hover:text-on-surface transition-colors" href="terms.html">Terms &amp; Privacy</a>'
    new_footer_link = f'<a class="hover:text-on-surface transition-colors" href="{link_url}">Contact</a>'
    
    if new_footer_link not in html:
        html = html.replace(footer_target, f'{new_footer_link}{footer_target}')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Updated navs")
