# coding=utf-8
"""
Multi-threaded download.

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '15/10/29'

import threading
import requests
import os
import time

dir_path = os.path.join(os.path.dirname(__file__), 'font.ttf.zip')
chunk_bytes = 65536

lock = threading.Lock()


def get_length_by_range(url):
    """Whether to accept a file by HTTP head.
    Accept-Ranges:  If accepts will return bytes, otherwise return none.
    content-length: the length of response data

    @:arg url: download url
    @:return bytes or None
    """
    head = requests.head(url)
    if head.headers.get('accept-ranges'):
        return int(head.headers.get('content-length', 0))
    return None


def write_file(start, buf, f):
    """Write file"""
    f.seek(start)
    f.write(buf)


def download(url, f):
    """download the whole file."""
    print 'download the whole file....'
    ret = requests.get(url)
    f.write(ret.content)


class DownloadThread(threading.Thread):
    """download thead"""
    def __init__(self, url, tid, length, f):
        """We need to use chunked download
        @:arg url: download url
        @:arg tid: current num
        @:arg length: current length
        @:arg f: fileobject
        """
        self.url = url
        self.tid = tid
        self.length = length
        self.f = f
        super(DownloadThread, self).__init__()

    def run(self):
        start = chunk_bytes * self.tid
        end = chunk_bytes * (self.tid + 1) - 1

        if end >= self.length:
            end = self.length - 1

        headers = dict()
        headers['Range'] = 'bytes=%s-%s' % (start, end)
        print 'chunk thread:%s Range: %s download...' % (self.tid, headers['Range'])
        ret = requests.get(self.url, headers=headers)

        with lock:
            write_file(start, ret.content, self.f)


if __name__ == '__main__':
    url = 'http://7xkcd8.com1.z0.glb.clouddn.com/tuandui.apk'       # 5535143
    f = open(dir_path, 'wb')
    plist = []
    content_length = get_length_by_range(url)
    print 'the length of response:', content_length
    if not content_length:
        # download full file
        s = time.time()
        download(url, f)
        print 'Use time:', time.time() - s
    else:
        # download file trunk
        s = time.time()
        block = content_length / chunk_bytes + 1

        for i in range(0, block):
            t = DownloadThread(url, i, content_length, f)
            plist.append(t)

    for t in plist:
        t.start()

    for t in plist:
        t.join()

    f.close()
    print '文件下载完成'
    print 'Use time:', time.time() - s