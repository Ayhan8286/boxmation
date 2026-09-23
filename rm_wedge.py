import os, re

files = ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']
for filename in files:
    path = f'd:/boxmation/{filename}'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # remove all links to the wedge
    content = re.sub(r'<a[^>]*href="[^"]*the-wedge"[^>]*>.*?</a>\s*', '', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed wedge links.")
