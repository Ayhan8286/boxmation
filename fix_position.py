import codecs

def fix_position():
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    # Change fixed to absolute inset-0
    html = html.replace('class="fixed top-0 left-0 w-full h-full pointer-events-none z-0"', 'class="absolute inset-0 w-full h-full pointer-events-none z-0"')
    
    # Also I will make the base text color SOLID black #000000 so it has MAXIMUM visibility on white!
    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(html)
        
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()
    
    js = js.replace("ctx.fillStyle = '#a0a0a0';", "ctx.fillStyle = '#000000';")
    js = js.replace("ctx.globalAlpha = 0.4;", "ctx.globalAlpha = 0.5;")
    
    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)

if __name__ == '__main__':
    fix_position()
