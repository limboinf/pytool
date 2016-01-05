# coding=utf-8
"""
使用多个界定符分割字符串
string.split Vs re.split

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/5/16'


line = 'asdf fjdk; afed, fjek,asdf, foo'


def string_split():
    return line.split(',')      # string.split()只能分隔简单的字符串,不能有多个分隔符


def re_split():
    import re
    return re.split(r'[;,\s]\s*', line)    # 使用正则更加灵活的切割字符串


print string_split()
print re_split()        # outputs: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
