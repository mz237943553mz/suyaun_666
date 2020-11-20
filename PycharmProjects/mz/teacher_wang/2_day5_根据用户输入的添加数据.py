#coding=utf-8

# 1.导包
from pymysql import *

# 2.连接对象
conn = connect(user="root",password="root",port=3306,database="user",host="localhost",charset="utf8")

# 3.游标对象
cor = conn.cursor()

# 4.用户输入信息 id | name | sex  | math | english
new_name = input("请输入姓名")
new_english = input("请输入英语成绩")

result = (new_name,new_english)

# 5.写sql语句
sql = """
	insert into score(name,english) values (%s,%s)
"""

try:
	# 与数据库交互
	cor.execute(sql,result)

	# 提交
	conn.commit()

except Exception as error:
	print("异常为",error)
	# 回滚
	conn.rollback()

finally:
	print("成功插入",cor.rowcount,"记录")

cor.close()
conn.close()






