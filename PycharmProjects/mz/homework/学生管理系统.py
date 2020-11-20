for i in range(3):
    admin=input("请输入用户名")
    keywords=input("请输入密码")
    if admin=="abc" and keywords=="123":
        print("登陆成功")
        break
    elif admin!="abc" or keywords!="123":
        print("用户名或者密码输入有误")
        continue
else:
    print("账户锁定稍后再试")
stuall=[]
def menu():
    print("="*40)
    print("\t\t\t\t学生管理系统\t\t\t\t")
    print("\t\t\t\t1.添加学生信息\t\t\t\t")
    print("\t\t\t\t2.删除学生信息\t\t\t\t")
    print("\t\t\t\t3.修改学生信息\t\t\t\t")
    print("\t\t\t\t4.显示所有学生信息\t\t\t\t")
    print("\t\t\t\t5.c查看单一\t\t\t\t")
    print("\t\t\t\t6.根据序号删除单一\t\t\t\t")
    print("\t\t\t\t0.退出系统\t\t\t\t")
    print("="*40)
    choose=int(input("请输入操作的序号："))
    return choose
def add():
    dic={}
    # input("1.添加学生信息")
    name_old=input("姓名:")
    sex_old=input("性别:")
    tel_old = input("电话:")
    dic.update(name=name_old,sex=sex_old,tel=tel_old)
    dic.update()
    stuall.append(dic)
    print(stuall)
def delect():
    # input("2.删除学生信息")
    stuall.clear()
    print("信息已删除")
def modify():
    # [{},{}]
    xiu = int(input("请输入要修改的学生序号"))-1
    dic = {}
    name_new = input("姓名:")
    sex_new = input("性别:")
    tel_new = input("电话:")
    dic.update(name=name_new, sex=sex_new, tel=tel_new)
    dic.update()
    stuall.append(dic)
    stuall[xiu]=dic
    print(stuall)

def show():
    # input("4.显示所有学生信息")
    print(input("序号 姓名 性别 电话"))
    n = 1
    for i in stuall:
        print(n, i["name"], i["sex"],i["tel"])
        n += 1
# def exit1():
# #     b=input("退出系统")
# #     if b==0:
# #         print("退出")
# #         break
def find1():
    c = int(input("请输入学生姓名"))
    for i in stuall:
        if c==i["name"]:
            print(i)
def delc():
    b = int(input("请输入要删除的学生序号")) - 1
    stuall.pop(b)
    print(stuall)
def main():
    while True:
        a = menu()
        if a == 1:
            add()
        elif a == 2:
            delect()
        elif a == 3:
            modify()
        elif a == 4:
            show()
        elif a == 5:
            find1()
        elif a == 6:
            delc()
        elif a==0:
            exit()
main()












