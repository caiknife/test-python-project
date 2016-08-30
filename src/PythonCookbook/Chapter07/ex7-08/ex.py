#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
使用Berkeley DB
@author: CaiKnife
"""

try:
    from bsddb import db
except ImportError:
    from bsddb3 import db
print db.DB_VERSION_STRING

adb = db.DB()
adb.open('db_filename', dbtype=db.DB_HASH, flags=db.DB_CREATE)

for i, w in enumerate('some words for example'.split()):
    adb.put(w, str(i))


def irecords(curs):
    record = curs.first()
    while record:
        yield record
        record = curs.next()


for key, data in irecords(adb.cursor()):
    print 'key=%r, data=%r' % (key, data)

adb.close()
