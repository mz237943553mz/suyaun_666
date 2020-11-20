#coding=utf-8

# 运算符：
# 1.定义：7+9  +：运算符    a = 10    =:运算符

# 运算符的分类：
# 1.算术运算符:+  - *  /:正常的除 (小数点)  //:整除(取整数)    %:取余   **
print(9/2)
print(9//2)
print(9%2)
print(2*6)
print(2**3)

# 2.比较运算符:True:真      False:假
# >   <   >=  <=  !=  ==
print(9>2)
print(3==6)
print(5!=9)



# 3.逻辑运算符
# and:与===两方都为真就为真，一方为假就为假====一般结合if语句使用
# 在数字里，除0外，其余数字都为真
print(10 and 20)
print(33 and 5)
print(0 and 5)


# or
# or:或===有一方为真就为真,两方为假才为假
print(99 or 5)
print(7 or 3)
print(78 or 0)
print(0 or 0)

# not
# not():非====取反：只有两个值True和False
print(not(78 or 8))
print(not(34 and 0))

# 4.成员运算符
# in:在   not in：不在
a = [1,2,3,"你好",99]
print(8 in a)
print(99 in a)
print( 8 not in a)

# 5.赋值运算符
# =  +=  -=  *=  /=
a = 10
b = 5
c = 0

# =+
# a=a+c
a += c
print(a)

# -=
# a=a-b
a-=b
print(a)

# *=


