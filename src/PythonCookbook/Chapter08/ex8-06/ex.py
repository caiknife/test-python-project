#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-22
从traceback中获得更多信息
@author: CaiKnife
'''

import sys, traceback

def print_exc_plus():
    tb = sys.exc_info()[2]
    while tb.tb_text:
        tb = tb.tb_text
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    traceback.print_exc()
    print 'Locals by frame, innermost last'
    for frame in stack:
        print
        print "Frame %s in %s at line %s" % (frame.f_code.co_name, 
                                             frame.f_code.co_filename,
                                             frame.f_lineno)
        for key, value in frame.f_locals.items():
            print '\t%20s' % key
            try:
                print value
            except:
                print '<ERROR WHILE PRINTING VALUE>'