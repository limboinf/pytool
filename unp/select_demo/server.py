# coding=utf-8
"""
select demo for server
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import socket
import select
import Queue

# 创建非阻塞socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# 设置socket地址复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 12345)
server.bind(server_address)
server.listen(10)

read_puts = [server]            # 待读socket列表
write_puts = []                 # 待写socket列表
queue = {}                      # 消息队列
timeout = 20                    # select超时时间

while read_puts:
    # select三个列表包含要监视的通信通道
    readable, writeable, execptional = select.select(read_puts,
                                                     write_puts,
                                                     read_puts,
                                                     timeout)

    # 如果超时则返回三个空列表
    if not (readable or writeable or execptional):
        print "Time out."
        break

    for s in readable:
        if s is server:
            # 准备accept的可读socket
            connection, client_address = s.accept()
            print "connect from", client_address
            connection.setblocking(False)
            read_puts.append(connection)
            queue[connection] = Queue.Queue()
        else:
            # 有排队数据供读取
            data = s.recv(1024)
            if data:
                print "received data:%s from %s" % (data, s.getpeername())
                queue[s].put(data)
                # Echo, 加入待写列表
                if s not in write_puts:
                    write_puts.append(s)
            else:
                # Interpret empty result as closed connection
                print "closing", client_address

                # 关闭连接,移除该socket
                if s in write_puts:
                    write_puts.remove(s)
                read_puts.remove(s)
                s.close()
                del queue[s]

    for s in writeable:
        try:
            next_msg = queue[s].get_nowait()
        except Queue.Empty:
            print s.getpeername(), 'queue empty'
            write_puts.remove(s)
        else:
            print "sending " , next_msg , " to ", s.getpeername()
            s.send(next_msg)

    for s in execptional:
        print "exception condition on ", s.getpeername()
        read_puts.remove(s)
        if s in write_puts:
            write_puts.remove(s)
        s.close()
        del queue[s]