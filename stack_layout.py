import re

with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the gallery div opening
target_start = '<div class="flex flex-wrap justify-center gap-8 md:gap-12 mt-16 pb-20">'
replacement_start = '<div class="flex flex-wrap justify-center items-center gap-y-16 -space-x-24 md:-space-x-32 mt-16 pb-32 max-w-[1000px] mx-auto px-8">'

text = text.replace(target_start, replacement_start)

# Add z-index transitions and higher hover z-index to cards
text = text.replace('hover:z-20', 'hover:z-50 focus-within:z-50')

# Randomize rotations a bit more for a dense stack look
import random
rotations = ['rotate-2', '-rotate-3', 'rotate-6', '-rotate-6', 'rotate-3', '-rotate-2', 'rotate-4', '-rotate-4', 'rotate-1', '-rotate-1']
margins = ['mt-0', 'mt-8', '-mt-8', 'mt-4', '-mt-4', 'mt-12', '-mt-12']

# We need to replace the margins and rotations in the div class.
# The original script injected classes like: class="group relative w-64 md:w-80 flex-shrink-0 mt-12 -rotate-2 transition-all...

def replacer(match):
    r = random.choice(rotations)
    m = random.choice(margins)
    # The regex matches the margin and rotation classes
    return f'class="group relative w-64 md:w-80 flex-shrink-0 {m} {r} transition-all'

text = re.sub(r'class="group relative w-64 md:w-80 flex-shrink-0 mt-[-\d]+ -?rotate-\d transition-all', replacer, text)

# Just in case the regex doesn't match perfectly, let's use a simpler one based on what was actually injected:
text = re.sub(r'class="group relative w-64 md:w-80 flex-shrink-0 [a-z0-9-]+ [a-z0-9-]+ transition-all', replacer, text)


with open('founder.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated layout to dense stack!")
