#coding=utf-8

class Animal():

	# 接受实参的实例方法
	def set_name(self,name):
		# 实例属性
		self.na = name

	# 输出名字的方法
	def dy_name(self):
		print("我的姓名为",self.na)

# 定义一个函数
# def zhu(dx):
# 	dx.dy_name()
#
# a = Animal()
# a.set_name("小李")
# zhu(a)
# a2 = Animal()
# a2.set_name("大漂亮")
# zhu(a2)


#调用一个函数
def zhu(dx):
	dx.dy_name()

a = Animal()
a.set_name("小李")
zhu(a)