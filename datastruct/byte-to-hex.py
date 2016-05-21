# coding=utf-8
"""
handle byte string and hex.

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import struct


def byte_string_to_hex(bstr):
    """
    Convenience method for converting a byte string to its hex representation
    `%02x` means print at least 2 digits, prepend it with 0's if there's less.

    pythond standlib:
    >>>import binascii
    >>>binascii.a2b_hex()

    ref:https://github.com/BeginMan/pythonStdlib/blob/master/binascii.md
    """
    if not isinstance(bstr, str):
        bstr = bstr.encode("utf-8")

    return ''.join(['%02x' % i for i in struct.unpack('%iB' % len(bstr), bstr)])


def byte_string_from_hex(hstr):
    """
    Convenience method for converting a byte string from its hex representation

    pythond standlib:
    >>>import binascii
    >>>binascii.b2a_hex()
    """
    byte_array = []

    # Make sure input string has an even number of hex characters
    # (2 hex chars = 1 byte). Add leading zero if needed.
    if len(hstr) % 2:
        hstr = '0' + hstr

    for obj in range(0,len(hstr), 2):
        byte = int(hstr[obj: obj+2], 16)
        byte_array.append(byte)
    return ''.join(struct.pack('%iB' % len(byte_array), *byte_array))

if __name__ == "__main__":
    s2 = u'中国'
    t = byte_string_to_hex(s2)
    print byte_string_from_hex(t)
    # In the same way, set `%x` to `%o` and set `int(xx, 16)` to `int(xx, 8)`
    # we can get methods to handle Octal