import codecs

def revert_position():
    with codecs.open('d:/boxmation/founder.html', 'r', 'utf-8') as f:
        html = f.read()

    # Change absolute back to fixed
    html = html.replace('class="absolute inset-0 w-full h-full pointer-events-none z-0"', 'class="fixed top-0 left-0 w-full h-full pointer-events-none z-0"')
    
    with codecs.open('d:/boxmation/founder.html', 'w', 'utf-8') as f:
        f.write(html)
        
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()
    
    js = js.replace("ctx.fillStyle = '#000000';", "ctx.fillStyle = '#a0a0a0';")
    js = js.replace("ctx.globalAlpha = 0.5;", "ctx.globalAlpha = 0.4;")
    
    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)
        
    print("Reverted canvas to fixed and text to a0a0a0.")

if __name__ == '__main__':
    revert_position()
