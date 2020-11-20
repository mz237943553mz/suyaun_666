a=[5,2,43,123,45]
for i in range(len(a)):
    for m in range(i+1,len(a)):
        if (a[i]>a[m]):
            a[i],a[m]=a[m],a[i]
print(a)

