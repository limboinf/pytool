# coding=utf-8
"""
通过某个字段将记录分组

groupby()函数扫描整个序列并且查找连续相同值(或者根据指定key函数返回值相同)的元素序列。
在每次迭代的时候，它会返回一个值和一个迭代器对象，这个迭代器对象可以生成元素值全部等于上面那个值的组中所有对象。

一个非常重要的准备步骤是要根据指定的字段将数据排序。
因为 groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。

如果你仅仅只是想根据date字段将数据分组到一个大的数据结构中去，并且允许随机访问
那么你最好使用 defaultdict() 来构建一个多值字典
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


# 首先按日期进行排序
rows.sort(key=itemgetter('date'))

# 然后再按date分组
for date, items in groupby(rows, key=itemgetter('date')):
    print date
    for i in items:
        print i

# outPrint:
# 07/01/2012
# {'date': '07/01/2012', 'address': '5412 N CLARK'}
# {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
# 07/02/2012
# {'date': '07/02/2012', 'address': '5800 E 58TH'}
# {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
# {'date': '07/02/2012', 'address': '1060 W ADDISON'}
# 07/03/2012
# {'date': '07/03/2012', 'address': '2122 N CLARK'}
# 07/04/2012
# {'date': '07/04/2012', 'address': '5148 N CLARK'}
# {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}

from collections import defaultdict
rows_by_date = defaultdict(list)

print rows_by_date      # defaultdict(<type 'list'>, {})

for i in rows:
    rows_by_date[i['date']].append(i)

for k, v in rows_by_date.items():
    print k
    print v

# outPrint:
# 07/02/2012
# [{'date': '07/02/2012', 'address': '5800 E 58TH'}, {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}, {'date': '07/02/2012', 'address': '1060 W ADDISON'}]
# 07/01/2012
# [{'date': '07/01/2012', 'address': '5412 N CLARK'}, {'date': '07/01/2012', 'address': '4801 N BROADWAY'}]
# 07/04/2012
# [{'date': '07/04/2012', 'address': '5148 N CLARK'}, {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}]
# 07/03/2012
# [{'date': '07/03/2012', 'address': '2122 N CLARK'}]

