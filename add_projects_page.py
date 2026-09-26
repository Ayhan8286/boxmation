import os
import glob
import re

# The HTML for the projects main content
PROJECTS_MAIN = """
<main class="w-full pt-20 bg-white min-h-screen flex flex-col">
<!-- PROJECTS / DEPLOYMENTS SECTION -->
<section class="w-full bg-[#f9f9f9] relative overflow-hidden flex-1 border-t border-[#1e1e1e]">
    <!-- Top label bar -->
    <div class="w-full border-b border-[#1e1e1e] px-6 lg:px-8 py-4 flex items-center justify-between bg-white">
        <div class="flex items-center gap-3">
            <span class="w-2 h-2 rounded-full bg-[var(--ts-green)]"></span>
            <span class="font-mono text-xs text-gray-400 uppercase tracking-[0.2em]">// sys.deployments — live instances</span>
        </div>
        <span class="font-mono text-xs text-gray-300 hidden sm:block">boxmation.projects</span>
    </div>
    
    <div class="max-w-[1240px] mx-auto px-6 lg:px-8 py-24">
        <div class="reveal mb-16 text-center max-w-3xl mx-auto">
            <h1 class="font-display text-5xl md:text-6xl font-extrabold tracking-tighter leading-[1.1] uppercase mb-4">
                Systems We've <span class="bg-[var(--ts-pink)] text-white px-2">Built</span>
            </h1>
            <p class="text-gray-500 text-lg leading-relaxed mt-4">
                A selection of active outbound pipelines currently running for B2B founders.
            </p>
        </div>

        <!-- Projects Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            
            <!-- Project 1 -->
            <div class="border border-[#1e1e1e] bg-white brutalist-border flex flex-col hover:-translate-y-2 transition-transform duration-300 group reveal">
                <div class="border-b border-[#1e1e1e] px-4 py-2 flex justify-between items-center bg-[#1e1e1e]">
                    <span class="font-mono text-xs text-white/50">id: 8492</span>
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-[var(--ts-green)] animate-pulse"></span>
                        <span class="font-mono text-xs text-[var(--ts-green)] uppercase">Active</span>
                    </div>
                </div>
                <div class="p-8 flex-1 flex flex-col">
                    <div class="font-mono text-xs text-[var(--ts-magenta)] font-bold tracking-widest uppercase mb-3">B2B SaaS</div>
                    <h3 class="font-display text-2xl font-bold mb-4 group-hover:text-[var(--ts-pink)] transition-colors">Fintech Infrastructure</h3>
                    <p class="text-gray-600 text-sm mb-8 flex-1 leading-relaxed">
                        Full-cycle outbound system targeting CFOs and VP Finance. Built custom scraping logic to identify companies recently raising Series B+.
                    </p>
                    <div class="border-t border-gray-100 pt-4 flex justify-between items-center">
                        <div class="font-mono text-xs text-gray-400">Volume</div>
                        <div class="font-mono text-sm font-bold">2,500/mo</div>
                    </div>
                </div>
            </div>

            <!-- Project 2 -->
            <div class="border border-[#1e1e1e] bg-white brutalist-border flex flex-col hover:-translate-y-2 transition-transform duration-300 group reveal" style="animation-delay: 0.1s;">
                <div class="border-b border-[#1e1e1e] px-4 py-2 flex justify-between items-center bg-[#1e1e1e]">
                    <span class="font-mono text-xs text-white/50">id: 7731</span>
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-[var(--ts-green)] animate-pulse"></span>
                        <span class="font-mono text-xs text-[var(--ts-green)] uppercase">Active</span>
                    </div>
                </div>
                <div class="p-8 flex-1 flex flex-col">
                    <div class="font-mono text-xs text-[var(--ts-teal)] font-bold tracking-widest uppercase mb-3">Enterprise Agency</div>
                    <h3 class="font-display text-2xl font-bold mb-4 group-hover:text-[var(--ts-pink)] transition-colors">Dev Shop Growth</h3>
                    <p class="text-gray-600 text-sm mb-8 flex-1 leading-relaxed">
                        Dual-channel (LinkedIn + Email) pipeline for a software development agency. Personalisation engine trained on prospects' recent github commits and tech stack.
                    </p>
                    <div class="border-t border-gray-100 pt-4 flex justify-between items-center">
                        <div class="font-mono text-xs text-gray-400">Meetings</div>
                        <div class="font-mono text-sm font-bold text-[var(--ts-green)]">12-15/mo</div>
                    </div>
                </div>
            </div>

            <!-- Project 3 -->
            <div class="border border-[#1e1e1e] bg-white brutalist-border flex flex-col hover:-translate-y-2 transition-transform duration-300 group reveal" style="animation-delay: 0.2s;">
                <div class="border-b border-[#1e1e1e] px-4 py-2 flex justify-between items-center bg-[#1e1e1e]">
                    <span class="font-mono text-xs text-white/50">id: 9102</span>
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-gray-400"></span>
                        <span class="font-mono text-xs text-gray-400 uppercase">Handed Over</span>
                    </div>
                </div>
                <div class="p-8 flex-1 flex flex-col">
                    <div class="font-mono text-xs text-[var(--ts-dark)] font-bold tracking-widest uppercase mb-3">Consulting</div>
                    <h3 class="font-display text-2xl font-bold mb-4 group-hover:text-[var(--ts-pink)] transition-colors">Cybersecurity Firm</h3>
                    <p class="text-gray-600 text-sm mb-8 flex-1 leading-relaxed">
                        Highly targeted campaign reaching CISOs. Utilised intent data signals (recent data breaches in competitor networks) to trigger perfectly timed outreach.
                    </p>
                    <div class="border-t border-gray-100 pt-4 flex justify-between items-center">
                        <div class="font-mono text-xs text-gray-400">Pipeline</div>
                        <div class="font-mono text-sm font-bold">$250k+</div>
                    </div>
                </div>
            </div>

        </div>
        
        <div class="mt-20 text-center pb-10">
            <a href="/booking.html" class="inline-flex items-center gap-2 px-8 py-4 bg-[#1e1e1e] text-white font-semibold transition-transform hover:-translate-y-1 brutalist-border brutalist-button">
                <span>Build My System</span>
                <span class="material-symbols-outlined text-sm">terminal</span>
            </a>
        </div>
    </div>
</section>
</main>
"""

