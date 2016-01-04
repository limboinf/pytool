# coding=utf-8
"""
保存字典顺序，插入和内部组合顺序一致

需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候
那么你就得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'
import json


def un_sorted_dict():
    """无序"""
    d = dict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4
    return d, json.dumps(d)

print un_sorted_dict()
# ({'a': 1, 'c': 3, 'b': 2, 'd': 4}, '{"a": 1, "c": 3, "b": 2, "d": 4}')


def sorted_dict():
    """
    使用 collections 模块中的 OrderedDict 类

    OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
    每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。
    对于一个已经存在的键的重复赋值不会改变键的顺序。

    """
    from collections import OrderedDict
    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4
    return d, json.dumps(d)

print sorted_dict()
# (OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)]), '{"a": 1, "b": 2, "c": 3, "d": 4}')
