#coding=utf-8
import time

"""
两种方式能调用
1.执行结束完毕，利用回收机制，自动调用
2.手动删除实例对象：del 实例对象 
"""

class Tea():

	# 析构方法
	def __del__(self):
		print("回收机制默认调用析构方法")


	# 自定义的实例化方法
	def func(self):
		# 实例属性
		self.age = 18
		print("我的年龄为",self.age)

t1 = Tea()

t1.func()
del t1

# t1.func()
print("1111111")
time.sleep(2)

