# coding=utf-8
"""
字符串开头或结尾匹配

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/5/16'

# 方式1.endwiths(), startswith()

# 方式2.切片

# 方式3.正则


import os
path = os.path.dirname(__file__)


def method_1():
    if any((name.endswith(('.py', '.md')) for name in os.listdir(path))):
        print 'py'


def method_2():
    if any((name[-3:] in ('.py', '.md') for name in os.listdir(path))):
        print 'py'


def method_3():
    import re
    if any((re.search(r'.py|md$', name) for name in os.listdir(path))):
        print 'py'

