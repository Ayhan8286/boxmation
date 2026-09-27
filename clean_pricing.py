with open('pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where the orphaned content starts (after the comment "Signal Engine + Full-Stack Engine Row")
# and where the real logos section starts
start_idx = None
end_idx = None

for i, line in enumerate(lines):
    # The orphaned content starts just after line 485 "<!-- /Signal Engine..."
    if start_idx is None and '<!-- /Signal Engine + Full-Stack Engine Row -->' in line:
        start_idx = i + 1  # start removing from the next line
    # The logos section starts with the mt-24 div
    if start_idx is not None and end_idx is None and 'mt-24 w-full flex' in line:
        end_idx = i
        break

if start_idx is not None and end_idx is not None:
    print(f"Removing lines {start_idx+1} to {end_idx} ({end_idx - start_idx} lines of orphaned content)")
    lines = lines[:start_idx] + lines[end_idx:]
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Done! File saved.")
else:
    print(f"start_idx={start_idx}, end_idx={end_idx}")
    for i, line in enumerate(lines[483:500], start=484):
        print(f"{i}: {line.rstrip()}")
