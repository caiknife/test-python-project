#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-23
计算文档中标签的个数
@author: CaiKnife
'''

from xml.sax.handler import ContentHandler
import xml.sax

class countHandler(ContentHandler):
    def __init__(self):
        self.tags = {}
        
    def startElement(self, name, attr):
        self.tags[name] = self.tags.get(name, 0) + 1
        
parser = xml.sax.make_parser()
handler = countHandler()
parser.setContentHandler(handler)
parser.parse('test.xml')
tags = handler.tags.keys()
tags.sort()
for tag in tags:
    print tag, handler.tags[tag]
