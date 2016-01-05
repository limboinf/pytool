# coding=utf-8
"""
字符串搜索与替换
string.replace VS re.sub

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/5/16'

print 'world.hello, world'.replace('world', 'beginman', 1)   # beginman.hello, world
print 'world.hello, world'.replace('world', 'beginman')      # beginman.hello, beginman


# 复杂的模式使用re模块中的sub()
import re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)       # Today is 2012-11-27. PyCon starts 2013-3-13.

# 反斜杠数字比如 \3 指向前面模式的捕获组号。

# 对于更加复杂的替换，可以传递一个替换回调函数来代替，比如：

from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print datepat.sub(change_date, text)        # Today is 27 Nov 2012. PyCon starts 13 Mar 2013.
