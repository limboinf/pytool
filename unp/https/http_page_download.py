# coding=utf-8
"""
下载HTTP(非TSL)
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import httplib


class MyHTTP:

    def __init__(self, host):
        self.host = host

    def fetch(self):
        # 创建http对象
        http = httplib.HTTP(self.host)

        # 准备请求路径和头部
        http.putrequest("GET", '/')

        http.putheader('User-Agent', __file__)
        http.putheader('Host', self.host)
        http.putheader('Accetp', '*/*')
        http.endheaders()

        try:
            errcode, errmsg, headers = http.getreply()      # 发起请求
        except Exception as e:
            print 'err', e, errcode, errmsg, headers
        else:
            print "Got homepage from %s" % self.host

        file = http.getfile()                               # 获取响应
        return file.read()


if __name__ == '__main__':
    http = MyHTTP('www.jianshu.com')
    print http.fetch()
