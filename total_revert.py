import codecs
import re

def revert_booking():
    # 1. Revert HTML
    filepath = 'd:/boxmation/booking.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    section = soup.find('section')
    if section:
        classes = section.get('class', [])
        if 'bg-transparent' in classes:
            classes.remove('bg-transparent')
        if 'bg-white' not in classes:
            classes.append('bg-white')
        section['class'] = classes

    card = soup.find('div', class_=lambda c: c and 'max-w-6xl' in c)
    if card:
        classes = card.get('class', [])
        if 'bg-white' in classes:
            classes.remove('bg-white')
        card['class'] = classes

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(str(soup))

    # 2. Revert JS
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    new_js = """// Booking Canvas Animation - Radar Sweep / Target Acquisition
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

    old_block = re.search(r'// Booking Canvas Animation.*?\}\);', js, flags=re.DOTALL)
    if old_block:
        js = js.replace(old_block.group(0), new_js)
        with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
            f.write(js)
            
    print("Reverted!")

if __name__ == '__main__':
    revert_booking()
