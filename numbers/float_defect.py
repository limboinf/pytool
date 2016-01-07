# coding=utf-8
"""
Python浮点数缺陷

>>> a = 0.1+0.2
>>> a
0.30000000000000004
>>> round(a, 2)
0.3
>>> 0.1+0.2 == 0.3
False

这些错误是由底层CPU和IEEE 754 (ref:https://zh.wikipedia.org/zh-cn/IEEE_754)
标准通过自己的浮点单位去执行算术时的特征。
由于Python的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的误差。

如果你想更加精确(并能容忍一定的性能损耗)，你可以使用 decimal 模块：

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/7/16'


"""
In [4]: from decimal import Decimal

In [5]: a = Decimal('0.1')

In [6]: b = Decimal('0.2')

In [7]: a + b
Out[7]: Decimal('0.3')

In [9]: a + b == Decimal('0.3')
Out[9]: True

In [12]: b
Out[12]: Decimal('1.7')

In [13]: a / b
Out[13]: Decimal('0.7647058823529411764705882353')

In [14]: from decimal import localcontext

In [15]: with localcontext() as ctx:
   ....:     ctx.prec = 3
   ....:     print a / b
   ....:
0.765

In [16]: with localcontext() as ctx:
    ....:   ctx.prec = 10
    ....:   print a / b
    ....:
0.7647058824

"""
