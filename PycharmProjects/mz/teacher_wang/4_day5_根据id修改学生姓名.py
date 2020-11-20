#coding=utf-8

# 1.导包
from pymysql import *

# 2.连接对象
conn = connect(user="root",password="root",port=3306,database="user",host="localhost",charset="utf8")

# 3.游标对象
cor = conn.cursor()

id = input("请输入修改的序号")
name = input("请输入修改的姓名")

ret = (name,id)


sql = """
	update score set name=%s where id=%s
"""
try:
	cor.execute(sql,ret)
	conn.commit()
except Exception as e:
	print("异常为:",e)
	conn.rollback()
finally:
	print("修改",cor.rowcount,"记录")

cor.close()
conn.close()




