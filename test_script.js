
        document.addEventListener("DOMContentLoaded", () => {
            
            // Mobile Menu Toggle
            const menuBtn = document.getElementById('mobile-menu-btn');
            const menu = document.getElementById('mobile-menu');
            const menuIcon = menuBtn.querySelector('.material-symbols-outlined');
            
            menuBtn.addEventListener('click', function() {
                if (menu.classList.contains('hidden')) {
                    menu.classList.remove('hidden');
                    menuIcon.textContent = 'close';
                } else {
                    menu.classList.add('hidden');
                    menuIcon.textContent = 'menu';
                }
            });
            
            document.querySelectorAll('.mobile-link').forEach(function(link) {
                link.addEventListener('click', function() {
                    menu.classList.add('hidden');
                    menuIcon.textContent = 'menu';
                });
            });

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
    