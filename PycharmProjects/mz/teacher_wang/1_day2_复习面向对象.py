#coding=utf-8

"""
1.面向对象：python  java php  .net
定义：对方法进行封装，减少代码的重复性
组成：类名(最好开头字母为大写)、属性、方法
属性：
	分类：分为公有属性:既能在方法中访问,也能在类外访问.私有属性：只能在方法中访问
		类属性和实例属性
		类属性：写在类下面方法之外
		实例属性：写在方法内的

方法：
分为：自定义方法和内置方法
内置方法：__init__():创建对象自动调用     __del__():1.程序执行完毕,自动调用  (2).del 实例对象
自定义方法：(1).实例方法def 方法名(self)

继承：分为单继承和多继承
（1).调用父类的方法：
	(1.1).self 方法名()
	(1.2).父类名.方法名(self,)
	(1.3).super().方法名()
(2).子类继承多个父类，若方法名相同,使用就近原则

重载。。。。







2.面向过程：c++
定义：根据逻辑冲上往下执行
"""


"""
class Teacher():

	# 类属性
	name = "王老师"

	def study(self):
		# 实例属性
		self.height = 165.6
		print("身高为",self.height)
		# 变量
		age = 18
		print("%s正在学"%self.name)

	def eat(self):
		print("eat的调用为",self.name)
		print("实例属性",self.height)

a = Teacher()
a.study()
print(a.height)
a.eat()

print("类对象调用",Teacher.name)
# print("实例对象调用",a.name)
"""

class Stu():

	def __init__(self):
		self.age = 10

class Stu2(Stu):
	def func(self):
		print(self.age)


s = Stu2()
s.func()

