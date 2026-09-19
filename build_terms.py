import os
import re

# Read index.html to grab the head config and header/footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract head and header
head_match = re.search(r'(<head>.*?</head>)', index_html, re.DOTALL)
head = head_match.group(1) if head_match else ''

header_match = re.search(r'(<header.*?</header>)', index_html, re.DOTALL)
header = header_match.group(1) if header_match else ''

footer_match = re.search(r'(<footer.*?</footer>)', index_html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

terms_content = """
<main class="w-full pt-32 pb-24 bg-background min-h-screen">
  <div class="max-w-[800px] mx-auto px-6 lg:px-8">
    
    <div class="mb-12">
      <h1 class="font-display text-4xl md:text-5xl text-on-surface font-bold tracking-tight mb-4">Terms of Service & Privacy Policy</h1>
      <p class="font-body-md text-on-surface-variant"><em>Last updated: [DATE]</em></p>
    </div>

    <div class="p-6 rounded-xl bg-surface-container border border-outline-variant/30 mb-12">
      <p class="font-body-sm text-on-surface-variant">
        <strong>Note before publishing:</strong> this is a working draft built from BoxMation's own offer, pilot, and guarantee terms. It is not a substitute for review by a lawyer familiar with outbound marketing, data privacy, and your operating jurisdiction. Have this reviewed before it governs real client contracts — this is especially important given outbound email/LinkedIn activity touches CAN-SPAM, GDPR, and platform terms of service. Do not treat this as the final legal document.
      </p>
    </div>

    <div class="space-y-12 text-on-surface-variant font-body-md leading-relaxed">
      
      <!-- TERMS SECTION -->
      <section>
        <h2 class="font-headline-lg text-3xl text-on-surface font-bold mb-6 border-b border-outline-variant/30 pb-4">Terms of Service</h2>
        
        <div class="space-y-8">
          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">1. The Service</h3>
            <p>BoxMation ("we," "us") provides automated email and LinkedIn outbound systems for B2B clients ("you," "the client"), including list building, enrichment, sequence design, deliverability infrastructure, lead scoring, and CRM routing, as described in the current Offer.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">2. What Is Not Included</h3>
            <p>Unless separately agreed and paid for in writing, BoxMation does not provide: content creation or personal branding services, SEO, paid advertising management, ambassador or affiliate program design, full GTM strategy documents, deal closing, or CRM systems beyond routing configuration. These are available as separate, individually scoped engagements.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">3. Pricing and Payment</h3>
            <ul class="list-disc pl-6 space-y-2">
              <li>Standard engagement: a one-time setup fee plus a recurring monthly retainer, as quoted at the time of agreement.</li>
              <li>Setup fees are due before work begins. Retainer is billed monthly in advance.</li>
              <li>Pricing is fixed for the duration of the client's engagement once agreed and does not change retroactively.</li>
              <li><strong>Pilot engagements</strong> (where offered) follow separate terms: a fixed pilot duration, tool costs only (no setup fee), and a defined conversion point to standard pricing, communicated in writing before the pilot begins.</li>
            </ul>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">4. Timeline and Guarantee</h3>
            <p class="mb-4">We commit to a "launch-ready" milestone (system built, tested, and live) by the timeline stated in your scope document. If that milestone is missed due to a delay on our part, we will extend the build at no additional cost until it is met.</p>
            <p>This is a commitment to build timeline and quality — <strong>it is not a guarantee of any specific number of meetings, leads, replies, or revenue outcome.</strong> Outbound performance depends on factors outside our control, including your market, your offer, and your team's responsiveness during setup.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">5. Client Responsibilities</h3>
            <p class="mb-3">To deliver on the committed timeline, you agree to:</p>
            <ul class="list-disc pl-6 space-y-2 mb-4">
              <li>Grant necessary access (domains, CRM, calendar) within the timeframe specified in your onboarding checklist</li>
              <li>Respond to approval requests (copy, targeting, sequences) within 2 business days</li>
              <li>Have someone available to handle and take booked meetings</li>
              <li>Provide accurate information about your business, offer, and target customers</li>
            </ul>
            <p>Delays on your end may extend the project timeline accordingly.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">6. Data and Compliance</h3>
            <ul class="list-disc pl-6 space-y-2">
              <li>We source contact data from providers we believe conduct their own compliance diligence. You are responsible for confirming that your target lists and messaging comply with applicable law (including CAN-SPAM, GDPR, and other regional regulations) in the markets you operate in.</li>
              <li>We honor opt-out and unsubscribe requests promptly across all managed channels.</li>
              <li>We do not knowingly send communications in violation of platform terms of service (LinkedIn, email providers) and reserve the right to pause or adjust campaigns that risk account restrictions.</li>
              <li>You retain ownership of your own client and prospect data collected through the engagement.</li>
            </ul>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">7. Term and Termination</h3>
            <ul class="list-disc pl-6 space-y-2">
              <li>Engagements are month-to-month following the initial setup and launch period, unless otherwise agreed in writing.</li>
              <li>Either party may terminate with 30 days' written notice.</li>
              <li>Fees paid for work already performed or in progress are non-refundable, except as described in Section 4.</li>
            </ul>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">8. Confidentiality</h3>
            <p>Both parties agree to keep confidential any non-public business information shared during the engagement, including client lists, pricing, and internal processes.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">9. Limitation of Liability</h3>
            <p>BoxMation's liability under any engagement is limited to the fees paid for the service period in question. We are not liable for indirect, consequential, or lost-profit damages arising from the use of the outbound system.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">10. Changes to These Terms</h3>
            <p>We may update these terms from time to time. Material changes will be communicated to active clients directly.</p>
          </div>
        </div>
      </section>

      <!-- PRIVACY SECTION -->
      <section class="mt-16 pt-16 border-t border-outline-variant/30">
        <h2 class="font-headline-lg text-3xl text-on-surface font-bold mb-6 border-b border-outline-variant/30 pb-4">Privacy Policy</h2>
        
        <div class="space-y-8">
          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">What We Collect</h3>
            <ul class="list-disc pl-6 space-y-2">
              <li><strong>From website visitors:</strong> standard analytics data (pages viewed, time on page, general location/device type) via our analytics tools.</li>
              <li><strong>From prospective clients:</strong> contact information you provide when booking a call or submitting an inquiry (name, email, company).</li>
              <li><strong>From clients:</strong> business information necessary to deliver the service (target customer data, CRM access, domain/sending infrastructure access).</li>
            </ul>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">How We Use It</h3>
            <ul class="list-disc pl-6 space-y-2 mb-4">
              <li>To respond to inquiries and schedule calls</li>
              <li>To deliver and improve the contracted service</li>
              <li>To understand how visitors use this website, so we can improve it</li>
            </ul>
            <p>We do not sell visitor or client data to third parties.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">Third-Party Tools</h3>
            <p>This site uses third-party tools for analytics (e.g., Vercel Analytics, PostHog) and scheduling (e.g., Zcal). These tools may collect data according to their own privacy policies, linked here: [insert links once finalized].</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">Data Retention</h3>
            <p>We retain client business data for the duration of the engagement and a reasonable period after, for record-keeping, unless you request earlier deletion.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">Your Rights</h3>
            <p>You may request access to, correction of, or deletion of your personal data by contacting us at [EMAIL]. If you are located in a jurisdiction with specific data rights (e.g., GDPR, CCPA), we will honor applicable requests under that law.</p>
          </div>

          <div>
            <h3 class="font-headline-sm text-xl text-on-surface font-semibold mb-3">Contact</h3>
            <p>Questions about these terms or this policy: [EMAIL]</p>
          </div>
        </div>
      </section>

    </div>
  </div>
</main>
"""

# We need to replace the relative anchor links in the header of terms.html to point to index.html#...
header_modified = header.replace('href="#', 'href="index.html#')

full_html = f"""<!DOCTYPE html>
<html class="dark" lang="en">
{head}
<body class="bg-background font-body-md text-on-surface antialiased selection:bg-primary-container selection:text-on-primary-container">
{header_modified}
{terms_content}
{footer}
</body>
</html>
"""

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

# Also update the footer link in index.html
index_html = index_html.replace('href="#" data-path="privacy-terms"', 'href="terms.html"')
index_html = index_html.replace('data-path="privacy-terms" href="#"', 'href="terms.html"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
