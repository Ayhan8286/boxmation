import codecs
from bs4 import BeautifulSoup

CLAY_SECTION = """
<!-- CLAY TABLE SECTION -->
<section class="w-full border-t border-[#1e1e1e] bg-white relative overflow-hidden">

    <!-- Top label bar -->
    <div class="w-full border-b border-[#1e1e1e] px-6 lg:px-8 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <span class="w-2 h-2 rounded-full bg-[var(--ts-pink)] animate-pulse"></span>
            <span class="font-mono text-xs text-gray-400 uppercase tracking-[0.2em]">// sys.pipeline.live — leads enriched &amp; ready</span>
        </div>
        <span class="font-mono text-xs text-gray-300 hidden sm:block">clay.table — sample output</span>
    </div>

    <div class="max-w-[1240px] mx-auto px-6 lg:px-8 py-20">

        <div class="reveal mb-12">
            <h2 class="font-display text-4xl md:text-5xl font-extrabold tracking-tighter leading-[1.1] uppercase mb-4">
                This is what your<br/>
                <span class="bg-[var(--ts-green)] text-white px-2">pipeline looks like</span><br/>
                on day 14.
            </h2>
            <p class="text-gray-500 text-sm max-w-xl mt-6 leading-relaxed">Every lead researched, verified, and personalised before a single email goes out. No spray and pray. No bought lists. Just precision targeting — powered by Clay and our AI layer on top.</p>
        </div>

        <!-- Clay table mock -->
        <div class="border border-[#1e1e1e] brutalist-border overflow-x-auto reveal">

            <!-- Table header -->
            <div class="bg-[#1e1e1e] text-white font-mono text-xs flex items-center gap-4 px-4 py-3 border-b border-white/10">
                <span class="text-[var(--ts-green)]">●</span>
                <span class="text-white/50">boxmation.pipeline</span>
                <span class="text-white/20 mx-2">|</span>
                <span class="text-white/50">leads: <span class="text-white">2,847</span></span>
                <span class="text-white/20 mx-2">|</span>
                <span class="text-white/50">enriched: <span class="text-[var(--ts-green)]">2,841</span></span>
                <span class="text-white/20 mx-2">|</span>
                <span class="text-white/50">sent: <span class="text-[var(--ts-pink)]">1,204</span></span>
                <span class="text-white/20 mx-2">|</span>
                <span class="text-white/50">meetings: <span class="text-white font-bold">31</span></span>
            </div>

            <!-- Column headers -->
            <div class="grid bg-[#fafafa] border-b border-[#1e1e1e] font-mono text-xs text-gray-400 uppercase tracking-wider" style="grid-template-columns: 2fr 2fr 2fr 1.5fr 1.5fr 2fr 1.5fr;">
                <div class="px-4 py-3 border-r border-[#1e1e1e]">Company</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">Contact</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">Title</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">Email</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">Verified</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">AI Personalisation</div>
                <div class="px-4 py-3">Status</div>
            </div>

            <!-- Row 1 -->
            <div class="grid border-b border-[#1e1e1e] text-xs hover:bg-[#fafafa] transition-colors" style="grid-template-columns: 2fr 2fr 2fr 1.5fr 1.5fr 2fr 1.5fr;">
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-medium flex items-center gap-2">
                    <div class="w-6 h-6 bg-blue-100 border border-[#1e1e1e] flex items-center justify-center text-blue-700 font-bold text-xs flex-shrink-0">S</div>
                    Synapse Labs
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-700">Marcus Chen</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-500 font-mono text-xs">VP of Growth</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-mono text-xs text-gray-400">m.chen@syn***</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">
                    <span class="bg-green-50 text-green-700 border border-green-200 px-2 py-0.5 font-mono text-xs brutalist-border">✓ valid</span>
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-600 text-xs italic">"Saw your Series A — congrats on the..."</div>
                <div class="px-4 py-3">
                    <span class="bg-[var(--ts-pink)] text-white px-2 py-0.5 font-mono text-xs">replied</span>
                </div>
            </div>

            <!-- Row 2 -->
            <div class="grid border-b border-[#1e1e1e] text-xs hover:bg-[#fafafa] transition-colors" style="grid-template-columns: 2fr 2fr 2fr 1.5fr 1.5fr 2fr 1.5fr;">
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-medium flex items-center gap-2">
                    <div class="w-6 h-6 bg-orange-100 border border-[#1e1e1e] flex items-center justify-center text-orange-700 font-bold text-xs flex-shrink-0">A</div>
                    Apex Digital
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-700">Sarah Okafor</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-500 font-mono text-xs">Head of Revenue</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-mono text-xs text-gray-400">s.okafor@ape***</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">
                    <span class="bg-green-50 text-green-700 border border-green-200 px-2 py-0.5 font-mono text-xs brutalist-border">✓ valid</span>
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-600 text-xs italic">"Your LinkedIn post on pipeline decay..."</div>
                <div class="px-4 py-3">
                    <span class="bg-[var(--ts-green)] text-white px-2 py-0.5 font-mono text-xs">meeting</span>
                </div>
            </div>

            <!-- Row 3 -->
            <div class="grid border-b border-[#1e1e1e] text-xs hover:bg-[#fafafa] transition-colors" style="grid-template-columns: 2fr 2fr 2fr 1.5fr 1.5fr 2fr 1.5fr;">
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-medium flex items-center gap-2">
                    <div class="w-6 h-6 bg-purple-100 border border-[#1e1e1e] flex items-center justify-center text-purple-700 font-bold text-xs flex-shrink-0">N</div>
                    NorthStack Inc
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-700">James Whitfield</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-500 font-mono text-xs">Founder / CEO</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-mono text-xs text-gray-400">j.whitfield@nor***</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">
                    <span class="bg-green-50 text-green-700 border border-green-200 px-2 py-0.5 font-mono text-xs brutalist-border">✓ valid</span>
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-600 text-xs italic">"Noticed you just hired two AEs — the..."</div>
                <div class="px-4 py-3">
                    <span class="bg-yellow-50 text-yellow-800 border border-yellow-200 px-2 py-0.5 font-mono text-xs brutalist-border">follow-up</span>
                </div>
            </div>

            <!-- Row 4 -->
            <div class="grid border-b border-[#1e1e1e] text-xs hover:bg-[#fafafa] transition-colors" style="grid-template-columns: 2fr 2fr 2fr 1.5fr 1.5fr 2fr 1.5fr;">
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-medium flex items-center gap-2">
                    <div class="w-6 h-6 bg-green-100 border border-[#1e1e1e] flex items-center justify-center text-green-700 font-bold text-xs flex-shrink-0">V</div>
                    Vaulted HQ
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-700">Priya Mehta</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-500 font-mono text-xs">CMO</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-mono text-xs text-gray-400">p.mehta@vau***</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">
                    <span class="bg-green-50 text-green-700 border border-green-200 px-2 py-0.5 font-mono text-xs brutalist-border">✓ valid</span>
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-600 text-xs italic">"Your content strategy shift in Q3..."</div>
                <div class="px-4 py-3">
                    <span class="bg-[var(--ts-green)] text-white px-2 py-0.5 font-mono text-xs">meeting</span>
                </div>
            </div>

            <!-- Row 5 (blurred/faded to imply more) -->
            <div class="grid border-b border-[#1e1e1e] text-xs opacity-40" style="grid-template-columns: 2fr 2fr 2fr 1.5fr 1.5fr 2fr 1.5fr;">
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-medium flex items-center gap-2">
                    <div class="w-6 h-6 bg-gray-100 border border-[#1e1e1e] flex items-center justify-center text-gray-400 font-bold text-xs flex-shrink-0">D</div>
                    Drift Capital
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-700">Tom Hargreaves</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-500 font-mono text-xs">Dir. of Sales</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] font-mono text-xs text-gray-400">t.harg@dri***</div>
                <div class="px-4 py-3 border-r border-[#1e1e1e]">
                    <span class="bg-green-50 text-green-700 border border-green-200 px-2 py-0.5 font-mono text-xs brutalist-border">✓ valid</span>
                </div>
                <div class="px-4 py-3 border-r border-[#1e1e1e] text-gray-600 text-xs italic">"Seen your expansion into EMEA..."</div>
                <div class="px-4 py-3">
                    <span class="bg-gray-100 text-gray-500 border border-gray-200 px-2 py-0.5 font-mono text-xs">queued</span>
                </div>
            </div>

            <!-- Footer -->
            <div class="bg-[#fafafa] px-4 py-3 flex items-center justify-between">
                <span class="font-mono text-xs text-gray-400">+ 2,842 more rows</span>
                <a href="/booking.html" class="font-mono text-xs text-[var(--ts-green)] hover:underline flex items-center gap-1">
                    Get your pipeline built <span class="material-symbols-outlined text-sm">arrow_forward</span>
                </a>
            </div>

        </div>

        <!-- Bottom caption -->
        <p class="font-mono text-xs text-gray-300 mt-4 text-center">All data is illustrative. Real pipelines are built around your ICP and offer.</p>

    </div>
</section>
"""

def add_clay_section():
    filepath = 'd:/boxmation/index.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find('main')
    sections = main.find_all('section', recursive=False)

    # Insert before the "How it Works" section (currently index 3)
    how_it_works = sections[3]
    new_soup = BeautifulSoup(CLAY_SECTION, 'html.parser')
    for tag in reversed(list(new_soup.children)):
        if tag.name:
            how_it_works.insert_before(tag)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Clay table section added!")

if __name__ == '__main__':
    add_clay_section()
