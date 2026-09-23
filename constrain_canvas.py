import codecs
import re

def constrain_canvas():
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    # 1. Remove the canvas from its current location
    canvas_regex = r'<canvas id="founder-bg"[^>]*></canvas>'
    html = re.sub(canvas_regex, '', html)

    # 2. Inject it into the founder card
    # The founder card starts with:
    # <div class="bg-[#fafafa] border border-[#1e1e1e] p-0 sm:p-0 brutalist-border flex flex-col md:flex-row relative reveal mb-16">
    #     <div class="absolute top-0 right-0 bg-[var(--ts-magenta)] ...
    
    new_canvas = '<canvas id="founder-bg" class="absolute top-0 left-0 w-full h-full z-0 opacity-80" style="pointer-events: auto;"></canvas>\n'
    
    # We find the founder card
    card_pattern = r'(<div class="bg-\[#fafafa\] border border-\[#1e1e1e\] p-0 sm:p-0 brutalist-border flex flex-col md:flex-row relative reveal mb-16">)'
    html = re.sub(card_pattern, r'\1\n        ' + new_canvas, html)

    # 3. Restore bg-white to main
    html = html.replace(
        '<main class="w-full pt-20 bg-transparent min-h-screen relative overflow-hidden">',
        '<main class="w-full pt-20 bg-white min-h-screen relative overflow-hidden">'
    )

    # 4. Restore bg-white to sections
    html = html.replace('bg-transparent', 'bg-white')
    
    # 5. Make sure the text inside the founder card sits above the canvas (z-10)
    # The right side is: <div class="w-full md:w-2/3 p-8 sm:p-12 flex flex-col justify-center">
    html = html.replace(
        '<div class="w-full md:w-2/3 p-8 sm:p-12 flex flex-col justify-center">',
        '<div class="w-full md:w-2/3 p-8 sm:p-12 flex flex-col justify-center relative z-10">'
    )
    # The left side is: <div class="w-full md:w-1/3 relative border-b md:border-b-0 md:border-r border-[#1e1e1e] bg-white p-6 flex flex-col justify-center items-center">
    html = html.replace(
        '<div class="w-full md:w-1/3 relative border-b md:border-b-0 md:border-r border-[#1e1e1e] bg-white p-6 flex flex-col justify-center items-center">',
        '<div class="w-full md:w-1/3 relative border-b md:border-b-0 md:border-r border-[#1e1e1e] bg-white p-6 flex flex-col justify-center items-center z-10">'
    )

    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(html)
        
    print("Constrained canvas to founder card.")

if __name__ == '__main__':
    constrain_canvas()
