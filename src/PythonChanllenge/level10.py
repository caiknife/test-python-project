#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/return/bull.html
"""


def look_and_say(member):
    while True:
        yield member
        breakpoints = (
        [0] + [i for i in range(1, len(member)) if member[i - 1] != member[i]] + [len(member)])
        groups = [member[breakpoints[i - 1]:breakpoints[i]] for i in range(1, len(breakpoints))]
        member = ''.join(str(len(group)) + group[0] for group in groups)


sequence = look_and_say("1")
a = [sequence.next() for i in range(1, 32)]
print len(a[30])
