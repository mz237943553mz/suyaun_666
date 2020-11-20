stuall = []
#定义菜单
def caidan():
    print('='*30)
    print('           学生管理系统')
    print('         1.添加学生信息')
    print('         2.删除学生信息')
    print('         3.修改学生信息')
    print('         4.显示所有学生信息')
    print('         0.退出系统')
    print('=' * 30)
    xuanze=int(input('请输入操作的序号：'))
    return xuanze
# caidan()
def add():
    message={}
    name_new=input("姓名:")
    sex_new=input("性别:")
    tel_new=input("电话号码:")
    message.update(name=name_new, sex=sex_new, tel=tel_new)
    stuall.append(message)
    print(message)
def display():
    for i in stuall:
        print(i)
def main():
    while True:
        x=caidan()
        if x==1:
            add()
        elif x==4:
            display()
main()