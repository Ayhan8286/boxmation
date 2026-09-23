import re
import codecs

def expand_founder_text():
    filepath = 'd:/boxmation/founder.html'
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # We will replace specific paragraphs with expanded versions
    p1 = "I build outbound systems for a living, but that's not really who I am — it's just what I'm good at right now."
    p1_expanded = """I build outbound systems for a living, but that's not really who I am — it's just what I'm good at right now. The engineering, the automation, the scaling — it's all just a mechanical expression of a deeper drive to understand how things connect and how people operate. I treat cold email and GTM infrastructure as a puzzle. When you piece it together perfectly, it works flawlessly. But my true self exists beyond the servers and the sales calls."""

    p2 = "I box. Featherweight. There's something clean about it that I don't get anywhere else — no ambiguity, no politics, just you, the work you put in, and whether you did it or not. The gym is the same way for me. It's where the noise stops."
    p2_expanded = """I box. Featherweight. There's something clean about it that I don't get anywhere else — no ambiguity, no politics, just you, the work you put in, and whether you did it or not. The gym is the same way for me. It's where the noise stops. In a world where everything is subjective and everyone is selling a narrative, the heavy bag doesn't lie. You either have the stamina or you don't. That raw, undeniable feedback loop is something I try to bring into my business as well."""

    p3 = "I read constantly — mostly mentalist books and self-help, the kind that try to explain why people do what they do. I think that's the same curiosity that pulled me into building systems in the first place: understanding what makes someone say yes, what makes them trust, what makes them act. One version of that curiosity became my career. The other version just makes me a better conversation at dinner."
    p3_expanded = """I read constantly — mostly mentalist books and self-help, the kind that try to explain why people do what they do. I think that's the same curiosity that pulled me into building systems in the first place: understanding what makes someone say yes, what makes them trust, what makes them act. One version of that curiosity became my career, turning human psychology into engineered outreach pipelines. The other version just makes me a better conversationalist at dinner, and keeps my mind sharp when I'm trying to decode complex human behavior."""

    p4 = "I want to travel properly one day — not tourist-checklist travel, but actually spend real time somewhere. Germany's on that list. Italy too. Sweden and Finland pull at me for a different reason — I don't know exactly why, but something about the quiet, the order, the cold clarity of those countries appeals to me. And Norway — the northern lights specifically — feels like one of those things you have to see with your own eyes at least once before you die."
    p4_expanded = """I want to travel properly one day — not tourist-checklist travel, but actually spend real time somewhere. Germany's on that list. Italy too. Sweden and Finland pull at me for a different reason — I don't know exactly why, but something about the quiet, the order, the cold clarity of those countries appeals to me. I crave environments that offer stark contrast to the loud, fast-paced startup world. And Norway — the northern lights specifically — feels like one of those phenomenons you have to see with your own eyes at least once before you die. I want to experience cultures that prioritize deep work and genuine human connection."""

    p5 = "There's also a version of my future where I'm doing a master's abroad, somewhere genuinely good, not just chasing a degree but finally getting to enjoy life without constantly grinding against something. I think about that a lot — what it would feel like to build toward something instead of just surviving toward it."
    p5_expanded = """There's also a version of my future where I'm doing a master's abroad, somewhere genuinely good. I don't just want to chase a piece of paper; I want to finally get to enjoy life without constantly grinding against something. I think about that a lot — what it would feel like to build toward a quiet, focused goal instead of just surviving the daily entrepreneurial hustle. Moving abroad, experiencing a completely different academic and social rhythm, is a goal that keeps me grounded when the day-to-day operations get heavy."""

    p6 = "I've also spent time building things that had nothing to do with revenue — an app for people with hearing disabilities, a period-tracking and guidance app, teaching automation workshops and speaking to students as Director of the AI Society at UCP. Not every build has to make money to matter."
    p6_expanded = """I've also spent a considerable amount of time building things that had nothing to do with revenue — an app for people with hearing disabilities to navigate the world easier, a period-tracking and guidance app, teaching automation workshops, and speaking to students as the Director of the AI Society at UCP. Those projects remind me that technology is a lever. Not every build has to make money to matter. The true value of knowing how to build systems is the freedom it gives you to solve problems that actually mean something to you."""

    # Note: Replace exact matches but we need to handle potential whitespace/newlines or unicode chars like  for dash.
    # We will use regex for robust matching.

    replacements = [
        (r"I build outbound systems for a living, but that's not really who I am [—\-] it's just what I'm good at right now\.", p1_expanded),
        (r"I box\. Featherweight\. There's something clean about it.*?It's where the noise stops\.", p2_expanded),
        (r"I read constantly [—\-] mostly mentalist books.*?better conversation at dinner\.", p3_expanded),
        (r"I want to travel properly one day.*?before you die\.", p4_expanded),
        (r"There's also a version of my future where I'm doing a master's abroad.*?surviving toward it\.", p5_expanded),
        (r"I've also spent time building things that had nothing to do with revenue.*?make money to matter\.", p6_expanded)
    ]

    for pattern, expanded in replacements:
        html = re.sub(pattern, expanded, html, flags=re.DOTALL)
        
    # Let's also make sure the paragraphs have enough bottom margin. They currently have `mb-8`. Let's change them to `mb-12` or `mb-16` to push the layout further down.
    html = html.replace('<p class="mb-8 reveal">', '<p class="mb-12 reveal text-justify">')
    # Text justify usually looks good in brutalist if combined with mono, but here it's sans-serif. It helps fill space evenly.
    
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    expand_founder_text()
