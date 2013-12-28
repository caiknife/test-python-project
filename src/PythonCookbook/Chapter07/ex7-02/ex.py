#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-22
使用pickle和cPickle模块序列化数据
@author: CaiKnife
'''

data = {
    12: 'twelve',
    'feep': list('ciao'),
    1.23: 4+5j,
    (1, 2, 3): u'wer'
}

import cPickle

text = cPickle.dumps(data)
print text
bytes = cPickle.dumps(data, 2)
print bytes

redata1 = cPickle.loads(text)
redata2 = cPickle.loads(bytes)
print redata1 == redata2

outf = file('datafile.txt', 'wb')
cPickle.dump(data, outf)
cPickle.dump('some string', outf)
cPickle.dump(range(19), outf)
outf.close()

inf = file('datafile.txt', 'rb')
try:
    a = cPickle.load(inf)
    b = cPickle.load(inf)
    c = cPickle.load(inf)
    d = cPickle.load(inf)
except EOFError, e:
    print e
finally:
    inf.close()