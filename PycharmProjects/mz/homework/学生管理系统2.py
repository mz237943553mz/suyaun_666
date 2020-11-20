from pymysql import *

class database():

    def __init__(self):
        self.conn = connect(user="root", password="123456", database="student_cor", port=3306, host="localhost",charset="utf8")
        self.cor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        self.cor.close()

    def excute_sql(self,sql="",parm=()):
        try:
            self.cor.execute(sql,parm)
            if "select" in sql:
                set=self.cor.fetchall()
                return set
            else:
                 self.conn.commit()
        except Exception as e:
            print("异常为", e)
            self.conn.rollback()
        finally:
            print("成功登陆", self.cor.rowcount, "条消息")
class login(database):

    # conn=connect(user="root",password="123456",database="student_cor",port=3306,host="localhost",charset="utf8")
    # cor=conn.cursor()

     #打印登陆菜单的静态方法
    @staticmethod
    def student_menu():
        menu="""
        ======================
	    请先注册/登录学生账号
	    [1].注册账号
	    [2].登录账号
	    [0].退出登录界面
	    ======================
        """
        print(menu)
        login_choice=int(input("请输入你要操作的序号"))
        return login_choice

      #注册账号
    def register(self):
         name = input("请输入用户名")
         pwd = input("请输入密码")
         parm=(name,pwd)
         sql="""
                 insert into control(name,pwd) values (%s,%s)
         """
         # try:
         #     self.cor.execute(sqal,parm)
         #     self.conn.commit()
         # except Exception as e:
         #     print("异常为",e)
         #     self.conn.rollback()
         # finally:
         #     print("成功登陆",self.cor.rowcount,"条消息")
         self.excute_sql(sql=sql,parm=parm)


      #登录账号
    def login(self):
        while True:
              name = input("请输入用户名")
              pwd = input("请输入密码")
              parm = (name, pwd)
              sql = """
                        select * from control where name=%s and pwd=%s
                       """
              # try:
              #     self.cor.execute(sqal, parm)
              #     result=self.cor.fetchall()
              #     if result:
              #         print("恭喜你登陆成功")
              #         return
              #     else:
              #         print("你输入有误，请从新输入")
              # except Exception as e:
              #     print("异常为", e)
              #     self.conn.rollback()
              # finally:
              #     print("成功登陆", self.cor.rowcount, "条消息")
              result=self.excute_sql(sql=sql,parm=parm)
              if result:
                  print("恭喜你，登陆成功")
                  return
              else:
                  print("你输入账号和密码有误")



class student(database):

    # conn = connect(user="root", password="123456", database="student_cor", port=3306, host="localhost", charset="utf8")
    # cor = conn.cursor()

    # 定义一个学生函数的逻辑：
    @staticmethod
    def students_func():
        menu="""
        **************************************************
			欢迎使用学生管理系统			
			[1]增加学生信息			
			[2]查看所有学生信息			
			[3]删除学生信息			
			[4]查看班级对应的学生			
			[5]退出学生管理系统
        **************************************************
            """
        print(menu)
        choice = int(input("请输入你要操作的序号"))
        return choice
    #[1]增加学生信息
    def add_stu(self):
    # 1学生序号2学生姓名3学生年龄4学生身高5学生性别6学生所在班级
    #     id=int(input('序号'))
        name=input('姓名')
        age=input('年龄')
        height=input('身高')
        gender=input('性别')
        class1=input('班级')
        parm=(name,age,height,gender,class1)
        sql="""
        insert into student1(name,age,height,gender,class1) values (%s,%s,%s,%s,%s)
        """
        # try:
        #     self.cor.execute(sqal, parm)
        #     self.conn.commit()
        # except Exception as e:
        #     print("异常为", e)
        #     self.conn.rollback()
        # finally:
        #     print("成功登陆", self.cor.rowcount, "条消息")
        self.excute_sql(sql=sql,parm=parm)

    #[2]查看所有学生信息
    def check_stu(self):
        sql = """
         select * from student1
               """
        # try:
        #     self.cor.execute(sqal)
        #     connect= self.cor.fetchall()
        #     print("学生序号 学生姓名 学生年龄 学生身高 学生性别 学生所在班级")
        #     for i in connect:
        #         print(i[0],i[1],i[2],i[3],i[4],i[5])
        # except Exception as e:
        #     print("异常为", e)
        #     self.conn.rollback()
        # finally:
        #     print("成功登陆", self.cor.rowcount, "条消息")
        content=self.excute_sql(sql=sql)
        print("学生序号 学生姓名 学生年龄 学生身高 学生性别 学生所在班级")
        for i in content:
            print(i[0],i[1],i[2],i[3],i[4],i[5])


    #[3]删除学生信息
    def del_stu(self):
        id=input('请输入你要删除的学生序号')
        sql="""
             delete from student1 where id=%s
             """
        # try:
        #     self.cor.execute(sqal,a)
        #     self.conn.commit()
        # except Exception as e:
        #     print("异常为", e)
        #     self.conn.rollback()
        # finally:
        #     print("成功登陆", self.cor.rowcount, "条消息")
        self.excute_sql(sql=sql,parm=id)
    #[4]查看班级对应的学生
    def check_class_stu(self):
        class1 = input('班级')
        sql = """
                select name from student1 where class1=%s
               """
        # try:
        #     self.cor.execute(sqal,class1)
        #     connect=self.cor.fetchall()
        #     for i in connect:
        #         print("学生为：",i[0])
        # except Exception as e:
        #     print("异常为", e)
        #     self.conn.rollback()
        # finally:
        #     print("成功登陆", self.cor.rowcount, "条消息")
        text=self.excute_sql(sql=sql,parm=class1)
        print(text)
        # for i in text:
        #     print("学生为：",i[0])
    #[5]退出学生管理系统
    def ex_stu(self):
        print("已退出学生管理系统")


#登陆注册的逻辑处理
def main():

    while True:
        a = login()
        num = a.student_menu()
        if num==1:
            a.register()
        elif num==2:
            a.login()
            main2()
        elif num==3:
            quit()
        else:
            print("您输入有误，请再次输入：")

def main2():
    while True:
        b=student()
        num2=b.students_func()
        if num2==1:
            b.add_stu()
        elif num2==2:
            b.check_stu()
        elif num2==3:
            b.del_stu()
        elif num2==4:
            b.check_class_stu()
        elif num2==5:
            exit()
        else:
            print("输入有误，请重新输入")

main()
main2()


