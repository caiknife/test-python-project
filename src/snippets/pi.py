#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife
"""
from operator import itemgetter

PI = r"3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823"

float_part = PI.split(".")[1]

numbers = dict()
for i in range(100):
    numbers[float_part[i]] = numbers.get(float_part[i], 0) + 1

print sorted(numbers.items(), key=itemgetter(1), reverse=True)