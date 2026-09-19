import os

photo_dir = r"d:\boxmation\founder_photos"
photos = [f for f in os.listdir(photo_dir) if f.endswith('.jpg')]

# Sort them alphabetically or just use them as is
photos.sort()

gallery_html = """
    <section class="mt-24 pt-16 border-t border-outline-variant/10">
      <div class="text-center mb-12">
        <h2 class="font-headline-md text-3xl text-on-surface font-bold tracking-tight mb-3">
          Behind the Scenes
        </h2>
        <p class="font-body-md text-on-surface-variant">
          A glimpse into the life, the work, and the hustle.
        </p>
      </div>
      
      <div class="columns-2 md:columns-3 lg:columns-4 gap-4 space-y-4">
"""

for photo in photos:
    gallery_html += f"""
        <div class="break-inside-avoid rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform duration-500 cursor-pointer border border-outline-variant/10 shadow-md bg-surface-container-low">
          <img src="founder_photos/{photo}" alt="Behind the scenes" class="w-full h-auto object-cover opacity-90 hover:opacity-100 transition-opacity" loading="lazy" />
        </div>
"""

gallery_html += """
      </div>
    </section>
"""

with open('founder.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We want to insert this right before the closing </main> or closing </div> inside main.
# Let's find </main>
target = "  </div>\n</main>"
if target in text:
    new_text = text.replace(target, gallery_html + "\n" + target)
    with open('founder.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Gallery injected!")
else:
    print("Target not found. Will try another replacement.")
    target2 = "</main>"
    if target2 in text:
        new_text = text.replace(target2, gallery_html + "\n" + target2)
        with open('founder.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Gallery injected before </main>!")
