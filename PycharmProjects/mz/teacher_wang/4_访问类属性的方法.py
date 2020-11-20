#coding=utf-8

"""
访问类属性的方法：
1.能通过实例方法进行访问

2.能直接在类外方通过类名访问
"""

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


# 直接在类外放调用类属性
print("类名调用类属性为:",Animal.name)
# 最好建议使用类对象进行调用
# 通过实例对象调用类属性
print("实例对象调用类属性为:",aa.name)
