#coding=utf-8

from pymysql import *


# 定义一个数据库的类：
class Database():

	# 定义一个初始化方法，创建连接对象和游标对象
	def __init__(self):
		# 实例属性
		self.conn = connect(user="root",password="root",database="sys_students",port=3306,host="localhost",charset="utf8")

		self.cur = self.conn.cursor()

	# 进行封装方法，把公共的操作封装到方法里：
	def execute_sql(self,sql="",parm=()):
		try:
			self.cur.execute(sql,parm)
			# 查询：fetchall()    增删改：commit()
			if "select" in sql:
				ret = self.cur.fetchall()
				return ret
			else:
				self.conn.commit()
		except Exception as e:
			print("异常为",e)
			self.conn.rollback()
		finally:
			print("成功记录为:",self.cur.rowcount)




# 创建一个登录的类
class Login(Database):

	# # 创建类属性：创建连接对象和游标对象
	# conn = connect(user="root",password="root",database="sys_students",port=3306,host="localhost",charset="utf8")
	#
	# cur = conn.cursor()

	# 打印登录菜单的静态方法
	@staticmethod
	def login_menu():
		menu = """
		======================
			请先注册/登录学生账号
			[1].注册账号
			[2].登录账号
			[0].退出登录界面
			======================
		"""
		print(menu)

		login_choice = int(input("情输入您要执行的操作"))
		return login_choice

	# 注册账号
	def register(self):

		name = input("请输入您要注册的账号")
		pwd = input("请输入您要注册的密码")

		parm = (name,pwd)

		sql = """
		insert into user(user_name,password) values (%s,%s)
		"""

		# try:
		# 	self.cur.execute(sql,parm)
		# 	self.conn.commit()
		# except Exception as e:
		# 	print("异常为：",e)
		# 	self.conn.rollback()
		# finally:
		# 	print("成功记录为",self.cur.rowcount,"条")

		self.execute_sql(sql=sql,parm=parm)


	# 登录账号
	def login(self):

		while True:
			name = input("请输入您要注册的账号")
			pwd = input("请输入您要注册的密码")

			parm = (name,pwd)

			sql = """
				select * from user where user_name=%s and password=%s
			"""

			# try:
			# 	self.cur.execute(sql,parm)
			# 	result = self.cur.fetchall()
			# 	if result:
			# 		print("恭喜您,登录成功")
			# 		return
			# 	else:
			# 		print("您输入的账号或密码错误,请重新输入")
			#
			# except Exception as e:
			# 	print("异常为：",e)
			# 	self.conn.rollback()
			# finally:
			# 	print("成功记录为",self.cur.rowcount,"条")

			result = self.execute_sql(sql=sql,parm=parm)
			if result:
				print("恭喜你,登录成功")
				return
			else:
				print("账号或密码错误,请重新登录")


class Student():

	# 菜单的静态方法：
	pass


# 登录注册的逻辑处理
def login_func():
	while 1==1:
		l1=Login()
		a_choice = l1.login_menu()
		if a_choice==1:
			l1.register()
		elif a_choice==2:
			l1.login()
			# 转本去调用学生的主函数
			students_func()
		elif a_choice==0:
			quit()
		else:
			print("您输入有误!")




# 定义一个学生函数的逻辑：
def students_func():
	pass


login_func()
