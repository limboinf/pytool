#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-01 05:16:42
# @Function: 返回URL状态码
# @Author  : BeginMan

import urllib2
try:
	response = urllib2.urlopen('http://bbs.csdn.net/why')
except urllib2.HTTPError, e:
	print e.code
