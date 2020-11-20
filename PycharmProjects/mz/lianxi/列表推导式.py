
example2 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# a=[]
# for i in example2:
#    for n in i:
#        if n%2==0:
#      # a.append(n)
#          print(n*n)
#
#          print(a.append(n*n))

# a=[n*n for i in example2 for n in i if n%2==0]
# print(a)


import random
# b=[]
# for i in range(8):
#     b.append(str(random.randint(1,9)))
# print("".join(b))

b="".join([str(random.randint(1,9)) for i in range(8)])
print(b)

