import codecs

def add_booking_animation():
    with codecs.open('d:/boxmation/booking.html', 'r', 'utf-8') as f:
        html = f.read()

    canvas_html = '\n<canvas id="pricing-bg" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0" style="opacity: 0.8;"></canvas>\n'
    if 'pricing-bg' not in html:
        html = html.replace('<body class="antialiased">', '<body class="antialiased">' + canvas_html)
        with codecs.open('d:/boxmation/booking.html', 'w', 'utf-8') as f:
            f.write(html)
    print('Added animation to booking.html')

if __name__ == '__main__':
    add_booking_animation()
