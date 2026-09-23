import codecs

def fix_copy():
    filepath = 'd:/boxmation/index.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # Fix the wrong "1" stat
    html = html.replace(
        '<div class="font-display text-6xl font-black text-[var(--ts-green)] mb-3">1</div>\n                <div class="font-mono text-xs uppercase tracking-[0.2em] text-gray-400 mb-2">System. Not a Service.</div>\n                <p class="text-gray-500 text-sm">You own the infrastructure. We build it, you keep it. No monthly retainer lock-in.</p>',
        '<div class="font-display text-6xl font-black text-[var(--ts-green)] mb-3">1</div>\n                <div class="font-mono text-xs uppercase tracking-[0.2em] text-gray-400 mb-2">Dedicated Partner</div>\n                <p class="text-gray-500 text-sm">One team running your pipeline. Ongoing — we optimise, iterate, and scale with you every month.</p>'
    )

    # Fix the step 03 copy that implied one-time
    html = html.replace(
        'Qualified meetings in your calendar. Not traffic. Not leads. Conversations with buyers who already know your offer before they pick up the phone.',
        'Qualified meetings in your calendar, month after month. Not traffic. Not leads. Conversations with buyers who already know your offer before they pick up the phone.'
    )

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
    print("Fixed copy to reflect retainer model.")

if __name__ == '__main__':
    fix_copy()
