#coding=utf-8

num = input("请输入一组字符串")

try:
	if not (num.isdigit()):
		raise Exception("您输入的不是数字")

except Exception as e:
	print(e)

