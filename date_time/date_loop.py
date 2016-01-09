# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/8/16'

from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        # 巧妙之处：计算出一个对应月份第一天的日期
        # 使用 date 或 datetime 对象的 replace() 方法简单的将 days 属性设置成1即可
        start_date = date.today().replace(day=1)

    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


# a_day = timedelta(days=1)
# first_day, last_day = get_month_range()
# while first_day < last_day:
#     print(first_day)
#     first_day += a_day


for d in date_range(datetime(2016, 1, 1), datetime(2016, 2, 1), timedelta(hours=6)):
    print d