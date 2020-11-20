#coding=utf-8

# 1.数学函数
"""
import math
print(math.ceil(11.234))
print(math.floor(12.34))
import random
print(random.randrange(4))
print(random.randint(1,3))
print(random.random())
print(random.uniform(2,4))
a=[1,23,3]
print(random.choice(a))
"""
"""
# 2.字符串函数
a="125645675"
print(a.find("6"))
print(a.rfind("3"))
#print(a.index("3"))
print("12sjufgdb".startswith("1"))
print("12sjufgdb".endswith("b"))
print("123456e".isdigit())
print("nsjhg123g".isalpha())
print("12$52gdgc".isalnum())
print("  1  ".isspace())
print(a.replace("125","888"))
b=["gdye","hgdyu","gdfgeey"]
print("*".join(b))
print(a.split("5"))
"""


'''
# 3.元组和列表
a = [1,2,6,5,3,9]
print(a.index(3))
print(tuple(a))
#增加
a.append(33)
print(a)
a.insert(2,"aa")
print(a)
a.extend([11,22])
print(a)
#删
a.remove("aa")
print(a)
del a[2]
print(a)
a.pop(0)
print(a)
#排序
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)'''

"""
# 4.字典
stu={'name':'zhangsan',"sex":'男',"age":'28'}
print(stu)
print(stu.items())
print(stu.keys())
print(stu.values())
stu.update(name="张三")
print(stu)
stu.update(score=98)
print(stu)
print(stu.get("name"))
stu.pop('age')
print(stu)
stu.popitem()
print(stu)
stu.setdefault("成绩")
print(stu)
stu.clear()
print(stu)
a = stu.copy()
print(a)
"""

"""
# 字符串 count  center  format   title   upper   lower
# pow()  round()
a = "heHDJSKkj"
# print(a.capitalize())
# pop()

"""
'''
1.编写一个名为collatz()的函数,它有一个名为number的参数
如果参数是偶数,那么collatz()就打印出number//2
如果number是奇数,collatz()就打印3*number+1
'''
# def collatz(number):
# 	if number%2==0:
# 		print(number//2)
# 	elif number%2!=0:
# 		print(3*number+1)
# a=int(input("请输入您要操作的数字"))
# collatz(a)
"""用匿名函数求多个数的和"""
a=lambda i,j:i+j
print(a(2,3))
b=lambda *args:sum(args)
print(b(2,3,4,5,6))






