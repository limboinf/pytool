# coding=utf-8
"""
https://github.com/dieseldev/diesel
代码示例:https://github.com/dieseldev/diesel/tree/master/examples
不建议使用diesel,这个库仅仅支持python2.x且两三年没更新了,连官网都找不到了

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import diesel


class EchoServer(object):

    def handler(self, remote_addr):
        host, port = remote_addr[0], remote_addr[1]
        print "Echo client connected from: %s:%d" % (host, port)
        while True:
            try:
                msg = diesel.until_eol()
                y = ': '.join(["you said", msg])
                diesel.send(y)
            except Exception as e:
                print e


def main(server_port):
    app = diesel.Application()
    server = EchoServer()
    app.add_service(diesel.Service(server.handler, server_port))
    app.run()

if __name__ == '__main__':
    main(8899)
