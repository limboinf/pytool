#/usr/bin/python
# coding=utf-8
"""
个人blog md生成：http://beginman.cn
command: genblog.sh genblog.py "文件名" "文件标题" 分类
注意换行符的问题
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '11/10/15'
import sys
import os
import datetime

def genmd():
    ds = datetime.datetime.now().strftime("%Y-%m-%d")
    if len(sys.argv) > 1:
        title = sys.argv[1]
        path = os.path.join(os.getcwd(), ds + '-' + title + '.md')
        if not os.path.exists(path):
            f = open(path, 'w')
            f.write('---\r\nlayout: post\r\ntitle: "%s"\r\ndescription: "%s"\r\ncategory: "%s"\r\ntags: [%s]\r\n---\r\n{%% include JB/setup %%}\r\n'
                    % (sys.argv[2], sys.argv[2], sys.argv[3], sys.argv[3]))
            f.close()


if __name__ == "__main__":
    genmd()
