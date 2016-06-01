# coding=utf-8
"""
Usage:

    python use_asyncore.py host

Example:

    python use_asyncore.py www.baidu.com

Then open the browser to input localhost:8080, you will see the specified host web pages

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import asyncore
import socket
import sys

LOCAL_HOST = 'localhost'
BUFSIZE = 4096


class PortForwarder(asyncore.dispatcher):
    def __init__(self, ip, port, remote_addr, remote_port, backlog=5):
        asyncore.dispatcher.__init__(self)
        self.remote_addr = remote_addr
        self.remote_port = remote_port
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip, port))
        self.listen(backlog)

    def handle_accept(self):
        conn, addr = self.accept()
        print "Connected to:", addr
        Sender(Receiver(conn, self.remote_addr), self.remote_addr, self.remote_port)


class Receiver(asyncore.dispatcher):
    def __init__(self, conn, remote_addr):
        asyncore.dispatcher.__init__(self, conn)
        self.remote_addr = remote_addr
        self.from_remote_buffer = ''
        self.to_remote_buffer = ''
        self.sender = None              # Sender object

    def handle_connect(self):
        pass

    def handle_read(self):
        self.from_remote_buffer += self.recv(BUFSIZE)
        self.from_remote_buffer = self.from_remote_buffer.replace('Host: 127.0.0.1:8080', 'Host: %s' % self.remote_addr)
        print "Receive request:\n", self.from_remote_buffer

    def writable(self):
        return len(self.to_remote_buffer) > 0

    def handle_write(self):
        sent = self.send(self.to_remote_buffer)
        self.to_remote_buffer = self.to_remote_buffer[sent:]
        print "Receiver, Write:", sent

    def handle_close(self):
        self.close()
        if self.sender:
            self.sender.close()


class Sender(asyncore.dispatcher):
    def __init__(self, reveiver, remote_addr, remote_port):
        asyncore.dispatcher.__init__(self)
        self.remote_addr = remote_addr
        self.reveiver = reveiver        # Reveiver object
        reveiver.sender = self
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((remote_addr, remote_port))
        print "Connected remote addr:", remote_addr

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(BUFSIZE)
        self.reveiver.to_remote_buffer += read
        if len(read):
            print "Sender,Read:", self.reveiver.to_remote_buffer

    def writable(self):
        return len(self.reveiver.from_remote_buffer) > 0

    def handle_write(self):
        send = self.send(self.reveiver.from_remote_buffer)
        self.reveiver.from_remote_buffer = self.reveiver.from_remote_buffer[send:]
        print "Sender,Retransmission:", self.remote_addr

    def handle_close(self):
        self.close()
        self.reveiver.close()


PortForwarder(LOCAL_HOST, 8080, sys.argv[1], 80)
asyncore.loop()
