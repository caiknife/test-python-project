#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1£1 + 150p + 220p + 15p + 12p + 31p
How many different ways can £2 be made using any number of coins?
"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]


def way_to_change(target, coins=coins):
    if target == 0 or len(coins) == 1:
        return 1
    else:
        largest = coins[-1]
        uses, total = target/largest, 0

        for i in range(uses+1):
            total += way_to_change(target-largest*i, coins[:-1])
        return total

print way_to_change(200, coins)