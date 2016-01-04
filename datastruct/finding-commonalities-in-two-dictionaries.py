# coding=utf-8
"""
两个字典中寻找相同点(比如相同的键、相同的值等)-->集合操作
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'


a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}


# 为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作。比如：

print set(a.keys()) & set(b.keys())         # set(['y', 'x'])
print set(a.values()) & set(b.values())     # set([2])

print {key: a[key] for key in set(a.keys()) - {'z', 'w'}}       # {'y': 2, 'x': 1}


