#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
捕获和记录异常
@author: CaiKnife
"""

import cStringIO
import traceback


def process_one_file(one_filename):
    pass


def process_all_files(all_filenames,
                      fatal_exceptions=(KeyboardInterrupt, MemoryError)):
    bad_filenames = {}
    for one_filename in all_filenames:
        try:
            process_one_file(one_filename)
        except fatal_exceptions:
            raise
        except Exception:
            f = cStringIO.StringIO()
            traceback.print_exc(file=f)
            bad_filenames[one_filename] = f.getvalue()
    return bad_filenames
