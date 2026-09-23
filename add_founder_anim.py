import codecs
import re

def add_founder_animation():
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    founder_canvas_js = """
// Founder Canvas Animation - Hex Matrix
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('founder-bg');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let mouse = { x: -1000, y: -1000 };
        
        function resize() {
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
        }
        
        window.addEventListener('resize', resize);
        resize();

        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
        });
        
        canvas.addEventListener('mouseleave', () => {
            mouse.x = -1000;
            mouse.y = -1000;
        });

        const columns = Math.floor(width / 40);
        const rows = Math.floor(height / 40);
        const grid = [];

        for (let i = 0; i < columns; i++) {
            grid[i] = [];
            for (let j = 0; j < rows; j++) {
                grid[i][j] = {
                    val: Math.random() > 0.5 ? '1' : '0',
                    targetVal: '',
                    timer: Math.random() * 100,
                    x: i * 40 + 20,
                    y: j * 40 + 20
                };
            }
        }

        const chars = '0123456789ABCDEF'.split('');

        function draw() {
            ctx.clearRect(0, 0, width, height);
            ctx.font = '12px "JetBrains Mono", monospace';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';

            for (let i = 0; i < grid.length; i++) {
                for (let j = 0; j < grid[i].length; j++) {
                    const cell = grid[i][j];
                    cell.timer--;
                    
                    if (cell.timer <= 0) {
                        cell.val = chars[Math.floor(Math.random() * chars.length)] + chars[Math.floor(Math.random() * chars.length)];
                        cell.timer = Math.random() * 50 + 20;
                    }

                    const dx = mouse.x - cell.x;
                    const dy = mouse.y - cell.y;
                    const dist = Math.sqrt(dx*dx + dy*dy);

                    if (dist < 100) {
                        ctx.fillStyle = '#03aa5c'; // ts-green
                        ctx.globalAlpha = 1 - (dist / 100);
                        // Make it type faster when mouse is near
                        if (Math.random() < 0.1) cell.timer = 0;
                    } else if (dist < 200) {
                        ctx.fillStyle = '#f386a1'; // ts-pink
                        ctx.globalAlpha = 0.3 - ((dist - 100) / 100) * 0.3;
                    } else {
                        ctx.fillStyle = '#e5e5e5';
                        ctx.globalAlpha = 0.2;
                    }

                    ctx.fillText(cell.val, cell.x, cell.y);
                }
            }
            
            requestAnimationFrame(draw);
        }
        
        draw();
    }
});
"""

    if 'founder-bg' not in js:
        with codecs.open('d:/boxmation/animations.js', 'a', 'utf-8') as f:
            f.write('\n' + founder_canvas_js)
        print("Injected founder animation JS.")

    # Now we need to add the canvas to founder.html
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    # We will put the canvas in the header block
    header_regex = r'(<div class="mb-20 text-center reveal">.*?)(<h1 class="font-display)'
    
    # Actually, we can put it behind the header absolutely positioned.
    # Let's wrap the header block in a relative container with the canvas.
    if '<canvas id="founder-bg"' not in html:
        # Find the max-w-[1000px] div that contains the header
        # The header is inside <div class="max-w-[1000px] mx-auto px-6 lg:px-8">
        # Let's just insert the canvas right after <main> and make it absolute top-0 left-0 w-full h-[500px] or something.
        # But wait, main is min-h-screen relative.
        canvas_html = '<canvas id="founder-bg" class="absolute top-0 left-0 w-full h-[600px] pointer-events-auto z-0" style="opacity: 0.8;"></canvas>\n'
        
        # Inject right after <main class="...">
        html = re.sub(r'(<main class="[^"]*relative[^"]*">)', r'\1\n' + canvas_html, html)
        
        with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
            f.write(html)
        print("Injected founder canvas into HTML.")

if __name__ == '__main__':
    add_founder_animation()
