# Python 测试 epoll模型

环境：Centos 6.5

启动服务端：

    python epoll_demo.py

客户端连接并发送数据：
    [root@xxx ~]# telnet 127.0.0.1 7800
    Trying 127.0.0.1...
    Connected to 127.0.0.1.
    Escape character is '^]'.
    jack
    HTTP/1.0 200 OK
    Date: Mon,1 Jan 1996 01:01:01 GMT
    Content-Type: text/plain
    Content-Length: 13

    Hello, world!jack
    Connection closed by foreign host.

则服务端变化如下：

    3 1 3
    已连接 ('127.0.0.1', 48774)
    connections: {5: <socket._socketobject object at 0x7f0b14686600>} 1
    5 1 3
    连接对象可读
    jack

    ----------------------------------------
    jack
    5 4 3
    连接对象可写
    5 16 3
    client连接关闭
