
from pymysql import *
con=connect(user="root",password="123456",database="scores",port=3306,host="localhost",charset="utf8")
cor=con.cursor()
sql="""
    select * from scores
    """
try:

    cor.execute(sql)

    c=cor.fetchmany(4)
    print("序号 姓名 性别 英语 数学")
    for i in c:

	    print(i[0],i[1],i[2],i[3],i[4])

except Exception as e:

    print("异常为:",e)
    cor.rollback()

finally:
    print("查询记录为:",cor.rowcount)

cor.close()
cor.close()
