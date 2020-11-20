#coding=utf-8

"""
实例方法和类方法以及静态方法的区别：
1.调用类属性的不同
2.在类外方调用的不同
3.写法不同

"""

class B():

	# 类属性
	color = "黄色"

	# 实例方法
	def func(self):
		print("实例方法调用类属性",self.color)
		print("实例方法")


	# 类方法
	@classmethod
	def run(cls):
		cls.age = 100
		print("类方法调用类属性",cls.color)
		print("类方法创建好了")


	# 静态方法
	@staticmethod
	def jinta():
		# 只能通过类对象访问
		print("静态方法",B.color)


# 在类外方调用两个方法
b1 = B()
b1.func()
# 实例方法不能通过类对象调用
# B.func()
# B().func()


# 在类外方调用类方法
# b1.run()
B.run()

# print(B.age)
# print(b1.age)
print("="*50)
b1.jinta()
B.jinta()

