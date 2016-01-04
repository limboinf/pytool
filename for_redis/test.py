# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/22/15'
import redis

r = redis.Redis(password='2015yunlianxiQAZWSX')

st = []
for i in range(100):
    print r.getbit('uu', i)
