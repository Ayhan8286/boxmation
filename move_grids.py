import codecs
from bs4 import BeautifulSoup
import re

def move_grids():
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find all gallery grids
    # They have class 'flex flex-wrap justify-center gap-6 reveal mt-12'
    galleries = soup.find_all('div', class_=lambda c: c and 'flex-wrap' in c and 'gap-6' in c and 'mt-12' in c)
    
    gallery_html = ""
    for g in galleries:
        # We extract their inner HTML (the actual picture divs)
        gallery_html += g.decode_contents() + "\n"
        # Remove the gallery from its current location
        g.decompose()

    # We want to put them all into a single grid in the first section.
    # Where should they go?
    # Right below the "WHO BUILDS & RUNS YOUR PIPELINE" card!
    # That card is inside `<div class="max-w-[1000px] mx-auto px-6 lg:px-8">` which is inside `<main>` before the `<section>`s begin.
    
    # Wait, in the current structure:
    # <div class="mb-20 text-center reveal"> ... header ... </div>
    # <div class="bg-[#fafafa] ... mb-16"> ... main founder card ... </div>
    # <h2 class='text-xl md:text-2xl font-medium mb-12 ...'>Beyond the Systems</h2>
    # </div> (closes the max-w container)
    # <section> ...
    
    # Let's inject a new gallery block between the main founder card and "Beyond the Systems"
    
    master_gallery = f"""
    <!-- MASTER GALLERY GRID -->
    <div class="flex flex-wrap justify-center gap-6 reveal mb-20">
        {gallery_html}
    </div>
    """
    
    new_html = str(soup)
    
    # Let's insert the master gallery before "Beyond the Systems"
    beyond_systems_tag = "<h2 class=\"text-xl md:text-2xl font-medium mb-12 uppercase mono font-bold border-b border-[#1e1e1e] pb-4\">Beyond the Systems</h2>"
    
    if beyond_systems_tag in new_html:
        new_html = new_html.replace(beyond_systems_tag, master_gallery + beyond_systems_tag)
    else:
        # Fallback
        new_html = new_html.replace('Beyond the Systems', master_gallery + 'Beyond the Systems')

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(new_html)
        
    print("Moved all gallery grids to the first section.")

if __name__ == '__main__':
    move_grids()
