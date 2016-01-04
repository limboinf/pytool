# coding=utf-8
"""
命名切片

内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。
避免了大量无法理解的硬编码下标
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'


items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print items[a]
print items[2: 4]

items[a] = [100, 101]
print items

del items[a]
print items


s = slice(5, 50, 2)
print s.start, s.step, s.stop

s = 'HelloWorld'
print a.indices(len(s))

for i in range(*a.indices(len(s))):
    print s[i]
