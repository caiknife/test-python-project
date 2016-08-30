#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Singleton
"""
from functools import wraps


# 使用__new__方法构造单例类
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# 使用单例装饰器构造单例类
def singleton(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class MyClass(object):
    pass


# 使用getInstance方法构造单例对象，非线程安全
class MySingleton(object):
    @classmethod
    def getInstance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance
