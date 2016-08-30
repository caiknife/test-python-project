#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
当未捕获异常发生时自动启用调试器
@author: CaiKnife
"""

import sys


def info(type, value, tb):
    if hasattr(sys, 'ps1') or not (sys.stderr.isatty() and sys.stdin.isatty()) or issubclass(type,
                                                                                             SyntaxError):
        sys.__excepthook__(type, value, tb)
    else:
        import traceback, pdb
        traceback.print_exception(type, value, tb)
        print
        pdb.pm()


sys.excepthook = info
