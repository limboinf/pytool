# coding=utf-8
"""
删除序列相同元素并保持顺序
如果使用set()则删除相同元素，但顺序会打乱
如果想保持元素在某一点位置不变，则可以考虑使用生成器

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'

a = [1, 5, 2, 1, 9, 1, 5, 10]
print set(a)            # set([1, 2, 10, 5, 9])


def method1(items):
    n = []
    for i in items:
        if i not in n:
            n.append(i)
    return n


def method2(items):
    """更高效些"""
    n = set()
    for i in items:
        if i not in n:
            yield i
            n.add(i)


print method1(a)            # [1, 5, 2, 9, 10]
print list(method2(a))      # [1, 5, 2, 9, 10]


# 如果如果你想读取一个文件，消除重复行，你可以很容易像这样做：
#
# with open(somefile,'r') as f:
# for line in method2(f):
#     ...

