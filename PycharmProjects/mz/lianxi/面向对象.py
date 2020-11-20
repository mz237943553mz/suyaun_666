# 定义类：
# class 类名:
# #     属性列表
# #     列表方法

# class Car():
#
#     wheelNum=2
#     color="red"
#     __money=500000
    #构造器/初始化方法：创建对象，默认使用__init__初始化方法
    # def __init__(self,name,sex):
    #     print(name,sex)
        # print('初始化方法开启')

    # def getCarinfo(self):
    #     print("共有为：",self.color)
    #     print("私有为：",self.__money)
    #     print("车轮子个数：%d,颜色%s"%(self.wheelNum,self.color))
    #     return  self.color
    # def func(self,*args):
    #     print(args)


# Car()#实例化过程
#实例方法-能通过实例对象和实例化过程调用

# a=Car()
# a.getCarinfo()
# Car().getCarinfo()
#
# print(a.color)
# print("通过类名调用类属性",Car.color)
# print("实例对象调用类属性",a.color)

# b=Car(name="老王",sex="男")
# b.func(43,1,2,3,3454)

# class dog():
    #类属性
    # color="white"
    # def run(self):
    #实类属性
        # self.name="老王"
    #局部变量
        # sex="男"
        # print("性别为：",sex)
        # print("我的名字为%s,性别为%s"%(self.name,self.sex))
    # def run1(self):

        #访问上面方法的实例属性
        # self.name="老王"
        # print(self.name)
        #直接访问类属性
        # print(self.color)

# d1=dog()
# d1.run()
# d1.run1()

class Father():
    name="大漂亮"
    def __init__(self):
        print("初始化方法调用")

    def run(self):
        print("%s会跑"%self.name)

class Son(Father):
    def eat(self):
        self.run()

        Father.run(self)

        super().run()
s1=Son()
s1.eat()