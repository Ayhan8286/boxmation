import os

photo_dir = r"d:\boxmation\founder_photos"
photos = [f for f in os.listdir(photo_dir) if f.endswith('.jpg')]
photos.sort()

# We still have 12 photos. 4 clusters of 3.
clusters = [
    photos[0:3],
    photos[3:6],
    photos[6:9],
    photos[9:12]
]

def make_cluster(photo_list, float_dir):
    margin = "ml-12 mb-10 mr-auto md:mr-0 float-none md:float-right" if float_dir == 'right' else "mr-12 mb-10 ml-auto md:ml-0 float-none md:float-left"
    
    html = f'<div class="{margin} w-full md:w-[480px] my-4 z-20 flex flex-wrap justify-center gap-6">'
    
    rotations = ['-rotate-2', 'rotate-2', '-rotate-1']
    
    for i, p in enumerate(photo_list):
        r = rotations[i % len(rotations)]
        
        html += f"""
        <div class="w-48 md:w-52 flex-shrink-0 {r} transition-transform duration-500 hover:rotate-0 hover:scale-[1.03] cursor-pointer relative">
            <div class="bg-surface-container-highest p-2 pb-6 rounded-xl border border-outline-variant/30 shadow-xl">
              <div class="rounded-lg overflow-hidden border border-outline-variant/10 bg-surface-container-lowest">
                <img src="founder_photos/{p}" class="w-full h-auto" loading="lazy" />
              </div>
              <div class="absolute top-2 left-1/2 -translate-x-1/2 w-6 h-1.5 bg-surface-bright/50 backdrop-blur-md rounded-full shadow-sm -rotate-1"></div>
            </div>
        </div>
        """
    html += '</div>'
    return html


story_html = f"""
<main class="w-full pt-28 pb-32 bg-background min-h-screen relative overflow-hidden">
  
  <!-- Artistic Background Elements -->
  <div class="absolute top-0 left-0 w-full h-full pointer-events-none opacity-20 [background-image:linear-gradient(to_right,#434655_1px,transparent_1px),linear-gradient(to_bottom,#434655_1px,transparent_1px)] [background-size:64px_64px]"></div>
  <div class="absolute top-1/4 -left-1/4 w-[800px] h-[800px] bg-primary/10 blur-[150px] rounded-full pointer-events-none"></div>
  <div class="absolute bottom-1/4 -right-1/4 w-[600px] h-[600px] bg-secondary/10 blur-[150px] rounded-full pointer-events-none"></div>

  <div class="max-w-6xl mx-auto px-6 lg:px-12 relative z-10">
    
    <div class="mb-16 text-center">
      <a href="/" class="inline-flex items-center gap-2 text-on-surface-variant hover:text-primary transition-colors font-label-code text-sm uppercase tracking-wider mb-10">
        <span class="material-symbols-outlined text-sm">arrow_back</span>
        Back to Home
      </a>
      <h1 class="font-display text-5xl md:text-7xl text-on-surface font-bold tracking-tighter mb-4">
        The <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">Founder</span>
      </h1>
      <h2 class="font-headline-md text-2xl md:text-3xl text-on-surface font-bold mt-12 text-center">Beyond the Systems</h2>
    </div>
    
    <div class="text-left font-body-lg text-on-surface-variant text-lg md:text-xl leading-relaxed relative clearfix pb-20">
      
      {make_cluster(clusters[0], 'right')}
      
      <p class="mb-8">I build outbound systems for a living, but that's not really who I am — it's just what I'm good at right now.</p>

      <p class="mb-8">I box. Featherweight. There's something clean about it that I don't get anywhere else — no ambiguity, no politics, just you, the work you put in, and whether you did it or not. The gym is the same way for me. It's where the noise stops.</p>
      
      {make_cluster(clusters[1], 'left')}

      <p class="mb-8">I read constantly — mostly mentalist books and self-help, the kind that try to explain why people do what they do. I think that's the same curiosity that pulled me into building systems in the first place: understanding what makes someone say yes, what makes them trust, what makes them act. One version of that curiosity became my career. The other version just makes me a better conversation at dinner.</p>

      <p class="mb-8">I want to travel properly one day — not tourist-checklist travel, but actually spend real time somewhere. Germany's on that list. Italy too. Sweden and Finland pull at me for a different reason — I don't know exactly why, but something about the quiet, the order, the cold clarity of those countries appeals to me. And Norway — the northern lights specifically — feels like one of those things you have to see with your own eyes at least once before you die.</p>

      {make_cluster(clusters[2], 'right')}

      <p class="mb-8">There's also a version of my future where I'm doing a master's abroad, somewhere genuinely good, not just chasing a degree but finally getting to enjoy life without constantly grinding against something. I think about that a lot — what it would feel like to build toward something instead of just surviving toward it.</p>

      <p class="mb-8">I've also spent time building things that had nothing to do with revenue — an app for people with hearing disabilities, a period-tracking and guidance app, teaching automation workshops and speaking to students as Director of the AI Society at UCP. Not every build has to make money to matter.</p>

      {make_cluster(clusters[3], 'left')}

      <p class="font-medium text-on-surface border-l-4 border-primary pl-5 py-2 mt-12 clear-both">
        So that's the fuller picture — the founder title is real, but so is the boxer, the reader, the guy still figuring out where he wants to end up, and the guy who'd rather build something useful than something impressive.
      </p>

    </div>
  </div>
</main>
"""

with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
new_text = re.sub(r'<main.*?</main>', story_html, text, flags=re.DOTALL)

with open('founder.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Spaced out cluster layout injected!")
