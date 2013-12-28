#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-22
调试垃圾回收进程
@author: CaiKnife
'''

import gc

def dump_garbage():
    print '\nGARBAGE:'
    gc.collect()
    print '\nGARBAGE OBJECTS:'
    for x in gc.garbage:
        s = str(x)
        if len(s) > 80:
            s = s[:77] + '...'
        print type(x), '\n ', s
        
if __name__ == '__main__':
    gc.enable()
    gc.set_debug(gc.DEBUG_LEAK)
    l = []
    l.append(l)
    del l
    dump_garbage()