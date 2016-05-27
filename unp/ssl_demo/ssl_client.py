# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket
import ssl
from pprint import pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# or:
# ssl_sock = ssl.wrap_socket(s,
#                            ca_certs='cert.pem',
#                            cert_reqs=ssl.CERT_REQUIRED)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

# Whether to try to verify other peers’ certificates and how to behave if verification fails.
# This attribute must be one of CERT_NONE, CERT_OPTIONAL or CERT_REQUIRED.
context.verify_mode = ssl.CERT_REQUIRED

# Wether to match the peer cert’s hostname with `match_hostname()` in `SSLSocket.do_handshake()`.
context.check_hostname = True

# Load CA used to validate other peers’ certificates when `verify_mode` is other than `CERT_NONE`.
context.load_verify_locations('cert.pem')

ssl_sock = context.wrap_socket(s, server_hostname='Beginman')

ssl_sock.connect(('127.0.0.1', 8899))

pprint(ssl_sock.getpeercert())

ssl_sock.send(b'a'*100)
data = ssl_sock.recv(1024)
print ("Received:", len(data), data)
ssl_sock.close()

# print:
"""
{'issuer': ((('countryName', u'CH'),),
            (('stateOrProvinceName', u'BeiJing'),),
            (('localityName', u'Beijing'),),
            (('organizationName', u'LZX'),),
            (('organizationalUnitName', u'TeamAPP'),),
            (('commonName', u'Beginman'),),
            (('emailAddress', u'xinxinyu2011@163.com'),)),
 'notAfter': 'May 27 04:32:31 2017 GMT',
 'notBefore': u'May 27 04:32:31 2016 GMT',
 'serialNumber': u'AE54E33F78B638E2',
 'subject': ((('countryName', u'CH'),),
             (('stateOrProvinceName', u'BeiJing'),),
             (('localityName', u'Beijing'),),
             (('organizationName', u'LZX'),),
             (('organizationalUnitName', u'TeamAPP'),),
             (('commonName', u'Beginman'),),
             (('emailAddress', u'xinxinyu2011@163.com'),)),
 'version': 3L}

('Received:', 1024, 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...
"""