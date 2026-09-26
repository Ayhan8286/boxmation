// typesafe-animations.js
document.addEventListener('DOMContentLoaded', () => {
    // 1. Scroll Reveal Animation using IntersectionObserver
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            } else {
                entry.target.classList.remove('active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach((el) => {
        observer.observe(el);
    });

    document.querySelectorAll('.bento-grid').forEach((grid) => {
        const children = Array.from(grid.children);
        children.forEach((child, index) => {
            child.classList.add('reveal');
            child.style.transitionDelay = `${index * 100}ms`;
            observer.observe(child);
        });
    });

    // 2. Machine-Native Text Scramble Effect
    class TextScramble {
        constructor(el) {
            this.el = el;
            this.chars = '!<>-_\\\\/[]{}—=+*^?#________';
            this.update = this.update.bind(this);
        }
        
        setText(newText) {
            const oldText = this.el.innerText;
            const length = Math.max(oldText.length, newText.length);
            const promise = new Promise((resolve) => this.resolve = resolve);
            this.queue = [];
            for (let i = 0; i < length; i++) {
                const from = oldText[i] || '';
                const to = newText[i] || '';
                const start = Math.floor(Math.random() * 40);
                const end = start + Math.floor(Math.random() * 40);
                this.queue.push({ from, to, start, end });
            }
            cancelAnimationFrame(this.frameRequest);
            this.frame = 0;
            this.update();
            return promise;
        }
        
        update() {
            let output = '';
            let complete = 0;
            for (let i = 0, n = this.queue.length; i < n; i++) {
                let { from, to, start, end, char } = this.queue[i];
                if (this.frame >= end) {
                    complete++;
                    output += to;
                } else if (this.frame >= start) {
                    if (!char || Math.random() < 0.28) {
                        char = this.randomChar();
                        this.queue[i].char = char;
                    }
                    output += `<span class="text-[var(--ts-magenta)]">${char}</span>`;
                } else {
                    output += from;
                }
            }
            this.el.innerHTML = output;
            if (complete === this.queue.length) {
                this.resolve();
            } else {
                this.frameRequest = requestAnimationFrame(this.update);
                this.frame++;
            }
        }
        
        randomChar() {
            return this.chars[Math.floor(Math.random() * this.chars.length)];
        }
    }

    const scramblers = [];
    document.querySelectorAll('h2.font-display, h3.font-display').forEach(el => {
        const fx = new TextScramble(el);
        const text = el.innerText;
        el.innerText = '';
        
        const scrambleObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    fx.setText(text);
                    scrambleObserver.unobserve(entry.target);
                }
            });
        });
        scrambleObserver.observe(el);
    });

    // 3. Ticker Parallax
    let lastScrollY = window.scrollY;
    let marqueeOffset = 0;
    const marqueeContents = document.querySelectorAll('.marquee-content');
    
    marqueeContents.forEach(el => {
        el.style.animation = 'none';
    });

    function renderMarquee() {
        const currentScrollY = window.scrollY;
        const scrollDelta = currentScrollY - lastScrollY;
        
        marqueeOffset -= 0.5;
        marqueeOffset -= scrollDelta * 0.1;
        
        if (marqueeOffset <= -100) {
            marqueeOffset += 100;
        } else if (marqueeOffset > 0) {
            marqueeOffset -= 100;
        }

        marqueeContents.forEach(el => {
            el.style.transform = `translateX(${marqueeOffset}%)`;
        });
        
        lastScrollY = currentScrollY;
        requestAnimationFrame(renderMarquee);
    }
    
    if (marqueeContents.length > 0) {
        requestAnimationFrame(renderMarquee);
    }

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

        window.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
        });
        
        window.addEventListener('mouseleave', () => {
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
                        ctx.fillStyle = '#a0a0a0';
                        ctx.globalAlpha = 0.4;
                    }

                    ctx.fillText(cell.val, cell.x, cell.y);
                }
            }
            
            requestAnimationFrame(draw);
        }
        
        draw();
    }
});


// Pricing Canvas Animation - Data Pipeline
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('pricing-bg');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        
        function resize() {
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
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
                this.speed = Math.random() * 4 + 2;
                this.length = Math.random() * 80 + 40;
                
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

// Booking Canvas Animation - Radar Sweep / Target Acquisition
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('booking-bg');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let centerX, centerY;
        let angle = 0;
        
        function resize() {
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
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
});

