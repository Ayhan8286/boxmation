import re
import codecs

def rebuild_founder_section():
    filepath = 'd:/boxmation/index.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # The new section to inject
    new_section = """<!-- 3. FOUNDER & HARD POSITIONING SECTION -->
<section class="w-full py-24 relative" id="founder">
    <div class="max-w-5xl mx-auto px-6 lg:px-8 reveal">
        
        <div class="bg-[#fafafa] border border-[#1e1e1e] p-0 sm:p-0 brutalist-border flex flex-col md:flex-row relative">
            
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
                <div class="mono text-sm sm:text-base leading-relaxed text-black space-y-6">
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
                <div class="mt-8 pt-6 border-t border-gray-200">
                    <a href="founder.html" class="inline-flex items-center gap-2 mono text-sm font-bold text-[var(--ts-dark)] hover:text-[var(--ts-magenta)] transition-colors group">
                        <span class="w-2 h-2 bg-[var(--ts-magenta)] group-hover:animate-pulse"></span> Read the full founder log
                    </a>
                </div>
            </div>

        </div>
    </div>
</section>
"""

    # We need to replace the broken section
    broken_regex = r'(<!-- 3\. FOUNDER & HARD POSITIONING SECTION -->\s*<section class="w-full py-24 relative" id="founder">\s*<div class="max-w-\[1240px\] mx-auto px-6 lg:px-8 reveal">\s*<div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">\s*</section>)'
    
    if re.search(broken_regex, html, flags=re.DOTALL):
        html = re.sub(broken_regex, new_section, html, flags=re.DOTALL)
    else:
        # Fallback if it's slightly different
        match = re.search(r'(<!-- 3\. FOUNDER & HARD POSITIONING SECTION -->.*?</section>)', html, flags=re.DOTALL)
        if match:
            html = html.replace(match.group(1), new_section)
            
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    rebuild_founder_section()
