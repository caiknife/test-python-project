#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Pentagon numbers
Problem 44
Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70  22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk  Pj| is minimised; what is the value of D?
"""

from itertools import combinations
from operator import itemgetter, add, sub
from euler import pentagon_number

pentagons = set(pentagon_number(n) for n in range(1, 3000))
c = combinations(pentagons, 2)
for p in c:
    if add(*p) in pentagons and abs(sub(*p)) in pentagons:
        print abs(sub(*p))
