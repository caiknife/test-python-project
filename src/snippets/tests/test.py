#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife
"""

import unittest


def __getattr__(self, name):
    if name in ("assertIs", "assertIsNone"):
        statement = "a is b"
    elif name in ("assertIsNot", "assertIsNotNone"):
        statement = "a is not b"
    elif name == "assertIn":
        statement = "a in b"
    elif name == "assertNotIn":
        statement = "a not in b"
    elif name == "assertIsInstance":
        statement = "isinstance(a, b)"
    elif name == "assertIsNotInstance":
        statement = "not isinstance(a, b)"
    else:
        raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))

    def wrapper(a=None, b=None):
        return self.assertTrue(eval(statement))

    return wrapper


unittest.TestCase.__getattr__ = __getattr__


class TestCase(unittest.TestCase):
    def test_func(self):
        self.assertIs(None, None)


if __name__ == '__main__':
    unittest.main()
