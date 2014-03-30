#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-03-30 21:31:53
# @Function: 爬点东西
# @Author  : BeginMan

#-*- encoding: gb2312 -*-
import urllib2, httplib
httplib.HTTPConnection.debuglevel = 1  
url = 'https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//beginman.cn/&response_type=code&client_id=2045297459'             

request = urllib2.Request(url)
opener = urllib2.build_opener()
f = opener.open(request)
print f.headers.dict