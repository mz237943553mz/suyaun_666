#coding=utf-8

a = {
	"name":"老王",
	"age":10
}

print(a)

# 字典的常用函数/方法
# keys()
print(a.keys())
# 2.values():所有的值
print(a.values())
# 3.get():通过key去拿值
print(a.get("age"))

# 4.setdefault():\
print(a.setdefault("name"))
a.setdefault("sex","男")
print(a)

# 5.删除
# pop()
a.pop("sex")
print(a)
# popitem():删除末尾
a.popitem()
print(a)

# update():
# 1.1通过键增加/修改值=====键存在修改，键不存在增加
a.update(height=178.9,name="小子")
print(a)

# 1.2：把字典里的内容追加到旧字典后面
a.update({"a":999,"b":666})
print(a)

# items()====[(键1,值1),(键2,值2)]
# print(a.items())
b=a.items()
print(list(b))

# clear():清空

# del 删除====del 变量名["键"]
del a ["a"]
print(a)


# 通过语法结构去增加/修改值
a["ccc"]=222
print(a)

