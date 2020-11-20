#coding=utf-8
import random
import time
from pymysql import *

class Database():
	# 类属性
	create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	def __init__(self):
		self.conn = connect(user="root",password="root",database="world",host="localhost",port=3306,charset="utf8")
		self.cor = self.conn.cursor()

	# 对数据库的操作做封装方法
	def execute_sql(self,sql="",cont=()):
		try:
			self.cor.execute(sql,cont)
			if "select" in sql:
				ret = self.cor.fetchall()
				return ret
			else:
				self.conn.commit()
		except Exception as e:
			print("异常为",e)
			self.conn.rollback()
		finally:
			print("成功记录为",self.cor.rowcount)

	# 对用户名和密码的判断
	def panduan(self):
		while True:
			card = input("请输入您的卡号")
			pwd = input("请输入您的密码")
			sql = """
			select * from user where card_number=%s and password=%s
			"""
			parm = (card,pwd)
			result = self.execute_sql(sql=sql,cont=parm)
			if result:
				# print("您的余额为%s"%result[0][6])
				# break
				return result
			else:
				print("您输入的用户名或密码错误")

# 银行类
class Bank(Database):

	# 菜单
	@staticmethod
	def menu():
		print("#" * 50)
		print("               欢迎使用银行                       ")
		print("               功 能 如 下:                      ")
		print("#" * 50)
		print("*         开户（1）            查询（2）            *")
		print("*         取款（3）            存款（4）            *")
		print("*         改密（5）            销户（6）            *")
		print("*                    退出(0)                      *")
		print("*" * 50)
		choice = int(input("请输入您要执行的功能:"))
		return choice

	# 开户
	def open_user(self):
		# 户主
		name = input("请输入您的名字：")
		# 身份证
		identity_card = input("请输入您的身份证号：")
		# 电话号
		phone = input("请输入您的电话号码：")
		# 随机生成8位卡号
		card_number = "".join([str(random.randint(1,9)) for i in range(8)])
		# 密码
		pwd = input("请输入您的密码：")
		# 存额
		#current time
		create_time=self.create_time

		while True:
			sum_cash = input("请输入要存的金额")
			if sum_cash.isdigit() and int(sum_cash)>=0:
				break
			else:
				print("只能输正整数的数字!")
		# 创建时间

		parm = (name,identity_card,phone,card_number,pwd,sum_cash,self.create_time)
		# name | identity_card | phone | card_number | password | sum_cash | create_time
		sql = """
			insert into user(name,identity_card,phone,card_number,password,sum_cash,create_time) values (%s,%s,%s,%s,%s,%s,%s)
		"""
		self.execute_sql(sql=sql,cont=parm)

	# 查询余额
	def show(self):
		ret = self.panduan()
		print("您的查询余额为%s"%ret[0][6])

	# 取款
	def qu_kuan(self):
		ret = self.panduan()
		while True:
			cash = input("请输入取款金额")
			if cash.isdigit() and int(cash)>0:
				if int(cash)>ret[0][6]:
					print("您的取款金额大于%s总金额"%ret[0][6])
				else:
					cash_after = ret[0][6]-int(cash)
					# print(cash_after)
					user_id = ret[0][0]
					parm=(cash_after,user_id)
					sql='''
						update user set sum_cash = %s where id = %s
					'''
					self.execute_sql(sql,parm)
					# 插入记录
					sql='''
						insert into access(user_id,type,cash,create_time) values (%s,%s,%s,%s)
					'''
					#current time
					c_time = self.create_time
					parm_01 = (user_id,0,cash,c_time)
					self.execute_sql(sql,parm_01)
					print("取款%s成功"%cash)
			else:
				print("您输入的取款金额必须为正整数!")

		# 下面修改user
	def cun_kuan(self):
		#登陆判断
		ret = self.panduan()
		while True:
			cash = input("请输入存款金额")
			if cash.isdigit() and int(cash)>0:
				cash_after = ret[0][6]+int(cash)
				# print(cash_after)
				user_id = ret[0][0]
				parm=(cash_after,user_id)
				sql='''
					update user set sum_cash = %s where id = %s
				'''
				self.execute_sql(sql,parm)
				print('您成功存款%s'%cash)
				# 插入记录
				sql='''
					insert into access(user_id,type,cash,create_time) values (%s,%s,%s,%s)
				'''
				#current time
				c_time = self.create_time
				parm_01 = (user_id,1,cash,c_time)
				self.execute_sql(sql,parm_01)
				print("存款%s成功"%cash)
				break
			else:
				print("您输入的存款金额必须为正整数!")
	def modify(self):
		result=self.panduan()
		if result:
			a=input("请输入你的新密码")
			id=result[0][0]
			tuple_a=(a,id)
			sql="""
			update user set password=%s where id=%s
			"""
			self.execute_sql(sql=sql,cont=tuple_a)
			print("恭喜您的密码修改成功")

	def del_user(self):

		ru=self.panduan()
		if ru:
			mi=(ru[0][0])
			sql="""
				delete from user where id=%s
			"""
			self.execute_sql(sql,mi)
			print("销户成功")


def main():
	while True:
		u1 = Bank()
		choice_u1=u1.menu()
		if choice_u1 == 1:
			u1.open_user()
		elif choice_u1 ==2:
			u1.show()
		elif choice_u1 ==3:
			u1.qu_kuan()
		elif choice_u1 ==4:
			u1.cun_kuan()
		elif choice_u1 ==5:
			u1.modify()
		elif choice_u1 ==6:
			u1.del_user()
		elif choice_u1 ==0:
			return
main()