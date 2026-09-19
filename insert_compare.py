with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_section = """<!-- COMPARE VS IN-HOUSE -->
<section class="w-full py-24 bg-surface-container relative" id="compare-vs-in-house">
  <div class="max-w-[1000px] mx-auto px-6 lg:px-8">
    
    <div class="text-center mb-16">
      <span class="text-primary font-label-code uppercase tracking-wider mb-4 block">The Math</span>
      <h2 class="font-headline-lg text-display-mobile lg:text-headline-lg text-on-surface font-bold tracking-tight mb-4">
        BoxMation vs. In-House SDR
      </h2>
      <p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto">
        Why pay $80k+/year for an unproven SDR when you can plug into a fully engineered outbound system?
      </p>
    </div>

    <div class="grid md:grid-cols-2 gap-8 relative">
      <!-- VS Badge -->
      <div class="hidden md:flex absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-10 w-12 h-12 rounded-full bg-surface-container-highest border-4 border-surface-container items-center justify-center font-bold text-on-surface">
        VS
      </div>

      <!-- In-House -->
      <div class="p-8 rounded-3xl bg-surface-container-low border border-outline-variant/30 flex flex-col gap-6 opacity-90 hover:opacity-100 transition-opacity">
        <div class="flex items-center gap-4 mb-2">
          <div class="w-12 h-12 rounded-xl bg-error-container/20 flex items-center justify-center">
            <span class="material-symbols-outlined text-error">person_off</span>
          </div>
          <div>
            <h3 class="font-headline-sm text-on-surface font-semibold">In-House SDR</h3>
            <p class="text-sm text-error font-medium">$8,000+ / month (fully loaded)</p>
          </div>
        </div>
        
        <ul class="space-y-4 font-body-md text-on-surface-variant">
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-error mt-0.5 text-xl">close</span>
            <span>Takes 3-4 months just to ramp up and learn your product.</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-error mt-0.5 text-xl">close</span>
            <span>Requires constant management, motivation, and training.</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-error mt-0.5 text-xl">close</span>
            <span>Limited to ~50-100 manual emails/calls per day.</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-error mt-0.5 text-xl">close</span>
            <span>High turnover risk (average SDR tenure is 14 months).</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-error mt-0.5 text-xl">close</span>
            <span>You still have to buy all the software tools and data.</span>
          </li>
        </ul>
      </div>

      <!-- BoxMation -->
      <div class="p-8 rounded-3xl bg-primary-container/10 border border-primary/30 shadow-[0_0_40px_rgba(5,150,105,0.15)] flex flex-col gap-6 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-32 h-32 bg-primary/20 blur-[50px] rounded-full pointer-events-none"></div>
        
        <div class="flex items-center gap-4 mb-2 relative z-10">
          <div class="w-12 h-12 rounded-xl bg-primary-container text-on-primary-container flex items-center justify-center shadow-lg">
            <span class="material-symbols-outlined">rocket_launch</span>
          </div>
          <div>
            <h3 class="font-headline-sm text-primary font-semibold">BoxMation System</h3>
            <p class="text-sm text-primary font-medium">Fraction of the cost. 10x the output.</p>
          </div>
        </div>
        
        <ul class="space-y-4 font-body-md text-on-surface relative z-10">
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-primary mt-0.5 text-xl">check_circle</span>
            <span><strong>Live in 14 days.</strong> No ramping, no training, no hand-holding.</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-primary mt-0.5 text-xl">check_circle</span>
            <span><strong>Infinite scale.</strong> Send thousands of highly-personalized emails daily.</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-primary mt-0.5 text-xl">check_circle</span>
            <span><strong>Fully managed.</strong> We handle the infrastructure, domains, and deliverability.</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-primary mt-0.5 text-xl">check_circle</span>
            <span><strong>Expert copywriting.</strong> Messaging constantly tested and optimized by us.</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-primary mt-0.5 text-xl">check_circle</span>
            <span><strong>Zero tool stack costs.</strong> Data, software, and sending tools are all included.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

insert_idx = -1
for i, line in enumerate(lines):
    if 'id="guarantee"' in line and '<section' in line:
        insert_idx = i
        break

if insert_idx != -1:
    lines.insert(insert_idx, new_section + '\n')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Inserted successfully')
else:
    print('Could not find guarantee section to insert before')
