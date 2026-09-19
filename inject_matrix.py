with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('extracted.html', 'r', encoding='utf-8') as f:
    matrix = f.read()

start_marker = '<!-- COMPARE VS IN-HOUSE -->'
end_marker = '<!-- THE WEDGE & STRICT QUALIFIERS -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + matrix + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Replaced successfully')
else:
    print('Failed to find markers')
