# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '16/3/22'
import socket
import select

EOL1=b'\n\n'
EOL2=b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon,1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 7800))
sock.listen(1)
sock.setblocking(0)

# 创建epoll对象，注册socket对象的可读事件
epoll = select.epoll()
epoll.register(sock.fileno(), select.EPOLLIN)
try:
    connections = {}
    requests = {}
    responses = {}
    while True:
        # 主循环，epoll系统调用，一旦有网络I/O事件发生，poll调用返回
        events = epoll.poll(1)
        # 通过事件通知获得监听的文件描述符
        for fileno, event in events:
            print fileno,event, sock.fileno()
            if fileno == sock.fileno(): # 注册监听的socket对象可读，获取连接，并注册连接socket的可读事件
                connection, address = sock.accept()
                print u"已连接", address
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)

                connections[connection.fileno()] = connection   # 连接socket描述符的字典
                requests[connection.fileno()] = b''             # 请求字典
                responses[connection.fileno()] = response       # 响应字典
                print 'connections:', connections, select.EPOLLIN
            elif event & select.EPOLLIN:    # 连接对象可读，处理客户端发生的信息，并注册连接对象可写
                print "连接对象可读"
                requests[fileno] += connections[fileno].recv(1024)
                print requests[fileno]
                #if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                #    epoll.modify(fileno, select.EPOLLOUT)
                #    print('-'*40+'\n'+requests[fileno].decode()[:-2])
                epoll.modify(fileno, select.EPOLLOUT)
                print('-'*40+'\n'+requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:   # 连接对象的可写事件发生，发送到客户端
                print u"连接对象可写"
                responses[fileno]+=requests[fileno]
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    epoll.modify(fileno, 0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                print u"client连接关闭"
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(sock.fileno())
    epoll.close()
    sock.close()