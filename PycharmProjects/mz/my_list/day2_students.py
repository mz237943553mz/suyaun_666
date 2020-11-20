#coding=utf-8


"""
1.增加学生信息
2.查看所有学生信息
3.查看单一(根据姓名查对应学生的信息)
4.删除所有
5.根据序号删除单一
6.修改学生信息
0.退出学生系统
"""

# 1.打印菜单的函数  menu()
def menu():

	print("="*40)
	print("\t\t\t欢迎使用学生管理系统\t\t\t")
	print("\t\t\t1.增加学生信息\t\t\t")
	print("\t\t\t2.查看所有学生信息\t\t\t")
	print("\t\t\t3.查看单一(根据姓名查对应学生的信息)\t\t\t")
	print("\t\t\t4.删除所有\t\t\t")
	print("\t\t\t5.根据序号删除单一\t\t\t")
	print("\t\t\t6.修改学生信息\t\t\t")
	print("\t\t\t0.退出学生系统\t\t\t")
	print("="*40)
	# 输入执行的功能
	choice = int(input("请输入您要执行的功能"))
	return choice
# menu()


# 总数据===用来存放所有的学生信息
stu_list = []

# 可变类型===列表/字典
# {"name":"狼王","sex":"男"....}
# 2.增加学生信息
def add_stu():
	stu_dict = {}
	add_name = input("请输入您要增加的姓名")
	add_sex = input("请输入您要增加的性别")
	add_age = input("请输入您要增加的年龄")
	add_phone = input("请输入您要增加的电话")
	# stu_dict["name"]=add_name
	stu_dict.update(name=add_name,sex=add_sex,age=add_age,phone=add_phone)

	# 把字典里的信息添加到列表里
	stu_list.append(stu_dict)
	# print(stu_list)
# add_stu()


# 查看所有学生信息
def show_all():
	print("学生信息如下")
	print("序号 姓名 性别 年龄 电话")
	# [{"name":"老王","sex":"女"},{"name":"老王","sex":"女"}]
	a = 1
	for i in stu_list:
		print(a,i["name"],i["sex"],i["age"],i["phone"])
		a+=1


# 定一个进行逻辑处理的函数
def main():
	while True:
		a = menu()
		if a==1:
			add_stu()
		elif a==2:
			show_all()

		elif a==0:
			quit()

main()

