# coding=utf-8
"""
python redis
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '15/11/4'
import redis
import tornado.ioloop
import tornado.web

r = redis.Redis(host='127.0.0.1', password='2015yunlianxiQAZWSX')       # 在这个阶段并没有开始TCP连接，TCP连接是发生在交互的过程，如下


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        info = r.info()
        self.write(info)


application = tornado.web.Application([
    (r'/', MainHandler),
])

if __name__ == '__main__':
    application.listen(7000)
    tornado.ioloop.IOLoop.current().start()

