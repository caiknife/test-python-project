#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-3
count the lines of file, 呵呵
@author: caiknife
"""
import time
import os


def timeo(func, n=10):
    start = time.clock()
    for i in xrange(n):
        func()
    send = time.clock()
    thetime = send - start
    return func.__name__, thetime


def linecount_w():
    return int(os.popen(r'wc -l bbe.txt').read().split()[0])


def linecount_1():
    return len(open(r'bbe.txt').readlines())


def linecount_2():
    count = -1
    for count, line in enumerate(open(r'bbe.txt')):
        pass
    return count + 1


def linecount_3():
    count = 0
    thefile = open(r'bbe.txt', 'rb')
    while True:
        buffer = thefile.read(65536)
        if not buffer:
            break
        count += buffer.count('\n')
    return count


for f in linecount_w, linecount_1, linecount_2, linecount_3:
    print f.__name__, f()

for f in linecount_w, linecount_1, linecount_2, linecount_3:
    print '%s: %.2f' % timeo(f, 100)
