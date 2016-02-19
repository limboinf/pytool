# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/15/16'

import urllib2

url = "https://www.zhihu.com/question/39525296?group_id=671466352761913344"

print urllib2.urlopen(url, timeout=3)

request = urllib2.Request(url=url, data={}, headers={'name': 'zh'})   # error with `data={}`
request.add_header('User-Agent', 'Mozilla/5.0')
print request.data
print request.headers
print urllib2.urlopen(request, timeout=3)
