#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-22
在单元测试中检查区间
@author: CaiKnife
'''
import unittest

class IntervalTestCase(unittest.TestCase):
    def failUnlessInside(self, first, second, error, msg=None):
        if not (second-error) < first < (second+error):
            raise self.failureException, (msg or '%r != %r (+-%r)' % (first, second, error))
    
    def failIfInside(self, first, second, error, msg=None):
        if (second-error) < first < (second+error):
            raise self.failureException, (msg or '%r != %r (+-%r)' % (first, second, error))
    
    assertInside = failUnlessInside
    assertNotInside = failIfInside
    
    
if __name__ == '__main__':
    class IntegerArithmenticTestCase(IntervalTestCase):
        def testAdd(self):
            self.assertInside(1+2, 3.3, 0.5)
            self.assertInside(0+1, 1.1, 0.01)
        
        def testMultiply(self):
            self.assertNotInside(0*10, 0.1, 0.05)
            self.assertNotInside(5*8, 40.1, 0.2)
        
    unittest.main()