#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-01 05:18:57
# @Function: 把 debug Log 打开
# @Author  : BeginMan

import urllib2
httpHandler =  urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.google.com')
