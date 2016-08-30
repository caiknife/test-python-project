#!/usr/bin/python
# coding: UTF-8

"""
@author: CaiKnife
"""
from itertools import groupby
from operator import methodcaller
from collections import defaultdict
import time, os


def main():
    s = "Hello, world! Hello, MOTO! Hello, world! Hello, MOTO! Hello, world! Hello, MOTO! "
    print groupby(s, key=methodcaller("isalnum"))

    for k, g in groupby(s, key=methodcaller("isalnum")):
        if k:
            word = ''.join(g)
            print k, g, word


if __name__ == '__main__':
    start_time = time.time()
    with open('bible/bbe.txt') as f:
        for line in f:
            # print line
            pass
        f.close()
    end_time = time.time()
    print end_time - start_time

    f = open('bible/bbe.txt')
    for line in f:
        pass
    f.close()
    print time.time() - end_time

    foldername, filename = os.path.split(__file__)
    print foldername
    print filename
    print os.path.abspath(filename)
    print os.path.basename(__file__)
