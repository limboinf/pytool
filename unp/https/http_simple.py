# coding=utf-8
"""
使用BaseHTTPServer实现简单的HTTP请求,响应hello,world.

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):           # 方法以 do_ 做前缀
        """response"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write("Hello, world!")


class CustomHTTPServer(HTTPServer):     # HTTPServer 继承 SocketServer.TCPServer

    def __init__(self, host, port):
        server_addr = (host, port)
        HTTPServer.__init__(self, server_addr, RequestHandler)  # 处理类


def run(host, port):
    try:
        server = CustomHTTPServer(host, port)
        print "Custom HTTP server started on host: %s port: %s" % (host, port)
        server.serve_forever()
    except Exception as err:
        print err
    except KeyboardInterrupt:
        print "Server interrupted and is shutting down..."


if __name__ == '__main__':
    run(sys.argv[1], int(sys.argv[2]))
