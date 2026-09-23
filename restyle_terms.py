import codecs
from bs4 import BeautifulSoup

def restyle_terms():
    filepath = 'd:/boxmation/terms.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find('main')

    # Fix main classes
    main['class'] = ['w-full', 'pt-20', 'bg-white', 'min-h-screen']

    # Replace the entire main content
    new_content = BeautifulSoup("""
<div class="w-full">

    <!-- Hero bar -->
    <div class="w-full border-b border-[#1e1e1e] bg-[#1e1e1e] text-white py-20 px-6 lg:px-8">
        <div class="max-w-[1000px] mx-auto">
            <span class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-6 block">// sys.legal.load</span>
            <h1 class="font-display text-5xl md:text-6xl font-extrabold tracking-tighter uppercase leading-[1.1]">
                Terms &amp;<br/>
                <span class="text-[var(--ts-pink)]">Privacy</span>
            </h1>
            <p class="font-mono text-sm text-white/40 mt-6">Last updated: 2025 &nbsp;|&nbsp; boxmation.labs@gmail.com</p>
        </div>
    </div>

    <!-- Content -->
    <div class="max-w-[1000px] mx-auto px-6 lg:px-8 py-20 flex flex-col gap-0">

        <!-- TERMS OF SERVICE -->
        <div class="border border-[#1e1e1e] brutalist-border mb-16">

            <!-- Section header -->
            <div class="bg-[#1e1e1e] px-6 py-4 flex items-center gap-3">
                <span class="w-2 h-2 rounded-full bg-[var(--ts-pink)]"></span>
                <span class="w-2 h-2 rounded-full bg-[var(--ts-green)]"></span>
                <span class="w-2 h-2 rounded-full bg-white/20"></span>
                <span class="font-mono text-xs text-white/50 ml-2">terms_of_service.md</span>
            </div>

            <div class="divide-y divide-[#1e1e1e]/10">

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// 01 — the service</div>
                    <p class="text-gray-600 text-sm leading-relaxed">BoxMation ("we," "us") provides automated email and LinkedIn outbound systems for B2B companies. This includes ICP research, lead sourcing and enrichment, AI-personalised copy, sending infrastructure, and reply handling — all built and managed under a retainer engagement.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// 02 — what is not included</div>
                    <p class="text-gray-600 text-sm leading-relaxed mb-4">Unless separately agreed and paid for in writing, BoxMation does not provide:</p>
                    <ul class="space-y-2 font-mono text-sm text-gray-500">
                        <li class="flex gap-3"><span class="text-[var(--ts-pink)]">—</span> Paid advertising or media buying</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-pink)]">—</span> CRM setup or management (beyond pipeline tagging)</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-pink)]">—</span> Sales team training or management</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-pink)]">—</span> Legal compliance review for your specific jurisdiction</li>
                    </ul>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// 03 — pricing and payment</div>
                    <p class="text-gray-600 text-sm leading-relaxed">Standard engagement: a one-time setup fee plus a recurring monthly retainer. Payment is due at the start of each billing period. Failure to pay within 7 days of the due date may result in pausing of services.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// 04 — timeline and guarantee</div>
                    <p class="text-gray-600 text-sm leading-relaxed">We commit to a "launch-ready" milestone (system built, tested, and live) within 14 days of receiving all required access and information from the client. This milestone is contingent on the client meeting their responsibilities outlined below.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// 05 — client responsibilities</div>
                    <p class="text-gray-600 text-sm leading-relaxed mb-4">To deliver on the committed timeline, you agree to:</p>
                    <ul class="space-y-2 font-mono text-sm text-gray-500">
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> Grant necessary account access within 48 hours of request</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> Provide accurate ICP and offer information during onboarding</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> Review and approve copy within the agreed review windows</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> Ensure sending domains are available and not previously flagged</li>
                    </ul>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// 06 — data and compliance</div>
                    <p class="text-gray-600 text-sm leading-relaxed">We source contact data from providers we believe conduct their own compliance processes. You are responsible for ensuring outbound activity complies with laws applicable to your business and target geography (e.g. CAN-SPAM, GDPR). We are not your legal counsel.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// 07 — term and termination</div>
                    <p class="text-gray-600 text-sm leading-relaxed">Engagements are month-to-month following the initial setup and launch period. Either party may terminate with 30 days written notice. No refunds are issued for the current billing month upon termination.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// 08 — confidentiality</div>
                    <p class="text-gray-600 text-sm leading-relaxed">Both parties agree to keep confidential any non-public business information shared during the engagement. This includes client ICP data, offer positioning, and pipeline results.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// 09 — limitation of liability</div>
                    <p class="text-gray-600 text-sm leading-relaxed">BoxMation's liability under any engagement is limited to the fees paid for the month in which the issue arose. We are not liable for lost revenue, missed opportunities, or consequential damages.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// 10 — changes to these terms</div>
                    <p class="text-gray-600 text-sm leading-relaxed">We may update these terms from time to time. Material changes will be communicated via email to active clients at least 14 days before taking effect.</p>
                </div>

            </div>
        </div>

        <!-- PRIVACY POLICY -->
        <div class="border border-[#1e1e1e] brutalist-border mb-16">

            <div class="bg-[#1e1e1e] px-6 py-4 flex items-center gap-3">
                <span class="w-2 h-2 rounded-full bg-[var(--ts-pink)]"></span>
                <span class="w-2 h-2 rounded-full bg-[var(--ts-green)]"></span>
                <span class="w-2 h-2 rounded-full bg-white/20"></span>
                <span class="font-mono text-xs text-white/50 ml-2">privacy_policy.md</span>
            </div>

            <div class="divide-y divide-[#1e1e1e]/10">

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// what we collect</div>
                    <p class="text-gray-600 text-sm leading-relaxed mb-4">From website visitors: standard analytics data (pages viewed, time on page, general location). From clients: business name, email address, and information needed to build and run your pipeline.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// how we use it</div>
                    <ul class="space-y-2 font-mono text-sm text-gray-500">
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> To respond to inquiries and schedule calls</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> To deliver and improve the contracted services</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> To communicate updates about your engagement</li>
                        <li class="flex gap-3"><span class="text-[var(--ts-green)]">→</span> We do not sell your data. Full stop.</li>
                    </ul>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// third-party tools</div>
                    <p class="text-gray-600 text-sm leading-relaxed">This site uses third-party tools for analytics (e.g., Vercel Analytics, PostHog) and booking (zcal.co). Each has their own privacy policy. We use Clay.com and similar tools to build client pipelines — data processed through these tools is governed by their respective policies.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// data retention</div>
                    <p class="text-gray-600 text-sm leading-relaxed">We retain client business data for the duration of the engagement and a reasonable period after (typically 90 days) in case of disputes or re-engagement. You may request earlier deletion.</p>
                </div>

                <div class="px-8 py-8">
                    <div class="font-mono text-xs text-[var(--ts-green)] uppercase tracking-[0.2em] mb-3">// your rights</div>
                    <p class="text-gray-600 text-sm leading-relaxed">You may request access to, correction of, or deletion of your personal data by contacting us directly. We will respond within 30 days.</p>
                </div>

                <div class="px-8 py-8 bg-[#fafafa]">
                    <div class="font-mono text-xs text-[var(--ts-pink)] uppercase tracking-[0.2em] mb-3">// contact</div>
                    <p class="text-gray-600 text-sm leading-relaxed">Questions about these terms or this policy:</p>
                    <a href="mailto:boxmation.labs@gmail.com" class="font-mono text-sm text-[var(--ts-green)] hover:underline mt-2 block">boxmation.labs@gmail.com</a>
                </div>

            </div>
        </div>

        <div class="text-center py-8">
            <a href="/" class="inline-flex items-center gap-2 font-mono text-xs text-gray-400 hover:text-black transition-colors uppercase tracking-wider">
                <span class="material-symbols-outlined text-sm">arrow_back</span>
                Back to Home
            </a>
        </div>

    </div>
</div>
""", 'html.parser')

    # Replace main content
    main.clear()
    for child in new_content.children:
        main.append(child.__copy__())

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Terms page restyled!")

if __name__ == '__main__':
    restyle_terms()
