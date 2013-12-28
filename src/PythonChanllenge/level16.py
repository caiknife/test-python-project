#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/return/mozart.html
"""

from PIL import Image
import sys

def straighten(line):
    index = 0
    while line[index] != 195:
        index += 1
    return line[index:] + line[:index]

source = Image.open("mozart.gif")
w, h = source.size[0], source.size[1]

for y in range(h):
    line = [source.getpixel((x, y)) for x in range(w)]
    line = straighten(line)
    [source.putpixel((x, y), line[x]) for x in range(len(line))]

source.save("16.gif")