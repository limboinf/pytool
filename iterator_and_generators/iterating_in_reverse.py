# coding=utf-8
"""
自定义一个高效的反向迭代
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/9/16'


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        x = self.start
        while x > 0:
            yield x
            x -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(5)):
    print(rr)

for rr in Countdown(5):
    print(rr)

