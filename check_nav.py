files = ['pricing.html', 'booking.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    
    print("=== " + fn + " ===")
    
    # Find the desktop nav
    start = c.find('hidden xl:flex items-center gap-7')
    if start == -1:
        print("  Desktop nav NOT FOUND")
    else:
        end = c.find('</nav>', start) + 6
        print("  Desktop nav:")
        print(c[start:end])
    
    # Check if projects.html is anywhere in the file
    if 'projects.html' in c:
        print("  projects.html IS in the file")
    else:
        print("  projects.html NOT IN FILE")
    print()
