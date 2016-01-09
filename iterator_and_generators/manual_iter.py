# coding=utf-8
"""
不用forloop,而是手动的遍历可迭代对象
则可以使用 next() 函数并在代码中捕获 StopIteration 异常
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/9/16'


def manual_iter():
    with open('__init__.py') as f:
        while 1:
            try:
                # line = f.next()           # f.next() 是_io库_IOBase类方法,同内建next()函数一样
                line = next(f)              # 内建函数 next(iterator[, default])
                print line
            except StopIteration:           # StopIteration 用来指示迭代的结尾
                break

manual_iter()