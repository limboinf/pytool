# coding=utf-8
"""
创建临时文件和文件夹
使用tempfile模块

>>>def TemporaryFile(mode='w+b', bufsize=-1, suffix="", prefix=template, dir=None):
    '''Create and return a temporary file.
    Arguments:
    'prefix', 'suffix', 'dir' -- as for mkstemp.
    'mode' -- the mode argument to os.fdopen (default "w+b").
    'bufsize' -- the buffer size argument to os.fdopen (default -1).
    The file is created as mkstemp() would do it.

    Returns an object with a file-like interface.  The file has no
    name, and will cease to exist when it is closed.
    '''

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/13/16'

from tempfile import TemporaryFile, NamedTemporaryFile

# 创建匿名的临时文件
with TemporaryFile('w+t',) as f:     # 文本模式, w+t 同时支持读和写
    f.write('hello\n')
    f.write('world')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print data


# 可使用`NamedTemporaryFile`创建有名临时文件
# 当你需要将文件名传递给其他代码来打开这个文件的时候，这个就很有用了
with NamedTemporaryFile('w+t', delete=True) as f:
    print 'name', f.name            # name /var/folders/jv/kxcwkrmx4hzfhtcb51mcwl3w0000gn/T/tmpuzb4Rr
    f.write('hello\n')
    f.write('world')
    f.seek(0)
    data = f.read()
    print data

# 创建临时目录 TemporaryDirectory

# or

"""
>>> f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
>>> f.name
'/tmp/mytemp8ee899.txt'
"""