import codecs
import re

def move_canvas_to_card():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # 1. Remove the canvas from the <main> block
    canvas_str = '<canvas id="booking-bg" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0" style="opacity: 1;"></canvas>'
    html = html.replace(canvas_str, '')

    # 2. Find the card
    # <div class="max-w-6xl mx-auto p-8 sm:p-16 border border-[#1e1e1e] brutalist-border">
    # Wait, in BS4 output it was:
    # ['max-w-6xl', 'mx-auto', 'p-8', 'sm:p-16', 'border', 'border-[#1e1e1e]', 'brutalist-border']
    
    card_pattern = r'(<div class="max-w-6xl mx-auto p-8 sm:p-16 border border-\[#1e1e1e\] brutalist-border">)'
    
    # We will make the card bg-white AND relative overflow-hidden
    new_card_open = '<div class="max-w-6xl mx-auto p-8 sm:p-16 border border-[#1e1e1e] brutalist-border bg-white relative overflow-hidden">'
    new_canvas = '\n<canvas id="booking-bg" class="absolute inset-0 w-full h-full pointer-events-none z-0" style="opacity: 1;"></canvas>\n'
    
    html = re.sub(card_pattern, new_card_open + new_canvas, html)
    
    # Ensure text container inside the card is elevated above the canvas
    # The first child is <div class="flex flex-col gap-16">
    html = html.replace('<div class="flex flex-col gap-16">', '<div class="flex flex-col gap-16 relative z-10">')

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
        
    print("Moved canvas inside the card and made card opaque.")

if __name__ == '__main__':
    move_canvas_to_card()
