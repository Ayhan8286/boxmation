with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_html = """<!-- FINAL HIGH-CONVERSION CTA & DISCOVERY CALL SECTION -->
<section class="w-full py-24 bg-background relative overflow-hidden" id="book-discovery">
<div class="absolute inset-0 pointer-events-none opacity-15 [background-image:radial-gradient(#2563eb_1px,transparent_1px)] [background-size:24px_24px]"></div>
<div class="max-w-[1240px] mx-auto px-6 lg:px-8 relative">
<div class="max-w-6xl mx-auto bg-surface-container-low rounded-3xl p-8 sm:p-12 shadow-2xl">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">

<!-- Text & Requirements Column -->
<div>
<div class="mb-8">
<span class="font-label-badge text-label-badge text-primary uppercase font-bold tracking-wider">READY TO TALK?</span>
<h2 class="font-display text-headline-lg md:text-display text-on-surface font-bold tracking-tight mt-2 mb-4">
            Book a Call
          </h2>
<p class="font-body-md text-body-md text-on-surface-variant">
            25 minutes. We'll look at who you're targeting, whether it's a fit, and if it is, walk through exactly how the 14-day build works.
          </p>
</div>

<div class="bg-surface-container rounded-2xl p-6 sm:p-8 shadow-inner">
<h3 class="font-headline-sm text-headline-sm text-on-surface font-semibold mb-4">Before You Book</h3>
<div class="space-y-3 font-body-sm text-body-sm text-on-surface-variant mb-6">
<div class="flex items-start gap-2.5">
<span class="material-symbols-outlined text-primary text-body-md mt-0.5">check_circle</span>
<span>You're the founder or the person who owns this decision</span>
</div>
<div class="flex items-start gap-2.5">
<span class="material-symbols-outlined text-primary text-body-md mt-0.5">check_circle</span>
<span>Revenue is roughly $100K–$300K/month</span>
</div>
<div class="flex items-start gap-2.5">
<span class="material-symbols-outlined text-primary text-body-md mt-0.5">check_circle</span>
<span>You're ready to start within 30 days if it's a fit</span>
</div>
</div>
<div class="flex items-center gap-3 pt-4 border-t border-outline-variant/30">
<img alt="Founder" class="w-10 h-10 rounded-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDj5Tv2ppvjJcc3MrowN44j_I3y_vOnnI4C1-Ny6Zm8EA51HQItDwCRajmqLM0c-V3gAlRxBsG3sFy5v656WUMZcJAa0b4NlKJ6eDNYHfUIFvzPfrjHDHXanzXLLkRkjDBbkr1pc1_-p4afWQLAEQHlQyhvzYE9m1GQyFheWtm7_BGEvkXLGLNf2b6H-dc978_-tIODHaIH2zy7RWjkfNuWesvQqlD5Q61Tx3SZ7r6SiLifxRKq0CEvAWwWA_49LelK"/>
<div>
<span class="font-headline-sm text-body-md text-on-surface font-bold block leading-none">25-minute call</span>
<span class="font-body-sm text-body-sm text-outline">direct with the founder</span>
</div>
</div>
</div>
</div>

<!-- Calendly Embed Column -->
<div class="bg-surface-container-high rounded-xl shadow-lg h-[650px] overflow-hidden">
<!-- Calendly inline widget begin -->
<div class="calendly-inline-widget" data-url="https://calendly.com/your-booking-link" style="min-width:320px;height:100%;width:100%;"></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
<!-- Calendly inline widget end -->
</div>

</div>
</div>
</div>
</section>
"""

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<!-- FINAL HIGH-CONVERSION CTA & DISCOVERY CALL SECTION -->' in line:
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if '</script>' in line and 'Interactive JavaScript for button selection micro-interactions' in ''.join(lines[start_idx:i]):
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx+1]
    lines.insert(start_idx, new_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Success")
else:
    print(f"Failed to find indices. Start: {start_idx}, End: {end_idx}")
