def sel_sort(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)