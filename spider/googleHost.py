#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Function: Google Host
# @Author  : BeginMan
import os
import urllib
import urllib2
import re
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf8')


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/57.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
headers = {'User-Agent' : user_agent}
dic = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'hostspasscode=19066; _ga=GA1.2.1163994556.1420907346; _gat=1; Hm_lvt_e26a7cd6079c926259ded8f19369bf0b=1420903331; Hm_lpvt_e26a7cd6079c926259ded8f19369bf0b=1420907346',
        'Host':'serve.netsh.org',
}
headers = dict(dic, **headers)

def getGoogleHost():
    print u'正在抓取google Host...............'
    try:
        url = "http://serve.netsh.org/pub/hosts.php"
        data = urllib.urlencode({
            "passcode":19066,
            'gs':'on',
            'wk':'on',
            'twttr':'on',
            'fb':'on',
            'flkr':'on',
            'dpbx':'on',
            'odrv':'on'
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