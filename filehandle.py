#!/usr/bin/python
#-*- coding:utf-8 -*-
from __future__ import division  
__author__ = 'beginman'
import sys
import urllib
import urllib2
reload(sys)
sys.setdefaultencoding( "utf-8" )
import platform
import os
import time
import datetime

NOW = datetime.datetime.now()
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'
headers = {'User-Agent' : user_agent}

def ChoiceFile():
    """博客文件分布在windows或Linux"""
    filepath = '/home/beginman/gitblog/blog/_posts'
    system = 'linux'
    if (platform.system()).lower() == 'windows':
        system = 'windows'
        filepath = r'E:\gitblog\beginman.github.com\_posts'
    if os.path.isdir(filepath):
        files = os.listdir(filepath)		# 列出该目录下的所有文件
        files_list = []
        newfile = ''
        compareDate = 0
        for obj in files:
            dic ={}
            single_file = filepath+'\\'+obj if system == 'windows' else filepath+'/'+obj
            dic['name'] = obj
            timestamp = os.path.getmtime(single_file)			# 获取文件最近修改时间戳
            # 获取最新的文件
            if timestamp>compareDate:
                compareDate = timestamp
                newfile = obj
            x = time.localtime(timestamp)
            dic['date'] = time.strftime('%Y-%m-%d %H:%M:%S',x)
            size = os.path.getsize(single_file)					# 获取文件大小
            dic['size'] = str(round(size/1024,2))+' KB'
            files_list.append(dic)
        # 文件默认选择最新的一个，如果否定了则从输入中获取
        y_or_n = raw_input(u'我猜你要处理的文件是：%s \n请输入y或n来决定吧: ' % newfile).strip()
        if y_or_n == 'y':
            # 选择该文件
            choiced_file = filepath+'\\'+newfile if system == 'windows' else filepath+'/'+newfile
        else:
            filename = raw_input(u'输入要处理的文件名或模糊名称：').strip()
            if filename:
                # 模糊查询反馈结果
                result = fileMatch(files_list,filename)
                files_msg = u"""
				****************************************************************************
				\n"""
                count = 0
                for obj in result:
                    count += 1
                    files_msg+=u'[%s]   %s   %s   %s\n' %(count,obj['name'],obj['date'],obj['size'])
                msg_end = u"""
				****************************************************************************
				\n 请选择备选文件目录前的数字来选取指定文件： 
				"""
                files_msg += msg_end
                option = raw_input(files_msg)
                newfile = result[int(option)-1]['name']
                choiced_file = filepath+'\\'+newfile if system == 'windows' else filepath+'/'+newfile
        # 处理文件
        return HandleFile(choiced_file)




def fileMatch(files,keyword):
    """
	文件匹配
	1.*xx.md 选取以xx结尾的文件；2.文件关键字
	"""
    alternative_files = []		# 备选文件
    if keyword[0] == '*':
        for obj in files:
            if obj['name'].endswith(keyword):
                alternative_files.append(obj)
    else:
        for obj in files:
            if obj['name'].find(keyword) != -1:
                alternative_files.append(obj)
    return alternative_files




def HandleFile(filename):
    """Print files"""
    fp = open(filename)
    content = fp.readlines()[5:]        # Cut the jekyll syntax info.
    con_msg = ''                        # Content.
    for s in content:con_msg+=s
    sign = u'<b style="color:Green;font-size:13px;">*******这篇博客由Python自动同步发送,同步时间:%s*******\n' %NOW
    con_msg += sign
    return con_msg


def sent_cnblog():
    """发送到博客园"""
    url = 'http://passport.cnblogs.com/login.aspx'
    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': 'wEPDwULLTE1MzYzODg2NzZkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQtjaGtSZW1lbWJlcm1QYDyKKI9af4b67Mzq2xFaL9Bt',
        '__EVENTVALIDATION': '/wEdAAUyDI6H/s9f+ZALqNAA4PyUhI6Xi65hwcQ8/QoQCF8JIahXufbhIqPmwKf992GTkd0wq1PKp6+/1yNGng6H71Uxop4oRunf14dz2Zt2+QKDEIYpifFQj3yQiLk3eeHVQqcjiaAP',
        'tbUserName': 'BeginMan',
        'tbPassword': '1991fang',
        'btnLogin': '登  录',
        'txtReturnUrl': 'http://www.cnblogs.com/'
    }
    encode_data = urllib.urlencode(data)
    headers = {
        'User-Agent' : user_agent,
        'Host':'passport.cnblogs.com',
        'Origin':'http://passport.cnblogs.com',
        'Referer':'http://passport.cnblogs.com/login.aspx'
        }
    req = urllib2.Request(url,encode_data,headers=headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Reason:', e
        elif hasattr(e, 'code'):
            print 'Code:', e
    else:
        result = response.read()
        print response.geturl()
        print result


def main():
    # print ChoiceFile()
    sent_cnblog()


if __name__ == '__main__':
    main()


