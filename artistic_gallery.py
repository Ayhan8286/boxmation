import os
import random

photo_dir = r"d:\boxmation\founder_photos"
photos = [f for f in os.listdir(photo_dir) if f.endswith('.jpg')]
photos.sort()

gallery_html = """
<main class="w-full pt-28 pb-32 bg-background min-h-screen relative overflow-hidden">
  
  <!-- Artistic Background Elements -->
  <div class="absolute top-0 left-0 w-full h-full pointer-events-none opacity-20 [background-image:linear-gradient(to_right,#434655_1px,transparent_1px),linear-gradient(to_bottom,#434655_1px,transparent_1px)] [background-size:64px_64px]"></div>
  <div class="absolute top-1/4 -left-1/4 w-[800px] h-[800px] bg-primary/10 blur-[150px] rounded-full pointer-events-none"></div>
  <div class="absolute bottom-1/4 -right-1/4 w-[600px] h-[600px] bg-secondary/10 blur-[150px] rounded-full pointer-events-none"></div>

  <div class="max-w-[1240px] mx-auto px-6 lg:px-8 relative z-10">
    
    <div class="mb-16 text-center">
      <a href="/" class="inline-flex items-center gap-2 text-on-surface-variant hover:text-primary transition-colors font-label-code text-sm uppercase tracking-wider mb-10">
        <span class="material-symbols-outlined text-sm">arrow_back</span>
        Back to Home
      </a>
      <h1 class="font-display text-5xl md:text-7xl text-on-surface font-bold tracking-tighter mb-4">
        The <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">Founder</span>
      </h1>
      <p class="font-body-lg text-on-surface-variant max-w-xl mx-auto">
        A glimpse into the life, the work, and the hustle.
      </p>
    </div>
    
    <!-- Scattered Cards Gallery -->
    <div class="flex flex-wrap justify-center gap-8 md:gap-12 mt-16 pb-20">
"""

rotations = ['rotate-1', '-rotate-2', 'rotate-3', '-rotate-3', 'rotate-2', '-rotate-1', 'rotate-4', '-rotate-4']
margins = ['mt-0', 'mt-12', 'mt-4', 'mt-16', 'mt-8', 'mt-2', 'mt-10']

for i, photo in enumerate(photos):
    rot = rotations[i % len(rotations)]
    margin = margins[i % len(margins)]
    
    gallery_html += f"""
      <div class="group relative w-64 md:w-80 flex-shrink-0 {margin} {rot} transition-all duration-700 hover:rotate-0 hover:scale-105 hover:z-20 cursor-pointer">
        
        <!-- Glow behind card -->
        <div class="absolute -inset-2 bg-gradient-to-r from-primary/0 via-primary/20 to-secondary/0 blur-xl opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
        
        <!-- Polaroid/Artistic Frame -->
        <div class="relative bg-surface-container-highest p-3 pb-8 rounded-xl border border-outline-variant/30 shadow-[0_20px_50px_rgba(0,0,0,0.5)] group-hover:shadow-[0_20px_50px_rgba(5,150,105,0.2)] transition-shadow duration-700">
          <div class="rounded-lg overflow-hidden border border-outline-variant/10 aspect-[4/5] bg-surface-container-lowest">
            <img src="founder_photos/{photo}" alt="Founder Photo" class="w-full h-full object-cover filter contrast-110 saturate-110" loading="lazy" />
          </div>
          
          <!-- Subtle decorative pin/tape element -->
          <div class="absolute top-2 left-1/2 -translate-x-1/2 w-8 h-2 bg-surface-bright/50 backdrop-blur-md rounded-full shadow-sm -rotate-2"></div>
        </div>
      </div>
"""

gallery_html += """
    </div>
  </div>
</main>
"""

with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the entire <main> block
import re
new_text = re.sub(r'<main.*?</main>', gallery_html, text, flags=re.DOTALL)

with open('founder.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Artistic layout created!")
