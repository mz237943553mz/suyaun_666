#coding=utf-8

import re

a = "<span>hellopython</span>"

ret = re.match("<[a-z]*>\w*</[a-z]*>",a)
print(ret.group())

# (分组)   \num:引用分组匹配到的内容
# a = "<span>hellopython</spancnhj>"
# ret = re.match(r"<([a-z]*)>\w*</\1>",a)
# print(ret.group())

"""
b = ["<html><h1>python</h2></html>","<html><h1>python</h1></html>"]
for i in b:
	ret = re.match(r"<([a-z]*)><(\w*)>\w*</\2></\1>",i)
	if ret:
		print("%s符合条件"%ret.group())
	else:
		print("%s不符合条件"%i)
"""

# 仅返回第一个匹配到的内容
a = re.search("\d+","hello999python887")
print(a.group())

# findall():能匹配到的所有
a = re.findall("\d+","hello999python887")
print(a)

# sub():替换
a = re.sub("\d+","100","hello999python887")
print(a)


# split():分割
a = re.split(":| ","info:xiaoZhang 33 shandong")
print(a)


