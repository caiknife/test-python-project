#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife
"""
import unittest, threading
from snippets.singleton import Singleton, MyClass, MySingleton

class TestSingleton(unittest.TestCase):
    def setUp(self):
        self.singleton_instances = [Singleton() for x in range(100)]
        self.my_class_instances = [MyClass() for x in range(100)]
        self.my_singleton_instances = [MySingleton.getInstance() for x in range(100)]

    def tearDown(self):
        del self.singleton_instances, self.my_class_instances, self.my_singleton_instances

    def test_singleton(self):
        for x in self.singleton_instances:
            self.assertIs(x, Singleton())

    def test_my_class(self):
        for x in self.my_class_instances:
            self.assertIs(x, MyClass())

    def test_my_singleton(self):
        for x in self.my_singleton_instances:
            self.assertIs(x, MySingleton.getInstance())

            
if __name__ == "__main__":
    unittest.main()