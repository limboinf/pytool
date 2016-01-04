# coding=utf-8
"""
字典的运算,如求最小值、最大值、排序等
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


def min_or_max_for_dict(dic):
    """求字典最大值最小值"""
    ziped = zip(dic.values(), dic.keys())
    return max(ziped), min(ziped)


def sorted_dict(dic):
    """字典数据排序"""
    ziped = zip(dic.values(), dic.keys())
    return sorted(ziped)


print sorted_dict(prices)


# 一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值
print max(prices)                               # IBM
print max(prices.values())                      # 612.78

# 可以在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息。比如：
print max(prices, key=lambda x: prices[x])      # AAPL

