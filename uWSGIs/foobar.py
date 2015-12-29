# coding=utf-8
"""
uWSGI demo
ref:http://uwsgi-docs-cn.readthedocs.org/zh_CN/latest/WSGIquickstart.html
base on  Python 2.x
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/28/15'


def application(env, start_response):
    """
     “application”，这是默认的函数名
     uWSGI的Python加载器将会搜索这个名字(但你当然可以修改它)。
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello, world"]

