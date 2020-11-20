def menu():
    print("="*40)
    print("\t\t\t学生信息管理系统\t\t\t")
    print("\t\t\t1.增加学生信息\t\t\t")
    print("\t\t\t2.查看所有学生信息\t\t\t")
    print("\t\t\t3.查看单一（根据姓名查看对应学生信息）\t\t\t")
    print("\t\t\t4.删除所有学生信息\t\t\t")
    print("\t\t\t5.根据序号删除单一学生\t\t\t")
    print("\t\t\t6.修改学生信息\t\t\t")
    print("\t\t\t7.退出学生系统\t\t\t")
    print("="*40)
    choice =int(input("请输入您要执行的命令"))
    return choice


stu_list = []
def add_stu():
    stu_dict={}
    add_name=input("请输入您要增加的姓名")
    add_sex=input("请输入您要增加的性别")
    add_age=input("请输入您要增加的年龄")
    add_phone=input("请输入您要增加的电话")
    stu_dict.update(name=add_name,sex=add_sex,age=add_age,phone=add_phone)
    stu_list.append(stu_dict)


def shou_all():
    print("学生信息如下")
    print("序号 姓名 性别 年龄 电话")
    a=1
    for i in stu_list:
        print(a,i["name"],i["sex"],i["age"],i["phone"])
        a+=1


def main():
    while True:
        a=menu()
        if a==1:
            add_stu()
        elif a==2:
            shou_all()
        elif a==0:
            quit()
main()











