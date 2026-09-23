import codecs

def fix_transparent_main():
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()

        # Remove bg-white from main
        html = html.replace('bg-white', 'bg-transparent', 1)
        
        # Or more accurately:
        html = html.replace('<main class="w-full pt-20 bg-white min-h-screen relative overflow-hidden">', '<main class="w-full pt-20 bg-transparent min-h-screen relative overflow-hidden">')

        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    print('Fixed transparent main')

if __name__ == '__main__':
    fix_transparent_main()
