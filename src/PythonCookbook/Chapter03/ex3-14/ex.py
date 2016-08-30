#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-17

@author: CaiKnife
"""

import decimal, re, operator

parse_input = re.compile(r"""(?x)    # 允许RE中的注释和空白符
                        (\d+\.?\d*)  # 带有可选的小数部分的数
                        \s*          # 可选的空白符
                        ([-+/*])     # 运算符
                        $""")  # 字符串结束

oper = {'+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv, }

total = decimal.Decimal('0')


def print_total():
    print '== == =\n', total


print """Welcome to Adding Machine:
Enter a number and operator,
an empty line to see the current subtotal,
or q to quit:
"""

while True:
    try:
        tape_line = raw_input().strip()
    except EOFError:
        tape_line = 'q'
    if not tape_line:
        print_total()
        continue
    elif tape_line == 'q':
        print_total()
        break

    try:
        num_next, op = parse_input.match(tape_line).groups()
    except AttributeError:
        print 'Invalid entry: %r' % tape_line
        print 'Enter number and operator, empty line for total, q to quit'
        continue

    total = oper[op](total, decimal.Decimal(num_next))
