#pip install pillow
from PIL import Image
from __future__ import print_function

im = Image.open("image.png")
print(im.format, im.size, im.mode)
im.show()
