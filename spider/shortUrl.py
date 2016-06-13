#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-03-30 21:53:13
# @Function: 短网址生成
# @Author  : BeginMan
import urllib
import urllib2
import re
import sys
from HTMLParser import HTMLParser
reload(sys)
sys.setdefaultencoding('utf8')


user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'
headers = {'User-Agent': user_agent}
regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.values = []

    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "input":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "value":
                        self.values.append(value)


def input_url():
    url = ''
    while True:
        url = raw_input('请输入想要处理的网址：\n')
        if regex.match(url):
            break
    return url


def get_short_url():
    url = input_url()
    data = {'url': url}
    data = urllib.urlencode(data)
    req = urllib2.Request(
        'http://www.waqiang.com/index.php/url/shorten',
        data,
        headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError as e:
        if hasattr(e, 'reason'):
            print 'Reason: ', e
        elif hasattr(e, 'code'):
            print 'Code: ', e
    else:
        result = response.read()
        hp = MyHTMLParser()
    hp.feed(result)
    hp.close()
    print(hp.values)


def main():
    get_short_url()

if __name__ == '__main__':
    main()
