with open('terms.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace date
html = html.replace('[DATE]', 'September 20, 2026')
# Replace emails
html = html.replace('[EMAIL]', 'boxmation.labs@gmail.com')
# Replace provider
html = html.replace('[scheduling provider]', 'Zcal')
# Replace links note
html = html.replace('linked here: [insert links once finalized]', 'available on their respective platforms')

# Remove the warning div entirely. Let's find it.
start_str = '<div class="p-6 rounded-xl bg-surface-container border border-outline-variant/30 mb-12">'
end_str = '</div>'

start_idx = html.find(start_str)
if start_idx != -1:
    # Find the matching closing div for this block.
    # The block contains a <p> and then a </div>
    next_div_close = html.find('</div>', start_idx)
    # Actually, it's just the immediate next </div> because there are no nested divs inside it
    if next_div_close != -1:
        # include the </div> in the cut
        html = html[:start_idx] + html[next_div_close + 6:]

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(html)
