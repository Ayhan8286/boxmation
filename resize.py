for file in ['index.html', 'terms.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('class="h-8 w-auto object-contain" src="logo.jpg"', 'class="h-12 w-auto object-contain" src="logo.jpg"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
