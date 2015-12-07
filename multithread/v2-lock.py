# coding=utf-8
"""
死锁的另一种情况：互相调用死锁
如下两个函数中都会调用相同的资源，互相等待对方结束的情况。
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/6/15'
import threading
import time


class MyThread(threading.Thread):
    def func1(self):
        if mutex1.acquire():
            print 'func1 mutex1 acquire'
            if mutex2.acquire():
                print 'func1 mutex2 acquire'
                time.sleep(1)
                mutex2.release()
            mutex1.release()

    def func2(self):
        if mutex2.acquire():
            print 'func2 mutex2 acquire'
            if mutex1.acquire():
                print 'func2 mutex1 acquire'
                time.sleep(1)
                mutex1.release()
            mutex2.release()

    def run(self):
        self.func1()
        self.func2()

mutex1 = threading.Lock()
mutex2 = threading.Lock()


t1 = MyThread()
t2 = MyThread()

t1.start()
t2.start()

