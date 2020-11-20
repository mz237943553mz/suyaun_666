# import os
# print(os.getcwd()+"\\txt")
# print(os.getcwd()[:-10])
# print(os.getcwd()[0:3])
import csv
# fw=open("test.csv","w",newline="")
# c=csv.writer(fw)
# dic={"selenium":"se","appium":"aa"}
# for key in dic:
#    c.writerow([key,dic[key]])
p='test.csv'
c=csv.reader(open(p,"r",encoding="utf-8"))
for cs in c:
    print(cs[1])