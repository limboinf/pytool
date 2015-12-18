#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-03-29 21:34:59
# @Function: 常用的日期时间函数
# @Author  : BeginMan

import datetime
import time


def str_datetime_to_timestamp(str_datetime, define_format="%Y-%m-%d %H:%M:%S"):
    """将字符串的时间转换为时间戳"""
    time_array = time.strptime(str_datetime, define_format)
    return int(time.mktime(time_array))


def format_datetime(str_datetime, old_format, new_format):
    """字符串时间格式更改
    2013-10-10 23:40:00 --> 2013/10/10 23:40:00
    """
    time_array = time.strptime(str_datetime, old_format)
    new_format = time.strftime(new_format, time_array)
    return new_format


def timestamp_to_format_time(timestamp, define_format):
    """时间戳转换为指定格式日期"""
    time_array = time.localtime(timestamp)
    return time.strftime(define_format, time_array)


def get_now_format(define_format, type=0):
    """获取当前时间并装换指定格式"""
    if type:
        # 方式1：
        now = datetime.datetime.now()
        return now.strftime(define_format)
    else:
        # 方式2
        now = int(time.time())
        timeArray = time.localtime(now)
        return time.strftime(define_format, timeArray)


def get_datetime_by_days(day, define_format):
    """获取几天前或几天后的日期时间"""
    t = datetime.datetime.now() - datetime.timedelta(days=day)
    time_stamp = int(time.mktime(t.timetuple()))
    return t.strftime(define_format), time_stamp


def get_datetime_obj(str_datetime, define_format):
    """日期时间按字符串装换为datetime对象"""
    t_obj = datetime.datetime.strptime(str_datetime, define_format)
    return t_obj

now = datetime.datetime.now()
# 昨天，明天，明年
yestoday = now - datetime.timedelta(days=1)
tommorow = now + datetime.timedelta(days=1)
next_year = now + datetime.timedelta(days = 365)


if __name__ == '__main__':
    str_time = "2015-01-20 23:40:00"
    define_format = '%Y-%m-%d %H:%M:%S'

    print str_datetime_to_timestamp(str_time)
    print format_datetime(str_time,define_format, '%Y/%m/%d %H:%M:%S')
    print timestamp_to_format_time(1421768400, define_format)
    print get_now_format(define_format, 1)
    print get_now_format(define_format, 0)
    print get_datetime_by_days(3, define_format)
    print get_datetime_by_days(-3, define_format)
    print get_datetime_obj(str_time, define_format)
