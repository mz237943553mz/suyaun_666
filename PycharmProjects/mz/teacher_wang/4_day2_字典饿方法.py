#coding=utf-8

# 字典：====dict
# 键：值
a = {
	"a":99,
	"b":131.5,
	"c":"朋友天弘"
}

print(a)

# 通过语法拿值99
print(a["a"])
# 若键不存在,会报错
# print(a["dd"])
# 字典的方法
# 1.输出所有的键key:keys()
print(a.keys())

# 2.输出所有的值value:values()
print(a.values())

# 3.输出所有的键值对:items()
print(a.items())

# 4.get():通过键获取值
print(a.get("b"))
# 若键不存在，会返回None
print(a.get("dd"))

# 5.setfefault():跟get类似，可以通过键拿值，并且还有增加键值
# 1.通过键获取值
print(a.setdefault("b"))
# 2.增加值
a.setdefault("dd")
print(a)

# 3.update():
# 3.1：增加/修改键值对
# 注意：键存在就是修改；键不存在增加
a.update(name="老王",a="看看")
print(a)

# 3.2把新字典增加到旧字典的后面
a.update({"sex":"男","age":"10"})
print(a)

# 4.删除
# 4.1pop():通过键(key)删除值
a.pop("name")
print(a)

# 5.popitem():默认删除最后一个
a.popitem()
print(a)