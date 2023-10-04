import random
from PIL import Image, ImageDraw

img = Image.open("/code/educative.jpeg")
draw = ImageDraw.Draw(img)

txt = "Best platform"
draw.text((250, 250), txt, fill =(0, 0, 0))
img.save('output/graph.png')
img.show()
