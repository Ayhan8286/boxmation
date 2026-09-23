import codecs
from bs4 import BeautifulSoup

STORY_SECTION = """
<!-- THE STORY SECTION -->
<section class="w-full border-t border-[#1e1e1e] bg-white relative">

    <!-- Top label bar -->
    <div class="w-full border-b border-[#1e1e1e] px-6 lg:px-8 py-4 flex items-center justify-between">
        <span class="font-mono text-xs text-gray-400 uppercase tracking-[0.2em]">// origin.story</span>
        <span class="font-mono text-xs text-gray-300">boxmation.sys v1.0</span>
    </div>

    <div class="max-w-[1240px] mx-auto px-6 lg:px-8 py-24">

        <!-- The main story layout -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-0 border border-[#1e1e1e] brutalist-border">

            <!-- LEFT: The narrative -->
            <div class="border-r border-[#1e1e1e] p-10 flex flex-col gap-12">

                <!-- Chunk 1 -->
                <div class="reveal">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-4">// the wrong direction</div>
                    <h3 class="font-display text-2xl font-black uppercase tracking-tight mb-4">Every agency sells you<br/>a spreadsheet and a script.</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">The standard outbound playbook: buy a contact list, blast 500 emails, hope. Agencies optimise for volume. They count sends, not conversations. They disappear after month one when the initial spike dies and the pipeline stalls.</p>
                </div>

                <div class="w-full h-px bg-[#1e1e1e] opacity-10"></div>

                <!-- Chunk 2 -->
                <div class="reveal">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-4">// the opposite approach</div>
                    <h3 class="font-display text-2xl font-black uppercase tracking-tight mb-4">We took the infrastructure<br/>route instead.</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">We asked a different question: what if outbound worked like software? Deterministic, repeatable, measurable. Not dependent on a sales rep having a good morning. We built Boxmation to be a pipeline system — not a headcount solution.</p>
                </div>

                <div class="w-full h-px bg-[#1e1e1e] opacity-10"></div>

                <!-- Chunk 3 -->
                <div class="reveal">
                    <div class="font-mono text-xs text-[var(--ts-dark)] uppercase tracking-[0.2em] mb-4">// the result</div>
                    <h3 class="font-display text-2xl font-black uppercase tracking-tight mb-4">Meetings, not metrics.<br/>Revenue, not reports.</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">The only number we talk about is qualified meetings booked. Because that is the only number that becomes revenue. Everything we build — the targeting, the copy, the sequencing, the AI — exists to put the right buyer in your calendar.</p>
                </div>

            </div>

            <!-- RIGHT: Terminal proof cards -->
            <div class="flex flex-col bg-[#0d0d0d]">

                <!-- Terminal window 1 -->
                <div class="border-b border-white/5 p-8 reveal">
                    <div class="flex items-center gap-2 mb-5">
                        <span class="w-2 h-2 rounded-full bg-[var(--ts-pink)]"></span>
                        <span class="w-2 h-2 rounded-full bg-[var(--ts-green)]"></span>
                        <span class="w-2 h-2 rounded-full bg-white/20"></span>
                        <span class="font-mono text-xs text-white/20 ml-2">old.agency.log</span>
                    </div>
                    <div class="font-mono text-xs leading-7 text-white/40">
                        <div><span class="text-red-400">ERR</span> &nbsp;personalisation: null</div>
                        <div><span class="text-red-400">ERR</span> &nbsp;targeting: "everyone"</div>
                        <div><span class="text-red-400">ERR</span> &nbsp;follow_up: manual</div>
                        <div><span class="text-red-400">ERR</span> &nbsp;reply_handling: unassigned</div>
                        <div><span class="text-red-400">ERR</span> &nbsp;pipeline_result: 0 meetings</div>
                        <div class="mt-2"><span class="text-white/20">exit code 1 — pipeline failed</span></div>
                    </div>
                </div>

                <!-- Terminal window 2 -->
                <div class="p-8 reveal flex-1">
                    <div class="flex items-center gap-2 mb-5">
                        <span class="w-2 h-2 rounded-full bg-[var(--ts-pink)]"></span>
                        <span class="w-2 h-2 rounded-full bg-[var(--ts-green)]"></span>
                        <span class="w-2 h-2 rounded-full bg-white/20"></span>
                        <span class="font-mono text-xs text-white/20 ml-2">boxmation.pipeline.log</span>
                    </div>
                    <div class="font-mono text-xs leading-7">
                        <div><span class="text-[var(--ts-green)]">OK &nbsp;</span><span class="text-white/50"> icp_built: </span><span class="text-white">true</span></div>
                        <div><span class="text-[var(--ts-green)]">OK &nbsp;</span><span class="text-white/50"> leads_enriched: </span><span class="text-[var(--ts-green)]">verified</span></div>
                        <div><span class="text-[var(--ts-green)]">OK &nbsp;</span><span class="text-white/50"> copy_personalised: </span><span class="text-white">AI-generated</span></div>
                        <div><span class="text-[var(--ts-green)]">OK &nbsp;</span><span class="text-white/50"> replies_handled: </span><span class="text-white">automated</span></div>
                        <div><span class="text-[var(--ts-green)]">OK &nbsp;</span><span class="text-white/50"> meetings_booked: </span><span class="text-[var(--ts-pink)] font-bold">qualified</span></div>
                        <div class="mt-4 flex items-center gap-2">
                            <span class="text-[var(--ts-green)]">✓</span>
                            <span class="text-white/60">pipeline operational — 24/7</span>
                            <span class="animate-pulse text-[var(--ts-green)]">█</span>
                        </div>
                    </div>

                    <!-- Mini stat -->
                    <div class="mt-8 pt-6 border-t border-white/5 grid grid-cols-2 gap-4">
                        <div>
                            <div class="font-mono text-2xl font-black text-[var(--ts-pink)]">$100k+</div>
                            <div class="font-mono text-xs text-white/30 mt-1">pipeline / 90 days</div>
                        </div>
                        <div>
                            <div class="font-mono text-2xl font-black text-[var(--ts-green)]">14</div>
                            <div class="font-mono text-xs text-white/30 mt-1">days to first send</div>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </div>
</section>
"""

def add_story():
    filepath = 'd:/boxmation/index.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find('main')
    sections = main.find_all('section', recursive=False)

    # Find the "How it works" section (the one with sys.process.init label) - it's the 3rd section
    how_it_works = sections[2]

    new_soup = BeautifulSoup(STORY_SECTION, 'html.parser')
    for tag in reversed(list(new_soup.children)):
        if tag.name:
            how_it_works.insert_before(tag)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Story section added!")

if __name__ == '__main__':
    add_story()
