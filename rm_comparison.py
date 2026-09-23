import os
import re

def remove_comparison_section():
    # 1. Remove the section from index.html
    index_path = 'd:/boxmation/index.html'
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # The section probably starts with <section... id="compare-vs-in-house">
        # Let's find it.
        match = re.search(r'(<!-- 6\. COMPARISON .*?<section[^>]*id="compare-vs-in-house".*?</section>)', content, flags=re.DOTALL)
        if match:
            content = content.replace(match.group(1), '')
        else:
            # Fallback if comment is missing
            match = re.search(r'(<section[^>]*id="compare-vs-in-house".*?</section>)', content, flags=re.DOTALL)
            if match:
                content = content.replace(match.group(1), '')
                
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)

    # 2. Remove links to #compare-vs-in-house from all HTML files
    files = ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']
    for filename in files:
        path = f'd:/boxmation/{filename}'
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to remove anchor tags with href="#compare-vs-in-house" or href="/#compare-vs-in-house"
        content = re.sub(r'<a[^>]*href="[^"]*compare-vs-in-house"[^>]*>.*?</a>\s*', '', content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    remove_comparison_section()
    print("Successfully removed Comparison section and all navigation links.")
