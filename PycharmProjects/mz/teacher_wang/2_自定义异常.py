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
class Myerror():
	def error(self):

		print("请输入纯数字",)




num = input("请输入数字")
try:
	if not(num.isdigit()):
		raise Myerror()
except Myerror as e:
	print(e)

