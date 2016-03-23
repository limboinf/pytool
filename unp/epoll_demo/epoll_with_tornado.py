# coding=utf-8
"""
文／人世间（简书作者）
原文链接：http://www.jianshu.com/p/0fb633010296

既然epoll是一种高性能的网络io模型，很多web框架也采取epoll模型。
大名鼎鼎tornado是python框架中一个高性能的异步框架，其底层也是来者epoll的IO模型。
当然，tornado是跨平台的，因此他的网络io，在linux下是epoll，unix下则是kqueue。
幸好tornado都做了封装，对于开发者及其友好，下面看一个tornado写的回显例子。
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '16/3/23'
import errno
import functools
import socket
import tornado.ioloop


def handle_connection(connection, address):
    """ 处理请求，返回数据给客户端 """
    data = connection.recv(1024)
    print data
    connection.send(data)


def connection_ready(sock, fd, events):
    """事件回调函数，主要用于socket可读事件，获取socket连接"""
    while True:
        try:
            conn, address = sock.accept()
            print 'connection:', address
        except socket.error as e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        conn.setblocking(0)
        handle_connection(conn, address)


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(('', 6000))
    sock.listen(128)
    return sock

if __name__ == '__main__':
    sock = server()
    # 使用tornado封装好的epoll接口，即IOLoop对象
    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(connection_ready, sock)

    # io_loop对象注册网络IO文件描述符和回调函数与IO事件绑定
    io_loop.add_handler(fd=sock.fileno(),
                        handler=callback,
                        events=io_loop.READ)
    io_loop.start()
