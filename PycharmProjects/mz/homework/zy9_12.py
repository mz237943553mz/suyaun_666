##### 1、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。实参如下:x='12', y='345', c='bywgh'
# def check(x, y, c):
#     m=(x,y,c)
#     for i in m:
#         if len(i)>2:
#             print(i[0],i[1])
# x="12"
# y="345"
# c="bywgh"
# check(x,y,c)

##### 2、从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# a=input("请输入一个字符串")
# a.upper()
# w=open("test.txt","w",encoding="utf8")
# w.write(a.upper())
# w.close()

##### 3、有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
# a=input("请输入一行字母：")
# b=input("请输入一行字母：")
# c=[a,b]
# d=[]
# for i in c:
#     for n in i:
#        d.append(n)
#        d.sort()
#        "".join(d)
# m=open("c.txt","w",encoding="utf8")
# m.write("".join(d))
# m.close()
##### 4、随机输入一个八位以内的整数，求它是几位数，然后逆序打印其他数字

# 操作结果如下：
#
# ```
# 请输入一个八位以内的整数：456789
# 这是一个6位数
# [‘9’, ‘8’, ‘7’, ‘6’, ‘5’, ‘4’]
# ```

# a=input("请输入一个八位以内的整数：")
#
# d=[]
# for i in a:
#     for n in i:
#         d.append(n)
#         d.reverse()
# print("这是一个",len(d),"位数")
# print(d)





##### 5、写函数，用户输入一组字符串，统计字符串中有几个字母，几个数字，几个空格，并返回结果字母有几个，数字有几个，空格有几个
# def str1(str):
#     digitals=0
#     alpha=0
#     space=0
#     for i in str:
#         if i.isdigit():
#             digitals+=1
#         elif i.isalpha():
#             alpha+= 1
#         elif i.isspace():
#             space+= 1
#     print(digitals,alpha,space)
# str = input("请输入一组字符串")
# str1(str)

##### 6、写一个函数：设计一个重量转换器，输入以'g'为单位的数字后返回换算成'kg'的结果

# 代码运行结果如下：
#
# > 请输入一个克数:500
# > 你输入的克数是0.50kg
# def kli(a):
#     print("你输入的克数是：",a/1000,"Kg")
# a=int(input("请输入的克数是："))
# kli(a)

##### 7、输入一个人名，如果字典中有这个人输出人名对应的城市。

# 字典如下：places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
#
# 执行结果如下：
#
# > 请输入名字李四
# > ['九寨沟', '张家界', '张++']
# places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
# for i in places:
#     a=input("请输入一个人名")
#     if i==a:
#         print(places[i])
#         break
#     elif i==a:
#         print(places[i])
#         break
#     else:
#         print("查无此人")
#         break