with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_html = """<!-- Client Success Marquee Visual -->
<div class="lg:col-span-5 flex flex-col justify-center relative min-h-[500px] h-full hidden lg:flex overflow-hidden rounded-2xl bg-surface-container-low/50">
  <div class="absolute inset-0 bg-primary-container/5 blur-[100px] rounded-full pointer-events-none"></div>
  
  <div class="text-center mb-10 relative z-10 px-6">
    <div class="inline-flex items-center justify-center px-5 py-3 rounded-2xl bg-primary-container/10 border border-primary/20 shadow-[0_0_30px_rgba(37,99,235,0.15)] backdrop-blur-md">
      <span class="material-symbols-outlined text-primary mr-2">trending_up</span>
      <span class="font-headline-sm text-primary font-bold tracking-tight">
        $100k+ Pipeline Generated in 90 Days
      </span>
    </div>
  </div>

  <style>
    @keyframes marquee-rtl {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }
    @keyframes marquee-ltr {
      0% { transform: translateX(-50%); }
      100% { transform: translateX(0); }
    }
    .animate-marquee-rtl {
      animation: marquee-rtl 25s linear infinite;
    }
    .animate-marquee-ltr {
      animation: marquee-ltr 25s linear infinite;
    }
    .marquee-fade-edges {
      mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
      -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
    }
  </style>

  <div class="relative w-full flex flex-col gap-5 marquee-fade-edges py-2">
    <!-- Row 1: Right to Left -->
    <div class="flex gap-4 animate-marquee-rtl w-max hover:[animation-play-state:paused]">
      <!-- Set 1 -->
      <div class="flex items-center gap-4">
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Exzellent.co</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Alhuda Network</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Orange Tree Systems</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Blackmont Consulting</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Namrah Trading LLC</span>
        </div>
      </div>
      <!-- Set 2 (Duplicate for loop) -->
      <div class="flex items-center gap-4">
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Exzellent.co</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Alhuda Network</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Orange Tree Systems</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Blackmont Consulting</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Namrah Trading LLC</span>
        </div>
      </div>
    </div>
    
    <!-- Row 2: Left to Right -->
    <div class="flex gap-4 animate-marquee-ltr w-max hover:[animation-play-state:paused]">
      <!-- Set 1 (Shuffled) -->
      <div class="flex items-center gap-4">
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Blackmont Consulting</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Exzellent.co</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Namrah Trading LLC</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Alhuda Network</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Orange Tree Systems</span>
        </div>
      </div>
      <!-- Set 2 (Shuffled Duplicate) -->
      <div class="flex items-center gap-4">
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Blackmont Consulting</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Exzellent.co</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Namrah Trading LLC</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Alhuda Network</span>
        </div>
        <div class="px-6 py-3 rounded-xl bg-surface-container border border-outline-variant/30 shadow-lg flex items-center justify-center whitespace-nowrap hover:-translate-y-1 transition-transform cursor-default">
          <span class="font-headline-sm text-on-surface font-semibold">Orange Tree Systems</span>
        </div>
      </div>
    </div>
  </div>
</div>
"""

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<!-- Abstract Artistic Visual -->' in line:
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if '<!-- COMPARISON MATRIX: IN-HOUSE VS FREELANCER VS BOXMATION -->' in line:
        # We need to backtrack to the closing divs of the previous section, specifically closing the grid and the container.
        # Actually, let's just find the end of the artistic visual div. It ends right before the closing tags of the section.
        pass

# The artistic visual is at 171. The section closes at 215. So the visual ends around 212.
if start_idx != -1:
    for i in range(start_idx, len(lines)):
        if '<!-- COMPARISON MATRIX: IN-HOUSE VS FREELANCER VS BOXMATION -->' in lines[i]:
            # The closing tags are usually:
            # 212: </div>
            # 213: </div>
            # 214: </div>
            # 215: </section>
            end_idx = i - 5
            break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx+1]
    lines.insert(start_idx, new_html + '\n')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Success")
else:
    print(f"Failed to find indices. Start: {start_idx}, End: {end_idx}")
