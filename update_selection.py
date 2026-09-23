import os
import re

files = ['founder.html', 'pricing.html', 'booking.html', 'terms.html']
for filename in files:
    path = f'd:/boxmation/{filename}'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # The CSS block usually has something like:
    # ::selection {
    #     background-color: var(--ts-magenta);
    #     color: var(--ts-white);
    # }
    
    html = html.replace('background-color: var(--ts-magenta);', 'background-color: var(--ts-dark);')
    # Or if it was hardcoded pink:
    html = html.replace('background-color: #f386a1;', 'background-color: var(--ts-dark);')
    html = html.replace('background-color: #d45bb6;', 'background-color: var(--ts-dark);')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated selection color to black on all pages.")
