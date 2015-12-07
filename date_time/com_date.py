#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-03-29 21:34:59
# @Function: 常用的日期时间函数
# @Author  : BeginMan

import datetime
import time

def str_datetime_to_timestamp(str_datetime, define_format="%Y-%m-%d %H:%M:%S"):
    """将字符串的时间转换为时间戳"""

    #先装换成struct_time对象
    timeArray = time.strptime(str_datetime, define_format)
    #print timeArray     # time.struct_time(tm_year=2015, tm_mon=1, tm_mday=20, tm_hour=23, tm_min=40, tm_sec=0, tm_wday=1, tm_yday=20, tm_isdst=-1)

    #将struct_time装换成时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp



def format_datetime(str_datetime, old_format, new_format):
    """字符串时间格式更改，如a = "2013-10-10 23:40:00",想改为 a = "2013/10/10 23:40:00"""
    timeArray = time.strptime(str_datetime, old_format)
    new_format = time.strftime(new_format, timeArray)
    return new_format



def timestamp_to_format_time(timestamp, define_format):
    """时间戳转换为指定格式日期"""
    timeArray = time.localtime(timestamp)
    format_time = time.strftime(define_format, timeArray)
    return format_time


def get_now_format(define_format, type=0):
    """获取当前时间并装换指定格式"""
    if type:
        #方式1：
        now = datetime.datetime.now()
        return now.strftime(define_format)
    else:
        #方式2
        now = int(time.time())  #时间戳
        timeArray = time.localtime(now)
        return time.strftime(define_format, timeArray)


def get_datetime_by_days(day, define_format):
    """获取几天前或几天后的日期时间"""
    t = datetime.datetime.now() - datetime.timedelta(days=day)
    timeStamp = int(time.mktime(t.timetuple()))
    return t.strftime(define_format), timeStamp



def get_datetime_obj(str_datetime, define_format):
    """日期时间按字符串装换为datetime对象"""
    t_obj = datetime.datetime.strptime(str_datetime, define_format)
    print type(t_obj)
    return t_obj



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
