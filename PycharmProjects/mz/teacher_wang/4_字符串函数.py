#coding=utf-8

# 一、查找与替换
# 1.startswith(str):是否以"str"开头
a = "hellopython"
print(a.startswith("l"))

# 2.endswith(str):是否以"str"结尾
print(a.endswith("n"))

# 3.find():根据子字符串查找是否存在；存在为索引值，找不到为-1====默认从左找
print(a.find("o"))
print(a.find("9"))
# 根据指定位置查找
print(a.find("o",5,10))

# 4.rfind():默认从右找
print(a.rfind("o"))

# 5.replace(旧字符串,新字符串):替换
print(a.replace("hello","你好"))

# 6.split():分割,一定有内容
b = "my name is wsy"
print(b.split("a"))
print(b.split(" "))


# 7.join():连接,把多个字符串连接成一组字符串
c = ["nn","aa","sdd"]
print("*".join(c),type("*".join(c)))
print("_".join(c))

# 8.capitalize()将字符串的第一个字母变成大写,其他字母变小写。
print("hdhFG".capitalize())

# 9.center(总宽度,[填充字符]):居中
# 注意：center若不写填充字符时，默认以空格填充
print("你好".center(10))
print("看看".center(10,"*"))

# 10.count() 方法用于统计字符串里某个字符出现的次数
print("hello".count("l",3,5))


# 11.format():格式化函数===通过{}
# 写法1：注意：{}里若不给定索引,{}个数不能超过字符串个数
print("{}{}{}".format("你哈","python","数据"))

# 写法2：{下标}{下标}
print("{0}{1}{0}{1}{2}".format("你哈","python","数据"))

# 12.isdigit()如果字符串只包含数字则返回 True 否则返回 False.
print("6734244".isdigit())
print("hsdu786".isdigit())

# 13.index()====根据内容返回索引值
print("hskjh".index("j"))

# 14.isalnum()
# 方法检测字符串是否由字母和数字组成

print("hs78".isalnum())
print("hsdui ".isalnum())

# 15.isalpha()
# 方法检测字符串是否只由字母组成。
print("dhu".isalpha())
print("dhu78".isalpha())

# 16.isspace()
# 方法检测字符串是否只由空格组成。
print(" ".isspace())

# 17.max()    min()
# 字符串进行比较大小，通过ASCII码表===数字的===大写字母====小写字母
print(max("897678hdijJ"))

# zfill()
print("gdhj".zfill(3))
print("gss".zfill(8))