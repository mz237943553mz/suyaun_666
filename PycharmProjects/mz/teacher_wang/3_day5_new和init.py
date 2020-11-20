#coding=utf-8

"""
__new__和__init__的区别：
1.在创建对象，默认调用__init__，python解析器会首先自动调用__new__方法，为对象分配空间，返回引用地址

2.如果要自己手写__new__方法的话，代码很固定,return super().__new__(cls)即可。
"""

# __init__():构造器/初始化方法====创建对象默认被调用

class Stu():

	# __new__是一个内置方法。
	def __new__(cls, *args, **kwargs):
		print("分配空间,返回引用地址")
		return super().__new__(cls)

	# 创建对象,默认调用
	def __init__(self):
		print("初始化开始")

s1 = Stu()
s2 = Stu()
print(s1)
print(s2)
