with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full bg-surface-container font-label-badge text-label-badge text-primary uppercase">ENGINEERING</span>', '')

html = html.replace('<span class="font-label-badge text-label-badge px-2 py-0.5 rounded-full bg-surface-container-high text-primary">B2B PIPELINE</span>', '')

html = html.replace('<div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span><span>OUTBOUND INFRASTRUCTURE LIVE</span></div>', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
