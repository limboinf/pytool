#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-03-30 21:53:13
# @Function: 发送新浪微博
# @Author  : BeginMan
import os
import urllib
import urllib2
import re
import sys
from datetime import *
from HTMLParser import HTMLParser
reload(sys)
sys.setdefaultencoding('utf8')
import weibo

# 自己的新浪微博api 应用 (http://open.weibo.com/webmaster/build/?siteid=2045297459)
APP_KEY = '2045297459'  
APP_SECRET = '72e31e46b688167303d2ea737194fac1'  
CALL_BACK = 'http://beginman.cn/'  


user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'
headers = {'User-Agent' : user_agent}
regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)



class MyHTMLParser(HTMLParser):
    """HTML解析"""
    def __init__(self):
        HTMLParser.__init__(self)
        self.values = []
        self.links = []
 
    def handle_starttag(self, tag, attrs):
        """获取生成短网址文本框value和自己网站的最新博客链接"""
        if tag == "input":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    if variable == "value":
                        if regex.match(value):
                            self.values.append(value)
        if tag == 'a':
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        if regex.match(value):
                            self.links.append(value)

def WeiboRun(): 
     
    client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)        # weibo模块的APIClient是进行授权、API操作的类，先定义一个该类对象，传入参数为APP_KEY, APP_SECRET, CALL_BACK  
    auth_url = client.get_authorize_url()                           # 获取该应用（APP_KEY是唯一的）提供给用户进行授权的url  
    print u'还是将这个url粘贴到浏览器上吧\n %s' %auth_url                 ## 数据格式：http://beginman.cn/?code=1caa08eb6c0e7d44bd26feb4419efa82 
    code = raw_input(u'请输入code:\n')                             
    # 获取博客最新文章链接
    beginman = 'http://beginman.cn/'
    new_url = get_blog_newurl(beginman)
    weibo_short_url = get_short_url(new_url)                        # 获取微博短链接
    
    #通过该code获取access_token，r是返回的授权结果，具体参数参考官方文档：  
    # http://open.weibo.com/wiki/Oauth2/access_token  
    r = client.request_access_token(code)   
    client.set_access_token(r.access_token, r.expires_in)           # 将access_token和expire_in设置到client对象  
    
    # 发布微博  
    now = datetime.now()
    while True:  
        print u"是否要发布微博?(y/n)"  
        choice = raw_input()  
        if choice == 'y' or choice == 'Y':  
            content = """
            BeginMan于%s,在博客中(beginman.cn)发布了一篇惊天地泣鬼神的博客，相信会对你有帮助的，＼(◎o◎)／..点击链接查看%s
            """%(now,new_url)  
            # status=u'测试OAuth 2.0带图片发微博', pic=open('/Users/michael/test.png')
            #调用接口发一条新微薄，status参数就是微博内容  
            client.statuses.update.post(status=content)  
            print "微博发送成功！"  
            break;  
            
        if choice == 'n' or choice == 'N':  
            break      
        

def get_blog_newurl(blog_url):
    """通过验证，到自己网站中抓取数据，最新博客链接"""
    req = urllib2.Request(blog_url,headers=headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Reason: ', e
        elif hasattr(e, 'code'):
            print 'Code: ', e
    else:
        result = response.read()
        hp = MyHTMLParser()
        hp.feed(result)
        hp.close()
        # 选取链接
        links_list = hp.links          # 所有链接列表
        links_msg = u"""
        ****************************************************************************
        \n"""
        count = 0
        for obj in links_list:
            count += 1
            links_msg+=u'[%s]   %s \n' %(count,obj)
        msg_end = u"""
        ****************************************************************************
        \n 请选择链接前的数字来选取吧： 
        """
        links_msg += msg_end
        option = raw_input(links_msg)
        newurl = links_list[int(option)-1]
        return newurl
             
        


def get_short_url(long_url):
    """生成微博短网址"""
    data = {'url':long_url}
    data = urllib.urlencode(data)
    req = urllib2.Request('http://www.waqiang.com/index.php/url/shorten',data,headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Reason: ', e
        elif hasattr(e, 'code'):
            print 'Code: ', e
    else:
        result = response.read()
        hp = MyHTMLParser()
        hp.feed(result)
        hp.close()
        values_list = hp.values[0]
        return values_list   

def Get_Blog_Info(url):
    """"获取博客标题和简介，如果有图片抓取图片"""
    req = urllib2.Request(url,headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Reason: ', e
        elif hasattr(e, 'code'):
            print 'Code: ', e
    else:
        result = response.read()
        hp = MyHTMLParser()
        hp.feed(result)
        hp.close()
        values_list = hp.values[0]
        return values_list   

           
        
def main():
    WeiboRun()

if __name__ == '__main__':
    main()
        
