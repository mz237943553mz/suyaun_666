# ### 一、输出商品列表，用户输入序号，显示用户选中的商品。
#
# """
# 商品   li = ["手机", "电脑", "鼠标垫", "游艇" ]
#
# a. 允许用户添加商品
#
# b. 用户输入序号显示内容
#
# **结果执行如下：**
# """
#
# """
# 请输入您想加入的商品:冰箱
# 商品现有 ['手机', '电脑', '鼠标垫', '游艇', '冰箱']
# 请输入序号：2
# 电脑
# """
#
# """
# 1.
# li = ["手机", "电脑", "鼠标垫", "游艇" ]
# a= input("请输入您想加入的一个商品")
# if a not in li:
# li.append(a)
# print(li)
# 2.
# b= int(input("请输入序号"))-1
# print(li[b])
# """
#
# """
# ### 二、转换
#
# a. 将字符串 s = "alex"转换为列表
#
# b. 将字符串s = "alex"转换为元组
#
# c. 将列表li = ["alex", "seven"]转换为元组
#
# d.将元组 tu = ("Alex", "seven")转换为列表
# """
# """
# 1.
# s = "alex"
# print(list(s))
# 2.
# s = "alex"
# print(tuple(s))
# 3.
# li = ["alex", "seven"]
# print(tuple(li))
# 4.
# tu = ("Alex", "seven")
# print(list(tu))
# """
# """
# ### 三、写代码，有如下列表，li=[“alex”,“eric”,“rain”],按照要求实现每一个功能
#
# a.计算列表长度并输出
#
# b.列表中追加元素"seven",并输出添加后的列表
#
# c.请在列表中的第一个位置插入元素"Tony"，并输出添加后的列表
#
# d.请修改列表中的第2个位置的元素为"Kelly"，并输出修改后的列表
#
# e.请删除列表中的元素"eric",并输出删除后的列表
#
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除后的列表
#
# g.请删除列表中的第3个元素，并输出删除后的列表===用不同的方法，不能和上面的方法重复
#
# h.请删除列表中的第2至3个元素，并输出删除元素后的列表
#
# i.请将列表所有的元素反转，并输出反转后的列表
# """
# """
# 1.
# li=["alex","eric","rain"]
# print(len(li))
# 2.
# li.append("seven")
#  print(li)
# 3.
# li.insert(0,"Tony")
# print(li)
# 4.
# li[1]="Kelly"
# print(li)
# 5.
# del li[1]
# print(li)
# 6.
# print(li[1])
# del li[1]
# print(li)
# 7.
# del li[2]
# print(li)
#
# li.pop()
# print(li)
#
# li.remove("rain")
# print(li)
# 8.
# del li[1:3]
# print(li)
# 9.
# li.reverse()
# print(li)
# """
# """
# ### 四、写代码，有如下列表，li=["hello","seven",["mon",["h","kelly"],"all",123,446]],按照要求实现每一个功能
#
# a.请根据索引输出"kelly"
#
# ### 五、列举布尔值是False的所有值
#
# ### 六、列举10个字符串函数
# """
# """
# 1.
# li=["hello","seven",["mon",["h","kelly"],"all",123,446]]
# print(li[2][1][1])
# # 2.
# print(bool(0),bool(""),bool(None),bool([]),bool({}),bool())
# capitalize()
# find()
# upper()
# lower()
# find()
# index()
# join()
# split()
# max()
# min()
# rstrip()
# """
# """
# ### 1、使用while循环和for循环,求1～100之间所有偶数之和(至少一种方法)
# num=0
# for i in range(1,101):
#     if i%2==0:
#         num+=i
# print(num)
# """
# """
# ### 2、 使用while循环和for循环输出1 2 3 4 5 6     8 9 10(至少一种方法)
# """"""
# for i in range(1,11):
#      if i==7:
#         continue
#      print(i)
# """
# """
# ### 3、使用for循环,求1-100的所有数的和
# num=0
# for i in range(1,101):
#     num+=i
# print(num)
#
# """
# """
# ### 4、输入1到100之间的偶数:
# for i in range(1,101):
#     if i%2==0:
#      print(i)
# """
# ### 5、用户登陆（三次机会重试），用户名为:abc；密码为123
# """
# for i in range(1,4):
#     name = input("请输入用户名")
#     password = int(input("请输入密码"))
#     if name=="abc" and password == "123":
#         print("用户成功登录")
#         break
#     else:
#         print("用户登录不成功")
#         continue
# else:
#     print("账号冻结")
# """
#
#
# ### 六、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#
#
#
# ### 七、输入三个整数x,y,z，请把这三个数由小到大输出。
# """
# num1=int(input("输入一个整数"))
# num2=int(input("输入一个整数"))
# num3=int(input("输入一个整数"))
# list=[num1,num2,num3]
# list.sort()
# print(list)
# """
#
# ### 八、将一个列表的数据复制到另一个列表中。使用两种方法
# """
# list1=["fghdf","12432","毛展","rain"]
# list2=["bool","2379","恋人","sunny"]
#
# a=list1+list2
# print(a)
#
# list1.append(list2)
# print(list1)
# """
# ##### 列表如下所示list1 = [11,22,33,44]
# """
# ### 九、按相反的顺序输出列表的值。a = ['one', 'two', 'three']
# a = ['one', 'two', 'three']
# a.reverse()
# print(a)
# """
# """
# ### 十、有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，将小于66值保存至第二个key的值中。
# set=[11,22,33,44,55,66,77,88,99,90]
# dic={}
# dic1=[]
# dic2=[]
# for i in set:
#     if i<66:
#        dic1.append(i)
#     else:
#        if i>66:
#         dic2.append(i)
# dic.update(aaa=dic1,kk=dic2)
# print(dic)
# """
# """
# a = {
#     # "a":"ttyu",
#     # "b":99
# }
#
# # a.update({"cc":9999})
# # print(a)
#
# # a.update(a=100,hh="你好")
# # print(a)
# """
# """
# ## **一、输入一个人名，如果字典中有这个人输出人名对应的城市。**
#
# 字典如下：places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
#
# 执行结果如下：
#
# > 请输入名字李四
# > ['九寨沟', '张家界', '张++']
# >
# >
#
# places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
# num1=input("请输入名字")
# for name in places:
#     if num1==name:
# """
# """
# ### 二、求阶乘：
#
# 请输入一个数字：5
# 1*2*3*4*5=120
# 5的阶乘为：120
# """
"""
num1=int(input("请输入一个数字"))
sum1=1
if num1<0:
    print("负数没有阶乘")
elif num1==0:
    print("0的阶乘为0")
else:
    for i in range(1, num1+1):
        sum1*=i
    print("%d的阶乘为%d"%(num1, sum1))
"""

