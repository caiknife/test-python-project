#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-17

@author: CaiKnife
'''

import decimal

def make_table(n=1):
    try:
        return '\t'*n
    except TypeError, e:
        return ' '

def italformat(value, places=2, curr='EUR', sep='.', dp=',', pos='', neg='-', overall=10):
    """ 将十进制value转化为财务格式的字符串
    places: 十进制小数点后的数字的位数
    curr: 可选的货币符号，可能为空
    sep: 可选的分组（三个一组）分隔符（逗号、句号或空白）
    dp: 小数点指示符（逗号或是句号）当places为0时，小数点被指定为空白
    pos: 正数的可选的符号 '+'、空格或空白
    neg: 负数的可选的符号 '-'、'('、空格或空白
    overall: 最终结果的可选的总长度，若长度不够，左边货币符号和数字之间会被填充符占据
    """
    q = decimal.Decimal((0, (1,), -places))
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    append, next = result.append, digits.pop
    
    for i in range(places):
        if digits:
            append(next())
        else:
            append('0')
    append(dp)
    i = 0
    
    while digits:
        append(next())
        i += 1
        if i==3 and digits:
            i = 0
            append(sep)
    
    while len(result) < overall:
        append(' ')
    
    append(curr)
    
    if sign:
        append(neg)
    else:
        append(pos)
        
    result.reverse()
    return ''.join(result)

def getsubtotal(subtin=None):
    if subtin == None:
        subtin = input('Enter the subtotal: ')
    subtotal = decimal.Decimal(str(subtin))
    print '\n subtotal: ', make_table(3), italformat(subtotal)
    return subtotal

def cnpcalc(subtotal):
    contrib = subtotal * decimal.Decimal('0.02')
    print '+ contributo integrativo 2%: ', make_table(), italformat(contrib, curr='')
    return contrib

def vatcalc(subtotal, cnp):
    vat = (subtotal+cnp) * decimal.Decimal('0.20')
    print '+ IVA 20%: ', make_table(3), italformat(vat, curr='')
    return vat

def ritacalc(subtotal):
    rit = subtotal * decimal.Decimal('0.20')
    print "- Ritenuta d'acconto 20%: ", make_table(), italformat(rit, curr='')
    return rit

def dototal(subtotal, cnp, iva=0, rit=0):
    total = (subtotal+cnp+iva) - rit
    print 'TOTALE: ', make_table(3), italformat(total)
    return total

def invoicer(subtotal=None, context=None):
    if context is None:
        decimal.getcontext().rounding = 'ROUND_HALF_UP'
    else:
        decimal.setcontext(context)
        
    subtot = getsubtotal(subtotal)
    contrib = cnpcalc(subtot)
    dototal(subtot, contrib, vatcalc(subtot, contrib), ritacalc(subtot))
    
if __name__ == '__main__':
    print "Welcome to the invoice calculator"
    tests = [100, 1000.00, "10000", 555.55]
    print "Euro context"
    for test in tests:
        invoicer(test)
    print "default context"
    for test in tests:
        invoicer(test, context=decimal.DefaultContext)
