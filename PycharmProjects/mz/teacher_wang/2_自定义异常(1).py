#coding=utf-8

"""
try:
	发生错误的代码
	raise Exception("nsji")
except Exception as e:
	print(e)
else:
	不发生异常时,才去执行
finally:
	无论是否有异常,都会执行
"""
class Myerror(Exception):
	# def __init__(self):
	# 	print("必须为纯数字")

	def func(self):
		print("必须为纯数字")
	def func2(self):
		print("输入正确")

num = input("请输入数字")
try:
	if not(num.isdigit()):
		# 实例化过程
		raise Myerror().func()
	else:
		raise Myerror().func2()

except Exception as e:
	print("异常为",e)

