# coding=utf-8
"""
关于StringIO参考 ：https://github.com/BeginMan/pythonStdlib/blob/master/stringIO.md
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/13/16'

import StringIO
from flask import Flask, send_file


app = Flask(__name__)


@app.route('/')
def index():
    """Upload a StringIO object with send_file"""
    strIO = StringIO.StringIO()
    strIO.write("Hello, world\n")
    strIO.write("中国")
    strIO.seek(0)
    return send_file(strIO,
                     attachment_filename='strIO.txt',
                     as_attachment=True)

if __name__ == '__main__':
    app.run()


