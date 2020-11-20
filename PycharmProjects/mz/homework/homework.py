# 1.编写一个名为collatz()的函数,它有一个名为number的参数
#    如果参数是偶数,那么collatz()就打印出number//2
#    如果number是奇数,collatz()就打印3*number+1

# def collatz(number):
#     if number%2==0:
#         print(number//2)
#     else:
#         print(3*number+1)
# collatz(5)

# 2.使用匿名函数对多个数字求和，形参给多少个都能进行求和。
sum1=lambda *args:sum(args)
print(sum1(1,2,3,4,5))


