#coding=utf-8

class A():

	height = 187.9

	# 实例方法
	def func(self):
		self.sex = "男"


a1 = A()
a1.func()


# 创建实例属性的方式2
a1.name = "老王"
print(a1.name)

A.age = 18
print(A.age)
print(a1.age)
# print(A.name)

print(a1.sex)

# print(A.sex)
