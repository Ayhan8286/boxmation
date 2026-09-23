import codecs

def fix_header():
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()

        html = html.replace('bg-transparent/90', 'bg-white/90')

        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    print("Fixed header.")

if __name__ == '__main__':
    fix_header()
