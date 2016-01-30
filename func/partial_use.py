# coding=utf-8
"""
偏函数
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/28/16'
import logging
from functools import partial
from multiprocessing import Pool


def output_result(result, log=None):
    if log is not None:
        log.debug('got:%r', result)


def add(x, y):
    return x + y


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()