# coding=utf-8
"""
单线程VS多线程
在IO密集型业务中可以看出多线程优势挺大的
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '11/29/15'

import urllib2
import time
import threading


urls = [
        'http://www.baidu.com',
        'http://www.github.com',
        'http://www.weibo.com',
        'http://www.zhihu.com',
        'http://www.google.com'
    ]


def get_response():
    """单线程

    1.url顺序的被请求
    2.除非cpu从一个url获得了回应，否则不会去请求下一个url
    3.网络请求会花费较长的时间，所以cpu在等待网络请求的返回时间内一直处于闲置状态。
    """
    start = time.time()
    for url in urls:
        print url
        try:
            res = urllib2.urlopen(url, timeout=10)
            print res.getcode()
        except urllib2.URLError, e:
            print 'err', e

    print "Elapsed time: %s" % (time.time()-start)  # Elapsed time: 25.9800038338


class GetUrlThread(threading.Thread):
    """
    多线程

    1.意识到了程序在执行时间上的提升
    2.我们写了一个多线程程序来减少cpu的等待时间，当我们在等待一个线程内的网络请求返回时，这时cpu可以切换到其他线程去进行其他线程内的网络请求。
    3.我们期望一个线程处理一个url，所以实例化线程类的时候我们传了一个url。
    4.线程运行意味着执行类里的run()方法。
    5.为每个url创建一个线程并且调用start()方法，这告诉了cpu可以执行线程中的run()方法了。
    6.我们希望所有的线程执行完毕的时候再计算花费的时间，所以调用了join()方法。
    7.join()可以通知主线程等待这个线程结束后，才可以执行下一条指令。
    8.每个线程我们都调用了join()方法，所以我们是在所有线程执行完毕后计算的运行时间。
    9.cpu可能不会在调用start()后马上执行run()方法。
    10.你不能确定run()在不同线程建间的执行顺序。
    """
    def __init__(self, url):
        super(GetUrlThread, self).__init__()
        self.url = url

    def run(self):
        try:
            res = urllib2.urlopen(self.url, timeout=10)
            print self.url, res.getcode()
        except urllib2.URLError, e:
            print 'err', e


def start_with_thread():
    """多线程方式"""
    start = time.time()
    threads = []
    for i in urls:
        t = GetUrlThread(i)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time() - start)        # Elapsed time: 10.3441879749


if __name__ == '__main__':
    start_with_thread()
    # get_response()