import codecs
import time
import re

def bust_cache():
    for page in ['booking.html', 'pricing.html', 'index.html', 'founder.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()
        
        ts = int(time.time())
        html = re.sub(r'src="animations\.js(\?v=\d+)?"', f'src="animations.js?v={ts}"', html)
        
        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    print("Forced cache busting!")

if __name__ == '__main__':
    bust_cache()
