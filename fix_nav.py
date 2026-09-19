with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove System & Architecture links
html = html.replace('<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" data-path="system-architecture" href="#">System &amp; Architecture</a>', '')
html = html.replace('<a class="hover:text-on-surface transition-colors" data-path="system-architecture" href="#">System &amp; Architecture</a>', '')

# Update links (handles both attribute orders just in case)
html = html.replace('href="#" data-path="pricing-offer"', 'href="#transparent-offer"')
html = html.replace('data-path="pricing-offer" href="#"', 'href="#transparent-offer"')

html = html.replace('href="#" data-path="the-wedge"', 'href="#the-wedge"')
html = html.replace('data-path="the-wedge" href="#"', 'href="#the-wedge"')

html = html.replace('href="#" data-path="compare-vs-in-house"', 'href="#compare-vs-in-house"')
html = html.replace('data-path="compare-vs-in-house" href="#"', 'href="#compare-vs-in-house"')

html = html.replace('href="#" data-path="guarantee"', 'href="#guarantee"')
html = html.replace('data-path="guarantee" href="#"', 'href="#guarantee"')

html = html.replace('data-path="discovery-call" href="#"', 'href="#book-discovery"')
html = html.replace('href="#" data-path="discovery-call"', 'href="#book-discovery"')

# Add missing IDs to sections by searching for exact classes used
html = html.replace('<section class="w-full py-24 bg-surface-container-lowest relative">', '<section class="w-full py-24 bg-surface-container-lowest relative" id="compare-vs-in-house">', 1)
html = html.replace('<section class="w-full py-24 bg-background relative">', '<section class="w-full py-24 bg-background relative" id="the-wedge">', 1)
html = html.replace('<section class="w-full py-24 bg-surface-container-lowest relative">', '<section class="w-full py-24 bg-surface-container-lowest relative" id="guarantee">', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
