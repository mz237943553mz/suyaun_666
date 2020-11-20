#coding=utf-8

"""
继承：分为单继承和多继承
"""


# 父类
class Father():

	# 类属性
	name = "小漂亮"

	# 创建一个初始化方法
	def __init__(self):
		print("初始化方法默认调用")

	def run(self):
		print("%s会跑"%self.name)

# 子类
class Son(Father):

	def eat(self):
		# 调用父类的方法：1.self.方法名()
		self.run()
		# 方法2
		# Father.run(self)

		# 通过super().方法名()
		# super().run()
		print("会吃")

s1 = Son()
s1.eat()
# s1.run()
# print(s1.name)

