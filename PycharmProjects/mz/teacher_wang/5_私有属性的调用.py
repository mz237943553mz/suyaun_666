#coding=utf-8

class Stu():

	# 共有的类属性
	name = "老王"

	# 私有的类属性
	__age = 18


	#　现在的方法中访问
	def name_func(self):
		# print("公有的为",self.name)
		# print("私有的为",self.__age)
		return self.__age



s = Stu()
# s.name_func()
print(s.name_func())

# 在类外放访问两个属性的区别
print(Stu.name)

# 通过类对象/实例对象访问私有,不能在类外放访问私有属性
# print(Stu.__age)
# print(s.__age)

