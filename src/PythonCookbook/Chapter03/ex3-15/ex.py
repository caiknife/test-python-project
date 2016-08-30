#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-17
检查信用卡校验和
@author: CaiKnife
"""


def cardLuhnChecksumIsValid(card_number):
    """通过Luhn mod-10校验和算法检查信用卡号"""
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(num_digits):
        digit = int(card_number[count])
        if not ((count & 1) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum += digit
    return (sum % 10) == 0
