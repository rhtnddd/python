# def sel_sort(a):
#     for i in range(0,len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i]>a[j]:
#                 a[i],a[j]=a[j],a[i]
#     return a
# d = [2, 4, 5, 1, 3]
# sel_sort(d)
# print(d)
def ins_sort(a):
    for i in range(0,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a
d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)