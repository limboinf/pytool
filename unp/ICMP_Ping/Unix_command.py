# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import subprocess
import shlex
import sys

command_line = "ping -c 1 %s" % sys.argv[1]
args = shlex.split(command_line)
try:
    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print "Ping ok!"
except subprocess.CalledProcessError:
    print "Failed to get ping."
