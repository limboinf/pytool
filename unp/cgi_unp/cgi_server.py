# coding=utf-8
"""
CGI服务器
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import cgi
import cgitb
import argparse
import BaseHTTPServer
import CGIHTTPServer


cgitb.enable()  # enable CGI error reporting


def web_server(port):
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_addr = ("", port)
    handler.cgi_directories = ["/cgi-bin", ]
    httpd = server(server_addr, handler)
    print "Starting web server with CGI support on port: %s ..." % port
    httpd.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CGI Server")
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    args = parser.parse_args()
    web_server(args.port)

