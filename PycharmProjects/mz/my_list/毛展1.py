# tuple=('abcd',786,2.23,'runoob',70.2)
# tinytuple=(123,'runoob')
# print(tuple)
# print(tuple[0])
# print(tuple[1:3])
# print(tuple[2:])
# print(tinytuple*2)
# print(tuple+tinytuple)
# name, age,score="刘德华",60,99.8
# print(name)
# print(age)
# print(score)
# print(type(name))
# print("------------")
# name=95.6
# print(name)
# print(type(name))
# str='Runoob'
# print(str)
# print (str[0:-1])
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str*2)
# print(str+"TEST")
# var1 = 'hello world'
# print ("已更新字符串：",var1[:6]+'runood')
# a="hello"
# b="python"
# print("a+b输出结果:",a+b)
# print("a*2输出结果：",a*2)
# print("a[1]输出结果：",a[1])
# print(":a[1]输出结果：",a[1:4])
# if("h" in a):
#     print("h在变量a中")
# else:
#     print("h不在变量a中")
# if("m" not in a):
#     print("m不在变量a中")
# else:
#      print ("m在变量a中")
# a=["a","b","c","d"]
# b='helloeutjgekjggh'
# print(b.capitalize())#将字符串的第一个字符转化为大写
# print(b.count("l"))#“1”在字符串里面出现的次数
# print(b.index("l"))#检查字符是否包含在字符串中，如果字符不在字符串中汇报异常
# print(b.find("g"))#检查字符是否包含在字符串中，如果字符不在字符串中会返回-1
# print(len(b))#返回字符串长度
# c='...'
# print(c.join(a))#将a列表中的所有字符连接成一个新的字符串
# print(b.split('e'))#以e为分隔符，截取字符串
# a="this is a book"
# print(a.startswith("this"))#判断该字符串是否以this开头
# print(a.endswith("apple"))#判断该字符串是否以apple结尾
# b=r"This IS a book\n"
# print(b.lower())#将字符串里的大写字符转换为小写字符
# print(b.upper())#将字符串里的大写字符转换为大写字符
# print(b.rstrip(r'\n'))#字符串的末尾有一个回车符，将其删除
# print(len(b))#打印一下b的长度
# var1="abcd"
# print(var1.upper())#将字符串“abcd”转换成大写
# print(var1.count("cd"))#“cd”在字符串中出现的次数
# var2="a,b,c,d"
# print(var1.split(","))#以,为分隔符，截取字符串
# string="Python is good"
# print(id(string))
# print(string.replace("Python","python",1))#把Python替换成python
# print(id(string))
# string="python修炼第一期.html"
# print(id(string))
# print(string)
# print(string.rstrip(".html"))#截取.html前面的字符串
# print(id(string))
# d="this is a book"
# print(d.replace("book","apple",1))#将字符串里面的book转换成apple
# dict={}
# dict['one']="1-你好，世界"
# dict[2]="2-hello world"
# tinydict={"name":"runoob","cood":"1","site":"www.runoob.com"}
# tinydict["name"]=123
# print(dict)
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(list(tinydict.values())[0])
# list=['abcd','hello boss',"中软","软通"]
# list.append('bonia')#在列表末尾添加新的对象
# print(list)
# print(list.count("abcd"))#统计元素“abcd”在列表中出现的次数
# list.extend((1,))#在列表的末尾追加一个序列
# print(list)
# print(list.index("中软"))#从列表中找出“中软”第一个匹配的索引位置
# list.insert(2,"python")#将“python"插入列表
# print(list)
# list.pop()#移除列表元素中的最后一个元素
# print(list)
# list.remove("中软")#移除列表中某个值的第一个匹配项
# print(list)
# list.reverse()#反向列表中的元素
# print(list)
# list1=[1,4,5,2]
# list1.sort()#对原列表进行排序，默认正序
# print(list1)
# list.clear()#清空列表
# print(list)
# a=list.copy()#复制列表
# print(a)
# names=['fentiao','fendai',"fensi",'apple']
# # names.insert(3,"and")
# A=['I have']
# A.extend(names)
# A.append("!")
# A.insert(2,",")
# A.insert(4,",")
# # print(' '.join(A))
# print("i have",",".join(names[0:3]),"and",names[3]+"!")
# names = ["Lihua","Rain","Jack","Xiuxiu","Peiqi","Black"]
# 1、把names列表中Xiuxiu的名字改成中文。
# 2、往names列表中Rain后面插入一个子列表["oldboy","oldgirl"]。
# 3、返回names列表中Peiqi的索引值（下标）。
# 4、创建新列表[1,2,3,4,2,5,6,2,]，合并到names列表中。
# 5、取出names列表中索引4-7的元素。
# 6、遍历（迭代）names列表，打印每个元素的值。
# names[3]="秀秀"
# print(names)
# names.insert(2,["oldboy","oldgirl"])
# print(names)
# print(names.index('Peiqi'))
# list2=[1,2,3,4,5,6,2]
# # names.insert(5,list2)#添加一个新的元素
# print(names+list2)#创建列表list2,合并到names中
# names=['Lihua', 'Rain', 'Jack', 'Xiuxiu', 'Peiqi', 'Black', 1, 2, 3, 4, 5, 6, 2]
# print(names[4:8])
# names = ["Lihua","Rain","Jack","Xiuxiu","Peiqi","Black"]
# for i in names:
#     print(i)

