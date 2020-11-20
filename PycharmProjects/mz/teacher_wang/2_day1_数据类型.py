#coding=utf-8

# 数学函数
import math

# 随机数

import random

"""
# 数学math
# int   float
# 1.上入整数
print(math.ceil(22.39))

# 下舍整数
print(math.floor(12.06))

# pow()====次方
print(pow(2,4))

# max():最大值     min():最小值
print(max(12,34,6))

# π=====常量
print(math.pi)

"""


# 随机数
# 1.随机小数
# random()===[0,1)
print(random.random())

# 2.uniform()===随机生成自定义的小数
# round(总数,小数位数)=====四舍五入
print(round(random.uniform(5,12),3))


# 3.随机生成整数
# 1.randint()===包头包尾
print(random.randint(2,5))

# 2.randrange()====包头不包尾
print(random.randrange(2,5))

# 4.随机生成序列
# 1.choice()
print(random.choice(["向前","小寇","毛展","刘辉"]))

# 5.查看类型：type()     isinstance(变量名,类型)===判断类型
a = 100
print(type(a))
print(isinstance(a,str))

# 字符串  str====不可变数据类型
b = "hellopython"
# 1.切片
print(b[2:6])
print(b[4:])
print(b[:3])
print(b[:])
print(b[::-2])
print(b[::-1])
print(b[-4:-1])
print(b[3:-2])

# print(b[2])
# 字符串通过索引/下标修改值，会报错，所以str是不可变数据类型
# b[2]=999
# print(b)

# 字符串的转义：\   不发生转义：r
# \n:换行    \t:制表符(一个tab键)
print(r"四十九\t\t\thdsiu")


# 元组 tuple  ====不可变数据类型
c = (12,23)
c2 = (100)
c3 = ()
c6 = {}
c7 = set()
c4 = (1,2,"你好")
c5 = 1,2,3,"据我"
print(type(c),type(c2),type(c3),type(c4),type(c5))
print(bool(c3),c6,c7)


# 列表：list   =====可变数据类型
d = [1,2,3,"可以",99.9]
print(d[3:])
print(d[:4])
print(d[::-1])

# 通过索引修改值,由下可知列表是可变类型
d[1]="之你好好"
print(d)


# 字典：映射型的数据类型：一对一=====可变数据类型
# 1.字典的key是唯一的  2.键是不可变数据类型
e = {
	"a":100,
	"b":3.3,
	"c":[12,3,5],
	"a":88,
	# 键必须是不可变数据类型
	# ["e"]:9999
}
print(e)

# 通过key可以增加值/修改值
# 1.键存在会修改，键不存会添加
e["b"]="你好"
e["gg"]=300
print(e)


# 集合====无序不重复序列
# 1.set()====里面的值只能给一个
aa = set("helloy")
print(aa)

# 2.{}
bb = {"helo","baidu",9,9,8}
print(bb)


# 把下面列表的重复值去掉
ll = [1,1,2,34,77,5,34,2,89]
print(list(set(ll)))

