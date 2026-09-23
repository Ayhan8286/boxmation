import os
import re
import codecs
from bs4 import BeautifulSoup

def rebuild_founder_page():
    # 1. Read the original founder.backup.html to get the gallery images
    with codecs.open('d:/boxmation/founder.backup.html', 'r', 'utf-8') as f:
        backup = f.read()
    bs_backup = BeautifulSoup(backup, 'html.parser')
    
    # Extract the 4 gallery groups
    galleries = bs_backup.find_all('div', class_=lambda c: c and 'w-[480px]' in c)
    gallery_htmls = []
    for g in galleries:
        # Reformat images to be brutalist
        for div in g.find_all('div', class_=lambda c: c and 'pb-6' in c):
            classes = div.get('class', [])
            classes = [c for c in classes if not c.startswith('rounded') and not c.startswith('shadow') and 'outline' not in c]
            classes.extend(['brutalist-border', 'bg-white'])
            div['class'] = classes
            
            img_wrap = div.find('div', class_=lambda c: c and 'overflow-hidden' in c)
            if img_wrap:
                wclasses = img_wrap.get('class', [])
                wclasses = [c for c in wclasses if not c.startswith('rounded') and 'outline' not in c]
                wclasses.append('brutalist-border')
                img_wrap['class'] = wclasses
                
            img = div.find('img')
            if img:
                img['class'] = img.get('class', []) + ['grayscale', 'contrast-125']
        
        gallery_htmls.append(g.decode_contents())

    # 2. Rebuild the founder HTML body entirely based on the new requirements
    
    card_html = """
    <!-- WHO BUILDS & RUNS YOUR PIPELINE Card -->
    <div class="bg-[#fafafa] border border-[#1e1e1e] p-0 sm:p-0 brutalist-border flex flex-col md:flex-row relative reveal mb-16">
        
        <div class="absolute top-0 right-0 bg-[var(--ts-magenta)] text-white px-3 py-1 mono text-xs font-bold uppercase tracking-widest border-l border-b border-[#1e1e1e] z-10">
            sys.founder.profile
        </div>

        <!-- Founder Photo -->
        <div class="w-full md:w-1/3 relative border-b md:border-b-0 md:border-r border-[#1e1e1e] bg-white p-6 flex flex-col justify-center items-center">
            <div class="w-full aspect-square overflow-hidden brutalist-border relative">
                <img alt="BoxMation Systems Architect" class="w-full h-full object-cover object-center grayscale contrast-125" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCbhHlbX-oBSShr21-Y77cqEpCfDpdTHPb2BqcrttK2wiiVqVSP-C6_tMHnGvLYzRTdL3F3B_cJ_HWoZ3qdoU3t_yGs9mXljydcEkBWTyAxMFQXuonm1bU2UT_hBOVd8M11JR7beclnHjzzbpxMXxwklLjMqEAZq94qKxTJDIgebfKEmhb6XkT9rJ1QiUuok1t8PD_D7Fol2OMxPq3N4oDLahmW-mg0lK6_bRcpzAM1BLoxA-NpX5ZlJs_r-bIgiucQ"/>
            </div>
            <div class="mt-4 w-full bg-[var(--ts-green)] text-white text-center py-2 brutalist-border mono text-sm font-bold uppercase tracking-widest">
                Ayhan Mirza
            </div>
            <div class="mt-2 text-center mono text-xs text-black font-bold uppercase tracking-widest">
                GTM Engineer
            </div>
        </div>

        <!-- Typewriter Text -->
        <div class="w-full md:w-2/3 p-8 sm:p-12 flex flex-col justify-center">
            <h2 class="font-display text-3xl font-bold mb-6 text-black uppercase tracking-tight">
                WHO BUILDS & RUNS YOUR PIPELINE
            </h2>
            <div class="mono text-sm sm:text-base leading-relaxed text-black space-y-6 typewriter-text">
                <p class="font-bold text-[var(--ts-dark)] text-lg">
                    <span class="text-[var(--ts-magenta)]">></span> "You don't need hands to send emails. You need an automated system that never calls in sick."
                </p>
                <p>
                    <span class="text-[var(--ts-green)]">>></span> Built and run by an outbound systems specialist. We don't do fluffy SEO, paid ads, or generic branding. We engineer outbound pipelines that book meetings with qualified buyers.
                </p>
                <p>
                    <span class="text-[var(--ts-green)]">>></span> Most $100K–$300K/mo agency founders fall into the same trap: they hire a junior SDR for $6,000/month, spend 90 days writing scripts they could write in an afternoon, pay $800/month in fragmented software tools, and 4 months later end up with burned domains and zero qualified meetings.
                </p>
                <p>
                    <span class="text-[var(--ts-green)]">>></span> BoxMation was designed to break that cycle completely. We handle the entire outbound process for you—finding the right prospects, engaging them with a natural touch, and delivering qualified meetings directly to your calendar so you can focus on closing deals.
                </p>
            </div>
        </div>

    </div>
    """

    # Expanded paragraphs
    paragraphs = [
        "I build outbound systems for a living, but that's not really who I am — it's just what I'm good at right now. The engineering, the automation, the scaling — it's all just a mechanical expression of a deeper drive to understand how things connect and how people operate. I treat cold email and GTM infrastructure as a puzzle. When you piece it together perfectly, it works flawlessly. But my true self exists beyond the servers and the sales calls.",
        
        "I box. Featherweight. There's something clean about it that I don't get anywhere else — no ambiguity, no politics, just you, the work you put in, and whether you did it or not. The gym is the same way for me. It's where the noise stops. In a world where everything is subjective and everyone is selling a narrative, the heavy bag doesn't lie. You either have the stamina or you don't. That raw, undeniable feedback loop is something I try to bring into my business as well.",
        
        "I read constantly — mostly mentalist books and self-help, the kind that try to explain why people do what they do. I think that's the same curiosity that pulled me into building systems in the first place: understanding what makes someone say yes, what makes them trust, what makes them act. One version of that curiosity became my career, turning human psychology into engineered outreach pipelines. The other version just makes me a better conversationalist at dinner, and keeps my mind sharp when I'm trying to decode complex human behavior.",
        
        "I want to travel properly one day — not tourist-checklist travel, but actually spend real time somewhere. Germany's on that list. Italy too. Sweden and Finland pull at me for a different reason — I don't know exactly why, but something about the quiet, the order, the cold clarity of those countries appeals to me. I crave environments that offer stark contrast to the loud, fast-paced startup world. And Norway — the northern lights specifically — feels like one of those phenomenons you have to see with your own eyes at least once before you die. I want to experience cultures that prioritize deep work and genuine human connection.",
        
        "There's also a version of my future where I'm doing a master's abroad, somewhere genuinely good. I don't just want to chase a piece of paper; I want to finally get to enjoy life without constantly grinding against something. I think about that a lot — what it would feel like to build toward a quiet, focused goal instead of just surviving the daily entrepreneurial hustle. Moving abroad, experiencing a completely different academic and social rhythm, is a goal that keeps me grounded when the day-to-day operations get heavy.",
        
        "I've also spent a considerable amount of time building things that had nothing to do with revenue — an app for people with hearing disabilities to navigate the world easier, a period-tracking and guidance app, teaching automation workshops, and speaking to students as the Director of the AI Society at UCP. Those projects remind me that technology is a lever. Not every build has to make money to matter. The true value of knowing how to build systems is the freedom it gives you to solve problems that actually mean something to you."
    ]

    log_cards_html = ""
    for i, p in enumerate(paragraphs):
        log_cards_html += f"""
        <div class="bg-[#fafafa] border border-[#1e1e1e] p-6 sm:p-8 brutalist-border reveal relative mb-12">
            <div class="absolute top-0 left-0 bg-[#1e1e1e] text-white px-3 py-1 mono text-xs font-bold uppercase tracking-widest border-r border-b border-[#1e1e1e]">
                sys.log.write // seq_{i+1:02d}
            </div>
            <p class="mono text-sm sm:text-base leading-relaxed text-black pt-6 typewriter-text">
                <span class="text-[var(--ts-magenta)]">></span> {p}
            </p>
        </div>
        """
        # Interleave gallery
        if i < len(gallery_htmls):
            log_cards_html += f"""
            <div class="flex flex-wrap justify-center gap-6 reveal my-12">
                {gallery_htmls[i]}
            </div>
            """

    # 3. Read the base of founder.html and inject the newly built content
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()
        
    # Find where the main content starts. It's after <h2 class="text-xl md:text-2xl font-medium mt-6">Beyond the Systems</h2>
    # Actually, we can replace everything inside `<main class="w-full pt-20 bg-white min-h-screen relative overflow-hidden">`
    # Let's just find the header block and then replace the rest.
    
    header_block = """<div class="mb-20 text-center reveal">
                <a href="/" class="inline-flex items-center gap-2 text-gray-400 hover:text-black transition-colors font-semibold text-sm uppercase tracking-wider mb-10 group">
                    <span class="material-symbols-outlined text-sm transition-transform group-hover:-translate-x-1">arrow_back</span>
                    Back to Home
                </a>
                
                <h1 class="font-display text-5xl md:text-7xl max-w-5xl font-extrabold tracking-tighter leading-[1.1] mb-6 uppercase">
                        The <span class="bg-[var(--ts-pink)] text-[var(--ts-dark)] px-2">Founder</span><span class="cursor-blink"></span>
                    </h1>
            </div>"""
            
    # We will just replace the inner contents of max-w-[1000px] entirely
    match = re.search(r'(<div class="max-w-\[1000px\] mx-auto px-6 lg:px-8 relative z-10 py-24">).*?(<!-- FOOTER -->|</main>)', html, flags=re.DOTALL)
    
    if match:
        new_content = match.group(1) + "\n" + header_block + "\n" + card_html + "\n<h2 class='text-xl md:text-2xl font-medium mb-12 uppercase mono font-bold border-b border-[#1e1e1e] pb-4'>Beyond the Systems</h2>\n" + log_cards_html + "\n</div>\n" + match.group(2)
        html = html[:match.start()] + new_content + html[match.end():]

    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(html)
        
    print("Rebuilt founder.html perfectly.")
    
    # Also we should remove the founder section from index.html since we moved it.
    with codecs.open('d:/boxmation/index.html', 'r', 'utf-8') as f:
        index_html = f.read()
        
    # The section id="founder" we added earlier
    index_html = re.sub(r'<!-- 3\. FOUNDER & HARD POSITIONING SECTION -->\s*<section class="w-full py-24 relative" id="founder">.*?</section>', '', index_html, flags=re.DOTALL)
    
    with codecs.open('d:/boxmation/index.html', 'w', 'utf-8') as f:
        f.write(index_html)
        
if __name__ == '__main__':
    rebuild_founder_page()
