#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Function: Google Host
# @Author  : BeginMan
import os
import urllib
import urllib2
import cookielib
import re
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf8')

# 获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
# 将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
# 创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# 将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/57.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
headers = {'User-Agent' : user_agent}
dic = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection':'keep-alive',

        # Cookie 变更
        'Cookie':'hostspasscode=78053; Hm_lvt_e26a7cd6079c926259ded8f19369bf0b=1420903331,1422351431; Hm_lpvt_e26a7cd6079c926259ded8f19369bf0b=1422450312; _ga=GA1.2.1163994556.1420907346; _gat=1',
        'Host':'serve.netsh.org',
        'Referer':'http://serve.netsh.org/pub/gethosts.php',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
}

headers = dict(dic, **headers)

def getGoogleHost():
    print u'正在抓取google Host...............'
    try:
        url = "http://serve.netsh.org/pub/hosts.php"
        data = urllib.urlencode({
            "passcode":88194,
            'gs':'on',
            'wk':'on',
            'twttr':'on',
            'fb':'on',
            'flkr':'on',
            'dpbx':'on',
            'yt':'off',
            'validate':'b72bf',
            'nolh':'off',
        })
        url = url+'?'+data
        req = urllib2.Request(url, headers=headers)
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'Reason: ', e
            elif hasattr(e, 'code'):
                print 'Code: ', e
        else:
            host = response.read()
            host = unzip(host)
            print host
            writeHost(host)
    except Exception, e:
        print '失败'
        print e

    print u'全部处理完毕'



def unzip(data):
    import gzip
    import StringIO
    data = StringIO.StringIO(data)
    gz = gzip.GzipFile(fileobj=data)
    data = gz.read()
    gz.close()
    return data

def writeHost(host):
    hosts = '/etc/hosts'
    with open(hosts, 'w') as f:
        f.writelines(host)


if __name__ == '__main__':
    getGoogleHost()