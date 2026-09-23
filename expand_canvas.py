import codecs
import re

def expand_founder_canvas():
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    # 1. Update the canvas classes
    html = html.replace(
        '<canvas id="founder-bg" class="absolute top-0 left-0 w-full h-[600px] pointer-events-auto z-0"',
        '<canvas id="founder-bg" class="fixed top-0 left-0 w-full h-full pointer-events-none -z-10"'
    )

    # 2. Make the full-width section backgrounds translucent so the canvas can be seen through them
    # The current colors are:
    # bg-white -> bg-white/90
    # bg-gray-100 -> bg-gray-100/90
    # bg-[var(--ts-pink)] -> bg-[#f386a1]/90
    # bg-emerald-100 -> bg-emerald-100/90
    # bg-[var(--ts-green)] -> bg-[#03aa5c]/90
    # bg-[var(--ts-teal)] -> bg-[#09aea1]/90
    # bg-orange-200 -> bg-orange-200/90
    
    # Actually, the user asked to KEEP the background white in the PREVIOUS step, but they said "i want it on that whole page".
    # If the background is solid white, they won't see the canvas.
    # So we must make the backgrounds slightly transparent! Let's do /80 to make the animation clearly visible.
    
    # We will just replace `class="w-full border-b border-[#1e1e1e] py-16 bg-white"`
    # Wait, in the previous step we made ALL sections bg-white!
    # "u may keep the background whitet , and the text container u can do white grey mint green , pink, orange"
    
    # So the SECTIONS are `bg-white`. The CARDS are colored.
    # Let's replace `bg-white` on the SECTIONS with `bg-transparent`! Or `bg-white/70`.
    html = re.sub(
        r'(<section class="w-full border-b border-\[#1e1e1e\] py-16 )bg-white(">)',
        r'\1bg-white/60 backdrop-blur-sm\2',
        html
    )
    
    # Wait, the main container `<main class="w-full pt-20 bg-white min-h-screen relative overflow-hidden">`
    # That `bg-white` on <main> will hide the canvas!
    html = html.replace(
        '<main class="w-full pt-20 bg-white min-h-screen relative overflow-hidden">',
        '<main class="w-full pt-20 bg-transparent min-h-screen relative overflow-hidden">'
    )

    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(html)
        
    print("Expanded canvas and made backgrounds translucent.")

if __name__ == '__main__':
    expand_founder_canvas()
