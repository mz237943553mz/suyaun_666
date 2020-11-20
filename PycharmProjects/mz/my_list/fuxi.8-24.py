# num1=int(input('请输入一个数字'))
# # num2=int(input('请输入一个数字'))
# # a=num1+num2
# # b=num1-num2
# # print(a)
# # print(b)
"""
### 一、输出商品列表，用户输入序号，显示用户选中的商品。

商品   li = ["手机", "电脑", "鼠标垫", "游艇" ]

a. 允许用户添加商品

b. 用户输入序号显示内容

**结果执行如下：**

```
请输入您想加入的商品:冰箱
商品现有 ['手机', '电脑', '鼠标垫', '游艇', '冰箱']
请输入序号：2
电脑
```
"""
"""
li=["手机","电脑","鼠标垫","游艇"]
goods=input("请输入您想加入的商品")
order1=int(input("请输入序列号"))
li.append(goods)
print(li)
print(li[order1])
"""



### 二、转换

# a. 将字符串 s = "alex"转换为列表
# s = "alex"
# print(list(s))
# """
# b. 将字符串s = "alex"转换为元组
# s = "alex"
# print(tuple(s))
# c. 将列表li = ["alex", "seven"]转换为元组
# li = ["alex", "seven"]
# print(tuple(li))
# d.将元组 tu = ("Alex", "seven")转换为列表
# tu = ("Alex", "seven")
# print(list(tu))
"""
# ### 三、写代码，有如下列表，li=[“alex”,“eric”,“rain”],按照要求实现每一个功能
li=["alex","eric","rain"]
# a.计算列表长度并输出
print(len(li))

# b.列表中追加元素"seven",并输出添加后的列表
li.append("seven")
print(li)
# c.请在列表中的第一个位置插入元素"Tony"，并输出添加后的列表
li.insert(0,"tony")
print(li)
# d.请修改列表中的第2个位置的元素为"Kelly"，并输出修改后的列表
li[1]="kelly"
print(li)
# e.请删除列表中的元素"eric",并输出删除后的列表
del li[1]
print(li)
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除后的列表
print(li[1])
del li[1]
print(li)
# g.请删除列表中的第3个元素，并输出删除后的列表===用不同的方法，不能和上面的方法重复
# del li[2]
# print(li)
# li.pop()
# print(li)
li.remove("seven")
print(li)
# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
del li[1:4]
print(li)
# i.请将列表所有的元素反转，并输出反转后的列表
li=["alex","eric","rain"]
li.reverse()
print(li)
# ### 四、写代码，有如下列表，li=["hello","seven",["mon",["h","kelly"],"all",123,446]],按照要求实现每一个功能
#
# a.请根据索引输出"kelly"
li=["hello","seven",["mon",["h","kelly"],"all",123,446]]

print(li[2][1][1])
# ### 五、列举布尔值是False的所有值
print(bool(0),bool([]),bool({}),bool(()),bool(""),bool(None))
"""
# # ### 六、列举10个字符串函数
#
# list1=[]
# print(list1.startswith("1"))
#
#


"""
# 1.根据用于指定月份，打印该月份所属的季节。  3～5月为春季，6～8月为夏季，9～11月为秋季
month=int(input("请输入指定的月份"))
if month>=3 and month<=5:
    print("春季")
elif month>=6 and month<=8:
    print("夏季")
elif month>=9 and month<=11:
    print("秋季")
elif month in (1,2,12):
    print("冬季")
else:
    print("输入超出范围")

i=int(input("请输入月份"))
if i in (3,4,5):
    print("春季")
elif i in (6,7,8):
    print("夏季")
elif i in (9,10,11):
    print("夏季")
elif i in (12,1,2):
    print("冬季")
else:
    print("错误")
"""
# 2.比较胜负：用电脑随机生成1到3分别代表石头,剪刀,布；和用户进行比较胜负
# """1=石头 2=剪刀 3=布
# 石头胜剪刀
# 剪刀胜布
# 布胜石头
# """
# num1=int(input("请输入一个数字"))
# for i in range(1,4):
#     if num1==i:
#         print("平手")
#         break
#     elif num1>i:
#         print("失败")
#         break
#     else:
#         print("胜利")

# 3.判断闰年?
# 用户输入年份year, 判断是否为闰年?  input()
#  提示year能被4整除但是不能被100整除 或者 year能被400整除, 那么就是闰年;     %
years=int(input("请输入一个年份"))
if years%4==0 and years%100!=0:
    print("闰年")
elif years%400==0:
    print("世纪闰年")
