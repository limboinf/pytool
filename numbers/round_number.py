# coding=utf-8
"""
四舍五入

round(number[, ndigits]) -> floating point number

    Round a number to a given precision in decimal digits (default 0 digits).
    This always returns a floating point number.  Precision may be negative.

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/7/16'

print round(1.25, 1)        # 1.3
print round(1.5)            # 2.0
print round(2.5)            # 3.0

# round()函数的 ndigits 参数如果负数，则舍入运算会作用在十位、百位、千位等上面。
a = 1627731
print round(a, -1)          # 1627730.0
print round(a, -2)          # 1627700.0
print round(a, -3)          # 1628000.0
print round(a, -4)          # 1630000.0

# 如果用于输出宽度则格式化即可
x = 1.23456
print format(x, '0.2f')
print 'value is {:0.3f}'.format(x)

# Python浮点数
"""
>>> a = 0.1+0.2
>>> a
0.30000000000000004
>>> round(a, 2)
0.3
>>> 0.1+0.2 == 0.3
False
"""