#!/usr/bin/python
#coding: UTF-8
'''
Created on 2013-4-28 上午09:37:01

@author: CaiKnife
'''
import time, random

def timing(func):
    def wrapper(*args):
        t1 = time.clock()
        if (len(*args)) < 42: print args
        func(*args)
        if (len(*args)) < 42: print args
        t2 = time.clock()
        print 'The function %s took %0.3f ms and went through %s recursions.' % (func.func_name, (t2-t1)*1000.0, count)
        
    return wrapper

def recursion_count(func):
    def wrapper(*arg):
        global count
        func(*arg)
        count += 1
    return wrapper

@recursion_count
def quicksort(array, start, end):

    if (end <= start):
        return

    q = start
    p = end - 1

    pivot = array[end-1]

    while (p > q):
        while (array[p] >= pivot and p > start):
            p -= 1
        while (array[q] < pivot and q < end-1):
            q += 1
        if (p > q):
            (array[p], array[q]) = (array[q], array[p])

    if (q != end - 1):
        (array[q], array[end-1]) = (array[end-1], array[q])

    quicksort(array, start, q)
    quicksort(array, q+1, end)

@timing
def sort(array):
    quicksort(array, 0, len(array))

if __name__ == "__main__":

    count = 0
    alist = [random.random() for x in range(1,10000)]
    sort(alist)
    