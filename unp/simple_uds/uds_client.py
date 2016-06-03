# coding=utf-8
"""
Unix domain socket client
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket
import sys

BUFFER_SIZE = 10

server_address = './uds_socket'


def client_send():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    print "connecting to %s" % server_address
    try:
        sock.connect(server_address)
    except socket.error, (errno, msg):
        print "connection error, errno:%d, msg:%s" % (errno, msg)
        sys.exit(1)

    try:
        msg = sys.argv[1]
        print "Send:", msg
        sock.sendall(msg)

        amount_received = 0
        amount_expected = len(msg)

        while amount_received < amount_expected:
            data = sock.recv(BUFFER_SIZE)
            amount_received += len(data)
            print 'received "%s"' % data
    finally:
        sock.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        client_send()
    else:
        print "Usage: python %s msg" % sys.argv[0]