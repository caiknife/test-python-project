#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/return/italy.html
"""

from PIL import Image

source = Image.open("wire.png")
new = Image.new(source.mode, (100, 100))

doubled_steps = 200
directions = [(1,0), (0,1), (-1,0), (0,-1)] # vectors in [x,y] format
x, y, p = -1, 0, 0
while doubled_steps//2 > 0:
    for v in directions: # we will be taking steps in 4 directions
        steps = doubled_steps//2
        for s in range(steps):
            x, y = x+v[0], y+v[1]
            new.putpixel((x,y), source.getpixel((p,0)))
            p += 1
        doubled_steps -= 1
new.save('14.jpg')