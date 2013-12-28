#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2011-8-24

@author: ycai
'''
from operator import itemgetter, attrgetter

class Student:
    def __init__(self, name, grade, age):
        self.name, self.grade, self.age = name, grade, age
    
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10)                  
]

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10)                   
]

print sorted(student_tuples, key=lambda student: student[2])
print sorted(student_objects, key=lambda student: student.age)

print sorted(student_tuples, key=itemgetter(2))
print sorted(student_objects, key=attrgetter('age'))
