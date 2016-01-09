# coding=utf-8
"""
使用生成器创建新的迭代模式
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/9/16'


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for i in frange(0, 4, 0.5):
    print i