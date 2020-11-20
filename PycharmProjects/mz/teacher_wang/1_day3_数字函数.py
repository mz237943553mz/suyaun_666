#coding=utf-8

import math

import random

# del :直接删除对象
a = [100,13,3]
del a[0]
print(a)

# 1.ceil():上入整数
print(math.ceil(12.567))

# 2.下舍整数floor()
print(math.floor(12.053))

# max()  min()

# pow():次方
print(pow(2,3))

# 1.随机生成整数：====导randrom
# randint():包头包尾
print("随机生成1-3之间的整数",random.randint(1,3))


# randrange():包头不包尾
print(random.randrange(22,89))


# 随机生成小数
# randrom():[0,1)
print(random.random())

# unifrom():给定范围
print(round(random.uniform(12,55),3))

# 随机生成序列
# print(random.choice(["仵向前","寇旭柯","毛展","李锦龙"]))
# 整数的范围
print(random.choice(range(2,10)))


# 打印数学常量
print(math.pi)

# 格式化输出  %s   %.2f   %d


# 六个双引号除了多行注释外，还有跨多行显示
a = """
bgsu 
hei\t\t\tcgsdu
cdb
多数
"""
print(a,type(a))



print(round(random.uniform(12,55),3))


while True: pass

