#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-23
获得XML文档中的文本
@author: CaiKnife
'''

from xml.sax.handler import ContentHandler
import xml.sax
import sys

class textHandler(ContentHandler):
    def characters(self, ch):
        sys.stdout.write(ch.encode('Latin-1'))
        
parser = xml.sax.make_parser()
handler = textHandler()
parser.setContentHandler(handler)
parser.parse('test.xml')
