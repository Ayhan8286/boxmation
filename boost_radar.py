import codecs

def boost_radar():
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()

    js = js.replace("ctx.strokeStyle = 'rgba(30, 30, 30, 0.05)';", "ctx.strokeStyle = 'rgba(30, 30, 30, 0.2)';")
    js = js.replace("ctx.strokeStyle = 'rgba(30, 30, 30, 0.2)';", "ctx.strokeStyle = 'rgba(30, 30, 30, 0.5)';")
    js = js.replace("grad.addColorStop(1, 'rgba(30, 30, 30, 0.03)');", "grad.addColorStop(1, 'rgba(30, 30, 30, 0.1)');")

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)
        
    print("Boosted radar contrast.")

if __name__ == '__main__':
    boost_radar()
