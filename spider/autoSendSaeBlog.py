#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-07-16
# @Function: 自动发送SAE blog.
# @Author  : BeginMan

import urllib2
import urllib
import sys
import cookielib
import simplejson as json
reload(sys)
sys.setdefaultencoding('utf8')


user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'
headers = {'User-Agent' : user_agent}

def getCategoryOrTag(type=1):
    """get blog categories or tags"""
    if type:
        url='http://beginman.sinaapp.com/api/category/'
    else:
        url='http://beginman.sinaapp.com/api/tag/'
    req = urllib2.Request(url, headers=headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Reason: ', e
        elif hasattr(e, 'code'):
            print 'Code: ', e
    else:
        datas = response.read()
        return datas


def getMenuDatas():
    """get menu"""
    title = ''
    while not title:
        title = raw_input('标题： ').strip()

    categories = json.loads(getCategoryOrTag())
    cateID = 0
    while not cateID:
        for obj in categories:
            print '(%s) %6s' % (obj['id'], obj['name'])
        cateID = raw_input(u'分类ID：')

    cateID = int(cateID)

    id_tag = ''
    tags = json.loads(getCategoryOrTag(0))
    while not id_tag:
        print ','.join([i['name'] for i in tags])
        id_tag = raw_input(u'标签：')
    id_tag = json.dumps(id_tag.split(','))

    blogFile, content = '', ''
    while not blogFile and not content:
        blogFile = raw_input(u'博客文件：')
        with open(blogFile, 'r') as f:
            content = f.read()
    data = {'title':title, 'content':content,'id_tag':id_tag}
    data = urllib.urlencode(data)
    return data, cateID


def login():
    """login blog"""
    loginurl = 'http://beginman.sinaapp.com/login/'
    loginInfo = urllib.urlencode({'us':'****', 'pwd':'****'})
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    req = urllib2.Request(loginurl, loginInfo,headers=headers)
    response = None
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Reason: ', e
        elif hasattr(e, 'code'):
            print 'Code: ', e
    finally:
        if response and response.getcode() == 200:
            print u'登陆成功！'
            return True

        return False



def postBlog():
    """post"""
    datas = getMenuDatas()
    login()
    datas = datas[0]+'&type=%s' %datas[1]
    url='http://beginman.sinaapp.com/manage/add/'
    req = urllib2.Request(url, datas, headers=headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Reason: ', e
        elif hasattr(e, 'code'):
            print 'Code: ', e
    finally:
        if response.getcode() == 200:
            print u'上传成功！'






def main():
    postBlog()

if __name__ == '__main__':
    main()


