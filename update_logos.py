with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<div class="flex flex-col gap-16 items-center justify-center relative z-10 w-full px-8">'
end_marker = '  </div>\n</div>\n\n</div>\n</div>\n</section>'

start = text.find(start_marker)
end = text.find(end_marker, start)

if start != -1 and end != -1:
    new_html = """<div class="flex flex-row flex-wrap gap-x-12 gap-y-16 items-center justify-center relative z-10 w-full px-2">
    
    <!-- Logo 1: Exzellent -->
    <div class="w-32 sm:w-40 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)]">
      <img src="exzellent.png" alt="Exzellent" class="w-full h-auto object-contain" />
    </div>

    <!-- Logo 2: Blackmont -->
    <div class="w-28 sm:w-36 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)]">
      <img src="blackmont.png" alt="Blackmont Consulting" class="w-full h-auto object-contain" />
    </div>

    <!-- Logo 3: Orange Tree -->
    <div class="w-40 sm:w-48 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)]">
      <img src="orange.png" alt="Orange Tree Systems" class="w-full h-auto object-contain" />
    </div>

    <!-- Logo 4: Alhuda -->
    <div class="w-32 sm:w-40 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-80 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)] rounded-2xl overflow-hidden">
      <img src="alhuda.png" alt="Alhuda Network" class="w-full h-auto object-contain scale-[1.02]" />
    </div>

    <!-- Logo 5: Namrah -->
    <div class="w-48 sm:w-56 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)]">
      <img src="namrah.png" alt="Namrah Trading LLC" class="w-full h-auto object-contain" />
    </div>

"""
    
    # Replace it
    new_text = text[:start] + new_html + text[end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced perfectly.")
else:
    print(f"Could not find markers. Start={start} End={end}")
