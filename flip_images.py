from PIL import Image

files = [
    r"d:\boxmation\founder_photos\IMGL0882.jpg",
    r"d:\boxmation\founder_photos\IMGL0890.jpg"
]

for file in files:
    try:
        img = Image.open(file)
        # Rotate 180 degrees to fix upside down
        rotated = img.transpose(Image.ROTATE_180)
        rotated.save(file, "JPEG", quality=90)
        print(f"Flipped {file} upside down (rotated 180)")
    except Exception as e:
        print(f"Failed to flip {file}: {e}")
