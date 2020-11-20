#coding=utf-8

file=input("请输入您要打开的文件")

f = open(file,"rb")

con = f.read(3)
print(con)

# 定位：tell()
position = f.tell()
print("当前位置为:",position)

# 从文件的起始位置偏移
# f.seek(5,0)
# 从当前位置偏移
# f.seek(-2,1)

# 2:文件结尾位置
f.seek(10,2)
position = f.tell()

print("偏移后的位置为:",position)



f.close()

