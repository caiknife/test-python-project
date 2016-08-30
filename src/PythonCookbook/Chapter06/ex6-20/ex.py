#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-21
精确和安全地使用协作的超类调用
@author: CaiKnife
"""
import inspect


class SuperMixin(object):
    def super(cls, *a, **k):
        frame = inspect.currentframe(1)
        self = frame.f_locals['self']
        methodName = frame.f_code.co_name
        method = getattr(super(cls, self), methodName, None)
        if inspect.ismethod(method):
            return method(*a, **k)

    super = classmethod(super)


if __name__ == "__main__":
    class TestBase(list, SuperMixin):
        pass


    class MyTest1(TestBase):
        def myMethod(self):
            print 'in MyTest1'
            MyTest1.super()


    class MyTest2(TestBase):
        def myMethod(self):
            print 'in MyTest2'
            MyTest2.super()


    class MyTest(MyTest1, MyTest2):
        def myMethod(self):
            print 'in MyTest'
            MyTest.super()


    MyTest().myMethod()
