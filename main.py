from PIL import Image

d0 = Image.open("default-0.png")
d1 = Image.open("default-1.png")
d2 = Image.open("default-2.png")
d3 = Image.open("default-3.png")
d4 = Image.open("default-4.png")
d5 = Image.open("default-5.png")
d6 = Image.open("default-6.png")
d7 = Image.open("default-7.png")
d8 = Image.open("default-8.png")
d9 = Image.open("default-9.png")

hs = Image.open("hitcircle.png")
hso = Image.open("hitcircleoverlay.png")

dimensions = d0.size
hs.paste(d0, dimensions)
hs.show(0)