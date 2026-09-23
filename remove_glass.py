import codecs
import re

def remove_frosted_glass():
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    # Replace bg-white/60 backdrop-blur-sm with bg-transparent
    html = html.replace('bg-white/60 backdrop-blur-sm', 'bg-transparent')
    
    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(html)
        
    print("Removed frosted glass effect.")

if __name__ == '__main__':
    remove_frosted_glass()
