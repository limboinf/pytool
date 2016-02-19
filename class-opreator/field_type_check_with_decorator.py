# coding=utf-8
"""
数据模型的类型约束-版本2：装饰器
比第一版本更加高效：
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '2/18/16'


class Base(object):
    """描述器类作为基类"""
    def __init__(self, name=None, **opt):
        self.name = name
        for k, v in opt.items():
            setattr(self, k, v)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def typed(expected_type):
    def wrapper(cls):
        super_set = cls.__set__

        def __set__(self, instance, value):
            if not isinstance(value, expected_type):
                raise TypeError('expected ' + str(expected_type))
            super_set(self, instance, value)

        cls.__set__ = __set__
        return cls
    return wrapper


def unsigned(cls):
    super_set = cls.__set__

    def __set__(self, ins, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, ins, value)

    cls.__set__ = __set__
    return cls


def max_size(cls):
    super_init = cls.__init__
    super_set = cls.__set__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)

    def __set__(self, ins, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, ins, value)

    cls.__init__ = __init__
    cls.__set__ = __set__
    return cls


@typed(int)
class Integer(Base): pass


@unsigned
class UnsignedInteger(Integer): pass


@typed(float)
class Float(Base): pass


@unsigned
class UnsignedFloat(Float): pass


@typed(str)
class String(Base): pass


@max_size
class SizedString(String): pass


class Book(object):
    title = SizedString(size=20)
    star = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, title, star, price):
        self.title = title
        self.star = star
        self.price = price

b = Book('Python cookbook', 4, 102.2)
# b.price = 10
# b.title = 'abcedfghijklm********************'
# b.star = -1000
