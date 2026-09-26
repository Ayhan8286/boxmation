"""Force hard refresh by adding a cache-buster meta tag to all pages"""
import glob

files = glob.glob('*.html')
files = [f for f in files if not f.endswith('.bak')]

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Add cache-control meta tag right after <head>
    old = '<meta charset="utf-8"/>'
    new = '<meta charset="utf-8"/>\n<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"/>\n<meta http-equiv="Pragma" content="no-cache"/>'
    
    if 'Cache-Control' not in c:
        c = c.replace(old, new, 1)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated: " + fn)
    else:
        print("Already has cache control: " + fn)
