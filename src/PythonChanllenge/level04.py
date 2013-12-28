#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/def/linkedlist.html
"""

import urllib2, re

#number = 12345
number = 8022
url_pattern = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d"
pattern = re.compile(r"and the next nothing is (\d+)")

while True:
    f = urllib2.urlopen(url_pattern % number)
    data = f.read()
    f.close()
    match = pattern.findall(data)
    if match:
        number =  int(''.join(match))
        print number
    else:
        print data
        break

print int(number/2)