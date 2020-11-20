#coding=utf-8

# 打开/创建文件====（文件名,模式,编码格式）
# file = open("123.txt","w",encoding="utf8")
file = open ("123.txt","w",encoding="utf8")

# 2.写内容
file.write("hellopython\n世节\n你好")
# file.write("世界")
# file.write("你好")

# 3.关闭文件
file.close()

