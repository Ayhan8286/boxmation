import re
import codecs

def main():
    with codecs.open('d:/boxmation/index.backup.html', 'r', 'utf-8') as f:
        backup = f.read()

    # Get the text part of the founder section
    match = re.search(r'(<div class="lg:col-span-7">.*?</div>\s*</div>\s*</div>\s*</section>)', backup, flags=re.DOTALL)
    if match:
        text_part = match.group(1)
        
        # We want to put this text_part into index.html
        with codecs.open('d:/boxmation/index.html', 'r', 'utf-8') as f:
            curr = f.read()
            
        # The broken section is basically the start of the grid and then </section> immediately
        broken_regex = r'(<!-- 3\. FOUNDER & HARD POSITIONING SECTION -->\s*<section class="w-full py-24 relative" id="founder">\s*<div class="max-w-\[1240px\] mx-auto px-6 lg:px-8 reveal">\s*<div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">\s*</section>)'
        
        new_section = f'''<!-- 3. FOUNDER & HARD POSITIONING SECTION -->
<section class="w-full py-24 relative" id="founder">
<div class="max-w-[1240px] mx-auto px-6 lg:px-8 reveal">
<div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
{text_part}'''
        
        curr = re.sub(broken_regex, new_section, curr, flags=re.DOTALL)
        
        # Make the text full width
        curr = curr.replace('<div class="lg:col-span-7">', '<div class="lg:col-span-12 max-w-4xl mx-auto">')
        
        # Wait, the text_part might contain other stuff that was removed earlier? No, the founder text wasn't modified earlier today.
        
        with codecs.open('d:/boxmation/index.html', 'w', 'utf-8') as f:
            f.write(curr)
        print("Restored text part!")
    else:
        print("Could not find text part in backup")

if __name__ == '__main__':
    main()
