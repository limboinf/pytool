# coding=utf-8
"""
Python实现断点续传
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import urllib
import os

TARGET_URL = 'http://python.org/ftp/python/2.7.4/'
TARGET_FILE = 'Python-2.7.4.tgz'


class CustomURLOpener(urllib.FancyURLopener):
    """Override FancyURLopener to skip error 206 (when a
       partial file is being sent)
    """
    def http_error_206(self, url, fp, errcode, errmsg, headers, data=None):
        pass


def resume_download():
    file_size = 0
    loop = True

    download = CustomURLOpener()
    if os.path.exists(TARGET_FILE):
        out_file = open(TARGET_FILE, 'ab')
        file_size = os.path.getsize(TARGET_FILE)

        # If the file exists, then only download the unfinished part
        print "download from bytes:", file_size
        download.addheader("range", "bytes=%s-" % file_size)
    else:
        out_file = open(TARGET_FILE, "wb")

    web_page = download.open(TARGET_URL + TARGET_FILE)

    # Check if last download was OK
    file_total_size = int(web_page.headers['Content-Length'])
    if file_total_size == file_size:
        loop = False
        print "File already downloaded!"

    byte_count = 0
    while loop:
        data = web_page.read(8192)
        if not data:
            break

        out_file.write(data)
        byte_count += len(data)
        print "has download %s bytes, remain %s bytes" % (byte_count, file_total_size-byte_count)

    web_page.close()
    out_file.close()

    print '\n----------------- Headers:----------------------\n'
    for k, v in web_page.headers.items():
        print k, '=', v
    print '\n----------------- Summary:-----------------------\n'
    print "File copied", byte_count, "bytes from", web_page.url


if __name__ == '__main__':
    resume_download()
