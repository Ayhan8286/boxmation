with open('pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the orphaned dark card remnant: starts with the old Left panel comment after the new card ends
# New card ends at the closing </div> before "<!-- Bottom row"
# The orphan starts with "        <!-- Left: Title + Price + Specs -->" right after the new card's </div>

start_idx = None
end_idx = None

for i, line in enumerate(lines):
    # Second occurrence of this comment is the orphan
    if '<!-- Left: Title + Price + Specs -->' in line:
        if start_idx is None:
            pass  # first occurrence is the new card — skip
        else:
            start_idx = i - 1  # grab from the line before (which is blank or the old opening div)
            break
    if '<!-- Bottom row: 3 equal cards -->' in line:
        end_idx = i
        break

# Re-scan properly
start_idx = None
end_idx = None
count = 0

for i, line in enumerate(lines):
    if '<!-- Left: Title + Price + Specs -->' in line:
        count += 1
        if count == 2:
            # Go back to find the opening div of the old card
            start_idx = i - 1
    if start_idx is not None and '<!-- Bottom row: 3 equal cards -->' in line:
        end_idx = i
        break

if start_idx is not None and end_idx is not None:
    print(f"Removing lines {start_idx+1} to {end_idx} ({end_idx - start_idx} orphaned lines)")
    lines = lines[:start_idx] + lines[end_idx:]
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Done!")
else:
    print(f"start={start_idx}, end={end_idx}")
    for i, line in enumerate(lines[280:310], start=281):
        print(f"{i}: {line.rstrip()}")
