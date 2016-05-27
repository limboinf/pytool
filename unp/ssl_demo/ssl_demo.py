# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket
import ssl
from pprint import pprint

HOSTNAME = "www.python.org"

context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_verify_locations("cert.pem")
conn = context.wrap_socket(socket.socket(), server_hostname=HOSTNAME)
conn.connect((HOSTNAME, 443))
cert = conn.getpeercert()

pprint(cert)