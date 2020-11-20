#coding=utf-8
import copy
"""
copy模块的copy()
若没有嵌套关系，与深拷贝一致，只会拷贝原来的；
若是嵌套关系，修改父对象不起作用，则修改子对象，就起作用。
"""

"""
# 不可变类型，深浅拷贝都是一样的
a = (1,2,3,4)
b = copy.copy(a)
print(a,b)
"""

a = {
	"a":100,
	"b":[11,22,33]
}

# 修改父元素,跟深拷贝一样，拷贝是原来的对象
# b = copy.copy(a)
# a["a"]="python"
# print(a,b)

# 修改子元素
b = copy.copy(a)
a["b"].append("math")
print(a,b)
