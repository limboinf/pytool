#!/usr/bin/env python
# -*- coding: UTF-8 -*-

print "Content-type:text/html"      # "Content-type:text/html" 发送到浏览器并告知浏览器显示的内容类型为"text/html"。
print                               # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello Word - 我的第一个 CGI 程序！</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word!</h2>'
print '</body>'
print '</html>'
