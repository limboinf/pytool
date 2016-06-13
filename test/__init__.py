# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
lis = [{
  'week_count': 1,
  'weekly_month': 6,
  'weekly_year': 2016},
 {'week_count': 1,
  'weekly_month': 6,
  'weekly_year': 2016},
 {'week_count': 2,
  'weekly_month': 6,
  'weekly_year': 2016}]

tmp = []
for obj in lis:
    if obj not in tmp:
        tmp.append(obj)

print tmp