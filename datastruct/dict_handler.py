#coding=utf-8
'''
对字典对象的操作
'''

class DictWrapper(dict):
    """一个字典，允许对象属性访问语法"""
    def __getattr__(self, name):
        try:
            value = self[name]
            if isinstance(value, dict) and not isinstance(value, DictWrapper):
                value = self[name] = DictWrapper(value)
            print 'get attr'
            return value
        except KeyError:
            print 'arise exception'
            raise AttributeError(name)

    def __setattr__(self, key, value):
        try:
            self[key] = value
            print 'set it'
        except KeyError:
            raise AttributeError(key)


def object2dict(obj):
    #object转换为字典对象
    d = {}
    d.update(obj.__dict__)
    return d



class Obj2DictTest(object):
    def __init__(self):
        self.name = 'fang'
        self.age = 24

if __name__ == '__main__':
    dic = {'name':'fang', 'age':24}
    dic = DictWrapper(dic)
    print dic.name
    dic.email='xinxinyu2011@163.com'
    print dic
    print type(dic)
    print '-'*40
    #object转换为字典
    #print dict(dic)     # 转换为dict
    print dic.__dict__      # {}
    print object2dict(dic), type(object2dict(dic)) # {}, <type 'dict'>

    obj = Obj2DictTest()
    print obj.__dict__     # {'age': 24, 'name': 'fang'}
    print object2dict(obj) # {'age': 24, 'name': 'fang'}

