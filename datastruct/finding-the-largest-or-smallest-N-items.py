# coding=utf-8
"""
查找最大或最小的N个元素
    当N较小时，使用heapq:`nlargest()` & `nsmallest()`
    当N较大时，先排序在切片:sorted(items)[:N]
    当N为1时，使用`max()`,`min()`

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print heapq.nlargest(3, nums)       # 查找最大的三个元素,正序  [42, 37, 23]
print heapq.nsmallest(3, nums)      # 查找最小的三个元素,正序  [-4, 1, 2]

# 查找最大和最小
print min(nums), max(nums)          # -4 42

# 将集合数据进行堆排序
heapq.heapify(nums)
print nums                      # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

books = [
    {"book": "Python Cookbook", 'price': 112},
    {"book": "Redis In Action", 'price': 72},
    {"book": "Fluent Python", 'price': 182},
    {"book": "Code Complete", 'price': 148}
]

print heapq.nlargest(2, books, lambda x: x['price'])

