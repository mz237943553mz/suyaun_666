f =open("test.txt","r",encoding="utf8")

# lines=f.readlines()
# n=1
# for i in lines:
#     print(n,i,end="")
#     n+=1

lines=f.readline()
print(1,lines,end="")
print(2,lines,end="")
print(3,lines,end="")

f.close()