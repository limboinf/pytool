# coding=utf-8
"""
代理迭代
在任何可迭代对象中执行迭代操作只需要定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上去
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/9/16'


class Node(object):
    def __init__(self, name):
        self.name = name
        self._children = []

    def __repr__(self):
        return '<Node: %r>' % self.name

    def __iter__(self):
        # 将迭代请求传递给内部的 _children 属性。
        return iter(self._children)

    def __add__(self, other):
        self._children.append(other)


root = Node('root')
child_a = Node('a')
child_b = Node('b')
root + child_a
root + child_b

for obj in root:
    print obj


# outputs:
# <Node: 'a'>
# <Node: 'b'>
