#!/usr/bin/env python
# coding=utf-8
import time

class Timer(object):
    def __init__(self, verbose=True):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.times = (self.end - self.start)*1000
        if self.verbose:
            print u"程序运行时间为:%s" % self.times

def testTime():
    return [i for i in range(10000) if i%2 == 0]

with Timer() as t:
    testTime()
