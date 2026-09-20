import re
import glob

# Extract the raw a tags from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<!-- Social Links Toolbar -->.*?<div[^>]*>(.*?)</div>', text, re.DOTALL)
if m:
    raw_links = m.group(1).strip()
    
    footer_icons = f'<div class="flex flex-wrap items-center gap-6">{raw_links}</div>'
    
    # We will inject this into the footer before the closing </div> of the bottom row
    # Bottom row looks like: <div class="pt-space-md flex flex-col sm:flex-row items-center justify-between gap-4 font-label-code text-label-code text-outline"><p> 2025 BoxMation...</p></div>
    
    for filepath in glob.glob('*.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Check if already injected
        if 'class="flex flex-wrap items-center gap-6"' in html and 'wa.me' in html and filepath != 'index.html':
            pass # might need to be careful not to duplicate
            
        # Target: </p></div></div></footer>
        target = '</p></div></div></footer>'
        
        if target in html:
            # We insert it right after the </p>
            html = html.replace('</p></div></div></footer>', f'</p>{footer_icons}</div></div></footer>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Injected into {filepath}")
        else:
            print(f"Target not found in {filepath}")
            # Try a different target in case copyright symbol messed it up
            # just look for built for zero-fluff outbound execution.</p></div>
            alt_target = 'outbound execution.</p></div>'
            if alt_target in html:
                html = html.replace(alt_target, f'outbound execution.</p>{footer_icons}</div>')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"Injected into {filepath} (alt target)")
else:
    print("Could not extract social links.")
