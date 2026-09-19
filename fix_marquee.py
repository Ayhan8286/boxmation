with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_html_block = """<!-- Client Success Visual (Stationary Grid) -->
<div class="lg:col-span-5 flex flex-col justify-center relative min-h-[500px] h-full hidden lg:flex p-6 rounded-2xl bg-surface-container-low/30 border border-outline-variant/10 overflow-hidden">
  <!-- Subtle background glow -->
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-primary-container/10 blur-[100px] rounded-full pointer-events-none"></div>
  
  <!-- Headline Badge -->
  <div class="text-center mb-8 relative z-10 w-full mt-4">
    <div class="inline-flex items-center justify-center px-6 py-3 rounded-2xl bg-primary-container/10 border border-primary/20 shadow-[0_0_30px_rgba(37,99,235,0.15)] backdrop-blur-md hover:bg-primary-container/20 transition-colors cursor-default">
      <span class="material-symbols-outlined text-primary mr-2 text-2xl">trending_up</span>
      <span class="font-headline-sm text-primary font-bold tracking-tight">
        $100k+ Pipeline Generated in 90 Days
      </span>
    </div>
  </div>

  <!-- B2B Cards Grid -->
  <div class="relative w-full grid grid-cols-2 gap-5 z-10 mb-4">
    
    <!-- Card 1 -->
    <div class="p-6 rounded-2xl bg-surface-container border border-outline-variant/30 shadow-lg hover:-translate-y-1 transition-transform flex flex-col justify-center gap-2 group">
      <span class="text-xs font-label-badge text-primary uppercase font-bold tracking-wider">B2B SaaS</span>
      <span class="font-headline-sm text-on-surface font-semibold leading-tight group-hover:text-primary transition-colors">Exzellent.co</span>
      <div class="mt-1 flex items-center gap-1.5 text-on-surface-variant text-sm">
        <span class="material-symbols-outlined text-base text-[#25D366]">check_circle</span>
        <span>Qualified Meetings</span>
      </div>
    </div>
    
    <!-- Card 2 -->
    <div class="p-6 rounded-2xl bg-surface-container-high border border-outline-variant/30 shadow-lg hover:-translate-y-1 transition-transform flex flex-col justify-center gap-2 translate-y-6 group">
      <span class="text-xs font-label-badge text-tertiary uppercase font-bold tracking-wider">Consulting</span>
      <span class="font-headline-sm text-on-surface font-semibold leading-tight group-hover:text-tertiary transition-colors">Blackmont</span>
      <div class="mt-1 flex gap-0.5 text-yellow-500">
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
      </div>
    </div>
    
    <!-- Card 3 -->
    <div class="p-6 rounded-2xl bg-surface-container border border-outline-variant/30 shadow-lg hover:-translate-y-1 transition-transform flex flex-col justify-center gap-2 group">
      <div class="flex items-start justify-between mb-1">
        <span class="font-headline-sm text-on-surface font-semibold leading-tight group-hover:text-secondary transition-colors">Alhuda Network</span>
        <span class="material-symbols-outlined text-primary text-xl opacity-80 group-hover:opacity-100 group-hover:translate-x-1 group-hover:-translate-y-1 transition-all">rocket_launch</span>
      </div>
      <p class="text-sm text-on-surface-variant italic">"Transformed our outbound."</p>
    </div>
    
    <!-- Card 4 -->
    <div class="p-6 rounded-2xl bg-surface-container-high border border-outline-variant/30 shadow-lg hover:-translate-y-1 transition-transform flex flex-col justify-center gap-2 translate-y-6 group">
      <span class="text-xs font-label-badge text-secondary uppercase font-bold tracking-wider">Enterprise</span>
      <span class="font-headline-sm text-on-surface font-semibold leading-tight group-hover:text-secondary transition-colors">Orange Tree</span>
      <div class="mt-2 w-full bg-outline-variant/30 rounded-full h-1.5 overflow-hidden">
        <div class="bg-secondary h-1.5 rounded-full w-[85%] relative overflow-hidden">
           <div class="absolute inset-0 bg-white/30 animate-pulse"></div>
        </div>
      </div>
    </div>
    
    <!-- Card 5 (Full Width Bottom) -->
    <div class="col-span-2 p-6 rounded-2xl bg-gradient-to-br from-surface-container to-surface-container-high border border-outline-variant/30 shadow-lg hover:-translate-y-1 transition-transform flex items-center justify-between mt-8 group">
      <div class="flex flex-col">
        <span class="font-headline-sm text-on-surface font-semibold leading-tight">Namrah Trading LLC</span>
        <span class="text-sm text-on-surface-variant flex items-center gap-1.5 mt-1">
            <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
            Consistent lead flow
        </span>
      </div>
      <div class="h-12 w-12 rounded-full bg-surface-container-lowest border border-outline-variant/30 flex items-center justify-center group-hover:scale-110 transition-transform shadow-inner">
        <span class="material-symbols-outlined text-primary text-2xl">handshake</span>
      </div>
    </div>
    
  </div>
</div>
"""

start_line = -1
end_line = -1

for i, line in enumerate(lines):
    if '<!-- Client Success Marquee Visual -->' in line:
        start_line = i
    if start_line != -1 and '<!-- THE WEDGE & STRICT QUALIFIERS -->' in line:
        end_line = i
        break

if start_line != -1 and end_line != -1:
    # </div>
    # </div>
    # </section>
    # <!-- THE WEDGE & STRICT QUALIFIERS -->
    # end_line points to <!-- THE WEDGE & STRICT QUALIFIERS -->
    
    # Let's verify what's right above end_line
    # it should be </div> </div> </section>
    
    # We replace from start_line to end_line-4
    
    # Wait, let's just use string replace on the whole file
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    start_str = '<!-- Client Success Marquee Visual -->'
    end_str = '</section>'
    
    idx1 = html.find(start_str)
    idx2 = html.find(end_str, idx1)
    
    if idx1 != -1 and idx2 != -1:
        # html[idx1:idx2] includes the marquee and then some closing divs
        # Let's just find the closing </div> of lg:col-span-5
        
        # We know the marquee is wrapped in exactly one <div class="lg:col-span-5 ..."> ... </div>
        # and ends right before the closing divs of the grid.
        
        # Let's slice out from start_str up to the last </div> before idx2.
        # Actually it's easier to just replace lines
        new_lines = lines[:start_line] + [new_html_block + '\n'] + lines[end_line-3:end_line] + lines[end_line:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
        print("Success")
    else:
        print("Could not find start or end strings")
