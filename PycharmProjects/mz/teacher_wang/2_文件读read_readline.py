#coding=utf-8

f = open("123.txt","r",encoding="utf8")

# read():默认读取全部     read(num):根据字节进行读取
cont = f.read()
print(cont)

# readline():读一行内容
c = f.readline()
print(c)
c = f.readline()
print(c)

f.close()


import re
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)


import re
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)


import re
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)