#!/usr/bin/python
#coding:utf8

import os

def main():
    PATH = 'D:\\test'
    
    for path, dirs, files in os.walk(PATH):
        for f in files:
            if f.endswith('.py'):
                processFile(os.path.join(path, f))
                

def processFile(path):
    print 'writing encoing header to %s' % path
    try:
        #read content first
        fp = open(path, 'r')
        fc = fp.readlines()
        fp.close()
        
        if len(fc) <= 1:
            return
        
        #then write it back
        fp = open(path, 'w')
        #pop first line
        firstLine = fc.pop(0)
        
        ENCODING = '#coding:utf8\n'
        
        if firstLine == ENCODING:
            return
        
        if firstLine == '#!/usr/bin/env python\n':
            secondLine = fc.pop(0)
            if secondLine == ENCODING:
                head = [firstLine, ENCODING]
            else:
                head = [firstLine, ENCODING, secondLine]
        else:
            head = [ENCODING, firstLine]
        fc = head + fc
        fp.write(''.join(fc))
        fp.close()
    except Exception, e:
        print e
        

if __name__ == '__main__':
    main()
    #processFile(os.path.join(os.getcwdu(), 'index_bak.py'))