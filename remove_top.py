import re

with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The section starts with <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
# And ends before <section class="mt-24 pt-16 border-t border-outline-variant/10">

start = text.find('<div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">')
end = text.find('<section class="mt-24', start)

if start != -1 and end != -1:
    new_text = text[:start] + text[end:]
    # Now we need to remove the "Behind the Scenes" text and just make the gallery the main thing, 
    # OR leave it as is if they just wanted the top removed.
    
    with open('founder.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Removed top section!")
else:
    print("Could not find section bounds.")
