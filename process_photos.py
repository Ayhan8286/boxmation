import os
import glob
from PIL import Image
import pillow_heif

# Register HEIF opener
pillow_heif.register_heif_opener()

input_dir = r"C:\Users\Ayhan\Downloads\Photos-1-001"
output_dir = r"d:\boxmation\founder_photos"

os.makedirs(output_dir, exist_ok=True)

files = glob.glob(os.path.join(input_dir, "*"))

for file in files:
    filename = os.path.basename(file)
    name, ext = os.path.splitext(filename)
    
    out_filename = name + ".jpg"
    out_path = os.path.join(output_dir, out_filename)
    
    try:
        img = Image.open(file)
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        # Resize to max 1000px width/height for web
        img.thumbnail((1000, 1000), Image.Resampling.LANCZOS)
        
        img.save(out_path, "JPEG", quality=85)
        print(f"Processed: {filename} -> {out_filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
