import urllib2
import socket
import os
import threading
import sys
from bs4 import BeautifulSoup

baseurl = "http://jandan.net/ooxx/"
save_path = 'imgs/'


def agent(url):
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Mac OS X; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req_timeout = 15
    for i in range(2):
        try:
            req = urllib2.Request(url, None, req_header)
            page = urllib2.urlopen(req, None, req_timeout)
            return page
        except urllib2.URLError as e:
            print e.message
        except socket.timeout:
            print 'Timeout:', req_timeout


def start(page_id):
    url = baseurl + 'page-%s' % page_id
    print "fetch XXOO from", url
    page = agent(url)
    soup = BeautifulSoup(page, "html.parser")
    imgs = soup.find_all(['img'])
    for img in imgs:
        try:
            link = img.get('src')
            if link.startswith('http://k.min.us/') or link.startswith(
                    'http://i.min.us/') or link.startswith('http://s.jandan.com/'):
                continue

            file_name = link[-11:].replace('/', '')

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            context = agent(link)
            if context:
                context = context.read()
                with open(save_path + file_name, 'wb') as f:
                    f.write(context)

        except Exception:
            pass


def run(page_start, page_stop):
    try:
        page_start = int(page_start)
        page_stop = int(page_stop)
        if page_start < 0 or page_stop < 0 or page_stop < page_start:
            raise ValueError("Usage: python xx.py page_start page_stop")
    except:
        raise ValueError

    print "Prepare to fetch xxoo pictures from %s ~ %s page...." % (page_start, page_stop)
    threads = []
    for i in xrange(page_start, page_stop):
        t = threading.Thread(target=start, args=(i, ))
        threads.append(t)

    for t in threads:
        t.start()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python {0} <page_start> <page_stop>\n   example: python {0} 2000 2016".format(sys.argv[0])
    else:
        run(sys.argv[1], sys.argv[2])
