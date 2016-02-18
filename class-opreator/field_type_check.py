# coding=utf-8
"""
数据模型的类型约束
ref: http://python3-cookbook.readthedocs.org/zh_CN/latest/c08/p13_implementing_data_model_or_type_system.html
ref: http://beginman.cn/python/2016/02/16/python-descriptor-guide/
使用描述器
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


class Typed(Base):
    """指定类型描述器类"""
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super(Typed, self).__set__(instance, value)


class Unsigned(Base):
    """无符号限制描述器类"""
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super(Unsigned, self).__set__(instance, value)


class MaxSized(Base):
    """大小限制描述器类"""
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super(MaxSized, self).__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super(MaxSized, self).__set__(instance, value)


class Integer(Typed):
    """整型"""
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    """无符号整型"""
    pass


class Float(Typed):
    """浮点型"""
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    """无符号浮点型"""
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    """长度限制的字符串"""
    pass


# 方式1：类级别定义
class Book(object):
    title = SizedString('title', size=20)
    star = UnsignedInteger('star')
    price = UnsignedFloat('price')

    def __init__(self, title, star, price):
        self.title = title
        self.star = star
        self.price = price

b = Book('Python cookbook', 4, 102.2)
# b.price = 10
# b.title = 'abcedfghijklm********************'
# b.star = -1000


# 方式2：使用类装饰器简化代码(推荐)
def check_attributes(**kwargs):
    def decorate(cls):
        for k, v in kwargs.items():
            if isinstance(v, Base):
                cls.name = k
                setattr(cls, k, v)
            else:
                setattr(cls, k, v[k])
        return cls
    return decorate


@check_attributes(
    title=SizedString('title', size=20),
    star=UnsignedInteger('star'),
    price=UnsignedFloat('price'))
class BBook(object):
    def __init__(self, title, star, price):
        self.title = title
        self.star = star
        self.price = price

bb = BBook('Redis In Action', 4, 76.0)
# bb.star = -1
print bb.star


