# def sel_sort(a):
#     for i in range(0,len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i]>a[j]:
#                 a[i],a[j]=a[j],a[i]
#     return a
# d = [2, 4, 5, 1, 3]
# sel_sort(d)
# print(d)
# def ins_sort(a):
#     for i in range(0,len(a)):
#         key=a[i]
#         j=i-1
#         while j>=0 and a[j]>key:
#             a[j+1]=a[j]
#             j-=1
#         a[j+1]=key
#     return a
# d = [2, 4, 5, 1, 3]
# ins_sort(d)
# print(d)
def merge_sort(a):
    n=len(a)
    if n<=1:
        return a
    mid=n//2
    g1=a[:mid]
    g2=a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i=0
    j=0
    ai=0
    while i<len(g1) and j<len(g2):
        if g1[i]<g2[j]:
            a[ai]=g1[i]
            i+=1
            ai+=1
        else:
            a[ai]=g2[j]
            j+=1
            ai+=1
    while i<len(g1):
            a[ai]=g1[i]
            i+=1
            ai+=1
    while j<len(g2):
            a[ai]=g2[j]
            j+=1
            ai+=1

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)