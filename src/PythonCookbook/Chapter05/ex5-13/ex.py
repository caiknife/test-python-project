#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-18
寻找子序列
@author: CaiKnife
"""


def KnuthMorrisPratt(text, pattern):
    """ 在序列text中寻找pattern的子序列的起始位置
                    每个参数都可以是任何可迭代对象
                    在每次产生一个结果时，对text的读取正好到达（包括）
                    对pattern的一个匹配 """
    # 确保能对pattern进行索引操作，同时制作pattern的
    # 的一个拷贝，以防在生成结果时意外地修改pattern
    pattern = list(pattern)
    length = len(pattern)
    # 创建KMP偏移量表并命名为shifts
    shifts = [1] * (length + 1)
    shift = 1

    for pos, pat in enumerate(pattern):
        while shift <= pos and pat != pattern[pos - shift]:
            shift += shifts[pos - shift]
        shifts[pos + 1] = shift

    # 执行真正的搜索
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == length or matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == length:
            yield startPos


def finditer(text, pattern):
    pos = -1
    while True:
        pos = text.find(pattern, pos + 1)
        if pos < 0:
            break
        yield pos
