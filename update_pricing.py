import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = " " "<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch mb-12">
    <!-- Card 1: Pipeline -->
    <div class="border border-[#1e1e1e] p-8 bg-[#fafafa] lg:p-10 relative overflow-hidden flex flex-col reveal brutalist-border">
        <div class="flex flex-col sm:flex-row justify-between gap-4 pb-8 border-b border-[#1e1e1e] mb-8">
            <div>
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-2">Outbound System</span>
                <h3 class="font-display text-3xl font-bold text-black mt-1">The BoxMation Pipeline</h3>
            </div>
            <div class="text-left sm:text-right flex-shrink-0">
                <div class="flex items-baseline gap-1 sm:justify-end">
                    <span class="font-display text-4xl font-bold text-black">$3,500</span>
                    <span class="font-medium">/ month</span>
                </div>
                <span class="mono text-xs font-bold text-green-600 uppercase tracking-widest block mt-2">+ $3,000 One-Time Setup</span>
            </div>
        </div>
        <!-- Quick Specs Strip -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 p-5 bg-white border border-[#1e1e1e] mb-8 brutalist-border">
            <div>
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">CHANNELS</span>
                <span class="font-display text-sm font-bold text-black">Email + LinkedIn</span>
            </div>
            <div>
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">ONBOARDING</span>
                <span class="font-display text-sm font-bold text-green-600">14 Days Live</span>
            </div>
            <div class="col-span-2 sm:col-span-1">
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">COMMITMENT</span>
                <span class="font-display text-sm font-bold text-black">Month-to-Month</span>
            </div>
        </div>
        <!-- Included Features List -->
        <div class="space-y-4 mb-10 flex-1">
            <h4 class="mono text-xs font-bold uppercase tracking-widest mb-4">WHAT IS INCLUDED &amp; FULLY HANDLED:</h4>
            <div class="space-y-4">
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-green-50 text-green-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">dataset</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Deep Prospect Research:</strong>
                        <p class="text-sm leading-relaxed">Finding verified contact information and deep background details on every prospect before we reach out.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-blue-50 text-blue-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">mail</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Guaranteed Deliverability:</strong>
                        <p class="text-sm leading-relaxed">We handle all inbox setup and monitoring to ensure your messages always land in the primary inbox.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-purple-50 text-purple-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">connect_without_contact</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Automated LinkedIn Outreach:</strong>
                        <p class="text-sm leading-relaxed">Personalized connection requests and follow-ups that feel completely natural and conversational.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-orange-50 text-orange-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">alt_route</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Seamless Calendar Booking:</strong>
                        <p class="text-sm leading-relaxed">When a prospect is ready to talk, they are routed directly to your calendar.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 text-black flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">analytics</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Continuous Optimization:</strong>
                        <p class="text-sm leading-relaxed">We constantly test and refine our messaging every week to maximize positive reply rates.</p>
                    </div>
                </div>
            </div>
        </div>
        <a class="w-full py-4 text-white font-semibold text-lg text-center block hover:scale-[1.02] transition-transform mt-auto brutalist-border bg-[var(--ts-dark)] text-[var(--ts-white)] hover:bg-[var(--ts-dark)] brutalist-button" href="/booking.html">
            Lock In 14-Day Outbound Implementation ?
        </a>
    </div>

    <!-- Card 2: Signal Engine -->
    <div class="border border-[#1e1e1e] p-8 bg-[#fafafa] lg:p-10 relative overflow-hidden flex flex-col reveal brutalist-border" style="animation-delay: 0.1s;">
        <div class="flex flex-col sm:flex-row justify-between gap-4 pb-8 border-b border-[#1e1e1e] mb-8">
            <div>
                <span class="mono text-xs font-bold text-[var(--ts-teal)] uppercase tracking-widest block mb-2">Inbound System</span>
                <h3 class="font-display text-3xl font-bold text-black mt-1">The BoxMation Signal Engine</h3>
            </div>
            <div class="text-left sm:text-right flex-shrink-0">
                <div class="flex items-baseline gap-1 sm:justify-end">
                    <span class="font-display text-4xl font-bold text-black">$3,500</span>
                    <span class="font-medium">/ month</span>
                </div>
                <span class="mono text-xs font-bold text-green-600 uppercase tracking-widest block mt-2">+ $3,000 One-Time Setup</span>
            </div>
        </div>
        <!-- Quick Specs Strip -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 p-5 bg-white border border-[#1e1e1e] mb-8 brutalist-border">
            <div>
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">CHANNELS</span>
                <span class="font-display text-sm font-bold text-black">Website + Ad Platforms</span>
            </div>
            <div>
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">ONBOARDING</span>
                <span class="font-display text-sm font-bold text-green-600">14 Days Live</span>
            </div>
            <div class="col-span-2 sm:col-span-1">
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">COMMITMENT</span>
                <span class="font-display text-sm font-bold text-black">Month-to-Month</span>
            </div>
        </div>
        <!-- Included Features List -->
        <div class="space-y-4 mb-10 flex-1">
            <h4 class="mono text-xs font-bold uppercase tracking-widest mb-4">WHAT IS INCLUDED &amp; FULLY HANDLED:</h4>
            <div class="space-y-4">
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-teal-50 text-[var(--ts-teal)] flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">manage_search</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Anonymous Visitor Identification:</strong>
                        <p class="text-sm leading-relaxed">We identify the companies and people visiting your website — even the ones who never fill out a form.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-blue-50 text-blue-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">merge</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Unified Lead Capture:</strong>
                        <p class="text-sm leading-relaxed">Every lead from Meta, Google, LinkedIn, and your website gets pulled into one place.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-purple-50 text-purple-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">grade</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Unified Lead Scoring:</strong>
                        <p class="text-sm leading-relaxed">Visit behavior, form-fills, and platform source are combined into one score.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-orange-50 text-orange-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">hub</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Direct CRM Routing:</strong>
                        <p class="text-sm leading-relaxed">Every identified visitor and captured lead lands in your CRM automatically, tagged by source.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-green-50 text-green-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">bar_chart_4_bars</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Per-Platform Reporting:</strong>
                        <p class="text-sm leading-relaxed">See exactly which platform brings you real quality, not just volume.</p>
                    </div>
                </div>
            </div>
        </div>
        <a class="w-full py-4 text-white font-semibold text-lg text-center block hover:scale-[1.02] transition-transform mt-auto brutalist-border bg-[var(--ts-teal)] hover:opacity-90 brutalist-button" href="/booking.html">
            Lock In 14-Day Inbound Implementation ?
        </a>
    </div>

    <!-- Card 3: Full-Stack Engine -->
    <div class="border border-[#1e1e1e] p-8 bg-[#fafafa] lg:p-10 relative overflow-hidden flex flex-col reveal brutalist-border" style="animation-delay: 0.2s;">
        <div class="absolute top-0 left-0 right-0 h-2 bg-[var(--ts-green)]"></div>
        <div class="flex flex-col sm:flex-row justify-between gap-4 pb-8 border-b border-[#1e1e1e] mb-8">
            <div>
                <span class="mono text-xs font-bold text-[var(--ts-green)] uppercase tracking-widest block mb-2">? Best Value — Full System</span>
                <h3 class="font-display text-3xl font-bold text-black mt-1">The BoxMation Full-Stack Engine</h3>
            </div>
            <div class="text-left sm:text-right flex-shrink-0">
                <div class="flex items-baseline gap-1 sm:justify-end">
                    <span class="font-display text-4xl font-bold text-black">$6,000</span>
                    <span class="font-medium">/ month</span>
                </div>
                <span class="mono text-xs font-bold text-green-600 uppercase tracking-widest block mt-2">+ $5,000 One-Time Setup</span>
            </div>
        </div>
        <!-- Quick Specs Strip -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 p-5 bg-white border border-[#1e1e1e] mb-8 brutalist-border">
            <div>
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">CHANNELS</span>
                <span class="font-display text-sm font-bold text-black">Email + LinkedIn + Website + Ads</span>
            </div>
            <div>
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">ONBOARDING</span>
                <span class="font-display text-sm font-bold text-green-600">14 Days Live</span>
            </div>
            <div class="col-span-2 sm:col-span-1">
                <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-1">COMMITMENT</span>
                <span class="font-display text-sm font-bold text-black">Month-to-Month</span>
            </div>
        </div>
        <!-- Included Features List -->
        <div class="space-y-4 mb-10 flex-1">
            <h4 class="mono text-xs font-bold uppercase tracking-widest mb-4">WHAT IS INCLUDED &amp; FULLY HANDLED:</h4>
            <div class="space-y-4">
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-green-50 text-[var(--ts-green)] flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">join_full</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Outbound + Inbound, Combined:</strong>
                        <p class="text-sm leading-relaxed">Everything in the Pipeline and Signal Engine, running as one connected system.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-pink-50 text-[var(--ts-pink)] flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">bolt</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Signal-Triggered Outreach:</strong>
                        <p class="text-sm leading-relaxed">A hot inbound visitor can automatically trigger a personal outbound touch.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-blue-50 text-blue-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">dashboard</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">One Unified Dashboard:</strong>
                        <p class="text-sm leading-relaxed">Every touchpoint, every channel, every score — in a single view.</p>
                    </div>
                </div>
                <div class="flex items-start gap-4 p-4 bg-white border border-[#1e1e1e] transition hover:shadow-md brutalist-border">
                    <div class="h-10 w-10 bg-yellow-50 text-yellow-600 flex items-center justify-center flex-shrink-0 brutalist-border">
                        <span class="material-symbols-outlined">savings</span>
                    </div>
                    <div>
                        <strong class="font-display text-lg text-black block mb-1">Bundled Pricing:</strong>
                        <p class="text-sm leading-relaxed">Both systems together for less than buying them separately.</p>
                    </div>
                </div>
            </div>
        </div>
        <a class="w-full py-4 font-semibold text-lg text-center block hover:scale-[1.02] transition-transform mt-auto bg-[var(--ts-green)] text-[var(--ts-dark)] border border-[#1e1e1e] brutalist-button" href="/booking.html">
            Lock In Full-Stack Implementation ?
        </a>
    </div>

    <!-- Card 4: GTM Strategy -->
    <div class="border border-[#1e1e1e] p-8 bg-[#fafafa] lg:p-10 relative overflow-hidden flex flex-col reveal brutalist-border" style="animation-delay: 0.3s;">
        <div class="flex-1 relative z-10 flex flex-col h-full">
            <div class="flex flex-col sm:flex-row justify-between gap-4 pb-8 border-b border-[#1e1e1e] mb-8">
                <div>
                    <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mb-2">One-Time Engagement</span>
                    <h3 class="font-display text-3xl text-black font-bold mt-1">GTM Strategy &amp; Implementation</h3>
                </div>
                <div class="text-left sm:text-right flex-shrink-0">
                    <div class="flex items-baseline gap-1 sm:justify-end">
                        <span class="font-display text-4xl font-bold text-black">$3,500</span>
                    </div>
                    <span class="mono text-xs font-bold text-gray-400 uppercase tracking-widest block mt-2">One-Time Delivery</span>
                </div>
            </div>
            <p class="text-base leading-relaxed mb-8">
                A complete go-to-market strategy and phased implementation roadmap. Built specifically around your market, your offer, and what your team can realistically ship.
            </p>
            <div class="space-y-4 mb-8 flex-1">
                <h4 class="mono text-xs font-bold text-gray-400 uppercase tracking-widest mb-4">WHAT YOU RECEIVE:</h4>
                <div class="space-y-4">
                    <div class="flex items-start gap-3 p-4 border border-[#1e1e1e] bg-white brutalist-border">
                        <span class="material-symbols-outlined text-black flex-shrink-0">strategy</span>
                        <div>
                            <strong class="font-display text-base text-black block mb-1">Comprehensive GTM Strategy:</strong>
                            <p class="text-xs leading-relaxed">Deep ICP segmentation, positioning, messaging pillars, and pricing models.</p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3 p-4 border border-[#1e1e1e] bg-white brutalist-border">
                        <span class="material-symbols-outlined text-black flex-shrink-0">account_tree</span>
                        <div>
                            <strong class="font-display text-base text-black block mb-1">Phased Engineering Roadmap:</strong>
                            <p class="text-xs leading-relaxed">Dependency-ordered build plan for tracking, lead scoring, and automated flows.</p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3 p-4 border border-[#1e1e1e] bg-white brutalist-border">
                        <span class="material-symbols-outlined text-black flex-shrink-0">timeline</span>
                        <div>
                            <strong class="font-display text-base text-black block mb-1">Actionable Channel Plan:</strong>
                            <p class="text-xs leading-relaxed">Prioritized sequencing of outbound, inbound, and community channels.</p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3 p-4 border border-[#1e1e1e] bg-white brutalist-border">
                        <span class="material-symbols-outlined text-black flex-shrink-0">query_stats</span>
                        <div>
                            <strong class="font-display text-base text-black block mb-1">Metrics &amp; Feedback Loops:</strong>
                            <p class="text-xs leading-relaxed">Defined sales processes, dashboard frameworks, and leading/lagging indicators.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-full mt-auto">
                <a class="w-full py-4 bg-transparent border border-[#1e1e1e] text-black font-semibold text-lg text-center block hover:bg-[var(--ts-dark)] hover:text-white transition-colors brutalist-button" href="/booking.html">
                    Discuss Strategy ?
                </a>
            </div>
        </div>
    </div>
</div>" " ".strip()

start_str = r'<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch mb-12">'
end_str = r'<!-- /Signal Engine \+ Full-Stack Engine Row -->'

match = re.search(f"{start_str}.*?{end_str}", content, re.DOTALL)
if match:
    new_content = content[:match.start()] + new_cards + content[match.end():]
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not find the block to replace")
