import os
import re

def process_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 4. Text selection color
    content = content.replace('background-color: var(--ts-magenta);', 'background-color: var(--ts-dark);')
    content = content.replace('color: var(--ts-white);', 'color: var(--ts-white);') # already white
    
    # 5. Button at the top should be white
    # The header button:
    # <a class="... text-white bg-[var(--ts-green)] text-[var(--ts-white)] hover:bg-[var(--ts-teal)] brutalist-button" href="/#book-discovery">
    # We will just regex replace the specific classes on the header button.
    # It's inside <header>...
    content = re.sub(
        r'(<a[^>]*class="[^"]*)text-white bg-\[var\(--ts-green\)\] text-\[var\(--ts-white\)\] hover:bg-\[var\(--ts-teal\)\]( brutalist-button"[^>]*href="[^"]*book-discovery"[^>]*>.*?<span[^>]*>Book Fit Call / Discovery</span>)',
        r'\1bg-white text-black hover:bg-gray-100 border border-[#1e1e1e]\2',
        content,
        flags=re.DOTALL
    )

    # 3. Founder picture B&W filter
    # The founder img has alt="BoxMation Systems Architect"
    content = re.sub(
        r'(<img[^>]*alt="BoxMation Systems Architect"[^>]*class=")([^"]*)(")',
        r'\1\2 grayscale contrast-125\3',
        content
    )

    # 2. Update links to booking page
    content = content.replace('href="#book-discovery"', 'href="/booking.html"')
    content = content.replace('href="/#book-discovery"', 'href="/booking.html"')
    # Same for contact just in case
    content = content.replace('href="#contact"', 'href="/booking.html"')
    content = content.replace('href="/#contact"', 'href="/booking.html"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    with open('d:/boxmation/index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    # 1. Remove "The One Wedge" section
    # Let's find it. It has id="the-wedge" probably, or we can search for the text.
    # Section starts with <section... id="the-wedge">
    wedge_match = re.search(r'(<!-- 5\. THE WEDGE .*?<section[^>]*id="the-wedge".*?</section>)', index_html, flags=re.DOTALL)
    if wedge_match:
        index_html = index_html.replace(wedge_match.group(1), '')
    else:
        # Fallback if comment is missing
        wedge_match = re.search(r'(<section[^>]*id="the-wedge".*?</section>)', index_html, flags=re.DOTALL)
        if wedge_match:
            index_html = index_html.replace(wedge_match.group(1), '')

    # Remove wedge from nav links
    index_html = re.sub(r'<a[^>]*href="/#the-wedge"[^>]*>.*?</a>\s*', '', index_html)

    # 2. Extract Book Discovery section
    book_match = re.search(r'(<section[^>]*id="book-discovery".*?</section>)', index_html, flags=re.DOTALL)
    booking_section = ""
    if book_match:
        booking_section = book_match.group(1)
        index_html = index_html.replace(booking_section, '')

    # Write back index.html before processing it
    with open('d:/boxmation/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    # Create booking.html using pricing.html as template
    with open('d:/boxmation/pricing.html', 'r', encoding='utf-8') as f:
        pricing_html = f.read()

    # Replace <main> contents with booking_section
    match_main = re.search(r'(<main[^>]*>).*?(</main>)', pricing_html, flags=re.DOTALL)
    if match_main and booking_section:
        booking_html = pricing_html[:match_main.start()] + f"{match_main.group(1)}\n{booking_section}\n{match_main.group(2)}" + pricing_html[match_main.end():]
        booking_html = booking_html.replace('<title>BoxMation - Pricing & Offer</title>', '<title>BoxMation - Book a Call</title>')
        # Remove active menu highlighting if any, or adjust nav
        
        with open('d:/boxmation/booking.html', 'w', encoding='utf-8') as f:
            f.write(booking_html)

    # Now process all html files for other updates
    for file in ['index.html', 'founder.html', 'pricing.html', 'booking.html', 'terms.html']:
        process_file(f'd:/boxmation/{file}')

if __name__ == '__main__':
    main()
