# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/28/16'


def apply_async(func, args, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print 'go:%s' % result


def add(x, y):
    return x + y

apply_async(add, (10, 20), print_result)


class ResultHandler(object):
    def __init__(self):
        self.count = 0

    def handler(self, result):
        self.count += 1
        print self.count, result

r = ResultHandler()
apply_async(add, (10, 20), r.handler)
apply_async(add, ('hello', 'world'), r.handler)


point = 0
def make_handler():
    count = []
    # point = 0
    def handler(result):
        # nonlocal point            # python 3.x
        global point
        point += 1
        count.append(result)
        print point, count, result
    return handler

m = make_handler()
apply_async(add, (100, 1), m)
apply_async(add, (100, 2), m)


# 协程
def yield_make_handler():
    seq = 0
    while 1:
        result = yield
        seq += 1
        print('[{}] Got: {}'.format(seq, result))

handler = yield_make_handler()

# 先next()，否则 TypeError: can't send non-None value to a just-started generator
# 不next也行，可以用 handler.send(None)来替代
next(handler)

# 协程使用send方法做回调
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)