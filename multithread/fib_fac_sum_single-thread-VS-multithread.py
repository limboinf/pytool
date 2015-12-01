# coding=utf-8
"""
斐波那契，阶乘，累加 单线程 VS 多线程方式
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '11/29/15'

import threading
from time import ctime, sleep


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        print 'starting', self.name, ctime()
        self.res = apply(self.func, self.args)
        print 'end', self.name, ctime()

    def get_result(self):
        return self.res


def fib(x):
    """递归求斐波那契"""
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x-1))


def fac(x):
    """阶乘"""
    sleep(0.01)
    if x < 2: return 1
    return (x * fac(x-1))


def sum(x):
    """累加"""
    sleep(0.01)
    if x < 2: return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 15

def main():
    nfuncs = range(len(funcs))

    print '*** 单线程方式'
    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'at:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'end at', ctime()

    print '*** 多线程方式'
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n, ), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print threads[i].get_result()

if __name__ == '__main__':
    main()