// Projects Canvas Animation - Cascading Terminal Deploy Logs
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('projects-bg');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width, height;

    function resize() {
        // Use the parent section's dimensions for absolute-positioned canvas
        const parent = canvas.parentElement;
        width = canvas.width = parent.offsetWidth || window.innerWidth;
        height = canvas.height = parent.offsetHeight || window.innerHeight;
    }

    window.addEventListener('resize', resize);
    // Delay slightly to ensure DOM is fully laid out
    setTimeout(resize, 100);
    window.addEventListener('load', resize);
    // Also use ResizeObserver on the parent for dynamic height changes
    if (window.ResizeObserver) {
        new ResizeObserver(resize).observe(canvas.parentElement);
    }
    resize();

    const COLORS = {
        green:   '#03aa5c',
        pink:    '#f386a1',
        dark:    '#1e1e1e',
        teal:    '#09aea1',
        magenta: '#d45bb6',
    };

    // Pool of realistic deploy-log style strings
    const LOG_STRINGS = [
        '> icp.build()          OK',
        '> leads.enrich()       OK',
        '> email.verify()       OK',
        '> seq.init()           OK',
        '> ai.personalise()     OK',
        '> smtp.warmup()        OK',
        '> crm.connect()        OK',
        '> reply.handler()      OK',
        '> pipeline.deploy()    OK',
        '> outbound.start()    ███',
        '$ git push origin main',
        '$ npm run build',
        '✓ 2,847 leads loaded',
        '✓ verified: 2,841',
        '✓ pipeline: ACTIVE',
        '✓ status: 200 OK',
        '[ ████████░░ ] 82%',
        '[ ██████████ ] 100%',
        'DEPLOY → live',
        'STATUS → running',
        'UPTIME → 99.9%',
        'ERR  targeting: null',
        'WARN follow_up: slow',
        'OK   meetings: +31',
        'OK   reply_rate: 18%',
        'SYS  build complete.',
        '0x4F 0x4B 0x20 0x01',
        'init: seq[0..12]',
        'exec: enrich.js',
        'exec: copy.ai.js',
    ];

    // A "stream" is one column of falling log lines
    class Stream {
        constructor() {
            this.reset();
        }

        reset() {
            // Pick a random x position, snapped to a grid so columns look structured
            const colWidth = 280;
            const numCols = Math.max(1, Math.ceil(width / colWidth));
            const col = Math.floor(Math.random() * numCols);
            this.x = col * colWidth + Math.random() * 40;

            // Start above the canvas
            this.y = -Math.random() * height;

            // Speed: slow & majestic
            this.speed = Math.random() * 0.6 + 0.3;

            // How many lines in this stream burst
            this.lineCount = Math.floor(Math.random() * 8) + 4;
            this.lineHeight = 22;

            // Generate lines for this stream
            this.lines = [];
            for (let i = 0; i < this.lineCount; i++) {
                const str = LOG_STRINGS[Math.floor(Math.random() * LOG_STRINGS.length)];
                // Color: mostly dark, occasional green/pink accent for key lines
                let color = COLORS.dark;
                if (str.startsWith('✓') || str.includes('OK') || str.includes('ACTIVE')) {
                    color = Math.random() > 0.5 ? COLORS.green : COLORS.teal;
                } else if (str.startsWith('ERR') || str.startsWith('WARN')) {
                    color = COLORS.pink;
                } else if (str.startsWith('DEPLOY') || str.startsWith('SYS')) {
                    color = COLORS.magenta;
                } else if (str.startsWith('0x') || str.startsWith('init') || str.startsWith('exec')) {
                    color = COLORS.dark;
                }
                // Randomise alpha slightly per line for depth
                this.lines.push({ text: str, color, alpha: Math.random() * 0.25 + 0.15 });
            }
            // The leading "hot" line is slightly brighter
            if (this.lines.length > 0) {
                this.lines[0].alpha = 0.55;
                this.lines[0].hot = true;
            }

            this.totalHeight = this.lineCount * this.lineHeight;
        }

        update() {
            this.y += this.speed;
            // Once the entire stream has scrolled past the canvas, reset
            if (this.y > height + this.totalHeight) {
                this.reset();
            }
        }

        draw() {
            ctx.font = '11px "JetBrains Mono", monospace';
            ctx.textBaseline = 'top';
            for (let i = 0; i < this.lines.length; i++) {
                const lineY = this.y - (i * this.lineHeight);
                // Only draw if on screen
                if (lineY < -this.lineHeight || lineY > height + this.lineHeight) continue;

                const line = this.lines[i];
                ctx.globalAlpha = line.alpha;
                ctx.fillStyle = line.color;

                // Leading line gets a subtle highlight cursor
                if (line.hot && i === 0) {
                    ctx.fillStyle = COLORS.green;
                    ctx.globalAlpha = line.alpha * 1.4;
                }

                ctx.fillText(line.text, this.x, lineY);
            }
            ctx.globalAlpha = 1;
        }
    }

    // Spawn enough streams to fill the width
    const streams = [];
    const streamCount = Math.max(6, Math.ceil(width / 240));
    for (let i = 0; i < streamCount; i++) {
        const s = new Stream();
        // Stagger initial positions so they don't all start at once
        s.y = Math.random() * height * 1.5 - height * 0.5;
        streams.push(s);
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);
        streams.forEach(s => {
            s.update();
            s.draw();
        });
        requestAnimationFrame(animate);
    }

    animate();
});