# 1. Create projects.html based on pricing.html layout
with open("pricing.html", "r", encoding="utf-8") as f:
    pricing_content = f.read()

# Extract header (up to <main...>)
header_end = pricing_content.find("<main")
header = pricing_content[:header_end]

# Extract footer (from </main> onwards)
footer_start = pricing_content.rfind("</main>") + 7
footer = pricing_content[footer_start:]

# Assemble projects.html
projects_content = header + PROJECTS_MAIN + footer
with open("projects.html", "w", encoding="utf-8") as f:
    f.write(projects_content)
    
print("Created projects.html")

# 2. Update navigation in all files
files_to_update = glob.glob("*.html")
files_to_update = [f for f in files_to_update if not f.endswith(".bak")]

for filename in files_to_update:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content

    # Replace desktop nav - be careful with regex matches, ensure they are exact enough
    content = re.sub(
        r'(<a class="[^"]*" href="[^"]*founder\.html">The Founder</a>)\s+(<a class="[^"]*" href="/pricing\.html">Pricing &amp; Offer</a>)',
        r'\1\n<a class="text-sm font-medium hover:text-black transition-colors" href="/projects.html">Projects</a>\n\2',
        content
    )

    # Replace mobile nav
    content = re.sub(
        r'(<a class="[^"]*mobile-link[^"]*" href="[^"]*founder\.html">The Founder</a>)\s+(<a class="[^"]*mobile-link[^"]*" href="/pricing\.html">Pricing &amp; Offer</a>)',
        r'\1\n<a class="hover:text-black transition-colors mobile-link font-medium" href="/projects.html">Projects</a>\n\2',
        content
    )

    # Replace footer nav (careful not to double-match if it matches desktop nav class)
    # The desktop nav is: <a class="text-sm font-medium hover:text-black transition-colors"
    # The footer nav is: <a class="hover:text-black transition-colors" 
    content = re.sub(
        r'(<a class="hover:text-black transition-colors" href="[^"]*founder\.html">The Founder</a>)\s+(<a class="hover:text-black transition-colors" href="/pricing\.html">Pricing &amp; Offer</a>)',
        r'\1\n<a class="hover:text-black transition-colors" href="/projects.html">Projects</a>\n\2',
        content
    )
    
    if content != original_content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated navigation in {filename}")
    else:
        print(f"No changes made to {filename}")
