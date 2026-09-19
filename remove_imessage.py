with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<!-- iMessage Review Bubble -->')
end = text.find('</section>', start)

if start != -1 and end != -1:
    # We want to keep the closing tags that come right before </section>
    # In the snippet we saw:
    #     </div>
    # </div>
    # 
    # </div>
    # </div>
    # </section>
    # We will just replace the whole block with the proper closing tags for the transparent-offer grid.
    # The structure was:
    # <div class="lg:col-span-5 flex flex-col justify-center items-center ...">
    #   <div class="flex flex-row flex-wrap gap-x-12 ...">
    #      ... logos ...
    #   [WE ARE HERE]
    #   </div> <!-- ends flex row logos -->
    # </div> <!-- ends col-span-5 -->
    # </div> <!-- ends grid -->
    # </div> <!-- ends max-w container -->
    # </section>

    closing_tags = "\n  </div>\n</div>\n\n</div>\n</div>\n</section>"
    
    new_text = text[:start] + closing_tags + text[end+len('</section>'):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Removed iMessage bubbles!")
else:
    print("Not found")
