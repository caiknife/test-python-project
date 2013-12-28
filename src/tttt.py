#!/usr/bin/python
#coding: UTF-8
'''
Created on 2013-12-22 下午08:18:32

@author: CaiKnife
'''
import urlparse
import urllib

url = 'http://example.com/index.php?a=1&b=2&c=3'

r = urlparse.urlparse(url)
d = urlparse.parse_qs(r.query)
print d.keys()

d = urlparse.parse_qsl(r.query)
print d
print urllib.urlencode(d)
