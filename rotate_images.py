from PIL import Image

files = [
    r"d:\boxmation\founder_photos\IMGL0882.jpg",
    r"d:\boxmation\founder_photos\IMGL0890.jpg"
]

for file in files:
    try:
        img = Image.open(file)
        # Rotate 90 degrees clockwise (270 degrees counter-clockwise in PIL)
        rotated = img.transpose(Image.ROTATE_270)
        rotated.save(file, "JPEG", quality=90)
        print(f"Rotated {file}")
    except Exception as e:
        print(f"Failed to rotate {file}: {e}")
