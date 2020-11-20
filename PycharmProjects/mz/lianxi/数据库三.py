from pymysql import *
con=connect(user="root",password="123456",database="scores",port=3306,host="localhost",charset="utf8")
cor=con.cursor()
new_name=input("请输入姓名")
new_English=input("请输入英语")
result=(new_name,new_English)
sql="""
     insert into scores(name,english) values(%s,%s)
"""
try:
    cor.execute(sql,result)
    con.commit()
except Exception as a:
    print("异常为",a)
finally:
    print("成功插入",cor.rowcount,"记录")
cor.close()
con.close()

