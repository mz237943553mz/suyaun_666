#coding=utf-8

# 1.导包
from pymysql import *

# 2.连接对象
conn = connect(user="root",password="root",port=3306,database="user",host="localhost",charset="utf8")

# 3.游标对象
cor = conn.cursor()

# 4.写sql语句

try:
	sql = """
		select * from score
	"""
	cor.execute(sql)

	# fetchall():查询所有记录
	# content = cor.fetchall()

	# fetchmany():查询多个,若fetchmany()里没有num,默认打印1条记录
	# content = cor.fetchmany(4)

	# 只拿一条记录
	content = cor.fetchone()
	print(content)
	# print("id 姓名 性别 数学 英语")
	# for i in content:
	# 	print(i[0],i[1],i[2],i[3],i[4])

except Exception as e:
	print("异常为:",e)
	conn.rollback()

finally:
	print("查询记录为:",cor.rowcount)

cor.close()
conn.close()
