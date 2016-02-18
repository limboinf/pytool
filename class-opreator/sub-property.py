# coding=utf-8
"""
子类继承property.
ref: http://beginman.cn/python/2015/06/14/Python-oop/

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '2/15/16'


class Person(object):
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):

    @Person.name.setter
    def name(self, value):
        print ('setter')
        super(SubPerson, SubPerson).name.__set__(self, value)

s = SubPerson('Guido')
print s.name