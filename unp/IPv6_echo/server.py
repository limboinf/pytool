# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket
import os
import sys

HOST = 'localhost'

sockets = []        # IPv4 socket和 IPv6 socket


def echo_server(port, host=HOST):
    for result in socket.getaddrinfo(host,
                                     port,
                                     socket.AF_UNSPEC,      # family
                                     socket.SOCK_STREAM,    # socktype
                                     0,                     # proto
                                     socket.AI_PASSIVE):    # flags
        # return list of (family, socktype, proto, canonname, sockaddr)
        family, socktype, proto, canonname, sockaddr = result
        try:
            sock = socket.socket(family, socktype, proto)
        except socket.error, err:
            print "Error: %s" % err
            continue

        try:
            sock.bind(sockaddr)
            sock.listen(1)
            print "Server lisenting on %s:%s" % (host, port)
        except socket.error:
            sock.close()
            continue

        sockets.append({str(sockaddr): sock})

    print len(sockets)

    for item in sockets:
        sa, sock = item.items()[0]
        pid = os.fork()
        if pid == 0:
            print 'sockaddr,', sa
            conn, addr = sock.accept()
            print 'Connected to', addr
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                print "Received data from the client: [%s]" % data
                conn.send(data)
                print "Sent data echoed back to the client: [%s]" %data

            conn.close()
            sys.exit(1)

if __name__ == '__main__':
    echo_server(9900)