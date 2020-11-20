#coding=utf-8

# 文件名：123.txt

# 新文件重命名：123拷贝.txt
# find():从左    rfind(".")=3:123.txt


# 123.txt
old = input("请输入要拷贝的文件")
num=old.rfind(".")
# 新文件重命名
new=old[:num]+"拷贝"+old[num:]
# 打开旧文件
old_file=open(old,"r",encoding="utf8")
# 打开新文件
new_file = open(new,"w",encoding="utf8")
con = old_file.readlines()


for i in con:
	new_file.write(i)

old_file.close()
new_file.close()









