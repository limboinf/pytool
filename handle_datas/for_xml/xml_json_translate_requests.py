# coding=utf-8
"""
xml和json相关转换并使用requests 发起HTTP请求

xmltodict: https://github.com/martinblech/xmltodict
requests: https://github.com/kennethreitz/requests
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/7/15'

import requests
import xmltodict

mydict = {
    'name':'beginman',
    'cid': 1001
}

xml = xmltodict.unparse(mydict, pretty=True)
xml = xml.encode('utf-8')

# set what your server accepts
headers = {'Content-Type': 'application/xml'}
print requests.post('http://beginman.cn', data=xml, headers=headers).text
