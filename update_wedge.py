with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

replacement_html = """<div class="lg:col-span-5">
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-surface-container-high font-label-badge text-label-badge text-primary uppercase mb-6">
            WHO WE WORK WITH (AND WHO WE DECLINE)
          </div>
<h2 class="font-headline-lg text-headline-lg text-on-surface font-bold tracking-tight mb-6">
            The One Wedge: Founder-Led B2B Agencies
          </h2>
<p class="font-body-md text-body-md text-on-surface-variant mb-6">
            We don't work with pre-revenue businesses, unproven offers, or companies without a real sales motion. We built this system for one specific buyer — founder-led agencies ready to handle more pipeline than they currently have a system for.
          </p>
<div class="p-4 rounded-xl bg-surface-container-low shadow-sm">
<span class="font-label-badge text-label-badge text-secondary font-bold uppercase block mb-1">FOUNDER POLICY</span>
<p class="font-body-sm text-body-sm text-on-surface-variant">
              If you don't meet these criteria, we'll say so on the call rather than waste your time or ours.
            </p>
</div>
</div>
<!-- 7 Qualifiers vs Disqualifiers Cards -->
<div class="lg:col-span-7 space-y-6">
<!-- The Qualifiers -->
<div class="bg-surface-container-low rounded-xl p-6 shadow-md">
<div class="flex items-center gap-2 mb-4">
<span class="material-symbols-outlined text-primary">verified_user</span>
<h3 class="font-headline-sm text-headline-sm text-on-surface font-bold">The Qualifiers</h3>
</div>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 font-body-sm text-body-sm">
<div class="p-3 rounded-lg bg-surface-container flex items-center gap-2 text-on-surface">
<span class="material-symbols-outlined text-primary text-body-md">check</span>
<span>$100K–$300K/mo revenue</span>
</div>
<div class="p-3 rounded-lg bg-surface-container flex items-center gap-2 text-on-surface">
<span class="material-symbols-outlined text-primary text-body-md">check</span>
<span>5–15 team members</span>
</div>
<div class="p-3 rounded-lg bg-surface-container flex items-center gap-2 text-on-surface">
<span class="material-symbols-outlined text-primary text-body-md">check</span>
<span>Founder-owned, bootstrapped or light-touch VC</span>
</div>
<div class="p-3 rounded-lg bg-surface-container flex items-center gap-2 text-on-surface">
<span class="material-symbols-outlined text-primary text-body-md">check</span>
<span>Profitable or near-profitable, actively hiring</span>
</div>
<div class="p-3 rounded-lg bg-surface-container flex items-center gap-2 text-on-surface">
<span class="material-symbols-outlined text-primary text-body-md">check</span>
<span>An existing, proven offer already selling</span>
</div>
<div class="p-3 rounded-lg bg-surface-container flex items-center gap-2 text-on-surface">
<span class="material-symbols-outlined text-primary text-body-md">check</span>
<span>Someone in-house who can close a booked meeting</span>
</div>
<div class="p-3 rounded-lg bg-surface-container flex items-center gap-2 text-on-surface col-span-1 sm:col-span-2">
<span class="material-symbols-outlined text-primary text-body-md">check</span>
<span>Ready to grant CRM access and respond within 48 hours</span>
</div>
</div>
</div>
<!-- Immediate Disqualifiers -->
<div class="bg-surface-container-low rounded-xl p-6 shadow-md">
<div class="flex items-center gap-2 mb-4">
<span class="material-symbols-outlined text-error">cancel</span>
<h3 class="font-headline-sm text-headline-sm text-on-surface font-bold">Immediate Disqualifiers</h3>
</div>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 font-body-sm text-body-sm text-outline">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-error text-body-md">close</span>
<span>No proven offer yet</span>
</div>
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-error text-body-md">close</span>
<span>No one available to close a booked meeting</span>
</div>
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-error text-body-md">close</span>
<span>Recent layoffs, funding crunch, or hiring freeze</span>
</div>
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-error text-body-md">close</span>
<span>Wants a guaranteed revenue number before starting</span>
</div>
<div class="flex items-center gap-2 col-span-1 sm:col-span-2">
<span class="material-symbols-outlined text-error text-body-md">close</span>
<span>Leads by negotiating free work before seeing the offer</span>
</div>
</div>
</div>
</div>
"""

# Replace lines 354 to 437 (0-indexed 354 to 437) -> lines[354:438]
# Actually, I'll dynamically find the indices.

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div class="lg:col-span-5">' in line and 'WHO WE WORK WITH' in lines[i+2]:
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if '<!-- 14-DAY DELIVERY TIMELINE & MILESTONE GUARANTEE -->' in lines[i]:
        # go back to the closing div of the grid
        # lines[i-1] is </section>
        # lines[i-2] is </div>
        # lines[i-3] is </div>
        # lines[i-4] is </div>
        # lines[i-5] is </div>
        end_idx = i - 4 # The closing tag of lg:col-span-7
        break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx+1]
    lines.insert(start_idx, replacement_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Success")
else:
    print(f"Failed to find indices. Start: {start_idx}, End: {end_idx}")
