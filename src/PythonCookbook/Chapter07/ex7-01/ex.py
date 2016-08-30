#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
使用marshal模块序列化数据
@author: CaiKnife
"""

import marshal

data = {
    12: 'twelve',
    'feep': list('ciao'),
    1.23: 4 + 5j,
    (1, 2, 3): u'wer'
}

bytes = marshal.dumps(data)
print bytes

redata = marshal.loads(bytes)
print redata

print redata == data

outf = file('datafile.txt', 'wb')
marshal.dump(data, outf)
marshal.dump('some string', outf)
marshal.dump(range(19), outf)
outf.close()

inf = file('datafile.txt', 'rb')
try:
    a = marshal.load(inf)
    b = marshal.load(inf)
    c = marshal.load(inf)
    d = marshal.load(inf)
except EOFError, e:
    print e
finally:
    inf.close()
