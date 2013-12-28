#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/return/uzi.html
"""

import calendar

print [year for year in range(1006, 2006, 10) if calendar.weekday(year, 1, 26)==calendar.MONDAY and calendar.isleap(year)]
