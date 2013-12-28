#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-21
实现状态设计模式
@author: CaiKnife
'''

class TraceNormal(object):
    '正常的状态'
    def startMessage(self):
        self.nstr = self.characters = 0
        
    def emitString(self, s):
        self.nstr += 1
        self.characters += len(s)
        
    def endMessage(self):
        print '%d characters in %d strings' % (self.characters, self.nstr)
        
class TraceChatty(object):
    '详细的状态'
    def startMessage(self):
        self.msg = []
        
    def emitString(self, s):
        self.msg.append(repr(s))
        
    def endMessage(self):
        print 'Message: ', ', '.join(self.msg)
        
class TraceQuiet(object):
    '无输出的状态'
    def startMessage(self):
        pass
    
    def emitString(self, s):
        pass
    
    def endMessage(self):
        pass
    
class Trace(object):
    def __init__(self, state):
        self.state = state
        
    def setState(self, state):
        self.state = state
        
    def emitStrings(self, strings):
        self.state.startMessage()
        for s in strings:
            self.state.emitString(s)
        self.state.endMessage()
        
if __name__ == '__main__':
    t = Trace(TraceNormal())
    t.emitStrings('some example strings here'.split())
    
    t.setState(TraceQuiet())
    t.emitStrings('some example strings here'.split())
    
    t.setState(TraceChatty())
    t.emitStrings('some example strings here'.split())
    