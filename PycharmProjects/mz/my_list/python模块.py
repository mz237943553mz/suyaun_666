# 使用python标准库中模块
# import sys
# print("cfnsjk")
# for i in sys.argv:
#     print(i)
# print("\n\npython 路径为：",sys.data,"\n")


# import 语句
# import new_python
# new_python.print_func("runoob")



# from...import语句
# from new_python import my_max
# print(my_max(125,987,8))

# from...import*语句
#
# from new_python import *
# print(my_min(67,3542,2345))

# info ="adress"
# def func_fatger(country):
#     def func_son(area):
#         city="shangai"
#         print(info+country+city+area)
#     city="beijing"
#     func_son("chaoyang")
# func_fatger("china")
#
#
# i=1
# def func2():
#     globals()["i"]=100
#     # i+=1
#     print(i)
#
# a=100
# globals()["a"]=200
# print(a)
#
# func2()

# def func3():
#     y=123
#     # del y
#     print(y)
# func3()
# 局部命名空间可以locals()BIF来访问
# def func(i,str):
#     x=13435
#     print(locals())
# func(1,"first")

def func(i,info):
    x=12345
    print(locals())
    locals() ["x"]=6889
    print("x=",x)
y=67489
func(1,"hdc")
globals() ["y"]=68
print("y=",y)
print(globals())




