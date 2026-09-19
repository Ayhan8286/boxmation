with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_html = """<div class="text-center max-w-3xl mx-auto mb-16">
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-surface-container-high font-label-badge text-label-badge text-primary uppercase mb-4">
          SYSTEM ONBOARDING SPRINT
        </div>
<h2 class="font-headline-lg text-headline-lg text-on-surface font-bold tracking-tight mb-4">
          14-Day Delivery Timeline
        </h2>
<p class="font-body-md text-body-md text-on-surface-variant">
          No vague multi-month "discovery phases." A fixed, day-by-day build.
        </p>
</div>
<!-- Timeline Progress Graphic -->
<div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-16">
<!-- Milestone 1 -->
<div class="bg-surface-container-low p-6 rounded-xl relative shadow-md">
<div class="flex items-center justify-between mb-4">
<span class="font-label-badge text-label-badge text-primary font-bold">DAYS 01–04</span>
<span class="font-label-code text-label-code text-outline">SPRINT 1</span>
</div>
<h3 class="font-headline-sm text-headline-sm text-on-surface font-bold mb-2">Foundation</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">
            Sending infrastructure set up and warming, target list built and enriched with verified contact data.
          </p>
</div>
<!-- Milestone 2 -->
<div class="bg-surface-container-low p-6 rounded-xl relative shadow-md">
<div class="flex items-center justify-between mb-4">
<span class="font-label-badge text-label-badge text-primary font-bold">DAYS 05–09</span>
<span class="font-label-code text-label-code text-outline">SPRINT 2</span>
</div>
<h3 class="font-headline-sm text-headline-sm text-on-surface font-bold mb-2">Messaging</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">
            Email and LinkedIn sequences written, reviewed, and approved with you.
          </p>
</div>
<!-- Milestone 3 -->
<div class="bg-surface-container-low p-6 rounded-xl relative shadow-md">
<div class="flex items-center justify-between mb-4">
<span class="font-label-badge text-label-badge text-primary font-bold">DAYS 10–13</span>
<span class="font-label-code text-label-code text-outline">SPRINT 3</span>
</div>
<h3 class="font-headline-sm text-headline-sm text-on-surface font-bold mb-2">Connect &amp; Test</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">
            Everything routed into your CRM, tested end-to-end before anything goes live.
          </p>
</div>
<!-- Milestone 4 -->
<div class="bg-surface-container-low p-6 rounded-xl relative shadow-md">
<div class="flex items-center justify-between mb-4">
<span class="font-label-badge text-label-badge text-primary font-bold">DAY 14</span>
<span class="font-label-code text-label-code text-primary font-bold">DEPLOY</span>
</div>
<h3 class="font-headline-sm text-headline-sm text-on-surface font-bold mb-2">Live</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">
            Outbound running across email and LinkedIn. Reporting dashboard active.
          </p>
</div>
</div>
<!-- Explicit Milestone Guarantee Box -->
<div class="max-w-4xl mx-auto p-8 rounded-2xl bg-surface-container shadow-2xl">
<div class="flex flex-col sm:flex-row items-start sm:items-center gap-6">
<div class="p-4 rounded-xl bg-primary-container text-on-primary-container flex-shrink-0">
<span class="material-symbols-outlined text-display-mobile">gavel</span>
</div>
<div>
<span class="font-label-badge text-label-badge text-primary uppercase font-bold tracking-wider">THE BOXMATION COMMITMENT</span>
<h3 class="font-headline-md text-headline-md text-on-surface font-bold mt-1 mb-2">
              Launch-ready in 14 days.
            </h3>
<p class="font-body-md text-body-md text-on-surface-variant">
              If your system isn't built, tested, and live by day 14 &mdash; through a delay on our side &mdash; we extend the build at no additional cost until it is. This is a commitment to our timeline, not a promise about how fast you'll get meetings once it's running; those depend on your market and offer too, which we don't control.
            </p>
</div>
</div>
</div>
"""

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<div class="text-center max-w-3xl mx-auto mb-16">' in line and 'SYSTEM ONBOARDING SPRINT' in ''.join(lines[i:i+4]):
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if '<!-- FINAL HIGH-CONVERSION CTA & DISCOVERY CALL SECTION -->' in lines[i]:
        end_idx = i - 3 # lines[i-1] is </section>, lines[i-2] is </div>, lines[i-3] is </div>
        break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx]
    lines.insert(start_idx, new_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Success")
else:
    print(f"Failed to find indices. Start: {start_idx}, End: {end_idx}")
