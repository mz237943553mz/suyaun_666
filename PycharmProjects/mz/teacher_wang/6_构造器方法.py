#coding=utf-8

"""
几个实例对象，几个类对象
几个属性，几个方法
"""
class Stu():
	name = "老王"
	# 构造器/初始化方法:创建对象,默认掉用__init__初始化方法
	def __init__(self):
		print("初始化方法开启")

	# 定义一个自定义的方法
	def func(self):
		print("我的名字为",self.name)

# Stu():称之为实例化过程
s1 = Stu()
# 实例方法,能通过实例对象/实例化过程调用
Stu().func()
s1.func()

# 不能通过类对象访问
# Stu.func()
