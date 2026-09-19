with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_block = """<!-- Client Success Visual (Stationary Grid) -->
<div class="lg:col-span-5 flex flex-col justify-center relative min-h-[500px] h-full hidden lg:flex p-6 rounded-2xl bg-surface-container-low/30 border border-outline-variant/10 overflow-hidden">
  <!-- Subtle background glow -->
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-primary-container/10 blur-[100px] rounded-full pointer-events-none"></div>
  
  <!-- Headline Badge -->
  <div class="text-center mb-8 relative z-10 w-full mt-4">
    <div class="inline-flex items-center justify-center px-6 py-3 rounded-2xl bg-primary-container/10 border border-primary/20 shadow-[0_0_30px_rgba(5,150,105,0.15)] backdrop-blur-md cursor-default">
      <span class="material-symbols-outlined text-primary mr-2 text-2xl">trending_up</span>
      <span class="font-headline-sm text-primary font-bold tracking-tight">
        $100k+ Pipeline Generated in 90 Days
      </span>
    </div>
  </div>

  <!-- B2B Cards Grid -->
  <div class="relative w-full grid grid-cols-2 gap-5 z-10 mb-4">
    
    <!-- Card 1 -->
    <div class="p-6 rounded-2xl bg-surface-container border border-outline-variant/30 shadow-lg flex flex-col justify-center gap-3">
      <span class="text-xs font-label-badge text-primary uppercase font-bold tracking-wider">B2B SaaS</span>
      <img src="exzellent.png" class="h-6 w-auto object-contain object-left filter brightness-0 invert opacity-90" alt="Exzellent.co">
      <div class="mt-1 flex items-center gap-1.5 text-on-surface-variant text-sm">
        <span class="material-symbols-outlined text-base text-[#25D366]">check_circle</span>
        <span>Qualified Meetings</span>
      </div>
    </div>
    
    <!-- Card 2 -->
    <div class="p-6 rounded-2xl bg-surface-container-high border border-outline-variant/30 shadow-lg flex flex-col justify-center gap-3 translate-y-6">
      <span class="text-xs font-label-badge text-tertiary uppercase font-bold tracking-wider">Consulting</span>
      <span class="font-headline-sm text-on-surface font-semibold leading-tight">Blackmont</span>
      <div class="mt-1 flex gap-0.5 text-yellow-500">
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
        <span class="material-symbols-outlined text-sm fill-current" style="font-variation-settings: 'FILL' 1">star</span>
      </div>
    </div>
    
    <!-- Card 3 -->
    <div class="p-6 rounded-2xl bg-surface-container border border-outline-variant/30 shadow-lg flex flex-col justify-center gap-3">
      <div class="flex items-start justify-between mb-1">
        <span class="font-headline-sm text-on-surface font-semibold leading-tight">Alhuda Network</span>
        <span class="material-symbols-outlined text-primary text-xl opacity-90">rocket_launch</span>
      </div>
      <p class="text-sm text-on-surface-variant italic">"Transformed our outbound."</p>
    </div>
    
    <!-- Card 4 -->
    <div class="p-6 rounded-2xl bg-surface-container-high border border-outline-variant/30 shadow-lg flex flex-col justify-center gap-3 translate-y-6">
      <span class="text-xs font-label-badge text-secondary uppercase font-bold tracking-wider">Enterprise</span>
      <img src="orange.png" class="h-10 w-auto object-contain object-left" alt="Orange Tree">
      <div class="mt-2 w-full bg-outline-variant/30 rounded-full h-1.5 overflow-hidden">
        <div class="bg-secondary h-1.5 rounded-full w-[85%] relative overflow-hidden">
           <div class="absolute inset-0 bg-white/30 animate-pulse"></div>
        </div>
      </div>
    </div>
    
    <!-- Card 5 (Full Width Bottom) -->
    <div class="col-span-2 p-6 rounded-2xl bg-gradient-to-br from-surface-container to-surface-container-high border border-outline-variant/30 shadow-lg flex items-center justify-between mt-8">
      <div class="flex flex-col gap-2">
        <img src="namrah.png" class="h-6 w-auto object-contain object-left filter brightness-0 invert opacity-90" alt="Namrah Trading LLC">
        <span class="text-sm text-on-surface-variant flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
            Consistent lead flow
        </span>
      </div>
      <div class="h-12 w-12 rounded-full bg-surface-container-lowest border border-outline-variant/30 flex items-center justify-center shadow-inner">
        <span class="material-symbols-outlined text-primary text-2xl">handshake</span>
      </div>
    </div>
    
  </div>
</div>
"""

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<!-- Client Success Visual (Stationary Grid) -->' in line:
        start_idx = i
    if start_idx != -1 and '<!-- THE WEDGE & STRICT QUALIFIERS -->' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    # the section we want to replace ends before the `</div>\n</div>\n</section>`
    # We replace from start_idx up to end_idx - 3
    lines[start_idx:end_idx-3] = [new_block + '\n']
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Success")
