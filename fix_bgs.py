import codecs

def fix_all():
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()

        # Fix footer
        html = html.replace('<footer class="w-full bg-transparent', '<footer class="w-full bg-white')
        
        # Fix feature cards
        html = html.replace('p-4 bg-transparent border', 'p-4 bg-white border')
        html = html.replace('p-5 bg-transparent border', 'p-5 bg-white border')

        # Fix specific cards that were broken
        html = html.replace('hidden xl:hidden bg-transparent border-t', 'hidden xl:hidden bg-white border-t')

        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)

    print("Fixed backgrounds!")

if __name__ == '__main__':
    fix_all()
