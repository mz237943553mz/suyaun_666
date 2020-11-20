#coding=utf-8
import os
import time



# 批量在文件名前加前缀
import os

# 用来控制增加和删除的
funFlag = int(input("请输入数字:1.增加; 2.删除")) # 1表示添加标志  2表示删除标志

# 具体路径D:\Pycharmprojects\day01\xiugai
folderName = r'D:\Pycharmprojects\day01\xiugai\\'
# 获取指定路径的所有文件名字
dirList = os.listdir(folderName)


# 遍历输出所有文件名字
for name in dirList:
	# print(name)
	if funFlag == 1:
		newName = '新建' + name
	elif funFlag == 2:
		num = len('新建')
	# 		newName = name[num:]
	# 	# print(newName)
	# 用于修改文件名的
	os.rename(folderName+name, folderName+newName)










