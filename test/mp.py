# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
from math import radians, cos, sin, asin, sqrt


# todo hihihi


def haversine(lon1, lat1, lon2, lat2):    # 经度1，纬度1，经度2，纬度2 （十进制度数）
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371        # 地球平均半径，单位为公里
    return c * r * 1000     # 返回米


print haversine(106.486654,29.490295,106.581515,29.615467)      # 16670.9042735
# http://developer.baidu.com/map/jsdemo.htm#a6_1
