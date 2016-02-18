# coding=utf-8
"""
数据结构初始化
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '2/18/16'


class Structure(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {0} arguments, {1} given'.format((len(self._fields)), len(args)))

        # 设置所有的位置参数
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # 设置剩余的关键字参数
        for name in self._fields[len(args):]:
            if name not in kwargs:
                raise TypeError('Missing argument:{}'.format(name))

            setattr(self, name, kwargs.pop(name))

        # 检查任何剩余的未知参数
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Book(Structure):
    _fields = ['name', 'star', 'price']


s1 = Book('ACME', 100, 100.20)
s2 = Book('ACME', 100, price=1000)
s4 = Book('ACME', other=50, price=91.1)
s5 = Book('ACME', star=50, price=91.1, aa=1)