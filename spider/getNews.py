#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-07-15
# @Function: 抓取新闻联播稿子
# @Author  : BeginMan
import os
import urllib
import urllib2
import re
import sys
import datetime
import calendar
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'
headers = {'User-Agent' : user_agent}

regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def getUrl():
    """生成url"""
    baseUrl = "http://cctv.cntv.cn/lm/xinwenlianbo/"
    dates = getFinalDates()
    urls = [('%s%s.shtml' %(baseUrl, i), i) for i in dates]
    return urls


def unfoldList(multList):
    """摊平列表"""
    dates = [y for x in multList for z in x for j in z for y in j]
    dates_ = sorted(list(set(dates)))
    int_dates = [int('%s%s%s' % (i.year, i.month if i.month>=10 else '0'+str(i.month), i.day if i.day>=10 else '0'+str(i.day))) for i in dates_]
    now = datetime.datetime.now()
    int_now = int('%s%s%s' %(now.year, now.month if now.month>=10 else '0'+str(now.month), now.day if now.day>=10 else '0'+str(now.day)))
    result_dates = [i for i in int_dates if i < int_now]
    return result_dates


def getFinalDates():
    """获取2013~2014年最终日期"""
    cal = calendar.Calendar()
    calendar_2013 = cal.yeardatescalendar(2013)
    calendar_2014 = cal.yeardatescalendar(2014)
    dates_2013 = unfoldList(calendar_2013)
    dates_2014 = unfoldList(calendar_2014)
    return list(set(dates_2013+dates_2014))


def getRemoteUrl():
    """获取cctv.cntv.cn视频地址"""
    urls = getUrl()
    for url in urls:
        print u'正在抓取第%s期新闻联播................' %url[1]
        try:
            req = urllib2.Request(url[0], headers=headers)
            try:
                response = urllib2.urlopen(req)
            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    print 'Reason: ', e
                elif hasattr(e, 'code'):
                    print 'Code: ', e
            else:
                html_doc = response.read()
                soup = BeautifulSoup(html_doc)
                remoteUrls = soup.find_all("div", class_="title_list_box_130503")[0].find_all('a')
                remoteUrls = remoteUrls[1:]
                remoteUrlsDatas = [(i['href'], i.get_text()) for i in remoteUrls]
                # 调用另一页面方法
                datas = htmlText(remoteUrlsDatas)
                prettyTxt(url[1], datas)
                print u'第%s期新闻联播处理完毕' %url[1]
        except Exception, e:
            print '第%s期下载失败' %url[1]
            print e
            
    print u'全部处理完毕'


def htmlText(remoteUrls):
    """抓取页面文本"""
    datas = []
    for url in remoteUrls:
        req = urllib2.Request(url[0], headers=headers)
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'Reason: ', e
            elif hasattr(e, 'code'):
                print 'Code: ', e
        else:
            html_doc = response.read()
            soup = BeautifulSoup(html_doc)
            text = soup.find_all("div", class_="body")[0].find_all('p')
            textString='*'.join([i.get_text() for i in text])
            title = url[1]  # 新闻标题
            # 写入文件中
            dic = {}
            dic['title'] = title
            dic['text'] = textString
            datas.append(dic)
    return datas


def prettyTxt(title, datas):
    """写入文件，美化文本"""
    print u'正在写入中……'
    fobj = open('/home/beginman/tmp/%s.txt' % title, 'w')
    for obj in datas:
        titleLine = '================================================\n'
        fobj.write(titleLine)

        title = obj['title']+'\n'
        fobj.write(title)

        textStartLine = '--------------------------------------------------\n'
        fobj.write(textStartLine)

        text = obj['text']+'\n'
        fobj.write(text)

        textEndLine = '--------------------------------------------------\n'
        fobj.write(textEndLine)
    fobj.close()


def main():
    getRemoteUrl()

if __name__ == '__main__':
    main()
		
