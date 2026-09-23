import codecs
from bs4 import BeautifulSoup

def add_script_to_terms():
    with codecs.open('d:/boxmation/terms.html', 'r', 'utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    script_html = """
<script>
 document.addEventListener("DOMContentLoaded", () => {
            
            // Mobile Menu Toggle
            const menuBtn = document.getElementById('mobile-menu-btn');
            const menu = document.getElementById('mobile-menu');
            if (menuBtn && menu) {
                const menuIcon = menuBtn.querySelector('.material-symbols-outlined');
                
                menuBtn.addEventListener('click', function() {
                    if (menu.classList.contains('hidden')) {
                        menu.classList.remove('hidden');
                        if (menuIcon) menuIcon.textContent = 'close';
                    } else {
                        menu.classList.add('hidden');
                        if (menuIcon) menuIcon.textContent = 'menu';
                    }
                });
                
                document.querySelectorAll('.mobile-link').forEach(function(link) {
                    link.addEventListener('click', function() {
                        menu.classList.add('hidden');
                        if (menuIcon) menuIcon.textContent = 'menu';
                    });
                });
            }

            // Smooth Scroll Reveal
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.15
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        // Stop observing once revealed
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            const revealElements = document.querySelectorAll('.reveal');
            revealElements.forEach(el => observer.observe(el));
        });
</script>
"""
    
    # Append to body
    soup.body.append(BeautifulSoup(script_html, 'html.parser'))

    with codecs.open('d:/boxmation/terms.html', 'w', 'utf-8') as f:
        f.write(str(soup))
    print("Added script to terms.html")

if __name__ == '__main__':
    add_script_to_terms()
