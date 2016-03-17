# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket

msgs = ["Python", "C/C++", "Golang"]
server_addr = ("127.0.0.1", 12345)

socks = []
for i in range(10):
    socks.append(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    )

for s in socks:
    s.connect(server_addr)

counter = 0
for msg in msgs:
    for s in socks:
        counter += 1
        print "%s sending %s :counter:%d" % (s.getpeername(), msg, counter)
        s.send(msg + ":version:" + str(counter))

    for s in socks:
        data = s.recv(1024)
        print " %s received %s" % (s.getpeername(),data)
        if not data:
            print "closing socket ",s.getpeername()
            s.close()
