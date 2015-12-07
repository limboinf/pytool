# coding=utf-8
__author__ = 'fang'
import logging
import os
import datetime
from logging.handlers import RotatingFileHandler
from multiprocessing import current_process  # 返回当前对象进程

def config_log(log_path=None, logging_level=logging.DEBUG):
    if not log_path:
        log_path = os.path.join(os.path.dirname(__file__), 'logs')
    log_path = os.path.join(log_path, datetime.datetime.now().strftime('%Y-%m-%d %H'))
    # log_path: /Users/fang/project/beginman/pytool/log/logs/2014-12-03 11

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    root_log = logging.getLogger()      # 默认name：root
    root_log.setLevel(logging_level)
    rfh = RotatingFileHandler(
        filename = os.path.join(log_path, 'log-%s-%s.txt' %(current_process().name, current_process().ident)),
        mode = 'a',
        maxBytes = 1024*1024*1,
        backupCount=30,
        encoding='utf-8'
    )
    root_log.addHandler(rfh)
    stream = logging.StreamHandler()
    stream.setFormatter(logging.Formatter('%(asctime)s --%(message)s'))
    root_log.addHandler(stream)




if __name__ == '__main__':
    config_log()