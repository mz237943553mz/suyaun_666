#coding=utf-8

"""
/ :整除  //：取整   %：取余
is：身份运算符===判断对象是否引用一致   =:赋值   ==：值相等
"""

"""
# 1.算术运算符

# +  -   *  /:正常的除法   //:整除   %:取余  **:乘方
print(9/2)
print(9//2)
print(9%2)
print(2**2)
print(2*2*2)
print(pow(2,3))

# 比较运算符=====true   false
# >  >=  <   <=   ==    !=
print(8>=10)

# 逻辑运算符====经常和if语句结合使用
# and   or   not
# 1.and:左右两边都为真时，才为true；一方为假就为假
# 注意：光是输出打印时，and左右两边都为真，返回右边的值
print(10 and 20)
print(0 and 56)

# 2.or:有一方为真就为真；左右两边都为假时，才为假；
print(0 or 99)
print(65 or 96)
print(0 or "gshj")
if 0 or 99:
	print("真")
else:
	print("假")
"""

# 赋值运算符
# =  +=  -=  *=  /=
a = 5
b = 20
# a=a+b
a+=b
print(a)

a-=b
print(a)


# 成员运算符
# in:在    not in:不在
print("n" in ("nh","hsu"))
print("n" in "nhk")
print("gj" not in "hwui")

# is:用于判断对象是否引用一致
a = "10"
b = "dhiue"
c = "10"
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)


# r/R:原始字符串
print(R"hfesd\t\t\thkj")

