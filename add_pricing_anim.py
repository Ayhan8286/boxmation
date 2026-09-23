import codecs

def add_pricing_animation():
    # 1. Add the canvas to pricing.html
    with codecs.open('d:/boxmation/pricing.html', 'r', 'utf-8') as f:
        html = f.read()
        
    canvas_html = '\n<canvas id="pricing-bg" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0" style="opacity: 0.6;"></canvas>\n'
    
    # pricing.html has a `<div class="pt-24 pb-16 px-6 lg:px-8 relative z-10">` which is inside the `<body>`.
    # Let's inject it right after `<body class="antialiased">`
    if '<canvas id="pricing-bg"' not in html:
        html = html.replace('<body class="antialiased">', '<body class="antialiased">' + canvas_html)
        with codecs.open('d:/boxmation/pricing.html', 'w', 'utf-8') as f:
            f.write(html)
            
    # 2. Add the JS logic to animations.js
    pricing_js = """
// Pricing Canvas Animation - Data Pipeline
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('pricing-bg');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        
        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        
        window.addEventListener('resize', resize);
        resize();

        const packets = [];
        const linesX = [];
        const linesY = [];
        
        // Generate fixed tracks
        for (let i = 0; i < 15; i++) {
            linesX.push(Math.random() * 2000); // Wait, we will assign them based on width/height dynamically
        }

        class Packet {
            constructor() {
                this.reset();
            }
            
            reset() {
                this.axis = Math.random() > 0.5 ? 'x' : 'y';
                this.dir = Math.random() > 0.5 ? 1 : -1;
                this.speed = Math.random() * 2 + 1;
                this.length = Math.random() * 40 + 20;
                
                // Color choices: Pink, Green, Dark
                const colors = ['#03aa5c', '#f386a1', '#1e1e1e'];
                this.color = colors[Math.floor(Math.random() * colors.length)];
                
                if (this.axis === 'x') {
                    this.y = Math.floor(Math.random() * (height / 50)) * 50;
                    this.x = this.dir === 1 ? -this.length : width + this.length;
                } else {
                    this.x = Math.floor(Math.random() * (width / 50)) * 50;
                    this.y = this.dir === 1 ? -this.length : height + this.length;
                }
            }
            
            update() {
                if (this.axis === 'x') {
                    this.x += this.speed * this.dir;
                    if (this.dir === 1 && this.x > width + this.length) this.reset();
                    if (this.dir === -1 && this.x < -this.length) this.reset();
                } else {
                    this.y += this.speed * this.dir;
                    if (this.dir === 1 && this.y > height + this.length) this.reset();
                    if (this.dir === -1 && this.y < -this.length) this.reset();
                }
            }
            
            draw() {
                ctx.beginPath();
                ctx.strokeStyle = this.color;
                ctx.lineWidth = 2;
                if (this.axis === 'x') {
                    ctx.moveTo(this.x, this.y);
                    ctx.lineTo(this.x - (this.length * this.dir), this.y);
                } else {
                    ctx.moveTo(this.x, this.y);
                    ctx.lineTo(this.x, this.y - (this.length * this.dir));
                }
                ctx.stroke();
            }
        }

        for (let i = 0; i < 40; i++) {
            packets.push(new Packet());
        }

        function draw() {
            ctx.clearRect(0, 0, width, height);
            
            // Draw background grid lightly
            ctx.strokeStyle = 'rgba(30,30,30,0.03)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            for (let x = 0; x < width; x += 50) {
                ctx.moveTo(x, 0);
                ctx.lineTo(x, height);
            }
            for (let y = 0; y < height; y += 50) {
                ctx.moveTo(0, y);
                ctx.lineTo(width, y);
            }
            ctx.stroke();

            // Draw packets
            packets.forEach(p => {
                p.update();
                p.draw();
            });
            
            requestAnimationFrame(draw);
        }
        
        draw();
    }
});
"""

    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()
        
    if 'pricing-bg' not in js:
        with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
            f.write(js + "\n" + pricing_js)
            
    print("Added pricing data pipeline animation.")

if __name__ == '__main__':
    add_pricing_animation()
