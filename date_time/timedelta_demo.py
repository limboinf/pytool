# coding=utf-8
"""
datetime.timedelta对象是两个时间之间的时间差，两个date或datetime对象相减时可以返回一个timedelta对象。

构造函数：

    class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])

所有参数可选，且默认都是0，参数的值可以是整数，浮点数，正数或负数。

内部只存储days，seconds，microseconds，其他参数的值会自动按如下规则抓转换：

1 millisecond（毫秒） 转换成 1000 microseconds（微秒）
1 minute 转换成 60 seconds
1 hour 转换成 3600 seconds
1 week转换成 7 days

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '12/18/15'

import datetime


def timebefore(d):
    """
    N分钟，N小时，N天..前
    @:param d: 可以为日期时间对象，日期时间字符串，时间戳
    """
    chunks = (
               (60 * 60 * 24 * 365, u'年'),
               (60 * 60 * 24 * 30, u'月'),
               (60 * 60 * 24 * 7, u'周'),
               (60 * 60 * 24, u'天'),
               (60 * 60, u'小时'),
               (60, u'分钟'),
    )

    try:
        if isinstance(d, (str, unicode)):
            if d.isdigit():
                d = datetime.datetime.fromtimestamp(int(d))
            else:
                d = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")

        if isinstance(d, int):
            d = datetime.datetime.fromtimestamp(int(d))
    except:
        raise ValueError

    now = datetime.datetime.now()
    delta = now - d
    before = delta.total_seconds()      # 计算秒数 等于(td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
    if before <= 60:        # 1min内
        return u'刚刚'

    for seconds, unit in chunks:
        count = before // seconds
        if count != 0:
            break

    return unicode(int(count)) + unit + u'前'

if __name__ == '__main__':
    d = '2015-12-18 17:10:59'       # 日期时间字符串
    n = datetime.datetime.now()     # 日期时间对象
    t = 1450410236                  # 时间戳

    print timebefore(d)             # 20分钟前
    print timebefore(n)             # 刚刚
    print timebefore(t)             # 5小时前