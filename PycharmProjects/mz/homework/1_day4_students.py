#coding=utf-8


# 总列表：用来存储学生的所有信息
sum_stu=[]

# 定义一个打印菜单的函数
def menu():
	print("="*40)
	print("\t\t\t学生管理系统\t\t\t")
	print("\t\t\t1.添加学生信息\t\t\t")
	print("\t\t\t2.显示所有学生信息\t\t\t")
	print("="*40)
	choice = int(input("请输入操作的序号："))
	return choice

# menu()


# 定义一个添加学生信息
def add_stu():
	new_dict = {}
	new_name = input("请输入您要添加的学生姓名")
	new_sex = input("请输入您要添加的学生性别")
	new_phone = input("请输入您要添加的学生电话")

	# 添加学生信息
	new_dict.update(name=new_name,sex=new_sex,phone=new_phone)

	# 把字典里的内容放到总的列表
	sum_stu.append(new_dict)
	print(sum_stu)

# add_stu()


# 操作逻辑处理的函数====主函数
def main():

	while True:
		a=menu()
		if a==1:
			add_stu()
		elif a==0:
			break
		else:
			print("输出错误")

main()


