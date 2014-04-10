#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-08 12:38:02
# @Function:
# @Author  : BeginMan
class P1:
	def foo(self):
		print 'P1--foo()'

class P2:
	def foo(self):
		print 'P2--foo()'
	def bar(self):
		print 'P2--bar()'

class C1(P1,P2):
	pass

class C2(P1,P2):
	def bar(self):
		print 'C2--bar()'

class GC(C1,C2):
	pass

gc = GC()
print gc
gc.foo()		# p1--foo()
gc.bar()		# p2--bar()
c2 = C2()
c2.foo()		# P1--foo()
c2.bar()		# C2--bar()



