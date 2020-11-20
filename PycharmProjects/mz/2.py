# for i in 1234:
#     print(i)
# s="dghey82q"
# print(dir(s))
# print("__iter__"in dir(s))
s="你好"
print("__iter__"in dir(s))
print("__next__"in dir(s))
ss=s.__iter__()
try:
    print(ss.__next__())
    print(ss.__next__())
    print(ss.__next__())
except StopIteration:
    pass


def func():
    a=1
    print("我是1")
    yield a
    b=2
    print("我是er")
    yield b
f=func()
print(next(f))

