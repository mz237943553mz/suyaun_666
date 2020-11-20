# a=[1,6,85,3,67]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if(a[j]>a[j+1]):
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)


list1=[11,4,32,5455,11,43]
a=set(list1)
b=[i for i in a]
print(b)
#
# def demo(args_f,*args):
#     print(args_f)
#     for i in args:
#         print(i)
# demo("a","b","c","d")
#
#
# class A():
#     def __new__(cls):
#         print("new方法的id",cls)
#         return super().__new__(cls)
#     def __init__(self):
#         print("我们在一起",self)
# A()
