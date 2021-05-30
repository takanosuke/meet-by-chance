from PIL import Image
import numpy as np
import random

width = 900
height = 600
img = Image.new('RGBA', (width, height))
r = g = b = 0
for y in range(height):
  for x in range(width):
    if random.random() > 0.9:
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
    img.putpixel((x,y), (r, g, b))

img.show()
img.save('result.png')
