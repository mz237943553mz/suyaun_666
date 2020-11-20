#将一个整数转化为二进制

# num1=int(input("请输入一个整数"))
# list=[]
# while num1>0:
#     a=num1%2
#     list.append(str(a))
#     b=num1//2
#     num1=b
# reversed(list)
# s="".join(list)
# print(s)
"""
#将一个整数转化为八进制

num1=int(input("请输入一个整数"))
list=[]
while num1>0:
    a=num1%8
    list.append(str(a))
    #将整型转换为字符串
    b=num1//8
    num1=b
reversed(list)
s="".join(list)
print(s)

"""

#将一个整数转化为十六进制

num1=int(input("请输入一个整数"))
list1=[]
list2=[]
chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
while num1>0:
    yushu=num1%16
    list1.append(str(yushu))#将整型转换为字符串
    b=num1//16
    num1=b
    if yushu>=10:
        yushu=num1%16


    #  c=chaDic.keys(i)
    #  print(c)
    # b=num1//16
    # num1=b
   
reversed(list)

print(list)


# # 1、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
"""
def printlt(arg):
    list2=[]
    for i in range(len(arg)):
        if i%2==1:
            list2.append(arg[i])
        else:
            pass
    return list2
#调用函数
list3=[11,23,344,55,654]
a=printlt(list3)
print(list3)
print(a)
"""
# 2、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
"""
def printslt(arg):
    list=[]
    for i in range(len(arg)):
        if i >=5:
            print("输入的长度大于5")
        else:
            pass
#调用函数
a=[232,43,54,54,6,4,31]
printslt(arg=a)
"""
"""
# 3、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def printslt(arg):
    for i in range(len(arg)):
        if i <=2:
          continue
        else:
          print(arg[0:2])
          return arg[0:2]
#调用函数
a=[232,43,54,54,6,4,31]
print(printslt(arg=a))
"""

#  4、写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
""""
def printfunction(str):
    str=input("从键盘输入字符串")
    digital = 0
    alpha=0
    space=0
    others=0
    for i in str:
       if i.isdigit():
            digital+=1
       elif i.isalpha():
            alpha+=1
       elif i.isspace():
            space+=1
       else:
        others+=1
    print(digital, alpha, space, others)
    return digital, alpha, space, others

#调用函数
a="gsh  7689h %^ jgbu8"
printfunction(str=a)

"""
"""
# 5、写函数，接收两个数字参数，返回比较大的那个数字。
def canshu(num1,num2):
    if num1>num2:
        print(num1)
    else:
        print(num2)
#调用函数
a=3
b=6
canshu(a,b)
"""

# 6、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {“k1”: “v1v1”, “k2”: [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
"""
def dict1(dic):
    for i in dic.keys():
        a=len(dic[i])
        if a>2:
            b=dic[i][0:2]
            dic[i]=b
        else:
            pass
    print(dic)
#调用函数
dic={"k1": "v1v1", "k2": [11,22,33,44],"jsdfwj":"力霸天"}

dict1(dic)
"""





# 7、写函数，此函数只接收一个参数且此参数必须是列表数据类型，
# 此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。
# 例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# a="kkkpythoniskkgoodkk"
# print(a.split("k"))
# s="www.baidu.com"
# v1,v2,v3=s.split(".",2)
# print(v1)
# print(v2)
# print(v3)
# print(s.split(".",2)[0])
#
# s="http://www.baidu.com/luoru/p/57001.html"
# print(s.split("//")[1].split(".")[1])
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# # print("dict['name']:",dict['Name'])
# # dict['Age']=8

# print("dict['age']:",dict['Age'])
# print("dict['school']:",dict['school'])
# print("--------------------")
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict.clear()
# print(dict)
# dict.copy()
# print(dict)

print(dict.get())