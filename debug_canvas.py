import codecs
import re

def debug_canvas():
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    booking_block = re.search(r'(// Booking Canvas Animation.*?)(function draw\(\) \{)(.*?)(ctx\.clearRect\(0, 0, width, height\);)', js, flags=re.DOTALL | re.MULTILINE)
    if booking_block:
        new_booking = booking_block.group(0).replace('ctx.clearRect(0, 0, width, height);', 'ctx.clearRect(0, 0, width, height);\n            ctx.fillStyle = "rgba(255,0,0,0.5)";\n            ctx.fillRect(0, 0, width, height);')
        js = js.replace(booking_block.group(0), new_booking)

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)
    print("Added red background to canvas!")

if __name__ == '__main__':
    debug_canvas()
