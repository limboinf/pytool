# coding=utf-8
"""
利用heapq模块实现一个优先级队列
关于heapq模块参考：https://github.com/qiwsir/algorithm/blob/master/heapq.md
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'
import heapq


class PriorityQueue:
    """
    堆数据结构最重要的特征是 heap[0] 永远是最小的元素。
    heapq.heappush(heap, item):将item压入到堆数组heap中
    heapq.heappop():从堆数组heap中取出最小的值，并返回。
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """使用负数，则最高级别的就放在head处"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)

    def getlist(self):
        return self._queue


p = PriorityQueue()
p.push('java', 3)
p.push('python', 5)
p.push('c', 2)
p.push('go', 10)

print p.getlist()       # [(-10, 3, 'go'), (-5, 1, 'python'), (-2, 2, 'c'), (-3, 0, 'java')]

print p.pop()           # (-10, 3, 'go')
print p.pop()           # (-5, 1, 'python')

print (-10, 3, 'go') < (-5, 1, 'python')        # True

