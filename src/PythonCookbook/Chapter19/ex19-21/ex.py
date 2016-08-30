#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-25
用itertools.groupby来计算汇总报告
@author: CaiKnife
"""

from itertools import groupby
from operator import itemgetter


def summary(data, key=itemgetter(0), field=itemgetter(1)):
    for k, group in groupby(data, key):
        yield k, sum(field(row) for row in group)


if __name__ == '__main__':
    sales = [
        ('Scotland', 'Edinburgh', 20000),
        ('Scotland', 'Glasgow', 12500),
        ('Wales', 'Cardiff', 29700),
        ('Wales', 'Bangor', 12800),
        ('England', 'London', 90000),
        ('England', 'Manchester', 45600),
        ('England', 'Liverpool', 29700)
    ]

    for region, total in summary(sales, field=itemgetter(2)):
        print '%10s: %d' % (region, total)
