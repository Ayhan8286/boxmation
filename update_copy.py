import glob
import os

files = glob.glob('*.html')
files = [f for f in files if not f.endswith('.bak')]

replacements = {
    # Footers & Meta tags
    "Automated LinkedIn + Email Outbound Systems for B2B Founders": "Full-Stack Outbound & Inbound Systems for B2B Founders",
    "Automated LinkedIn + Email Outbound Systems": "Full-Stack Outbound & Inbound Systems",
    "Built for zero-fluff outbound execution.": "Built for zero-fluff revenue execution.",
    "optimise your pipeline.": "optimise your revenue engine.",
    
    # index.html Hero & timeline
    "Automated Outbound Systems That": "Full-Stack Revenue Systems That",
    "We map your outbound motion in 25 minutes.": "We map your revenue motion in 25 minutes.",
    "14 days. Full AI outbound infrastructure": "14 days. Full outbound and inbound infrastructure",
    
    # founder.html
    "Built and run by an outbound systems specialist": "Built and run by a full-stack growth systems specialist",
    "I build outbound systems for a living": "I build outbound and inbound systems for a living"
}

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
        
    if content != original:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated copy in {fn}")
    else:
        print(f"No changes needed in {fn}")
