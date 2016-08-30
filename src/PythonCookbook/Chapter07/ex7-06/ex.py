#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
Pickling代码对象
@author: CaiKnife
"""

import new, types, copy_reg


def code_ctor(*args):
    return new.code(*args)


def reduce_code(co):
    if co.co_freevars or co.co_cellvars:
        raise ValueError, 'Sorry, cannot pickle code objects from closures.'
    return code_ctor, (co.co_argcount, co.co_nlocals, co.co_stacksize,
                       co.co_flags, co.co_code, co.co_consts, co.co_names,
                       co.co_varnames, co.co_filename, co.co_name, co.co_firstlineno,
                       co.co_lnotab)


copy_reg.pickle(types.CodeType, reduce_code)

if __name__ == '__main__':
    import cPickle


    def f(x):
        print 'Hello, %s!' % x


    pickled_code = cPickle.dumps(f.func_code)
    recovered_code = cPickle.loads(pickled_code)

    g = new.function(recovered_code, globals())
    g('world')
