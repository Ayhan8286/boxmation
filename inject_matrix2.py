with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('extracted.html', 'r', encoding='utf-8') as f:
    matrix = f.read()

start = text.find('<!-- COMPARE VS IN-HOUSE -->')
end = text.find('</section>', start) + len('</section>')

if start != -1 and end > start:
    new_text = text[:start] + matrix + '\n' + text[end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Replaced!')
else:
    print('Not found')
