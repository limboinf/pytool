# coding=utf-8
"""
设计模式之单例模式：
Python单例模式的4种实现方法：http://blog.csdn.net/ghostfromheaven/article/details/7671853

"""
__author__ = 'fang'
import threading

#v1.0.0
class SingletonBasic(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        """保证只有一个实例,但是在并发的情况下可能出错"""
        if cls._instance is None:
            cls._instance = super(SingletonBasic, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance


#v1.0.1
class SingleLock(object):
    """经典双检查锁机制创建实例"""
    objs = {}
    objs_locker = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]

        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:             # 防止并发生成则要再检查一遍
                return cls.objs[cls]

            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()

        return cls.objs[cls]


#v1.0.2
#模块是最佳的单例模式实践产品，它使用变量都绑定到模块中，且只初始化一次，线程安全(并发下实例唯一)

#Test for v1.0.1
class SubSingleLock(SingleLock):
    """重载SingleLock类并覆盖__new__()和__init__()"""
    def __new__(cls, *args, **kwargs):
        super(SubSingleLock, cls).__new__(cls, *args, **kwargs)     # 如果重写父类__new__()则可行
        # return object.__new__(cls)            # 不调用父类的__new__()而是直接覆盖


if __name__ == '__main__':
    # s1 = SingletonBasic()
    # s2 = SingletonBasic()
    # assert id(s1) == id(s2)
    # print s1 == s2

    # s1 = SingleLock()
    # s2 = SingleLock()
    # # assert id(s1) == id(s2)
    # print id(s1), s1, id(s2), s2

    s1 = SubSingleLock()
    s2 = SubSingleLock()
    assert id(s1) == id(s2)