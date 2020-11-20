
"""
#字符串
a="dfq656 hkd0"
#查询
print(a.startswith(a))
print(a.endswith(a))
print(a.find("k",5,9))
print(a.rfind("q",1,7))
print(a.index("f",0,7))
#替换/计数
print(a.replace("df","python"))
print(a.count("6"))
#切分/连接
print(a.split(" "))
print("*".join(a))
#检查字符串...
print("231".isdigit())
print(" ".isspace())
print("6gj".isalnum())
print("dwq".isalpha())
#格式化
print("{}{}{}".format(1,2,3))
print("dewd".zfill(8))

"""
"""
#字典
b={
    "sex":"男",
    "name":"毛展",
     "list":{1,2,3,4,5}
}
#输出键
b.keys()
print(b.keys())
#输出值
b.values()
print(b.values())
#输出键值对
print(b.items())
#查询
b.get("sex")
print(b.get("sex"))

b.setdefault("age")
print(b.setdefault("age"))
print(b)

#update 1.查询出来返回值 2.没有查询出来增加
b.update(sex="中性")
print(b.update(sex="中性"))
print(b)

#删除
#1.根据内容删除
b.pop("sex")
print(b.pop("sex"))
#2.默认输出最后一个popitm()
b.popitem()
print(b.popitem())
#3.删除整个字典del

"""
"""
#列表
list=[1,2,3,34,"你看好","bhfdjsih"]
#append在列表后追加一个元素
list.append("hcdj")
print(list)
#extend在列表后面追加一个列表
list.extend("vh")
print(list)

# count 计数
print(list.count(2))

#index
list.index(2)
print(list.index(2))

#insert
list.insert(3,"你好")
print(list)

#remove根据内容删除
list.remove(2)
print(list)

#sort
list1=[1,3,45,7,34,]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

#pop
list1.pop()
print(list1)

#def 函数名（参数）:
    # 函数体
    # return()  结束函数，返回一个值给调用方
#调用函数
# 函数名（）
"""

# def dd(a):
#     a=[1,2,3]
#     return a
# b=4
# print(dd(b))
#必需参数
# def printme(str):
#     print(str)
#     return
# printme()
#关键字参数
# def printme(str,age):
#     print(str,age)
#     return
# printme(age=18,str="python")
#默认参数
# def printinfo(name,age=30):
#     print(name,age)
#     return
# printinfo(name="刘德华")
#不定长参数
# def function(*args,**kargs):
#
#     print(args,kargs)
#
# function(2,3,4,4,5,a=1,b=6)

#匿名函数
# lambda 参数：表达式
# sum=lambda a,b:a+b
# print(sum(265,78))

#深浅拷贝

import copy
#浅拷贝




#深拷贝
import file

file1=open(r"C:\Users\Administrator\Desktop\abc.txt","r",encoding="utf8")
for i in file1:
    print(i,end=" ")