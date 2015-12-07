#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-10 21:47:56
# @Function: 指定选取三列然后挑选出同时满足>=1或者同时<=-1的 将其所有数据存入新的csv表格中 
# @Author  : BeginMan

import os
import string
import xlrd
import xlwt

def get_data():
	"""获取excel数据源"""
	file = r'C:\Users\Administrator\Desktop\pytool\xlrd\initial_log_data.xls'			# 改成自己的路径
	filepath = raw_input(u'请将xls文件路径粘贴进去，如果程序里已经指定了文件则按Enter键继续：')
	is_valid = False 			# 验证文件
	try:
		filepath = [file, filepath][filepath != '']
		print filepath
		# 判断给出的路径是不是xls格式
		if os.path.isfile(filepath):
			filename = os.path.basename(filepath)
			if filename.split('.')[1] == 'xls':
				is_valid = True
		data = None
		if is_valid:
			data = xlrd.open_workbook(filepath)
	except Exception, e:
		print u'你操作错误：%s' %e
		return None
	return data

def handle_data():
	"""处理数据"""
	data = get_data()
	if data:
		col_format = ['B', 'C', 'D']		# 指定的列
		inp = raw_input(u'请选择指定的三列，用逗号分隔，默认的是B,C,D(英文逗号,不区分大小写)，如果选择默认则按Enter键继续:\n')
		try:
			inp = inp.split(',')
			col_format = [col_format,inp][len([i for i in inp if i in string.letters]) == 3]
			col_format = [i.upper() for i in col_format]					# 转换成大写
			table = data.sheet_by_index(0)									# 选取第一个工作区
			nrows = table.nrows												# 行数
			ncols = table.ncols												# 列数
			str_upcase = [i for i in string.uppercase]						# 所有大写字母
			i_upcase = range(len(str_upcase))								# 对应的数字
			ncols_dir = dict(zip(str_upcase,i_upcase))						# 格式成字典
			col_index = [ncols_dir.get(i) for i in col_format]				# 获取指定列所对应的索引

			# 选取的三列是否同时满足 >=1或者同时<=-1
			print u'正在检索中……'
			count = 0
			result = []
			for i in xrange(nrows):
				cell_0 = table.cell(i,col_index[0]).value
				cell_1 = table.cell(i,col_index[1]).value
				cell_2 = table.cell(i,col_index[2]).value
				if (cell_0>=1 and cell_1>=1 and cell_2>=1) or (cell_0<=-1 and cell_1<=-1 and cell_2<=-1):
					result.append(table.row_values(i))		# 将符合要求的一行添加进去
					count += 1
			print u'该文件中共%s行，%s列,其中满足条件的共有%s条数据' %(nrows, ncols, count)
			print u'正在写入数据……'
			col_name = col_format[0]+col_format[1]+col_format[2]
			if write_data(result, col_name):
				print u'写入成功！'
		except Exception, e:
			print u'你操作错误：%s' %e
			return None
	else:
		print u'操作失败'
		return None


def write_data(data, name):
	"""写入数据,data为符合条件的数据列表，name表示指定的哪三个列，以此命名"""
	file = xlwt.Workbook()
	table = file.add_sheet(name,cell_overwrite_ok=True)
	l = 0   # 表示行
	for line in data:
		c = 0 	# 表示一行下的列数
		for col in line:
			table.write(l,c,line[c])
			c += 1
		l += 1		
	defatul_f = r'C:\Users\Administrator\Desktop\pytool\xlrd'		# 默认路径
	f = raw_input(u'请选择保存文件的路径：按回车跳过：')
	f_name = r'\%s.xls' % name
	filepath = [defatul_f+f_name, f+f_name][f != '']
	file.save(filepath)
	return True


def main():
	handle_data()

if __name__ == '__main__':
	main()