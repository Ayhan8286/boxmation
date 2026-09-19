with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<div class="flex flex-row flex-wrap gap-x-12 gap-y-16 items-center justify-center relative z-10 w-full px-2">'
replacement = """  <div class="w-full text-center mb-10 relative z-10">
    <span class="font-label-badge text-label-badge text-primary uppercase tracking-[0.15em] font-bold">Trusted By Industry Leaders</span>
  </div>

  <div class="flex flex-row flex-wrap gap-x-12 gap-y-16 items-center justify-center relative z-10 w-full px-2">"""

if target in text:
    new_text = text.replace(target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Label added!")
else:
    print("Target not found.")
