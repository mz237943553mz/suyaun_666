#coding=utf-8

# 定义一个列表
a = [1,2,3,4,"间接",1]

# 计算长度
print(len(a))

# 计数
print(a.count(1))

# 根据内容返回索引值
print(a.index(1,2,6))

# 增加
# 1.insert(索引值,内容)
# a.insert(0,"悟空")
# print(a)
a.insert(2,"达令")
print(a)

# 2.append():把内容增加到列表末尾====只能增加一个元素
a.append([999,888])
print(a)

# 3.extend():把新列表追加到旧列表后面
a.extend([123,234,456])
print(a)

# +:拼接

# 删除
# 1.pop():
# 1.1默认删除末尾
print(a.pop())
print(a)

# 1.2根据索引删除
a.pop(1)
print(a)

# 根据索引删除
del a[0]
print(a)

# remove():根据内容删除
a.remove(4)
print(a)

# clear():清空内容
a.clear()
print(a)


b = [1,2,354,65,8,67,876.7]
# 排序
# 1.升序
# b.sort()
# print(b)

# 2.降序
# b.sort(reverse=True)
# print(b)

# 3.反向输出
b.reverse()
print(b)

# 切片::-1
print(b[::-1])

# 最大值和最小值
print(max(b))
print(min(b))

old = input("请输入要拷贝的文件")
num=old.rfind(".")
print(num)