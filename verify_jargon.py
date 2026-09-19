import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'(<h4 class="font-label-badge.*?WHAT IS INCLUDED.*?Lock In 14-Day Outbound)', text, re.DOTALL)
if m:
    print('--- OFFER SECTION ---')
    clean = re.sub('<[^<]+>', ' ', m.group(1)).strip()
    clean = re.sub(' +', ' ', clean)
    print(clean)

m2 = re.search(r'(<!-- COMPARISON MATRIX.*?RECOMMENDED FOR B2B.*?</section>)', text, re.DOTALL)
if m2:
    print('--- COMPARE SECTION ---')
    clean2 = re.sub('<[^<]+>', ' ', m2.group(1)).strip()
    clean2 = re.sub(' +', ' ', clean2)
    print(clean2)
