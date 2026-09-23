import codecs
import re

def update_grid_and_matrix():
    # 1. Update founder.html
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # Make the grid lines bigger and more prominent
    html = html.replace('rgba(30,30,30,0.06)', 'rgba(30,30,30,0.15)')
    html = html.replace('background-size: 40px 40px;', 'background-size: 80px 80px;')

    # Make the canvas fully opaque so it's as prominent as possible (the colors handle the faintness)
    html = html.replace('style="opacity: 0.5;"', 'style="opacity: 1;"')

    # Also let's make sure the background of the first section doesn't have bg-white
    # It currently is `<section class="w-full border-b border-[#1e1e1e] pt-32 pb-24 bg-grid-pattern relative z-10">`
    # That is perfectly transparent.

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
        
    # 2. Update animations.js to make the matrix text darker and more prominent
    with codecs.open('d:/boxmation/animations.js', 'r', 'utf-8') as f:
        js = f.read()
        
    # Find the fallback fillStyle for the hex matrix
    # Currently: ctx.fillStyle = '#e5e5e5'; ctx.globalAlpha = 0.2;
    js = js.replace("ctx.fillStyle = '#e5e5e5';", "ctx.fillStyle = '#a0a0a0';")
    js = js.replace("ctx.globalAlpha = 0.2;", "ctx.globalAlpha = 0.4;")

    with codecs.open('d:/boxmation/animations.js', 'w', 'utf-8') as f:
        f.write(js)

    print("Updated grid size/prominence and hex matrix prominence.")

if __name__ == '__main__':
    update_grid_and_matrix()
