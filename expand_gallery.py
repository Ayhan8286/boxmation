with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'max-w-[1000px]'
replacement = 'max-w-[1500px] w-full'

if target in text:
    text = text.replace(target, replacement)
    # Also let's slightly adjust the negative space so they don't overlap *too* much now that we have more room
    text = text.replace('-space-x-24 md:-space-x-32', '-space-x-20 md:-space-x-24 lg:-space-x-28')
    with open('founder.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Expanded width!")
else:
    print("Not found.")
