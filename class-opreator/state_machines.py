# coding=utf-8
"""
Python状态模式，实现状态机

如果代码中出现太多的条件判断语句的话，代码就会变得难以维护和阅读。
这里的解决方案是`将每个状态抽取出来定义成一个类`。

ref:http://python3-cookbook.readthedocs.org/zh_CN/latest/c08/p19_implements_stateful_objects_or_state_machines.html
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '2/22/16'


class Connection(object):
    def __init__(self):
        self.new_state(ClosedConnectionState)   # 为每个状态定义一个类

    # 代理状态类
    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState(object):
    @staticmethod
    def read(conn):
        raise NotImplementedError()     # 确保子类实现了相应的方法

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError("Not open")

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


c = Connection()
print c._state
# c.read()
c.open()
c.read()
# c.open()
c.close()