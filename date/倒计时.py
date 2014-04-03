#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-02 21:48:36
# @Function:
# @Author  : BeginMan

import time
count = 0	
a = input('time:')	
b = a * 60	
while (count < b):
	ncount = b - count
	print ncount	
	time.sleep(1)
	count += 1	
print 'done'	
