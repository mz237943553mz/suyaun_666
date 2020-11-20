#coding=utf-8
class myerror(Exception):

    @classmethod
    def fun(cls):
        print("the input is of length ", len(a),"expecting at least 5")

    @classmethod
    def fun1(cls):
        print("pirnt success")

a = (input("请输入一个字符串："))
try:
    if (len(a) < 5):
        raise myerror.fun()
    else:
        raise myerror.fun1()

except Exception as e:
    print("异常为：",e)

