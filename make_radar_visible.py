import codecs

def fix_radar():
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    js = js.replace('ctx.fillStyle = "rgba(255,0,0,0.5)";\\n            ctx.fillRect(0, 0, width, height);', '')
    js = js.replace("ctx.strokeStyle = 'rgba(30, 30, 30, 0.3)';", "ctx.strokeStyle = 'rgba(30, 30, 30, 1)';")
    js = js.replace("ctx.lineWidth = 1;", "ctx.lineWidth = 4;")
    js = js.replace("ctx.strokeStyle = 'rgba(30, 30, 30, 0.5)';", "ctx.strokeStyle = 'rgba(255, 0, 0, 1)';")
    js = js.replace("ctx.lineWidth = 2;", "ctx.lineWidth = 10;")

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)
    print("Made radar incredibly visible.")

if __name__ == '__main__':
    fix_radar()
