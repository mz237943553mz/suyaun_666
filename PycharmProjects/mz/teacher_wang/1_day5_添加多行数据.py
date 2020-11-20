#coding=utf-8

# 1.导包
# from pymysql import *
from pymysql import *
# 2.创建连接对象connect()
# conn = connect(user="root",password="root",database="user",port=3306,host="localhost",charset="utf8")
conn=connect(user="root",password="123456",database="user",port=3306,host="localhost",charset="utf8")
# 3.创建游标对象===对数据库进行操作的
# sor = conn.cursor()
sor=conn.cursor()
# 添加多行数据id | name | sex  | math | english

# sql = ((0,"你好","女",96,80),(0,"nn","男",56,98))
sql=((0,"吼吼","女",177),(0,"林东","男",189))
# try:
try:
	# 4.增加信息
	# sor.executemany("insert into score values(%s,%s,%s,%s,%s)",sql)
	sor.executemany("insert into score values(%s,%s,%s,%s,%s) ",sql)

	# 5.提交数据
	# conn.commit()
	conn.commit()
except Exception as e:
	# print("异常为:",e)
	print("异常为",e)
	# 回滚数据
	# conn.rollback()
	conn.rollback()

finally:

	# print("成功添加",sor.rowcount,"记录")
    print("成功过添加",sor.rowcount,"记录")




# 6.关闭游标对象
sor.close()

# 7.关闭连接对象
conn.close()

