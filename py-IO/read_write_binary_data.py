# coding=utf-8
"""

在Python3.x中 print改进了很多，且字节字符串和文本字符串还不一样,索引和迭代动作返回的是字节的值而不是字节字符串.
eg:
    # Python 2.x
    for i in b'hello':
        print i,

    # outputs:h,e,l,l,o

    # Python 3.x
    for i in b'hello':
        print(i)

    # outputs:
    72
    101
    ...

如果你想从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码操作。比如：

    with open('somefile.bin', 'wb') as f:
        text = b'Hello World'
        f.write(text.encode('utf-8'))

    with open('somefile.bin', 'rb') as f:
        data = f.read(16)
        text = data.decode('utf-8')

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/12/16'

# 二进制I/O可以将数组和C结构体类型能直接被写入，而不需要中间转换为自己对象。比如：
import array
nums = array.array('i', [1, 2, 3, 4])
print nums
with open('somefile.bin','wb') as f:
    f.write(nums)
