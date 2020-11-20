#coding=utf-8

"""
for 循环的完整格式
for i in 序列:
	循环的执行语句
else:
	执行语句
"""

# int 整型
a = 1234
# 浮点型  float
b = 12.9
# 字符串  str
c = "自负是"
# 列表  list
d = [1,2,4,"彻底结束"]
# 元组  tuple
e = (23,65,99)
# 字典 dict
f = {
	"a":999,
	"b":"你哈",
	"c":123
}
print(f.items())

# 1.遍历字符串类型
# for i in c:
# 	print(i)

# 2.遍历列表===右下可知，列表是可以遍历的
# for i in d:
# 	print(i,end="*")
# for i in e:
# 	print(i)

# 遍历字典  items():获取字典的键和值
# for a,b in f.items():
# 	print(a,b)

# 遍历整型/浮点型====如下可知，不能遍历
# for i in a:
# 	print(i)
# =====================
# for i in (1,2,3,4):
# 	print(i)


# 通过range()去遍历1,2,3,4,5
# range(5):起始位置从0,切记包头不包尾的
# range(5,10):5,6,7,8,9
# range(5,11,2):====2：部长
# for i in range(5,11,2):
# 	print(i)


# break:直接跳出循环
# a = "hellopyth"
# for i in a:
# 	if i == "o":
# 		break
# 	else:
# 		print(i)



# continue:退出本次循环继续执行下一次的循环

a = "hellopyth"
for i in a:
	if i == "o":
		# pass:保证代码的完整性
		continue
	else:
		print(i)
else:
	print("循环你好")





