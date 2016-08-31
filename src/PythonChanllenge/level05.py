#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/def/peak.html
"""

import pickle
import cPickle
import urllib2

url = "http://www.pythonchallenge.com/pc/def/banner.p"

f = urllib2.urlopen(url)
data = f.read()
f.close()

obj = cPickle.loads(data)
for ele in obj:
    print "".join([x[0] * x[1] for x in ele])
