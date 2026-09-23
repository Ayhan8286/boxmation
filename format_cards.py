import re
import codecs

def format_founder_cards():
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # Find all seq cards
    # They look like:
    # <div class="bg-[#fafafa] border border-[#1e1e1e] p-6 sm:p-8 brutalist-border reveal relative mb-12">
    #     <div class="absolute top-0 left-0 bg-[#1e1e1e] text-white px-3 py-1 mono text-xs font-bold uppercase tracking-widest border-r border-b border-[#1e1e1e]">
    #         sys.log.write // seq_01
    #     </div>
    #     <p class="mono text-sm sm:text-base leading-relaxed text-black pt-6 typewriter-text">
    #         <span class="text-[var(--ts-magenta)]">></span> ...
    #     </p>
    # </div>
    
    # We will use regex to find them all and replace them one by one.
    pattern = r'(<div class="bg-\[#fafafa\] border border-\[#1e1e1e\] p-6 sm:p-8 brutalist-border reveal relative mb-12">.*?sys\.log\.write // seq_0(\d).*?<span class="text-\[var\(--ts-magenta\)\]">></span>.*?</div>)'
    
    matches = re.finditer(pattern, html, flags=re.DOTALL)
    
    # We will replace them sequentially
    colors = [
        ('bg-[var(--ts-pink)]', 'text-black', 'border-black'),
        ('bg-white', 'text-[var(--ts-magenta)]', 'border-[#1e1e1e]'),
        ('bg-[var(--ts-green)] text-white', 'text-black', 'border-black'), # Green background, white text looks better but black is fine. Let's make text-black globally except arrow. Wait, if bg is green, text should be white.
        ('bg-gray-100', 'text-[var(--ts-teal)]', 'border-[#1e1e1e]'),
        ('bg-[var(--ts-teal)] text-white', 'text-black', 'border-black'),
        ('bg-[#fafafa]', 'text-[var(--ts-green)]', 'border-[#1e1e1e]')
    ]

    # Let's rebuild the cards specifically.
    def replacer(match):
        full_match = match.group(0)
        seq_num = int(match.group(2))
        
        idx = (seq_num - 1) % len(colors)
        bg_class, arrow_color, border_color = colors[idx]
        
        # Replace the background
        new_card = full_match.replace('bg-[#fafafa]', bg_class)
        
        # Replace arrow color
        new_card = new_card.replace('text-[var(--ts-magenta)]', arrow_color)
        
        # Add a black straight line separator BEFORE the card (if it's not the first, or maybe above all of them)
        # The user wants "divided into sections with black straight line"
        # Let's wrap the card in a section that has top and bottom borders and full width!
        # Actually, the cards are already inside a max-w container. Adding a hr before it is easiest.
        
        separator = f'\n<div class="w-full h-px bg-black my-16"></div>\n'
        
        return separator + new_card

    new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)
    
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(new_html)
        
    print("Cards formatted.")

if __name__ == '__main__':
    format_founder_cards()
