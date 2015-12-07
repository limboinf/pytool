# coding=utf-8
"""
死锁是一个资源被多次调用，而多次调用方都未能释放该资源就会造成死锁，这里结合例子说明下两种常见的死锁情况。

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/6/15'

import threading
import time


class MyThread(threading.Thread):
    """
    该情况是一个线程“迭代”请求同一个资源，直接就会造成死锁：
    """
    def run(self):
        """
        在run函数的if判断中第一次请求资源，请求后还未 release ，再次acquire，最终无法释放，造成死锁
        """
        global num
        time.sleep(1)
        if mutex.acquire(1):
            num = num+1
            msg = self.name+' set num to '+str(num)
            print msg
            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0
mutex = threading.Lock()


def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()

    # 为了支持在同一线程中多次请求同一资源，python提供了“可重入锁”：threading.RLock。
    # RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。
    # 直到一个线程所有的acquire都被release，其他的线程才能获得资源。
    # 如上例如果使用RLock代替Lock，则不会发生死锁

