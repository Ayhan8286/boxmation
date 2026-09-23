import os
import re

files = ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']
for filename in files:
    path = f'd:/boxmation/{filename}'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the ::selection block
    pattern = r'::selection\s*\{[^}]*\}'
    
    bulletproof_selection = """::selection {
            background-color: #1e1e1e !important;
            color: #fefefe !important;
        }
        ::-moz-selection {
            background-color: #1e1e1e !important;
            color: #fefefe !important;
        }"""
        
    if re.search(pattern, html):
        html = re.sub(pattern, bulletproof_selection, html)
    else:
        # Inject it before </style>
        html = html.replace('</style>', f'\n{bulletproof_selection}\n</style>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Injected bulletproof selection CSS.")
