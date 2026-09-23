import codecs
import re

def dual_radar():
    new_js = """// Booking Canvas Animation - Dual Radar Sweep
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('booking-bg');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let angle = 0;
        
        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        
        window.addEventListener('resize', resize);
        resize();

        const targets = [];
        // Generate targets
        for (let i = 0; i < 50; i++) {
            targets.push({
                x: Math.random() * width,
                y: Math.random() * height,
                alpha: 0,
                baseRadius: Math.random() * 4 + 3,
                color: Math.random() > 0.5 ? '#03aa5c' : '#f386a1'
            });
        }

        function drawRadar(cx, cy) {
            // Draw concentric radar rings
            ctx.strokeStyle = 'rgba(30, 30, 30, 0.3)';
            ctx.lineWidth = 1;
            for (let r = 100; r < Math.max(width, height) * 1.5; r += 100) {
                ctx.beginPath();
                ctx.arc(cx, cy, r, 0, Math.PI * 2);
                ctx.stroke();
            }

            // Draw sweep line
            const sweepLength = Math.max(width, height) * 1.5;
            const sweepX = cx + Math.cos(angle) * sweepLength;
            const sweepY = cy + Math.sin(angle) * sweepLength;
            
            ctx.beginPath();
            ctx.moveTo(cx, cy);
            ctx.lineTo(sweepX, sweepY);
            ctx.strokeStyle = 'rgba(30, 30, 30, 0.5)';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Draw sweep gradient
            ctx.beginPath();
            ctx.moveTo(cx, cy);
            ctx.arc(cx, cy, sweepLength, angle - 0.3, angle, false);
            ctx.lineTo(cx, cy);
            const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, sweepLength);
            grad.addColorStop(0, 'rgba(30, 30, 30, 0.0)');
            grad.addColorStop(1, 'rgba(30, 30, 30, 0.1)');
            ctx.fillStyle = grad;
            ctx.fill();
            
            // Check targets against this radar
            targets.forEach(t => {
                let tAngle = Math.atan2(t.y - cy, t.x - cx);
                if (tAngle < 0) tAngle += Math.PI * 2;
                
                let normalizedSweep = angle % (Math.PI * 2);
                if (normalizedSweep < 0) normalizedSweep += Math.PI * 2;
                
                let angleDiff = normalizedSweep - tAngle;
                if (angleDiff < 0) angleDiff += Math.PI * 2;
                
                if (angleDiff < 0.1) {
                    t.alpha = 1; // Ping!
                }
            });
        }

        function draw() {
            ctx.clearRect(0, 0, width, height);
            
            // Draw TWO radars (one on left, one on right) so they are visible around the center card
            drawRadar(width * 0.15, height / 2);
            drawRadar(width * 0.85, height / 2);

            // Draw targets
            targets.forEach(t => {
                if (t.alpha > 0) {
                    ctx.beginPath();
                    ctx.arc(t.x, t.y, t.baseRadius, 0, Math.PI * 2);
                    ctx.fillStyle = t.color;
                    ctx.save();
                    ctx.globalAlpha = t.alpha;
                    ctx.fill();
                    
                    ctx.beginPath();
                    ctx.arc(t.x, t.y, t.baseRadius + (1 - t.alpha) * 15, 0, Math.PI * 2);
                    ctx.strokeStyle = t.color;
                    ctx.lineWidth = 2;
                    ctx.stroke();
                    ctx.restore();
                    
                    t.alpha -= 0.015;
                }
            });

            angle += 0.02;
            requestAnimationFrame(draw);
        }
        
        draw();
    }
});"""

    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    old_block = re.search(r'// Booking Canvas Animation.*?\}\);', js, flags=re.DOTALL)
    if old_block:
        js = js.replace(old_block.group(0), new_js)
        with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
            f.write(js)
        print('Updated to dual radar!')

if __name__ == '__main__':
    dual_radar()
