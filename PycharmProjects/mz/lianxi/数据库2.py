# 导包
from pymysql import *
# 创建连接对象
conn = connect(user="root",password="123456",database="scores",port=3306,host="localhost",charset="utf8")
# 创建游标对象=====对数据库进行操作
youbiao = conn.cursor()
# 添加多行数据------- id name sex math english
sql=((0,"老王","女",89,78),(0,"辉哥","男",84,70))
try:
    # 增加信息
    youbiao.executemany("insert into scores values(%s,%s,%s,%s,%s)",sql)
    # 提交数据
    conn.commit()
except Exception as e:
    print("异常为:",e)
    conn.rollback()
finally:
    print("成功添加",youbiao.rowcount,"记录")
conn.close()
youbiao.close()


