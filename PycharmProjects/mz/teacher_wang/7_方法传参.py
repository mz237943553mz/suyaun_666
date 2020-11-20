#coding=utf-8

class Stu():

	# 构造器/初始化方法
	def __init__(self,name,sex):
		print(name,sex)

	def func(self,*args):
		print(args)

# 创建对象默认调用__init__方法
s = Stu(sex="男",name="老王")

s.func(1,24,455)



