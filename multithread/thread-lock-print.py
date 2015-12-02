# coding=utf-8
__author__ = 'fang'

import threading
import time

lock = threading.Lock()

class CreateListThread(threading.Thread):
    """
    当一个线程正在打印的时候，cpu切换到了另一个线程，所以产生了不正确的结果。
    我们需要确保print是个逻辑上的原子操作，以防打印时被其他线程打断。
    """
    def run(self):
        self.lis = []
        for i in range(10):
            time.sleep(1)       # time.sleep()可以使一个线程挂起，强制线程切换发生。
            self.lis.append(i)

        with lock:              # 防止竞态打印
            print self.lis


def use_create_list_thread():
    for i in range(3):
        t = CreateListThread()
        t.start()


if __name__ == '__main__':
    use_create_list_thread()
