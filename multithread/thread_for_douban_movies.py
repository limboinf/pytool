# coding=utf-8
"""
多线程爬豆瓣电影TOP250
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '11/29/15'

import urllib2
import re
import Queue
import threading
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

_DATA = []
FILE_LOCK = threading.Lock()    # Lock
SHARE_Q = Queue.Queue()         # 构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 4          # 设置线程的个数


class Mythread(threading.Thread):
    def __init__(self, func, thread_name=''):
        super(Mythread, self).__init__(name=thread_name)
        self.func = func        # 传入线程函数逻辑

    def run(self):
        self.func()


def wroker():
    global SHARE_Q
    while not SHARE_Q.empty():
        url = SHARE_Q.get()
        page = get_page(url)
        find_title(page)        # 获得当前页面的电影名
        time.sleep(1)
        SHARE_Q.task_done()


def get_page(url):
    try:
        page = urllib2.urlopen(url).read().decode('utf-8')
        return page
    except urllib2.URLError, e:
        pass


def find_title(page):
    temp_data = []
    movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', page, re.S)
    for index, item in enumerate(movie_items) :
        if item.find("&nbsp") == -1:
            temp_data.append(item)
    _DATA.append(temp_data)



def main():
    global SHARE_Q
    threads = []
    douban_url = "http://movie.douban.com/top250?start={page}&filter=&type="
    for index in range(10):
        SHARE_Q.put(douban_url.format(page=index * 25))

    for i in range(_WORKER_THREAD_NUM):
        t = Mythread(wroker, str(i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join(3)

    # 等待所有任务完成
    SHARE_Q.join()

    with open("movie.txt", "w+") as my_file :
        for page in _DATA :
            for movie_name in page:
                my_file.write(movie_name + "\n")

    print "Spider Successful!!!"

if __name__ == '__main__':
    s = time.time()
    main()
    print 'use time:', time.time() - s



