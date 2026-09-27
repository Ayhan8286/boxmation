import glob

threads_link = '<a class="hover:text-black transition-colors" href="https://www.threads.com/@ayhansiillusion" target="_blank" title="Threads"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 192 192"><path d="M141.537 88.988a66.667 66.667 0 0 0-2.518-1.143c-1.482-27.307-16.403-42.94-41.457-43.1h-.34c-14.986 0-27.449 6.396-35.12 18.036l13.779 9.452c5.73-8.695 14.724-10.548 21.348-10.548h.229c8.249.053 14.474 2.452 18.503 7.129 2.932 3.405 4.893 8.107 5.864 14.05-7.314-1.243-15.224-1.626-23.68-1.14-23.82 1.371-39.134 15.264-38.105 34.568.522 9.792 5.4 18.216 13.735 23.719 7.047 4.652 16.124 6.927 25.557 6.412 12.458-.683 22.231-5.436 29.049-14.127 5.178-6.6 8.453-15.153 9.899-25.93 5.937 3.583 10.337 8.298 12.767 13.966 4.132 9.635 4.373 25.468-8.546 38.376-11.319 11.308-24.925 16.2-45.488 16.35-22.72-.169-39.898-7.451-51.063-21.639C37.786 134.671 32.025 116.527 31.808 96c.217-20.527 5.978-38.671 16.685-52.524C59.658 29.288 76.836 22.006 99.556 21.837c22.886.17 40.393 7.484 52.023 21.737 5.675 6.975 9.944 15.717 12.7 25.602l16.231-4.333c-3.359-12.51-8.744-23.312-16.11-32.182C147.147 14.406 125.587 4.91 99.64 4.7h-.084c-25.882.21-47.214 9.736-63.397 28.313C22.3 49.522 15.554 70.881 15.3 96c.254 25.119 7 46.478 20.859 63.487 16.183 18.576 37.515 28.102 63.397 28.313h.084c23.124-.187 39.365-6.206 52.726-19.555 17.97-17.956 17.42-40.414 11.501-54.225-4.252-9.92-12.437-17.958-22.33-22.032Zm-38.66 42.707c-10.418.583-21.256-4.087-21.82-14.041-.424-7.972 5.674-16.86 24.09-17.9 2.107-.122 4.175-.181 6.207-.181 6.127 0 11.868.558 17.16 1.638-1.954 24.375-15.204-25.637 30.484Z"/></svg></a>'

files = glob.glob('*.html')
files = [f for f in files if not f.endswith('.bak')]

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if 'threads.com' in c:
        print(f"[{fn}] Threads ALREADY present.")
        continue
        
    print(f"[{fn}] Threads missing. Searching for WhatsApp anchor...")
    
    # Use split to find the exact boundary of the WhatsApp anchor tag
    parts = c.split('title="WhatsApp">')
    if len(parts) < 2:
        print(f"  -> Could not find WhatsApp title attribute.")
        continue
        
    # The second part starts with <svg... then </a>
    subparts = parts[1].split('</a>', 1)
    if len(subparts) < 2:
        print(f"  -> Could not find closing </a> for WhatsApp.")
        continue
        
    # Reconstruct the string with Threads link inserted
    new_c = parts[0] + 'title="WhatsApp">' + subparts[0] + '</a>\n' + threads_link + subparts[1]
    
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(new_c)
        
    print(f"[{fn}] Successfully injected Threads link.")

