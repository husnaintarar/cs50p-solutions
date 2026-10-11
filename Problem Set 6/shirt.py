import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file1, ext1 = os.path.splitext(sys.argv[1])
file2, ext2 = os.path.splitext(sys.argv[2])
ext1 = ext1.lower()
ext2 = ext2.lower()

valid_extensions = [".jpg", ".jpeg", ".png"]

if ext1 not in valid_extensions or ext2 not in valid_extensions:
    sys.exit("Invalid input")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")

images = []
try:
    user_image = Image.open(sys.argv[1])
    shirt_image =Image.open("shirt.png")
    shirt_size = shirt_image.size
    resized_user_image = ImageOps.fit(user_image, shirt_size)
    resized_user_image.paste(shirt_image, mask=shirt_image)
    resized_user_image.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")