#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-4

@author: caiknife
"""

import time


def is_dst():
    return bool(time.localtime().tm_isdst)


if __name__ == '__main__':
    print is_dst()
