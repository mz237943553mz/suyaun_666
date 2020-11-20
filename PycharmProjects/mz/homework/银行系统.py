from pymysql import *
import time
import random

class database():
    create_time = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    def __init__(self):
        self.conn = connect(user="root", password="123456", database="world", port=3306, host="localhost",charset="utf8")
        self.cor = self.conn.cursor()

    # def __del__(self):
    #     self.conn.close()
    #     self.cor.close()

    def execute_sql(self,sql="",parm=()):
        try:
            self.cor.execute(sql,parm)
            if "select" in sql:
                set=self.cor.fetchone()
                return set
            else:
                 self.conn.commit()
        except Exception as e:
            print("异常为", e)
            self.conn.rollback()
        finally:
            print("成功登陆", self.cor.rowcount, "条消息")

    def method(self):
        while True:
            card = input("请输入您的卡号")
            pwd = input("请输入您的密码")
            sql = """
        	select * from user where card_number=%s and password=%s
        	"""
            parm = (card, pwd)
            result = self.execute_sql(sql=sql, parm=parm)
            if result:
                return result
            else:
                print("您输入的用户名或密码错误")

class Login(database):

    # 打印菜单
    @staticmethod
    def Bank_menu():
        menu="""
        ####################################
                    欢迎使用银行
                    功 能 如 下：
        *      开户（1）      查询（2）     *
        *      取款（3）      存款（4）     *
        *      改密（5）      销户（6）     *
        *              退 出 （0）          *
        ####################################
        """
        print(menu)
        choose=int(input("请输入你要执行的操作序号"))
        return choose

    #开户
    def open_account(self):
        name=input("请输入你的名字：")
        identity_card=input("请输入您的身份证号：")
        phone=input("请输入您的电话号码：")
        card_number=("".join([str(random.randint(1,9)) for i in range(8)]))
        password = input("请输入您的账户密码：")

        while True:
            sum_cash=input("请输入你的预存金额：")
            if sum_cash.isdigit() and int(sum_cash)>=0:
                break
            else:
                print("请输入正整数")

        parm=(name,identity_card,phone,card_number,password,sum_cash,self.create_time)
        sql="""
        insert into user(name,identity_card,phone,card_number,password,sum_cash,create_time) values (%s,%s,%s,%s,%s,%s,%s)
        """
        self.execute_sql(sql=sql,parm=parm)

     #查询

    def Check_bank(self):
        ret=self.method()
        print("您的查询余额为%s"%ret[6])

    #取款
    def draw_money(self):
        result=self.method()
        if result:
            print("恭喜你登陆成功")
        while True:
            draw1_money = input("请输入您要取款的金额")
            if draw1_money.isdigit() and int(draw1_money)>=0:
                if int(draw1_money)>result[6]:
                    print("您取款的金额大于%s存款金额"%result[6])
                else:
                    remain = result[6]-int(draw1_money)
                    id=result[0]
                    parm = (remain,id)
                    sql="""
                    update user set sum_cash=%s where id=%s 
                    """
                    self.execute_sql(sql=sql,parm=parm)
                    print("您的取款金额为%s" % draw1_money)
                    break
                    user_id = result[0]
                    type = 1
                    cash = int(draw1_money) - result[6]
                    parm = (user_id, type, cash, self.create_time)
                    sql = """
                        insert into access(user_id, type,cash,create_time) values (%s,%s,%s,%s)
                        """
                    self.execute_sql(sql=sql, parm=parm)
            else:
                print("你输入的金额必须为正整数")

    def save_account(self):
        result=self.method()
        while True:
            save1_account = input("请输入存款金额")
            if save1_account.isdigit() and int(save1_account)>=0:
                total_moeny=int(save1_account)+result[6]
                id=result[0]
                parm = (total_moeny, id)
                sql = """
                    update user set sum_cash=%s where id=%s
                     """
                self.execute_sql(sql=sql, parm=parm)
                user_id = result[0]
                type = 0
                cash = int(save1_account) + result[6]
                parm = (user_id, type, cash, self.create_time)
                sql = """
                    insert into access(user_id,type,cash,create_time) values (%s,%s,%s,%s)
                     """
                self.execute_sql(sql=sql, parm=parm)
                print("恭喜您存款成功金额为%s" % save1_account)
                break
            else:
                print("你输入的金额必须为正整数")

        #改密
    def exchange_pwd(self):
        result=self.method()
        if result:
            new_pwd=input("请输入您的新密码")
            id=result[0]
            parm=(new_pwd,id)
            sql="""
                update user set password=%s where id=%s 
                """
            self.execute_sql(sql=sql, parm=parm)
            print("恭喜您修改密码成功")
    def Cancel_account(self):
        result=self.method()
        if result:
            id=result[0]
            sql="""
            delete from user where  id=%s
            """
            self.execute_sql(sql,id)
            print('销户成功')
def main():
    while True:
        a=Login()
        num=a.Bank_menu()
        if num==1:
            a.open_account()
        elif num==2:
            a.Check_bank()
        elif num==3:
            a.draw_money()
        elif num==4:
            a.save_account()
        elif num==5:
            a.exchange_pwd()
        elif num==6:
            a.Cancel_account()
        elif num==0:
            quit()
        else:
            print("您输入有误")
main()








