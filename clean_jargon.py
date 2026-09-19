replacements = {
    "Clay Waterfall Data Enrichment:": "Multi-Layer Data Enrichment:",
    "Domain &amp; Deliverability Cluster (Instantly/Smartlead):": "Domain &amp; Deliverability Cluster:",
    "Domain & Deliverability Cluster (Instantly/Smartlead):": "Domain & Deliverability Cluster:",
    "HeyReach Automated LinkedIn Sequences:": "Automated LinkedIn Sequences:",
    "HubSpot CRM Direct Routing &amp; Scoring:": "CRM Direct Routing &amp; Scoring:",
    "HubSpot CRM Direct Routing & Scoring:": "CRM Direct Routing & Scoring:",
    "Email + HeyReach LinkedIn": "Email + LinkedIn",
    "HubSpot CRM Routed": "CRM Routed",
    "Procurement &amp; DNS configuration of 10+ clean secondary domains": "Procurement &amp; configuration of 10+ clean secondary sending domains",
    "Procurement & DNS configuration of 10+ clean secondary domains": "Procurement & configuration of 10+ clean secondary sending domains",
    "waterfall schemas &amp; API webhooks": "waterfall schemas &amp; routing automations",
    "waterfall schemas & API webhooks": "waterfall schemas & routing automations",
    "DKIM/SPF setup, Clay waterfall enrichment schema build": "Email authentication setup, data enrichment schema build",
    "DKIM/SPF setup, Clay": "Authentication setup, data",
    "HeyReach multi-touch connection copy": "LinkedIn multi-touch connection copy",
    "HubSpot webhook routing configured": "CRM routing configured",
    "HubSpot webhook routing": "CRM routing",
    "Agency pays for Clay, ZoomInfo, SalesNav (~$1,200/mo)": "Agency pays for multiple expensive data tools (~$1,200/mo)",
    "Turnkey engineered stack (Clay + HeyReach + Instantly)": "Turnkey engineered outbound stack",
    "HubSpot pipeline integration": "CRM pipeline integration",
    "deploy synchronized LinkedIn outreach via HeyReach, and route qualified responses directly into your HubSpot pipeline.": "deploy synchronized LinkedIn outreach, and route qualified responses directly into your CRM pipeline.",
    "Clay": "Data", # Generic fallback if any isolated ones remain
    "HeyReach": "LinkedIn",
    "Instantly": "our sending infrastructure",
    "Smartlead": "sending tools",
    "HubSpot": "CRM",
    "DKIM/SPF": "authentication",
    "ZoomInfo": "data tools",
    "SalesNav": "sales tools",
    "API webhooks": "automations"
}

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# First replace specific long phrases
for k, v in list(replacements.items())[:21]:
    html = html.replace(k, v)

# Then do a pass for isolated terms but we have to be careful not to break HTML classes/IDs or text we already changed.
# Actually, the specific long phrases should cover 99% of them. Let's write it to see.
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Replaced jargon.")
