#coding=utf-8

class Pig():

	# 共有的类属性
	color = "白色"

	# 私有的类属性
	__age = 28

	# 在方法中访问,私有公有属性都有
	def func(self):

		self.sex="男"
		print(self.color)
		print(self.__age)

p = Pig()
p.func()

# 在类外方直接访问公有属性,最好使用类对象访问
print(Pig.color)
print(p.color)
print(Pig().color)


# 在类外方访问实例属性，只能通过实例对象访问
print(p.sex)
# print(Pig.sex)
# print(Pig().sex)

# 不能在类外方直接访问私有属性
# print(Pig.age)
# print(p.age)


