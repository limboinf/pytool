#!/usr/bin/env python
# encoding: utf-8

from threading import Thread
import time
import dis


def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    s = time.time()
    COUNT = 100000000       # 100 million
    # countdown(COUNT)        # use time 5.29941797256
    print dis.dis(countdown)
    # t1 = Thread(target=countdown, args=(COUNT//2, ))
    # t2 = Thread(target=countdown, args=(COUNT//2, ))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # use time 6.96924901009
    print 'use time', time.time() - s