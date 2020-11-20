#coding=utf-8

import re


# 匹配单个字符
# .：任意一个字符
# a = re.match("hel..","helljl")
# print(a.group())
a=re.match("bdgcsg..","bdgcsgjnksd")
print(a.group())

# 匹配[ ]中列举的字符
# 不含数字4
# a = re.match("长江[0-35-9]号","长江4号")
# print(a.group())
# a = re.match("长江[0-35-9][0-9]号","长江89号")
# print(a.group())

# \d:   0-9
# a = re.match("\d\d","400")
# print(a.group())
a=re.match("\d\d","2000")
print(a.group())

# \w:  匹配单词字符，即a-z、A-Z、0-9、_
# a = re.match("\w\w","_A")
# print(a.group())
a=re.match("\w\w","_a")
print(a.group())


# 匹配多个字符
# *:可有可无
# a = re.match("\w*","你6fshHDI你第几")
# print(a.group())
a=re.match("\w*","您7gugu不干净")
print(a.group())

# +：前一个字符出现1次或者无限次
a = re.match("\w+","k6fshHDI你第几")
print(a.group())

# ? :要么1次要么没有
a = re.match("\d?","678fshHDI你第几")
print(a.group())

# {m} 匹配前一个字符出现m次   ，必须为{m次}
a = re.match("\d{8}","67879838878fshHDI你第几")
print(a.group())


# {m,n}
a = re.match("\d{4,8}","6788111179fshHDI你第几")
print(a.group())

# 匹配下面的变量名是否有效
names = ["name1", "_name", "2_name", "正则"]

for i in names:
	ret = re.match("[a-zA-Z_]+[a-zA-Z_0-9]*",i)
	if ret:
		print("%s变量名符合条件"%ret.group())
	else:
		print("%s变量名不符合条件"%i)


# 开头^b    结尾b$
a = re.match("^h\w*9$","hjosjfis9")
print(a.group())


# 匹配分组：
# |    匹配左右任意一个表达式
# a = re.match("\d$|100|600","100")
# print(a.group())
a=re.match("\d$|200|100","1")
print(a.group())


ret = re.search(r"\d+", "阅读次数为9999")
print(ret.group())

ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)

ret = re.sub(r"\d+", '998', "python = 997")
print(ret)

ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print(ret)