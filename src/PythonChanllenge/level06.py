#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/def/channel.html
"""

import zipfile, re, os

number = 90052
pattern = re.compile(r"Next nothing is (\d+)")
z = zipfile.ZipFile('channel.zip')
loop = True

while loop:
    textname = "%s.txt" % number
    filename = os.path.join("channel", textname)
    f = file(filename)
    data = f.read()
    f.close()

    match = pattern.search(data)
    if match:
        print z.getinfo(textname).comment,
        number = match.groups()[0]
    else:
        loop = False