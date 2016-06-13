# coding=utf-8
"""
ref: http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
ref: http://beginman.cn/unp/2016/03/07/unix-socket-basic-api-summary/#ipv4

    -  inet_aton(string) -> packed 32-bit IP representation
    -  inet_ntoa(packed_ip) -> ip_address_string
    -  inet_ntop(af, packed_ip) -> string formatted IP address
    -  inet_pton(af, ip) -> packed IP address string

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket


def is_ipv4_address(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
    except AttributeError:              # no inet_pton here
        try:
            socket.inet_aton(addr)
        except socket.error:
            return False

        return addr.count('.') == 3
    except socket.error:                # not a valid address
        return False

    return True


def is_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True

if __name__ == '__main__':
    print is_ipv4_address('127.1')                              # False
    print is_ipv4_address('127.0.0.1')                          # True
    print is_ipv4_address('192.168.1.999')                      # False
    print is_ipv6_address("fe80::16dd:a9ff:fe7d:3de8")          # True
    print is_ipv6_address("0000::0000:0000:0000:0000")          # True
    print is_ipv6_address("000:xxxx:0000")                      # False


