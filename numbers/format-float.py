# coding=utf-8
"""
数字的格式化输出，使用format()还是挺有意思的
'[<>^]?width[,]?(.digits)?':其中 width 和 digits 为整数，？代表可选部分。

>>> x = 1234.56789
>>> format(x, '0.1f')
'1234.6'
>>> format(x, '10.1f')
'    1234.6'
>>> format(x, '>10.1f')
'    1234.6'
>>> format(x, '<10.1f')
'1234.6    '
>>> format(x, '*>10.1f')
'****1234.6'
>>> format(x, '^10.1f')
'  1234.6  '
>>> format(x, ',')
'1,234.56789'
>>> format(x, '0,.1f')
'1,234.6'
>>> format(x, ',.1f')
'1,234.6'
>>> format(x, ',.3f')
'1,234.568'
>>> format(x, 'e')
'1.234568e+03'
>>> format(x, 'E')
'1.234568E+03'
>>> format(x, '0.2E')
'1.23E+03'

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/7/16'

