with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """<span class="material-symbols-outlined text-outline">south</span>
</a>
</div>"""

replacement = """<span class="material-symbols-outlined text-outline">south</span>
</a>
</div>

<!-- Performance Proof Badge -->
<div class="inline-flex items-center gap-3 mt-4 px-4 py-2 rounded-full bg-surface-container-low border border-outline-variant/30 shadow-sm">
  <span class="material-symbols-outlined text-primary text-body-lg">trending_up</span>
  <span class="font-body-sm text-on-surface-variant font-medium tracking-wide">Recently generated <strong class="text-on-surface">$100k+ pipeline</strong> for a single client in 90 days.</span>
</div>"""

if target in text:
    new_text = text.replace(target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Added proof badge!")
else:
    print("Target not found")
