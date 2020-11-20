# copy模块的copy()
# 若没有嵌套关系，与深拷贝一致，只会拷贝原来的；
# 若是嵌套关系，修改父对象不起作用，则修改子对象，就起作用。
import copy
#不可变类型，深浅拷贝都一样
# a=(1,2,3,4)
# b=copy.copy(a)
# b=copy.deepcopy(a)
# print(a,b)
#可变内形
# a={
#     "b":100,
#     "c":[11,22,33]
# }
#修改父元素，跟深拷贝一样，拷贝原来的对象
# b=copy.copy(a)
# a["b"]="阿西吧"
# print(a,b)
#修改子元素
# b=copy.copy(a)
# a["c"].append("韩立")
# print(a,b)


import re

b = ["<html><h1>python</h1></html>","<html><h1>python</h1></html>"]
for i in b:
    ret=re.match(r"<([a-z]*)><([\w]*)>\w*</\2></\1>")
    print(ret.group(i))