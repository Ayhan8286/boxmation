import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Tailwind config
m = re.search(r'tailwind\.config=(.*?);</script>', text, re.DOTALL)
if m:
    config_str = m.group(1)
    
    # We will do a simple string replacement to inject keyframes and animations inside 'extend: {'
    if 'keyframes:' not in config_str:
        injection = """extend:{keyframes:{float:{'0%, 100%':{transform:'translateY(0)'},'50%':{transform:'translateY(-12px)'}}},animation:{'float-1':'float 6s ease-in-out infinite','float-2':'float 5s ease-in-out infinite 1s','float-3':'float 7s ease-in-out infinite 2s','float-4':'float 5.5s ease-in-out infinite 0.5s','float-5':'float 6.5s ease-in-out infinite 1.5s'},"""
        config_str = config_str.replace('extend:{', injection)
        
        new_text = text[:m.start()] + f"tailwind.config={config_str};</script>" + text[m.end():]
        text = new_text

# 2. Update the logos to use these animations
# Replace hover:-translate-y-1 hover:scale-105 with animate-float-X

text = text.replace(
    '<!-- Logo 1: Exzellent -->\n    <div class="w-32 sm:w-40 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100',
    '<!-- Logo 1: Exzellent -->\n    <div class="w-32 sm:w-40 animate-float-1 transition-opacity duration-500 opacity-70 hover:opacity-100'
)

text = text.replace(
    '<!-- Logo 2: Blackmont -->\n    <div class="w-28 sm:w-36 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100',
    '<!-- Logo 2: Blackmont -->\n    <div class="w-28 sm:w-36 animate-float-2 transition-opacity duration-500 opacity-70 hover:opacity-100'
)

text = text.replace(
    '<!-- Logo 3: Orange Tree -->\n    <div class="w-40 sm:w-48 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100',
    '<!-- Logo 3: Orange Tree -->\n    <div class="w-40 sm:w-48 animate-float-3 transition-opacity duration-500 opacity-70 hover:opacity-100'
)

text = text.replace(
    '<!-- Logo 4: Alhuda -->\n    <div class="w-32 sm:w-40 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-80 hover:opacity-100',
    '<!-- Logo 4: Alhuda -->\n    <div class="w-32 sm:w-40 animate-float-4 transition-opacity duration-500 opacity-80 hover:opacity-100'
)

text = text.replace(
    '<!-- Logo 5: Namrah -->\n    <div class="w-48 sm:w-56 transition-all duration-500 hover:-translate-y-1 hover:scale-105 opacity-70 hover:opacity-100',
    '<!-- Logo 5: Namrah -->\n    <div class="w-48 sm:w-56 animate-float-5 transition-opacity duration-500 opacity-70 hover:opacity-100'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated config and logos.")
