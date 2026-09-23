import codecs
import re

def add_grid_to_first_section():
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # 1. Add the .bg-grid-pattern CSS rule to the <style> block
    grid_css = """
        .bg-grid-pattern {
            background-image: linear-gradient(rgba(30,30,30,0.06) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(30,30,30,0.06) 1px, transparent 1px);
            background-size: 40px 40px;
            background-position: center top;
        }
    """
    if '.bg-grid-pattern' not in html:
        html = html.replace('</style>', grid_css + '</style>')

    # 2. Modify the HTML structure of the first section
    # The current top block is:
    # <div class="max-w-[1000px] mx-auto px-6 lg:px-8 relative z-10 py-24">
    #     <div class="mb-20 text-center reveal"> ... </div>
    #     <div class="bg-[#fafafa] ... mb-16"> ... founder card ... </div>
    #     <h2 class='text-xl md:text-2xl font-medium mb-12 uppercase mono font-bold border-b border-[#1e1e1e] pb-4'>Beyond the Systems</h2>
    # </div>
    
    # Let's extract everything UP TO "Beyond the Systems"
    
    pattern = r'(<div class="max-w-\[1000px\] mx-auto px-6 lg:px-8 relative z-10 py-24">)(.*?(?:mb-16">.*?</div>\s*</div>\s*</div>))(\s*<h2)'
    
    # Using a simpler string replace since regex with DOTALL on huge blocks can be fragile
    # The header starts with `<div class="mb-20 text-center reveal">`
    # The card ends at `</div>` before `<h2 class='text-xl md:text-2xl font-medium mb-12`
    
    match = re.search(r'(<div class="max-w-\[1000px\] mx-auto px-6 lg:px-8 relative z-10 py-24">)(.*?)(<h2 class=[\'"]text-xl)', html, flags=re.DOTALL)
    
    if match:
        top_content = match.group(2)
        
        # We wrap top_content in a new full-width section
        new_first_section = f"""
<section class="w-full border-b border-[#1e1e1e] pt-32 pb-24 bg-grid-pattern relative z-10">
    <div class="max-w-[1000px] mx-auto px-6 lg:px-8">
        {top_content}
    </div>
</section>
<div class="max-w-[1000px] mx-auto px-6 lg:px-8 relative z-10 pt-16">
"""
        
        html = html[:match.start()] + new_first_section + match.group(3) + html[match.end(3):]
        
        # We need to remove the original opening div that we replaced:
        # Wait, the match replaced `<div class="max-w-[1000px]...>` with `<section>...<div>...`. That's perfect.
        # But wait! There is a `</div>` at the end of the sections block that corresponds to the ORIGINAL `<div class="max-w-[1000px]... py-24">`!
        # Because we closed `<section>` and opened a NEW `<div class="max-w-[1000px]... pt-16">`, the closing `</div>` later on will correctly close this NEW div!
        # This is a perfect 1:1 replacement.
        
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
        
    print("Added grid pattern to first section.")

if __name__ == '__main__':
    add_grid_to_first_section()
