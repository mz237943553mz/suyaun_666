#coding=utf-8

a = "hellopython"

# 查找与替换
# 1.startswith()
print(a.startswith("l"))

# 2.endswith()
print(a.endswith("n"))

# 3.find():从左往右找
print(a.find("l"))
print(a.find("l",3,9))

# 4.rfind():从右找
print(a.rfind("o"))

# 5.replace(旧的,新的)
print(a.replace("python","旧的"))

# split():一个字符串分割成多个
a = "今天 是个 好天气"
print(a.split(" "))

# join():连接/合并
b = ["12","间接","记"]
print("*".join(b))

# join()连接时，里面的元素必须为字符串类型
c = ["11","23","56","7"]
print(" ".join(c))

# 将字符串的第一个字母变成大写,其他字母变小写。
d = "dnhGGYGU"
print(d.capitalize())

# center():居中
# 注意：center填充字符不写，默认是空格
print("你好".center(10,"*"))

# count():计数
a = "hello"
print("hello".count("l",3,5))
print(len(a))

# format()格式化函数
print("{0}{0}{2}{1}".format("你好","时间","python"))
print("{0}{1}{2}".format("cds","sd","csad"))
# isdigit():是否只包含纯数字
print("1234".isdigit())
print("dgwu67".isdigit())

# isalnum():包含数字或字母
print("78dw".isalnum())

# isalpha() :只有字母
print("njd".isalpha())
print("dsgu7".isalpha())

# isspace():是否只含有空格
print("  ".isspace())
print("  gh ".isspace())

# zfill()
# print("abc".zfill(6))




