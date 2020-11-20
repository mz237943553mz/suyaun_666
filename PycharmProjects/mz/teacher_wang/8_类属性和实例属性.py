#coding=utf-8

"""
类属性：写法跟变量类似
实例属性：在实例方法中写的：，写法格式: self.属性名=值
实例属性的调用：self.实例属性名访问   注意：若要在其它方法访问上面的实例属性时，必须先调用自身的方法
"""

class Dog():

	# 类属性
	color = "白色"

	def run(self):
		# 实例属性
		self.name = "二狗"
		# 局部变量
		sex = "男"
		print("性别为:",sex)
		print("我的名字为%s,颜色为%s"%(self.name,self.color))

	def run2(self):
		# 访问上面方法的实例属性
		# self.name="三狗"

		print(self.name)
		# 直接访问的类属性
		print(self.color)

		# 在这个方法里访问不了上面的局部变量
		# print(self.sex)

d1 = Dog()
d1.run()
d1.run2()

# 直接可以在类外方访问的
print(Dog.color)
print(d1.color)


# 在类外方访问实例属性
# print(Dog.name)
# 可以在类外方通过实例对象访问实例属性
print(d1.name)




