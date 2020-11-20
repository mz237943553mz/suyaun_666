#coding=utf-8

# 列表===list===可变数据类型
a = [1,2,3,4,"回我",99.7]
print(a[2:])
print(a[0])
# 通过索引/下标修改值
a[0]="八戒"
print(a)

# 列表的常用函数
# 一、增加
# 1.append():把内容增加到列表末尾
# a = [1,2,3,4,"回我",99.7]
a.append(["毛展","nn"])
print(a)

# 2.insert():根据索引/下标增加内容
a.insert(4,999)
print(a)

# 3.extend():把新列表的内容增加到旧列表的后面
a.extend([100,200,"啦"])
print(a)

# 删除
# 1.pop():默认删除的是最后一个。也可以根据索引删除内容
a.pop()
print(a)
# 根据索引删除内容
a.pop(1)
print(a)

# 根据索引删除2
del a [0]
print(a)

# 根据内容删除
a.remove(99.7)
print(a)

# count():统计元素出现的次数
print(a.count(100))

# 清空
a.clear()
print(a)

# 排序：
a2 = [12,4,7,98,56]
# 1.反向输出reverse()
a2.reverse()
print(a2)

# 2.升序sort()
a2.sort()
print(a2)

# 降序sort(reverse=True)
a2.sort(reverse=True)
print(a2)


