#coding=utf-8

"""
两大对象：类对象和实例对象   ====注意：一个类可以创建多个实例对象
类的由3大组成：
1、类名:Cat()
2、属性:color      name
3、方法:catch()    run()
"""

# 类名
class Cat():

	# 类属性，写法跟变量名类似
	color = "白色"
	name = "加菲猫"

	# 方法(实例方法)：写法：def 方法名(self):
	def catch(self,color):
		self.color=color
		print(color,"会抓老鼠")

	def run(self):
		print("会跑")

if __name__ == '__main__':

	# 调用实例方法:   写法：c1(实例对象) = 类名()
	c1 = Cat()
	c1.catch("yello")
	c2 = Cat()
	c2.run()





