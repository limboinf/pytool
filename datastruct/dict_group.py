# coding=utf-8
"""
字典分组的几种方式
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/4/15'

names = [{'first_name': u'Jack', 'last_name': u'MM'},
         {'first_name': u'Jack', 'last_name': u'Jone'},
         {'first_name': u'Frank', 'last_name': u'donne'},
         {'first_name': u'Jack', 'last_name': u'whiles'}]


def v1_simple():
    """simple"""
    dic = {}
    for n in names:
        if n['first_name'] not in dic:
            dic[n['first_name']] = []
        dic[n['first_name']].append(n['last_name'])

    print dic


def v2_setdefault():
    """dict.setdefault()"""
    dic = {}
    for n in names:
        dic.setdefault(n['first_name'], []).append(n['last_name'])
    print dic


def v3_defaultdict():
    """collection.defaultdict()
    ref:https://github.com/BeginMan/pythonStdlib/blob/master/collections.md#五defaultdict
    """
    import collections
    dic = collections.defaultdict(list)
    for n in names:
        dic[n['first_name']].append(n['last_name'])
    print dic


def v4_defaultdict_with_map():
    """map and list"""
    import collections
    dic = collections.defaultdict(list)
    map(lambda n: dic[n['first_name']].append(n['last_name']), names)
    # [dic[n['first_name']].append(n['last_name']) for n in names]
    print dic


if __name__ == '__main__':
    v4_defaultdict_with_map()