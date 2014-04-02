#! /usr/bin/env python
# coding:utf-8
import os
path = '/home/beginman/桌面/test'

def Tree(path):
    """Simulation tree of file"""
    pathfile= os.listdir(path)
    info = []
    i = 1
    for file in pathfile:
        dic = {}
        dic['%s' %i] = file



def TestPath():
    while True:
        path = raw_input('Please input path\n:')
        if os.path.isdir(path):
            break
    return path