import codecs

def fix_js():
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    idx = js.find('// Booking Canvas Animation')
    if idx != -1:
        js = js[:idx].strip() + '\n\n'

    booking_js = """// Booking Canvas Animation - Radar Sweep / Target Acquisition
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('booking-bg');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let centerX, centerY;
        let angle = 0;
        
        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            centerX = width / 2;
            centerY = height / 2;
        }
        
        window.addEventListener('resize', resize);
        resize();

        const targets = [];
        for (let i = 0; i < 30; i++) {
            targets.push({
                x: Math.random() * width,
                y: Math.random() * height,
                alpha: 0,
                baseRadius: Math.random() * 3 + 2,
                color: Math.random() > 0.5 ? '#03aa5c' : '#f386a1'
            });
        }

        function draw() {
            ctx.clearRect(0, 0, width, height);
            
            ctx.strokeStyle = 'rgba(30, 30, 30, 0.3)';
            ctx.lineWidth = 1;
            for (let r = 100; r < Math.max(width, height); r += 100) {
                ctx.beginPath();
                ctx.arc(centerX, centerY, r, 0, Math.PI * 2);
                ctx.stroke();
            }

            const sweepLength = Math.max(width, height);
            const sweepX = centerX + Math.cos(angle) * sweepLength;
            const sweepY = centerY + Math.sin(angle) * sweepLength;
            
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(sweepX, sweepY);
            ctx.strokeStyle = 'rgba(30, 30, 30, 0.5)';
            ctx.lineWidth = 2;
            ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.arc(centerX, centerY, sweepLength, angle - 0.3, angle, false);
            ctx.lineTo(centerX, centerY);
            const grad = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, sweepLength);
            grad.addColorStop(0, 'rgba(30, 30, 30, 0.0)');
            grad.addColorStop(1, 'rgba(30, 30, 30, 0.1)');
            ctx.fillStyle = grad;
            ctx.fill();

            targets.forEach(t => {
                let tAngle = Math.atan2(t.y - centerY, t.x - centerX);
                if (tAngle < 0) tAngle += Math.PI * 2;
                
                let normalizedSweep = angle % (Math.PI * 2);
                if (normalizedSweep < 0) normalizedSweep += Math.PI * 2;
                
                let angleDiff = normalizedSweep - tAngle;
                if (angleDiff < 0) angleDiff += Math.PI * 2;
                
                if (angleDiff < 0.1) {
                    t.alpha = 1;
                }
                
                if (t.alpha > 0) {
                    ctx.beginPath();
                    ctx.arc(t.x, t.y, t.baseRadius, 0, Math.PI * 2);
                    ctx.fillStyle = t.color;
                    ctx.save();
                    ctx.globalAlpha = t.alpha;
                    ctx.fill();
                    
                    ctx.beginPath();
                    ctx.arc(t.x, t.y, t.baseRadius + (1 - t.alpha) * 10, 0, Math.PI * 2);
                    ctx.strokeStyle = t.color;
                    ctx.stroke();
                    ctx.restore();
                    
                    t.alpha -= 0.02;
                }
            });

            angle += 0.02;
            requestAnimationFrame(draw);
        }
        
        draw();
    }
});"""

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js + booking_js + '\n')
        
    print("Fixed animations.js")

if __name__ == '__main__':
    fix_js()
