import codecs

def fix_retainer():
    with codecs.open('d:/boxmation/index.html', 'r', 'utf-8') as f:
        html = f.read()

    # Fix the wrong stat block - replace everything wrong
    html = html.replace(
        'System. Not a Service.',
        'Dedicated Partner.'
    )
    html = html.replace(
        'You own the infrastructure. We build it, you keep it. No monthly retainer lock-in.',
        'One team, ongoing. We build, run, and optimise your pipeline month after month as your business scales.'
    )

    with codecs.open('d:/boxmation/index.html', 'w', 'utf-8') as f:
        f.write(html)
    print("Fixed!")

if __name__ == '__main__':
    fix_retainer()
