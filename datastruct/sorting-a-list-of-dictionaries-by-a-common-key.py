# coding=utf-8
"""
通过某个关键字排序一个字典列表
ref:http://python3-cookbook.readthedocs.org/zh_CN/latest/c01/p13_sort_list_of_dicts_by_key.html
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'
from operator import itemgetter


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


def sorted_with_itemgetter():
    """
    通过使用 operator 模块的 itemgetter 函数进行排序
    着用方式会快点
    """
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))      # 支持多个key

    print rows_by_fname
    print rows_by_uid
    print rows_by_lfname


def sorted_with_lambda():
    """
    itemgetter() 有时候也可以用 lambda 表达式代替
    """
    rows_by_fname = sorted(rows, key=lambda r: r['fname'])
    rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
    print rows_by_fname
    print rows_by_lfname


sorted_with_lambda()

print min(rows, key=itemgetter('uid'))      # {'lname': 'Cleese', 'uid': 1001, 'fname': 'John'}
print max(rows, key=itemgetter('uid'))      # {'lname': 'Jones', 'uid': 1004, 'fname': 'Big'}

