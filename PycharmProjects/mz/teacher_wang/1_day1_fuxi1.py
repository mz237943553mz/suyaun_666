#coding=utf-8

# python PPT2


# 六个双引号除了多行注释外，还有原样输出的作用
name = """
# 输出
print("过端午够")

name = "小王"
age = 18
height  = 189.9
print("我的姓名为,年龄为:",(name,age))
print("我的姓名为%s,年龄为%d"%（name，age)

# 格式化输出 %s:字符串   %f:浮点型  %d:整型
print("我的姓名为%s,身高为%.2f,年龄为%d"%(name,height,age))

# 输入 input()  #输入的类型是字符串类型
a = int(input("请输入你的年龄"))
print(a,type(a))
b = int(input("请输入你的年龄"))
print(b,type(b))
print(a+b)
"""
print(name,type(name))



# 变量的作用以及类型
# 1.变量的作用：用来存储数据   写法：变量名=值
# 2.变量的命名规则：2.1:字母、数字、下划线组成    2.2不能以数字开头
"""
name_stu  _stuage_  name  4sdh_hh（x）  代_hsi（x）   hds_ch&^%di-（x）
_stuage_ = "间接"
print(_stuage_)
"""

# 3.数据类型:
# 3.1数值型：int   float  complex()   bool()
# a,b = 100,99.8
# print(a,type(a),b,type(b))

# bool()：True   False
# 布尔类型为false的值有哪些
# print(bool(0),bool([]),bool(()),bool(set()),bool({}),bool(None),bool(""))

a = []
if a:
	print("为假")
else:
	print("为真")

# 驼峰式命名法：====方便识别
# 学生系统：student_system  学生添加:stu_add

# 注意：变量名不能以关键字重名
# 1.查看关键字
# 1.1导包
import keyword
# 1.2kwlist()====去查看关键字
print(keyword.kwlist)


# python能在一行执行多条语句：在后面加;====但不建议这样使用
# print("shu");print("jjj")

# end的使用
print("nihao",end=" ")
print("hello")



