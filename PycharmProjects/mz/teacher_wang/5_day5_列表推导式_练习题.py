#coding=utf-8

import random
# print(random.randint(1,9))

# [表达式 一个/多个for循环以及if语句 ]

# 1--10的平方
# a=[]
# for i in range(1,11):
# 	if i%2==0:
# 		a.append(i*i)
# print(a)


# a=[i*i for i in range(1,11) if i%2==0]
# print(a)


example2 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# for i in example2:
# 	for j in i:
# 		if j%2==0:
# 			print(j*j)
# a=[j*j for i in example2 for j in i if j%2==0]
# print(a)


"""
# 随机生成8为数字  randint():包头包尾    randrange()：包头不包尾
# print(random.randint(1,9))
a=[]
for i in range(8):
	a.append(str(random.randint(1,9)))
print("".join(a))
"""

a="".join([str(random.randint(1,9)) for i in range(8)])
print(a)

