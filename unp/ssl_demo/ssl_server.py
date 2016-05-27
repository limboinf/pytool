# coding=utf-8
"""
Python SSL Server
ref:https://docs.python.org/2/library/ssl.html

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket
import ssl
import _ssl

# The Class `SSLContext`: Create a new SSL context with protocol
context = ssl.SSLContext(_ssl.PROTOCOL_TLSv1)       # ssl.PROTOCOL_TLSv1

# Load a private key and the corresponding certificate
# If keyfile is None, we need the third argument password
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

bindsocket = socket.socket()
bindsocket.bind(('127.0.0.1', 8899))
bindsocket.listen(5)


def do_something(connstream, data):
    print len(data)
    return True

def deal_with_client(connstream):
    data = connstream.recv(1024)
    print "receive data:", data
    while data:
        if not do_something(connstream, data):
            break

        connstream.send(b'b'*1024)
        data = connstream.recv(1024)

while 1:
    conn_socket, form_addr = bindsocket.accept()
    print(">>> Receive from:", form_addr)

    # Wrap an existing Python socket sock and return an SSLSocket object
    # sock must be a SOCK_STREAM socket; other socket types are unsupported.
    # Specifying server_hostname will raise a ValueError if server_side is true.
    conn_stream = context.wrap_socket(conn_socket, server_side=True)

    try:
        deal_with_client(conn_stream)
    finally:
        # conn_stream.shutdown(socket.SHUT_RDWR)      # Performs the SSL shutdown handshake
        conn_stream.close()