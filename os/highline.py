#! /usr/bin/env python
# coding:utf-8
# **************************************
# Function: python 打开Py文件高亮显示
# Version:  1.0
# Author:   'beginman'
# **************************************
# py colorama:https://pypi.python.org/pypi/colorama
import os
import random
from colorama import *
init(autoreset=True)
COLOR = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.BLACK, Fore.YELLOW,
         Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.RESET]
BACK = Back.GREEN                               # 行号

Syna = {
    'def': Fore.RED+Style.BRIGHT,
    'class': Fore.GREEN+Style.BRIGHT,
    '"""': Fore.YELLOW+Style.BRIGHT,
    "'''": Fore.YELLOW+Style.BRIGHT,
    'import': Fore.YELLOW,
    'from': Fore.YELLOW,
    'for': Fore.MAGENTA+Style.BRIGHT,
    'elif': Fore.MAGENTA+Style.BRIGHT,
    'else': Fore.MAGENTA+Style.BRIGHT,
    'print': Fore.CYAN,
    '#': Fore.GREEN
    }


def PrintFile(path):
    """Print file"""
    f = open(path)
    count = 1
    for line in f.readlines():
        sy_list = [i for i in Syna.items()]
        RANDOM_COLOR = [s[1] for s in sy_list if line.strip().startswith(s[0])]
        RANDOM_COLOR = RANDOM_COLOR[0] if RANDOM_COLOR else random.choice(COLOR)

        n = u'☺ %s   ' % count if count<10 else u'☺ %s  ' % count
        linenum = Style.NORMAL+BACK + n
        count += 1
        print linenum,RANDOM_COLOR + line.strip()


def GetPath():
    """choice file"""
    while True:
        file = raw_input(u'请输入指定文件:')
        if os.path.isfile(file):
            break
    return file

def main():
    PrintFile(GetPath())

if __name__ == '__main__':
    main()

