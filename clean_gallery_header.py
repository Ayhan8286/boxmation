with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<section class="mt-24 pt-16 border-t border-outline-variant/10">', '<section class="mt-8">')
text = text.replace('Behind the Scenes', 'The Founder')

with open('founder.html', 'w', encoding='utf-8') as f:
    f.write(text)
