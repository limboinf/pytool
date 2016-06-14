# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket

HOST = 'localhost'


def echo_client(port, host=HOST):
    for result in socket.getaddrinfo(host,
                                     port,
                                     socket.AF_UNSPEC,
                                     socket.SOCK_STREAM,
                                     0,
                                     socket.AI_PASSIVE):

        family, socktype, proto, canonname, sockaddr = result
        try:
            sock = socket.socket(family, socktype, proto)
        except socket.error, err:
            print "Error,", err
            continue

        try:
            sock.connect(sockaddr)
        except socket.error, err:
            print sockaddr, err
            sock.close()
            continue

        if sock:
            try:
                print sockaddr, 'Send...'
                sock.send('Hello, World!')
                data = sock.recv(1024)
                print 'Received from server', repr(data)
            except socket.error,err:
                sock.close()
                print err

if __name__ == '__main__':
    echo_client(9900)
