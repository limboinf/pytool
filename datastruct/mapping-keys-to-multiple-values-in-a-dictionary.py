# coding=utf-8
"""
一个键对应多个值的字典的三种实现方法

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'


# method 1:一个键映射多个值，将这多个值放到另外的容器中，比如列表或者集合里面
dic1 = {
    'key_1': [1, 3, 4, 5],      # 保持元素的插入顺序就应该使用列表
    'key_2': {1, 3, 5}          # 去掉重复元素就使用集合
}

# method 2:collections模块defaultdict来始化每个 key 刚开始对应的值
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(10)
print d         # defaultdict(<type 'list'>, {'a': [1, 2], 'b': [10]})

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
print d         # defaultdict(<type 'set'>, {'a': set([1, 2])})

# method 3:setdefault
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(10)
print d         # {'a': [1, 2], 'b': [10]}
