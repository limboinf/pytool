# coding=utf-8
__author__ = 'fang'
import threading
import time
import sys

class threadTest(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        # 开始开启一个进程
        print '%s delay for %s\n' % (self.name, self.delay)
        time.sleep(self.delay)
        c = 0
        while 1:
            print 'This is thread %s on line %s' % (self.name, c)
            c += 1
            if c == 3:
                print 'End of thread %s' % self.name
                break


t1 = threadTest('thread1', 2)
t2 = threadTest('thread2', 2)
t1.start()
print 'Main Thread: Wait t1 to end\n'  # 主线程
t1.join()
t2.start()
print 'End of main\n'


