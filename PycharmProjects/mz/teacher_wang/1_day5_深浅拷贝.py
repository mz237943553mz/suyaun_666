#coding=utf-8

import copy

"""
# 对象拷贝的是对象的引用地址
# 深浅拷贝，得导入模块,import copy
# 深拷贝：无论修改哪个元素，都是拷贝原来的对象====deepcopy()
"""

# 不可变：int  str  tuple set
a = 100
b = copy.deepcopy(a)
print(a,b)
# 不可变；int str tuple set {无序不重复}

# 可变：字典dir和列表list
a2 = {
	"a":99,
	"b":[1,2,3,4,5]
}

b2 = copy.deepcopy(a2)
# 修改父元素
# a2["a"]=(200,300)
# print(a2,b2)
a2["a"]=("hello","python")
print(a2,b2)

# 修改子元素
# a2["b"].append("你好")
# print(a2,b2)
a2["b"].append("朱竹青")
print(a2,b2)






