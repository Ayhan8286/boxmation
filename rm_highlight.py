import os

for filename in ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']:
    path = f'd:/boxmation/{filename}'
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We want to remove the green highlight background from normal text, 
    # but keep it if it's the hero text "Fill Your Calendar" which is pink now, or anything similar.
    # The user specifically mentioned the checkboxes in booking.
    html = html.replace('<span class="bg-[var(--ts-green)] text-white px-2">You\'re the founder', '<span>You\'re the founder')
    html = html.replace('<span class="bg-[var(--ts-green)] text-white px-2">Revenue is roughly', '<span>Revenue is roughly')
    html = html.replace('<span class="bg-[var(--ts-green)] text-white px-2">You\'re ready to start', '<span>You\'re ready to start')
    
    # Let's also just remove it globally if it was mistakenly applied anywhere else except the buttons
    # Wait, the buttons also had it inside: <span class="bg-[var(--ts-green)] text-white px-2">Book Discovery Call</span>
    # The user didn't mention the buttons, just the text. I'll stick to removing it from those specific 3 lines.
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
