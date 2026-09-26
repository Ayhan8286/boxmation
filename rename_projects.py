import glob, re

files = glob.glob('*.html')
files = [f for f in files if not f.endswith('.bak')]

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    original = c
    # Rename nav/footer link text "Projects" -> "Case Studies" and update href
    c = c.replace('href="/projects.html">Projects</a>', 'href="/projects.html">Case Studies</a>')
    if c != original:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated: " + fn)
    else:
        print("No change: " + fn)
