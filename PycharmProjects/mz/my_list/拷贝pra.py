# # # try:
# #     print("drgv.txt",'r')
# #     print("__kjojds__")
# # # except SyntaxError:
# # #     pass
# # num=1
# # try:
# #     print(num)
# #     print(nvv)
# # except (NameError) as b:
# #     print(b)
#
# try:
#     print("----a----")
#     print(num)
#     with open("123.text","r"):
#         pass
#     print("----b----")
#
#
# except:
#     pass
# else:
#     print("jdi")
# finally:
#     print("ncdsj")
#

# try:
#     a=input("请输入一个数数字")
#     if not(a.isdigit()):
#         raise Exception("必须是数字")
# except Exception as e:
#     print(e)

# 拷贝
# file=input("请输入文件名:")
# num=file.rfind(".")
# new=file[:num]+"拷贝"+file[num:]
# old_file=open(file,"r",encoding="utf8")
# new_file=open(new,"w",encoding="utf8")
# a=old_file.readlines()
# for i in a:
#    new_file.write(i)
# old_file.close()
# new_file.close()
# 文件复制-重命名

import os
flage = int(input("请输入数字:1.增加; 2.删除"))
path=r"C:\Users\Administrator\PycharmProjects\mz\my_list\new_python.py"
file=os.listdir(path)
for i in file:
   if flage==1:
      new_name="新建"+i
   elif flage==2:
      num=len("新建")
      new_name=i[num:]
      print(new_name)
   os.rename(path+i,path+new_name)




