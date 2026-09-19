import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

header_match = re.search(r'(<html.*?</header>)', text, re.DOTALL)
footer_match = re.search(r'(<footer.*?</html>)', text, re.DOTALL)

if header_match and footer_match:
    header = header_match.group(1)
    footer = footer_match.group(1)
    
    # Founder Body
    body = """
<main class="w-full pt-28 pb-24 bg-background min-h-screen">
  <div class="max-w-[1000px] mx-auto px-6 lg:px-8">
    
    <div class="mb-12">
      <a href="/" class="inline-flex items-center gap-2 text-on-surface-variant hover:text-primary transition-colors font-label-code text-sm uppercase tracking-wider">
        <span class="material-symbols-outlined text-sm">arrow_back</span>
        Back to Home
      </a>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      
      <!-- Image Side -->
      <div class="relative">
        <div class="absolute -inset-4 bg-primary-container/10 blur-3xl rounded-full -z-10"></div>
        <div class="rounded-3xl overflow-hidden border border-outline-variant/30 shadow-2xl relative aspect-[4/5]">
          <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBBFz7641ed1scywEw_kMFNZliJxu72LsO4PCHFEtvlcdT76re5j45JRB5lTgwietH3-ahcXsijnVBnBlRspCDUCVGlBKVk0ckLAjvAgsk6zG7CGonnNbzPDCbduSg7ol-gtr26VsoTm2MDByyypeKzxlMUZsSI8gdoVBcBP-uHrduOya4x_hcoWwQdFOpcMwrxc9GDpprdpBKPhDt1lMRn4Abk5f7ie-wbgMxuohVdtK10MseBi95YuCbhrTTh2e1g" alt="Ayhan" class="w-full h-full object-cover" />
        </div>
        
        <div class="grid grid-cols-2 gap-4 mt-4">
           <div class="rounded-2xl overflow-hidden border border-outline-variant/30 aspect-square">
              <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBmKajU7L5lWyjAikWodJPKDttdkEJXaja6ar9LCGYbwKC2te-l5NsH52e4FSiv00fTJVz8dU9wQS4oGpDbTP-Km-8ytkKtyCC3AQ3kJwOttOBvzRYWR5DqwIjcm6FVYJ9bh8mpfq4CmybQVxGch2tIm0cIUGv47QZsg6wCVUI3MScB2nCjpNMoE4ZQZEzVyitRzUFTT4El6ec45wrLI-WaIYuu6mjLIX-nzt4J--jLaoRoW4Ny-av5I57ppPAWTdCJ" alt="Ayhan working" class="w-full h-full object-cover" />
           </div>
           <div class="rounded-2xl overflow-hidden border border-outline-variant/30 aspect-square">
              <img src="https://lh3.googleusercontent.com/aida/AEtjO1XiGel-EIKQvxtl0cS-36Zc_G6Ne9A0zAyMgSS243Lfclf_1YJpD-3YymM8L8gooi6kjqdtJxb6aCWjr_zFMu0R--74uXeTCfhVGASM3MiAg8J7T4ne66vS94uSAnF2gndfAIv-fFc21waqLFcAuMKlM2wgOnnQd-Cu4QjL4il5dP0HDnrCYgnpMLibjpcMR6IpvKNgnVd7gqWVSwuLDZajM7cO2BoNeDP0BMppA5aY6nPnqeyQdmpVnJFi-BDIcyO9HVUeNGT9" alt="Ayhan profile" class="w-full h-full object-cover" />
           </div>
        </div>
      </div>

      <!-- Text Side -->
      <div class="flex flex-col justify-center">
        <span class="font-label-badge text-label-badge text-primary uppercase tracking-[0.2em] mb-4 block">Behind the Brand</span>
        <h1 class="font-headline-lg text-4xl lg:text-5xl text-on-surface font-bold tracking-tight mb-8">
          Meet Ayhan
        </h1>
        
        <div class="space-y-6 font-body-md text-on-surface-variant text-lg leading-relaxed">
          <p>
            Hi, I'm Ayhan. I built BoxMation out of a deep frustration with seeing brilliant agency founders burn out trying to do everything themselves.
          </p>
          <p>
            When you run a business, your time is your most valuable asset. But too many founders spend their days stressed out about where their next client is coming from, manually sending messages, or trying to manage unreliable freelancers. It pulls them away from what they actually love doing: delivering amazing work and building genuine relationships.
          </p>
          <p>
            I'm a massive believer in working smarter, not harder. I love taking complex, chaotic problems and organizing them into smooth, predictable systems. That's why I focus so heavily on transparency, direct communication, and zero-fluff execution. 
          </p>
          <p>
            Outside of building BoxMation, I'm passionate about continuous learning, design, and finding ways to simplify the noise of the modern digital world. I value honesty above all else—which is exactly how I run my partnerships. If we work together, you get direct access to me, no middle-men, and complete transparency.
          </p>
          <p class="font-medium text-on-surface italic mt-4">
            "My goal isn't just to fill your calendar. It's to give you your time back."
          </p>
        </div>
        
        <div class="mt-10">
          <a href="/#book-discovery" class="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl bg-primary-container text-on-primary-container font-body-md font-semibold hover:bg-secondary-container transition-all shadow-[0_0_20px_rgba(5,150,105,0.3)]">
            Let's chat
          </a>
        </div>

      </div>
    </div>

  </div>
</main>
"""
    
    # Ensure correct title in founder.html header
    header = header.replace("<title>BoxMation</title>", "<title>About Ayhan - BoxMation</title>")
    
    full_html = header + body + footer
    with open('founder.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("founder.html created successfully.")
else:
    print("Could not extract header/footer")
