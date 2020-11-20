#coding=utf-8

class Animal():

	# 类属性
	age = 3
	name = "波斯"

	# 实例方法：self
	def eat(self):
		print("%s会跑,年龄为%d"%(self.name,self.age))

# 创建实例对象
aa=Animal()
aa.eat()



