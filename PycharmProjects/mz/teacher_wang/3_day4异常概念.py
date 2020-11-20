#coding=utf-8



print("今天天气很好")
name=123
try:

	f=open("123.txt","r",encoding="utf8")
	print(name)

except (FileNotFoundError,NameError) as e:
	print("异常为:",e)
	# pass

print("交急哦五")

# a=f.read()
# print(a)



