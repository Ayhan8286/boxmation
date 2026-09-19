with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<!-- Client Success Visual (Stationary Grid) -->')
end = text.find('<!-- THE WEDGE & STRICT QUALIFIERS -->')

new_block = """<!-- Client Success Visual (Floating Logos) -->
<div class="lg:col-span-5 flex flex-col justify-center items-center relative min-h-[500px] h-full hidden lg:flex p-6">
  <!-- Subtle background glow -->
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-primary-container/10 blur-[80px] rounded-full pointer-events-none"></div>
  
  <div class="flex flex-col gap-16 items-center justify-center relative z-10 w-full px-8">
    
    <!-- Logo 1: Exzellent -->
    <div class="w-48 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-80 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)]">
      <img src="exzellent.png" alt="Exzellent" class="w-full h-auto object-contain" />
    </div>

    <!-- Logo 2: Orange Tree -->
    <div class="w-56 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-80 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)]">
      <img src="orange.png" alt="Orange Tree Systems" class="w-full h-auto object-contain" />
    </div>

    <!-- Logo 3: Namrah -->
    <div class="w-64 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-80 hover:opacity-100 drop-shadow-[0_0_20px_rgba(5,150,105,0.15)]">
      <img src="namrah.png" alt="Namrah Trading LLC" class="w-full h-auto object-contain" />
    </div>

  </div>
</div>

</div>
</div>
</section>
"""

# Note: The original block contains the closing div/section tags for transparent-offer grid.
# The `new_block` includes `</div></div></section>\n` to correctly close the grid, the max-w container, and the section.

if start != -1 and end != -1:
    new_text = text[:start] + new_block + '\n' + text[end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced!")
else:
    print("Failed to find markers")
