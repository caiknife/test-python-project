#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
在Linux上测量内存使用
@author: CaiKnife
"""

import os

_proc_status = '/proc/%d/status' % os.getpid()
_scale = {
    'kB': 1024.0,
    'mB': 1024.0 * 1024.0,
    'KB': 1024.0,
    'MB': 1024.0 * 1024.0
}


def _VmB(VmKey):
    try:
        t = open(_proc_status)
        v = t.read()
        t.close()
    except IOError:
        return 0.0
    i = v.index(VmKey)
    v = v[i:].split(None, 3)
    if len(v) < 3:
        return 0.0
    return float(v[1]) * _scale[v[2]]


def memory(since=0.0):
    return _VmB('VmSize:') - since


def resident(since=0.0):
    return _VmB('VmRSS:') - since


def stacksize(since=0.0):
    return _VmB('VmStk:') - since
