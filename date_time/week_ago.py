# coding=utf-8
"""
计算从指定时间到周N的时间距离
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/8/16'

from datetime import datetime, timedelta


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    """
    当前日期时间对象与timedelta(days=n)之差
    """
    if not start_date:
        start_date = datetime.today()
    week = start_date.weekday()
    week_ago = weekdays.index(dayname)
    ago = (7 + week - week_ago) % 7
    if ago == 0:
        ago = 7

    return start_date - timedelta(days=ago)


print get_previous_byday('Tuesday')


def get_previous_by_dateutil(dayname, start_date=None, start_type=1):
    """
    dateutil 模块计算
    @:param start_type：表示之前(0)还是之后(-1)，
    """
    from dateutil.relativedelta import relativedelta
    from dateutil import rrule

    rrule_weekdays = {'Monday': rrule.MO,
                      'Tuesday': rrule.TU,
                      'Wednesday': rrule.WE,
                      'Thursday': rrule.TH,
                      'Friday': rrule.FR,
                      'Saturday': rrule.SA,
                      'Sunday': rrule.SU}
    if not start_date:
        start_date = datetime.now()

    weekday_obj = rrule_weekdays.get(dayname)
    return start_date + relativedelta(weekday=weekday_obj(start_type))


print get_previous_by_dateutil('Tuesday', start_type=-1)