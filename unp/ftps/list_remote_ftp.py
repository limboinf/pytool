# coding=utf-8
"""
列出FTP远程服务器的文件
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import ftplib

FTP_SERVER_URL = 'ftp.kernel.org'


def test_ftp_connection(path, user_name, email):
    ftp = ftplib.FTP(path, user_name, email)

    ftp.cwd('/pub/')
    files = ftp.dir()
    print files

    ftp.quit()

if __name__ == '__main__':
    test_ftp_connection(FTP_SERVER_URL,'anonymous','nobody@nourl.com')

    # output:
    # drwxrwxr-x    6 ftp      ftp          4096 Dec 01  2011 dist
    # drwxr-xr-x   14 ftp      ftp          4096 Nov 11  2014 linux
    # drwxrwxr-x    3 ftp      ftp          4096 Sep 23  2008 media
    # drwxr-xr-x   15 ftp      ftp          4096 Aug 03  2013 scm
    # drwxrwxr-x    2 ftp      ftp          4096 Aug 09  2013 site
    # drwxr-xr-x   13 ftp      ftp          4096 Nov 27  2011 software
    # drwxr-xr-x    3 ftp      ftp          4096 Apr 30  2008 tools
    # None

