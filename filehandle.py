#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = 'beginman'
import platform
import os
import time



def ChoiceFile(filename):
	"""选取文件分布在windows或Linux"""
	filepath = '/home/beginman/github/blog/_post'
	system = 'linux'
	if (platform.system()).lower() == 'windows':
		system = 'windows'
		filepath = 'E:\\gitblog\\beginman.github.com\_posts'
	if os.path.isdir(filepath):
		files = os.listdir(filepath)		# 列出该目录下的所有文件
		files_list = []
		for obj in files:
			dic ={}
			single_file = filepath+'\\'+obj if system == 'windows' else filepath+'//'+obj
			dic['name'] = obj
			timestamp = os.path.getmtime(single_file)			# 获取文件最近修改时间戳
			x = time.localtime(timestamp)
			dic['date'] = time.strftime('%Y-%m-%d %H:%M:%S',x)
			size = os.path.getsize(single_file)					# 获取文件大小
			dic['size'] = str(round(size/1024,2))+' KB'
			files_list.append(dic)
		return files_list	
		#filename = raw_input('输入要处理的文件名或模糊名称：')
		#if filename:

def main():
	print ChoiceFile('linux.md')


if __name__ == '__main__':
	main()


