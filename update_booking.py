import codecs
import re

def update_booking():
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # 1. Swap the background canvas id
    html = html.replace('id="pricing-bg"', 'id="booking-bg"')

    # 2. Resize calendar and add a loader
    # Currently iframe is: <iframe class="w-full flex-grow min-h-[800px]" src="https://zcal.co/ayhan/boxmation?embed=1" style="border: none;"></iframe>
    # Parent is: <div class="bg-white border border-[#1e1e1e] w-full min-h-[800px] overflow-hidden flex flex-col relative z-10 brutalist-border">
    
    # Change parent height
    html = html.replace('min-h-[800px] overflow-hidden flex flex-col', 'h-[650px] overflow-hidden flex flex-col')
    
    # Change iframe height and add onload
    new_iframe = '<iframe class="w-full h-full relative z-10" src="https://zcal.co/ayhan/boxmation?embed=1" style="border: none;" onload="document.getElementById(\'cal-loader\').style.display=\'none\';"></iframe>'
    
    html = re.sub(r'<iframe[^>]*src="https://zcal.co/[^>]*></iframe>', new_iframe, html)
    
    # Inject the loader before the iframe
    loader_html = """
    <div id="cal-loader" class="absolute inset-0 bg-[#fafafa] flex flex-col items-center justify-center z-0">
        <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#1e1e1e] mb-4"></div>
        <span class="font-mono text-xs tracking-widest uppercase text-gray-500">Initializing Booking Node...</span>
    </div>
    """
    
    # We find the parent div to inject the loader
    parent_tag = r'(<div class="bg-white border border-\[#1e1e1e\] w-full h-\[650px\] overflow-hidden flex flex-col relative z-10 brutalist-border">)'
    html = re.sub(parent_tag, r'\1\n' + loader_html, html)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
        
    print("Updated booking.html layout and added loader.")

if __name__ == '__main__':
    update_booking()
