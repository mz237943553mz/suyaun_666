import os
funFlag = int(input("请输入数字:"))
os.chdir(r'C:\Users\Administrator\PycharmProjects\mz\homework')
dirList = os.listdir(r'C:\Users\Administrator\PycharmProjects\mz\homework')
for name in dirList:
	if funFlag == 1:
		os.rename(name ,"new"+name)
	elif funFlag == 2:
		os.rename(name, name.replace("new",""))










