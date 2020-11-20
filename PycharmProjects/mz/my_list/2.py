# a=45
# h=0.1
# name="张三"
# age=25
# print(a)
# print(h)
# print(name)
# print(age)
# a=b=c=d=1
# print(a,b,c,d)

# a,b,c,d=1,2,3,4
# print(a,b,c,d)


# name,age,score="刘德华",60,80
# print(name)
# print(age)
# print(score)
# print(type(name))
# name=1.5
# print(name)
# print(type(name))
# age=88
# print(age)
# print(type(age))
# score=98
# print(score)
# print(type(score))

var1=1
var2=2
var3=3
del var1,var2,var3
# print(var1,var2,var3)

a,b,c,d=1,"name",0.01,4+3j
# print(type(a),type(b),type(c),type(d))

a=5.5
i=isinstance(a,float)
print(i)
if i:
    print("a是float类型")
    print("-------")
else:
    print("a不是float类型")

b="张三"
j=isinstance(b,str)
print(j)
if j:
    print("b是str类型")
else:
    print("b是str类型")


# print(2**2)
str='123456'
print (str)
print(str[0],str[5])
print(str[0:-1])
print(str[2:4])
print(str[2:])
print(str * 5)
print(str+"ture\n"+"runboot")


print('abcde')
print('abc\nde')
print(r'abc\nde')


word='Python'
print(word)
print(word[0],word[4])
print(word[0],word[5])
print(word[-1])
print(word[-1],word[-5])
print(word[2 :])
print(word * 2)
print(word+'Holleword')

list=[123,'abc',0.87,'runboot']
tinylist=['def',567]
print(list)
print(tinylist)
print(list[0:2])
print(tinylist * 2)
print(list[0:])
print(list+tinylist)

tuple=(123,'abc',0.87,'runboot')
tinytuple=('def',567)
print(tuple)
print(tinytuple)
print(tuple[0:2])
print(tuple[2:])
print(tinytuple *2)
print(tuple+tinytuple)


tup=(1,2,3,4,5,6)
print(tup[0])
print(tup[2:5])
# tup[0]=11
# tup1=()
# tup2=(20)


student={'Tom','Jim','Rose','Jack','Tom'}
print(student)
if('Rose' in student):
    print('Rose在集合中')
else:
    print('Rose不在集合中')


a=set('abcdefg')
b=set('bcrow')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)


dict={}
dict['one']="你好，世界"
dict[2]="Helloword"
tinydict={'name':'runboot','code':1,'site':'www.runboot.com'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(tinydict.clear())


