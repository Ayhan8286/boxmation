import re
with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'class="group relative w-64 md:w-80 flex-shrink-0.*?transition-all', text)
for m in matches[:3]:
    print(m)
