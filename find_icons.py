import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Try to find SVG icons for social media
matches = re.finditer(r'<a[^>]*href="[^"]*".*?</svg>.*?</a>', text, re.DOTALL)
for i, m in enumerate(matches):
    print(f"Match {i}:")
    # print(m.group(0)[:200] + "...")
