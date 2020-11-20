#coding=utf-8

"""
if ...  elif ...else
"""

num = int(input("请输入一个数字"))
guess = 100
if num>guess:
	print("您输入过大....")
elif num<guess:
	print("您输入过小...")
else:
	print("恭喜你，猜对了")

