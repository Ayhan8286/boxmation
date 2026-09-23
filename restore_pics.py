import os
from bs4 import BeautifulSoup
import re

def main():
    # 1. Parse backup html
    with open('d:/boxmation/founder.backup.html', 'r', encoding='utf-8') as f:
        backup_html = f.read()
    backup_soup = BeautifulSoup(backup_html, 'html.parser')
    
    # 2. Parse current html
    with open('d:/boxmation/founder.html', 'r', encoding='utf-8') as f:
        curr_html = f.read()
    curr_soup = BeautifulSoup(curr_html, 'html.parser')

    # Find the 4 gallery containers in backup
    backup_containers = backup_soup.find_all('div', class_=lambda c: c and 'w-[480px]' in c)
    # Find the 4 gallery containers in current
    curr_containers = curr_soup.find_all('div', class_=lambda c: c and 'w-[480px]' in c)

    if len(backup_containers) == len(curr_containers) and len(backup_containers) > 0:
        for backup_div, curr_div in zip(backup_containers, curr_containers):
            # We want to take the children of backup_div, apply brutalist styles, and put them in curr_div
            
            new_children = []
            for child in backup_div.find_all(recursive=False):
                if child.name != 'div':
                    continue
                
                # child is the <div class="w-48 ... relative">
                # inside is the <div class="bg-surface-container-highest p-2 pb-6 rounded-xl border ... shadow-xl">
                polaroid = child.find('div', class_=lambda c: c and 'pb-6' in c)
                if polaroid:
                    # Strip classes like rounded-xl, shadow-xl, border-outline-variant
                    classes = polaroid.get('class', [])
                    classes = [c for c in classes if not c.startswith('rounded') and not c.startswith('shadow') and 'outline' not in c]
                    classes.append('brutalist-border')
                    classes.append('bg-white')
                    polaroid['class'] = classes
                    
                    # Inside polaroid is another div wrapping the img
                    img_wrapper = polaroid.find('div', class_=lambda c: c and 'overflow-hidden' in c)
                    if img_wrapper:
                        w_classes = img_wrapper.get('class', [])
                        w_classes = [c for c in w_classes if not c.startswith('rounded') and 'outline' not in c]
                        w_classes.append('brutalist-border')
                        img_wrapper['class'] = w_classes
                    
                    # The img tag
                    img = polaroid.find('img')
                    if img:
                        img_classes = img.get('class', [])
                        img_classes.append('grayscale')
                        img_classes.append('contrast-125')
                        img['class'] = img_classes
                
                new_children.append(str(child))
            
            # Now set the curr_div's contents
            curr_div.clear()
            # We must use BeautifulSoup to parse the new children and append them
            for child_str in new_children:
                curr_div.append(BeautifulSoup(child_str, 'html.parser'))

        # Write back
        with open('d:/boxmation/founder.html', 'w', encoding='utf-8') as f:
            f.write(str(curr_soup))
        print("Restored images successfully.")
    else:
        print(f"Mismatch: backup {len(backup_containers)}, curr {len(curr_containers)}")

if __name__ == '__main__':
    main()
