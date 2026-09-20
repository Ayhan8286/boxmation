import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<a[^>]*href="[^"]*".*?</svg>.*?</a>', text, re.DOTALL)
for i, m in enumerate(matches):
    if "hover:text-primary" in m.group(0) or "hover:-translate-y-1" in m.group(0):
        print(f"Match {i}: {m.group(0)}")
