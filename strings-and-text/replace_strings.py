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


# 替换
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
# outputs: ['PYTHON', 'python', 'Python']
re.sub('python', 'snake', text, flags=re.IGNORECASE)
# outputs: 'UPPER snake, lower snake, Mixed snake'

# 一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小写保持一致。 为了修复这个，你可能需要一个辅助函数，就像下面的这样：


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
# outputs: 'UPPER SNAKE, lower snake, Mixed Snake'

# matchcase('snake') 返回了一个回调函数(参数必须是 match 对象)
# sub() 函数除了接受替换字符串外，还能接受一个回调函数。