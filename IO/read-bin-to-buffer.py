# coding=utf-8
"""
读取二进制数据到可变缓冲区
ref:http://python3-cookbook.readthedocs.org/zh_CN/latest/c05/p09_read_binary_data_into_mutable_buffer.html
1. 预先分配内存， bytearray(size)
2. 二进制文件读入预先分配的buffer中
3. 无需中间介入处理，可直接操作缓冲区中二进制数据，可原地修改数据并将它写回到一个文件中去。

这些需要文件对象的`readinto()`方法
用于填充已存在的缓冲区而不是为新对象重新分配内存再返回它们。
因此，你可以使用它来避免大量的内存分配操作。

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/13/16'

import os.path


def read_to_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        print f.readinto(buf)           # 返回
    return buf

with open('test.bin', 'wb') as f:
    f.write(b'hello, world')

buf = read_to_buffer('test.bin')
print buf
buf[0:5] = b'Hallo'
print buf

with open('new.bin', 'wb') as f:
    f.write(buf)

# outputs:

# hello, world
# Hallo, world

record_size = 32        # Size of each record
buf = bytearray(record_size)
with open('somefile', 'wb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the contents of buf

