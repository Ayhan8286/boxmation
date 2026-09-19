with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<div class="lg:col-span-10 lg:col-start-2 bg-surface-container-low' in line:
        lines[i] = line.replace('lg:col-span-10 lg:col-start-2', 'lg:col-span-7')
        break

art_html = '''<!-- Abstract Artistic Visual -->
<div class="lg:col-span-5 flex items-center justify-center relative min-h-[500px] h-full hidden lg:flex">
  <!-- Background Glows -->
  <div class="absolute inset-0 bg-primary-container/10 blur-[100px] rounded-full pointer-events-none"></div>
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-tertiary-container/20 blur-[80px] rounded-full pointer-events-none"></div>
  
  <!-- Geometric Tech Elements -->
  <div class="relative w-full h-full max-w-sm mx-auto flex flex-col items-center justify-center gap-10">
    <!-- Connecting Dashed Line -->
    <div class="absolute top-10 bottom-10 left-1/2 -translate-x-1/2 w-px border-l-2 border-dashed border-primary/30 z-0"></div>
    
    <!-- Box 1 -->
    <div class="relative z-10 w-56 h-32 rounded-2xl bg-surface-container border border-outline-variant/30 shadow-2xl flex flex-col items-center justify-center overflow-hidden group transform -translate-x-8 hover:-translate-y-1 transition-transform">
      <div class="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
      <span class="material-symbols-outlined text-primary text-headline-lg mb-2">hub</span>
      <span class="font-label-code text-label-code text-on-surface-variant uppercase tracking-widest">Pipeline Active</span>
    </div>

    <!-- Box 2 (Highlight) -->
    <div class="relative z-10 w-64 h-36 rounded-2xl bg-surface-container-high border border-primary/40 shadow-[0_0_40px_rgba(37,99,235,0.25)] flex flex-col items-center justify-center overflow-hidden transform translate-x-8 scale-105">
      <div class="absolute inset-0 bg-gradient-to-tr from-secondary/15 to-transparent"></div>
      <div class="absolute top-3 right-3 flex items-center gap-1">
          <span class="animate-ping absolute inline-flex h-2 w-2 rounded-full bg-primary opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-primary"></span>
      </div>
      <span class="material-symbols-outlined text-primary text-display-mobile mb-2">rocket_launch</span>
      <span class="font-label-code text-label-code text-primary uppercase font-bold tracking-widest">System Routing</span>
    </div>

    <!-- Box 3 -->
    <div class="relative z-10 w-56 h-32 rounded-2xl bg-surface-container border border-outline-variant/30 shadow-2xl flex flex-col items-center justify-center overflow-hidden group transform -translate-x-4 hover:-translate-y-1 transition-transform">
      <div class="absolute inset-0 bg-gradient-to-tl from-tertiary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
      <span class="material-symbols-outlined text-secondary text-headline-lg mb-2">insights</span>
      <span class="font-label-code text-label-code text-on-surface-variant uppercase tracking-widest">Optimization</span>
    </div>
    
    <!-- Floating micro elements -->
    <div class="absolute top-1/4 left-4 w-3 h-3 rounded-sm bg-tertiary-container animate-pulse"></div>
    <div class="absolute bottom-1/4 right-8 w-2 h-2 rounded-full bg-secondary animate-ping"></div>
    <div class="absolute top-1/2 -left-2 w-4 h-1 rounded-full bg-primary-container opacity-50"></div>
  </div>
</div>
'''

for i in range(len(lines)):
    if 'Lock In 14-Day Outbound Implementation' in lines[i]:
        insert_idx = i + 3
        lines.insert(insert_idx, art_html)
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
