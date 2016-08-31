#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/return/5808.html
"""

from PIL import Image

src = Image.open("cave.jpg")
print "Image info:", src.format, src.size, src.mode
w, h = src.size[0], src.size[1]
new = Image.new(src.mode, (w // 2, h))

for i in range(w * h):
    y, x = divmod(i, w)
    p = src.getpixel((x, y))
    if i % 2:  # even==info, odd==photo
        new.putpixel((x / 2, y / 2 + h // 2), p)
    else:
        new.putpixel((x / 2, y / 2), p)

new.save("11.jpg")
