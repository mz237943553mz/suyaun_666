from pymysql import *

con=connect(user="root",password="123456",database="scores",port=3306,host="localhost",charset="utf8")

sor=con.cursor()

id=input("请输入修改的序号")
name=input("请输入修改的名字")

set=(name,id)

sql="""
    update scores set name=%s where id=%s 
"""
try:
    sor.execute(sql,set)
    con.commit()
except Exception as a:
     print("异常为",a)
     con.rollback()
finally:
    print("修改",sor.rowcount,"数据")
sor.close()
con.close()
