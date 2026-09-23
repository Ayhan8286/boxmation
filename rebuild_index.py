import re

with open('d:/boxmation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I need to rebuild index.html to reflect all the changes:
# 1. Add Canvas
html = html.replace('<section class="relative w-full overflow-hidden py-24 md:py-32 bg-white flex flex-col justify-center items-center text-center brutalist-border ">', '<section class="relative w-full overflow-hidden py-24 md:py-32 bg-white flex flex-col justify-center items-center text-center brutalist-border min-h-[80vh]">\n<canvas id="hero-bg" class="absolute inset-0 w-full h-full z-0 opacity-60"></canvas>')

# 2. Inject animations.js
if 'animations.js' not in html:
    html = html.replace('</body>', '<script src="animations.js"></script>\n</body>')
    
# 3. Remove Wedge, Comparison, Pricing, Booking
for target_id in ['transparent-offer', 'the-wedge', 'compare-vs-in-house', 'book-discovery']:
    match = re.search(f'(<section[^>]*id="{target_id}".*?</section>)', html, flags=re.DOTALL)
    if match:
        html = html.replace(match.group(1), '')
        
# 4. Remove the Visual Presentation Frame (founder picture)
match_pic = re.search(r'(<!-- Visual Presentation Frame -->\s*<div class="lg:col-span-5 relative">.*?<!-- Floating Live Card -->.*?</div>\s*</div>\s*</div>\s*</div>)', html, flags=re.DOTALL)
if match_pic:
    html = html.replace(match_pic.group(1), '')
    
# 5. Make the founder text full width
html = html.replace('<div class="lg:col-span-7">', '<div class="lg:col-span-12 max-w-4xl mx-auto">')

# 6. Update links
html = html.replace('href="#transparent-offer"', 'href="/pricing.html"')
html = html.replace('href="/#transparent-offer"', 'href="/pricing.html"')
html = html.replace('href="#book-discovery"', 'href="/booking.html"')
html = html.replace('href="/#book-discovery"', 'href="/booking.html"')
html = html.replace('href="#contact"', 'href="/booking.html"')
html = html.replace('href="/#contact"', 'href="/booking.html"')

# 7. Remove wedge and compare links
html = re.sub(r'<a[^>]*href="[^"]*the-wedge"[^>]*>.*?</a>\s*', '', html)
html = re.sub(r'<a[^>]*href="[^"]*compare-vs-in-house"[^>]*>.*?</a>\s*', '', html)

# 8. Selection color
html = html.replace('background-color: var(--ts-magenta);', 'background-color: var(--ts-dark);')

# 9. Top button color
html = re.sub(
    r'(<a[^>]*class="[^"]*)text-white bg-\[var\(--ts-green\)\] text-\[var\(--ts-white\)\] hover:bg-\[var\(--ts-teal\)\]( brutalist-button"[^>]*href="[^"]*book[^>]*>.*?<span[^>]*>Book Fit Call / Discovery</span>)',
    r'\1bg-white text-black hover:bg-gray-100 border border-[#1e1e1e]\2',
    html,
    flags=re.DOTALL
)

with open('d:/boxmation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored index.html and applied all changes!")
