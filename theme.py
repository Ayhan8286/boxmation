for file in ['index.html', 'terms.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    replacements = {
        '"primary":"#b4c5ff"': '"primary":"#6ee7b7"',
        '"primary-container":"#2563eb"': '"primary-container":"#059669"',
        '"on-primary-container":"#eeefff"': '"on-primary-container":"#ecfdf5"',
        '"primary-fixed":"#dbe1ff"': '"primary-fixed":"#a7f3d0"',
        '"on-primary":"#002a78"': '"on-primary":"#022c22"',
        '"surface-tint":"#b4c5ff"': '"surface-tint":"#6ee7b7"',
        
        '"secondary":"#adc6ff"': '"secondary":"#99f6e4"',
        '"secondary-container":"#0566d9"': '"secondary-container":"#0f766e"',
        '"on-secondary-container":"#e6ecff"': '"on-secondary-container":"#f0fdfa"'
    }
    
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
