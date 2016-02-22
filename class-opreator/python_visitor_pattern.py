# coding=utf-8
"""
Python访问者模式

应用场景：处理大量不同类型的对象组成的复杂数据结构，每个对象进行不同的处理
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '2/22/16'


class Wheel:
    def __init__(self,name):
        self.name = name

    def accept(self, visitor):
        """定义accept方法，回调访问者的visit方法"""
        visitor.visitWheel(self)


class Engine:
     def accept(self, visitor):
         visitor.visitEngine(self)


class Body:
     def accept(self, visitor):
         visitor.visitBody(self)


class Car:
     def __init__(self):
         self.engine = Engine()
         self.body   = Body()
         self.wheels = [ Wheel("front left"), Wheel("front right"),
                         Wheel("back left") , Wheel("back right") ]

     def accept(self, visitor):
         """在对象结构的一次访问过程中，我们遍历整个对象结构，
         对每一个元素都实施accept方法，在每一个元素的accept方法中回调访问者的visit方法，
         从而使访问者得以处理对象结构的每一个元素。"""
         visitor.visitCar(self)
         self.engine.accept(visitor)
         self.body.accept(visitor)
         for wheel in self.wheels:
             wheel.accept(visitor)


class PrintVisitor:
    """
    访问者类
    访问者是一个接口，它拥有一个visit方法
    这个方法对访问到的对象结构中不同类型的元素作出不同的反应；"""
    def visitWheel(self, wheel):
         print "Visiting "+wheel.name+" wheel"

    def visitEngine(self, engine):
         print "Visiting engine"

    def visitBody(self,body):
         print "Visiting body"

    def visitCar(self,car):
         print "Visiting car"

car = Car()
visitor = PrintVisitor()
car.accept(visitor)
