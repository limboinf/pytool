#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = 'beginman'
import platform
import os


def ChoiceFile(filename):
	"""选取文件分布在windows或Linux"""
	filepath = '/home/beginman/github/blog/_post'
	if (platform.system()).lower() == 'windows':
		filepath = 'E:\\gitblog\\beginman.github.com\_posts'
	files = os.listdir(filepath)
	if os.path.isdir(filepath):
		return files
	#filename = raw_input('输入要处理的文件名或模糊名称：')
	#if filename:

def main():
	print ChoiceFile('linux.md')


if __name__ == '__main__':
	main()


