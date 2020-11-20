#coding=utf-8

"""
模块：
1.import 包 as 别名                调用：别名.函数名()
2.from 包名 import *              调用：函数名()
3.from 包名 import 函数名 as 别名        调用：函数名/别名()
4.if __name__ == '__main__': 不让第三方查看自己调用的结果
5.locals():不能进行修改变量，以字典的形式输出
global: (1).globals()["变量名"]=值：修改全局变量的值    (2)global 局部变量：修改作用域
"""
import 包 as 别名 调用：别名.函数名（）
from 包名 import *  调用：函数名()
from 包名 import 函数名 as 别名 调用：函数名/别名()
if __name__ == '__main__':不让第三方查看自己调用的结果
locals() 不能进行修改变量，以字典形式输出
global:（1）.globals() [“变量名”]=值：修改全局变量的值  （2）global 局部变量:修改作用域

"""
文件：
1.文件三部操作：open()   read()/write()   close()
2.读的三个函数：
read(num):读全部/根据字节读取内容
readline():读一行
readlines():以列表的形式读取全部

# 定位/偏移：tell()/seek():0:   1:   2:
os的模块：
1.rename()    getcwd()     chdir()   remove()   rmdir()  listdir()

"""
文件：
read(num):读全部/根据自己读取内容
readline():读一行
readlines():以{列表}的形式读取全部

定位tell()
偏移seek(): 0从文件开始处,1从当前位置,2从文章末尾

os 模块
1.rename(旧名字,新名字) 修改文件名
2 getcwd() 获取当前目录
3.chdir() 改变工作目录
4.remove() 删除文件
5.rmdir() 删除文件夹
6 listdir() 获取目录列表


