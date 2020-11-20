#coding=utf-8

a = [1,2,3,4,5]

# 一.增加
# 1.append():增加到末尾
a.append([99,22])
print(a)

# 2.insert():通过索引增加
a.insert(0,"密码")
print(a)

# 3.extend():新列表追加到旧列表后面
print(a.extend(["八戒","悟空"]))
print(a)

# 删除
# 1.pop():若没有给索引值的话，默认删除最后一个
print(a.pop())
print(a)

a.pop(3)
print(a)

# 2.remove():根据内容删除
a.remove("八戒")
print(a)

# 3.del 变量[索引值]
del a [0]
print(a)

# 4.clear():清空内容
# a.clear()
# print(a)


# index():根据内容返回索引值,若找不到则为报错
print(a.index(5))

# 排序
b = [233,54,7,98,3]
# 1.升序
b.sort()
print(b)

# 2.降序
b.sort(reverse=True)
print(b)

# 3.反向输出
# 3.1
b.reverse()
print(b)
print(b[::-1])

# count():计数
print(b.count(7))
# tuple()====把类型转换为列表
print(tuple(b))



# ================================================
# 元组：
c = (1,2,3,4,5)
print(max(c),min(c))
print(c.count(1))
print(len(c))
# list()=====把类型转换为元组
print(list(c))

