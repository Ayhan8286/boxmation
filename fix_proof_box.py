import codecs
from bs4 import BeautifulSoup

def fix_proof_box():
    filepath = 'd:/boxmation/index.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    old = '''<div class="inline-flex items-center gap-3 px-5 py-2.5 bg-green-50 border border-green-200 brutalist-border">
<span class="material-symbols-outlined text-green-600">trending_up</span>
<span class="text-sm text-green-800 font-medium tracking-wide">Recently generated <strong>$100k+ pipeline</strong> for a single client in 90 days.</span>
</div>'''

    new = '''<div class="border border-[#1e1e1e] brutalist-border bg-[#1e1e1e] text-left max-w-sm w-full">
<div class="flex items-center gap-2 px-4 py-2 border-b border-white/10">
    <span class="w-2.5 h-2.5 rounded-full bg-[var(--ts-pink)] inline-block"></span>
    <span class="w-2.5 h-2.5 rounded-full bg-[var(--ts-green)] inline-block"></span>
    <span class="w-2.5 h-2.5 rounded-full bg-white/20 inline-block"></span>
    <span class="font-mono text-xs text-white/30 ml-1">sys.proof.log</span>
</div>
<div class="px-4 py-4 font-mono text-xs leading-relaxed">
    <span class="text-[var(--ts-green)]">&gt;</span>
    <span class="text-white/50"> pipeline.generated(</span>
    <span class="text-[var(--ts-pink)] typewriter-proof">$100k+</span>
    <span class="text-white/50">)</span>
    <br/>
    <span class="text-[var(--ts-green)]">&gt;</span>
    <span class="text-white/60"> client_window: <span class="text-white">90 days</span></span>
    <br/>
    <span class="text-[var(--ts-green)]">&gt;</span>
    <span class="text-[var(--ts-green)]"> ✓ verified</span>
    <span class="animate-pulse text-[var(--ts-green)] ml-1">_</span>
</div>
</div>'''

    html = html.replace(old, new)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
    print("Done!")

if __name__ == '__main__':
    fix_proof_box()
