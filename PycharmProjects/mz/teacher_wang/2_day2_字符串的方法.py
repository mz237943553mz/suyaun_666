#coding=utf-8

a = "hellopython"
# 字符串函数

# 一.查找与替换
# 1.startswitch():从头找，
print(a.startswith("h"))
print(a.startswith("j"))

# 2.endswitch():从尾找
print(a.endswith("k"))

# find():根据字符串里的内容打印索引值，若没有返回-1=====总左找
print(a.find("o"))

# rfind():根据字符串里的内容打印索引值，若没有返回-1=====总右找
print(a.rfind("o"))

# index():根据内容返回索引值,若找不到会报错
print(a.index("h"))
# print(a.index("m"))

# 替换：replace("旧字符串","新字符串")
print(a.replace("python","世界"))

# split():分割====将一个字符串分割成多个
a2 = "my name is wsy"
# print(a2)
print(a2.split(" "))

# join():连接====将两个或两个以上的字符串连接成一个
a3 = ["您","进去哦","nkj"]
aa = "*".join(a3)
aa = "_".join(a3)
print(aa,type(aa))

# isdigit():查看字符串里是否只有数字
print("shjk78".isdigit())
print("34567".isdigit())

# isalpha():查看字符串里是否只有字母
print("gduws".isalpha())
print("hi87".isalpha())

#isalnum():查看字符串里是否由数字/字母组成
print("6789".isalnum())
print("dhwu987".isalnum())
print("sh*7".isalnum())

# count():统计字母出现的次数
print("bhwbub".count("b"))