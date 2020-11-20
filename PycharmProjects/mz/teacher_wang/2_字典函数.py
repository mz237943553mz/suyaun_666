#coding=utf-8

d1 = {
	"name":"老王",
	"sex":99,
	("age",):18,   # 对的
	"name":"密码",  # 错的
	# ["pwd"]:5678,  # 错
	"user":["uss","add","python"]   # 对的
}
# print(d1)

# 1.通过语法，用key去修改值
# 键存在，表示修改
d1["user"]="那你"
print(d1)

# 键不存在,表示增加
d1["a"]=123456
print(d1)

# 字典的常用函数
# 1.所有的值values()
print(d1.values())

# 2.所有的键keys()
print(d1.keys())

# 3.输出所有的键值对[(键1,值1),(键2,值2)...]
print(d1.items())

# 4.get()===通过key去拿值
# print(d1["sex"])
# print(d1["bb"])
print(d1.get("name"))
print(d1.get("bb"))

# 5.setdefault():1.跟get()类似，可以通过键拿值    2.可以增加键值对
# 1.跟get()类似，可以通过键拿值
print(d1.setdefault("name"))

# 2.可以增加键值对
# d1.setdefault("性别")
d1.setdefault("性别","男")
print(d1)

# 3.update()
# 3.1把新字典增加到旧字典后面
d1.update({"nn":111,"kk":222})
print(d1)

# 3.2键存在,修改值     键不存在,增加值
d1.update(name=123456,height=189.9)
print(d1)

# 删除
# 1.删除末尾
d1.popitem()
print(d1)

# 2.根据键删除
d1.pop("性别")
print(d1)