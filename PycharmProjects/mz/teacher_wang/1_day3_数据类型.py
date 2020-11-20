#coding=utf-8

# int  float  bool
# 布尔类型里，0   ()   []   {}   set()  None  ""
print(bool("chdei"),bool((1,2,3)),bool([]),bool(0))

# 2.查看类型：type()   isinstance()===True   False


# 3.转义\n:换行   \t:制表符tab键====不发生转义r

# 4.python一行代码实现两个变量之间的交换

a1 = 100
a2 = 200
# 拆包
a1,a2=a2,a1
print(a1,a2)
# 4.1 一个值赋值给多个变量
a=b=c=100
print(a,b,c)

# 4.2多个变量赋值给多个值
a,b,c=12,13,14
print(a,b,c)

# 运算符
# 1.算术运算符
# +   -   *  /:正常除   //:取整   %:求余   **:乘方

# 比较运算符====结果只有true   false
# >   >=   <   <=  ==    !=

# 赋值运算符
# =   +=   -=   *= ....

# 逻辑运算符
# and:
print(bool(12 and 0))

print(34 and 12)


# or
print(12 or 34)


# not===true  false
print(not (12 or 34))


# 成员运算符
# in   not in
print(12 not in {1,2,3})


# 身份运算符
# is  is not

# 整数:[-5,256]
a = 300
b = 100
c = 300
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)


# 一行代码比较两个数字的大小
# a= 3
# b = 8
# small = ("小于" if a < b else "大于")
# print(small)

a=3
b=4
small=("小于" if a<b else "大于")
print(small)








