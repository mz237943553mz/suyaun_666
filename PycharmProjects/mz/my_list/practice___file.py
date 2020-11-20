# 打开，关闭文件
# f=open("test1.txt","a",encoding="utf8")
# r:以只读的方式打开文件。文件的指针将会放在文件的开头。这是默认模式
# f.write("zaiganma ")
# f.close()
# 读数据
# f=open("test1.txt","rb")
# f.write("zaiganma ")
# a=f.read(4)
# f.seek(2,1)

# lines=f.readlines()
# print(lines)
# position=f.tell()
# print(position)

# os模块
# 修改
import os
# os.rename("test.txt","mz.txt")
# 删除
import os
# os.remove("mz.txt")
# 创建文件夹
# import  os
# os.mkdir("毛展")
# 获取当前目录
# import os,sys
# print(os.getcwd())
# print(sys.argv)
# os.chdir(r"C:\Users\Administrator\PycharmProjects\mz\lianxi")
# os.remove("123.txt")
os.rmdir(r"C:\Users\Administrator\PycharmProjects\mz")