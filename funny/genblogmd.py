# coding=utf-8
"""
blog markdown 自动生成, 博客markdown文件在 _post 下,文件格式:

```
---
layout: post
title: "博客标题"
description: "该篇博客的简介"
category: "分类"
tags: [标签,逗号分隔]
---
balabal 博客内容..

```

github项目: https://github.com/BeginMan/beginman.github.io

    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""

import os
import datetime
import argparse

BLOG_DIR = '_posts'


def gen_md(parses):
    ds = datetime.datetime.now().strftime("%Y-%m-%d")
    basepath = os.path.join(os.getcwd(), BLOG_DIR + '/' + parses.category)
    filepath = os.path.join(basepath, ds + '-' + parses.filename + '.md')
    if not os.path.exists(filepath):

        if not os.path.exists(basepath):
            os.makedirs(basepath)

        with open(filepath, 'w') as f:
            parser = vars(parses)
            parser.pop('filename')
            parser.update({'template': '{% include JB/setup %}'})
            f.write("""---
                    \r\nlayout: post
                    \r\ntitle: "{title}"
                    \r\ndescription: "{desc}"
                    \r\ncategory: "{category}"
                    \r\ntags: [{tags}]
                    \r\n---
                    \r\n{template}\r\n""".format(**parser))
    else:
        print("file exist!")

    print(filepath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate markdown blog template.")
    parser.add_argument('-f', '--filename', help="blog filename.", required=True)
    parser.add_argument('-t', '--title', help="blog title.", required=True)
    parser.add_argument('-d', '--desc', help="blog describe.", default='')
    parser.add_argument('-c', '--category', help="blog category.", default='Tech')
    parser.add_argument('--tags', help="blog tags, multiple tags split with comma.", default='')
    args = parser.parse_args()
    gen_md(args)
