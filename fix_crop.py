with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the aspect ratio container and image classes
# Old:
# <div class="rounded-lg overflow-hidden border border-outline-variant/10 aspect-[4/5] bg-surface-container-lowest">
#   <img src="founder_photos/..." alt="..." class="w-full h-full object-cover ...">

text = text.replace('aspect-[4/5]', '')
text = text.replace('w-full h-full object-cover', 'w-full h-auto')

with open('founder.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed forced cropping!")
