# coding=utf-8
# 对datetime,date类型序列化
__author__ = 'fang'
from datetime import datetime, date
try:
    import simplejson as json
except ImportError:
    import json

# 方式1
def jsonTimeDefault(obj):
    """
    >>> data = json.dumps(datetime.now(), default=jsonTimeDefault)
    """
    print obj, type(obj)
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


# 方式2：重写JSONEncoder类,此类负责编码，主要是通过其default函数进行转化
class DateTimeEncoder(json.JSONEncoder):
    """
    >>> data = json.dumps(datetime.now(), cls=DateTimeEncoder)
    """
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')

        return json.JSONEncoder.default(self, o)
