# names = ['fentiao','fendai','fensi','apple']
# # 'I have fentiao, fendai, fensi and apple!'
# str1="'I have','.join(names[:3]),'and',names[3]+'!'"
# print('I have',",".join(names[:3]),'and',names[3]+'!')
# names = ["Lihua","Rain","Jack","Xiuxiu","Peiqi","Black"]
# names[3]="秀秀"
# print(names)
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# a={1:1,2:2,3:3}
# print("name的值是",dict['Name'])
# dict.keys()
# dict.values()

"""
1.数据类型：
2.可变和不可变数据类型：
可变数据类型：列表，字典
不可变数据类型元组，字符串，数值型：float，int,集合
"""

a="""
a=100
b=99.9
# %s:字符串   %f:浮点型  %d:整型
name = "老王"
age = 15
height = 188.8
# 格式化输出
print("我的姓名为%s,年龄为,%d身高为%.2f"%(name,age,height))
# print("我的姓名,年龄为,身高为",(name,age,height))
"""
# print(a,type(a))


# 字符串
b="hellopythyon"
# 切片：截取一部分
# print(b[:4])
# print(b[::-1])

# 元组
c = ("hello",)
print(c,type(c))

# 字典：

d = {
    "a":999,
    89:"jj",
    ("name"):"老王",
    "b":[1,2,3,4,5]
    # ["age",]:29,
    # "a":100
}

# update():
# 1.将新字典追加到就字典后面
# d.update({"age":100})
# print(d)

# 2.通过键增加或修改键值对
# key存在,增加键值对覆盖数据,key不存在
d.update(name="小李",cc=999)
print(d)

ee = [1,2,3,[55,66,77]]
print(ee[3][1])

