import json

with open(r'C:\Users\Ayhan\.gemini\antigravity\brain\a5c45da4-cab7-4e9a-a09a-402915cb3e01\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in reversed(lines):
    if '<!-- COMPARISON MATRIX: IN-HOUSE VS FREELANCER VS BOXMATION -->' in line:
        obj = json.loads(line)
        if obj.get('source') == 'USER_EXPLICIT':
            content = obj['content']
            start = content.find('<!-- COMPARISON MATRIX: IN-HOUSE VS FREELANCER VS BOXMATION -->')
            end = content.find('<!-- THE WEDGE & STRICT QUALIFIERS -->')
            if start != -1 and end != -1:
                code = content[start:end]
                # Inject the ID
                code = code.replace('<section class="w-full py-24 bg-surface-container-lowest relative">', '<section class="w-full py-24 bg-surface-container-lowest relative" id="compare-vs-in-house">')
                
                with open('extracted.html', 'w', encoding='utf-8') as out:
                    out.write(code)
                print('Extracted perfectly')
                break
