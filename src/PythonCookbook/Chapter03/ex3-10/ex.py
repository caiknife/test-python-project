#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-4

@author: caiknife
"""
import time
import os
import sys


def main(cmd, inc=60):
    while True:
        os.system(cmd)
        print inc
        time.sleep(inc)


if __name__ == '__main__':
    numargs = len(sys.argv) - 1
    if numargs < 1 or numargs > 2:
        print 'usage: ' + sys.argv[0] + ' command [seconds delay]'
        sys.exit(1)
    cmd = sys.argv[1]
    if numargs < 2:
        main(cmd)
    else:
        inc = int(sys.argv[2])
        main(cmd, inc)
