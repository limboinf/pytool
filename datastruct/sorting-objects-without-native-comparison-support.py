# coding=utf-8
"""
排序不支持原生比较的对象

内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给它
这个 callable 对象对每个传入的对象返回一个值，这个值会被 sorted 用来排序这些对象。
ref:http://python3-cookbook.readthedocs.org/zh_CN/latest/c01/p14_sort_objects_without_compare_support.html

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'


class User(object):
    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return '<User({})>'.format(self.uid)


users = [User(30), User(2), User(10), User(50)]
print users

# 以 User 实例作为输入并输出对应 uid 值的 callable 对象
sorted_users = sorted(users, key=lambda u: u.uid)
print sorted_users

# 另外一种方式是使用 operator.attrgetter() 来代替lambda函数：
# 注意不是itemgetter-->item getter; 而是 attrgetter-->attr getter
from operator import attrgetter
sorted_uids = sorted(users, key=attrgetter('uid'))
print sorted_uids

# 同样适用于像 min() 和 max() 之类的函数
print min(users, key=attrgetter('uid'))
print max(users, key=lambda u: u.uid)
