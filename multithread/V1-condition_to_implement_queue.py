# coding=utf-8
"""
展示Condition，wait()和notify()来实现Queue模块

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/2/15'

from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()


class ProducerThread(Thread):
    """
    在加入数据前，生产者检查队列是否为满。
    如果不为满，生产者可以继续正常流程。
    如果为满，生产者必须等待，调用condition实例的wait()。
    消费者可以运行。消费者消耗队列，并产生一个空余位置。
    然后消费者notify生产者。
    当消费者释放lock，生产者可以acquire这个lock然后往队列中加入数据。
    """
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print "Queue full, producer is waiting"
                condition.wait()
                print "Space in queue, Consumer notified the producer"

            num = random.choice(nums)
            queue.append(num)
            print "Produced", num
            condition.notify()

            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    """
    对于消费者，在消费前检查队列是否为空。
    如果为空，调用condition实例的wait()方法。
    消费者进入wait()，同时释放所持有的lock。
    除非被notify，否则它不会运行。
    生产者可以acquire这个lock，因为它已经被消费者release。
    当调用了condition的notify()方法后，消费者被唤醒，但唤醒不意味着它可以开始运行。
    notify()并不释放lock，调用notify()后，lock依然被生产者所持有。
    生产者通过condition.release()显式释放lock。
    消费者再次开始运行，现在它可以得到队列中的数据而不会出现IndexError异常。
    """
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
                print "Producer added something to queue and notified the consumer"

            num = queue.pop(0)
            print "Consumed", num
            condition.notify()

            condition.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()