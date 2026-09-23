import codecs
import re

def emergency_fix():
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    # Remove the red debug fill
    js = js.replace('ctx.fillStyle = "rgba(255,0,0,0.5)";\n            ctx.fillRect(0, 0, width, height);\n            ', '')
    
    # Restore the red sweep line back to dark
    js = js.replace("ctx.strokeStyle = 'rgba(255, 0, 0, 1)';", "ctx.strokeStyle = 'rgba(30, 30, 30, 0.5)';")
    
    # Restore lineWidth = 10 back to 2
    js = js.replace("ctx.lineWidth = 10;", "ctx.lineWidth = 2;")
    
    # Restore lineWidth = 4 back to 1
    js = js.replace("ctx.lineWidth = 4;", "ctx.lineWidth = 1;")
    
    # Restore thick rings back to subtle
    js = js.replace("ctx.strokeStyle = 'rgba(30, 30, 30, 1)';", "ctx.strokeStyle = 'rgba(30, 30, 30, 0.3)';")

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)
    print("Reverted all debug changes.")

if __name__ == '__main__':
    emergency_fix()
