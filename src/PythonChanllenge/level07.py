#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/def/oxygen.html
"""

from PIL import Image

img = Image.open("oxygen.png")
print "Image info: ", img.format, img.size, img.mode

y_axis = 0
while True:
    p = img.getpixel((0, y_axis))
    if p[0] == p[1] == p[2]:
        print p
        break
    y_axis += 1

x_axis = 0
while True:
    p = img.getpixel((x_axis, y_axis))
    if not p[0] == p[1] == p[2]:
        print p
        break
    x_axis += 1

message = []
for i in range(0, x_axis, 7):
    p = img.getpixel((i, y_axis))
    message.append(chr(p[0]))
print "".join(message)

contents = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join([chr(x) for x in contents])
