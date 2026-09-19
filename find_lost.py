import json

found = False
with open(r'C:\Users\Ayhan\.gemini\antigravity\brain\a5c45da4-cab7-4e9a-a09a-402915cb3e01\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if 'compare-vs-in-house' in line or 'COMPARE VS IN-HOUSE' in line:
            obj = json.loads(line)
            
            # check tool outputs
            if 'tool_calls' in obj:
                for t in obj['tool_calls']:
                    out = str(t.get('output', ''))
                    if 'compare-vs-in-house' in out:
                        idx = out.find('compare-vs-in-house')
                        print("FOUND IN TOOL OUTPUT:")
                        print(out[max(0, idx-500):idx+2000])
                        found = True
                        break
        if found:
            break
