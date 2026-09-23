import re
import codecs

def update_founder_styling():
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # 1. Change the Ayhan Mirza box from green to black
    # Current: <div class="mt-4 w-full bg-[var(--ts-green)] text-white text-center py-2 brutalist-border mono text-sm font-bold uppercase tracking-widest">Ayhan Mirza</div>
    html = html.replace(
        'bg-[var(--ts-green)] text-white text-center py-2 brutalist-border mono text-sm font-bold uppercase tracking-widest">\n                Ayhan Mirza',
        'bg-[#1e1e1e] text-white text-center py-2 brutalist-border mono text-sm font-bold uppercase tracking-widest">\n                Ayhan Mirza'
    )
    # Also catch inline version if formatting differs
    html = re.sub(
        r'bg-\[var\(--ts-green\)\]( text-white text-center py-2 brutalist-border mono text-sm font-bold uppercase tracking-widest">\s*Ayhan Mirza)',
        r'bg-[#1e1e1e]\1',
        html
    )

    # 2. Remove grayscale and contrast filters from the founder picture
    # Current: <img alt="BoxMation Systems Architect" class="w-full h-full object-cover object-center grayscale contrast-125" src="...">
    html = html.replace(' grayscale contrast-125', '')

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
        
    print("Updated founder page styling.")

if __name__ == '__main__':
    update_founder_styling()
