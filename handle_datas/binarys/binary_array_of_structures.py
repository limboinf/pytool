# coding=utf-8
"""
二进制数组的读写
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/12/16'
from struct import Struct


def tuple_to_bin_file(records, format, f):
    """元组写入二进制文件中

    使用 struct 模块处理二进制数据,每个元组编码为一个结构体,写入一个二进制文件内
    Args:
        records: 元组对象
        format: struct格式化字符串
        f:  file object.
    Returns:
        None
    Raises:

    """
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def bin_file_to_tuple(format, f):
    """二进制文件转换元组

    以块的形式增量读取文件，使用`iter()`来处理，通过 struct format转换
    iter被用来创建一个返回固定大小数据块的迭代器,这个迭代器会不断的调用一个用户提供的可调用对象
    Example:

        lambda: f.read(record_struct.size) )

    直到它返回一个特殊的值(如b’‘)，这时候迭代停止。

    Args:
        format: struct格式字符串
        f:  file object.
    Returns:
        generator object.
    """
    struct_it = Struct(format)
    chunks = iter(lambda: f.read(struct_it.size), b'')
    return (struct_it.unpack(chunk) for chunk in chunks)


if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    # with open('data.b', 'wb') as f:
    #     tuple_to_bin_file(records, '<idd', f)

    with open('data.b', 'rb') as f:
        # for rec in bin_file_to_tuple('<idd', f):
        #     print rec
        data = f.read()
        struct_it = Struct('<idd')
        for offset in range(0, len(data), struct_it.size):
            print struct_it.unpack_from(data, offset)
