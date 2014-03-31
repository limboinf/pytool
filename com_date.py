#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-03-29 21:34:59
# @Function:
# @Author  : BeginMan

import datetime
import time

def get_date(str_date,days):
    tem = time.mktime(time.strptime(str_date,'%Y-%m-%d %H:%M:%S'))
    x = time.localtime(tem)
    date = datetime.datetime(x.tm_year,x.tm_mon,x.tm_mday,x.tm_hour,x.tm_min,x.tm_sec)
    hope_date_format = date+datetime.timedelta(days=days)
    return hope_date_format

if __name__ == '__main__':
    get_date('2011-09-28 10:00:00',1)

