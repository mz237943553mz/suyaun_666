#coding=utf-8

# 多行注释：注释代码，代码不执行
"""
条件语句：
if 条件1:
	第一个条件里的内容
elif 条件2:
	第二个条件里的内容
elif 条件3:
	第三个条件里的内容
else:
	最后一个语句
"""


"""
# 1.一个if语句
a = []
b = ()

# bool()===true和false
# 数字里0是False,空内容是false。其他内容都是true
print(bool(a))
print(bool(""))
print(bool(()))
print(bool(0))

a2 = []
if a2:
	print("有")
else:
	print("没有")
"""




"""
# 数值型和字符串的使用
# 数值型：int:整型   float:浮点型
# 字符串
a = 10
b = 23.7
c = '5'
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(a+b)
print(a+c)
"""

# 多个条件 if ...elif ..else
# 注意：input():不管输入的是什么，它的类型都是字符串

"""
num = int(input("请输入你家宠物的年龄"))
# print(num,type(num))
if num>1:
	print("大于1岁")
elif num<1:
	print("小于1")
else:
	print("1岁了")
"""


# 循环和条件一起使用
# 条件：if..elif..else
# 循环：while 循环的条件
num = 9
guess = 7
while num!=guess:
	guess = int(input("请输入您要猜的数字"))
	if guess>num:
		print("您猜的数字过大了")
	elif guess<num:
		print("您猜的数字过小了")
	else:
		print("恭喜你,猜对了！")

