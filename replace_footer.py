import codecs
from bs4 import BeautifulSoup

def replace_footer():
    with codecs.open('d:/boxmation/terms.html', 'r', 'utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    footer = soup.find('footer')

    if footer:
        new_footer_html = """
<footer class="w-full bg-white py-20 border-t border-[#1e1e1e] brutalist-border" id="contact">
 <div class="max-w-[1240px] mx-auto px-6 lg:px-8">
  <div class="flex flex-col items-center justify-center gap-6 text-center">
   <div class="space-y-2">
    <div class="font-display text-3xl font-bold text-black uppercase tracking-tighter">BoxMation</div>
    <p class="font-mono text-xs text-gray-500 uppercase tracking-widest">Automated LinkedIn + Email Outbound Systems for B2B Founders</p>
   </div>
   <div class="flex flex-wrap justify-center items-center gap-6 text-sm font-semibold text-gray-700 mt-4">
    <a class="hover:text-black transition-colors" href="/founder.html">The Founder</a>
    <a class="hover:text-black transition-colors" href="/pricing.html">Pricing &amp; Offer</a>
    <a class="hover:text-black transition-colors" href="/booking.html">Contact</a>
    <a class="hover:text-black transition-colors" href="/terms.html">Terms &amp; Privacy</a>
   </div>
   <div class="pt-8 w-full border-t border-gray-100 mt-4">
    <p class="font-mono text-xs font-bold text-gray-400 uppercase tracking-wider">
     © 2026 BoxMation Systems Inc. Built for zero-fluff outbound execution.
    </p>
   </div>
  </div>
 </div>
</footer>
"""
        footer.replace_with(BeautifulSoup(new_footer_html, 'html.parser').find('footer'))

    with codecs.open('d:/boxmation/terms.html', 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Replaced footer!")

if __name__ == '__main__':
    replace_footer()
