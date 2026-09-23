import os
from bs4 import BeautifulSoup
import re

def reformat_founder():
    filepath = 'd:/boxmation/founder.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the main text container
    container = soup.find('div', class_=lambda c: c and 'text-left' in c and 'clearfix' in c)
    if not container:
        print("Could not find the text container.")
        return

    # Extract all elements sequentially
    elements = []
    for child in container.find_all(recursive=False):
        if child.name == 'p':
            elements.append(('text', child.decode_contents()))
        elif child.name == 'div' and 'w-[480px]' in child.get('class', []):
            # It's an image group
            elements.append(('images', child.decode_contents()))

    # Build the new HTML structure
    new_html = ""
    
    # Add a typing effect script hook
    new_html += '<div class="max-w-4xl mx-auto space-y-16">\n'

    for el_type, content in elements:
        if el_type == 'text':
            # Format text as a typewriter/terminal block
            # To make it look like typewriter text, we use mono font, add a '>' prompt, and style it.
            # We can also add a typing animation class.
            text_lines = content.strip()
            
            new_html += f'''
            <div class="bg-[#fafafa] border border-[#1e1e1e] p-6 sm:p-8 brutalist-border reveal relative">
                <div class="absolute top-0 left-0 bg-[#1e1e1e] text-white px-3 py-1 mono text-xs font-bold uppercase tracking-widest border-r border-b border-[#1e1e1e]">
                    sys.log.write
                </div>
                <p class="mono text-sm sm:text-base leading-relaxed text-black pt-6 typewriter-text">
                    <span class="text-[var(--ts-magenta)]">></span> {text_lines}
                </p>
            </div>
            '''
        elif el_type == 'images':
            # Format images as a centered flex row, removing float
            new_html += f'''
            <div class="flex flex-wrap justify-center gap-6 reveal my-12">
                {content}
            </div>
            '''

    new_html += '</div>\n'

    # Replace the container's outer html with the new structure
    # Wait, using bs4 for replacement is sometimes messy.
    # We will replace the original container string in the raw HTML.
    
    container_str = str(container)
    
    # Let's write the raw HTML back
    # We need to make sure we replace it exactly.
    new_full_html = html.replace(container_str, new_html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_full_html)

if __name__ == '__main__':
    reformat_founder()
