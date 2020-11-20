### 1、使用while循环和for循环,求1～100之间所有偶数之和(至少一种方法)

# sum=0
# for i in range(0,101,2):
#     sum+=i
# print(sum)
#
#
# sum=0
# counter=0
# while counter<=100:
#     sum+=counter
#     counter+=2
# print(sum)


### 2、 使用while循环和for循环输出1 2 3 4 5 6     8 9 10(至少一种方法)
# list1=(1,2,3,4,5,6,7,8,9,10)
# for i in list1:
#     if i==7:
#         continue
#     print(i,end=" ")

# counter=0
# while counter<=10:
#     counter += 1
#     if counter!=7:
#         print(counter,end=" ")
#         continue

### 3、使用for循环,求1-100的所有数的和
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

### 4、输出1到100之间的偶数:
# for i in range(0,101,2):
#     print(i,end=" ")

### 5、用户登陆（三次机会重试），用户名为:abc；密码为123

# for i in range(3):
#     admin=input("请输入用户名")
#     keywords=input("请输入密码")
#     if admin=="abc" and keywords=="123":
#         print("登陆成功")
#         break
#     elif admin!="abc" or keywords!="123":
#         print("用户名或者密码输入有误")
#         # continue
# else:
#     print("账户锁定稍后再试")

### 六、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
a=[1,2,3,4]
for i in a:
    for m in a[]:
        for n in range(i+2,5):
            b.append(i)
            b.append(m)
            b.append(n)
print(b)





### 七、输入三个整数x,y,z，请把这三个数由小到大输出。
# x=input("请输入一个整数")
# y=input("请输入二个整数")
# z=input("请输入三个整数")
# list=[]
# list.append(x)
# list.append(y)
# list.append(z)
# list.sort()
# print(list)

### 八、将一个列表的数据复制到另一个列表中。使用两种方法
##### 列表如下所示list1 = [11,22,33,44]
# list=["七夕","吕布","貂蝉","牛郎织女"]
# list1=[11,22,33,44]
# # list.extend(list1)
# # print(list)
# list.append(list1)
# print(list)


### 九、按相反的顺序输出列表的值。a = ['one', 'two', 'three']
# a = ['one', 'two', 'three']
# a.reverse()
# print(a)

### 十、有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，将小于66值保存至第二个key的值中。
# set=[11,22,33,44,55,66,77,88,99,90]
# dict0={}
# list1=[]
# list2=[]
# for i in set:
#     if i>66:
#          list1.append(i)
#     else:
#          list2.append(i)
# dict0.update(a=list1,b=list2)
# print(dict0)



