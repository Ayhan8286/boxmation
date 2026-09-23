import codecs
from bs4 import BeautifulSoup

NEW_SECTION = """
<!-- HOW IT WORKS SECTION -->
<section class="w-full py-24 border-t border-[#1e1e1e] bg-white relative">
    <div class="max-w-[1240px] mx-auto px-6 lg:px-8">

        <!-- Section Label -->
        <div class="mb-20 reveal">
            <span class="font-mono text-xs font-bold uppercase tracking-[0.2em] text-gray-400 border border-[#1e1e1e] px-3 py-1 brutalist-border">// sys.process.init</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">

            <!-- Left: Big Statement -->
            <div class="reveal">
                <h2 class="font-display text-4xl md:text-5xl font-extrabold tracking-tighter leading-[1.1] uppercase mb-8">
                    Most agencies<br/>
                    <span class="bg-[var(--ts-pink)] text-[var(--ts-dark)] px-2">disappear</span><br/>
                    after the sale.
                </h2>
                <p class="text-gray-600 text-lg leading-relaxed mb-8">
                    We stay in the terminal. Every pipeline we build runs under one rule: if it breaks, we fix it. If the market shifts, we adapt it. You get a system that compounds — not a project that ends.
                </p>
                <a href="/pricing.html" class="inline-flex items-center gap-2 font-semibold text-sm uppercase tracking-wider border border-[#1e1e1e] px-6 py-3 brutalist-border brutalist-button hover:bg-[#1e1e1e] hover:text-white transition-colors">
                    See What You Get
                    <span class="material-symbols-outlined text-sm">arrow_forward</span>
                </a>
            </div>

            <!-- Right: The 3 steps -->
            <div class="flex flex-col gap-0 reveal">

                <div class="border border-[#1e1e1e] p-8 brutalist-border flex gap-6 items-start hover:bg-[#fafafa] transition-colors">
                    <span class="font-mono text-4xl font-black text-[var(--ts-pink)] leading-none select-none flex-shrink-0">01</span>
                    <div>
                        <h3 class="font-display text-xl font-bold uppercase tracking-tight mb-2">The Audit</h3>
                        <p class="text-gray-500 text-sm leading-relaxed">We map your outbound motion in 25 minutes. ICP, offer, sequencing — everything that's working, everything that's leaking money.</p>
                    </div>
                </div>

                <div class="border border-[#1e1e1e] border-t-0 p-8 brutalist-border flex gap-6 items-start hover:bg-[#fafafa] transition-colors">
                    <span class="font-mono text-4xl font-black text-[var(--ts-green)] leading-none select-none flex-shrink-0">02</span>
                    <div>
                        <h3 class="font-display text-xl font-bold uppercase tracking-tight mb-2">The Build</h3>
                        <p class="text-gray-500 text-sm leading-relaxed">14 days. Full AI outbound infrastructure — lead sourcing, enrichment, personalised copy, delivery, reply handling. Built around your business, not a template.</p>
                    </div>
                </div>

                <div class="border border-[#1e1e1e] border-t-0 p-8 brutalist-border flex gap-6 items-start hover:bg-[#fafafa] transition-colors">
                    <span class="font-mono text-4xl font-black text-[var(--ts-dark)] leading-none select-none flex-shrink-0">03</span>
                    <div>
                        <h3 class="font-display text-xl font-bold uppercase tracking-tight mb-2">The Output</h3>
                        <p class="text-gray-500 text-sm leading-relaxed">Qualified meetings in your calendar. Not traffic. Not leads. Conversations with buyers who already know your offer before they pick up the phone.</p>
                    </div>
                </div>

            </div>
        </div>
    </div>
</section>

<!-- NUMBERS SECTION -->
<section class="w-full border-t border-[#1e1e1e] bg-[#1e1e1e] text-white relative">
    <div class="max-w-[1240px] mx-auto px-6 lg:px-8">
        <div class="grid grid-cols-1 sm:grid-cols-3 divide-y sm:divide-y-0 sm:divide-x divide-white/10">

            <div class="py-16 px-8 reveal text-center">
                <div class="font-display text-6xl font-black text-[var(--ts-pink)] mb-3">14</div>
                <div class="font-mono text-xs uppercase tracking-[0.2em] text-gray-400 mb-2">Days to Launch</div>
                <p class="text-gray-500 text-sm">From zero to a live, sending pipeline. No six-week onboarding. No waiting.</p>
            </div>

            <div class="py-16 px-8 reveal text-center">
                <div class="font-display text-6xl font-black text-[var(--ts-green)] mb-3">1</div>
                <div class="font-mono text-xs uppercase tracking-[0.2em] text-gray-400 mb-2">System. Not a Service.</div>
                <p class="text-gray-500 text-sm">You own the infrastructure. We build it, you keep it. No monthly retainer lock-in.</p>
            </div>

            <div class="py-16 px-8 reveal text-center">
                <div class="font-display text-6xl font-black text-white mb-3">∞</div>
                <div class="font-mono text-xs uppercase tracking-[0.2em] text-gray-400 mb-2">Scalable Outreach</div>
                <p class="text-gray-500 text-sm">The pipeline runs 24/7. Prospects enriched, emails sent, replies handled — while you sleep.</p>
            </div>

        </div>
    </div>
</section>
"""

def add_sections():
    filepath = 'd:/boxmation/index.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    main = soup.find('main')
    sections = main.find_all('section', recursive=False)

    # Insert BEFORE the guarantee section (second section)
    guarantee_section = None
    for s in sections:
        if s.get('id') == 'guarantee':
            guarantee_section = s
            break

    if guarantee_section:
        new_soup = BeautifulSoup(NEW_SECTION, 'html.parser')
        for tag in reversed(list(new_soup.children)):
            if tag.name:
                guarantee_section.insert_before(tag)
        print("Inserted new sections before guarantee!")
    else:
        print("Could not find guarantee section!")

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    add_sections()
