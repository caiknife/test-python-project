#!/usr/bin/env python
# coding:UTF-8
"""
Created on 2011-12-14

@author: ycai
"""
import types


class HotelRoomCalc(object):
    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoomCalc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        '''Calculate total; default to daily rate'''
        daily = round((self.roomRate * (1 + self.salesTax + self.roomTax)), 2)
        return float(daily) * days


if __name__ == '__main__':
    print HotelRoomCalc.__dict__
    inst = HotelRoomCalc(100)
    print inst.__class__
    if isinstance(inst, HotelRoomCalc):
        print inst.__class__.__name__
