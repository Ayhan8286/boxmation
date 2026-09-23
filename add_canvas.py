import codecs

code = """
    // 4. Hero Background Canvas Animation (Machine-Native Network)
    const canvas = document.getElementById('hero-bg');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];

        function resize() {
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
        }

        window.addEventListener('resize', resize);
        resize();

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 1.5;
                this.vy = (Math.random() - 0.5) * 1.5;
                this.color = Math.random() > 0.5 ? '#03aa5c' : '#f386a1';
                this.char = ['{', '}', '[', ']', 'int', 'str', '=>', '||'][Math.floor(Math.random()*8)];
            }
            update() {
                this.x += this.vx;
                this.y += this.vy;
                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;
            }
            draw() {
                ctx.fillStyle = this.color;
                ctx.font = '12px "JetBrains Mono", monospace';
                ctx.fillText(this.char, this.x, this.y);
            }
        }

        for (let i = 0; i < 60; i++) {
            particles.push(new Particle());
        }

        function animateBg() {
            ctx.clearRect(0, 0, width, height);
            
            // Draw connections
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx*dx + dy*dy);
                    
                    if (dist < 150) {
                        ctx.beginPath();
                        ctx.strokeStyle = '#1e1e1e';
                        ctx.globalAlpha = 1 - (dist / 150);
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                        ctx.globalAlpha = 1.0;
                    }
                }
            }

            particles.forEach(p => {
                p.update();
                p.draw();
            });

            requestAnimationFrame(animateBg);
        }

        animateBg();
    }
});
"""

with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
    original = f.read()

# Replace the closing "});" of the DOMContentLoaded event with our code,
# so the canvas logic runs when the DOM is ready.
new_content = original.replace('});', code)

with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
    f.write(new_content)
