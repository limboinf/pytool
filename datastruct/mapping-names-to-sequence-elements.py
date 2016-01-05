# coding=utf-8
"""
映射名称到序列元素

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/5/16'

from collections import namedtuple

My = namedtuple('My', ('address', 'birthday'))
my = My(u'北京市天通苑', '91/2/19')
print my.address
print my.birthday

# namedtuple实例支持所有的普通元组操作，比如索引和解压
print len(my)
a, b = my
print b

n = my._replace(address='USA')
print n
# import MySQLdb
# conn = MySQLdb.Connect(host='192.168.0.120', user='root', passwd='!qaz2wsx', db='yOpreate')
# cursor = conn.cursor()
# cursor.execute("select * from user")
# data = cursor.fetchall()
# print data
# conn.close()