import math
import random
a="jnduewhndf"
print(a.startswith("d"))

a6 = ["hdwi",99,9.4,994,7,8,9]
print(a6[::4])

a=["dvsg","bnjs","djmsal"]
# print(a.split(" "))
print(isinstance(a,tuple))

print("*".join(a))

print("你好".center(10,"*"))

a="hello"
print("hello".count("l",3,5))
print(len(a))

print("abc".zfill(6))

print("{0}{1}{2}{3}".format("new","python","hello","word"))



print(math.ceil(12.55))
print(math.floor(12.55))

print(pow(2,3))

print("随机产生1-3z之间的整数",random.randint(1,3))
print(random.randrange(1,9))

print(random.random())

print(round(random.uniform(1,4),2))


print(random.choice(range(11,33)))

a=100
b=200
a,b=b,a
print(a,b)

print(100 or 0)