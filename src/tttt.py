#!/usr/bin/python
# coding: UTF-8

"""
Created on 2013-12-22 下午08:18:32

@author: CaiKnife
"""
import urlparse
import urllib

url = 'http://example.com/index.php?a=1&b=2&c=3&a=3'

r = urlparse.urlparse(url)
d = urlparse.parse_qs(r.query)
print d
print d.keys()

d = urlparse.parse_qsl(r.query)
print d
print urllib.urlencode(d)


def func():  # 定义函数 func()
    x = 4  # 函数内部变量 x
    action = (lambda n: x ** n)  # 定义匿名函数 action(n)
    return action  # 返回函数 action 本身，而不是它的值


x = func()  # func() 的返回值赋值给 x
print x(2)  # 调用 action(2)


def outer_func():
    x = 4

    def inner_func(n):
        return x ** n

    return inner_func


x = outer_func()
print x(2)