### 三、从键盘输入一个字符串，将小写字母都转换成大写字母，将字符串以列表的形式输出：
"""
str1="edfhuiwekowe"
str1.upper()
print(list(str1))
"""
# ### 四、随机输入一个八位以内的整数，求它是几位数，然后逆序打印其他数字
"""
num1=(input("请随机输入一个八位数"))
print(len(list(num1)))
print(tuple(reversed(num1)))
"""

 ### 五、猜年龄游戏

# 要求：
#     1.允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# 2.猜的数字给定要求：1----18之间的整数（随机产生1到18的数字）
"""
import random
random.randrange(1,19)
a=random.randrange(1,19)
for i in range(1,6):
    guess_age=int(input("请说出你猜想的年龄"))
    if guess_age > a:
        print("你猜的年龄大了")
    elif guess_age <a:
        print("你猜的年龄小了")
    elif guess_age == a:
        print("恭喜你猜对了")
"""


# ### 六、打印一个矩形

# ```
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# ```
"""
i=1
while i<=6:
    j=1
    while j<=6:
        print("*   ",end="")
        j+=1
    print("\n")
    i+=1
"""
"""
i=1
for i in range(1,7):
    j=1
    for j in range(1,7):
        print("* ",end="") 
    print("\n")
    """
# ### 七、打印一个直角三角形
#
# ```
# *
# **
# ***
# ****
# *****
# ******
# ```
"""
for i in range(1,7):
    for j in range(i):
        print("*   ",end="")
    print("\n")
# 八、打印一个等腰三角形
"""
#
# ```
#       *
#     * * *
#   * * * * *
# * * * * * * *
# ```
#


for i in range(1,5):
    for space in range(5-i):
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print("\n")

