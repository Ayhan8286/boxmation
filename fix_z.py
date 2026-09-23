import codecs

def fix_z_index():
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()

        # Change z-[-1] to z-0
        html = html.replace('z-[-1]', 'z-0')
        
        # Ensure all major content sections sit above the canvas
        html = html.replace('<section class="w-full', '<section class="w-full relative z-10')

        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    print("Fixed canvas z-index.")

if __name__ == '__main__':
    fix_z_index()
