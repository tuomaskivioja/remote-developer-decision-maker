from PIL import Image

# Open an image file
with Image.open("./Developer's Brain.png") as img:
    # Apply an effect (e.g., rotate)
    # img = img.rotate(45)
    img = img.crop((30, 30, 30, 30))
    # Save the modified image
    img.save("./Developer's Brain_2.png")
