import re

bio_html = """      <h1 class="font-display text-5xl md:text-7xl text-on-surface font-bold tracking-tighter mb-4">
        The <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">Founder</span>
      </h1>
      
      <div class="max-w-2xl mx-auto mt-16 text-left space-y-6 font-body-lg text-on-surface-variant text-lg leading-relaxed relative">
        <div class="absolute -inset-12 bg-surface-container-lowest/50 blur-2xl rounded-[3rem] -z-10"></div>
        
        <h2 class="font-headline-md text-3xl text-on-surface font-bold mb-10 text-center">Beyond the Systems</h2>
        
        <p>I build outbound systems for a living, but that's not really who I am — it's just what I'm good at right now.</p>

        <p>I box. Featherweight. There's something clean about it that I don't get anywhere else — no ambiguity, no politics, just you, the work you put in, and whether you did it or not. The gym is the same way for me. It's where the noise stops.</p>
        
        <p>I read constantly — mostly mentalist books and self-help, the kind that try to explain why people do what they do. I think that's the same curiosity that pulled me into building systems in the first place: understanding what makes someone say yes, what makes them trust, what makes them act. One version of that curiosity became my career. The other version just makes me a better conversation at dinner.</p>

        <p>I want to travel properly one day — not tourist-checklist travel, but actually spend real time somewhere. Germany's on that list. Italy too. Sweden and Finland pull at me for a different reason — I don't know exactly why, but something about the quiet, the order, the cold clarity of those countries appeals to me. And Norway — the northern lights specifically — feels like one of those things you have to see with your own eyes at least once before you die.</p>

        <p>There's also a version of my future where I'm doing a master's abroad, somewhere genuinely good, not just chasing a degree but finally getting to enjoy life without constantly grinding against something. I think about that a lot — what it would feel like to build toward something instead of just surviving toward it.</p>

        <p>I've also spent time building things that had nothing to do with revenue — an app for people with hearing disabilities, a period-tracking and guidance app, teaching automation workshops and speaking to students as Director of the AI Society at UCP. Not every build has to make money to matter.</p>

        <p class="font-medium text-on-surface border-l-4 border-primary pl-5 py-2 mt-10">
          So that's the fuller picture — the founder title is real, but so is the boxer, the reader, the guy still figuring out where he wants to end up, and the guy who'd rather build something useful than something impressive.
        </p>
      </div>
"""

with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The target starts with <h1 and ends right before </div> <!-- Scattered Cards Gallery -->
# Wait, currently it's:
# <h1 class="...">The ... Founder</span></h1>
# <p class="...">A glimpse into the life, the work, and the hustle.</p>

m = re.search(r'(<h1 class="font-display.*?</h1>)\s*<p class="font-body-lg.*?</p>', text, re.DOTALL)
if m:
    new_text = text[:m.start()] + bio_html + text[m.end():]
    with open('founder.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Bio injected!")
else:
    print("Not found.")
