# IPv6 Echo Server

同时处理IPV6和IPv4,主要使用`getaddrinfo`函数.

>gethostbyname和gethostbyaddr这两个函数仅仅支持IPv4，getaddrinfo函数能够处理名字到地址以及服务到端口这两种转换，返回的是一个sockaddr结构的链表而不是一个地址清单。


套接口地址结构的类型,`AF_INET`，`AF_INET6`和`AF_UNSPEC`。

- 如果指定`AF_INET`，那么不能返回任何IPV6相关的地址信息；
- 如果仅指定了`AF_INET6`，则就不能返回任何IPV4地址信息。
- `AF_UNSPEC`则意味着函数返回的是适用于指定主机名和服务名且适合任何协议族的地址。如果某个主机既有AAAA记录(IPV6)地址，同时又有A记录(IPV4)地址，那么AAAA记录将作为`sockaddr_in6`结构返回，而A记录则作为`sockaddr_in`结构返回。

具体教程参考我的印象笔记。