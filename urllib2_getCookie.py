#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-01 04:58:08
# @Function:
# @Author  : BeginMan

import os
import urllib2
import cookielib

"""获取Cookie"""
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
print cookie
print '*'*10
for i in cookie:
	print 'name:=' +i.name
	print 'value:=' +i.value 

