def Change1(list1):
    a = list1.index(0)
    list1.pop(a)
    list1.insert(0,0)
    print(list1)
Change1([1,2,6,0,8])
