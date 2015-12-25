# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '11/6/15'
import redis
import logging


class MyRedis(object):
    # 已经使用的有5个库，这里使用key值前缀来作命名空间
    dbs = {
        'user': 0,
        'team': 1,
        'event': 2,
        'talk': 3,
        'docs': 4,
        'other': 5,
    }
    servers = {
        'test': {'host': '127.0.0.1', 'port': 6379, 'password': 'yourpasswd'},
        'prod': {'host': '', 'port': 6379, 'password': ''},
        'talk': {'host': '', 'port': 6379, 'password': ''}
    }

    def __init__(self, db, server='test', **kwargs):
        db = MyRedis.dbs.get(db, 0)
        server = MyRedis.servers.get(server)
        server.update({'db': db})
        server.update(kwargs)
        self.db = db
        self.server = server
        self.redis_pool = redis.ConnectionPool(**server)

    def get_redis(self):
        return redis.Redis(connection_pool=self.redis_pool)

    def shutdown(self):
        self.redis_pool.disconnect()

    def release(self, conn):
        self.redis_pool.release(conn)

    def show(self):
        logging.error(self.redis_pool.max_connections)
        logging.error(self.redis_pool._available_connections)
        logging.error(self.redis_pool._in_use_connections)


if __name__ == "__main__":
    # r = MyRedis('user', 'test')
    # rr = r.get_redis()
    # print rr.get('name')
    # # r.release(rr)
    #
    # rr = r.get_redis()
    # print rr.get('name')
    # print r.show()

    import time
    R = redis.Redis(password='2015yunlianxiQAZWSX')
    s = time.time()
    ids = R.lrange('test', 0, -1)
    print ids
    lis = []
    for i in ids:
        dic = {}
        prefix = 'test:%s:' % i
        keys = ['name', 'age', 'sex', 'score']
        print R.mget(('prefix:%s' % i,'test:%s:gs' % i, 'test:%s:sex' % i, 'test:%s:score' % i))
        # dic['name'] = R.get('test:%s:name' % i)
        # dic['age'] = R.get('test:%s:age' % i)
        # dic['sex'] = R.get('test:%s:sex' % i)
        # dic['score'] = R.get('test:%s:score' % i)
        # print dic
        lis.append(dic)
    print lis

    print 'use time:', (time.time()-s)


