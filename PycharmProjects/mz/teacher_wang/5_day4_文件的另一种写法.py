#coding=utf-8

# f = open("123.txt","r",encoding="utf8")
# a=f.read()
# print(a)
# f.close()


with open("123.txt","r",encoding="utf8") as f:
	a = f.read()
	print(a)
