import re

files = ['founder.html', 'pricing.html', 'booking.html', 'terms.html', 'index.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    links = re.findall(r'href="[^"]*">[^<]+</a>', c)
    print("\n=== " + fn + " ===")
    for l in links[:20]:
        print(l)
