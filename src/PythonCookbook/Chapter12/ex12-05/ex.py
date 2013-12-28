#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-23
将一个XML文档转化成Python对象树
@author: CaiKnife
'''

from xml.parsers import expat
from fileinput import filename

class Element(object):
    '''一个解析出来的元素'''
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.cdata = ''
        self.children = []
        
    def addChild(self, element):
        self.children.append(element)
    
    def getAttribute(self, key):
        return self.attributes.get(key)

    def getData(self):
        return self.cdata
    
    def getElements(self, name=''):
        if name:
            return [c for c in self.children if c.name==name]
        else:
            return list(self.children)
        
    def __str__(self):
        return '%s ( %s )' % (self.name, self.children)
    
    __repr__ = __str__
        
class Xml2Obj(object):
    '''XML到对象的转换器'''
    def __init__(self):
        self.root = None
        self.nodeStack = []
        
    def startElement(self, name, attributes):
        element = Element(name.encode(), attributes)
        if self.nodeStack:
            parent = self.nodeStack[-1]
            parent.addChild(element)
        else:
            self.root = element
        self.nodeStack.append(element)
        
    def endElement(self, name):
        self.nodeStack.pop()
        
    def characterData(self, data):
        if data.strip():
            data = data.encode()
            element = self.nodeStack[-1]
            element.cdata += data
    
    def parse(self, filename):
        parser = expat.ParserCreate()
        parser.StartElementHandler = self.startElement
        parser.EndElementHandler = self.endElement
        parser.CharacterDataHandler = self.characterData
        
        parserStatus = parser.Parse(open(filename).read(), 1)
        return self.root
    
parser = Xml2Obj()
root_element = parser.parse('test.xml')

print root_element