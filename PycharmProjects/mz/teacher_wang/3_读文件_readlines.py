#coding=utf-8

f = open("123.txt","r",encoding="utf8")

# con = f.readline()

# print(con)
# print(1,con,end="")
# con = f.readline()
# print(2,con,end="")
# con = f.readline()
# print(3,con,end="")
con = f.readlines()
# print(con)
n=1
# for i in con:
# 	print(n,i,end="")
# 	n+=1


print(con)
for i in con:
	print(n,i.replace("\n",""))
	n+=1
f.close()

