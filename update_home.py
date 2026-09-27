import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "Without hiring a costly SDR, managing flaky freelancers": "Without hiring a costly SDR, juggling multiple ad agencies",
    "From zero to a live, sending pipeline.": "From zero to a live, revenue-generating system.",
    "optimise your pipeline month": "optimise your entire growth engine month",
    "The pipeline runs 24/7. Prospects enriched, emails sent": "The system runs 24/7. Prospects enriched, visitors identified, emails sent",
    "EVERY AGENCY SELLS YOU A SPREADSHEET AND A SCRIPT.": "EVERY AGENCY SELLS YOU ONE PIECE OF THE PUZZLE.",
    "The standard outbound playbook: buy a contact list, blast 500 emails, hope. Agencies optimise for volume. They count sends, not conversations.": "The standard agency playbook: buy a list and blast emails, or run ads with zero follow-up. They optimise for volume and vanity metrics.",
    "what if outbound worked like software?": "what if growth worked like a unified software product?",
    "We built Boxmation to be a pipeline system": "We built BoxMation to be a full-stack revenue system",
    
    "ERR follow_up: manual": "ERR inbound_leads: lost",
    "ERR reply_handling: unassigned": "ERR outbound_touches: zero",
    "ERR pipeline_result: 0 meetings": "ERR revenue_result: 0 meetings",
    "exit code 1 — pipeline failed": "exit code 1 — system failed",
    
    "OK leads_enriched: verified": "OK visitors_identified: true",
    "OK copy_personalised: AI-generated": "OK inbound_outbound: unified",
    
    "pipeline operational": "system operational",
    "THIS IS WHAT YOUR PIPELINE LOOKS LIKE": "THIS IS WHAT YOUR REVENUE ENGINE LOOKS LIKE",
    "Every lead researched, verified, and personalised before a single email goes out.": "Every lead researched, anonymous visitor identified, and outreach personalised.",
    
    "Get your pipeline built": "Get your system built",
    "Real pipelines are built": "Real systems are built",
    "Every pipeline we build": "Every system we build",
    
    "Sending infrastructure set up and warming, target list built and enriched with verified contact data.": "Outbound infrastructure set up, inbound tracking pixels placed, and target lists enriched.",
    "Email and LinkedIn sequences written, reviewed, and approved with you.": "Email/LinkedIn sequences written, and website visitor identification configured.",
    "Outbound running across email and LinkedIn. Reporting dashboard active.": "Systems running across email, LinkedIn, website, and ads. Unified dashboard active."
}

original = content
for old_t, new_t in replacements.items():
    content = content.replace(old_t, new_t)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Homepage copy updated.")
