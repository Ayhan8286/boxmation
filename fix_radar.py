import codecs
import re

def fix_radar_centering():
    # 1. Update the HTML files to make the canvas fixed again
    for page in ['pricing.html', 'booking.html']:
        with codecs.open(f'd:/boxmation/{page}', 'r', 'utf-8') as f:
            html = f.read()
            
        html = html.replace('class="absolute inset-0 w-full h-full pointer-events-none z-0"', 'class="fixed top-0 left-0 w-full h-full pointer-events-none z-0"')
        
        with codecs.open(f'd:/boxmation/{page}', 'w', 'utf-8') as f:
            f.write(html)
            
    # 2. Update animations.js to use window innerWidth/innerHeight for both animations
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()
        
    # For Pricing
    # Currently: width = canvas.width = canvas.offsetWidth; height = canvas.height = canvas.offsetHeight;
    pricing_block = re.search(r'(// Pricing Canvas Animation.*?)(function resize\(\) \{)(.*?)(^\s*\})', js, flags=re.DOTALL | re.MULTILINE)
    if pricing_block:
        new_pricing = pricing_block.group(0).replace('canvas.offsetWidth', 'window.innerWidth').replace('canvas.offsetHeight', 'window.innerHeight')
        js = js.replace(pricing_block.group(0), new_pricing)
        
    # For Booking
    booking_block = re.search(r'(// Booking Canvas Animation.*?)(function resize\(\) \{)(.*?)(^\s*\})', js, flags=re.DOTALL | re.MULTILINE)
    if booking_block:
        new_booking = booking_block.group(0).replace('canvas.offsetWidth', 'window.innerWidth').replace('canvas.offsetHeight', 'window.innerHeight')
        js = js.replace(booking_block.group(0), new_booking)

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)
        
    print("Fixed canvas positioning to fixed viewport.")

if __name__ == '__main__':
    fix_radar_centering()