# 有字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}
# 1、遍历字典 dic 中所有的key
# 2、遍历字典 dic 中所有的value
# 3、循环遍历字典 dic 中所有的key和value
#    参考答案：
# 	dic = {"k1": "v1", "k2": "v2", "k3": "v3"}
#
# 	for k,v in dic.items():
#     		print(k,v)
# 4、添加一个键值对"k4","v4",输出添加后的字典 dic
# 5、删除字典 dic 中的键值对"k1","v1",并输出删除后的字典 dic
# 6、有字典 dic2 = {'k1':"v111",'a':"b"} 通过一行操作使 dic2 = {'k1':"v111",'k2':"v2",'k3':"v3",'k4': 'v4','a':"b"}
#
# 7、组合嵌套，实现功能，现有列表如下：
#
# list = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
# 　　（1）将列表中的‘tt’变成大写（2）将数字 3 变成字符串 ‘100’

# dic = {"k1": "v1", "k2": "v2", "k3": "v3"}
# # print(dic.keys())
# # print(dic.values())
# # print(dic.items())
# list2={"k4":"v4"}
# dic.update(list2)
# print(dic)
# dic.pop("k1")
# print(dic)
# dic2 = {'k1': "v111", 'a': "b"}
# dic3={'k2':"v2",'k3':"v3",'k4': 'v4'}
# dic2.update(dic3)
# print(dic2)
# list = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
# # list2=list[0][1][2]["k1"][0]="TT"
# # print(list)
# list2=list[0][1][2]["k1"][1]=100
# print(list)
#

# print()
# age=int(input("请输入你家狗狗的年龄")
# print("")
# if age <0:
#     print("你是在逗我吧")
# elif age ==1:
#     print("相当于4岁的人")
# elif age ==2:
#     print("相当于22岁的人")
# elif age >2:
#     human=22+(age-2)*5
#     print("对应人类年龄：",human)
#
# ###退出提示
# input('点击enter键退出')


# number=7
# guess=-1#临时的开发变量
# print("数字猜谜游戏")
# while guess != number:
#     guess=int(input("请输入你猜的数字"))#循环
#
#     if guess==number:
#         print("恭喜,你猜对了!")
#     elif guess<number:
#         print("猜的数字小了...")
#     elif guess>number:
#         print("猜的数字大了...")


# number1=int(input("请输入第一个数字"))
# number2=int(input("请输入第二个数字"))
# if number1<number2:
#     print("number1小于number2")
# else:
#     print("number大于number2")

# num=int(input("输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print("你输入的数字可以整除2和3")
#     else:
#         print("你输入的数字可以整除2，但不整除3")
# else:
#     if num%3==0:
#         print("你输入的数字可以整除3","但不能整除2")
#     else:
#         print("你输入的数字不能整除2和3")

# number1=int(input("请输入第一个数字"))
# number2=int(input("请输入第二个数字"))
# number3=int(input("请输入第三个数字"))
# if number1>number2:
#     if number2>number3:
#         print("num1>num2>num3")
#     elif number3>number1:
#          print("num3>num1>num2")
#     else:
#         print("num1>num3>num2")
# else:
#     if number1>number3:
#         print("num2>num1>num3")
#     elif number3>number2:
#         print("num3>num2>num1")
#     else:
#         print("num2>num3>num1")

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

# hight=float(input("请输入身高"))
# weight=float(input("请输入体重"))
# BMI=weight/(hight*hight)
# if BMI<18.5:
#     print("过轻")
# elif 18.5<BMI<25:
#     print("正常")
# elif 25<BMI<28:
#     print("过重")
# elif 28<BMI<32:
#     print("肥胖")
# elif 32<BMI:
#     print("严重肥胖")















