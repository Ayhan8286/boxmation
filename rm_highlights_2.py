import os
import re

files = ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']
for filename in files:
    path = f'd:/boxmation/{filename}'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove pink hover from guarantee section
    html = html.replace('hover:bg-[var(--ts-magenta)]', '')

    # 2. Remove green background span inside the buttons
    html = html.replace('<span class="bg-[var(--ts-green)] text-white px-2">Book Discovery Call</span>', '<span>Book Discovery Call</span>')
    html = html.replace('<span class="bg-[var(--ts-green)] text-white px-2">See The Fixed Offer</span>', '<span>See The Fixed Offer</span>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Removed pink highlight from hover and green highlights from buttons.")
