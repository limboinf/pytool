# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/6/16'


def sample():
    yield 'I'
    yield 'Love'
    yield 'You'


print ' '.join(sample())    # outputs: I Love You
