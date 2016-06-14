# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '16/3/18'
import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置地址复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 12355))
server.listen(5)

inputs = [server]       # select监听的列表

while(inputs):
    # 调用 select 函数，阻塞等待, 这里只处理 readable
    rlist, wlist, xlist = select.select(inputs, [], [])
    # 网络IO就绪，readable, 则遍历可读socket（PS.readable满足的几个条件）
    for sock in rlist:
        # (1). 建立连接
        if sock == server:
            # accept()方法建立TCP三次握手的连接
            # 然后把该连接socket 追加到inputs监视列表中
            # 接下来的遍历中，select要监视该连接是否有数据IO操作
            conn, addr = server.accept()
            inputs.append(conn)             # select监听连接socket
            print "connected, ", addr
        else:
            # (2).读取客户端连接发送的数据
            data = sock.recv(1024)
            if data:
                sock.send("good:" + data)
                if data.endswith('\r\n\r\n'):
                    # 移除select监听的socket并关闭连接
                    inputs.remove(sock)
                    sock.close()
            else:
                # 如果客户端端口连接，data为空，这里移除select监听的socket并关闭连接
                print 'EOF'
                inputs.remove(sock)
                sock.close()
