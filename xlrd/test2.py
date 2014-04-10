#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-10 23:10:35
# @Function:
# @Author  : BeginMan

import os
import xlwt
file = xlwt.Workbook()
table = file.add_sheet('name',cell_overwrite_ok=True)
table.write(0,0,'a')
defatul_f = r'C:\Users\Administrator\Desktop\pytool\xlrd\'		# 默认路径
f = raw_input(u'请选择保存文件的路径：')
f_name = 'test.xls'
file.save()

