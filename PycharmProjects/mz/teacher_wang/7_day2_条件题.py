#coding=utf-8


"""
# 1.根据用户指定月份，打印该月份所属的季节。
# 春：3，4，5 夏: 6,7,8 秋 ：9，10，11 冬：1，2，12
yuefen=int(input("请输入月份"))
if 3<=yuefen<=5:
	print('春')
elif 6<=yuefen<=8:
	print('夏')
elif 9<=yuefen<=11:
	print('秋')
elif 1<=yuefen<=2 or yuefen==12 :
	print('冬')

else:
	print('输入有误')
"""
# month=int(input("请输入月份"))
# if month in (3,4,5):
# 	print("春季")
# elif month in(6,7,8):
# 	print("夏季")
# elif month in(9,10,11):
# 	print("秋季")
# elif month in (1,2,12):
# 	print("冬季")
# else:
# 	print("输入有误")
# 2.判断闰年?
# 用户输入年份year, 判断是否为闰年?  input()
# 提示year能被4整除但是不能被100整除 或者 year能被400整除, 那么就是闰年;
# year%4==0 and year%100!=0 year%400==0
year=int(input("请输入年份"))
if (year%4==0 and year%100!=0) or year%400==0:
	print("闰年")
else:
	print("不是闰年")





