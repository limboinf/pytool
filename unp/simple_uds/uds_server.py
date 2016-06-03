# coding=utf-8
"""
Unix domain socket server

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import os
import socket

BUFFER_SIZE = 10

server_address = './uds_socket'

# Make sure the socket does not already exist
try:
    # unlink: Remove a file (same as remove(path)).
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print 'starting up on %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print 'waiting for a connection..............\n'
    conn, client_address = sock.accept()
    try:
        print "connection from", client_address
        while True:
            data = conn.recv(BUFFER_SIZE)
            if data:
                print "received data", data
                conn.sendall(data)
            else:
                print "no more data from"
                break
    finally:
        conn.close()

