#coding=utf-8

# 父类
class Father():

	# 类属性
	name = "小漂亮"

	# 创建一个初始化方法
	def __init__(self):
		print("初始化方法默认调用")

	def run(self,age):
		self.age = age
		print("年龄为",self.age)
		print("%s会跑"%self.name)

# 子类
class Son(Father):
	def eat(self,age):
		# 调用父类的方法：1.self.方法名()
		self.run(age)
		# 方法2
		# Father.run(self,age)

		# 通过super().方法名()
		# super().run(age)
		print("会吃")

s1 = Son()
s1.eat(30)
# s1.run()
# print(s1.name)