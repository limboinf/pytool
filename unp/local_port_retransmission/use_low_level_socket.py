# coding=utf-8
"""
Usage:

    python use_low_level_socket.py host

Example:

    python use_low_level_socket.py www.jianshu.com

Then open the browser to input localhost:8080, you will see the specified host web pages

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket
import sys

BUFFER_SIZE = 4096


def server(remote_addr):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 8080))
    sock.listen(5)

    while True:
        try:
            conn, addr = sock.accept()
            print "Contented:", addr
            datas = conn.recv(BUFFER_SIZE)
            requests = datas.replace('Host: 127.0.0.1:8080', 'Host: %s' % remote_addr).\
                replace('Host: localhost:8080', 'Host: %s' % remote_addr)
            print requests
            print '*' * 40
        except Exception as ex:
            print ex
            break

        try:
            remote_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_sock.connect((remote_addr, 80))
            print "Connected remote addr:", remote_addr
            remote_sock.send(requests)
        except socket.error, e:
            print e
            break

        while True:
            print '.......'
            try:
                response = remote_sock.recv(BUFFER_SIZE)
            except socket.error, e:
                print e
                break
            if not response:
                print "no more data"
                break
            else:
                try:
                    conn.sendall(response)
                except socket.error, e:
                    print e
                    break

        remote_sock.close()
        conn.close()

if __name__ == '__main__':
    server(sys.argv[1])