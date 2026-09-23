import codecs

def fix_bg_pos():
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()

        html = html.replace('background-position: center top;', 'background-position: top left;')

        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    print('Fixed background position')

if __name__ == '__main__':
    fix_bg_pos()
