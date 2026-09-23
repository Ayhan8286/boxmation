import codecs

def update():
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    js = js.replace("canvas.addEventListener('mousemove', (e) => {", "window.addEventListener('mousemove', (e) => {")
    js = js.replace("canvas.addEventListener('mouseleave', () => {", "window.addEventListener('mouseleave', () => {")

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)
    print('Updated mouse events')

if __name__ == '__main__':
    update()
