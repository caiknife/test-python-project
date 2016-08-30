#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
自动运行单元测试
@author: CaiKnife
"""

import os
import sys
import microtest


def pretest(modulename, force=False, deleteOnFail=False, runner=microtest.test, verbose=False,
            log=sys.stdout):
    module = __import__(modulename)
    if force or module.__file__.endswith('.py'):
        if runner(modulename, verbose, log):
            pass
        elif deleteOnFail:
            filename = module.__file__
            if filename.endswith('.py'):
                filename = filename + 'c'
            try:
                os.remove(filename)
            except OSError:
                pass
